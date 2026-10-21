# hig · symbols · whatsnew – nachschlagen

## hig <frage>

1. Passende Referenzdatei prüfen (Plattform/Grundlage/Komponente) – schnellster Weg.
2. Zur Absicherung oder bei Detailfragen: `hig_search.py search "<2–4 Begriffe>" [--platform …]`, dann `hig_search.py page <slug> --section "<Abschnitt>"`.
3. Plattformspezifisch: `hig_search.py platform <p> --page <slug>`.
4. Antwort: direkte Antwort zuerst, dann Regeln mit `hig:<slug>#Anchor`, ggf. SwiftUI-Snippet. Keine Zahlen ohne Quelle; findet sich nichts, das sagen.
5. Bei sehr aktuellen Themen vorher `hig_sync.py --if-stale 7`.

## symbols <begriff>

1. `sf_symbols.py search <begriff> [--min-ios <Ziel-OS>]` – Ziel-OS aus `APPLE_DESIGN.md`.
2. Für Favoriten `sf_symbols.py info <name>`: Fill-Variante, Kategorien, **Einschränkungen** (manche Symbole dürfen nur für das jeweilige Apple-Produkt/-Dienst stehen und nicht verändert werden).
3. 3–6 Vorschläge mit kurzer Bedeutung, Mindest-OS, empfohlenem Rendering-Modus; SwiftUI: `Image(systemName: "…")` bzw. `Label("…", systemImage: "…")`.
4. Visuelle Kontrolle: SF Symbols App (`resources.py show "sf symbols"`; DMG ggf. bereits unter `~/.apple-design/downloads`).
5. Kein Treffer: Synonyme probieren (englisch), Kategorie durchsuchen (`sf_symbols.py categories`, `category <key>`), sonst Custom Symbol aus SF-Symbols-Template (hig:sf-symbols#Custom-symbols).

## whatsnew

1. `hig_sync.py --if-stale 1`, dann `hig_search.py updates --since <Datum>` (Standard: letzte 6 Monate).
2. Für die Plattformen aus `APPLE_DESIGN.md` relevante Änderungen auswählen, je Seite die geänderte Stelle lesen und in 1–2 Sätzen zusammenfassen, was das fürs Projekt heißt.
