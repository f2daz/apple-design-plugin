# Materialien und Liquid Glass

> Quelle: HIG-Spiegel `materials.md` (Apple-Update 2025-09-09), `color.md#Liquid-Glass-color` (2025-12-16), `buttons`, `toolbars`, `tab-bars`, `sidebars`, `scroll-views` (2026-06-08), `layout`, `app-icons` (2026-06-08), `widgets`, `motion`, `branding`, `virtual-keyboards`, `dark-mode`, `sheets`. Gespiegelt 2026-10-21. Paraphrasiert.

## Einordnung

Ein Material erzeugt Tiefe und Hierarchie, indem es Farbe vom Hintergrund in den Vordergrund durchlässt. Apple-Plattformen kennen zwei Arten:

| | **Liquid Glass** | **Standard Materials** |
|---|---|---|
| Ebene | Funktions-Layer (Controls, Navigation) | Content-Layer |
| Zweck | Controls über Inhalt schweben lassen, ohne ihn zu verdecken | Struktur und Abgrenzung *innerhalb* des Contents |
| Beispiele | Tab Bar, Toolbar, Sidebar, Buttons in Bars, Alerts, Popovers | App-Hintergründe, Karten, Overlays im Content |
| APIs | `glassEffect(_:in:)`, `Glass.regular` / `.clear` | `Material` (`.ultraThin` … `.thick`), `UIBlurEffect`, `UIVibrancyEffect`, `NSVisualEffectView` |

(hig:materials)

**Liquid Glass** ist ein dynamisches Material, das die Designsprache plattformübergreifend vereinheitlicht: Es bildet eine eigene funktionale Ebene über dem Content, lässt Inhalt darunter durchscheinen und hält Controls dennoch lesbar. Es hat keine Eigenfarbe, sondern nimmt Farbe vom Inhalt dahinter auf, reagiert auf Interaktion (bei Touch stärker, bei Trackpad gedämpfter) und passt sich Systemeinstellungen an. (hig:materials#Liquid-Glass, hig:color#Liquid-Glass-color, hig:motion)

## Kernregeln

### Content-Layer vs. Funktions-Layer
- Verwende Liquid Glass **nicht im Content-Layer**; dort Standard Materials nutzen. Ausnahme: transiente Interaktionselemente im Content (Slider, Toggles) nehmen während der Bedienung kurz Glass-Optik an. (hig:materials#Liquid-Glass)
- Trenne Controls vom Content über Liquid Glass – nicht über solide oder halbtransparente Hintergrundflächen; für zusätzliche Abgrenzung Scroll Edge Effect. (hig:layout#Visual-hierarchy)
- Lass Content unter Sidebars, Toolbars und Tab Bars bis zum Rand laufen; ggf. Background Extension Effect. (hig:layout#Visual-hierarchy, hig:sidebars#Best-practices)

### Sparsamkeit, Standard vs. Custom
- Standardkomponenten übernehmen Liquid Glass automatisch – zuerst Systemkomponenten nutzen. (hig:materials#Liquid-Glass)
- Auf Custom Controls Liquid Glass **sparsam** und nur für die wichtigsten Funktionselemente einsetzen; zu viel Glass lenkt vom Inhalt ab. (hig:materials#Liquid-Glass)
- Custom-Komponenten in Bars mit konzentrischen Eckradien zur Bar gestalten (Standardkomponenten tun das bereits). (hig:toolbars#Best-practices)
- Keine eigenen Toolbar-Hintergründe/-Appearances, die die Systemeffekte überlagern. (hig:toolbars#Best-practices)
- Custom-Controls über der Tastatur: Glass anwenden, wenn die übrige App Glass nutzt oder die Leiste sonst fremd wirkt; eine Standard-Toolbar übernimmt Glass automatisch. (hig:virtual-keyboards)

### Regular vs. Clear
- **Regular** (Default der meisten Systemkomponenten): weichzeichnet und passt Luminanz des Hintergrunds an → Lesbarkeit. Verwenden, wenn der Hintergrund Lesbarkeit gefährden kann oder die Komponente viel Text trägt (Alerts, Sidebars, Popovers). (hig:materials#Liquid-Glass)
- **Clear**: stark transluzent, priorisiert den Inhalt dahinter. **Nur** über visuell reichen Hintergründen (Fotos, Video) für immersive Erlebnisse. (hig:materials#Liquid-Glass)
- Bei Clear über hellem Inhalt eine **dunkle Abdunklungsebene mit 35 % Deckkraft** erwägen; bei ausreichend dunklem Inhalt oder AVKit-Standard-Playback-Controls (eigene Abdunklung) nicht nötig. (hig:materials#Liquid-Glass)

### Tinting / Farbe auf Glass
- Farbe auf Glass sparsam: nur für Primäraktionen und Statusindikatoren. (hig:color#Liquid-Glass-color)
- Primäraktion über **getönten Hintergrund** hervorheben (wie System-Prominent-Buttons, z. B. Done, mit Akzentfarbe), nicht über farbigen Text/Symbole. Nicht mehrere Controls farbig hinterlegen. (hig:color#Liquid-Glass-color)
- Prominente Buttons: ein bis zwei pro View; in Toolbars genau eine Primäraktion im `.prominent`-Stil auf der trailing Seite. (hig:buttons#Style, hig:toolbars#Actions)
- Bei farbigem Content: Labels auf Bars/Buttons monochrom lassen oder eine deutlich abgesetzte Akzentfarbe wählen. (hig:color#Liquid-Glass-color, hig:buttons#Style, hig:toolbars#Best-practices, hig:tab-bars#Best-practices)
- Marke lieber im Content-Layer zeigen, wo sie unter Glass durchscheint und dynamisch aufgenommen wird. (hig:branding)
- Custom Colors immer mit Light- **und** Dark-Variante, sonst passt sich Glass nicht korrekt an. (hig:color#Best-practices)

### Adaptives Verhalten
- Kleine Glass-Elemente (Toolbar, Tab Bar) schalten je nach Untergrund zwischen hellem und dunklem Erscheinungsbild; Symbole/Text darauf sind standardmäßig monochrom (dunkel auf hellem, hell auf dunklem Content). (hig:color#Liquid-Glass-color)
- Große Glass-Elemente (Sidebars) sind opaker, um über komplexem Hintergrund lesbar zu bleiben. (hig:color#Liquid-Glass-color)
- Die Ruhelage (z. B. Scroll-Anfang) muss klar lesbar sein, auch wenn bunter Content zwischendurch darunter scrollt. (hig:color#Liquid-Glass-color)

### Scroll Edge Effects (hig:scroll-views#Scroll-edge-effects)
- Zweck: visuelle Trennung zwischen schwebenden Elementen (z. B. Toolbar) und dem scrollenden Content dahinter (iOS, iPadOS, macOS). Weichzeichnet und reduziert die Deckkraft des Contents am Rand.
- Stil **automatic** bevorzugen; er wird opaker bei Toolbars mit vielen Controls, bei Text außerhalb von Glass-Controls und bei gepinnten Tabellen-Headern. Stile: automatic, hard, soft – soft nur mit gründlichem Lesbarkeitstest.
- Nur einsetzen, wenn eine Scroll View hinter schwebenden Elementen liegt – nicht dekorativ, kein Overlay/Abdunkeln.
- Ein Effekt pro View; in Split Views je Pane einer, mit gleicher Höhe.
- Bei Custom Bars ggf. manuell hinzufügen.

### Barrierefreiheit
- Die Darstellung von Regular und Clear ändert sich mit Systemeinstellungen: bevorzugter Liquid-Glass-Look (Geräteeinstellung), **Reduce Transparency**, **Increase Contrast**. Custom Glass daher mit allen Kombinationen testen. (hig:materials#Liquid-Glass)
- In Dark Mode mit Increase Contrast und Reduce Transparency (einzeln und kombiniert) auf schwer lesbare dunkle Texte prüfen. (hig:dark-mode#Best-practices)
- Bewegungsverhalten passt sich Eingabemethode und Accessibility-Einstellungen an – Systemkomponenten nutzen statt eigene Glass-Animationen. (hig:motion)
- Der Spiegel beschreibt **nicht** im Detail, wie Glass bei Reduce Transparency konkret aussieht (z. B. Opazitätswerte) – keine Annahmen treffen, sondern auf dem Gerät prüfen.

### Standard Materials
- Material nach semantischem Zweck wählen, nicht nach der Farbe, die es scheinbar erzeugt. (hig:materials#Standard-materials)
- Auf Materials **vibrant colors** verwenden (Labels, Fills, Separators). (hig:materials#Standard-materials)
- Dicker = opaker = besserer Kontrast für Text/feine Details; dünner = transluzenter = mehr Kontext. (hig:materials#Standard-materials)

## Kennwerte

| Kennwert | Wert | Beleg |
|---|---|---|
| Abdunklung unter Clear Glass bei hellem Inhalt | dunkle Ebene, 35 % Opazität | hig:materials#Liquid-Glass |
| Glass-Varianten | regular, clear | hig:materials#Liquid-Glass |
| Scroll-Edge-Stile | automatic (Default), hard, soft | hig:scroll-views#Scroll-edge-effects |
| Standard Materials iOS/iPadOS | ultraThin, thin, regular (Default), thick | hig:materials#iOS-iPadOS |
| App-Icon-Erscheinungsbilder iOS/iPadOS/macOS | Default, Dark, Clear Light, Clear Dark, Tinted Light, Tinted Dark | hig:app-icons#Specifications |

### Vibrancy auf Standard Materials (iOS/iPadOS) (hig:materials#iOS-iPadOS)

| Typ | Stufen (`UIVibrancyEffectStyle`) | Einschränkung |
|---|---|---|
| Label | `label` (Default), `secondaryLabel`, `tertiaryLabel`, `quaternaryLabel` | `quaternaryLabel` nicht auf `thin`/`ultraThin` (zu wenig Kontrast) |
| Fill | `fill` (Default), `secondaryFill`, `tertiaryFill` | auf allen Materials |
| Separator | `separator` | auf allen Materials |

## Plattform-Unterschiede

### iOS
- Tab Bar schwebt unten auf Liquid Glass; kann bei Scroll minimieren, Accessory (z. B. MiniPlayer) rückt inline. (hig:tab-bars#iOS)
- Toolbar-Buttons erhalten automatisch Glass; Primäraktion `.prominent`, trailing. (hig:toolbars, hig:buttons)
- Vier Standard Materials für den Content-Layer.

### iPadOS
- Tab Bar oben, optional als Sidebar; Sidebar schwebt im Glass-Layer, Content läuft darunter (Background Extension Effect). (hig:tab-bars#iPadOS, hig:sidebars)
- Split Views: je Pane ein Scroll Edge Effect, gleiche Höhe.

### macOS
- Sidebars schweben im Glass-Layer; Toolbar-Items ohne Bezel. (hig:sidebars, hig:toolbars#macOS)
- Standard Materials über `NSVisualEffectView.Material` mit festgelegten Zwecken; vibrante Versionen aller Systemfarben. Blending Modes: behind window, within window. (hig:materials#macOS)
- Vibrancy in Custom Views bewusst zulassen und testen.

### watchOS
- Toolbar-Buttons erhalten Glass-Appearance zur Abgrenzung vom Content. (hig:buttons)
- Materials in Vollbild-Modals geben Kontext; Standard-Material-Hintergründe von Sheets nicht entfernen. Sheets sind halbtransparent, Hintergrund wird weichgezeichnet und entsättigt. (hig:materials#watchOS, hig:sheets#watchOS)

### tvOS / visionOS (Rand)
- tvOS: Glass in Navigation, Top Shelf, Control Center; Bildviews/Buttons werden bei Fokus zu Glass. Standard Materials: ultraThin/thin (helles Schema), regular, thick (dunkles Schema). (hig:materials#tvOS)
- visionOS: Fenster nutzen unveränderliches System-Material „glass“ (kein separater Dark Mode). Transluzenz statt Opazität; thin für interaktive Elemente, regular für Sektionen, thick für dunkle Elemente auf regular; Vibrancy label/secondaryLabel/tertiaryLabel. Buttons auf Fenster: thin, frei im Raum: glass. Toolbar mit variablem Blur. (hig:materials#visionOS, hig:buttons, hig:toolbars#visionOS)

### App-Icons und Widgets
- App-Icons (iOS, iPadOS, macOS, watchOS) bestehen aus Hintergrund- und Vordergrund-Layern und erhalten Liquid-Glass-Attribute (Specular Highlights, Refraction, Translucency) automatisch. Keine eigenen Glanzlichter, Schatten, Blurs einbauen; Layer ungemaskt und mit klaren Kanten liefern; Effekte in Icon Composer konfigurieren, ggf. auf Gruppenebene. (hig:app-icons#Layer-design, hig:app-icons#Visual-effects)
- Widgets im Clear-Erscheinungsbild: System entsättigt und fügt Transluzenz, Highlights und Liquid Glass hinzu; im Accented Rendering Mode ersetzt Glass den Hintergrund. Accent- und Primary-Gruppe definieren. (hig:widgets)

## Umsetzung

> **Belegt im Spiegel:** `glassEffect(_:in:)`, `Glass.regular`, `Glass.clear`, „Applying Liquid Glass to custom views“, „Adopting Liquid Glass“, `ScrollEdgeEffectStyle` / `UIScrollEdgeEffect.Style` / `NSScrollEdgeEffectStyle`, `backgroundExtensionEffect()`, `UIBackgroundExtensionView`, `TabBarMinimizeBehavior`, `Material`, `UIVisualEffectView`, `UIBlurEffect`, `UIVibrancyEffect`, `NSVisualEffectView`, `widgetAccentable(_:)`.
> **Framework-Wissen (iOS/iPadOS/macOS 26 SDK), nicht im Spiegel:** `GlassEffectContainer`, `.interactive()`, `.tint(_:)` auf `Glass`, `glassEffectID(_:in:)`, `.buttonStyle(.glass/.glassProminent)`, `UIGlassEffect`, `NSGlassEffectView`. Vor Verwendung gegen die aktuelle Developer-Dokumentation prüfen.

**SwiftUI**
```swift
// 1. Standard zuerst: Systemkomponenten bringen Glass mit
NavigationStack { list }
    .toolbar {
        ToolbarItem(placement: .confirmationAction) {
            Button("Fertig") { save() }            // Primäraktion trailing
        }
    }

// 2. Custom Control (sparsam!)
Button(action: locate) { Image(systemName: "location") }
    .padding()
    .glassEffect(.regular, in: .circle)         // belegt: glassEffect(_:in:), Glass.regular

// 3. Über Foto/Video: clear + ggf. 35 % Abdunklung
ZStack {
    photo
    Color.black.opacity(0.35)                   // nur bei hellem Inhalt
    controls.glassEffect(.clear, in: .capsule)
}

// 4. Mehrere Glass-Elemente gemeinsam rendern/morphen (Framework-Wissen)
GlassEffectContainer(spacing: 20) {
    HStack(spacing: 20) {
        Button("A") {}.glassEffect(.regular.interactive())
        Button("B") {}.glassEffect(.regular.tint(.accentColor).interactive()) // Tint = Primäraktion
    }
}

// Standard Material im Content-Layer
card.background(.thinMaterial, in: .rect(cornerRadius: 16))

// Scroll Edge Effect nur bei Bedarf umstellen
ScrollView { … }.scrollEdgeEffectStyle(.hard, for: .top)

// Barrierefreiheit prüfen
@Environment(\.accessibilityReduceTransparency) var reduceTransparency
```

**UIKit:** Systemleisten (`UINavigationBar`, `UITabBar`, `UIToolbar`) übernehmen Glass automatisch – keine `backgroundColor`/`standardAppearance`-Hintergründe setzen. Custom: `UIVisualEffectView` mit Glass-Effect (Framework: `UIGlassEffect`), Standard Materials mit `UIBlurEffect` + `UIVibrancyEffect`. `UIAccessibility.isReduceTransparencyEnabled` beachten.

**AppKit:** Sidebar/Toolbar über Standard-`NSSplitViewController`/`NSToolbar`; Standard Materials mit `NSVisualEffectView` (Material + Blending Mode); Custom Glass laut Framework über `NSGlassEffectView`.

## Review-Checkliste

- [ ] Liquid Glass nur im Funktions-Layer (Bars, Navigation, schwebende Controls), nicht für Karten/Hintergründe im Content
- [ ] Systemkomponenten statt Eigenbau; Custom Glass nur für wenige zentrale Controls
- [ ] Keine soliden/halbtransparenten Flächen unter Bars; Content läuft unter Bars/Sidebar durch
- [ ] Regular als Default; Clear nur über Foto/Video, bei hellem Inhalt mit 35-%-Abdunklung
- [ ] Farbe auf Glass nur für Primäraktion/Status, als Hintergrund-Tint, max. ein bis zwei prominente Controls
- [ ] Bei buntem Content monochrome Labels auf Glass
- [ ] Ruhelage (Scroll-Anfang) gut lesbar
- [ ] Scroll Edge Effect: nur hinter schwebenden Elementen, einer pro View, automatic bevorzugt
- [ ] Konzentrische Eckradien bei Custom-Komponenten in Bars
- [ ] Getestet mit Reduce Transparency, Increase Contrast, Dark Mode, bevorzugtem Glass-Look
- [ ] Custom Colors mit Light- und Dark-Variante
- [ ] Standard Materials nach Zweck gewählt; vibrante Farben darauf; kein quaternaryLabel auf thin/ultraThin
- [ ] App-Icon: Layer ungemaskt, ohne eingebackene Effekte, alle Appearances (Default/Dark/Clear/Tinted) geprüft
- [ ] watchOS: Material-Hintergründe von Modals/Sheets nicht entfernt

## Anti-Patterns

- „Glass everywhere“: Karten, Listenzellen, Hintergründe im Content mit `glassEffect`.
- Clear Glass über Text oder ruhigem Hintergrund – Lesbarkeit bricht.
- Getönte Glass-Buttons in Serie (alle farbig = keiner hervorgehoben).
- Farbiger Text/Icon auf Glass statt getöntem Hintergrund für die Primäraktion.
- Eigene opake Navigation-Bar-Farbe über dem System-Glass.
- Scroll Edge Effect als Deko oder doppelt (Toolbar + eigener Gradient).
- Eigene Blur-/Glanz-Effekte im App-Icon, vorgerundete Icon-Layer.
- Glass-Optik nachgebaut mit `.ultraThinMaterial` + Rahmen statt echter API (verliert Adaptivität und Accessibility-Verhalten).
- Material nach „sieht hellgrau aus“ gewählt statt nach Zweck.

## Auffälligkeiten im Spiegel

- `sheets.md` erwähnt Liquid Glass nicht (nur watchOS-Material-Hintergrund) – keine HIG-Aussage zu Glass-Sheets verfügbar.
- `app-icons.md` nennt für Icon Composer Annotationen „default, dark, and mono“, an anderer Stelle Erscheinungsbilder „default, dark, clear, tinted“ – Terminologie inkonsistent.
- `materials.md` erwähnt `glassEffect(_:in:)` und `Glass.regular/.clear`, aber keine Container- oder Morphing-APIs; diese Angaben oben sind daher als Framework-Wissen markiert.
- Konkrete Darstellung bei Reduce Transparency ist im Spiegel nicht spezifiziert.
