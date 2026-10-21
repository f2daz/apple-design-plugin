# Icons, SF Symbols, App-Icons und Bild-Assets

Quellen (HIG-Spiegel, Stand 2026-10-21): `sf-symbols` (Update 2025-07-28, SF Symbols 7), `icons` (2025-06-09), `app-icons` (2026-06-08, Liquid Glass), `images` (2025-12-16), ergänzend `dark-mode`, `right-to-left`, `inclusion`.

## Einordnung

Drei Ebenen, die oft verwechselt werden:

| Ebene | Zweck | Format | Wer gestaltet |
|---|---|---|---|
| **Interface-Icon / Glyph** | Ein Konzept in UI ausdrücken (Toolbar, Tab Bar, Menü, Button) | SF Symbol oder eigenes Vektor-Asset (PDF/SVG), Template (schwarz + transparent) | Bevorzugt SF Symbols, sonst Custom Symbol |
| **App-Icon** | Identität der App auf Home Screen, Spotlight, Settings, Notifications, Share Sheet | Geschichtete Quelle (Icon Composer bzw. Image Stack) | Eigenes Design, System legt Liquid-Glass-Effekte darüber |
| **Bild-Asset** | Inhalte, Illustrationen, Fotos | PNG/JPEG/HEIC/PDF/SVG in Asset Catalog, Scale Factors | Eigenes Design |

Werkzeug im Plugin: **`scripts/sf_symbols.py`** zur Suche passender Symbolnamen (z. B. nach Begriff oder Kategorie). Vor jeder Symbolwahl damit prüfen, ob ein Systemsymbol existiert, statt ein eigenes Icon zu zeichnen. Verfügbarkeit hängt von der Ziel-OS-Version ab – Symbole und Features eines Jahrgangs gibt es in älteren Systemen nicht (hig:sf-symbols).

## Kernregeln

### SF Symbols
- Nutze SF Symbols für Interface-Icons; sie richten sich automatisch an San Francisco in allen Gewichten und Größen aus (hig:sf-symbols).
- Verwende SF Symbols (oder ähnlich aussehende Bilder) **nie** in App-Icons, Logos oder sonstiger Markennutzung – das verbieten die Nutzungsbedingungen (hig:sf-symbols).
- Prüfe den Rendering-Modus in jedem Kontext (Größe, Hintergrundkontrast); „automatic“ liefert den bevorzugten Modus, ersetzt aber keine Sichtprüfung (hig:sf-symbols#Rendering-modes).
- Nutze Systemfarben für Symbole, damit sie sich an Dark Mode, Vibrancy und Accessibility-Einstellungen anpassen (hig:sf-symbols#Rendering-modes).
- Setze Variable Color nur für sich ändernde Werte (Stärke, Füllstand) ein – nicht für Tiefe; Tiefe = Hierarchical (hig:sf-symbols#Variable-color).
- Stimme Symbol-Gewicht auf das Gewicht des benachbarten Texts ab; Betonung über Scale statt Gewicht steuern (hig:sf-symbols#Weights-and-scales, hig:icons#Best-practices).
- Überlasse die Wahl Outline vs. Fill möglichst dem Container (Tab Bar iOS → Fill, Toolbar → Outline) (hig:sf-symbols#Design-variants).
- Animiere Symbole sparsam und nur mit klarer Aussage; zu viele Animationen überladen (hig:sf-symbols#Animations).
- Passe Symbole, die Apple-Produkte oder -Features darstellen, **nicht** an – sie sind urheberrechtlich geschützt (im SF-Symbols-App mit Info-Badge markiert) (hig:sf-symbols#Custom-symbols).
- Gib Custom Symbols und eigenen Interface-Icons eine Accessibility-Beschreibung (hig:sf-symbols#Custom-symbols, hig:icons#Best-practices).

### Interface-Icons
- Gestalte stark vereinfacht und mit vertrauten Metaphern, direkt bezogen auf Aktion oder Inhalt (hig:icons#Best-practices).
- Halte Größe, Detailgrad, Strichstärke und Perspektive über alle Icons der App konsistent – auch bei Mischung aus Custom und System (hig:icons#Best-practices).
- Zentriere optisch, nicht geometrisch; Korrektur als Padding im Asset ablegen (hig:icons#Best-practices).
- Liefere eine Selected-Variante nur, wenn nötig – Standardkomponenten (Toolbar, Tab Bar, Buttons) erzeugen den Selected-State selbst (hig:icons#Best-practices).
- Nutze geschlechtsneutrale Figuren und kulturübergreifend verständliche Bilder (hig:icons#Best-practices, hig:inclusion#Gender-identity).
- Text im Icon nur, wenn bedeutungstragend (z. B. Textformatierung); Zeichen dann lokalisieren, Textandeutungen für RTL spiegeln (hig:icons#Best-practices).
- Liefere Custom-Interface-Icons als Vektor (PDF/SVG); PNG nur, wenn nötig, dann in allen Scale Factors (hig:icons#Best-practices).
- Bilde keine Apple-Hardware nach; falls nötig, nur Apple Design Resources oder die entsprechenden SF Symbols (hig:icons#Best-practices).

### App-Icons
- Baue das Icon geschichtet: Hintergrund + ein oder mehrere Vordergrund-Layer (iOS, iPadOS, macOS, watchOS); das System legt Liquid-Glass-Effekte (Specular Highlights, Refraction, Translucency) darüber (hig:app-icons#Layer-design).
- Liefere **ungemaskte, quadratische** Layer (tvOS: rechteckig); vormaskierte Ecken verschlechtern Highlights und erzeugen gezackte Kanten (hig:app-icons#Icon-shape).
- Halte Hauptinhalt zentriert – besonders bei kreisförmiger Maske (watchOS, visionOS) (hig:app-icons#Icon-shape).
- Bevorzuge klare Kanten in Vordergrund-Layern, keine weichen/gefederten Ränder (hig:app-icons#Layer-design).
- Importiere Layer bevorzugt als Vektor (SVG/PDF), Text in Outlines umwandeln; Mesh-Gradients/Raster als PNG (hig:app-icons#Layer-design).
- Hintergrund: Volltonfarbe oder Verlauf direkt in Icon Composer; importierte Hintergründe vollflächig und opak (hig:app-icons#Layer-design).
- Keine eigenen Schatten, Glows, Bevels, Blurs, Specular Highlights – das macht das System dynamisch (hig:app-icons#Visual-effects).
- Halte das Design einfach, mit wenigen Formen; Illustration statt Foto; keine Screenshots oder Standard-UI-Komponenten nachbauen (hig:app-icons#Design).
- Text nur, wenn für Erlebnis oder Marke essenziell; keine Wörter wie „Watch“, „Play“, „New“, „For visionOS“ (hig:app-icons#Design).
- Halte das Icon über alle Plattformen visuell konsistent (hig:app-icons#Design).
- Halte Kernmerkmale über alle Darstellungsvarianten gleich; keine Elemente je Variante austauschen (hig:app-icons#Appearances).
- Keine Nachbildung von Apple-Hardware (hig:app-icons#Design).

### Bild-Assets
- Liefere für jedes Bitmap alle Scale Factors der unterstützten Geräte (hig:images#Resolution).
- Gestalte auf niedrigster Auflösung, skaliere hoch; Kontrollpunkte von Vektorformen auf ganze Werte legen, damit @2x/@3x pixelgenau bleiben (hig:images#Resolution).
- Bette in jedes Bild ein Farbprofil ein (hig:images#Best-practices).
- Teste auf realen Geräten (hig:images#Best-practices).

## Kennwerte und Tabellen

### SF Symbols – Rendering-Modi (hig:sf-symbols#Rendering-modes)

| Modus | Verhalten | Typischer Einsatz |
|---|---|---|
| Monochrome | Eine Farbe für alle Layer | Standard in Text-nahen Kontexten |
| Hierarchical | Eine Farbe, Deckkraft je Layer-Ebene (primary/secondary/tertiary) | Tiefe/Hierarchie mit Akzentfarbe |
| Palette | Eine Farbe pro Layer; bei 2 Farben für 3 Ebenen teilen sich secondary und tertiary eine Farbe | Abstimmung auf Farbschema |
| Multicolor | Intrinsische Bedeutungsfarben (z. B. `leaf` grün, `trash.slash` rot) | Bedeutung durch Farbe verstärken |

Layer-Prinzip: Pfade sind in Ebenen organisiert, Beispiel `cloud.sun.rain.fill` = Wolke (primary), Sonne (secondary), Tropfen (tertiary).

**Gradients** (ab SF Symbols 7): linearer Verlauf aus einer Quellfarbe, in allen Modi, für System- und Custom-Farben sowie Custom Symbols; wirkt am besten bei großen Größen (hig:sf-symbols#Gradients).

**Variable Color:** Färbt Layer schwellwertabhängig zwischen 0 und 100 %. Einzelne Layer können ausgenommen werden (z. B. Lautsprecherkorpus in `speaker.wave.3`) (hig:sf-symbols#Variable-color).

### SF Symbols – Gewichte und Skalen (hig:sf-symbols#Weights-and-scales)

| Merkmal | Werte |
|---|---|
| Gewichte | 9, von Ultralight bis Black, je entsprechend einem SF-Font-Gewicht |
| Skalen | Small, Medium (Default), Large – relativ zur Cap Height von SF |
| Design-Varianten | Outline (häufigste), Fill, Slash, Enclosed (Circle/Square/Rectangle); kombinierbar |
| Sprach-/Schriftvarianten | u. a. Latin, Arabic, Hebrew, Hindi, Thai, Chinese, Japanese, Korean, Cyrillic, Devanagari, indische Ziffernsysteme; wechseln automatisch mit Gerätesprache |

Varianten-Faustregeln: Outline neben Text (Toolbar, Liste); Enclosed verbessert Lesbarkeit bei kleinen Größen; Fill für mehr Gewicht (iOS-Tab-Bar, Swipe Actions, Auswahl mit Akzentfarbe); Slash für „nicht verfügbar“.

### SF Symbols – Animationen (hig:sf-symbols#Animations)

| Effekt | Wirkung | Einsatz |
|---|---|---|
| Appear / Disappear | Symbol erscheint/verschwindet schrittweise | Ein-/Ausblenden |
| Bounce | Kurzes elastisches Skalieren, kehrt zurück; einmalig per Default | „Aktion ist passiert / nötig“ |
| Scale | Größenänderung, bleibt bestehen bis zurückgesetzt | Auswahl hervorheben |
| Pulse | Deckkraft variiert (nur annotierte Layer oder alle) | Laufende Aktivität |
| Variable Color | Layer-Deckkraft schrittweise; cumulative oder iterative; optional autoreverse, inaktive Layer ausblenden; open loop vs. closed loop | Fortschritt, Verbinden, Senden, Wiedergabe |
| Replace | Tausch zweier Symbole; Varianten Down-Up, Up-Up (Fortschritt), Off-Up (nächster Zustand betont) | Zustandswechsel |
| Magic Replace | Smarter Übergang verwandter Formen (Slash zeichnet, Badge erscheint); Default-Replace, fällt bei unverwandten Symbolen auf Down-Up zurück | Play/Pause, Mic/Mic-Slash |
| Wiggle | Hin-und-her entlang einer Achse | Übersehbaren Call-to-Action betonen |
| Breathe | Deckkraft **und** Größe pulsieren | Laufende Aufnahme, Status |
| Rotate | Ganzes Symbol oder Teile (By Layer, z. B. Ventilatorblätter) | Laufender Vorgang |
| Draw On / Draw Off | Zeichnet entlang Führungspunkten (ab SF Symbols 7); alle Layer, gestaffelt oder einzeln | Fortschritt (Download), Richtung |

Wiedergabe steuerbar: einmalig oder wiederholt bis Bedingung erfüllt, Geschwindigkeit, Reverse vor Wiederholung. Animationen gelten für alle Modi, Gewichte, Skalen und Custom Symbols. Animationen nur mit SF Symbols 5 oder neuer (hig:motion#Providing-feedback).

### Standard-Symbole für häufige Aktionen (Auswahl, hig:icons#Standard-icons)

| Aktion | Symbol |
|---|---|
| Cut / Copy / Paste | `scissors` / `document.on.document` / `document.on.clipboard` |
| Done, Save | `checkmark` |
| Cancel, Close, Deselect | `xmark` |
| Delete | `trash` |
| Undo / Redo | `arrow.uturn.backward` / `arrow.uturn.forward` |
| Compose | `square.and.pencil` |
| Duplicate | `plus.square.on.square` |
| Rename | `pencil` |
| Move to, Folder | `folder` |
| Attach / Add / More | `paperclip` / `plus` / `ellipsis` |
| Select | `checkmark.circle` |
| Bold / Italic / Underline | `bold` / `italic` / `underline` |
| Superscript / Subscript | `textformat.superscript` / `textformat.subscript` |
| Align Left / Center / Justified / Right | `text.alignleft` / `text.aligncenter` / `text.justify` / `text.alignright` |
| Search | `magnifyingglass` |
| Find (inkl. Replace, Next, Previous, Use Selection) | `text.page.badge.magnifyingglass` |
| Filter | `line.3.horizontal.decrease` |
| Share, Export | `square.and.arrow.up` |
| Print | `printer` |
| Account, User, Profile | `person.crop.circle` |
| Like / Dislike | `hand.thumbsup` / `hand.thumbsdown` |
| Bring to Front / Send to Back | `square.3.layers.3d.top.filled` / `square.3.layers.3d.bottom.filled` |
| Bring Forward / Send Backward | `square.2.layers.3d.top.filled` / `square.2.layers.3d.bottom.filled` |
| Alarm / Archive / Calendar | `alarm` / `archivebox` / `calendar` |

Hinweis: Mehrere Namen (`document.on.document`, `text.page.badge.magnifyingglass`) sind neuere Umbenennungen; bei älteren Deployment Targets mit `scripts/sf_symbols.py` bzw. der SF-Symbols-App die Verfügbarkeit prüfen.

### App-Icon-Spezifikationen (hig:app-icons#Specifications)

| Plattform | Layout-Form | Form nach Maskierung | Layout-Größe | Stil | Darstellungsvarianten |
|---|---|---|---|---|---|
| iOS, iPadOS, macOS | Quadrat | Abgerundetes Rechteck (quadratisch) | 1024x1024 px | Layered | Default, Dark, Clear Light, Clear Dark, Tinted Light, Tinted Dark |
| tvOS | Rechteck (Querformat) | Abgerundetes Rechteck | 800x480 px | Layered (Parallax, 2–5 Layer) | – |
| visionOS | Quadrat | Kreis | 1024x1024 px | Layered (3D, Hintergrund + 1–2 Layer) | – |
| watchOS | Quadrat | Kreis | 1088x1088 px | Layered | – |

- Kleinere Varianten (Settings, Notifications) skaliert das System automatisch.
- Farbräume: sRGB, Gray Gamma 2.2, Display P3 (Wide Gamut; nicht visionOS).
- Nicht gelieferte Darstellungsvarianten erzeugt das System selbst (hig:app-icons#Appearances).
- Alternative App-Icons (iOS, iPadOS, tvOS, kompatible Apps in visionOS) brauchen in iOS/iPadOS jeweils eigene Dark-, Clear- und Tinted-Varianten; alle unterliegen App Review (hig:app-icons#Appearances).

### Icon Composer – Workflow (hig:app-icons#Layer-design)

1. Vordergrund-Layer im eigenen Design-Tool anlegen (Vektor, klare Kanten, zunächst voll opak).
2. In Icon Composer (Teil von Xcode, auch separat über Apple Developer) importieren.
3. Hintergrund definieren (Farbe/Verlauf), Layer-Positionen anpassen.
4. Effekte setzen: Specular Highlights, Refraction, Translucency; Deckkraft der Vordergrund-Layer variieren für Tiefe.
5. Layer gruppieren, wenn Effekte auf Gruppenebene wirken sollen (Gruppen bieten zusätzliche Liquid-Glass-Optionen).
6. Darstellungsvarianten annotieren, über Systemversionen vorschauen, nach Xcode exportieren.

tvOS/visionOS: Layer stattdessen als Image Stack im Asset Catalog; Parallax Previewer / Parallax Exporter aus Apple Design Resources.

Für das Erzeugen und Validieren von `.icon`-Paketen steht der Skill **compose-app-icon** zur Verfügung.

### Darstellungsvarianten (Light/Dark/Clear/Tinted) (hig:app-icons#Appearances)

| Variante | Gestaltungshinweis |
|---|---|
| Default | Basis-Design |
| Dark | Aus dem Light-Icon ableiten; komplementäre Farben, keine überhellen Bilder; farbige Hintergründe liefern meist den besten Kontrast |
| Clear (Light/Dark) | Noch zurückhaltender als Dark; Form muss ohne Farbe tragen |
| Tinted (Light/Dark) | Ebenfalls stark gedämpft; Erkennbarkeit über Silhouette |

Alle Varianten: sichtbar, lesbar, wiedererkennbar; sollen neben System-Icons und Widgets stimmig wirken.

### Bild-Auflösungen (hig:images#Resolution)

| Plattform | Scale Factors |
|---|---|
| iOS | @2x und @3x |
| iPadOS, watchOS | @2x |
| macOS, tvOS | @1x und @2x |
| visionOS | @2x oder höher; über @6x merkliche Performance-Kosten, bei > @2x hochwertige Filterung setzen |

### Bildformate (hig:images#Formats)

| Bildtyp | Format |
|---|---|
| Bitmap/Raster | De-interlaced PNG |
| PNG ohne 24-bit-Bedarf | 8-bit-Palette |
| Fotos | JPEG (optimiert) oder HEIC |
| Stereo/Spatial Photos | Stereo HEIC |
| Flache Icons, Interface-Icons, skalierende Flachgrafik | PDF oder SVG |

### macOS – Document Icons (hig:icons#Document-icons)

| Element | Größen |
|---|---|
| Background Fill | 512x512 @1x / 1024x1024 @2x · 256 / 512 · 128 / 256 · 32 / 64 · 16 / 32 px |
| Center Image (halbe Canvas-Größe) | 256x256 @1x / 512x512 @2x · 128 / 256 · 32 / 64 · 16 / 32 px |
| Rand im Center Image | ca. 10 % der Canvas; Motiv ca. 80 % (z. B. ~205x205 in 256x256) |

- Ohne eigenes Document Icon komponiert macOS App-Icon + Dateiendung.
- Obere rechte Ecke freihalten (System zeichnet die Eselsohr-Ecke darüber).
- Kleine Größen vereinfachen (z. B. Rasterlinien reduzieren, bei 16x16 weglassen).
- Optional kurzer Begriff statt unbekannter Endung (z. B. „scene“ statt „scn“); System setzt ihn in Großbuchstaben und skaliert ihn.

### watchOS – Autoscaling-PDFs (hig:images#watchOS)

Design für 40 mm und 42 mm in @2x; WatchKit skaliert:

| Bildschirm | Skalierung |
|---|---|
| 38 mm | 90 % |
| 40 mm | 100 % |
| 41 mm | 106 % |
| 42 mm | 100 % |
| 44 mm | 110 % |
| 45 mm | 119 % |
| 49 mm | 119 % |

## Plattform-Unterschiede

| Thema | iOS / iPadOS | macOS | watchOS |
|---|---|---|---|
| App-Icon-Maske | Abgerundetes Quadrat | Abgerundetes Quadrat (gleiche Spezifikation wie iOS) | Kreis – Inhalt streng zentrieren |
| App-Icon-Größe | 1024x1024 px | 1024x1024 px | 1088x1088 px |
| Darstellungsvarianten | Default, Dark, Clear, Tinted | Default, Dark, Clear, Tinted | keine |
| Besonderheit | Alternative App-Icons möglich (mit eigenen Varianten) | Document Icons für eigene Dateitypen | Kein schwarzer Icon-Hintergrund (verschmilzt mit Display) |
| Bild-Scale | iOS @2x+@3x, iPadOS @2x | @1x+@2x | @2x, Autoscaling-PDF; Transparenz nur wo nötig (Template-Bilder, Complications), sonst Hintergrund einbacken |
| Symbol-Varianten | Tab Bar nutzt Fill | Toolbar/Sidebar meist Outline | Kompakte Darstellung, Enclosed hilft bei Kleinstgrößen |

## Umsetzung

### SwiftUI
```swift
Image(systemName: "cloud.sun.rain.fill")
    .symbolRenderingMode(.hierarchical)      // .monochrome / .palette / .multicolor
    .foregroundStyle(.tint)
    .imageScale(.large)                      // small / medium / large
    .font(.body.weight(.semibold))           // Gewicht folgt Font

Image(systemName: "wifi", variableValue: signal) // Variable Color 0.0–1.0

Image(systemName: "bell")
    .symbolEffect(.bounce, value: count)     // Discrete Effect bei Wertänderung
Image(systemName: isMuted ? "mic.slash" : "mic")
    .contentTransition(.symbolEffect(.replace))

Label("Teilen", systemImage: "square.and.arrow.up")   // Text + Symbol, VoiceOver-Label inklusive
Image("CustomGlyph").accessibilityLabel("Zähler")       // Custom Symbol beschriften
Image(decorative: "Ornament")                           // rein dekorativ
```

### UIKit
```swift
let config = UIImage.SymbolConfiguration(textStyle: .body, scale: .large)
    .applying(UIImage.SymbolConfiguration(paletteColors: [.systemBlue, .systemGray]))
imageView.image = UIImage(systemName: "speaker.wave.3", withConfiguration: config)
imageView.addSymbolEffect(.pulse)               // iOS 17+
```

### AppKit
```swift
let config = NSImage.SymbolConfiguration(textStyle: .body, scale: .medium)
let image = NSImage(systemSymbolName: "trash", accessibilityDescription: "Löschen")?
    .withSymbolConfiguration(config)
```

Hinweise: Symbol-Effekte gibt es ab SF Symbols 5 (iOS 17 / macOS 14 / watchOS 10); Draw On/Off und Gradients ab SF Symbols 7 – Deployment Target prüfen. Custom Symbols: Template eines ähnlichen Systemsymbols aus der SF-Symbols-App exportieren, im Vektor-Tool anpassen, in der App annotieren.

## Custom Symbols – Prozess (hig:sf-symbols#Custom-symbols)

- [ ] Ähnlichstes Systemsymbol als Template exportieren; Detailgrad, optisches Gewicht, Ausrichtung, Perspektive übernehmen.
- [ ] Ziele: einfach, erkennbar, inklusiv, direkt auf Aktion/Inhalt bezogen.
- [ ] Layer annotieren (Farbe oder Hierarchie-Ebene) für die gewünschten Rendering-Modi.
- [ ] Bei Badges/Breitenzuwachs negative Side Margins setzen; Benennung nach Muster `left-margin-Regular-M`.
- [ ] Für Animationen ganze Formen zeichnen und Lücken als Erase-Layer annotieren (statt Ausschnitte); Z-Order für Variable Color festlegen; Layer-Gruppen nutzen.
- [ ] Mit **allen** Animations-Presets testen.
- [ ] Enclosures/Badges nicht einzeichnen, sondern über die Component Library der SF-Symbols-App erzeugen.
- [ ] Directionality für RTL festlegen (hig:right-to-left).
- [ ] Accessibility-Label vergeben.
- [ ] Keine Apple-Produkte nachbilden; Apple-Feature-Symbole nicht anpassen.

## Review-Checkliste

**Interface-Icons und Symbole**
- [ ] Für jede Standardaktion das Standardsymbol aus der Tabelle verwendet (mit `scripts/sf_symbols.py` gegengeprüft).
- [ ] Symbolgewicht passt zum Nachbartext; Betonung über Scale, nicht über Gewichtsbruch.
- [ ] Rendering-Modus in Light, Dark und Increase Contrast sowie bei kleinster Größe geprüft.
- [ ] Variable Color nur für veränderliche Werte.
- [ ] Animationen haben klaren Zweck, wenige gleichzeitig, passen zur Tonalität; Reduce Motion berücksichtigt (siehe `motion-and-feedback.md`).
- [ ] Custom Icons: Vektor (PDF/SVG), optisch zentriert, konsistente Strichstärke, Accessibility-Label.
- [ ] Keine SF Symbols in App-Icon, Logo oder Marke.
- [ ] Keine angepassten Apple-Produkt-/Feature-Symbole, keine Hardware-Nachbildungen.
- [ ] Icons mit Leserichtung für RTL gespiegelt bzw. Systemvarianten genutzt.

**App-Icon**
- [ ] Geschichtete Quelle in Icon Composer (iOS/iPadOS/macOS/watchOS) bzw. Image Stack (tvOS/visionOS).
- [ ] Layer quadratisch, ungemaskt, Vektor; Text in Outlines.
- [ ] Keine eingebackenen Schatten, Glows, Highlights, Blurs.
- [ ] Hauptmotiv zentriert, funktioniert in kreisförmiger Maske (watchOS).
- [ ] Varianten Default/Dark/Clear/Tinted geprüft; Kernmerkmale identisch.
- [ ] watchOS: kein schwarzer Hintergrund.
- [ ] Keine Fotos, Screenshots, UI-Nachbauten, überflüssigen Wörter.
- [ ] Alternative Icons (falls vorhanden) mit eigenen Varianten.

**Bilder**
- [ ] Alle Scale Factors je Plattform vorhanden.
- [ ] Farbprofil eingebettet; Formate gemäß Tabelle.
- [ ] Light/Dark-Varianten wo nötig (z. B. weiße Bildhintergründe im Dark Mode abdunkeln) (hig:dark-mode#Icons-and-images).
- [ ] Auf echten Geräten geprüft.

## Anti-Patterns

- SF Symbol (z. B. `bolt.fill`) als App-Logo oder im App-Icon.
- Vormaskiertes, abgerundetes PNG als App-Icon-Layer → gezackte Kanten, kaputte Highlights.
- Eingebackene Drop Shadows/Glanz im Icon, die mit Liquid-Glass-Effekten kollidieren.
- Dark-Icon, das Elemente austauscht oder anderes Motiv zeigt.
- Selbst gezeichnete Varianten mit Badge/Kreis statt Component Library.
- Variable Color als Deko-Verlauf für Tiefe.
- Dauerhaft wiederholte Wiggle/Bounce-Effekte ohne Bedeutung.
- Nur PNG @1x für ein Interface-Icon.
- Unterschiedliche Strichstärken zwischen eigenen und System-Icons.
- Männliche Standardfigur für „Person“.
- Apple-Hardware im Icon nachgebaut.

## Unklarheiten / Widersprüche im Spiegel

- **Darstellungsvarianten:** `app-icons#Layer-design` nennt für Icon Composer „default, dark, and mono“, die Abschnitte *Appearances* und *Specifications* nennen „default, dark, clear, tinted“ (Spezifikation: Clear Light/Dark, Tinted Light/Dark). Vermutlich ist „mono“ die Basis für Clear/Tinted; maßgeblich ist die Spezifikationstabelle.
- **watchOS 42 mm = 100 %** in der Autoscaling-Tabelle, obwohl 41 mm bei 106 % liegt; das Apple-Dokument nennt 40 mm und 42 mm als Designbasis. Werte so übernommen, nicht interpoliert.
- **App-Icon macOS:** Die Plattform-Sektion nennt „keine zusätzlichen Überlegungen“ für macOS; macOS-Spezifika stehen nur unter Document Icons (`icons`).
- Konkrete Punktgrößen für Symbol-Skalen nennt die HIG nicht – sie sind relativ zur Cap Height definiert.
