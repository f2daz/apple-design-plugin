# audit – HIG-Konformität prüfen

Systematische, belegte Prüfung. Für große Ziele (ganze App, mehrere Plattformen) den Agenten `apple-design:hig-reviewer` je Plattform parallel starten und die Ergebnisse zusammenführen.

## Umfang klären

Ziel bestimmen (Datei, Screen, Feature, ganze App). Ist das unklar: AskUserQuestion – „Welcher Umfang?“ (aktuelle Änderung (Empfohlen) · ein Screen · ganze App) und „Welche Plattformen?“.

## Prüfschritte

1. **Kontext**: `APPLE_DESIGN.md`, Ziel-OS, Plattformen. Je Plattform die Checkliste aus `reference/platforms/<p>.md` (Abschnitt „Review-Checkliste“) laden.
2. **Statische Prüfung im Code** – schnelle Funde:
   ```bash
   grep -rnE "\.font\(\.system\(size:" --include=*.swift .             # feste Schriftgrößen
   grep -rnE "Color\((red|.*#)|UIColor\(red:|NSColor\(red:|Color\(hex" --include=*.swift .  # Rohfarben
   grep -rnE "\.frame\((width|height): *[1-3][0-9]\b" --include=*.swift .   # evtl. zu kleine Trefferflächen
   grep -rnE "onTapGesture" --include=*.swift .                          # Tap ohne Button-Semantik/Label?
   grep -rnE "\.glassEffect|\.background\(\.ultraThinMaterial" --include=*.swift .   # Glass/Material-Einsatzorte prüfen
   grep -rnE "Image\(\"" --include=*.swift .                              # eigene Bilder statt SF Symbols?
   grep -rnE "accessibilityLabel|accessibilityHidden" --include=*.swift . | wc -l
   ```
   Jeden Treffer im Kontext bewerten – kein automatisches Urteil.
3. **Gerenderte Prüfung** (wenn baubar): Screenshots je Gerätklasse, hell/dunkel, AX-Textgröße (siehe build.md). Ohne Simulator: sagen, dass nur statisch geprüft wurde.
4. **Querschnitt**: [accessibility](../foundations/accessibility.md), [typography](../foundations/typography.md), [color-and-dark-mode](../foundations/color-and-dark-mode.md), [materials-and-liquid-glass](../foundations/materials-and-liquid-glass.md), Komponentenregeln der verwendeten Komponenten.
5. **Zweifelsfälle** am Original prüfen: `hig_search.py page <slug> --section "<…>"`.

## Schweregrade

| Grad | Bedeutung | Beispiele |
|---|---|---|
| P0 Blocker | bricht Bedienbarkeit/Barrierefreiheit oder App-Review-relevante Regel | kein VoiceOver-Label auf Icon-Button, Text abgeschnitten bei großer Schrift, blockierter Back-Swipe, eingeschränktes Apple-Symbol zweckentfremdet |
| P1 Hoch | deutlich unplattformtypisch | eigene Tab-Bar, Hamburger-Menü auf iOS, iPhone-Layout gestreckt auf iPad, fehlende Menübefehle auf dem Mac |
| P2 Mittel | Konsistenz/Feinschliff | Rohfarben statt semantischer Farben, gemischte Symbolgewichte, falsche Button-Hierarchie |
| P3 Niedrig | Verbesserung | Haptik, Animation, Texte |

## Bericht

```markdown
## HIG-Audit: <Ziel> (<Plattformen>, Ziel-OS …)
Geprüft: statisch | Simulator (<Geräte>) · Stand HIG-Spiegel: <Datum>

| # | Grad | Fundstelle | Befund | Beleg | Fix |
|---|---|---|---|---|---|
| 1 | P0 | `Views/Foo.swift:42` | … | hig:buttons#Best-practices | … |

**Stärken:** …
**Nächste Schritte:** P0/P1 jetzt beheben? (→ AskUserQuestion: alle P0+P1 fixen (Empfohlen) · nur P0 · nur Bericht)
```

Nach Zustimmung fixen, dann betroffene Screens erneut prüfen.
