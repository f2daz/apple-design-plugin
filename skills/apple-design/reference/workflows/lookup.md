# hig · symbols · whatsnew – look things up

## hig <question>

1. Check the matching reference file (platform/foundation/component) – the fastest path.
2. To confirm or for detailed questions: `hig_search.py search "<2–4 terms>" [--platform …]`, then `hig_search.py page <slug> --section "<section>"`.
3. Platform-specific: `hig_search.py platform <p> --page <slug>`.
4. Answer: direct answer first, then rules with `hig:<slug>#Anchor`, optionally a SwiftUI snippet. No numbers without a source; if nothing is found, say so.
5. For very recent topics run `hig_sync.py --if-stale 7` first.

## symbols <term>

1. `sf_symbols.py search <term> [--min-ios <target OS>]` – target OS from `APPLE_DESIGN.md`. Search terms are English; translate the user's words.
2. For favorites, `sf_symbols.py info <name>`: fill variant, categories, **restrictions** (some symbols may only refer to the respective Apple product/service and must not be modified).
3. 3–6 suggestions with a short meaning, minimum OS, recommended rendering mode; SwiftUI: `Image(systemName: "…")` or `Label("…", systemImage: "…")`.
4. Visual check: SF Symbols app (`resources.py show "sf symbols"`; the DMG may already be in `~/.apple-design/downloads`).
5. No match: try synonyms, browse a category (`sf_symbols.py categories`, `category <key>`), otherwise a custom symbol from the SF Symbols template (hig:sf-symbols#Custom-symbols).

## whatsnew

1. `hig_sync.py --if-stale 1`, then `hig_search.py updates --since <date>` (default: last 6 months).
2. Pick the changes relevant to the platforms in `APPLE_DESIGN.md`, read the changed section of each page and summarize in 1–2 sentences what it means for the project.
