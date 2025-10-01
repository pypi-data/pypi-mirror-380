from __future__ import annotations
import json
import logging
import re
from typing import List, Tuple
from django.conf import settings
from django.utils.deprecation import MiddlewareMixin

# Logger
logger = logging.getLogger("xssdefense")
logger.setLevel(logging.INFO)
if not logger.handlers:
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
    logger.addHandler(handler)

# Intentar usar bleach si está disponible
try:
    import bleach

    _BLEACH_AVAILABLE = True
except Exception:
    _BLEACH_AVAILABLE = False

# Patrones de detección XSS
XSS_PATTERNS: List[Tuple[re.Pattern, str]] = [
    (re.compile(r"<\s*script\b", re.I), "Etiqueta <script>"),
    (re.compile(r"on\w+\s*=", re.I), "Atributo evento (on*)"),
    (re.compile(r"javascript:\s*", re.I), "URI javascript:"),
    (re.compile(r"<\s*iframe\b", re.I), "Etiqueta <iframe>"),
    (re.compile(r"<\s*embed\b", re.I), "Etiqueta <embed>"),
]


# Funciones auxiliares
def detect_xss_text(text: str) -> Tuple[bool, List[str]]:
    matches: List[str] = []
    if not text:
        return False, matches
    for patt, message in XSS_PATTERNS:
        if patt.search(text):
            matches.append(message)
    return len(matches) > 0, matches


def sanitize_input_basic(text: str) -> str:
    if text is None:
        return text
    if _BLEACH_AVAILABLE:
        return bleach.clean(text, tags=[], attributes={}, protocols=[], strip=True)
    replacements = [
        ("&", "&amp;"),
        ("<", "&lt;"),
        (">", "&gt;"),
        ('"', "&quot;"),
        ("'", "&#x27;"),
        ("/", "&#x2F;"),
    ]
    result = text
    for old, new in replacements:
        result = result.replace(old, new)
    return result


def extract_payload_text(request) -> str:
    parts: List[str] = []
    try:
        ct = request.META.get("CONTENT_TYPE", "")
        if "application/json" in ct:
            parts.append(
                json.dumps(
                    json.loads(request.body.decode("utf-8") or "{}"), ensure_ascii=False
                )
            )
        else:
            parts.append(request.body.decode("utf-8", errors="ignore"))
    except Exception:
        pass
    qs = request.META.get("QUERY_STRING", "")
    if qs:
        parts.append(qs)
    parts.append(request.META.get("HTTP_USER_AGENT", ""))
    parts.append(request.META.get("HTTP_REFERER", ""))
    return " ".join([p for p in parts if p])


# Middleware XSS
class XSSDefenseMiddleware(MiddlewareMixin):
    """
    Middleware Django que detecta XSS en IPs no confiables.
    Solo marca el ataque en request.sql_attack_info para que
    AuditoriaMiddleware lo registre y bloquee.
    """

    def process_request(self, request):
        trusted_ips: List[str] = getattr(settings, "XSS_DEFENSE_TRUSTED_IPS", [])
        ip = request.META.get("REMOTE_ADDR", "")
        if ip in trusted_ips:
            return None  # IP confiable → no analizar

        excluded_paths: List[str] = getattr(settings, "XSS_DEFENSE_EXCLUDED_PATHS", [])
        if any(request.path.startswith(p) for p in excluded_paths):
            return None

        payload = extract_payload_text(request)
        if not payload:
            return None

        flagged, matches = detect_xss_text(payload)
        if not flagged:
            return None

        logger.warning(
            "XSS detectado desde IP %s: %s ; payload truncated: %.200s",
            ip,
            matches,
            payload,
        )

        # Solo marcamos el ataque, no bloqueamos aquí
        request.sql_attack_info = {
            "ip": ip,
            "tipos": ["XSS"],
            "descripcion": matches,
            "payload": payload,
        }

        return None


""" 
Algoritmos relacionados:
    *Guardar entradas sospechosas con AES-GCM para confidencialidad y autenticidad.
Contribución a fórmula de amenaza S:
S_xss = w_xss * detecciones_xss
S_xss = 0.3 * 2
donde w_xss es peso asignado a XSS y detecciones_xss es la cantidad de patrones detectados.

"""
