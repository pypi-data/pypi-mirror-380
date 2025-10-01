"""FastAPI Safeguard - Security auditing framework for FastAPI applications.

This module provides a comprehensive security checking system for FastAPI applications,
detecting common vulnerabilities aligned with OWASP API Security Top 10.

The framework includes:
- Authentication and authorization enforcement
- Data exposure prevention
- Resource consumption protection
- Security misconfiguration detection
- Baseline management for accepted findings

Example:
    >>> from fastapi import FastAPI
    >>> from fastapi_safeguard import FastAPISafeguard
    >>>
    >>> app = FastAPI(lifespan=FastAPISafeguard.recommended().get_lifespan())

For more information, see the documentation at https://github.com/yourusername/fastapi-safeguard
"""
from __future__ import annotations

from fastapi import FastAPI, UploadFile
from fastapi.routing import APIRoute
from fastapi.security import (
    OAuth2PasswordBearer,
    OAuth2PasswordRequestForm,
    HTTPBasic,
    HTTPBearer,
    APIKeyHeader,
    APIKeyQuery,
    APIKeyCookie,
)
from contextlib import asynccontextmanager
from typing import (
    Any,
    Callable,
    Iterable,
    List,
    Optional,
    Sequence,
    Set,
    Type,
    Union,
    get_origin,
    Dict,
)
import sys
import os
import json
from abc import ABC, abstractmethod
from datetime import datetime, timezone
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.httpsredirect import HTTPSRedirectMiddleware
from starlette.middleware.trustedhost import TrustedHostMiddleware

# --------------------------------------------------------------------------------------
# Decorator markers
# --------------------------------------------------------------------------------------
_OPEN_ATTR = "_secure_open"          # Only bypasses dependency/auth check
_SKIP_ALL_ATTR = "_secure_skip_all"  # Bypasses every check


def open_route(func: Callable) -> Callable:
    """Mark a route as intentionally open (auth dependency check skipped, others enforced)."""
    setattr(func, _OPEN_ATTR, True)
    return func


def disable_security_checks(func: Callable) -> Callable:
    """Disable ALL security checks for this route."""
    setattr(func, _SKIP_ALL_ATTR, True)
    return func


def _is_open(route: APIRoute) -> bool:
    return bool(getattr(route.endpoint, _OPEN_ATTR, False))


def _skip_all(route: APIRoute) -> bool:
    return bool(getattr(route.endpoint, _SKIP_ALL_ATTR, False))


# --------------------------------------------------------------------------------------
# Shared constants & helpers
# --------------------------------------------------------------------------------------
DEFAULT_ALLOWED_UNSECURED: Set[str] = {"/openapi.json", "/docs", "/redoc"}
SUSPICIOUS_FIELD_PARTS = [
    "password", "passwd", "secret", "token", "api_key", "apikey",
    "key", "credential", "auth", "private",
]
SUSPICIOUS_QUERY_PARTS = SUSPICIOUS_FIELD_PARTS  # reuse same list
RATE_LIMIT_KEYWORDS = ["ratelimit", "throttle"]


def _route_dependencies(route: APIRoute) -> List[Callable]:
    return [dep.call for dep in route.dependant.dependencies]


# --------------------------------------------------------------------------------------
# Base classes
# --------------------------------------------------------------------------------------
class SecurityCheck(ABC):
    """Contract for a security check.

    Attributes:
        CATEGORY: Classification category for reporting (e.g., 'auth', 'schema').
        OWASP: List of related OWASP API Security Top 10 identifiers (e.g., ['API3']).

    Returns:
        check_route: None if the route passes the check, otherwise a string describing
                     the security issue.
    """
    CATEGORY = "general"
    OWASP: List[str] = []  # e.g. ["API3"]

    @abstractmethod
    def check_route(self, route: APIRoute) -> Optional[str]:  # pragma: no cover - interface
        ...


class RouteCheck(SecurityCheck):
    """Base for checks needing allowed_unsecured handling and skip_all support.

    Args:
        allowed_unsecured: Paths that should be excluded from checks
                          (defaults to /openapi.json, /docs, /redoc).
    """

    def __init__(self, allowed_unsecured: Optional[Sequence[str]] = None) -> None:
        self.allowed_unsecured: Set[str] = set(allowed_unsecured or DEFAULT_ALLOWED_UNSECURED)

    @abstractmethod
    def _analyze(self, route: APIRoute) -> Optional[str]:  # pragma: no cover - interface
        """Core check logic implemented by subclasses.

        Args:
            route: The FastAPI route to analyze.

        Returns:
            None if check passes, otherwise a finding description.
        """
        ...

    def check_route(self, route: APIRoute) -> Optional[str]:
        if _skip_all(route):
            return None
        if route.path in self.allowed_unsecured:
            return None
        return self._analyze(route)


class SingleRunMixin:
    """Mixin for checks that should run only once per application lifecycle.

    Correct usage: subclasses perform detection when not yet _done; subsequent invocations skip.
    """
    def __init__(self) -> None:
        self._done = False

    def should_run(self) -> bool:
        if self._done:
            return False
        self._done = True
        return True


# --------------------------------------------------------------------------------------
# Concrete Checks
# --------------------------------------------------------------------------------------
class DependencySecurityCheck(SecurityCheck):
    # OWASP: API2 (Broken Authentication), API5 (Broken Function Level Authorization)
    CATEGORY = "auth"
    OWASP = ["API2", "API5"]

    """Ensure at least one accepted auth/security dependency is present.

    open_route decorator: bypasses this check only.
    disable_security_checks decorator: bypasses all checks (handled globally by _skip_all).
    """

    DEFAULT_SECURITY_DEPENDENCIES: Set[Type] = {
        OAuth2PasswordBearer,
        OAuth2PasswordRequestForm,
        HTTPBasic,
        HTTPBearer,
        APIKeyHeader,
        APIKeyQuery,
        APIKeyCookie,
    }

    def __init__(
        self,
        allowed_unsecured: Optional[Sequence[str]] = None,
        extra_dependencies: Optional[Union[List[Any], Set[Any]]] = None,
    ) -> None:
        self.allowed_unsecured = set(allowed_unsecured or DEFAULT_ALLOWED_UNSECURED)
        raw = set(self.DEFAULT_SECURITY_DEPENDENCIES)
        if extra_dependencies:
            raw |= set(extra_dependencies)
        self.accepted_type_dependencies: Set[Type] = {d for d in raw if isinstance(d, type)}
        self.accepted_callable_dependencies: Set[Callable] = {d for d in raw if not isinstance(d, type)}

    def _has_accepted_dependency(self, deps: List[Callable]) -> bool:
        """Check if any dependency matches accepted security dependencies.

        Args:
            deps: List of dependency callables from route.

        Returns:
            True if at least one accepted dependency is found.
        """
        types_tuple = tuple(self.accepted_type_dependencies)
        for dep in deps:
            if types_tuple and isinstance(dep, types_tuple):
                return True
            if dep in self.accepted_callable_dependencies:
                return True
        return False

    def check_route(self, route: APIRoute) -> Optional[str]:
        if _skip_all(route):
            return None
        if _is_open(route):  # explicit open route
            return None
        if route.path in self.allowed_unsecured:
            return None
        deps = _route_dependencies(route)
        if self._has_accepted_dependency(deps):
            return None
        return f"{','.join(route.methods)} {route.path} has no accepted security dependency"


class ResponseModelSecurityCheck(RouteCheck):
    # OWASP: API3 (Broken Object Property Level Authorization / Excessive Data Exposure)
    CATEGORY = "schema"
    OWASP = ["API3"]
    def __init__(self, enforce_methods: Optional[Iterable[str]] = None, allowed_unsecured: Optional[Sequence[str]] = None) -> None:
        super().__init__(allowed_unsecured)
        self.methods = {m.upper() for m in (enforce_methods or ["POST", "PUT", "PATCH", "DELETE"])}

    def _analyze(self, route: APIRoute) -> Optional[str]:
        if not (self.methods & route.methods):
            return None
        if route.response_model is None:
            return f"{','.join(route.methods)} {route.path} missing response_model for unsafe method(s)"
        return None


class UnsecuredAllowedMethodsCheck(RouteCheck):
    # OWASP: API5 (Broken Function Level Authorization)
    CATEGORY = "auth"
    OWASP = ["API5"]
    def __init__(self, allowed_unsecured: Optional[Sequence[str]] = None, safe_methods: Optional[Iterable[str]] = None) -> None:
        # Here allowed_unsecured means explicit open paths list.
        super().__init__(allowed_unsecured)
        self.safe = {m.upper() for m in (safe_methods or ["GET", "HEAD", "OPTIONS"])}

    def _analyze(self, route: APIRoute) -> Optional[str]:
        """Check if allowed unsecured paths expose unsafe methods.

        This check has inverted logic: it ONLY checks routes in allowed_unsecured.
        """
        # This will never be called by RouteCheck.check_route() for paths in allowed_unsecured
        # So we override check_route() instead
        return None

    def check_route(self, route: APIRoute) -> Optional[str]:
        """Override to invert the allowed_unsecured logic."""
        if _skip_all(route):
            return None
        # Only check routes that ARE in allowed_unsecured
        if route.path not in self.allowed_unsecured:
            return None
        unsafe = [m for m in route.methods if m not in self.safe]
        if unsafe:
            return f"{','.join(route.methods)} {route.path} exposes unsafe method(s) without security (allowed_unsecured)"
        return None


class CORSMisconfigurationCheck(SingleRunMixin, SecurityCheck):
    # OWASP: API8 (Security Misconfiguration)
    CATEGORY = "config"
    OWASP = ["API8"]
    def __init__(self, allow_wildcards: bool = False) -> None:
        super().__init__()
        self.allow_wildcards = allow_wildcards

    # Route-level invocation now no-op; detection done in app_check
    def check_route(self, route: APIRoute) -> Optional[str]:
        return None

    def app_check(self, app: FastAPI) -> Optional[str]:
        if not self.should_run():  # single-run guard
            return None
        issues: List[str] = []

        def is_wild(v: Any) -> bool:
            return v == "*" or v == ["*"]

        for mw in getattr(app, "user_middleware", []):
            if mw.cls is CORSMiddleware:
                opt = getattr(mw, "options", None) or getattr(mw, "kwargs", {}) or {}
                origins = opt.get("allow_origins")
                methods = opt.get("allow_methods")
                headers = opt.get("allow_headers")
                credentials = opt.get("allow_credentials")
                if not self.allow_wildcards:
                    if is_wild(origins):
                        issues.append("allow_origins='*'")
                    if is_wild(methods):
                        issues.append("allow_methods='*'")
                    if is_wild(headers):
                        issues.append("allow_headers='*'")
                if credentials and is_wild(origins):
                    issues.append("credentials allowed with wildcard origins")
        if issues:
            return "CORS misconfiguration: " + ", ".join(issues)
        return None


class DebugModeCheck(SingleRunMixin, SecurityCheck):
    # OWASP: API8 (Security Misconfiguration)
    CATEGORY = "config"
    OWASP = ["API8"]
    def __init__(self) -> None:
        super().__init__()

    def check_route(self, route: APIRoute) -> Optional[str]:
        return None

    def app_check(self, app: FastAPI) -> Optional[str]:
        if not self.should_run():
            return None
        if getattr(app, "debug", False):
            return "Application running in debug mode"
        return None


class BodyModelEnforcementCheck(RouteCheck):
    # OWASP: API6 (Mass Assignment), API3 (Excessive Data Exposure)
    CATEGORY = "schema"
    OWASP = ["API6", "API3"]
    def __init__(self, enforce_methods: Optional[Iterable[str]] = None, allowed_unsecured: Optional[Sequence[str]] = None) -> None:
        super().__init__(allowed_unsecured)
        self.methods = {m.upper() for m in (enforce_methods or ["POST", "PUT", "PATCH"])}

    def _analyze(self, route: APIRoute) -> Optional[str]:
        if not (self.methods & route.methods):
            return None
        raw_names: List[str] = []
        for p in route.dependant.body_params:  # type: ignore[attr-defined]
            t = getattr(p, "type_", None)
            if t in (None, UploadFile, bytes):
                continue
            origin = getattr(t, "__origin__", None)
            if t in (dict, list, Any) or origin in (dict, list):
                raw_names.append(p.name)
        if raw_names:
            return f"{','.join(route.methods)} {route.path} uses non-model raw body param(s): {','.join(raw_names)}"
        return None


class PaginationEnforcementCheck(RouteCheck):
    # OWASP: API4 (Unrestricted Resource Consumption)
    CATEGORY = "performance"
    OWASP = ["API4"]
    def __init__(self, pagination_param_names: Optional[Iterable[str]] = None, allowed_unsecured: Optional[Sequence[str]] = None) -> None:
        super().__init__(allowed_unsecured)
        self.pagination_params = set(pagination_param_names or ["limit", "offset", "page", "page_size"])

    def _analyze(self, route: APIRoute) -> Optional[str]:
        if "GET" not in route.methods:
            return None
        ann = route.endpoint.__annotations__.get("return")
        if ann is None:
            return None
        origin = get_origin(ann)
        try:
            is_list = origin in (list, List) or ann in (list, List)
        except TypeError:
            is_list = False
        if not is_list:
            return None
        query_names = {p.name for p in route.dependant.query_params}
        if self.pagination_params.isdisjoint(query_names):
            return f"GET {route.path} returns a collection without pagination params ({'/'.join(sorted(self.pagination_params))})"
        return None


class WildcardPathCheck(RouteCheck):
    # OWASP: API5 (Broken Function Level Authorization), API3 (Excessive Data Exposure)
    CATEGORY = "routing"
    OWASP = ["API5", "API3"]
    def _analyze(self, route: APIRoute) -> Optional[str]:
        if ":path}" in route.path:
            return f"{','.join(route.methods)} {route.path} uses broad wildcard path parameter (:path)"
        return None


class SensitiveFieldExposureCheck(RouteCheck):
    # OWASP: API3 (Excessive Data Exposure)
    CATEGORY = "data_exposure"
    OWASP = ["API3"]
    def _analyze(self, route: APIRoute) -> Optional[str]:
        model = route.response_model
        if not (model and isinstance(model, type)):
            return None
        try:
            if not issubclass(model, BaseModel):  # type: ignore[arg-type]
                return None
        except TypeError:
            return None
        field_names = (
            list(getattr(model, "model_fields", {}).keys())
            if hasattr(model, "model_fields")
            else list(getattr(model, "__fields__", {}).keys())
        )
        # Optimize: single pass with combined lower() and check
        hits = {
            name_lower
            for name in field_names
            if (name_lower := name.lower())
            and any(sub in name_lower for sub in SUSPICIOUS_FIELD_PARTS)
        }
        if hits:
            return f"{','.join(route.methods)} {route.path} response_model exposes potentially sensitive fields: {','.join(sorted(hits))}"
        return None


class ReturnTypeAnnotationCheck(RouteCheck):
    # OWASP: API3 (Excessive Data Exposure)
    CATEGORY = "schema"
    OWASP = ["API3"]
    def _analyze(self, route: APIRoute) -> Optional[str]:
        if route.response_model is not None:
            return None
        ann = route.endpoint.__annotations__.get("return") if hasattr(route.endpoint, "__annotations__") else None
        if ann is None:
            return f"{','.join(route.methods)} {route.path} has neither response_model nor return type annotation"
        return None


class SensitiveQueryParamCheck(RouteCheck):
    # OWASP: API3 (Excessive Data Exposure)
    CATEGORY = "data_exposure"
    OWASP = ["API3"]
    def __init__(self, allowed_unsecured: Optional[Sequence[str]] = None, allowlist: Optional[Iterable[str]] = None) -> None:
        super().__init__(allowed_unsecured)
        self.allowlist = {a.lower() for a in (allowlist or [])}

    def _analyze(self, route: APIRoute) -> Optional[str]:
        hits = []
        for qp in route.dependant.query_params:
            name_l = qp.name.lower()
            if name_l in self.allowlist:
                continue
            if any(sub in name_l for sub in SUSPICIOUS_QUERY_PARTS):
                hits.append(qp.name)
        if hits:
            return f"{','.join(route.methods)} {route.path} exposes potentially sensitive data via query params: {','.join(sorted(set(hits)))}"
        return None


class HTTPSRedirectMiddlewareCheck(SingleRunMixin, SecurityCheck):
    # OWASP: API8 (Security Misconfiguration)
    CATEGORY = "config"
    OWASP = ["API8"]
    def __init__(self) -> None:
        super().__init__()

    def check_route(self, route: APIRoute) -> Optional[str]:
        return None

    def app_check(self, app: FastAPI) -> Optional[str]:
        if not self.should_run():
            return None
        for mw in getattr(app, "user_middleware", []):
            if mw.cls is HTTPSRedirectMiddleware:
                return None
        return "HTTPS redirect middleware not configured (consider HTTPSRedirectMiddleware or upstream TLS enforcement)"


class TrustedHostMiddlewareCheck(SingleRunMixin, SecurityCheck):
    # OWASP: API8 (Security Misconfiguration)
    CATEGORY = "config"
    OWASP = ["API8"]
    def __init__(self) -> None:
        super().__init__()

    def check_route(self, route: APIRoute) -> Optional[str]:
        return None

    def app_check(self, app: FastAPI) -> Optional[str]:
        if not self.should_run():
            return None
        for mw in getattr(app, "user_middleware", []):
            if mw.cls is TrustedHostMiddleware:
                return None
        return "TrustedHostMiddleware not configured (consider restricting allowed hosts)"


class RateLimitingPresenceCheck(SingleRunMixin, SecurityCheck):
    # OWASP: API4 (Unrestricted Resource Consumption)
    CATEGORY = "performance"
    OWASP = ["API4"]
    def __init__(self) -> None:
        super().__init__()

    def check_route(self, route: APIRoute) -> Optional[str]:
        return None

    def app_check(self, app: FastAPI) -> Optional[str]:
        if not self.should_run():
            return None
        for mw in getattr(app, "user_middleware", []):
            name = mw.cls.__name__.lower()
            full = str(mw.cls).lower()
            if any(k in name or k in full for k in RATE_LIMIT_KEYWORDS):
                return None
        return "No apparent rate limiting middleware detected (consider adding to mitigate abuse)"


# ---------------- Additional (non-OWASP-top10-specific) Checks ----------------
class DangerousMethodExposureCheck(RouteCheck):
    """Flag usage of rarely needed and potentially unsafe HTTP methods (TRACE/CONNECT).
    These methods are almost never required in public APIs and can aid in fingerprinting or tunneling.
    """
    CATEGORY = "http_methods"
    OWASP: List[str] = []  # informational
    DANGEROUS = {"TRACE", "CONNECT"}

    def _analyze(self, route: APIRoute) -> Optional[str]:
        exposed = self.DANGEROUS & route.methods
        if exposed:
            return f"{','.join(route.methods)} {route.path} exposes dangerous HTTP method(s): {','.join(sorted(exposed))}"
        return None


class SSRFParameterCheck(RouteCheck):
    """Detect query parameters that commonly indicate potential SSRF vectors (e.g. 'url', 'uri', 'target').
    Purely heuristic – encourages explicit allowlists or validation for remote resource fetches.
    """
    CATEGORY = "ssrf"
    OWASP: List[str] = []  # informational
    RISKY = {"url", "uri", "target", "endpoint", "callback"}

    def __init__(self, allowed_unsecured: Optional[Sequence[str]] = None, allowlist: Optional[Iterable[str]] = None) -> None:
        super().__init__(allowed_unsecured)
        self.allowlist = {a.lower() for a in (allowlist or [])}

    def _analyze(self, route: APIRoute) -> Optional[str]:
        hits: List[str] = []
        for qp in route.dependant.query_params:
            name_l = qp.name.lower()
            if name_l in self.allowlist:
                continue
            if name_l in self.RISKY:
                hits.append(qp.name)
        if hits:
            return f"{','.join(route.methods)} {route.path} contains potential SSRF parameter(s): {','.join(sorted(set(hits)))}"
        return None


class AdminRouteOpenCheck(RouteCheck):
    """Flag admin-related routes that appear to lack any dependency-based security.
    Heuristic: path contains '/admin' and dependant.dependencies is empty.
    """
    CATEGORY = "auth"
    OWASP: List[str] = []  # informational

    def _analyze(self, route: APIRoute) -> Optional[str]:
        if "/admin" in route.path.lower():
            if not getattr(route.dependant, "dependencies", []):
                return f"{','.join(route.methods)} {route.path} admin route without explicit security dependencies"
        return None

# ---------------- Recommended preset utilities ----------------

def recommended_checks(
    *,
    allowed_unsecured: Optional[Sequence[str]] = None,
    extra_dependencies: Optional[Union[List[Any], Set[Any]]] = None,
) -> List[SecurityCheck]:
    """Return a curated set of checks considered a strong default.

    Core checks (always included):
    - Authentication & authorization enforcement
    - Response model & body validation (prevents data leaks & mass assignment)
    - Sensitive data exposure detection
    - CORS & debug mode misconfiguration

    include_heuristics controls inclusion of softer / more subjective rules:
    - Infrastructure-level checks (HTTPS redirect, trusted host, rate limiting)
    - Heuristic-based checks (dangerous methods, SSRF params, admin routes, wildcard paths)
    - Type annotation enforcement
    """
    allowed_unsecured = allowed_unsecured or DEFAULT_ALLOWED_UNSECURED

    # High-value core checks: critical security issues with low false positives
    core: List[SecurityCheck] = [
        # Authentication & Authorization (OWASP API2, API5)
        DependencySecurityCheck(allowed_unsecured=allowed_unsecured, extra_dependencies=extra_dependencies),
        UnsecuredAllowedMethodsCheck(allowed_unsecured=allowed_unsecured),

        # Data Exposure Prevention (OWASP API3, API6)
        ResponseModelSecurityCheck(allowed_unsecured=allowed_unsecured),
        BodyModelEnforcementCheck(allowed_unsecured=allowed_unsecured),
        SensitiveFieldExposureCheck(allowed_unsecured=allowed_unsecured),
        SensitiveQueryParamCheck(allowed_unsecured=allowed_unsecured),

        # Resource Consumption (OWASP API4)
        PaginationEnforcementCheck(allowed_unsecured=allowed_unsecured),

        # Configuration Issues (OWASP API8)
        CORSMisconfigurationCheck(),
        DebugModeCheck(),
    ]
    return core


# --------------------------------------------------------------------------------------
# Baseline (lock file) orchestration plugin
# --------------------------------------------------------------------------------------
class FastAPISafeguard:
    """Run registered security checks and manage a baseline (accepted findings) file.

    Baseline logic:
      * If baseline exists, findings listed there are accepted.
      * Startup fails only on NEW findings unless update_baseline / SECURITY_BASELINE_UPDATE=1.
      * With update flag, current findings overwrite the baseline.
      * Resolved (previously accepted but now gone) findings can be pruned with update.

    Added: grouped category summary of findings (total/new/accepted per category).
    """

    def __init__(
        self,
        checks: Optional[List[SecurityCheck]] = None,
        baseline_path: Optional[str] = None,
        update_baseline: Optional[bool] = None,
    ) -> None:
        self.checks: List[SecurityCheck] = checks or [DependencySecurityCheck()]
        raw_path = (
            baseline_path
            or os.environ.get("SECURITY_BASELINE_PATH")
            or "security_baseline.json"
        )
        # Validate baseline path to prevent path traversal attacks
        self.baseline_path = self._validate_baseline_path(raw_path)
        if update_baseline is None:
            self.update_baseline = os.environ.get("SECURITY_BASELINE_UPDATE") == "1"
        else:
            self.update_baseline = update_baseline

    def _validate_baseline_path(self, path: str) -> str:
        """Validate and normalize baseline file path for security.

        Args:
            path: Raw path from user input or environment.

        Returns:
            Validated absolute path.

        Raises:
            ValueError: If path attempts traversal outside working directory.
        """
        abs_path = os.path.abspath(path)
        cwd = os.getcwd()
        # Ensure the path is within the current working directory or is absolute
        # This prevents malicious paths like "../../etc/passwd"
        if not abs_path.startswith(cwd):
            # Allow absolute paths outside cwd only if explicitly provided
            if not os.path.isabs(path):
                raise ValueError(
                    f"Baseline path '{path}' resolves outside working directory. "
                    f"Use absolute path if intentional."
                )
        return abs_path

    @classmethod
    def recommended(
        cls,
        *,
        allowed_unsecured: Optional[Sequence[str]] = None,
        extra_dependencies: Optional[Union[List[Any], Set[Any]]] = None,
        baseline_path: Optional[str] = None,
        update_baseline: Optional[bool] = None,
    ) -> "FastAPISafeguard":
        """Instantiate plugin with the recommended preset of checks.
        """
        checks = recommended_checks(
            allowed_unsecured=allowed_unsecured,
            extra_dependencies=extra_dependencies,
        )
        return cls(
            checks=checks,
            baseline_path=baseline_path,
            update_baseline=update_baseline,
        )

    # -------- Baseline helpers --------
    def _load_baseline(self) -> Set[str]:
        if not (self.baseline_path and os.path.exists(self.baseline_path)):
            return set()
        try:
            with open(self.baseline_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            accepted = data.get("accepted_findings")
            if isinstance(accepted, list):
                return set(accepted)
        except (OSError, json.JSONDecodeError, ValueError, KeyError) as exc:  # pragma: no cover - defensive
            print(f"⚠️  Could not parse baseline file '{self.baseline_path}': {exc}")
        return set()

    def _write_baseline(self, findings: Sequence[str]) -> None:
        if not self.baseline_path:
            return
        payload = {
            "schema_version": 1,
            "generated_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
            "accepted_findings": sorted(set(findings)),
            "checks_count": len(self.checks),
        }
        try:
            with open(self.baseline_path, "w", encoding="utf-8") as f:
                json.dump(payload, f, indent=2)
            # Set secure permissions: owner read/write only
            try:
                os.chmod(self.baseline_path, 0o600)
            except OSError:
                pass  # Best effort; may fail on Windows or restricted environments
            print(f"💾 Updated security baseline written to {self.baseline_path}")
        except (OSError, TypeError, ValueError) as exc:  # pragma: no cover - defensive
            print(f"⚠️  Failed to write baseline file '{self.baseline_path}': {exc}")

    # -------- Summary helpers --------
    def _print_category_summary(
        self,
        category_map: Dict[str, List[str]],
        new_findings: Set[str],
        category_owasp: Dict[str, Set[str]],
    ) -> None:
        if not category_map:
            print("ℹ️  No findings to summarize by category.")
            return
        print("\nCategory Summary:")
        header = f"{'Category':<15} {'Total':>5} {'New':>5} {'Accepted':>9}  {'OWASP':<25}"
        print(header)
        print("-" * len(header))
        for cat in sorted(category_map.keys()):
            findings = category_map[cat]
            total = len(findings)
            new_cnt = sum(1 for f in findings if f in new_findings)
            accepted_cnt = total - new_cnt
            owasp_list = sorted(category_owasp.get(cat, []))
            owasp_str = "/".join(owasp_list)[:25]
            print(f"{cat:<15} {total:>5} {new_cnt:>5} {accepted_cnt:>9}  {owasp_str:<25}")
        print()

    # -------- Lifespan --------
    def run_checks(self, app: FastAPI) -> None:
        """Run all security checks on the FastAPI app and exit on failures.

        This method can be called from within a custom lifespan context manager
        for apps that already have their own lifespan logic.

        Args:
            app: The FastAPI application instance to check.

        Raises:
            SystemExit: If new security findings are detected and not in baseline.
        """
        findings: List[str] = []
        category_map: Dict[str, List[str]] = {}
        category_owasp: Dict[str, Set[str]] = {}
        # App-level checks
        for check in self.checks:
            app_check_fn = getattr(check, "app_check", None)
            if callable(app_check_fn):
                res = app_check_fn(app)
                if res:
                    findings.append(res)
                    cat = getattr(check, 'CATEGORY', 'general')
                    category_map.setdefault(cat, []).append(res)
                    for code in getattr(check, 'OWASP', []):
                        category_owasp.setdefault(cat, set()).add(code)
        route_count = 0
        for route in app.routes:
            if isinstance(route, APIRoute):
                route_count += 1
                for check in self.checks:
                    res = check.check_route(route)
                    if res:
                        findings.append(res)
                        cat = getattr(check, 'CATEGORY', 'general')
                        category_map.setdefault(cat, []).append(res)
                        for code in getattr(check, 'OWASP', []):
                            category_owasp.setdefault(cat, set()).add(code)

        baseline = self._load_baseline()
        current = set(findings)
        new = current - baseline
        resolved = baseline - current if baseline else set()

        # Always print summary (it reflects current findings regardless of baseline state)
        if findings:
            self._print_category_summary(category_map, new, category_owasp)

        if findings:
            if new:
                if self.update_baseline:
                    self._write_baseline(findings)
                    print("✅ Security checks passed with new findings accepted into baseline.")
                else:
                    print("❌ Security check failed: new findings detected (not in baseline):")
                    for f in sorted(new):
                        print(f"  + {f}")
                    if baseline:
                        accepted_only = current & baseline
                        if accepted_only:
                            print("ℹ️  Previously accepted findings (baseline):")
                            for f in sorted(accepted_only):
                                print(f"    = {f}")
                    print("\nTo accept current findings run with SECURITY_BASELINE_UPDATE=1 or set update_baseline=True.")
                    sys.exit(1)
            else:
                if self.update_baseline and resolved:
                    self._write_baseline(findings)
                    print("✅ All security findings match baseline (baseline refreshed removing resolved items).")
                else:
                    print(f"✅ All security findings match accepted baseline ({len(findings)} accepted).")
                    if resolved:
                        print(f"ℹ️  {len(resolved)} previously accepted finding(s) resolved; run with SECURITY_BASELINE_UPDATE=1 to prune baseline.")
        else:
            if baseline:
                if self.update_baseline:
                    self._write_baseline([])
                    print("✅ No security findings. Baseline cleared (was non-empty).")
                else:
                    print("✅ No security findings. (Baseline exists – run with SECURITY_BASELINE_UPDATE=1 to clear.)")
            else:
                print(f"✅ All security checks passed (0 findings, {route_count} routes, {len(self.checks)} checks).")

    def get_lifespan(self):
        """Return an async context manager for FastAPI lifespan integration.

        Usage:
            app = FastAPI(lifespan=safeguard.get_lifespan())

        Returns:
            An async context manager that runs security checks on startup.
        """
        @asynccontextmanager
        async def _lifespan(app: FastAPI):
            self.run_checks(app)
            yield

        return _lifespan


# --------------------------------------------------------------------------------------
# Public exports
# --------------------------------------------------------------------------------------
__all__ = [
    # Decorators
    "open_route",
    "disable_security_checks",
    # Core types
    "FastAPISafeguard",
    "SecurityCheck",
    # Checks
    "DependencySecurityCheck",
    "ResponseModelSecurityCheck",
    "UnsecuredAllowedMethodsCheck",
    "CORSMisconfigurationCheck",
    "DebugModeCheck",
    "BodyModelEnforcementCheck",
    "PaginationEnforcementCheck",
    "WildcardPathCheck",
    "SensitiveFieldExposureCheck",
    "ReturnTypeAnnotationCheck",
    "SensitiveQueryParamCheck",
    "HTTPSRedirectMiddlewareCheck",
    "TrustedHostMiddlewareCheck",
    "RateLimitingPresenceCheck",
    "DangerousMethodExposureCheck",
    "SSRFParameterCheck",
    "AdminRouteOpenCheck",
    # Preset helpers
    "recommended_checks",
]
