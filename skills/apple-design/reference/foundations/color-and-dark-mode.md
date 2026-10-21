# Farbe und Dark Mode

> Quelle: HIG-Spiegel `color.md` (Apple-Update 2025-12-16, Liquid Glass), `dark-mode.md` (2024-08-06), ergänzend `accessibility`, `materials`, `buttons`, `toolbars`, `tab-bars`, `sidebars`, `branding`, `widgets`. Gespiegelt 2026-10-21. Paraphrasiert; Farbwerte als Fakten übernommen.

## Einordnung

Farbe kommuniziert Status, Interaktivität und Marke – aber nur, wenn sie konsistent und sparsam eingesetzt wird. Auf Apple-Plattformen ist der Normalfall: **semantische, dynamische Systemfarben**, die sich automatisch an Light/Dark, Increase Contrast, Vibrancy und Liquid Glass anpassen. Eigene Farben brauchen immer vier Varianten (Light, Dark, je + Increased Contrast). Dark Mode ist eine systemweite Einstellung, die Apps respektieren müssen – keine App-eigene Umschaltung.

## Kernregeln

### Allgemein
- Verwende eine Farbe nie für zwei Bedeutungen (z. B. Markenfarbe für interaktive Buttons **und** für nicht-interaktiven Text). (hig:color#Best-practices)
- Stelle sicher, dass jede Farbe in Light, Dark und Increased Contrast funktioniert; Custom Colors mit Light/Dark-Variante und je einer deutlich kontrastreicheren Increased-Contrast-Variante anlegen. (hig:color#Best-practices)
- Liefere Light- **und** Dark-Varianten auch dann, wenn die App nur ein Erscheinungsbild nutzt – Liquid Glass passt sich sonst nicht korrekt an. (hig:color#Best-practices)
- Teste unter verschiedenen Lichtverhältnissen und auf verschiedenen Geräten (True Tone, P3/sRGB-Profile am Mac). (hig:color#Best-practices)
- Berücksichtige, wie Artwork und Transluzenz benachbarte Farben verändern. (hig:color#Best-practices)
- Nutze für Farbauswahl durch Nutzer den System-Color-Picker (`ColorPicker`). (hig:color#Best-practices)

### Inklusiv
- Transportiere Information nie nur über Farbe – zusätzlich Text, Form oder Symbol. (hig:color#Inclusive-color)
- Vermeide Kombinationen mit zu wenig Kontrast oder die für Farbfehlsichtige ununterscheidbar sind. (hig:color#Inclusive-color)
- Prüfe kulturelle Farbbedeutungen (z. B. Rot). (hig:color#Inclusive-color)

### Systemfarben
- Hartkodiere keine Systemfarbwerte; die Tabellenwerte sind Design-Referenz und können sich je Release ändern. Über APIs (`Color`, `UIColor`, `NSColor`) referenzieren. (hig:color#System-colors)
- Missbrauche keine semantischen Farben (z. B. `separator` nicht als Textfarbe, `secondaryLabel` nicht als Hintergrund). (hig:color#System-colors)

### Liquid Glass color
- Liquid Glass ist standardmäßig farblos und übernimmt Farbe vom Inhalt dahinter. Färbung („stained glass“) nur für echte Betonung, z. B. Primäraktion oder Status. (hig:color#Liquid-Glass-color)
- Für Primäraktionen den **Hintergrund** einfärben, nicht Symbol/Text – so macht es das System bei prominenten Buttons (z. B. Done) mit der Akzentfarbe. Nicht mehrere Controls farbig hinterlegen. (hig:color#Liquid-Glass-color)
- Bei farbigem Content: monochrome Toolbars/Tab Bars bevorzugen oder eine klar unterscheidbare Akzentfarbe wählen; bei monochromem Content ist die Markenfarbe als Akzent sinnvoll. (hig:color#Liquid-Glass-color, hig:toolbars#Best-practices, hig:tab-bars#Best-practices, hig:buttons#Style)
- Achte auf die Ruhelage: ähnliche Farben im Content-Layer und in Controls nicht überlappen lassen; mindestens der Startzustand (Scroll-Anfang) muss klar lesbar sein. (hig:color#Liquid-Glass-color)
- Kleine Glass-Elemente (Toolbar, Tab Bar) wechseln adaptiv zwischen hell/dunkel; Symbole/Text darauf sind standardmäßig monochrom. Große Elemente (Sidebar) sind opaker. (hig:color#Liquid-Glass-color)

### Akzentfarbe / Tint
- Setze die Akzentfarbe gezielt ein: Primäraktionen, Statusindikatoren (z. B. Badges), ausgewähltes Tab-Icon – nicht flächig auf allen Controls. (hig:branding)
- Marke lieber in den Content-Layer verlagern, wo sie unter Liquid Glass durchscheint. (hig:branding)
- Toolbar-Hintergründe und getönte Controls reduzieren; Farbe aus dem Content ableiten. (hig:toolbars#Best-practices)
- Prominente Buttons: höchstens ein bis zwei pro View; destruktive Rolle nutzt System-Rot, primäre Rolle die Akzentfarbe. (hig:buttons#Style, hig:buttons#Role)
- macOS: Die App-Akzentfarbe gilt nur, wenn der Nutzer „Multicolor“ eingestellt hat; sonst überschreibt die gewählte Systemakzentfarbe sie – außer bei Sidebar-Icons mit bewusst fixer Farbe. (hig:color#App-accent-colors, hig:sidebars#Best-practices)

### Kontrast
- Mindestkontrast 4.5:1; für eigene Vorder-/Hintergrundfarben 7:1 anstreben, besonders bei kleinem Text. (hig:dark-mode#Dark-Mode-colors)
- Accessibility Inspector prüft nach folgender Tabelle; falls der Default sie nicht erfüllt, mindestens bei Increase Contrast ein kontrastreicheres Schema liefern. (hig:accessibility)

| Textgröße | Gewicht | Mindestkontrast |
|---|---|---|
| bis 17 pt | alle | 4.5:1 |
| 18 pt | alle | 3:1 |
| alle | Bold | 3:1 |

Widerspruch: `dark-mode` nennt pauschal „mindestens 4.5:1“, `accessibility` erlaubt 3:1 ab 18 pt bzw. bei Bold. Für Fließtext 4.5:1 als Untergrenze verwenden, 3:1 nur für großen/fetten Text.

### Dark Mode
- Biete keine app-eigene Hell/Dunkel-Einstellung an; respektiere die Systemeinstellung (inkl. „Automatisch“, die während der Laufzeit umschalten kann). (hig:dark-mode#Best-practices)
- Teste in Dark Mode mit Increase Contrast und Reduce Transparency – einzeln und kombiniert. (hig:dark-mode#Best-practices)
- Nur in Ausnahmefällen (immersive Medien) dauerhaft dunkel. (hig:dark-mode#Best-practices)
- Dark-Mode-Farben sind keine simple Invertierung: dunklere Hintergründe, hellere Vordergründe. (hig:dark-mode#Dark-Mode-colors)
- Custom Colors als Color Set im Asset Catalog mit hell/dunkel-Variante anlegen. (hig:dark-mode#Dark-Mode-colors)
- Weiße Bildhintergründe leicht abdunkeln, damit sie nicht „glühen“. (hig:dark-mode#Dark-Mode-colors)
- SF Symbols verwenden; wo nötig getrennte Icons für hell/dunkel (z. B. Kontur nur im Light Mode). Full-Color-Assets in beiden Modi prüfen, ggf. Varianten im Asset Catalog. (hig:dark-mode#Icons-and-images)
- Für Labels die System-Label-Farben, für Textfelder/Textviews System-Views verwenden. (hig:dark-mode#Text)

## Kennwerte

### Systemfarben (SwiftUI; RGB, Hex umgerechnet) (hig:color#Specifications)

| Name | SwiftUI | Light | Dark | Increased Contrast Light | Increased Contrast Dark |
|---|---|---|---|---|---|
| Red | `red` | 255,56,60 (#FF383C) | 255,66,69 (#FF4245) | 233,21,45 (#E9152D) | 255,97,101 (#FF6165) |
| Orange | `orange` | 255,141,40 (#FF8D28) | 255,146,48 (#FF9230) | 197,83,0 (#C55300) | 255,160,86 (#FFA056) |
| Yellow | `yellow` | 255,204,0 (#FFCC00) | 255,214,0 (#FFD600) | 161,106,0 (#A16A00) | 254,223,67 (#FEDF43) |
| Green | `green` | 52,199,89 (#34C759) | 48,209,88 (#30D158) | 0,137,50 (#008932) | 74,217,104 (#4AD968) |
| Mint | `mint` | 0,200,179 (#00C8B3) | 0,218,195 (#00DAC3) | 0,133,117 (#008575) | 84,223,203 (#54DFCB) |
| Teal | `teal` | 0,195,208 (#00C3D0) | 0,210,224 (#00D2E0) | 0,129,152 (#008198) | 59,221,236 (#3BDDEC) |
| Cyan | `cyan` | 0,192,232 (#00C0E8) | 60,211,254 (#3CD3FE) | 0,126,174 (#007EAE) | 109,217,255 (#6DD9FF) |
| Blue | `blue` | 0,136,255 (#0088FF) | 0,145,255 (#0091FF) | 30,110,244 (#1E6EF4) | 92,184,255 (#5CB8FF) |
| Indigo | `indigo` | 97,85,245 (#6155F5) | 109,124,255 (#6D7CFF) | 86,74,222 (#564ADE) | 167,170,255 (#A7AAFF) |
| Purple | `purple` | 203,48,224 (#CB30E0) | 219,52,242 (#DB34F2) | 176,47,194 (#B02FC2) | 234,141,255 (#EA8DFF) |
| Pink | `pink` | 255,45,85 (#FF2D55) | 255,55,95 (#FF375F) | 231,18,77 (#E7124D) | 255,138,196 (#FF8AC4) |
| Brown | `brown` | 172,127,94 (#AC7F5E) | 183,138,102 (#B78A66) | 149,109,81 (#956D51) | 219,166,121 (#DBA679) |

visionOS verwendet die Dark-Werte. Laut Change Log wurden die Systemfarbwerte am 9. Juni 2025 aktualisiert – Werte aus älteren Referenzen nicht übernehmen.

### iOS/iPadOS System-Grautöne (UIKit) (hig:color#Specifications)

| Name | UIKit | Light | Dark | Increased Contrast Light | Increased Contrast Dark |
|---|---|---|---|---|---|
| Gray | `systemGray` | 142,142,147 (#8E8E93) | 142,142,147 (#8E8E93) | 108,108,112 (#6C6C70) | 174,174,178 (#AEAEB2) |
| Gray 2 | `systemGray2` | 174,174,178 (#AEAEB2) | 99,99,102 (#636366) | 142,142,147 (#8E8E93) | 124,124,128 (#7C7C80) |
| Gray 3 | `systemGray3` | 199,199,204 (#C7C7CC) | 72,72,74 (#48484A) | 174,174,178 (#AEAEB2) | 84,84,86 (#545456) |
| Gray 4 | `systemGray4` | 209,209,214 (#D1D1D6) | 58,58,60 (#3A3A3C) | 188,188,192 (#BCBCC0) | 68,68,70 (#444446) |
| Gray 5 | `systemGray5` | 229,229,234 (#E5E5EA) | 44,44,46 (#2C2C2E) | 216,216,220 (#D8D8DC) | 54,54,56 (#363638) |
| Gray 6 | `systemGray6` | 242,242,247 (#F2F2F7) | 28,28,30 (#1C1C1E) | 235,235,240 (#EBEBF0) | 36,36,38 (#242426) |

SwiftUI-Äquivalent zu `systemGray` ist `Color.gray`; für Gray 2–6 nennt der Spiegel kein SwiftUI-Pendant.

Nicht im Spiegel: konkrete RGB-Werte für semantische Farben (`label`, `systemBackground` …) – diese sind nur über APIs zu beziehen.

### Semantische Farben iOS/iPadOS (hig:color#iOS-iPadOS)

**Hintergründe** – zwei Sets mit je drei Ebenen (Primary = gesamter View, Secondary = Gruppierung darin, Tertiary = Gruppierung in Secondary):

| Kontext | Primary | Secondary | Tertiary |
|---|---|---|---|
| Standard | `systemBackground` | `secondarySystemBackground` | `tertiarySystemBackground` |
| Grouped Table View | `systemGroupedBackground` | `secondarySystemGroupedBackground` | `tertiarySystemGroupedBackground` |

**Vordergrund:**

| Farbe | Verwendung | UIKit |
|---|---|---|
| Label | Primärer Text | `label` |
| Secondary label | Sekundärer Text | `secondaryLabel` |
| Tertiary label | Tertiärer Text | `tertiaryLabel` |
| Quaternary label | Quartärer Text | `quaternaryLabel` |
| Placeholder text | Platzhalter in Controls/Textviews | `placeholderText` |
| Separator | Trenner, lässt Inhalt durchscheinen | `separator` |
| Opaque separator | Deckender Trenner | `opaqueSeparator` |
| Link | Text als Link | `link` |

Dark Mode iOS/iPadOS: Hintergründe existieren als **base** (dunkler, tritt zurück) und **elevated** (heller, tritt hervor, z. B. Popover, Sheet, Multitasking). Das System wechselt automatisch – daher Systemhintergründe statt eigener Farben verwenden. (hig:dark-mode#iOS-iPadOS)

### Semantische Farben macOS (AppKit `NSColor`) (hig:color#macOS)

| Zweck | API |
|---|---|
| Text Label (1–4) | `labelColor`, `secondaryLabelColor`, `tertiaryLabelColor`, `quaternaryLabelColor` |
| Dokumenttext / -hintergrund | `textColor`, `textBackgroundColor` |
| Platzhalter | `placeholderTextColor` |
| Link | `linkColor` |
| Fenster / unter Dokument | `windowBackgroundColor`, `underPageBackgroundColor` |
| Große Elemente (Browser, Tabelle) | `controlBackgroundColor` |
| Alternierende Zeilen | `alternatingContentBackgroundColors` |
| Control-Fläche / -Text / deaktiviert | `controlColor`, `controlTextColor`, `disabledControlTextColor` |
| Ausgewähltes Control / Text | `selectedControlColor`, `selectedControlTextColor`, `alternateSelectedControlTextColor` |
| Auswahl Inhalt (Key / Non-Key Window) | `selectedContentBackgroundColor`, `unemphasizedSelectedContentBackgroundColor` |
| Auswahl Text (Key / Non-Key) | `selectedTextBackgroundColor`, `selectedTextColor`, `unemphasizedSelectedTextBackgroundColor`, `unemphasizedSelectedTextColor` |
| Menü-Auswahltext | `selectedMenuItemTextColor` |
| Akzent / Tint | `controlAccentColor`, `currentControlTint` |
| Fokusring | `keyboardFocusIndicatorColor` |
| Suche-Hervorhebung | `findHighlightColor` |
| Raster, Trenner, Header | `gridColor`, `separatorColor`, `headerTextColor` |
| Licht / Schatten | `highlightColor`, `shadowColor` |
| Titelleiste | `windowFrameTextColor` |

macOS **Desktop Tinting** (bei Akzentfarbe Graphite): Fensterhintergründe übernehmen Farbe vom Schreibtischbild. Eigene Komponenten mit sichtbarem Hintergrund im **neutralen** Zustand leicht transparent machen, im farbigen Zustand nicht. (hig:dark-mode#macOS)

### Farbmanagement (hig:color#Color-management)
- Bildern Farbprofile zuweisen; sRGB ist für die meisten Displays korrekt.
- Wide Color (Display P3) für reichere Farben: P3-Profil, 16 Bit pro Kanal, Export als PNG; Gestaltung nur auf Wide-Color-Display.
- Bei sehr ähnlichen P3-Farben oder P3-Verläufen ggf. sRGB-Varianten im Asset Catalog hinterlegen.

## Plattform-Unterschiede

| Plattform | Besonderheiten |
|---|---|
| iOS/iPadOS | Zwei Hintergrund-Sets (system/grouped), base/elevated im Dark Mode, Liquid Glass passt sich Content an |
| macOS | Umfangreiche `NSColor`-Semantik, App-Akzent nur bei „Multicolor“, Desktop Tinting, vibrante Varianten aller Systemfarben |
| watchOS | Kein Dark Mode (dunkel by default). Hintergrundfarbe nur mit Aussage (Kontext, Orientierung), nicht dekorativ; keine Vollflächenfarbe in langlaufenden Views (Workout, Audio). Complications können im Tinted Mode einfarbig erscheinen. (hig:color#watchOS) |
| visionOS | Kein Dark Mode; Farben auf Glass sparsam, in fetter Schrift und großen Flächen; Systemfarben = Dark-Werte; Helligkeit in Immersion ausbalancieren. (hig:color#visionOS) |
| tvOS | Begrenzte Palette passend zum Logo; Fokus nicht nur über Farbe. (hig:color#tvOS) |

Widgets: Können full-color, getönt (accented) oder clear erscheinen; Bedeutung nie nur über Farbe, Elemente in Accent- und Primary-Gruppe aufteilen (`widgetAccentable`). (hig:widgets)

## Umsetzung

> Zuordnung UIKit/AppKit-Systemfarbnamen (`systemRed` …) und SwiftUI-Semantik (`.primary`, `.secondary`) ist Framework-Wissen, nicht im Spiegel belegt.

| Konzept | SwiftUI | UIKit | AppKit |
|---|---|---|---|
| Systemfarbe | `Color.red`, `.blue` … | `UIColor.systemRed` … | `NSColor.systemRed` … |
| Primärtext | `.foregroundStyle(.primary)` | `.label` | `.labelColor` |
| Sekundärtext | `.foregroundStyle(.secondary)` | `.secondaryLabel` | `.secondaryLabelColor` |
| Tertiär/Quartär | `.tertiary`, `.quaternary` | `.tertiaryLabel`, `.quaternaryLabel` | `.tertiaryLabelColor`, `.quaternaryLabelColor` |
| Hintergrund | `Color(uiColor: .systemBackground)` bzw. Standard-Container | `.systemBackground` | `.windowBackgroundColor` |
| Trenner | `Divider()` / `Color(uiColor: .separator)` | `.separator` | `.separatorColor` |
| Akzent | `.tint(_:)`, `Color.accentColor`, AccentColor im Asset Catalog | `tintColor` | `controlAccentColor` |
| Custom Color | Color Set (Any/Dark + High Contrast) im Asset Catalog | `UIColor(named:)` / `UIColor { traits in … }` | `NSColor(name:dynamicProvider:)` |

```swift
// Primäraktion: Hintergrund getönt, nicht der Text
Button("Fertig") { save() }
    .buttonStyle(.borderedProminent)       // System wendet Akzentfarbe auf Hintergrund an
Button("Löschen", role: .destructive) { delete() } // System-Rot über Rolle

// Erscheinungsbild abfragen, nicht erzwingen
@Environment(\.colorScheme) var scheme
@Environment(\.colorSchemeContrast) var contrast   // .increased bei Increase Contrast
```
- Kein `.preferredColorScheme(.dark)` als App-Option; nur für bewusst immer-dunkle Medienansichten.
- White-Point: Lese-/Foto-/Video-/Spiele-Apps können `UIWhitePointAdaptivityStyle` setzen. (hig:color#Best-practices)

## Review-Checkliste

- [ ] Keine hartkodierten RGB-/Hex-Werte für Systemfarben
- [ ] Jede Custom Color: Light, Dark, Increased Contrast Light/Dark
- [ ] Light- und Dark-Variante auch bei Single-Appearance-Apps (Liquid-Glass-Adaptivität)
- [ ] Semantische Farben gemäß Zweck verwendet (kein Separator als Text etc.)
- [ ] Information zusätzlich über Text/Form/Symbol, nicht nur Farbe
- [ ] Kontrast ≥ 4.5:1 (Fließtext), Ziel 7:1 für kleinen Custom-Text; 3:1 nur ≥ 18 pt oder Bold
- [ ] Getestet: Light, Dark, Increase Contrast, Reduce Transparency, Kombinationen
- [ ] Keine app-eigene Dark-Mode-Option
- [ ] Liquid Glass: Farbe nur für Primäraktion/Status, als Hintergrund-Tint, max. ein bis zwei prominente Controls
- [ ] Bei buntem Content: monochrome Bars oder klar abgesetzte Akzentfarbe; Ruhelage lesbar
- [ ] macOS: Systemakzentfarbe wird respektiert (Sidebar-Icons), Desktop Tinting berücksichtigt
- [ ] Bilder mit Farbprofil; P3-Assets mit sRGB-Fallback wo nötig
- [ ] Dark Mode: weiße Bildflächen abgedunkelt, Icons in beiden Modi sichtbar
- [ ] iOS: Systemhintergründe (base/elevated) statt eigener Hintergrundfarben

## Anti-Patterns

- Markenfarbe auf jedem Button, jedem Icon und als Textfarbe für Fließtext.
- Rot/Grün als einzige Unterscheidung für Fehler/Erfolg.
- Eigene „Dunkles Design“-Umschaltung in den App-Einstellungen.
- Dark Mode durch Invertieren der Light-Palette.
- Getönte, opake Toolbar-Hintergründe über Liquid Glass.
- Farbige Labels auf Glass über ähnlich farbigem Content.
- Mehrere farbig hinterlegte Glass-Buttons nebeneinander.
- `secondaryLabel` als Flächenfarbe oder `separator` als Textfarbe.
- Hex-Werte aus alten HIG-Versionen übernehmen (Werte änderten sich 2025).
- Vollflächige Farbhintergründe in watchOS-Workout-Views.
