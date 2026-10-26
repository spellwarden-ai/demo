#!/usr/bin/env python3
"""Checks this repository on every push (live demo spec 8.2, 8.8 and test 23). Standard library only.

    python3 tools/check_repo.py                    the shape of the repository and the safety of the fixtures
    python3 tools/check_repo.py --report scan.json  also compares a `spellwarden scan --format json` report with the
                                                    rule ids README.md records for each fixture

The shape: at most 2,000 tracked files and 20 MiB, no symbolic links, no name with a backslash or a `.`, `..` or empty
segment (the hosted importer refuses the whole archive otherwise), and nothing at the root that Claude Code loads
(`.claude/`, `.mcp.json`, `.claude-plugin/`). The safety: no provider token shape in any file, every URL in the fixtures
on a reserved or documentation host (or Spellwarden's own demo hosts), and every plugin description starting with the
warning. One line per failure; exit 1 on any failure, else 0."""
from __future__ import annotations

import argparse
import ipaddress
import json
import re
import subprocess
import sys
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parent.parent
MAX_FILES = 2000
MAX_BYTES = 20 * 2**20
ROOT_LOADED = (".claude", ".mcp.json", ".claude-plugin")
WARNING = "Demo fixture with deliberate problems. Do not install."
SKILLS = "fixtures/marketplace/plugins"

# Provider token shapes GitHub push protection and the scanner treat as secrets. Built from parts, so this file holds none.
TOKEN_SHAPES = tuple(re.compile(pattern) for pattern in (
    "AKIA" + "[0-9A-Z]{16}",
    "ASIA" + "[0-9A-Z]{16}",
    "gh[pousr]" + "_[A-Za-z0-9]{36,}",
    "github" + "_pat_[A-Za-z0-9_]{22,}",
    "glpat" + "-[A-Za-z0-9_-]{20,}",
    "xox[abprs]" + "-[A-Za-z0-9-]{10,}",
    "sk-ant" + "-[A-Za-z0-9_-]{20,}",
    "sk" + "-[A-Za-z0-9]{20,}",
    "AIza" + "[0-9A-Za-z_-]{35}",
    "-----BEGIN [A-Z ]*" + "PRIVATE KEY-----",
    "eyJ[A-Za-z0-9_-]{10,}" + r"\.eyJ[A-Za-z0-9_-]{10,}\.",
))
URL = re.compile(r"https?://([^/\s\"'`<>()\[\]{},;]+)", re.IGNORECASE)
RESERVED_SUFFIXES = (".invalid", ".example.com", ".example.org")
RESERVED_HOSTS = frozenset({"example.com", "example.org", "169.254.169.254"})
DOCUMENTATION = (ipaddress.ip_network("192.0.2.0/24"), ipaddress.ip_network("198.51.100.0/24"),
                 ipaddress.ip_network("203.0.113.0/24"), ipaddress.ip_network("2001:db8::/32"))
# Spellwarden's own: the demo MCP endpoints (spec 9.1), the site and this repository.
OWN_HOSTS = frozenset({"demo-mcp.spellwarden.ai", "spellwarden.ai", "github.com"})
RULE = re.compile(r"\bSW-[A-Z0-9]+-[0-9]{3}\b")


def tracked() -> list[tuple[str, str]]:
    """`(mode, path)` of every tracked file."""
    out = subprocess.run(["git", "ls-files", "-s", "-z"], cwd=ROOT, check=True, capture_output=True).stdout.decode("utf-8")
    entries = []
    for record in filter(None, out.split("\0")):
        meta, path = record.split("\t", 1)
        entries.append((meta.split()[0], path))
    return entries


def host_allowed(host: str, url: str) -> bool:
    host = host.rsplit("@", 1)[-1].split(":", 1)[0].strip("[]").lower().rstrip(".")
    if host in RESERVED_HOSTS or host.endswith(RESERVED_SUFFIXES):
        return True
    if host in OWN_HOSTS:
        return host != "github.com" or url.lower().startswith("https://github.com/spellwarden-ai/")
    try:
        address = ipaddress.ip_address(host)
    except ValueError:
        return False
    return any(address in network for network in DOCUMENTATION)


def descriptions(document: object) -> list[str]:
    """The plugin descriptions of a marketplace or a plugin manifest."""
    if not isinstance(document, dict):
        return []
    if isinstance(document.get("plugins"), list):
        return [plugin.get("description") for plugin in document["plugins"] if isinstance(plugin, dict)]
    return [document.get("description")]


def check_shape() -> list[str]:
    failures = []
    entries = tracked()
    if len(entries) > MAX_FILES:
        failures.append(f"repository: {len(entries)} files, at most {MAX_FILES}")
    total = 0
    for mode, path in entries:
        if mode == "120000":
            failures.append(f"{path}: a symbolic link")
            continue
        if mode == "160000":
            failures.append(f"{path}: a submodule")
            continue
        parts = path.split("/")
        if "\\" in path or any(part in ("", ".", "..") for part in parts):
            failures.append(f"{path}: a name the hosted importer refuses")
        if parts[0] in ROOT_LOADED:
            failures.append(f"{path}: Claude Code loads this from the root of a clone")
        data = (ROOT / path).read_bytes()
        total += len(data)
        text = data.decode("utf-8", errors="replace")
        for shape in TOKEN_SHAPES:
            if shape.search(text):
                failures.append(f"{path}: a provider token shape ({shape.pattern[:12]}...)")
        if path.startswith("fixtures/"):
            for line_number, line in enumerate(text.splitlines(), start=1):
                for match in URL.finditer(line):
                    if not host_allowed(match.group(1), match.group(0) + line[match.end():]):
                        failures.append(f"{path}:{line_number}: {match.group(0)} is not a reserved or documentation host")
            name = PurePosixPath(path).name
            if name in ("marketplace.json", "plugin.json") and PurePosixPath(path).parent.name == ".claude-plugin":
                for description in descriptions(json.loads(text)):
                    if not (isinstance(description, str) and description.startswith(WARNING)):
                        failures.append(f"{path}: a plugin description that does not start with the warning")
    if total > MAX_BYTES:
        failures.append(f"repository: {total} bytes, at most {MAX_BYTES}")
    return failures


def ids_on(line: str, name: str) -> set[str]:
    return set(RULE.findall(line.replace(f"`{name}`", " ")))


def recorded(readme: str, skills: list[str]) -> tuple[dict[str, set[str]], dict[str, set[str]], set[str]]:
    """What README.md records: per skill (a line with the skill's name in backticks), per fixture file (a table row that
    starts with its path in backticks) and for the whole repository (the lines with `repository`), as `seed.py check`
    reads them."""
    per_skill: dict[str, set[str]] = {}
    per_file: dict[str, set[str]] = {}
    repository: set[str] = set()
    for line in readme.splitlines():
        for name in skills:
            if f"`{name}`" in line:
                per_skill.setdefault(name, set()).update(ids_on(line, name))
        match = re.match(r"\|\s*`(fixtures/[^`]+)`\s*\|", line)
        if match:
            per_file.setdefault(match.group(1), set()).update(ids_on(line, match.group(1)))
        if "`repository`" in line:
            repository |= ids_on(line, "repository")
    return per_skill, per_file, repository


def check_report(report_path: str) -> list[str]:
    report = json.loads(Path(report_path).read_text(encoding="utf-8"))
    failures = [f"scan: the scanner reported an error ({error.get('code')}: {error.get('path')})" for error in report.get("errors") or []]
    skills = sorted(path.parent.name for path in (ROOT / SKILLS).glob("*/skills/*/SKILL.md"))
    per_skill, per_file, repository = recorded((ROOT / "README.md").read_text(encoding="utf-8"), skills)
    found_skill: dict[str, set[str]] = {}
    found_file: dict[str, set[str]] = {}
    skill_items = {item["path"]: item["path"].rsplit("/", 1)[-1] for item in report.get("items") or [] if item.get("kind") == "skill"}
    for finding in report.get("findings") or []:
        item = finding.get("item") or ""
        if item in skill_items:
            found_skill.setdefault(skill_items[item], set()).add(finding["rule_id"])
        else:
            found_file.setdefault(finding["location"]["path"], set()).add(finding["rule_id"])
    for name in sorted(set(found_skill) | set(per_skill)):
        if found_skill.get(name, set()) != per_skill.get(name, set()):
            failures.append(f"skill {name}: the scan reports {sorted(found_skill.get(name, ()))}, README.md records "
                            f"{sorted(per_skill.get(name, ()))}")
    for path in sorted(set(found_file) | set(per_file)):
        if found_file.get(path, set()) != per_file.get(path, set()):
            failures.append(f"{path}: the scan reports {sorted(found_file.get(path, ()))}, README.md records "
                            f"{sorted(per_file.get(path, ()))}")
    engine = {finding["rule_id"] for finding in report.get("findings") or []}
    recorded_engine = {rule for rule in repository if not rule.startswith(("SW-REG-", "SW-ORG-"))}
    if engine != recorded_engine:
        failures.append(f"repository: the scan reports {sorted(engine)}, README.md records {sorted(recorded_engine)}")
    return failures


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0])
    parser.add_argument("--report", help="a `spellwarden scan --format json` report of this repository")
    args = parser.parse_args(argv)
    failures = check_shape()
    if args.report:
        failures += check_report(args.report)
    for failure in failures:
        print(failure)
    if not failures:
        print("check_repo: no problems" + (" (shape, safety and the README's record)" if args.report else " (shape and safety)"))
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
