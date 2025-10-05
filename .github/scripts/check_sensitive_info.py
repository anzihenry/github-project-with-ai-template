#!/usr/bin/env python3
"""Scan the repository for accidental leakage of local machine details.

The script flags potential occurrences of absolute user directories or host-specific
identifiers so that contributors can replace them with neutral placeholders.
"""
from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path
from typing import Iterable, Iterator, List, Sequence, Tuple

EXCLUDED_DIRS: Sequence[str] = (
    ".git",
    ".github/scripts/__pycache__",
    "node_modules",
    ".venv",
)

# Regex patterns paired with human readable descriptions.
PATTERNS: Sequence[Tuple[re.Pattern[str], str]] = (
    (
        re.compile(r"/Users/([A-Za-z0-9._-]+)/"),
        "macOS-style absolute user path (/Users/<name>/)",
    ),
    (
        re.compile(r"\\Users\\([A-Za-z0-9._-]+)\\"),
        "Windows-style absolute user path (\\\\Users\\\\<name>\\\\)",
    ),
    (
        re.compile(r"/home/([A-Za-z0-9._-]+)/"),
        "Linux-style absolute home path (/home/<name>/)",
    ),
)

PLACEHOLDER_TOKENS: Sequence[str] = (
    "USER",
    "USERNAME",
    "HOST",
    "HOSTNAME",
    "OWNER",
)


def is_placeholder(token: str) -> bool:
    """Return True if the matched token looks like a safe placeholder."""
    stripped = token.strip()

    if not stripped:
        return True

    if stripped.startswith("${") and stripped.endswith("}"):
        return True

    if stripped.startswith("<") and stripped.endswith(">"):
        return True

    normalized = stripped.replace("_", "").replace("-", "").upper()
    return normalized in PLACEHOLDER_TOKENS


def iter_candidate_files(root: Path) -> Iterator[Path]:
    for path in root.rglob("*"):
        if not path.is_file():
            continue

        rel_path = path.relative_to(root)
        parts = rel_path.parts
        if any(part.startswith(".") and part != ".github" for part in parts):
            continue

        rel_str = str(rel_path)
        if any(rel_str.startswith(excluded) for excluded in EXCLUDED_DIRS):
            continue

        try:
            if path.stat().st_size > 1_000_000:  # skip files larger than 1 MB
                continue
        except OSError:
            continue

        yield path


def scan_file(path: Path) -> List[Tuple[int, str, str, str]]:
    findings: List[Tuple[int, str, str, str]] = []
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            return findings
    except Exception:
        return findings

    for lineno, line in enumerate(text.splitlines(), start=1):
        for pattern, description in PATTERNS:
            for match in pattern.finditer(line):
                token = match.group(1)
                if is_placeholder(token):
                    continue
                findings.append((lineno, line.strip(), token, description))
    return findings


def format_report(findings: List[Tuple[Path, List[Tuple[int, str, str, str]]]]) -> str:
    lines: List[str] = []
    lines.append("Sensitive information check failed. Found potential leaks:")
    lines.append("")
    for file_path, entries in findings:
        lines.append(f"- {file_path}")
        for lineno, snippet, token, description in entries:
            truncated = snippet if len(snippet) <= 160 else snippet[:157] + "..."
            lines.append(
                f"    L{lineno}: {description} => '{token}'\n"
                f"        {truncated}"
            )
    lines.append("")
    lines.append(
        "Please replace real user or host identifiers with placeholders such as '<USER>' or '${USER}'."
    )
    return "\n".join(lines)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--root",
        type=Path,
        default=Path.cwd(),
        help="Repository root path (defaults to current working directory).",
    )
    args = parser.parse_args(argv)

    root = args.root.resolve()
    findings: List[Tuple[Path, List[Tuple[int, str, str, str]]]] = []

    for file_path in iter_candidate_files(root):
        entries = scan_file(file_path)
        if entries:
            findings.append((file_path.relative_to(root), entries))

    if findings:
        sys.stderr.write(format_report(findings) + "\n")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
