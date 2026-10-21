# iPadOS (iPad) – Plattformreferenz

> Quelle: lokaler HIG-Spiegel `~/.apple-design/hig/pages/<slug>.md` (Stand 2026-10-21). Belege als `(hig:<slug>)` bzw. `(hig:<slug>#Anchor)`.
> Paraphrasiert und verdichtet. Zahlen nur, wenn sie im Spiegel stehen. Viele Regeln gelten für iOS und iPadOS gemeinsam – siehe `ios.md`; hier stehen die iPad-spezifischen Punkte und die gemeinsamen nur, soweit sie auf dem iPad anders wirken.

---

## 1. Kurzprofil

- **Display:** groß, hochauflösend; App läuft **full screen** oder **windowed** (frei skalierbare Fenster, mehrere gleichzeitig) (hig:designing-for-ipados, hig:windows#iPadOS).
- **Ergonomie:** gehalten, auf dem Tisch oder im Ständer; Sehabstand meist innerhalb von etwa drei Fuß. Dichte und Größe an Sehabstand und Eingabeart ausrichten (hig:designing-for-ipados).
- **Eingabe:** Multi-Touch, virtuelle oder Hardware-Tastatur, Trackpad/Maus (Pointer), Apple Pencil, Sprache; oft kombiniert (hig:designing-for-ipados).
- **Nutzung:** kurze Aktionen bis zu stundenlangen Produktiv-, Kreativ- und Mediensessions; mehrere Apps sichtbar, Drag and Drop zwischen Apps (hig:designing-for-ipados).
- **Systemfeatures:** Multitasking/Fenster, Widgets (inkl. extra large), Drag and Drop, Menüleiste (hig:designing-for-ipados, hig:the-menu-bar#iPadOS).
- **Ziel:** großen Screen für Inhalt nutzen, Modals und Vollbild-Übergänge minimieren, Controls erreichbar, aber nicht im Weg; nahtlos auch auf dem Mac lauffähig (hig:designing-for-ipados).

---

## 2. Nicht verhandelbar

1. **Fenster fluid skalierbar gestalten.** Jede Breite von schmal (compact) über mittlere Breiten bis voll muss funktionieren; die App erfährt nicht, welche Multitasking-Konfiguration gewählt wurde (hig:multitasking#iPadOS, hig:windows#Best-practices).
2. **Layout über Size Classes, nicht über Gerät/Orientierung**; Funktionalität bleibt bei jeder Größe gleich, nur die sichtbare Menge ändert sich (hig:layout#Size-classes).
3. **Window Controls nicht überdecken:** leading Toolbar-Items nach innen rücken, wenn Fensterkontrollen erscheinen (hig:windows#iPadOS).
4. **Keine eigenen Fensterrahmen/Window-Controls** nachbauen; im UI-Text „Fenster“ sagen, nicht „Scene“ (hig:windows#Best-practices).
5. **Tab Bar bevorzugen** (oben, ggf. in Sidebar wandelbar); Sidebar nur bei komplexer Struktur bzw. per `sidebarAdaptable` (hig:tab-bars#iPadOS, hig:sidebars#iOS-iPadOS).
6. **Sidebar nicht standardmäßig ausblenden**, Edge-Swipe zum Ein-/Ausblenden respektieren, max. zwei Hierarchieebenen (hig:sidebars#Best-practices).
7. **Split View: aktuelle Auswahl in jeder Spalte persistent hervorheben**; Navigation zwischen Spalten auch in schmalen Fenstern logisch (hig:split-views).
8. **Pointer unterstützt Touch, ersetzt ihn nicht**; System-Pointer-Effekte (highlight/lift/hover) für Standard- und standardähnliche Elemente (hig:pointing-devices#iPadOS).
9. **Standard-Tastaturkürzel nicht umdefinieren**; Full Keyboard Access unterstützen; keine eigene Tastaturnavigation für Buttons/Switches/Segmented Controls (hig:keyboards).
10. **Alle Funktionen auch ohne Menüleiste erreichbar** – die Menüleiste ist meist versteckt und nur mit Hardware-Tastatur voll nutzbar (hig:the-menu-bar#iPadOS).
11. **Popovers für regular width, Sheets in Form-/Page-Sheet-Stil**; in compact automatisch zu Sheet (hig:popovers#iOS-iPadOS, hig:sheets#iOS-iPadOS).
12. **Hit-Targets 44×44 pt Standard / 28×28 pt Minimum** – auch mit Pointer (hig:accessibility#Mobility).
13. **Liquid Glass nur für die Funktionsebene**; Inhalt unter Sidebar/Toolbar durchlaufen lassen (hig:materials#Liquid-Glass, hig:sidebars#Best-practices).
14. **Apple Pencil: sofort markieren, kein Modus-Zwang; Hover/Double-Tap/Squeeze nie destruktiv** (hig:apple-pencil-and-scribble).
15. **Dynamic Type, Dark Mode, Orientierung und Multitasking-Modi nahtlos** (hig:designing-for-ipados).

---

## 3. Layout & Maße

### 3.1 Belegte Kennwerte

| Kennwert | Wert | Quelle |
|---|---|---|
| Control-Größe Standard / Minimum | 44×44 pt / 28×28 pt | (hig:accessibility#Mobility) |
| Pointer-Hit-Region: Padding um Element mit Bezel | ca. 12 pt | (hig:pointing-devices#Standard-pointers-and-effects) |
| Pointer-Hit-Region: Padding ohne Bezel | ca. 24 pt um sichtbare Kanten | (hig:pointing-devices#Standard-pointers-and-effects) |
| Text Standard / Minimum | 17 pt / 11 pt | (hig:typography#Ensuring-legibility) |
| Toolbar-Titel | unter 15 Zeichen | (hig:toolbars#Titles) |
| Toolbar-Gruppen | max. ca. 3 (auch auf iPad) | (hig:toolbars#Item-groupings) |
| Anpassbare Tab-Bar: Default-Tabs | 5 oder weniger | (hig:tab-bars#iPadOS) |
| Sidebar-Hierarchie | max. 2 Ebenen, sonst Split View mit Content-Liste | (hig:sidebars#Best-practices) |
| Split-View-Spalten | 2 (z. B. Mail) oder 3 (z. B. Keynote) | (hig:split-views#iPadOS) |
| Drag-Image ab | ca. 3 pt Bewegung | (hig:drag-and-drop#Providing-feedback) |
| App-Icon | 1024×1024 px, quadratisch, Systemmaske | (hig:app-icons#Specifications) |

### 3.2 Gerätegrößen / Safe Areas

**Im Spiegel nicht enthalten.** `layout.md` (Update 2026-09-09) enthält keine Gerätetabelle und keine Safe-Area-Insets (das Change Log nennt frühere Spezifikationen für iPad 11", iPad Air 11"/13", iPad mini 8,3", iPad Air 10,9"). Safe Areas zur Laufzeit beziehen, nicht hart kodieren (hig:layout#Guides-and-safe-areas).

Indirekt belegte iPad-Bildschirmgrößen (Portrait, pt) aus der Widget-Tabelle, **ohne Gerätezuordnung**: 768×1024, 744×1133, 810×1080, 820×1180, 834×1112, 834×1194, 1024×1366; mit Display Zoom „More Space“: 954×1373, 970×1389, 1192×1590 (hig:widgets#Specifications).

### 3.3 Size Classes auf dem iPad
(hig:layout#Size-classes)
- Fenster können in **jeder** Kombination aus compact/regular in Breite und Höhe erscheinen (schmal-kurz, schmal-hoch, breit-kurz, breit-hoch).
- Nicht nur für Landscape-iPhone (regular width/compact height) oder Portrait-compact designen; vertikalen Platz in regular height nutzen.
- Bei mehr Platz: Tab Bar → Sidebar, Overflow-Items ausklappen. Idiom bleibt gleich → Layout bleibt iPad-typisch erkennbar.
- Sehr breite/flache und schmale/hohe Fenster: Hintergrundartwork über den „Standard“-Ausschnitt hinaus anlegen (hig:layout#Adaptability).
- Testen u. a. mit Device Hub, insbesondere kleinste und größte Fenster (hig:layout#Adaptability).

### 3.4 Visuelle Hierarchie
- Wichtiges oben/leading; Inhalt elevieren, Controls nicht im Weg (hig:layout#Visual-hierarchy, hig:designing-for-ipados).
- Vollflächige Hintergründe unter Sidebar, Toolbar, Tab Bar; ggf. Background Extension Effect unter Sidebar/Inspector (hig:layout#Visual-hierarchy).

---

## 4. Navigation & Struktur

### 4.1 Entscheidungsmatrix

| Situation | Muster | Quelle |
|---|---|---|
| Wenige Hauptbereiche | **Tab Bar oben** (fest, `tabBarOnly`) | (hig:tab-bars#iPadOS) |
| Viele Bereiche, komplexere App | **Tab Bar, in Sidebar wandelbar** (`sidebarAdaptable`), anpassbar | (hig:tab-bars#iPadOS, hig:sidebars#iOS-iPadOS) |
| Nur Sidebar, ohne Umschalten | **NavigationSplitView / UISplitViewController** | (hig:sidebars#iOS-iPadOS, hig:tab-bars#iPadOS) |
| Hierarchie > 2 Ebenen | **Split View** mit 2–3 Spalten (Sidebar – Liste – Detail) | (hig:sidebars#Best-practices, hig:split-views#iPadOS) |
| Hauptbereiche + volle Breite für Inhalt | **Tab Bar + Toolbar in derselben Zeile oben** | (hig:toolbars#iPadOS) |
| Eng umrissene Teilaufgabe | **Sheet** (Form/Page Sheet) | (hig:sheets#iOS-iPadOS) |
| Kontextoptionen zu einem Element (regular) | **Popover** | (hig:popovers#iOS-iPadOS) |
| Eigenständige Aufgabe parallel zum Kontext | **neues Fenster** (z. B. Mail-Compose) | (hig:windows#Best-practices, hig:modality) |
| Objekt neu anlegen „im Leerraum“ | **Context Menu** (Long Press / Sekundärklick) | (hig:context-menus#iOS-iPadOS) |
| Optionsauswahl in Popover/Modal für Listeneintrag | **Pop-up Button** statt Disclosure-Drilldown | (hig:pop-up-buttons#iPadOS) |

### 4.2 Tab Bar (iPadOS)
(hig:tab-bars, hig:tab-bars#iPadOS)
- Liegt **oben**; entweder fest oder mit Button zur Umwandlung in eine Sidebar.
- **Anpassbar machen** bei vielen Bereichen (Nutzer pinnt z. B. Playlist als Tab); Default ≤ 5 Tabs für Kontinuität zwischen compact und regular.
- In regular: Icon und Label nebeneinander; in compact: Icon über Label.
- Allgemeine Regeln wie iOS: nur Navigation, sichtbar halten, nicht deaktivieren, Labels, Badges sparsam.
- In der Menüleiste: jeden Tab als Eintrag im View-Menü, ggf. mit Tastenkürzel (hig:the-menu-bar#iPadOS).

### 4.3 Sidebar
(hig:sidebars)
- Leading, schwebt in der Liquid-Glass-Ebene; Inhalt darunter scrollen lassen oder Background Extension Effect.
- Inhalte vom Nutzer anpassbar; Gruppen mit Disclosure Controls; SF Symbols bzw. Custom Symbols statt Bitmaps.
- Icons in Akzentfarbe; feste Farben nur sparsam mit Bedeutung (z. B. VIP gelb).
- Zwei Ebenen mit knappen Gruppentiteln; tiefer → Split View mit Content-Liste.
- Ausblenden per System-Edge-Swipe; nicht standardmäßig versteckt.
- Ohne SwiftUI: `UICollectionLayoutListConfiguration.Appearance.sidebar` (hig:sidebars#iOS-iPadOS).
- Suche oben in der Sidebar, wenn sie die Sidebar filtert (Settings-Muster) (hig:search-fields#iPadOS-macOS).

### 4.4 Split View
(hig:split-views)
- 2 oder 3 vertikale Spalten; Auswahl pro Spalte sichtbar halten; Drag and Drop zwischen Spalten.
- **Schmale, mittlere, breite Fensterbreiten** durchspielen – Spalten müssen kollabieren und logisch navigierbar bleiben.
- Je Spalte ein eigener Scroll Edge Effect, Höhen konsistent halten (hig:scroll-views#Scroll-edge-effects).

### 4.5 Toolbar (iPadOS)
(hig:toolbars)
- Toolbar und Tab Bar können oben dieselbe Zeile teilen.
- **Overflow-Menü legt das System automatisch an**, nicht manuell bauen; Layouts vermeiden, die standardmäßig überlaufen. Center-Items kollabieren beim Verkleinern ins Overflow; trailing Items bleiben immer sichtbar; leading Items sind nicht anpassbar.
- **Toolbar-Anpassung** anbieten bei vielen Items oder langen Sessions.
- Leading: Back, Sidebar-Toggle, Titel, Dokumentmenü (Duplicate, Rename, Move, Export). Trailing: Inspector-Buttons, Suche, More, primäre Aktion.
- Fensterkontrollen erscheinen windowed am leading Rand der Toolbar → leading Buttons einrücken (hig:windows#iPadOS).
- Titel: aussagekräftig je Fenster, damit mehrere Fenster unterscheidbar sind; nicht App-Name (hig:toolbars#Titles).

### 4.6 Fenster & Multitasking
(hig:windows#iPadOS, hig:multitasking#iPadOS)
- **Full screen:** Fenster füllen den Bildschirm, Wechsel über App-Switcher. **Windowed:** frei skalierbar, mehrere sichtbar, verschiebbar; System merkt sich Größe/Position. Systemsteuerung für Kacheln, Vollbild, Minimieren, Schließen; vorderstes Fenster mit farbigen Controls und Schatten.
- Picture in Picture für Video/FaceTime in beiden Modi.
- Primär- vs. Hilfsfenster: Hilfsfenster ohne App-Navigation, mit Schließen-Button (hig:windows).
- Neue Fenster gezielt (Compose, Dokument), nicht standardmäßig; „In neuem Fenster öffnen“ per Context Menu oder File-Menü; Pinch-to-open-in-new-window erwägen (hig:windows).
- Tipp im Spiegel: Wer nur eine Datei anzeigen will, kann Quick Look nutzen, **muss aber Mehrfenster unterstützen** (hig:windows#iPadOS).
- Multitasking-Grundregeln: Kontext sichern, Medien/Spiele pausieren, Audio-Unterbrechungen korrekt behandeln, Hintergrundaufgaben fertigstellen, Notifications sparsam (hig:multitasking#Best-practices).

### 4.7 Sheets & Modality (iPadOS)
- **Page- oder Form-Sheet** bevorzugen (Default-Größe, zentriert, gedimmter Hintergrund) (hig:sheets#iOS-iPadOS).
- Buttons wie iOS: Cancel leading, Done trailing; Multi-Step mit Back (hig:sheets#iOS-iPadOS).
- Nichtmodale Sheets möglich, wenn der Parent bearbeitet wird (hig:sheets#Anatomy).
- Modals minimieren; für parallele Aufgaben eher Fenster (hig:designing-for-ipados, hig:modality).
- Dark Mode: Vordergrund-Modals nutzen automatisch *elevated* Hintergründe, auch zur Trennung zwischen Fenstern/Apps (hig:dark-mode#iOS-iPadOS).

### 4.8 Suche (iPadOS)
(hig:search-fields#iPadOS-macOS)
- Standard: Suchfeld **trailing in der Toolbar** (Split-View-Apps wie Mail, Notes).
- Oben in der Sidebar, wenn die Suche die Sidebar filtert.
- Eigener Bereich (Sidebar-Item/Tab), wenn Suche mit Entdecken verbunden ist (Music, TV); Feld dort sofort fokussieren – **außer** nur die virtuelle Tastatur ist verfügbar.
- Feld skaliert mit dem Fenster; in compact über der Content-Liste platzieren.
- Konsistent mit der Mac-Version halten.

---

## 5. Komponenten-Besonderheiten (Platform considerations iPadOS)

### 5.1 Pointer (Trackpad/Maus)
(hig:pointing-devices#iPadOS)
- Pointer ist Zusatz zu Touch. Standardform Kreis; I-Beam über Text automatisch.
- **Content Effects:** *highlight* (kleine Elemente mit transparentem Hintergrund; Default für Bar-Buttons, Tab Bars, Segmented Controls, Edit Menus), *lift* (kleine Elemente mit opakem Hintergrund; App-Icons, Control-Center-Buttons), *hover* (große Elemente; Skalierung/Tint/Schatten selbst definieren).
- **Magnetismus** bei highlight/lift und Textbereichen, nicht bei hover.
- Hit-Regionen: ca. 12 pt Padding mit Bezel, ca. 24 pt ohne; benachbarte Bar-Buttons mit **lückenlosen** Hit-Regionen.
- Bei lift auf nicht standardförmigen Elementen Eckradius angeben.
- Band-Selektion (Ziehen über mehrere Items) in Custom Views selbst implementieren.
- Pointer vs. Finger nur unterscheiden, wenn es Mehrwert bringt (z. B. präzises Scrubbing).
- Keine dekorativen Pointer-Effekte, kein Anleitungstext am Pointer; Annotationen mit echtem Nutzen (z. B. X/Y-Werte) ok.
- Hover-Effekte: Skalierung nur mit Platz drumherum; Schatten nie ohne Skalierung; Tabellenzeilen nur Tint.
- Pointer Accessories: einfache Bilder, Übergänge für Zustandswechsel (z. B. `plus` → `circle.slash`).

### 5.2 Tastatur & Fokus
- Fokussystem mit **Fokusgruppen**: Tab wechselt zwischen Gruppen (Sidebar, Grid, Liste), Pfeiltasten innerhalb einer Gruppe; Reihenfolge leading→trailing, oben→unten (hig:focus-and-selection#iPadOS).
- Fokusanzeige: Halo (Focus Ring, anpassbar per `UIFocusHaloEffect`) oder Highlight in Akzentfarbe; Primary Item per Priorität (hig:focus-and-selection#iPadOS).
- Tastaturnavigation in Textfeldern, Text Views, Sidebars, Collections; **nicht** für Buttons, Segmented Controls, Switches – dafür Full Keyboard Access (hig:keyboards).
- Standardkürzel respektieren; eigene nur für häufige Befehle; Modifier-Reihenfolge Control, Option, Shift, Command; kein Shift bei Zeichen, die Shift ohnehin brauchen (hig:keyboards#Custom-keyboard-shortcuts).
- Beim Drop Option-Taste prüfen (erzwingt Kopie) (hig:drag-and-drop#Accepting-drops).

### 5.3 Menüleiste (iPadOS)
(hig:the-menu-bar#iPadOS)
- Erscheint durch Pointer an die obere Kante oder Wischen von oben; belegt die Höhe der Statusleiste; zentriert; keine Menu Bar Extras, kein Apple-Menü; App-Menü ohne About/Services; Fensterkontrollen in der Menüleiste, wenn die App full screen läuft.
- Kein Sammelbecken für sonst nicht platzierbare Funktionen; dynamische Menüeinträge immer auch anders erreichbar.
- *App > Settings* öffnet die App-Seite in den iPadOS-Einstellungen; eigene Einstellungen als separaten Eintrag darunter.
- Häufiger Untermenüs nutzen als am Mac (Menüzeilen sind auf dem iPad höher).

### 5.4 Apple Pencil & Scribble
(hig:apple-pencil-and-scribble)
- Sofort markieren, ohne Werkzeugwahl oder Modus; Controls auch per Pencil bedienbar.
- Tilt, Druck, Azimut, Barrel Roll für Ausdruck nutzen; direkte, unmittelbare Rückmeldung.
- Links- und Rechtshänder: Controls nicht unter der Hand; ggf. verschiebbar.
- **Hover:** nur Vorschau (Größe/Farbe des Strichs), nie Aktion auslösen; Vorschau nur für Pencil, nicht Pointer.
- **Double Tap:** Nutzereinstellung respektieren (Default: Werkzeug ↔ Radierer); nie Inhalt verändern.
- **Squeeze:** einzelne diskrete Aktion, UI nahe der Pencil-Spitze, nicht-destruktiv/undo-fähig.
- **Barrel Roll:** nur Strichverhalten modifizieren, keine Navigation.
- **Scribble:** funktioniert in Standard-Textkomponenten (nicht Passwortfelder); Feld beim Schreiben nicht bewegen, kein Autoscroll, keine störende Autovervollständigung, genug Schreibfläche.
- PencilKit: Tool Picker hat Undo/Redo nur in regular; in compact eigene Undo/Redo-Buttons.

### 5.5 Weitere Komponenten

| Komponente | iPad-spezifische Regel | Quelle |
|---|---|---|
| Context Menu | Long Press oder Sekundärklick; gut zum Anlegen neuer Objekte im Leerraum | (hig:context-menus#iOS-iPadOS) |
| Edit Menu | vertikaler Stil bei Tastatur/Pointer, horizontaler bei Touch – beides prüfen | (hig:edit-menus#iOS-iPadOS) |
| Drag and Drop | mehrere gleichzeitige Drags; Items während des Drags hinzufügen (Flocking), mehrere Drops annehmen; Spring Loading | (hig:drag-and-drop#iOS-iPadOS, hig:drag-and-drop) |
| Page Control | Pointer kann einzelne Indikatoren anwählen | (hig:page-controls#iOS-iPadOS) |
| Pop-up Button | in Popover/Modal statt Disclosure für kleine Optionsmengen | (hig:pop-up-buttons#iPadOS) |
| Popover | nur in regular width | (hig:popovers#iOS-iPadOS) |
| Gesten | Vier-Finger-Swipe = App-Wechsel (System, nicht belegen); Drei-Finger-Undo/Copy wie iOS | (hig:gestures#iOS-iPadOS) |
| Menüs | small/medium/large Layout wie iOS | (hig:menus#iOS-iPadOS) |
| Toolbars | Anpassung durch Nutzer, System-Overflow | (hig:toolbars) |
| Dateien | Document Launcher (ab iPadOS 18); File-Provider-Extension ohne eigene Top-Toolbar | (hig:file-management#iOS-iPadOS) |
| SharePlay | geteiltes Video in Picture in Picture weiterspielen | (hig:shareplay#iOS-iPadOS-macOS) |
| Sonstige gemeinsame Regeln | Action Sheets, Alerts, Toggles, Slider, Text Fields, Pickers, Refresh, Haptik → siehe `ios.md` Abschnitt 5 | |

---

## 6. Liquid Glass & Materialien

- Liquid Glass = Funktionsebene (Tab Bar, Toolbar, **Sidebar**); Standardmaterialien (ultraThin, thin, regular, thick) für den Content Layer (hig:materials, hig:materials#iOS-iPadOS).
- **Sidebar** ist größeres Glass-Element → erscheint opaker zur Lesbarkeit; Tab Bar/Toolbar wechseln automatisch hell/dunkel mit monochromen Symbolen (hig:color#Liquid-Glass-color).
- Inhalt unter Sidebar und Toolbar laufen lassen; Bildhintergründe per **Background Extension Effect** spiegeln (hig:sidebars#Best-practices, hig:layout#Visual-hierarchy).
- Regular-Variante für textreiche Elemente (Sidebars, Popovers, Alerts); clear nur über Medien, bei hellem Inhalt 35-%-Dimming (hig:materials#Liquid-Glass).
- Scroll Edge Effect: in Split Views **pro Spalte einer**, Höhen angleichen; automatic bevorzugen (hig:scroll-views#Scroll-edge-effects).
- Keine eigenen Toolbar-Hintergründe/Tönungen; eine prominente Aktion mit getöntem Hintergrund (hig:toolbars#Best-practices, hig:color#Liquid-Glass-color).
- Vibrancy: Labels label…quaternaryLabel (quaternary nicht auf thin/ultraThin), Fills, Separator (hig:materials#iOS-iPadOS).
- Custom Komponenten in Bars: Eckradien konzentrisch (hig:toolbars#Best-practices).
- App-Icon geschichtet mit Glass-Effekten, Varianten default/dark/clear/tinted (hig:app-icons).

---

## 7. Typografie & Dynamic Type

- SF Pro und New York; Default 17 pt, Minimum 11 pt; Dynamic Type mit denselben Tabellen wie iOS (`typography.md` führt „iOS, iPadOS“ gemeinsam) (hig:typography#iOS-iPadOS, hig:typography#Specifications).
- Größerer Sehabstand (bis ca. drei Fuß) → Größe und Dichte bewusst wählen, nicht einfach iPhone-Maße hochskalieren (hig:designing-for-ipados).
- Bei großen Textgrößen Spaltenzahl reduzieren (mehrspaltige Layouts sind auf dem iPad häufiger) (hig:typography#Supporting-Dynamic-Type).
- Nicht alles mitskalieren: z. B. Tab-Titel müssen nicht wachsen, Inhalt schon (hig:typography#Conveying-hierarchy).

### Default „Large“ (pt)
(hig:typography#Specifications)

| Style | Gewicht | Größe | Leading | Emphasized |
|---|---|---|---|---|
| Large Title | Regular | 34 | 41 | Bold |
| Title 1 | Regular | 28 | 34 | Bold |
| Title 2 | Regular | 22 | 28 | Bold |
| Title 3 | Regular | 20 | 25 | Semibold |
| Headline | Semibold | 17 | 22 | Semibold |
| Body | Regular | 17 | 22 | Semibold |
| Callout | Regular | 16 | 21 | Semibold |
| Subhead | Regular | 15 | 20 | Semibold |
| Footnote | Regular | 13 | 18 | Semibold |
| Caption 1 | Regular | 12 | 16 | Semibold |
| Caption 2 | Regular | 11 | 13 | Semibold |

Größenverlauf xSmall–AX5: siehe `ios.md` Abschnitt 7.2 (identische Quelle).

---

## 8. Systemintegration

### 8.1 Widgets
(hig:widgets)
- Home Screen / Today View: small, medium, large, **extra large**; Lock Screen: small (system) sowie accessory circular, rectangular, inline.
- Lock Screen des iPad: monochrom **ohne** Tint.
- Home Screen: light, dark, clear, tinted.
- iPadOS rendert Widgets groß und skaliert sie dann herunter → für die Canvas-Größe gestalten (hig:widgets#Choosing-margins-and-padding).
- Ränder 16 pt (eng 11 pt), Text ≥ 11 pt, Animationen ≤ 2 s, Deep Links, keine App-artigen Layouts.
- Extra large nicht als aufgeblasene kleinere Größe – nur mit echtem Mehrwert (hig:widgets#Best-practices).

**Widget-Größen iPad (pt; Canvas = Gestaltung, Device = Darstellung)** (hig:widgets#Specifications)

| Screen (Portrait) | Ziel | Small | Medium | Large | Extra large |
|---|---|---|---|---|---|
| 768×1024 | Canvas | 141×141 | 305.5×141 | 305.5×305.5 | 634.5×305.5 |
|  | Device | 120×120 | 260×120 | 260×260 | 540×260 |
| 744×1133 | Canvas | 141×141 | 305.5×141 | 305.5×305.5 | 634.5×305.5 |
|  | Device | 120×120 | 260×120 | 260×260 | 540×260 |
| 810×1080 | Canvas | 146×146 | 320.5×146 | 320.5×320.5 | 669×320.5 |
|  | Device | 124×124 | 272×124 | 272×272 | 568×272 |
| 820×1180 | Canvas | 155×155 | 342×155 | 342×342 | 715.5×342 |
|  | Device | 136×136 | 300×136 | 300×300 | 628×300 |
| 834×1112 | Canvas | 150×150 | 327.5×150 | 327.5×327.5 | 682×327.5 |
|  | Device | 132×132 | 288×132 | 288×288 | 600×288 |
| 834×1194 | Canvas | 155×155 | 342×155 | 342×342 | 715.5×342 |
|  | Device | 136×136 | 300×136 | 300×300 | 628×300 |
| 954×1373 * | Canvas/Device | 162×162 | 350×162 | 350×350 | 726×350 |
| 970×1389 * | Canvas/Device | 162×162 | 350×162 | 350×350 | 726×350 |
| 1024×1366 | Canvas | 170×170 | 378.5×170 | 378.5×378.5 | 795×378.5 |
|  | Device | 160×160 | 356×160 | 356×356 | 748×356 |
| 1192×1590 * | Canvas/Device | 188×188 | 412×188 | 412×412 | 860×412 |

\* Display Zoom „More Space“.

### 8.2 Live Activities
(hig:live-activities)
- Auf dem iPad: **Lock Screen und Home Screen**; Dynamic Island und StandBy sind iPhone-only.
- Regeln wie iOS: Anfang/Ende, max. ca. 8 h, keine Werbung, keine sensiblen Daten, Lock-Screen-Rand 14 pt, endet sofort (Lock Screen bis zu 4 h sichtbar).

**Lock-Screen-Maße iPad (pt)** (hig:live-activities#Specifications)

| Screen (laut Spiegel „portrait“) | Lock Screen (Breite × Höhe) |
|---|---|
| 1366×1024 | 500 × 84–160 |
| 1194×834 | 425 × 84–160 |
| 1012×834 | 425 × 84–160 |
| 1080×810 | 425 × 84–160 |
| 1024×768 | 425 × 84–160 |

### 8.3 Controls, App Shortcuts, Notifications, Quick Actions
- Controls für Control Center und Lock Screen (Action Button ist iPhone-spezifisch): Symbol selbsterklärend, Zustandsanimation, Redaktion im Sperrzustand, Authentifizierung für Sicherheitsaktionen (hig:controls).
- App Shortcuts in Spotlight und Shortcuts-App nach Wichtigkeit ordnen (hig:app-shortcuts#iOS-iPadOS).
- Notifications: knapp, keine Dubletten, keine sensiblen Daten; Badge nur für Ungelesenes (hig:notifications).
- Home Screen Quick Actions: max. 4 (hig:home-screen-quick-actions).
- Tastaturkürzel und Menüleiste als Systemintegration für Power-User (hig:the-menu-bar#iPadOS).

---

## 9. Umsetzung: SwiftUI / UIKit

Legende: **[S]** = API im Spiegel referenziert; **[K]** = gängige API, nicht im Spiegel belegt – vor Verwendung prüfen.

| Muster | SwiftUI | UIKit |
|---|---|---|
| Tab Bar oben, fest | `TabView` + `.tabViewStyle(.tabBarOnly)` – `tabBarOnly` [S] | `UITabBarController` [K] |
| Tab Bar ↔ Sidebar | `sidebarAdaptable` [S] | `UITab.Placement` [S] |
| Tab-Anpassung | `TabViewCustomization` [S] | `UITab.Placement` [S] |
| Nur Sidebar / Split View | `NavigationSplitView` [S] | `UISplitViewController` [S], `UICollectionLayoutListConfiguration.Appearance.sidebar` [S] |
| Toolbar | `.toolbar`, `ToolbarItem` [K], `ToolbarItemGroup` [S], Anpassung über `.toolbar(id:)` [K] | `UIToolbar` [S], `UIBarButtonItem` [S] |
| Sheet-Stile | `.sheet` [S], `.presentationSizing(.form/.page)` [K] | `UIModalPresentationStyle` (`.formSheet`, `.pageSheet`) [S] |
| Popover | `.popover` [K] | `UIPopoverPresentationController` [K] |
| Fenster | `WindowGroup` [K], `OpenWindowAction` [S] | `UIWindowScene.ActivationInteraction` [S], `collectionView(_:sceneActivationConfigurationForItemAt:point:)` [S] |
| Quick Look in eigenem Fenster | – | `QLPreviewSceneActivationConfiguration` [S] |
| Pointer-Effekte | `.hoverEffect(.highlight/.lift)` [K] | `UIPointerInteraction` [K], `UIPointerShape.roundedRect(_:radius:)` [S], `UIPointerAccessory` [S] |
| Band-Selektion | – | `UIBandSelectionInteraction` [S] |
| Fokus | `.focusable`, `.focusSection` [K] | `focusGroupIdentifier` [S], `UIFocusGroupPriority` [S], `UIFocusHaloEffect` [S] |
| Tastenkürzel / Menüleiste | `.keyboardShortcut` [K], `.commands { CommandMenu }` [K] | `UIKeyCommand` [K], `UIMenuBuilder` [K] |
| Background Extension | `backgroundExtensionEffect()` [S] | `UIBackgroundExtensionView` [S] |
| Liquid Glass custom | `.glassEffect(_:in:)` [S], `Glass.regular/.clear` [S] | `UIGlassEffect` [K] |
| Scroll Edge Effect | `ScrollEdgeEffectStyle` [S] | `UIScrollEdgeEffect.Style` [S] |
| Size Classes | `UserInterfaceSizeClass` [S] | `UITraitChangeObservable` [S] |
| Pencil | PencilKit [K] | `UIPencilInteraction` [K] |
| Widgets / Live Activities | WidgetKit, ActivityKit [S], `ContainerRelativeShape` [S] | – |

---

## 10. Review-Checkliste (iPadOS)

- [ ] App funktioniert in full screen **und** windowed; kleinste und größte Fenstergröße getestet (hig:windows#iPadOS, hig:layout#Adaptability)
- [ ] Alle Size-Class-Kombinationen (compact/regular × compact/regular) sinnvoll; keine Entscheidung nach `idiom`/Orientierung (hig:layout#Size-classes)
- [ ] Mittlere Fensterbreiten: Split View kollabiert logisch, Navigation zwischen Spalten möglich (hig:split-views#iPadOS)
- [ ] Gleiche Funktionalität in jeder Größe; nur Sichtbarkeit variiert (hig:layout#Size-classes)
- [ ] Leading Toolbar-Items werden von Fensterkontrollen nicht verdeckt (hig:windows#iPadOS)
- [ ] Keine Custom-Fensterrahmen/-kontrollen; im UI „Fenster“ statt „Scene“ (hig:windows#Best-practices)
- [ ] Mehrfenster unterstützt; neue Fenster nur gezielt (Context Menu / File-Menü) (hig:windows)
- [ ] Tab Bar oben bzw. `sidebarAdaptable`; Default ≤ 5 Tabs bei Anpassbarkeit (hig:tab-bars#iPadOS)
- [ ] Sidebar: nicht standardmäßig versteckt, max. 2 Ebenen, SF Symbols, Edge-Swipe funktioniert (hig:sidebars)
- [ ] Auswahl in jeder Split-View-Spalte persistent hervorgehoben (hig:split-views#Best-practices)
- [ ] Kein manuelles Overflow-Menü; Toolbar überläuft nicht im Normalzustand; ggf. anpassbar (hig:toolbars)
- [ ] Eine prominente Aktion trailing; max. ca. 3 Toolbar-Gruppen (hig:toolbars)
- [ ] Sheets als Form/Page Sheet; Popovers nur in regular, sonst Sheet (hig:sheets#iOS-iPadOS, hig:popovers#iOS-iPadOS)
- [ ] Modals minimiert; parallele Aufgaben eher als Fenster (hig:designing-for-ipados)
- [ ] Pointer: Standard-Effekte aktiv; Custom-Buttons mit highlight/lift; lückenlose Hit-Regionen in Bars; Padding 12/24 pt (hig:pointing-devices#iPadOS)
- [ ] Keine dekorativen Pointer-Effekte, kein Anleitungstext am Pointer (hig:pointing-devices#Customizing-pointers)
- [ ] Hit-Targets ≥ 44×44 pt auch für Touch, wenn Pointer vorhanden (hig:accessibility#Mobility)
- [ ] Tastatur: Standardkürzel unverändert, Tab/Pfeil-Fokus in Listen/Sidebars/Grids sinnvoll; Full Keyboard Access getestet (hig:keyboards, hig:focus-and-selection#iPadOS)
- [ ] Menüleiste: alle Funktionen auch im UI erreichbar; Settings-Eintrag korrekt; Tabs im View-Menü (hig:the-menu-bar#iPadOS)
- [ ] Context Menus per Long Press **und** Sekundärklick; Edit Menu horizontal und vertikal geprüft (hig:context-menus#iOS-iPadOS, hig:edit-menus#iOS-iPadOS)
- [ ] Drag and Drop: zwischen Spalten und Apps, Multi-Item, Undo, Option-Kopie (hig:drag-and-drop)
- [ ] Apple Pencil (falls relevant): sofortiges Markieren, Hover nur Vorschau, Double Tap/Squeeze nicht destruktiv, Scribble in Textfeldern ohne Springen (hig:apple-pencil-and-scribble)
- [ ] Liquid Glass nur in Bars/Sidebar; Inhalt läuft unter Sidebar/Toolbar; ein Scroll Edge Effect pro Spalte (hig:materials, hig:scroll-views#Scroll-edge-effects)
- [ ] Dynamic Type inkl. AX-Größen; Spalten bei großen Größen reduziert (hig:typography#Supporting-Dynamic-Type)
- [ ] Dark Mode mit base/elevated System-Hintergründen (hig:dark-mode#iOS-iPadOS)
- [ ] Suche: trailing in Toolbar bzw. oben in Sidebar; bei rein virtueller Tastatur nicht auto-fokussieren (hig:search-fields#iPadOS-macOS)
- [ ] Widgets inkl. extra large mit echtem Mehrwert; Lock Screen monochrom geprüft (hig:widgets)
- [ ] Multitasking: Kontext gesichert, Medien pausieren, Audio-Unterbrechungen korrekt (hig:multitasking#Best-practices)

---

## 11. Häufige Fehler („Web-Port-“ bzw. „iPhone-Port-Geruch“)

- **Hochskalierte iPhone-App**: einspaltige Listen über volle 13"-Breite, riesige Zeilen, Tab Bar unten (hig:tab-bars#iPadOS, hig:split-views).
- **Fixe Breakpoints nach Gerätebreite** (z. B. „> 768 = Tablet“) statt Size Classes; Layout bricht in mittleren Fensterbreiten (hig:layout#Size-classes, hig:split-views#iPadOS).
- **Funktionen verschwinden bei schmalem Fenster** statt in Overflow/Tab-Bar zu wandern (hig:layout#Size-classes).
- **Eigene Fensterchrome, Fake-Ampeln, Custom-Resize-Griffe** (hig:windows#Best-practices).
- **Buttons ganz links in der Toolbar**, die im Fenstermodus unter den Window Controls landen (hig:windows#iPadOS).
- **Hamburger-Drawer** statt Sidebar/Split View; Sidebar standardmäßig zu (hig:sidebars).
- **Selbstgebautes „…“-Overflow** in der Toolbar, obwohl das System es liefert (hig:toolbars).
- **Vollbild-Modals für alles** (Einstellungen, Detailansichten) statt Popover/Sheet/Fenster (hig:designing-for-ipados, hig:modality).
- **Hover-only-Bedienung** (Menüs, die nur bei Mouseover öffnen; Tooltips als einzige Erklärung) – Pointer ersetzt Touch nicht (hig:pointing-devices#iPadOS).
- **CSS-artige Hover-Effekte** (Skalierung auf Tabellenzeilen, Schatten ohne Skalierung) (hig:pointing-devices#Customizing-pointers).
- **Lücken zwischen Bar-Buttons**, Pointer springt zum Kreis zurück (hig:pointing-devices#Standard-pointers-and-effects).
- **Eigene Tastaturnavigation für Buttons** statt Full Keyboard Access; umdefinierte Cmd-Standardkürzel (hig:keyboards).
- **Funktionen nur in der Menüleiste** (hig:the-menu-bar#iPadOS).
- **Pencil-Modus-Schalter** vor dem ersten Strich; Double Tap löscht Inhalte (hig:apple-pencil-and-scribble).
- **Opake Markenfarb-Sidebar** statt Liquid Glass mit durchlaufendem Inhalt (hig:sidebars, hig:materials).

---

## Widersprüche & Lücken im Spiegel

- **Keine Gerätetabelle/Safe-Area-Werte** in `layout.md` (Change Log nennt sie aber). Bildschirmgrößen nur aus Widget-/Live-Activity-Tabellen.
- **Live-Activity-Tabelle iPadOS** ist mit „portrait“ überschrieben, listet aber Querformat-Maße (z. B. 1366×1024), während die Widget-Tabelle 1024×1366 als Portrait führt. Orientierung der LA-Werte ist unklar.
- **Multitasking-Begriffe:** `layout.md` erwähnt noch „Slide Over“, `multitasking.md#iPadOS` beschreibt nur full screen vs. windowed (plus PiP). Für neue Designs vom Fenstermodell ausgehen.
- **Tab Bar vs. Sidebar:** `sidebars.md` rät „erst Tab Bar erwägen“, `tab-bars.md#iPadOS` „Tab Bar bevorzugen, bei Komplexität wandelbar“. Das ist konsistent, aber `split-views.md` und `sidebars.md` empfehlen für Hierarchien über zwei Ebenen eine Split View mit Content-Liste. Bei tiefen Hierarchien gilt also Split View statt Tab Bar.
- **Overflow:** iPadOS liefert das System-Overflow automatisch (toolbars.md); auf iOS soll ein More-Menü manuell entstehen. Für Universal-Apps unterschiedlich behandeln.
- **Tastatur:** Fokus-Navigation per Tab/Pfeil ist erwünscht (focus-and-selection), für Controls aber ausdrücklich nicht (keyboards) – dort nur Full Keyboard Access.
- **Sheet-Größen** (Form/Page) sind im Spiegel ohne Zahlenwerte beschrieben.
