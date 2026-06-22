# Contributing

This is a curated directory of public **AI agent skill / extension ecosystems** —
protocols, platform skill systems, and marketplaces. Listings are pointers to
canonical pages — no third-party code is vendored.

## Add or update an entry

1. Edit [`data.py`](data.py) — add a `Tool(...)` with the correct category, the
   `open_source` flag, the license (or `"Proprietary"`), a short note, and the
   canonical link. Omit anything you can't verify.
2. Run `python main.py generate` to refresh `README.md`.
3. Run `pytest -q`.
4. Open a PR linking the canonical page.

## Quality bar

- Catalog skill **systems / protocols / marketplaces** — not individual tools
  (see "agent tools") or code SDKs (see "agent frameworks").
- This is new and fast-moving — **accuracy over count**. Omit any entry whose
  name, URL, or license you can't confirm.
- `python main.py generate` must leave `README.md` unchanged in CI.
