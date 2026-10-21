# Typography

> Source: local HIG mirror `~/.apple-design/hig/pages/typography.md` (mirrored 2026-10-21, Apple update 2025-12-16: Emphasized Weights added). Supplementary: `accessibility`, `layout`, `sf-symbols`. Content paraphrased; specification tables taken over as facts.

## Overview

On Apple platforms, typography serves three purposes: legibility, information hierarchy and (sparingly) brand expression. The system fonts (San Francisco, New York) and the system-defined **text styles** are the default – they come with Dynamic Type, Bold Text, optical sizes and tracking built in. Custom fonts are allowed, but must replicate these behaviors themselves.

## Core rules

- Use at least the minimum size per platform, and the default size for body text (table below); choose larger sizes for thin custom weights. (hig:typography#Ensuring-legibility)
- Avoid Ultralight, Thin and Light – especially at small sizes; prefer Regular, Medium, Semibold, Bold. (hig:typography#Ensuring-legibility)
- Test legibility in the real context (distance, lighting, game overlays); if there are problems, increase size or contrast. (hig:typography#Ensuring-legibility)
- Build hierarchy through weight, size and color – and preserve this hierarchy when the text size changes. (hig:typography#Conveying-hierarchy)
- Keep the number of typefaces minimal, even in highly customized UIs. (hig:typography#Conveying-hierarchy)
- When scaling, prioritize the content people actually want to read (e.g. dialogue rather than tab titles or transient damage numbers). (hig:typography#Conveying-hierarchy)
- Use the built-in text styles; they provide Dynamic Type and accessibility sizes. (hig:typography#Using-system-fonts)
- Modify text styles via symbolic traits (Bold, Loose/Tight Leading) instead of inventing your own sizes; no tight leading for three or more lines. (hig:typography#Using-system-fonts)
- Don't embed system fonts in the app – access them via `Font.Design` (`.default` = SF, `.serif` = New York). (hig:typography#Using-system-fonts)
- Adjust tracking in mockups where needed (tracking table below); at runtime the system handles this. (hig:typography#Tracking-values)
- Custom fonts: ensure legibility and support Dynamic Type and Bold Text yourself. (hig:typography#Using-custom-fonts)
- The layout must accommodate all text sizes including Larger Accessibility Sizes; test on device (Settings > Accessibility > Display & Text Size > Larger Text). (hig:typography#Supporting-Dynamic-Type)
- Scale meaningful icons with the font (SF Symbols do this automatically). (hig:typography#Supporting-Dynamic-Type)
- Minimize truncation at large sizes; goal: at the largest AX size, as much useful text as at the largest standard size. Allow multiline labels. (hig:typography#Supporting-Dynamic-Type)
- At large sizes, switch to stacked layouts (text above secondary elements) and reduce columns. (hig:typography#Supporting-Dynamic-Type)
- Keep primary elements at the top of the view, even with very large text. (hig:typography#Supporting-Dynamic-Type)
- Design layouts so that side-by-side views stack vertically at large text sizes and rows grow in height. (hig:layout#Adaptability)

## Specifications

### Default and minimum sizes (hig:typography#Ensuring-legibility)

| Platform | Default size | Minimum size |
|---|---|---|
| iOS, iPadOS | 17 pt | 11 pt |
| macOS | 13 pt | 10 pt |
| tvOS | 29 pt | 23 pt |
| visionOS | 17 pt | 12 pt |
| watchOS | 16 pt | 12 pt |

### System fonts (hig:typography#Using-system-fonts)

| Family | Character | Variants / notes |
|---|---|---|
| San Francisco (SF) | Sans serif | SF Pro, SF Compact, SF Arabic, SF Armenian, SF Georgian, SF Hebrew, SF Mono |
| SF Rounded | rounded variant | for SF Pro, SF Compact, SF Arabic, SF Armenian, SF Georgian, SF Hebrew |
| New York (NY) | Serif | can be used alone or combined with SF |

- Both families are available as **variable fonts**; the system uses **dynamic optical sizes** (Text/Display interpolated continuously). Discrete optical sizes are only needed in tools without variable-font support.
- Weights from Ultralight to Black; SF additionally in widths (including Condensed, Expanded). SF Symbols have equivalent weights → set symbol and text in matching weights.
- SF Mono is part of the SF family; the mirror lists no separate size/tracking values for SF Mono.

| Platform | System font | NY | Dynamic Type |
|---|---|---|---|
| iOS, iPadOS | SF Pro | yes | yes |
| macOS | SF Pro | mentioned only for Mac Catalyst apps | **no** |
| watchOS | SF Compact (complications: SF Compact Rounded) | yes | yes |
| tvOS | SF Pro | yes | yes |
| visionOS | SF Pro (bolder Body/Title variants, plus Extra Large Title 1/2) | yes, specify text styles explicitly | yes |

### Emphasized Weights

Emphasized variants of the text styles are created via symbolic traits (SwiftUI `bold()`, UIKit `traitBold` in `UIFontDescriptor`). Possible emphasized weights: Medium, Semibold, Bold, Heavy. The tables list the emphasized weight for each style. (hig:typography#Specifications)

### iOS/iPadOS Dynamic Type – standard sizes (size/leading in pt; default = Large)

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

Point sizes based on 144 ppi (@2x) and 216 ppi (@3x) respectively. (hig:typography#Specifications)

### iOS/iPadOS – Larger Accessibility Type Sizes (size/leading in pt)

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

### macOS – built-in text styles (no Dynamic Type; size/line height in pt)

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

Based on 144 ppi (@2x). Note: on macOS, Headline is Bold (iOS: Semibold) and Caption 2 is Medium.

### watchOS Dynamic Type – standard sizes (size/leading in pt)

Defaults according to the mirror: Small = 38 mm, Large = 40/41/42 mm, xLarge = 44/45/49 mm.

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

### watchOS – Larger Accessibility Type Sizes (size/leading in pt)

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

Note on watchOS: the order of styles differs from iOS (Caption before Footnote; Footnote 1/2 instead of Footnote/Subhead/Callout).

### Tracking (1/1000 em / pt)

SF Pro applies to iOS, iPadOS, visionOS; macOS and tvOS have their own, nearly identical tables. SF Compact (Rounded) applies to watchOS. "–" = no value in the mirror for this size. Not every tool works in 1/1000 em. (hig:typography#Tracking-values)

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

New York additionally (larger sizes): 100 pt −16/−1.56 · 120 pt −16/−1.88 · 140 pt −16/−2.26 · 160 pt −16/−2.58 · 180 pt −17/−2.99 · 200 pt −17/−3.32 · 220 pt −18/−3.76 · 240 pt −18/−4.22 · 260 pt −18/−4.57.

## Platform differences

- **iOS/iPadOS:** SF Pro + NY, full Dynamic Type range (7 standard + 5 AX sizes). (hig:typography#iOS-iPadOS)
- **macOS:** No Dynamic Type. For text that should look like system controls, use the dynamic font variants of `NSFont`: (hig:typography#macOS)

| Variant | AppKit API |
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

- **watchOS:** SF Compact, complications in SF Compact Rounded; 6 standard + 3 AX sizes; the default size depends on the case size. (hig:typography#watchOS)
- **visionOS (peripheral):** Prefer 2D text, maximize contrast against the glass background, make text without a background bold rather than adding shadows, rotate labels anchored to points in space toward the user via billboarding. (hig:typography#visionOS)

## Implementation

> SwiftUI/UIKit API mapping: the HIG names the styles, not every API constant. The mapping below is established framework knowledge, not sourced from the mirror.

| HIG style | SwiftUI `Font` | UIKit `UIFont.TextStyle` |
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
Text(preview).font(.body).leading(.loose)          // Symbolic trait leading (hig: leading(_:))
Text("Important").font(.body).bold()                // Emphasized weight
Text("Quote").font(.system(.body, design: .serif))  // New York via Font.Design.serif
Text(code).font(.system(.body, design: .monospaced))
// Custom font with Dynamic Type (relativeTo ties it to a text style)
Text(title).font(.custom("BrandSerif", size: 17, relativeTo: .body))
```
- Restructure the layout at large sizes: `@Environment(\.dynamicTypeSize)` and `.isAccessibilitySize` → `HStack` to `VStack`; `ViewThatFits` as an alternative.
- Scale spacing/icon sizes along with text: `@ScaledMetric`.

**UIKit**
```swift
label.font = UIFont.preferredFont(forTextStyle: .body)
label.adjustsFontForContentSizeCategory = true
label.numberOfLines = 0                                   // Avoid truncation (hig: numberOfLines)
let custom = UIFontMetrics(forTextStyle: .body).scaledFont(for: UIFont(name: "Brand", size: 17)!)
if traitCollection.preferredContentSizeCategory.isAccessibilityCategory { /* stacked layout */ }
```

**AppKit:** `NSFont.preferredFont(forTextStyle:)` for the macOS text styles, otherwise the `NSFont` variants from the table above.

**Unity:** Dynamic Type via Apple's Unity plug-ins; otherwise offer your own text size setting. (hig:typography#Using-custom-fonts)

## Review checklist

- [ ] Body text ≥ default size, no text below the platform minimum size
- [ ] No Ultralight/Thin/Light weights at small sizes
- [ ] At most a few typefaces; hierarchy via text styles, not ad-hoc sizes
- [ ] All text uses text styles or scaling custom fonts (`relativeTo:` / `UIFontMetrics`)
- [ ] Bold Text (accessibility setting) also takes effect with custom fonts
- [ ] Tested at AX5 (iOS) or AX3 (watchOS): no overlap, minimal truncation, primary content at the top
- [ ] Horizontal layouts stack at accessibility sizes; number of columns reduced
- [ ] Meaningful icons scale along (SF Symbols)
- [ ] No tight leading for ≥ 3 lines
- [ ] System fonts not embedded; NY/Mono via `Font.Design`
- [ ] macOS: control-related text via `NSFont` variants; Bold Headline weight taken into account
- [ ] Mockups: tracking set according to the table

## Anti-patterns

- Fixed point sizes (`.system(size: 15)`) for body text → no Dynamic Type.
- Everything scales equally, including tab titles and chrome, instead of prioritizing content.
- `numberOfLines = 1` + truncation in scrollable areas with no way to see the full text.
- Custom font without Bold Text and Dynamic Type support.
- Seven different typefaces for "branding".
- Hierarchy based on size alone, which collapses at large text sizes.
- Emphasis via a Light weight or extremely tight tracking.
- 3D text or drop shadows for reading text in visionOS.

## Anomalies in the mirror

- watchOS AX1, Title 2: leading **41** at size 34 – breaks the otherwise consistent pattern (leading = size + 2.5, or +2/+3). Probably a source error; value taken over unchanged.
- watchOS AX2, Footnote 2: leading **17.5** at size 16 (the pattern would suggest 18.5). Taken over unchanged.
- Tracking 52/53 pt: iOS table +0.33/+0.31, macOS and tvOS tables +0.31/+0.33 (swapped). Both variants are in the mirror; the 1/1000 em value (+6) is identical.
- New York 11 pt: the source writes "+.12" (= +0.12).
- Font family table: the mirror contains no specification for SF Mono.
