"""AI Agent Skills & Extensions Directory — CLI.

Search, filter, and export a curated registry of agent skill systems/protocols/
marketplaces, and regenerate the README from it.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import asdict
from importlib.resources import files
from pathlib import Path

from __version__ import __version__
from data import TOOLS, Category, Tool


if Path(__file__).with_name("pyproject.toml").is_file():
    RESOURCE_DIR = Path(__file__).parent / "resources"
else:
    RESOURCE_DIR = files("agent_skills_directory_resources")

RESOURCE_CATALOG = RESOURCE_DIR.joinpath("design-motion.csv")
SOURCE_CATALOG = RESOURCE_DIR.joinpath("creative-discovery.csv")


def _matches(t: Tool, query: str) -> bool:
    q = query.lower()
    hay = " ".join([t.name, t.org, t.category.value, t.license,
                    t.note, " ".join(t.tags)]).lower()
    return q in hay


def _to_dict(t: Tool) -> dict:
    out = asdict(t)
    out["category"] = t.category.value
    out["tags"] = list(t.tags)
    return out


def _source_glyph(t: Tool) -> str:
    if t.open_source:
        return "🟢"
    if t.license != "Proprietary":
        return "🔃"
    return "🔒"


def _print_table(tools: list[Tool]) -> None:
    if not tools:
        print("No entries matched.")
        return
    width = max(len(t.name) for t in tools)
    for t in sorted(tools, key=lambda t: (t.category.value, t.name.lower())):
        print(f"{_source_glyph(t)} {t.name.ljust(width)}  {t.org:<26} [{t.category.label}]")


def cmd_list(args: argparse.Namespace) -> int:
    tools = list(TOOLS)
    if args.category:
        tools = [t for t in tools if t.category.value == args.category]
    if args.open_source:
        tools = [t for t in tools if t.open_source]
    if args.proprietary:
        tools = [t for t in tools if not t.open_source]
    _print_table(tools)
    print(f"\n{len(tools)} entry(ies).")
    return 0


def cmd_search(args: argparse.Namespace) -> int:
    tools = [t for t in TOOLS if _matches(t, args.query)]
    _print_table(tools)
    print(f"\n{len(tools)} match(es) for {args.query!r}.")
    return 0


def cmd_categories(_: argparse.Namespace) -> int:
    counts: dict[str, int] = {}
    for t in TOOLS:
        counts[t.category.label] = counts.get(t.category.label, 0) + 1
    width = max(len(k) for k in counts)
    for label in sorted(counts):
        print(f"{label.ljust(width)}  {counts[label]}")
    print(f"\n{len(counts)} categories, {len(TOOLS)} entries.")
    return 0


def cmd_stats(_: argparse.Namespace) -> int:
    oss = sum(1 for t in TOOLS if t.open_source)
    print(f"entries:       {len(TOOLS)}")
    print(f"open:          {oss}")
    print(f"proprietary:   {len(TOOLS) - oss}")
    print(f"categories:    {len({t.category for t in TOOLS})}")
    return 0


def cmd_export(args: argparse.Namespace) -> int:
    rows = [_to_dict(t) for t in TOOLS]
    if args.format == "json":
        print(json.dumps(rows, indent=2))
    else:
        cols = ["name", "org", "category", "open_source", "license", "url"]
        w = csv.writer(sys.stdout)
        w.writerow(cols)
        for r in rows:
            w.writerow([r.get(c, "") for c in cols])
    return 0


def cmd_resources(args: argparse.Namespace) -> int:
    """Search the companion collection of skills and tools for design and motion."""
    terms = " ".join(args.words).casefold().split()
    with RESOURCE_CATALOG.open(encoding="utf-8", newline="") as catalog:
        rows = []
        for row in csv.DictReader(catalog):
            if args.kind and row["kind"] != args.kind:
                continue
            searchable = " ".join(row[key] for key in ("id", "name", "description", "tags")).casefold()
            if all(term in searchable for term in terms):
                rows.append({**row, "tags": row["tags"].split("|") if row["tags"] else []})
    rows.sort(key=lambda row: (row["name"].casefold(), row["id"]))
    if args.format == "json":
        print(json.dumps(rows, indent=2, ensure_ascii=False))
    else:
        for row in rows:
            print(f"{row['name']} [{row['kind']}]  {row['description']}")
            print(f"  {row['evidence_url']}")
        print(f"{len(rows)} resource(s).")
    return 0


def cmd_sources(args: argparse.Namespace) -> int:
    """Search creative project and skill discovery sources."""
    terms = " ".join(args.words).casefold().split()
    with SOURCE_CATALOG.open(encoding="utf-8", newline="") as catalog:
        rows = []
        for row in csv.DictReader(catalog):
            if args.has_feed and not row["feed_url"].strip():
                continue
            searchable = " ".join(row[key] for key in ("id", "name", "type", "focus", "notes")).casefold()
            if all(term in searchable for term in terms):
                rows.append(row)
    rows.sort(key=lambda row: (row["name"].casefold(), row["id"]))
    if args.format == "json":
        print(json.dumps(rows, indent=2, ensure_ascii=False))
    else:
        for row in rows:
            print(f"{row['name']} [{row['type']}]  {row['focus']}")
            print(f"  {row['browse_url']}")
            if row["feed_url"]:
                print(f"  Feed: {row['feed_url']}")
        print(f"{len(rows)} source(s).")
    return 0


def cmd_generate(_: argparse.Namespace) -> int:
    from report import generate
    readme = Path(__file__).parent / "README.md"
    readme.write_text(generate() + "\n", encoding="utf-8")
    print(f"Wrote {readme} ({len(TOOLS)} entries).")
    return 0


def cmd_version(_: argparse.Namespace) -> int:
    print(f"ai-agent-skills-directory {__version__}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="skill-dir", description="AI Agent Skills & Extensions Directory CLI")
    p.add_argument("-V", "--version", action="version", version=f"%(prog)s {__version__}")
    sub = p.add_subparsers(dest="command")

    pl = sub.add_parser("list", help="List entries")
    pl.add_argument("--category", choices=[c.value for c in Category])
    pl.add_argument("--open-source", action="store_true", help="Only open protocols/systems")
    pl.add_argument("--proprietary", action="store_true", help="Only proprietary platforms")
    pl.set_defaults(func=cmd_list)

    ps = sub.add_parser("search", help="Search name/org/note/tags")
    ps.add_argument("query")
    ps.set_defaults(func=cmd_search)

    sub.add_parser("categories", help="List categories + counts").set_defaults(func=cmd_categories)
    sub.add_parser("stats", help="Registry statistics").set_defaults(func=cmd_stats)

    pe = sub.add_parser("export", help="Export the registry")
    pe.add_argument("--format", choices=["json", "csv"], default="json")
    pe.set_defaults(func=cmd_export)

    pr = sub.add_parser("resources", help="Search the companion design and motion collection")
    pr.add_argument("words", nargs="*", help="Match every word against names, descriptions, IDs and tags")
    pr.add_argument("--kind", choices=["skill", "tool"], help="Filter by resource type")
    pr.add_argument("--format", choices=["text", "json"], default="text")
    pr.set_defaults(func=cmd_resources)

    sources = sub.add_parser("sources", help="Find sources for discovering creative projects and skills")
    sources.add_argument("words", nargs="*", help="Match every word against source IDs, names, types, focus and notes")
    sources.add_argument("--has-feed", action="store_true", help="Only list sources with a feed URL")
    sources.add_argument("--format", choices=["text", "json"], default="text")
    sources.set_defaults(func=cmd_sources)

    sub.add_parser("generate", help="Regenerate README.md").set_defaults(func=cmd_generate)
    sub.add_parser("version", help="Print version").set_defaults(func=cmd_version)
    return p


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    if not getattr(args, "command", None):
        parser.print_help()
        sys.exit(0)
    sys.exit(args.func(args))


if __name__ == "__main__":
    main()
