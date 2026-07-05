#!/usr/bin/env python3
import ast
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_GATES = [
    "intent",
    "language",
    "layout",
    "system",
    "ratio",
    "implementation",
    "quality",
    "explanation",
]
EXPECTED_MODES = {"advisory", "balanced", "hybrid-strict", "strict"}

def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def fail(message):
    raise SystemExit(message)

def require_path(path):
    if not (ROOT / path).exists():
        fail(f"Missing required path: {path}")

def validate_plugin_manifest():
    manifest = load_json(ROOT / ".codex-plugin/plugin.json")
    if manifest.get("name") != "frameward":
        fail("Plugin manifest name must be frameward.")
    for key in ("skills", "hooks"):
        value = manifest.get(key)
        if not isinstance(value, str):
            fail(f"Plugin manifest field {key} must be a string path.")
        require_path(value.removeprefix("./"))

    interface = manifest.get("interface", {})
    for asset_key in ("composerIcon", "logo"):
        require_path(interface.get(asset_key, "").removeprefix("./"))
    for screenshot in interface.get("screenshots", []):
        require_path(str(screenshot).removeprefix("./"))

def validate_hooks():
    hooks_config = load_json(ROOT / "hooks/hooks.json")
    hooks = hooks_config.get("hooks", {})
    for event, entries in hooks.items():
        if not isinstance(entries, list):
            fail(f"Hook event {event} must be a list.")
        for entry in entries:
            for hook in entry.get("hooks", []):
                command = hook.get("command", "")
                match = re.search(r"\$\{PLUGIN_ROOT\}/([^ ]+\.py)", command)
                if match:
                    require_path(match.group(1))

    for hook_file in sorted((ROOT / "hooks").rglob("*.py")):
        try:
            ast.parse(hook_file.read_text(encoding="utf-8"), filename=str(hook_file))
        except SyntaxError as exc:
            fail(f"Hook Python syntax error in {hook_file.relative_to(ROOT)}: {exc}")

    common = (ROOT / "hooks/lib/frameward_common.py").read_text(encoding="utf-8")
    for gate in EXPECTED_GATES:
        if f'"{gate}"' not in common:
            fail(f"Missing default hook gate: {gate}")

def validate_skills():
    skill_files = sorted((ROOT / "skills").glob("*/SKILL.md"))
    if not skill_files:
        fail("No skills found.")
    for skill in skill_files:
        text = skill.read_text(encoding="utf-8")
        if not text.startswith("---\n"):
            fail(f"Skill missing YAML frontmatter: {skill.relative_to(ROOT)}")
        end = text.find("\n---", 4)
        if end == -1:
            fail(f"Skill frontmatter is not closed: {skill.relative_to(ROOT)}")
        frontmatter = text[4:end].strip().splitlines()
        fields = {}
        for line in frontmatter:
            if ":" in line:
                key, value = line.split(":", 1)
                fields[key.strip()] = value.strip().strip('"')
        if not fields.get("name"):
            fail(f"Skill frontmatter missing name: {skill.relative_to(ROOT)}")
        if not fields.get("description"):
            fail(f"Skill frontmatter missing description: {skill.relative_to(ROOT)}")
        if len(fields["description"]) < 40:
            fail(f"Skill description is too vague: {skill.relative_to(ROOT)}")

def validate_configs_and_schemas():
    for schema in (ROOT / "schemas").glob("*.json"):
        load_json(schema)

    loop_schema = load_json(ROOT / "schemas/frameward-loop-state.schema.json")
    modes = set(loop_schema["properties"]["mode"]["enum"])
    if modes != EXPECTED_MODES:
        fail(f"Frameward loop mode schema mismatch: {sorted(modes)}")

    gates = load_json(ROOT / ".frameward/gates.example.json").get("requiredGates", [])
    if gates != EXPECTED_GATES:
        fail(f"Frameward gates mismatch: {gates}")

    config = load_json(ROOT / ".frameward/config.example.json")
    design_system = config.get("designSystem", {})
    astryx = config.get("providers", {}).get("astryx", {})
    if config.get("enforcementMode") != "advisory":
        fail("Example config must default to advisory mode.")
    if design_system.get("allowDependencyInstall") is not False:
        fail("Example config must not allow dependency installs by default.")
    if design_system.get("allowMcp") is not False:
        fail("Example config must not allow MCP by default.")
    if astryx.get("enabled") is not False:
        fail("Astryx must be disabled by default.")
    if astryx.get("requireExplicitInstallApproval") is not True:
        fail("Astryx install must require explicit approval.")

def main():
    required = [
        ".codex-plugin/plugin.json",
        "hooks/hooks.json",
        "README.md",
        "AGENTS.md",
        "providers/astryx/provider.md",
        "skills/client-intent-discovery/SKILL.md",
        "skills/design-system-provider-detection/SKILL.md",
        "skills/astryx-adapter/SKILL.md",
    ]

    missing = [p for p in required if not (ROOT / p).exists()]
    if missing:
        fail(f"Missing required files: {missing}")

    validate_plugin_manifest()
    validate_hooks()
    validate_skills()
    validate_configs_and_schemas()

    print("Frameward scaffold validation passed.")

if __name__ == "__main__":
    main()
