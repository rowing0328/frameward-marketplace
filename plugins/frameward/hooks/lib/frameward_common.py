import json
import os
import re
from pathlib import Path
from typing import Any, Dict, List

UI_KEYWORDS = [
    "ui", "ux", "screen", "page", "layout", "button", "form", "modal",
    "dashboard", "card", "table", "mobile", "responsive", "accessibility",
    "design", "style", "component", "frontend", "astryx",
    "화면", "페이지", "버튼", "레이아웃", "디자인", "모바일", "반응형",
    "예쁘", "깔끔", "고급", "사용하기", "불편", "복잡", "촌스럽", "보기 좋",
    "카드", "폼", "대시보드", "테이블"
]

VAGUE_WORDS = [
    "better", "cleaner", "modern", "polished", "premium", "nice", "easier",
    "좋게", "깔끔", "고급", "예쁘", "모던", "쉽게", "불편", "촌스럽", "복잡"
]

DEFAULT_REQUIRED_GATES = [
    "intent",
    "language",
    "layout",
    "system",
    "ratio",
    "implementation",
    "quality",
    "explanation"
]

VALID_MODES = {"advisory", "balanced", "hybrid-strict", "strict"}

DEPENDENCY_INSTALL_RE = re.compile(
    r"\b(npm\s+install|pnpm\s+add|yarn\s+add|bun\s+add|pip(?:3)?\s+install)\b",
    re.IGNORECASE,
)

ASTRYX_ACTIVATION_RE = re.compile(
    r"\b(astryx\s+init|astryx\s+setup|mcpServers|mcp\s+.*astryx|astryx.*mcp)\b",
    re.IGNORECASE,
)

UI_FILE_RE = re.compile(
    r"(\.(tsx|jsx|vue|svelte|css|scss|sass|less)$|/(components|pages|app|views|screens|ui|styles?)/)",
    re.IGNORECASE,
)

NEGATED_APPROVAL_RE = re.compile(
    r"\b(do not|don't|never|without approval|unless .*approve|no automatic|not automatic)\b",
    re.IGNORECASE,
)

INSTALL_APPROVAL_RE = re.compile(
    r"\b(approve|approved|allow|allowed|yes).*(install|dependency|dependencies|astryx)\b",
    re.IGNORECASE,
)

MCP_APPROVAL_RE = re.compile(
    r"\b(approve|approved|allow|allowed|yes).*(mcp|external provider|astryx)\b",
    re.IGNORECASE,
)

def read_event() -> Dict[str, Any]:
    try:
        raw = os.sys.stdin.read()
        if not raw.strip():
            return {}
        return json.loads(raw)
    except Exception:
        return {}

def plugin_data_dir() -> Path:
    env = os.environ.get("PLUGIN_DATA")
    if env:
        p = Path(env)
    else:
        p = Path.cwd() / ".frameward" / "runtime"
    p.mkdir(parents=True, exist_ok=True)
    return p

def state_path() -> Path:
    return plugin_data_dir() / "frameward-loop-state.json"

def load_state() -> Dict[str, Any]:
    path = state_path()
    if not path.exists():
        return {
            "active": False,
            "taskType": "unknown",
            "requiredGates": DEFAULT_REQUIRED_GATES,
            "completedGates": [],
            "failedGates": [],
            "loopCount": 0,
            "maxLoops": 3,
            "mode": "advisory",
            "provider": "project-native",
            "providerMode": "native",
            "approvals": {
                "dependencyInstall": False,
                "astryxMcp": False
            },
            "lastChangedFiles": []
        }
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {
            "active": False,
            "taskType": "unknown",
            "requiredGates": DEFAULT_REQUIRED_GATES,
            "completedGates": [],
            "failedGates": ["state_read_error"],
            "loopCount": 0,
            "maxLoops": 3,
            "mode": "advisory",
            "provider": "project-native",
            "providerMode": "native",
            "approvals": {
                "dependencyInstall": False,
                "astryxMcp": False
            },
            "lastChangedFiles": []
        }

def save_state(state: Dict[str, Any]) -> None:
    path = state_path()
    path.write_text(json.dumps(state, indent=2, ensure_ascii=False), encoding="utf-8")

def detect_ui_task(text: str) -> bool:
    if not text:
        return False
    t = text.lower()
    return any(k.lower() in t for k in UI_KEYWORDS)

def detect_vague(text: str) -> bool:
    if not text:
        return False
    t = text.lower()
    return any(k.lower() in t for k in VAGUE_WORDS)

def prompt_from_event(event: Dict[str, Any]) -> str:
    for key in ("prompt", "user_prompt", "input", "message"):
        value = event.get(key)
        if isinstance(value, str):
            return value
    return json.dumps(event, ensure_ascii=False)

def complete_gate(state: Dict[str, Any], gate: str) -> None:
    completed = set(state.get("completedGates", []))
    completed.add(gate)
    state["completedGates"] = sorted(completed)

def missing_gates(state: Dict[str, Any]) -> List[str]:
    required = set(state.get("requiredGates", DEFAULT_REQUIRED_GATES))
    completed = set(state.get("completedGates", []))
    return sorted(required - completed)

def active_config_mode() -> str:
    # Project config, if present, wins. Keep failure-safe advisory default.
    candidates = [
        Path.cwd() / ".frameward" / "config.json",
        Path.cwd() / ".frameward" / "config.example.json",
    ]
    for c in candidates:
        if c.exists():
            try:
                data = json.loads(c.read_text(encoding="utf-8"))
                mode = str(data.get("enforcementMode", "advisory"))
                return mode if mode in VALID_MODES else "advisory"
            except Exception:
                pass
    return "advisory"

def approval_flags(text: str) -> Dict[str, bool]:
    if not text or NEGATED_APPROVAL_RE.search(text):
        return {
            "dependencyInstall": False,
            "astryxMcp": False
        }
    return {
        "dependencyInstall": bool(INSTALL_APPROVAL_RE.search(text)),
        "astryxMcp": bool(MCP_APPROVAL_RE.search(text)),
    }

def event_text(event: Dict[str, Any]) -> str:
    parts: List[str] = []
    for key in ("tool_name", "tool", "name"):
        value = event.get(key)
        if isinstance(value, str):
            parts.append(value)
    tool_input = event.get("tool_input", {})
    if isinstance(tool_input, dict):
        for key in ("command", "file_path", "path", "filename"):
            value = tool_input.get(key)
            if isinstance(value, str):
                parts.append(value)
    return "\n".join(parts)

def is_dependency_or_provider_activation(event: Dict[str, Any]) -> str:
    text = event_text(event)
    if DEPENDENCY_INSTALL_RE.search(text):
        return "dependency"
    if ASTRYX_ACTIVATION_RE.search(text):
        return "astryx-mcp"
    return ""

def is_ui_edit_event(event: Dict[str, Any]) -> bool:
    return bool(UI_FILE_RE.search(event_text(event)))

def make_context(message: str, event_name: str) -> Dict[str, Any]:
    return {
        "hookSpecificOutput": {
            "hookEventName": event_name,
            "additionalContext": message
        }
    }

def make_deny(message: str) -> Dict[str, Any]:
    return {
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": message
        }
    }
