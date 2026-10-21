# Typografie

> Quelle: lokaler HIG-Spiegel `~/.apple-design/hig/pages/typography.md` (gespiegelt 2026-10-21, Apple-Update 2025-12-16: Emphasized Weights ergänzt). Ergänzend: `accessibility`, `layout`, `sf-symbols`. Inhalte paraphrasiert; Kennwert-Tabellen als Fakten übernommen.

## Einordnung

Typografie trägt auf Apple-Plattformen drei Aufgaben: Lesbarkeit, Informationshierarchie und (sparsam) Markenausdruck. Die Systemschriften (San Francisco, New York) und die systemdefinierten **Text Styles** sind der Normalfall – sie bringen Dynamic Type, Bold Text, optische Größen und Tracking automatisch mit. Eigene Schriften sind erlaubt, müssen diese Verhaltensweisen aber selbst nachbauen.

## Kernregeln

- Verwende pro Plattform mindestens die Mindestgröße, im Fließtext die Standardgröße (Tabelle unten); bei dünnen Custom-Schnitten größer wählen. (hig:typography#Ensuring-legibility)
- Meide Ultralight, Thin und Light – vor allem bei kleinen Größen; bevorzuge Regular, Medium, Semibold, Bold. (hig:typography#Ensuring-legibility)
- Teste Lesbarkeit im echten Kontext (Distanz, Licht, Spiele-Overlays); bei Problemen Größe oder Kontrast erhöhen. (hig:typography#Ensuring-legibility)
- Baue Hierarchie über Gewicht, Größe und Farbe – und erhalte diese Hierarchie auch bei geänderter Textgröße. (hig:typography#Conveying-hierarchy)
- Halte die Zahl der Schriftfamilien minimal, auch in stark individualisierten UIs. (hig:typography#Conveying-hierarchy)
- Priorisiere beim Skalieren den Inhalt, den Menschen tatsächlich lesen wollen (z. B. Dialog statt Tab-Titel oder flüchtige Schadenszahlen). (hig:typography#Conveying-hierarchy)
- Nutze die eingebauten Text Styles; sie liefern Dynamic Type und Accessibility-Größen. (hig:typography#Using-system-fonts)
- Modifiziere Text Styles über Symbolic Traits (Bold, Loose/Tight Leading) statt eigene Größen zu erfinden; ab drei Zeilen kein Tight Leading. (hig:typography#Using-system-fonts)
- Bette Systemschriften nicht in die App ein – greife über `Font.Design` darauf zu (`.default` = SF, `.serif` = New York). (hig:typography#Using-system-fonts)
- Passe in Mockups ggf. das Tracking an (Tracking-Tabelle unten); zur Laufzeit erledigt das System das. (hig:typography#Tracking-values)
- Custom Fonts: Lesbarkeit sicherstellen und Dynamic Type sowie Bold Text selbst unterstützen. (hig:typography#Using-custom-fonts)
- Das Layout muss alle Textgrößen inkl. Larger Accessibility Sizes tragen; auf dem Gerät testen (Einstellungen > Bedienungshilfen > Anzeige & Textgröße > Größerer Text). (hig:typography#Supporting-Dynamic-Type)
- Skaliere bedeutungstragende Icons mit der Schrift (SF Symbols tun das automatisch). (hig:typography#Supporting-Dynamic-Type)
- Minimiere Truncation bei großen Größen; Ziel: bei der größten AX-Größe so viel nützlichen Text wie bei der größten Standardgröße. Mehrzeilige Labels zulassen. (hig:typography#Supporting-Dynamic-Type)
- Wechsle bei großen Größen auf gestapelte Layouts (Text über Sekundärelementen) und reduziere Spalten. (hig:typography#Supporting-Dynamic-Type)
- Halte Primärelemente auch bei sehr großer Schrift oben im View. (hig:typography#Supporting-Dynamic-Type)
- Lege Layouts so an, dass nebeneinanderliegende Views bei großer Schrift vertikal stapeln und Zeilen in der Höhe wachsen. (hig:layout#Adaptability)

## Kennwerte

### Standard- und Mindestgrößen (hig:typography#Ensuring-legibility)

| Plattform | Standardgröße | Mindestgröße |
|---|---|---|
| iOS, iPadOS | 17 pt | 11 pt |
| macOS | 13 pt | 10 pt |
| tvOS | 29 pt | 23 pt |
| visionOS | 17 pt | 12 pt |
| watchOS | 16 pt | 12 pt |

### Systemschriften (hig:typography#Using-system-fonts)

| Familie | Charakter | Varianten / Hinweise |
|---|---|---|
| San Francisco (SF) | Sans Serif | SF Pro, SF Compact, SF Arabic, SF Armenian, SF Georgian, SF Hebrew, SF Mono |
| SF Rounded | gerundete Variante | für SF Pro, SF Compact, SF Arabic, SF Armenian, SF Georgian, SF Hebrew |
| New York (NY) | Serif | allein oder mit SF kombinierbar |

- Beide Familien liegen als **Variable Fonts** vor; das System nutzt **dynamische optische Größen** (Text/Display stufenlos interpoliert). Diskrete optische Größen nur in Tools ohne Variable-Font-Support nötig.
- Gewichte Ultralight bis Black; SF zusätzlich in Breiten (u. a. Condensed, Expanded). SF Symbols haben äquivalente Gewichte → Symbol und Text gewichtsgleich setzen.
- SF Mono ist Teil der SF-Familie; der Spiegel nennt keine eigenen Größen-/Tracking-Werte für SF Mono.

| Plattform | Systemschrift | NY | Dynamic Type |
|---|---|---|---|
| iOS, iPadOS | SF Pro | ja | ja |
| macOS | SF Pro | nur für Mac-Catalyst-Apps genannt | **nein** |
| watchOS | SF Compact (Complications: SF Compact Rounded) | ja | ja |
| tvOS | SF Pro | ja | ja |
| visionOS | SF Pro (bolder Body/Title-Varianten, zusätzlich Extra Large Title 1/2) | ja, Text Styles explizit angeben | ja |

### Emphasized Weights

Hervorgehobene Varianten der Text Styles entstehen über Symbolic Traits (SwiftUI `bold()`, UIKit `traitBold` in `UIFontDescriptor`). Mögliche Emphasized Weights: Medium, Semibold, Bold, Heavy. In den Tabellen steht die jeweilige Emphasized Weight pro Style. (hig:typography#Specifications)

### iOS/iPadOS Dynamic Type – Standardgrößen (Größe/Leading in pt; Default = Large)

| Style | Weight | Emph. | xSmall | Small | Medium | Large | xLarge | xxLarge | xxxLarge |
|---|---|---|---|---|---|---|---|---|---|
| Large Title | Regular | Bold | 31/38 | 32/39 | 33/40 | 34/41 | 36/43 | 38/46 | 40/48 |
| Title 1 | Regular | Bold | 25/31 | 26/32 | 27/33 | 28/34 | 30/37 | 32/39 | 34/41 |
| Title 2 | Regular | Bold | 19/24 | 20/25 | 21/26 | 22/28 | 24/30 | 26/32 | 28/34 |
| Title 3 | Regular | Semibold | 17/22 | 18/23 | 19/24 | 20/25 | 22/28 | 24/30 | 26/32 |
| Headline | Semibold | Semibold | 14/19 | 15/20 | 16/21 | 17/22 | 19/24 | 21/26 | 23/29 |
| Body | Regular | Semibold | 14/19 | 15/20 | 16/21 | 17/22 | 19/24 | 21/26 | 23/29 |
| Callout | Regular | Semibold | 13/18 | 14/19 | 15/20 | 16/21 | 18/23 | 20/25 | 22/28 |
| Subhead | Regular | Semibold | 12/16 | 13/18 | 14/19 | 15/20 | 17/22 | 19/24 | 21/28 |
| Footnote | Regular | Semibold | 12/16 | 12/16 | 12/16 | 13/18 | 15/20 | 17/22 | 19/24 |
| Caption 1 | Regular | Semibold | 11/13 | 11/13 | 11/13 | 12/16 | 14/19 | 16/21 | 18/23 |
| Caption 2 | Regular | Semibold | 11/13 | 11/13 | 11/13 | 11/13 | 13/18 | 15/20 | 17/22 |

Punktgrößen bezogen auf 144 ppi (@2x) bzw. 216 ppi (@3x). (hig:typography#Specifications)

### iOS/iPadOS – Larger Accessibility Type Sizes (Größe/Leading in pt)

| Style | Weight | Emph. | AX1 | AX2 | AX3 | AX4 | AX5 |
|---|---|---|---|---|---|---|---|
| Large Title | Regular | Bold | 44/52 | 48/57 | 52/61 | 56/66 | 60/70 |
| Title 1 | Regular | Bold | 38/46 | 43/51 | 48/57 | 53/62 | 58/68 |
| Title 2 | Regular | Bold | 34/41 | 39/47 | 44/52 | 50/59 | 56/66 |
| Title 3 | Regular | Semibold | 31/38 | 37/44 | 43/51 | 49/58 | 55/65 |
| Headline | Semibold | Semibold | 28/34 | 33/40 | 40/48 | 47/56 | 53/62 |
| Body | Regular | Semibold | 28/34 | 33/40 | 40/48 | 47/56 | 53/62 |
| Callout | Regular | Semibold | 26/32 | 32/39 | 38/46 | 44/52 | 51/60 |
| Subhead | Regular | Semibold | 25/31 | 30/37 | 36/43 | 42/50 | 49/58 |
| Footnote | Regular | Semibold | 23/29 | 27/33 | 33/40 | 38/46 | 44/52 |
| Caption 1 | Regular | Semibold | 22/28 | 26/32 | 32/39 | 37/44 | 43/51 |
| Caption 2 | Regular | Semibold | 20/25 | 24/30 | 29/35 | 34/41 | 40/48 |

### macOS – eingebaute Text Styles (kein Dynamic Type; Größe/Line Height in pt)

| Text Style | Weight | Size | Line height | Emph. |
|---|---|---|---|---|
| Large Title | Regular | 26 | 32 | Bold |
| Title 1 | Regular | 22 | 26 | Bold |
| Title 2 | Regular | 17 | 22 | Bold |
| Title 3 | Regular | 15 | 20 | Semibold |
| Headline | **Bold** | 13 | 16 | Heavy |
| Body | Regular | 13 | 16 | Semibold |
| Callout | Regular | 12 | 15 | Semibold |
| Subheadline | Regular | 11 | 14 | Semibold |
| Footnote | Regular | 10 | 13 | Semibold |
| Caption 1 | Regular | 10 | 13 | Medium |
| Caption 2 | **Medium** | 10 | 13 | Semibold |

Bezogen auf 144 ppi (@2x). Achtung: Headline ist auf macOS Bold (iOS: Semibold), Caption 2 Medium.

### watchOS Dynamic Type – Standardgrößen (Größe/Leading in pt)

Defaults laut Spiegel: Small = 38 mm, Large = 40/41/42 mm, xLarge = 44/45/49 mm.

| Style | Weight | Emph. | xSmall | Small | Large | xLarge | xxLarge | xxxLarge |
|---|---|---|---|---|---|---|---|---|
| Large Title | Regular | Bold | 30/32.5 | 32/34.5 | 36/38.5 | 40/42.5 | 41/43.5 | 42/44.5 |
| Title 1 | Regular | Semibold | 28/30.5 | 30/32.5 | 34/36.5 | 38/40.5 | 39/41.5 | 40/42.5 |
| Title 2 | Regular | Semibold | 24/26.5 | 26/28.5 | 28/30.5 | 30/32.5 | 31/33.5 | 32/34.5 |
| Title 3 | Regular | Semibold | 17/19.5 | 18/20.5 | 19/21.5 | 20/22.5 | 21/23.5 | 22/24.5 |
| Headline | Semibold | Semibold | 14/16.5 | 15/17.5 | 16/18.5 | 17/19.5 | 18/20.5 | 19/21.5 |
| Body | Regular | Semibold | 14/16.5 | 15/17.5 | 16/18.5 | 17/19.5 | 18/20.5 | 19/21.5 |
| Caption 1 | Regular | Semibold | 13/15.5 | 14/16.5 | 15/17.5 | 16/18.5 | 17/19.5 | 18/20.5 |
| Caption 2 | Regular | Semibold | 12/14.5 | 13/15.5 | 14/16.5 | 15/17.5 | 16/18.5 | 17/19.5 |
| Footnote 1 | Regular | Semibold | 11/13.5 | 12/14.5 | 13/15.5 | 14/16.5 | 15/17.5 | 16/18.5 |
| Footnote 2 | Regular | Semibold | 10/12.5 | 11/13.5 | 12/14.5 | 13/15.5 | 14/16.5 | 15/17.5 |

### watchOS – Larger Accessibility Type Sizes (Größe/Leading in pt)

| Style | Weight | Emph. | AX1 | AX2 | AX3 |
|---|---|---|---|---|---|
| Large Title | Regular | Bold | 44/46.5 | 45/47.5 | 46/48.5 |
| Title 1 | Regular | Semibold | 42/44.5 | 43/46 | 44/47 |
| Title 2 | Regular | Semibold | 34/41 | 35/37.5 | 36/38.5 |
| Title 3 | Regular | Semibold | 24/26.5 | 25/27.5 | 26/28.5 |
| Headline | Semibold | Semibold | 21/23.5 | 22/24.5 | 23/25.5 |
| Body | Regular | Semibold | 21/23.5 | 22/24.5 | 23/25.5 |
| Caption 1 | Regular | Semibold | 18/20.5 | 19/21.5 | 20/22.5 |
| Caption 2 | Regular | Semibold | 17/19.5 | 18/20.5 | 19/21.5 |
| Footnote 1 | Regular | Semibold | 16/18.5 | 17/19.5 | 18/20.5 |
| Footnote 2 | Regular | Semibold | 15/17.5 | 16/17.5 | 17/19.5 |

Hinweis watchOS: Reihenfolge der Styles weicht von iOS ab (Caption vor Footnote; Footnote 1/2 statt Footnote/Subhead/Callout).

### Tracking (1/1000 em / pt)

SF Pro gilt für iOS, iPadOS, visionOS; macOS und tvOS haben eigene, nahezu identische Tabellen. SF Compact (Rounded) gilt für watchOS. „–“ = für diese Größe kein Wert im Spiegel. Nicht jedes Tool rechnet in 1/1000 em. (hig:typography#Tracking-values)

| pt | SF Pro | SF Pro Rounded | New York | SF Compact | SF Compact Rounded |
|---|---|---|---|---|---|
| 6 | +41 / +0.24 | +87 / +0.51 | +40 / +0.23 | +50 / +0.29 | +28 / +0.16 |
| 7 | +34 / +0.23 | +80 / +0.54 | +32 / +0.22 | +30 / +0.21 | +26 / +0.18 |
| 8 | +26 / +0.21 | +72 / +0.57 | +25 / +0.20 | +30 / +0.23 | +24 / +0.19 |
| 9 | +19 / +0.17 | +65 / +0.57 | +20 / +0.18 | +30 / +0.26 | +22 / +0.19 |
| 10 | +12 / +0.12 | +58 / +0.57 | +16 / +0.15 | +30 / +0.29 | +20 / +0.20 |
| 11 | +6 / +0.06 | +52 / +0.56 | +11 / +.12 | +24 / +0.26 | +18 / +0.19 |
| 12 | 0 / 0.0 | +46 / +0.54 | +6 / +0.07 | +20 / +0.23 | +16 / +0.19 |
| 13 | -6 / -0.08 | +40 / +0.51 | +4 / +0.05 | +16 / +0.20 | +14 / +0.18 |
| 14 | -11 / -0.15 | +35 / +0.48 | +2 / +0.03 | +14 / +0.19 | +12 / +0.16 |
| 15 | -16 / -0.23 | +30 / +0.44 | +0 / +0.00 | +4 / +0.06 | +10 / +0.15 |
| 16 | -20 / -0.31 | +26 / +0.41 | -2 / -0.03 | 0 / 0.00 | +8 / +0.12 |
| 17 | -26 / -0.43 | +22 / +0.37 | -4 / -0.07 | -4 / -0.07 | +6 / +0.10 |
| 18 | -25 / -0.44 | +21 / +0.37 | -6 / -0.11 | -8 / -0.14 | +4 / +0.07 |
| 19 | -24 / -0.45 | +20 / +0.37 | -8 / -0.15 | -12 / -0.22 | +2 / +0.04 |
| 20 | -23 / -0.45 | +18 / +0.36 | -10 / -0.20 | 0 / 0.00 | 0 / 0.00 |
| 21 | -18 / -0.36 | +17 / +0.35 | -10 / -0.21 | -2 / -0.04 | -2 / -0.04 |
| 22 | -12 / -0.26 | +16 / +0.34 | -10 / -0.23 | -4 / -0.09 | -4 / -0.09 |
| 23 | -4 / -0.10 | +16 / +0.35 | -11 / -0.25 | -6 / -0.13 | -6 / -0.13 |
| 24 | +3 / +0.07 | +15 / +0.35 | -11 / -0.26 | -8 / -0.19 | -8 / -0.19 |
| 25 | +6 / +0.15 | +14 / +0.35 | -11 / -0.27 | -10 / -0.24 | -10 / -0.24 |
| 26 | +8 / +0.22 | +14 / +0.36 | -12 / -0.29 | -11 / -0.28 | -11 / -0.28 |
| 27 | +11 / +0.29 | +14 / +0.36 | -12 / -0.32 | -12 / -0.30 | -12 / -0.30 |
| 28 | +14 / +0.38 | +13 / +0.36 | -12 / -0.33 | -12 / -0.34 | -12 / -0.34 |
| 29 | +14 / +0.40 | +13 / +0.37 | -12 / -0.34 | -14 / -0.38 | -14 / -0.38 |
| 30 | +14 / +0.40 | +12 / +0.37 | -12 / -0.37 | -14 / -0.42 | -14 / -0.42 |
| 31 | +13 / +0.39 | +12 / +0.36 | -13 / -0.39 | -15 / -0.45 | -15 / -0.45 |
| 32 | +13 / +0.41 | +12 / +0.38 | -13 / -0.41 | -16 / -0.50 | -16 / -0.50 |
| 33 | +12 / +0.40 | +12 / +0.39 | -13 / -0.42 | -17 / -0.55 | -17 / -0.55 |
| 34 | +12 / +0.40 | +12 / +0.38 | -14 / -0.45 | -18 / -0.60 | -18 / -0.60 |
| 35 | +11 / +0.38 | +11 / +0.38 | -14 / -0.48 | -18 / -0.63 | -18 / -0.63 |
| 36 | +10 / +0.37 | +11 / +0.39 | -14 / -0.49 | -20 / -0.69 | -20 / -0.69 |
| 37 | +10 / +0.36 | +10 / +0.38 | – | -20 / -0.72 | -20 / -0.72 |
| 38 | +10 / +0.37 | +10 / +0.39 | -14 / -0.52 | -20 / -0.74 | -20 / -0.74 |
| 39 | +10 / +0.38 | +10 / +0.38 | – | -20 / -0.76 | -20 / -0.76 |
| 40 | +10 / +0.37 | +10 / +0.39 | -14 / -0.55 | -20 / -0.78 | -20 / -0.78 |
| 41 | +9 / +0.36 | +10 / +0.38 | – | -20 / -0.80 | -20 / -0.80 |
| 42 | +9 / +0.37 | +10 / +0.39 | -14 / -0.57 | -20 / -0.82 | -20 / -0.82 |
| 43 | +9 / +0.38 | +9 / +0.38 | – | -20 / -0.84 | -20 / -0.84 |
| 44 | +8 / +0.37 | +8 / +0.37 | -14 / -0.62 | -20 / -0.86 | -20 / -0.86 |
| 45 | +8 / +0.35 | +8 / +0.37 | – | -20 / -0.88 | -20 / -0.88 |
| 46 | +8 / +0.36 | +8 / +0.36 | -14 / -0.65 | -20 / -0.92 | -20 / -0.92 |
| 47 | +8 / +0.37 | +8 / +0.37 | – | -20 / -0.94 | -20 / -0.94 |
| 48 | +8 / +0.35 | +8 / +0.35 | -14 / -0.68 | -20 / -0.96 | -20 / -0.96 |
| 49 | +7 / +0.33 | +8 / +0.36 | – | -21 / -1.00 | -21 / -1.00 |
| 50 | +7 / +0.34 | +7 / +0.34 | -14 / -0.71 | -21 / -1.03 | -21 / -1.03 |
| 51 | +7 / +0.35 | +6 / +0.32 | – | -21 / -1.05 | -21 / -1.05 |
| 52 | +6 / +0.33 | +6 / +0.33 | -14 / -0.74 | -21 / -1.07 | -21 / -1.07 |
| 53 | +6 / +0.31 | +6 / +0.31 | – | -22 / -1.11 | -22 / -1.11 |
| 54 | +6 / +0.32 | +6 / +0.32 | -15 / -0.79 | -22 / -1.13 | -22 / -1.13 |
| 56 | +6 / +0.30 | +6 / +0.30 | – | -22 / -1.20 | -22 / -1.20 |
| 58 | +5 / +0.28 | +4 / +0.25 | -15 / -0.85 | -22 / -1.25 | -22 / -1.25 |
| 60 | +4 / +0.26 | +4 / +0.23 | – | -22 / -1.32 | -22 / -1.32 |
| 62 | +4 / +0.24 | +4 / +0.21 | -15 / -0.91 | -22 / -1.36 | -22 / -1.36 |
| 64 | +4 / +0.22 | +3 / +0.19 | – | -23 / -1.44 | -23 / -1.44 |
| 66 | +3 / +0.19 | +2 / +0.16 | -15 / -0.97 | -24 / -1.51 | -24 / -1.51 |
| 68 | +2 / +0.17 | +2 / +0.13 | – | -24 / -1.56 | -24 / -1.56 |
| 70 | +2 / +0.14 | +2 / +0.14 | -16 / -1.06 | -24 / -1.64 | -24 / -1.64 |
| 72 | +2 / +0.14 | +2 / +0.11 | -16 / -1.09 | -24 / -1.69 | -24 / -1.69 |
| 76 | +1 / +0.07 | +1 / +0.07 | – | -25 / -1.86 | -25 / -1.86 |
| 80 | 0 / 0 | 0 / 0.00 | -16 / -1.21 | -26 / -1.99 | -26 / -1.99 |
| 84 | 0 / 0 | 0 / 0.00 | – | -26 / -2.13 | -26 / -2.13 |
| 88 | 0 / 0 | 0 / 0.00 | -16 / -1.33 | -26 / -2.28 | -26 / -2.28 |
| 92 | 0 / 0 | 0 / 0.00 | – | -28 / -2.47 | -28 / -2.47 |
| 96 | 0 / 0 | 0 / 0.00 | -16 / -1.50 | -28 / -2.62 | -28 / -2.62 |

New York zusätzlich (größere Größen): 100 pt −16/−1.56 · 120 pt −16/−1.88 · 140 pt −16/−2.26 · 160 pt −16/−2.58 · 180 pt −17/−2.99 · 200 pt −17/−3.32 · 220 pt −18/−3.76 · 240 pt −18/−4.22 · 260 pt −18/−4.57.

## Plattform-Unterschiede

- **iOS/iPadOS:** SF Pro + NY, voller Dynamic-Type-Umfang (7 Standard- + 5 AX-Stufen). (hig:typography#iOS-iPadOS)
- **macOS:** Kein Dynamic Type. Für Text, der wie System-Controls aussehen soll, die dynamischen Font-Varianten von `NSFont` nutzen: (hig:typography#macOS)

| Variante | AppKit-API |
|---|---|
| Control content | `controlContentFont(ofSize:)` |
| Label | `labelFont(ofSize:)` |
| Menu | `menuFont(ofSize:)` |
| Menu bar | `menuBarFont(ofSize:)` |
| Message | `messageFont(ofSize:)` |
| Palette | `paletteFont(ofSize:)` |
| Title | `titleBarFont(ofSize:)` |
| Tool tips | `toolTipsFont(ofSize:)` |
| Document text | `userFont(ofSize:)` |
| Monospaced document text | `userFixedPitchFont(ofSize:)` |
| Bold system font | `boldSystemFont(ofSize:)` |
| System font | `systemFont(ofSize:)` |

- **watchOS:** SF Compact, Complications in SF Compact Rounded; 6 Standard- + 3 AX-Stufen; Default-Stufe hängt von der Gehäusegröße ab. (hig:typography#watchOS)
- **visionOS (Rand):** 2D-Text bevorzugen, Kontrast zum Glass-Hintergrund maximieren, Text ohne Hintergrund eher bold statt mit Schatten, an Raumpunkte gebundene Labels per Billboarding zum Nutzer drehen. (hig:typography#visionOS)

## Umsetzung

> API-Zuordnung SwiftUI/UIKit: Die HIG nennt die Style-Namen, nicht jede API-Konstante. Die Zuordnung unten ist etabliertes Framework-Wissen, nicht aus dem Spiegel belegt.

| HIG-Style | SwiftUI `Font` | UIKit `UIFont.TextStyle` |
|---|---|---|
| Large Title | `.largeTitle` | `.largeTitle` |
| Title 1 | `.title` | `.title1` |
| Title 2 | `.title2` | `.title2` |
| Title 3 | `.title3` | `.title3` |
| Headline | `.headline` | `.headline` |
| Subhead(line) | `.subheadline` | `.subheadline` |
| Body | `.body` | `.body` |
| Callout | `.callout` | `.callout` |
| Footnote | `.footnote` | `.footnote` |
| Caption 1 | `.caption` | `.caption1` |
| Caption 2 | `.caption2` | `.caption2` |

**SwiftUI**
```swift
Text("Inbox").font(.largeTitle)
Text(subject).font(.headline)
Text(preview).font(.body).leading(.loose)          // Symbolic Trait Leading (hig: leading(_:))
Text("Wichtig").font(.body).bold()                  // Emphasized Weight
Text("Zitat").font(.system(.body, design: .serif))  // New York via Font.Design.serif
Text(code).font(.system(.body, design: .monospaced))
// Custom Font mit Dynamic Type (relativeTo koppelt an einen Text Style)
Text(title).font(.custom("BrandSerif", size: 17, relativeTo: .body))
```
- Bei großen Größen Layout umbauen: `@Environment(\.dynamicTypeSize)` und `.isAccessibilitySize` → `HStack` zu `VStack`; `ViewThatFits` als Alternative.
- Abstände/Icongrößen mitskalieren: `@ScaledMetric`.

**UIKit**
```swift
label.font = UIFont.preferredFont(forTextStyle: .body)
label.adjustsFontForContentSizeCategory = true
label.numberOfLines = 0                                   // Truncation vermeiden (hig: numberOfLines)
let custom = UIFontMetrics(forTextStyle: .body).scaledFont(for: UIFont(name: "Brand", size: 17)!)
if traitCollection.preferredContentSizeCategory.isAccessibilityCategory { /* gestapeltes Layout */ }
```

**AppKit:** `NSFont.preferredFont(forTextStyle:)` für die macOS-Text-Styles, sonst die `NSFont`-Varianten aus der Tabelle oben.

**Unity:** Dynamic Type über Apples Unity-Plug-ins; sonst eigene Textgrößen-Einstellung anbieten. (hig:typography#Using-custom-fonts)

## Review-Checkliste

- [ ] Fließtext ≥ Standardgröße, kein Text unter der Plattform-Mindestgröße
- [ ] Keine Ultralight/Thin/Light-Schnitte in kleinen Größen
- [ ] Höchstens wenige Schriftfamilien; Hierarchie über Text Styles, nicht über Ad-hoc-Größen
- [ ] Alle Texte nutzen Text Styles bzw. skalierende Custom Fonts (`relativeTo:` / `UIFontMetrics`)
- [ ] Bold Text (Bedienungshilfe) wirkt auch bei Custom Fonts
- [ ] Bei AX5 (iOS) bzw. AX3 (watchOS) getestet: keine Überlappung, minimale Truncation, Primärinhalt oben
- [ ] Horizontale Layouts stapeln bei Accessibility-Größen; Spaltenzahl reduziert
- [ ] Bedeutungstragende Icons skalieren mit (SF Symbols)
- [ ] Kein Tight Leading bei ≥ 3 Zeilen
- [ ] Systemschriften nicht eingebettet; NY/Mono über `Font.Design`
- [ ] macOS: Control-nahe Texte über `NSFont`-Varianten; Headline-Gewicht Bold berücksichtigt
- [ ] Mockups: Tracking gemäß Tabelle gesetzt

## Anti-Patterns

- Feste Punktgrößen (`.system(size: 15)`) für Fließtext → kein Dynamic Type.
- Alles skaliert gleichermaßen mit, auch Tab-Titel und Chrome, statt Inhalt zu priorisieren.
- `numberOfLines = 1` + Truncation in scrollbaren Bereichen ohne Möglichkeit, den Volltext zu sehen.
- Eigene Schrift ohne Bold-Text- und Dynamic-Type-Unterstützung.
- Sieben verschiedene Schriftarten zur „Markenbildung“.
- Hierarchie nur über Größe, die bei großen Textstufen kollabiert.
- Hervorhebung über Light-Schnitt oder extrem enges Tracking.
- 3D-Text oder Schlagschatten für Lesetext in visionOS.

## Auffälligkeiten im Spiegel

- watchOS AX1, Title 2: Leading **41** bei Größe 34 – bricht das sonst durchgängige Muster (Leading = Größe + 2,5 bzw. +2/+3). Vermutlich Quellfehler; Wert unverändert übernommen.
- watchOS AX2, Footnote 2: Leading **17.5** bei Größe 16 (Muster ließe 18.5 erwarten). Unverändert übernommen.
- Tracking 52/53 pt: iOS-Tabelle +0.33/+0.31, macOS- und tvOS-Tabellen +0.31/+0.33 (vertauscht). Beide Varianten im Spiegel; 1/1000-em-Wert (+6) identisch.
- New York 11 pt: Quelle schreibt „+.12“ (= +0.12).
- Font-Familien-Tabelle: Für SF Mono enthält der Spiegel keine Spezifikation.
