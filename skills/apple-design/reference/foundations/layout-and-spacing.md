# Layout und Abstände

> Quelle: HIG-Spiegel `layout.md` (Apple-Update 2026-09-09 „Updated guidance to reflect current best practices“), `right-to-left.md`, am Rande `spatial-layout.md`; Kennwerte ergänzend aus `accessibility`, `widgets`, `live-activities`, `buttons`, `toolbars`, `sidebars`, `tab-bars`, `scroll-views`. Gespiegelt 2026-10-21. Paraphrasiert.

## Einordnung

Layout strukturiert Inhalt nach Wichtigkeit und muss sich an Displaygrößen, Ausrichtung, Fenstergrößen, Multitasking, Textgröße und Leserichtung anpassen. Grundlage sind **Safe Areas**, **Layout Guides/Margins** und **Size Classes** – nicht Gerätetyp oder Orientierung. Mit Liquid Glass gilt zusätzlich: Controls schweben in einer eigenen Ebene über dem Content; Content läuft bis an die Fensterkanten darunter durch.

> **Wichtig – Gerätespezifikationen:** Die aktuelle Fassung von `layout.md` im Spiegel (Stand Apple-Update 2026-09-09) enthält **keine** Gerätetabellen (iPhone/iPad/Mac/Watch: Auflösung, Punktgröße, Safe-Area-Insets, Size Classes je Modell) mehr – obwohl das Change Log frühere Ergänzungen bis iPhone 17 / Apple Watch Series 11 / Ultra 3 aufführt. Es werden hier daher keine Modelltabellen aus dem Gedächtnis ergänzt. Verfügbare Ersatz-Kennwerte aus anderen Seiten stehen unter „Kennwerte“. Aktuelle Gerätedaten (pt, px, Scale, Eckenradius je Modell): `python3 -I scripts/device_specs.py [--family iphone|ipad|watch]` – liest die Simulatorprofile aus Xcode. Safe-Area-Insets dort nicht enthalten → im Simulator/Preview messen oder `safeAreaInsets` zur Laufzeit.

## Kernregeln

### Visuelle Hierarchie
- Ordne nach Wichtigkeit: Wichtiges oben und auf der führenden Seite (leading); für RTL Systemkomponenten verwenden, die automatisch spiegeln. (hig:layout#Visual-hierarchy)
- Richte Elemente aus und nutze Einrückung, um Unterordnung auszudrücken. (hig:layout#Visual-hierarchy)
- Gruppiere Zusammengehöriges über Weißraum, Container-Formen oder Trennlinien. (hig:layout#Visual-hierarchy)
- Setze Progressive Disclosure ein (Disclosure-Dreiecke, Menüs, verschachtelte Views, scrollbare Sektionen). (hig:layout#Visual-hierarchy)
- Trenne Controls vom Content über Liquid Glass – keine soliden oder halbtransparenten Hintergrundflächen unter Controls, stattdessen Scroll Edge Effect. (hig:layout#Visual-hierarchy)
- Lass Vollbild-Hintergrundinhalte unter Sidebars, Toolbars und Tab Bars durchlaufen; verdecken Sidebars/Inspektoren wichtige Bildteile, Background Extension Effect nutzen (spiegelt und weichzeichnet das Bild darunter). (hig:layout#Visual-hierarchy, hig:sidebars#Best-practices)

### Adaptivität
- Unterstütze: Size Classes (horizontal/vertikal, compact/regular), Bildschirmgrößen, Orientierungen und Seitenverhältnisse, Dynamic Island, externe Displays, Display Zoom, frei skalierbare Fenster auf iPad und Mac, Textgrößen, Lokalisierung (LTR/RTL, Formate, Textlängen). (hig:layout#Adaptability)
- Respektiere Safe Areas, Margins und Guides; feinjustiere per Layout-Modifiern. (hig:layout#Adaptability)
- Auch orientierungsfixierte Apps (z. B. Landscape-Spiele) müssen sauber über Geräte und Fenstergrößen skalieren. (hig:layout#Adaptability)
- Plane Textgrößenänderungen ein: nebeneinanderliegende Views stapeln, Zeilen/Container wachsen in der Höhe, einzeilige Zeilen werden mehrzeilig. (hig:layout#Adaptability)
- Teste mit größtem und kleinstem Layout, verschiedenen Size Classes, Lokalisierungen und Textgrößen (Device Hub, inkl. iPad-Resize und iPhone Mirroring auf dem Mac). (hig:layout#Adaptability)
- Hintergrund-Artwork bei anderem Seitenverhältnis skalieren (füllen), nicht verzerren; bei sehr breiten/hohen Fenstern über den üblichen Sichtbereich hinaus anlegen. (hig:layout#Adaptability)

### Size Classes
- Entscheide Layout nach Size Class, **nicht** nach Gerätetyp (Idiom) oder Orientierung. (hig:layout#Size-classes)
- Berücksichtige alle Kombinationen aus compact/regular × compact/regular in Hoch- und Querformat. (hig:layout#Size-classes)
- Funktionalität bleibt bei Size-Class-Wechsel gleich; nur die sichtbare Menge ändert sich (z. B. Tab Bar → Sidebar, Overflow-Menü auflösen). (hig:layout#Size-classes)
- Das Idiom bleibt beim Resizing gleich – Layout muss plattformtypisch erkennbar bleiben. (hig:layout#Size-classes)

### Guides und Safe Areas
- **Layout Guide**: rechteckige Region zum Positionieren/Ausrichten; System liefert Guides für Standard-Margins und lesbare Textbreite, eigene Guides möglich. (hig:layout#Guides-and-safe-areas)
- **Safe Area**: Bereich, der nicht von Hardware (Dynamic Island, Kamera-Gehäuse) oder Bars (Toolbar, Tab Bar, Status Bar) verdeckt wird. Controls und kritischer Inhalt immer darin; Hintergründe dürfen darüber hinaus laufen. (hig:layout#Guides-and-safe-areas)

### Abstände und Gruppierung
- Abstand zwischen Controls ist so wichtig wie deren Größe: ca. **12 pt** Padding um Elemente mit Bezel, ca. **24 pt** um Elemente ohne Bezel (gemessen an sichtbaren Kanten). (hig:accessibility)
- Standard-Komponenten in Toolbars haben zu den Bar-Ecken konzentrische Eckradien; Custom-Komponenten ebenso konzentrisch gestalten. (hig:toolbars#Best-practices)
- Toolbar-Items nach Funktion und Häufigkeit gruppieren: leading (Zurück, Sidebar, Titel, Dokumentmenü – nicht anpassbar), Mitte (häufige Controls, anpassbar, kollabieren ins Overflow-Menü), trailing (wichtige Items, Inspektoren, Suche, More-Menü, Primäraktion – immer sichtbar). (hig:toolbars#Item-groupings)
- Scroll Edge Effect nur hinter schwebenden Elementen, einer pro View; in Split Views je Pane einer, gleich hoch. (hig:scroll-views#Scroll-edge-effects)

### Right-to-left (hig:right-to-left)
- Systemframeworks spiegeln Standardkomponenten automatisch; Eigenes gezielt nachziehen.
- Textausrichtung an Interface-Richtung anpassen; Absätze (≥ 3 Zeilen) aber nach **ihrer Sprache** ausrichten; Listen einheitlich ausrichten.
- Ziffernfolge einer Zahl (Telefon-, Kartennummer) nie umdrehen; Reihenfolge von Fortschritts-/Zählsequenzen schon – Ziffern selbst nie spiegeln.
- Spiegeln: Slider, Fortschrittsanzeigen, Zurück/Weiter, Icons mit Lese- oder Bewegungsrichtung, geordnete Bildfolgen.
- Nicht spiegeln: Fotos/Illustrationen, Logos, universelle Zeichen (Häkchen), reale Objekte (Uhr), Controls mit echter Richtung („nach rechts“).
- Arabisch/Hebräisch neben Latein-Versalien ca. 2 pt größer setzen.
- Komplexe Icons komponentenweise prüfen (Badge, Schrägstrich, Werkzeug-Händigkeit); SF Symbols liefern RTL- und lokalisierte Varianten.

## Kennwerte

### Control-Größen (hig:accessibility, hig:buttons#Best-practices)

| Plattform | Standard-Control | Minimum |
|---|---|---|
| iOS, iPadOS | 44×44 pt | 28×28 pt |
| macOS | 28×28 pt | 20×20 pt |
| tvOS | 66×66 pt | 56×56 pt |
| visionOS | 60×60 pt | 28×28 pt |
| watchOS | 44×44 pt | 28×28 pt |

Buttons: Trefferfläche mind. 44×44 pt (visionOS 60×60 pt). visionOS: Button-Zentren mind. 60 pt auseinander; Button-Größen Mini 28 / Small 32 / Regular 44 / Large 52 / Extra large 64 pt. (hig:buttons, hig:layout#visionOS)

Hinweis: `accessibility` nennt für visionOS ein Minimum von 28×28 pt, `buttons` eine Trefferfläche von mindestens 60×60 pt – Minimum = kleinste zulässige Control-Größe, 60×60 = empfohlene Hit Region.

### Screen-Größen (Punkte, Hochformat) – nur indirekt im Spiegel

Der Spiegel nennt Bildschirmgrößen nur als Bezugsgröße für Widget-Spezifikationen, **ohne Modellzuordnung**. Nicht als vollständige Geräteliste verwenden.

| iPhone (pt, portrait) laut `widgets#Specifications` |
|---|
| 430×932 · 428×926 · 414×896 · 414×736 · 393×852 · 390×844 · 375×812 · 375×667 · 360×780 · 320×568 |

| iPad (pt, portrait) laut `widgets#Specifications` |
|---|
| 768×1024 · 744×1133 · 810×1080 · 820×1180 · 834×1112 · 834×1194 · 1024×1366 · mit Display Zoom „More Space“: 954×1373 · 970×1389 · 1192×1590 |

`live-activities#Specifications` listet iPad-Maße unter „portrait“ teils im Querformat (1366×1024, 1194×834, 1012×834, 1080×810, 1024×768) – Widerspruch in der Quelle; 1012×834 taucht in der Widget-Liste nicht auf.

| Apple Watch Gehäuse | Smart-Stack-Widget (pt) |
|---|---|
| 40 mm | 152×69.5 |
| 41 mm | 165×72.5 |
| 42 mm | 176×72.5 |
| 44 mm | 173×76.5 |
| 45 mm | 184×80.5 |
| 46 mm | 194×80.5 |
| 49 mm (Ultra 3, 4) | 198×81.5 (nur in `live-activities`, fehlt in `widgets`) |

Mac: keine Bildschirm- oder Fenstergrößen im Spiegel. watchOS-Display-Auflösungen: nicht im Spiegel.

### tvOS (Rand)
Safe Area: Inhalt 60 pt oben/unten, 80 pt seitlich einrücken. Grids (unfokussierte Breite / horizontaler Abstand 40 pt / vertikal mind. 100 pt): 2 Spalten 860 pt · 3: 560 · 4: 410 · 5: 320 · 6: 260 · 7: 217 · 8: 184 · 9: 160 pt. (hig:layout#tvOS)

## Plattform-Unterschiede

### iOS
- Size Classes primär; iPhone in Landscape kann compact height haben. Dynamic Island und Bars über die Safe Area respektieren. (hig:layout)
- Tab Bar schwebt unten auf Liquid Glass; kann beim Scrollen minimieren (Accessory inline). (hig:tab-bars#iOS)
- Large Title in der Toolbar, wechselt beim Scrollen zum Standardtitel. (hig:toolbars#iOS)

### iPadOS
- Fenster frei skalierbar, alle Size-Class-Kombinationen möglich; Tab Bar oben, optional in Sidebar umwandelbar (`sidebarAdaptable`); Toolbar und Tab Bar können sich die obere Zeile teilen. (hig:tab-bars#iPadOS, hig:toolbars#iPadOS)
- Sidebar: max. zwei Hierarchieebenen, sonst Split View mit Content-Liste. (hig:sidebars)
- Standard-Präsentation von Sheets: Page oder Form Sheet. (hig:sheets#iOS-iPadOS)

### macOS
- Keine Controls oder kritischen Infos am unteren Fensterrand (Fenster werden oft unter den Bildschirmrand geschoben) – gilt auch für Sidebars. (hig:layout#macOS, hig:sidebars#macOS)
- Keinen Inhalt hinter dem Kameragehäuse am oberen Rand (`NSPrefersDisplaySafeAreaCompatibilityMode`). (hig:layout#macOS)
- Sidebar ggf. bei kleinem Fenster automatisch einklappen; Zeilenhöhe hängt von Sidebar-Größe (Systemeinstellung) ab. (hig:sidebars#macOS)
- Jedes Toolbar-Item auch als Menübefehl anbieten. (hig:toolbars#macOS)

### watchOS
- Höchstens drei Glyph-Buttons oder zwei Text-Buttons nebeneinander; Text-Buttons am besten volle Breite; zwei nebeneinander nur ohne Scrollen. (hig:layout#watchOS)
- Autorotation in Views, die man anderen zeigt (Bild, QR-Code). (hig:layout#watchOS)
- Toolbar-Buttons oben in den Ecken oder unten; Content scrollt darunter. (hig:toolbars#watchOS)

### visionOS (Rand)
- Fenster/Volumes resizable halten, bei großen Größen Inhalt horizontal zentrieren; Min-/Max-Größen nur gegen Überlappung, nicht gegen Resizing. (hig:layout#visionOS)
- 3D in Fenstern sparsam und eingerückt; Zusatzinhalte in ein Nachbarfenster statt Ornament. (hig:layout#visionOS)
- Wichtiges im Sichtfeld zentrieren, Inhalte nicht am Kopf verankern, Tiefe für Hierarchie, aber nicht für Text. Punkte sind in visionOS Winkelmaße (Dynamic Scale). (hig:spatial-layout)

## Umsetzung

**SwiftUI**
```swift
@Environment(\.horizontalSizeClass) var hSize      // UserInterfaceSizeClass
var body: some View {
    if hSize == .compact { TabView { … } } else { NavigationSplitView { … } detail: { … } }
}
// Adaptive Navigation in einem Schritt
TabView { … }.tabViewStyle(.sidebarAdaptable)
// Safe Area: Hintergrund darf raus, Inhalt bleibt drin
content.background { Image("hero").resizable().scaledToFill().ignoresSafeArea() }
// Inhalt unter Sidebar „verlängern“
Image("hero").backgroundExtensionEffect()
// Scroll Edge Effect (Stil nur bei Bedarf ändern)
ScrollView { … }.scrollEdgeEffectStyle(.soft, for: .top)
// Textgröße → Stapeln
ViewThatFits { HStack { … }; VStack { … } }
```
- `safeAreaInset(edge:)` / `safeAreaPadding` für eigene schwebende Leisten; `ContainerRelativeShape` für konzentrische Ecken (in `live-activities` genannt).
- RTL: `.leading/.trailing` statt `.left/.right`; `Image(systemName:)` spiegelt automatisch, eigene Assets mit Direction „Left to Right, Mirrors“ im Asset Catalog. Vorschau mit `\.layoutDirection`.

**UIKit**
- `safeAreaLayoutGuide`, `layoutMarginsGuide`, `readableContentGuide` (lesbare Textbreite), `UILayoutGuide`; Trait-Änderungen über `UITraitChangeObservable` / `registerForTraitChanges`.
- `UIBackgroundExtensionView`, `UIScrollEdgeEffect.Style`, `UITabBarController.MinimizeBehavior`.
- Leading/Trailing-Constraints statt Left/Right; `semanticContentAttribute` für Sonderfälle.

**AppKit**
- `NSLayoutGuide`, Auto Layout; `NSScrollEdgeEffectStyle`; Split View mit einklappbarer Sidebar.

> API-Namen aus dem Spiegel: `backgroundExtensionEffect()`, `UIBackgroundExtensionView`, `SafeAreaRegions`, `UILayoutGuide`, `NSLayoutGuide`, `UITraitChangeObservable`, `UserInterfaceSizeClass`, `ScrollEdgeEffectStyle`, `TabBarMinimizeBehavior`, `sidebarAdaptable`, `isAutorotating`, `defaultWindowPlacement(_:)`. Übrige Namen (`readableContentGuide`, `safeAreaInset`, `ViewThatFits`, `scrollEdgeEffectStyle(_:for:)`) sind Framework-Wissen.

## Review-Checkliste

- [ ] Wichtigstes oben/leading; Ausrichtung und Einrückung bilden Hierarchie ab
- [ ] Gruppen über Weißraum/Container/Trenner klar erkennbar
- [ ] Layout entscheidet per Size Class, nicht per Gerät/Orientierung
- [ ] Alle vier Size-Class-Kombinationen geprüft; Funktionalität identisch
- [ ] Controls und Text innerhalb der Safe Area; Hintergründe randlos
- [ ] Keine Flächen hinter Bars; Scroll Edge Effect nur hinter schwebenden Elementen, einer pro View
- [ ] Hintergrund-Content läuft unter Sidebar/Toolbar/Tab Bar (ggf. Background Extension Effect)
- [ ] Trefferflächen ≥ Plattform-Standard (iOS 44×44 pt), Minimum nie unterschritten
- [ ] Padding ~12 pt (mit Bezel) / ~24 pt (ohne Bezel)
- [ ] Größte Dynamic-Type-Stufe: Stapeln statt Überlappen
- [ ] iPad: freies Resizing getestet (schmal bis breit), Tab Bar ↔ Sidebar
- [ ] macOS: nichts Kritisches am unteren Fensterrand, nichts hinter Kameragehäuse
- [ ] watchOS: max. 3 Glyph- / 2 Text-Buttons pro Zeile
- [ ] RTL: gespiegelt, wo Richtung Bedeutung trägt; Zahlen, Logos, Fotos unverändert
- [ ] Getestet in kleinstem und größtem Gerät/Fenster, mit langen Lokalisierungen

## Anti-Patterns

- `if UIDevice.current.userInterfaceIdiom == .pad` als Layout-Entscheidung.
- Feste Frames für Screens einer bestimmten iPhone-Größe.
- Halbtransparenter Balken unter einer Toolbar „für Lesbarkeit“ statt Scroll Edge Effect.
- Inhalt endet hart an der Sidebar-Kante statt darunter weiterzulaufen.
- Funktionen verschwinden in Compact Width ersatzlos.
- Speichern-Button unten links im Mac-Fenster.
- `.left/.right`-Constraints; gespiegelte Logos oder Telefonnummern im RTL-Modus.
- Mehr als drei Icon-Buttons nebeneinander auf der Watch.
- Gerätespezifikationen aus dem Gedächtnis in Mockups übernehmen statt aus `device_specs.py` bzw. den UI-Kits der Apple Design Resources.
