# macOS – Plattformreferenz

Quelle: lokaler HIG-Spiegel (`~/.apple-design/hig/pages`, Stand 2026-10-21). Belege als `(hig:<slug>)` bzw. `(hig:<slug>#Anker)`. Alle Zahlen stammen aus dem Spiegel; wo der Spiegel keine Zahl nennt, steht hier auch keine.

---

## 1. Kurzprofil

- **Nutzungskontext:** stationär am Schreibtisch, Sichtabstand ca. 1–3 Fuß; Sitzungen von wenigen Minuten bis zu Stunden konzentrierter Arbeit; mehrere Apps gleichzeitig offen, häufiger Wechsel zwischen aktiven und inaktiven Zuständen (hig:designing-for-macos).
- **Eingabe:** physische Tastatur (praktisch immer), Maus/Trackpad mit hoher Präzision, Gamecontroller, Siri; Trackpad-Gesten und Force Click (hig:designing-for-macos, hig:pointing-devices#macOS, hig:keyboards).
- **Displays:** große, hochauflösende Displays, zusätzliche Monitore inkl. iPad; einige Macs haben eine Kameraaussparung oben mittig (hig:designing-for-macos, hig:layout#macOS, hig:going-full-screen#macOS).
- **Systemrahmen:** Menüleiste, Dock, Finder/Dateiverwaltung, Vollbild in eigenem Space, Fenster in drei Zuständen (main/key/inactive) (hig:designing-for-macos, hig:windows#macOS).
- **Erwartung:** mehr Inhalt in weniger Hierarchieebenen, wenig Modalität, frei skalierbare Fenster, alle Befehle in der Menüleiste, Tastaturkürzel, Personalisierung (Toolbar, Fenster, Farben, Schriften) (hig:designing-for-macos).
- **Kein Dynamic Type** auf macOS (hig:typography#macOS).

---

## 2. Nicht verhandelbar

1. Jeden Befehl der App in der Menüleiste anbieten – auch selten genutzte und solche, die bereits in Toolbar oder Kontextmenü stehen (hig:the-menu-bar#App-specific-menus, hig:toolbars#macOS).
2. Standardmenüs in Standardreihenfolge: App-Menü, File, Edit, Format, View, App-spezifische Menüs, Window, Help (hig:the-menu-bar#Anatomy).
3. Menüpunkte nicht ausblenden, wenn sie gerade nicht anwendbar sind – deaktivieren (hig:the-menu-bar#Best-practices).
4. Standard-Tastaturkürzel unterstützen und nicht für fremde Aktionen umwidmen; eigene Kürzel nur für die häufigsten App-Befehle, Command als Hauptmodifier, Control vermeiden (hig:keyboards#Standard-keyboard-shortcuts, hig:keyboards#Custom-keyboard-shortcuts).
5. Fenster frei skalierbar, verschiebbar, minimierbar; Vollbild über das System anbieten und Nutzer entscheiden lassen, wann es betreten/verlassen wird (hig:designing-for-macos, hig:going-full-screen#macOS).
6. Keine eigenen Fensterrahmen/-controls nachbauen; Systemdarstellung der Fensterzustände (key/main/inactive) erhalten (hig:windows#Best-practices, hig:windows#macOS).
7. Keine kritischen Controls oder Informationen am unteren Fenster- oder Sidebar-Rand – Fenster werden oft teilweise unter den Bildschirmrand geschoben (hig:layout#macOS, hig:windows#macOS, hig:sidebars#macOS).
8. Einstellungen über *App-Name > Settings…* (Command-Komma) öffnen, nicht über einen Toolbar-Button (hig:settings#macOS).
9. Window-Menü immer anbieten, auch bei nur einem Fenster, mit Minimize und Zoom (Full Keyboard Access) (hig:the-menu-bar#Window-menu).
10. View-Menü immer anbieten, auch wenn nur Enter/Exit Full Screen darin steht; Show/Hide-Titel spiegeln den aktuellen Zustand (hig:the-menu-bar#View-menu).
11. Undo/Redo oben im Edit-Menü mit Command-Z / Shift-Command-Z (hig:undo-and-redo#macOS).
12. Liquid Glass nur in der Funktionsebene (Toolbar, Sidebar, Controls), nie im Inhaltsbereich; sparsam auf eigene Controls anwenden (hig:materials#Liquid-Glass).
13. Menu Bar Extra öffnet ein Menü, kein Popover (außer Funktion ist für ein Menü zu komplex); Nutzer entscheiden, ob es angezeigt wird (hig:the-menu-bar#Menu-bar-extras).
14. Vom Accent Color des Nutzers abhängige Elemente (Sidebar-Icons, Auswahl) nicht hart einfärben, außer eine fixe Farbe trägt Bedeutung (hig:sidebars#Best-practices, hig:color#App-accent-colors).
15. Full Keyboard Access unterstützen (hig:keyboards#Best-practices).

---

## 3. Layout & Maße

### Konkrete Werte aus dem Spiegel

| Größe | Wert | Quelle |
|---|---|---|
| Menüleistenhöhe | 24 pt | (hig:the-menu-bar#Menu-bar-extras) |
| Standard-Textgröße / Minimum | 13 pt / 10 pt | (hig:typography#Ensuring-legibility) |
| Control-Größe Default / Minimum | 28x28 pt / 20x20 pt | (hig:accessibility#Mobility) |
| Abstand um Elemente mit Bezel / ohne Bezel | ca. 12 pt / ca. 24 pt | (hig:accessibility#Mobility) |
| Split-View-Divider (thin, bevorzugt) | 1 pt | (hig:split-views#macOS) |
| Padding Bild ↔ Kante beim Image Button | ca. 10 px | (hig:buttons#macOS) |
| Toolbar-/Fenstertitel | unter 15 Zeichen | (hig:toolbars#Titles) |
| Toolbar-Gruppen | max. 3 anstreben | (hig:toolbars#Item-groupings) |
| Tooltip-Länge | max. 60–75 Zeichen | (hig:offering-help#macOS-visionOS) |
| App-Name im About-Menüpunkt | 16 Zeichen oder weniger | (hig:the-menu-bar#App-menu) |
| Radio Buttons pro Gruppe | typisch 2–5; ab ca. 5 Optionen Pop-up Button | (hig:toggles#macOS) |
| Tabs in Tab View | nicht mehr als 6 | (hig:tab-views#Best-practices) |
| Stepper Shift-Klick | größere Schritte, Beispiel: 10× Standard | (hig:steppers#macOS) |
| Kontrast (WCAG AA) | bis 17 pt: 4.5:1; ab 18 pt oder fett: 3:1 | (hig:accessibility#Vision) |
| App-Icon Layoutgröße | 1024x1024 px, quadratisch, System maskiert zu abgerundetem Rechteck | (hig:app-icons#Specifications) |
| Widget-Textgröße | 11 pt oder größer | (hig:widgets#Displaying-text-in-widgets) |
| Widget-Ränder | 16 pt Standard, 11 pt eng; auf dem Mac-Desktop kleiner (ohne Zahl) | (hig:widgets#Choosing-margins-and-padding) |
| Mac Catalyst, iPad-Idiom | Skalierung auf 77 %, z. B. 17 pt → 13 pt | (hig:mac-catalyst#Choose-an-idiom) |
| Dokument-Icon Hintergrund | 512/256/128/32/16 px @1x (jeweils @2x doppelt) | (hig:icons#macOS) |
| Dokument-Icon Center Image | halbe Canvas-Größe; ca. 10 % Rand, Motiv ca. 80 % (z. B. 205x205 in 256x256) | (hig:icons#macOS) |
| Kleinste Dokument-Icon-Größe | 16x16 px | (hig:icons#macOS) |

### Layoutregeln

- Wichtigstes oben und an der führenden Seite (Lesereihenfolge); top-down-Fluss, wichtige Aktionen oben im Fenster (hig:layout#Visual-hierarchy, hig:mac-catalyst#Layout).
- Hintergrundinhalte bis unter Sidebar und Toolbar ziehen; wenn Sidebar/Inspector Bildteile verdecken, Background Extension Effect nutzen (hig:layout#Visual-hierarchy, hig:sidebars#Best-practices).
- Keine Inhalte hinter der Kameraaussparung oben am Fensterrand (hig:layout#macOS).
- Split-View-Panes: sinnvolle Min-/Max-Breiten, damit der Divider sichtbar bleibt (hig:split-views#macOS).
- Spalten in Tabellen/Outline/Column Views vom Nutzer skalierbar (hig:lists-and-tables#macOS, hig:outline-views, hig:column-views).
- Tab View mit Rand aus Window-Body auf allen Seiten einrücken (hig:tab-views#Anatomy).
- Im Vollbild Proportionen anpassen, aber Fenster nicht programmatisch skalieren (hig:going-full-screen#Best-practices).

**Lücke im Spiegel:** Es gibt keine Default-, Minimal- oder Maximalgrößen für macOS-Fenster, keine Toolbar-Höhe, keine Sidebar-Breiten und keine Zeilenhöhen (Sidebar-Größe small/medium/large nur qualitativ, hig:sidebars#macOS). Solche Werte nicht erfinden; im Zweifel Systemkomponenten verwenden.

---

## 4. Navigation & Struktur

### Fenster
- **Primärfenster** für Hauptnavigation und Inhalt; **Hilfsfenster** für eine abgeschlossene Aufgabe ohne Navigation in andere Bereiche (hig:windows).
- Neue Fenster gezielt öffnen (z. B. Compose in Mail), nicht als Default-Verhalten; Option „In neuem Fenster öffnen“ via Kontextmenü oder File-Menü anbieten (hig:windows#Best-practices).
- Im UI-Text immer „Fenster/window“ sagen, nie „Scene“ (hig:windows#Best-practices).
- Zustände: *main* (vorderstes App-Fenster), *key* (nimmt Eingaben an, farbige Fensterknöpfe), *inactive* (grau, ohne Vibrancy) (hig:windows#macOS-window-states).
- Bottom Bar nur für wenig, kontextbezogene Info (z. B. Finder-Statusleiste); mehr Info → Inspector (hig:windows#macOS).

### Menüleiste
- Pflichtmenüs und Reihenfolge siehe Abschnitt 2; Details zu App-, File-, Edit-, Format-, View-, Window-, Help-Menü in (hig:the-menu-bar).
- App-Menü: About zuerst und allein in einer Gruppe; Settings…; Services; Hide/Hide Others/Show All; Quit (hig:the-menu-bar#App-menu).
- App-spezifische Menüs zwischen View und Window, Reihenfolge von allgemein zu speziell, Hierarchie der App spiegeln (Mail: Mailbox → Message → Format) (hig:the-menu-bar#App-specific-menus).
- Menütitel kurz, möglichst ein Wort; Title Case (hig:the-menu-bar#Best-practices).
- Ellipse (…) bei Menüpunkten, die weitere Eingaben verlangen (hig:menus, hig:the-menu-bar#File-menu).
- Dynamische Menüpunkte (Option-Varianten) nur in Menüleistenmenüs, nur ein Modifier, nie einziger Weg (hig:the-menu-bar#Dynamic-menu-items).
- Duplicate statt Save As/Export/Copy To bevorzugen; Export As nur für Fremdformate (hig:the-menu-bar#File-menu).

### Sidebar
- Führende Seite, Navigation zwischen Bereichen/Top-Level-Sammlungen; max. zwei Hierarchieebenen, tiefer → zusätzliche Content-Liste im Split View (hig:sidebars#Best-practices).
- Ein-/ausblendbar per Button und View-Menü (Show/Hide Sidebar), standardmäßig sichtbar (hig:sidebars#Best-practices).
- Kann beim Verkleinern des Fensters automatisch einklappen (hig:sidebars#macOS).
- Suchfeld oben in der Sidebar, wenn es die Sidebar filtert (hig:search-fields#iPadOS-macOS).

### Toolbar
- Im Fensterrahmen oben, unter oder integriert mit der Titelleiste; Items ohne Bezel (hig:toolbars#macOS).
- Leading: Zurück, Sidebar-Toggle, Titel, ggf. Dokumentmenü (nicht anpassbar). Center: häufige Controls, anpassbar, fallen ins System-Overflow. Trailing: immer sichtbar – Inspector-Buttons, Suchfeld, More-Menü, primäre Aktion (hig:toolbars#Item-groupings).
- Suchfeld für viele Fälle am trailing Ende der Toolbar (hig:search-fields#iPadOS-macOS).
- Toolbar-Anpassung anbieten bei vielen Items oder langen Sitzungen (hig:toolbars#Best-practices).
- Fenstertitel nicht mit dem App-Namen belegen (hig:toolbars#Titles).

### Inspector
- Zeigt Details der aktuellen Auswahl und aktualisiert sich mit ihr; als Panel oder als trailing Split-View-Pane; ein „Info“-Fenster mit festem Inhalt ist dagegen ein normales Fenster (hig:panels#Best-practices, hig:windows#macOS).
- Inspector neben dem Inhalt statt Popover (hig:mac-catalyst#Layout).

### Settings
- Eigenes Settings-Fenster mit nicht anpassbarer, immer sichtbarer Toolbar zum Wechsel der Panes; aktiver Pane markiert; Fenstertitel = Pane-Name (ohne Panes: „*App Name* Settings“); zuletzt genutzten Pane wiederherstellen; Minimize/Maximize dimmen (hig:settings#macOS).
- Dokumentbezogene Optionen ins File-Menü (hig:settings#macOS).
- Nur seltene, allgemeine Einstellungen; Aufgabenoptionen dort, wo die Aufgabe stattfindet; keine Kopien systemweiter Einstellungen (hig:settings#Best-practices).

### Muster-Auswahl
| Datenform | Muster | Quelle |
|---|---|---|
| Flach, mehrspaltig, sortierbar | Table View | (hig:lists-and-tables#macOS) |
| Hierarchisch mit Attributspalten | Outline View (Hierarchie nur in Spalte 1) | (hig:outline-views) |
| Tiefe Hierarchie, häufiges Vor/Zurück, keine Sortierung nötig | Column View (Browser) | (hig:column-views) |
| Wenige eng verwandte Bereiche im Fensterkörper | Tab View (statt Segmented Control) | (hig:tab-views, hig:segmented-controls#macOS) |
| Wiederholte Eingabe mit Ergebnisbeobachtung | Panel statt Sheet | (hig:sheets#macOS) |

---

## 5. Komponenten-Besonderheiten (Platform considerations)

**Buttons**
- Push Button ist Standard; Ellipse im Titel, wenn er ein weiteres Fenster/View/App öffnet; Flexible-Height nur für zweizeiligen/hohen Inhalt (hig:buttons#macOS).
- Square (Gradient) Buttons nur im View (z. B. +/- unter Tabelle), nicht in Toolbar/Statusleiste, Symbol statt Text, kein einleitendes Label (hig:buttons#macOS).
- Help Button: systemeigener, max. einer pro Fenster, kontextbezogenes Hilfethema; Position: Dialog mit OK/Cancel → untere Ecke gegenüber den Buttons; Settings → untere linke oder rechte Ecke; nie in Toolbar (hig:buttons#macOS).
- Image Buttons im View, nicht im Fensterrahmen; Label darunter (hig:buttons#macOS).
- Spring Loading (Force Click beim Draggen) für Buttons und Segmente erwägen (hig:buttons#macOS, hig:segmented-controls#macOS).

**Toggles:** Switch für gewichtige Gruppenschalter, Mini-Switch in Grouped-Form-Zeilen, Checkbox für Hierarchien und Einzeloptionen (inkl. Mixed State), Radio Buttons für exklusive Optionen; nie in Toolbar/Statusleiste; bestehende Checkboxen nicht durch Switches ersetzen (hig:toggles#macOS).

**Sheets:** karten­artig über dem Elternfenster, Elternfenster gedimmt; vernünftige Default-Größe; andere App-Fenster bleiben nutzbar (hig:sheets#macOS).

**Popovers:** können abgelöst (detached) werden und werden dann zum Panel mit möglichst gleicher Optik (hig:popovers#macOS).

**Panels:** schweben über Fenstern, kurzer Substantiv-Titel („Inspector“, „Fonts“); bei App-Aktivierung alle Panels nach vorn, bei Inaktivität ausblenden; nicht in der Fensterliste des Window-Menüs; kein Minimize; einfache Controls (Slider, Stepper) bevorzugen; HUD-Stil nur für medienlastige Apps, klein, sparsam farbig, kaum Controls (hig:panels).

**Alerts:** App-Icon automatisch; Unterdrückungsoption für wiederholte Alerts, Accessory View, Help Button möglich; Warnsymbol nur bei echtem Risiko von Datenverlust (hig:alerts#macOS).

**Listen/Tabellen/Outline/Column:** Sortieren per Spaltenkopf (erneuter Klick kehrt um), Spalten skalierbar, alternierende Zeilenfarben bei breiten Tabellen; Outline: Option-Klick expandiert rekursiv, Expansionszustand merken, Spaltenköpfe als Substantive ohne Doppelpunkt, mittige Ellipse bei Kürzung; Column View: Wurzel in Spalte 1, Vorschau bei Blattobjekten (hig:lists-and-tables#macOS, hig:outline-views, hig:column-views).

**Split Views:** vertikal, horizontal oder kombiniert; Panes ausblendbar, Wiederherstellung über Toolbar-Button und Menübefehl mit Kürzel; thin Divider (hig:split-views#macOS).

**Scroll Views:** Scroll Bars; in Panels ggf. small/mini, dann alle Controls im Panel in gleicher Größe (hig:scroll-views#macOS).

**Text/Eingabe:** Combo Box für Text + Vorschlagsliste; Expansion Tooltip für abgeschnittenen Feldinhalt; Token Fields; Path Controls nur im Window-Body (hig:text-fields#macOS, hig:entering-data#macOS, hig:token-fields, hig:path-controls).

**Pickers / Slider / Gauges:** Date Picker textuell oder grafisch; Slider mit Tick Marks, linear vs. zirkulär (für wiederkehrende Werte), Live-Feedback; Level Indicator (Capacity diskret/kontinuierlich, Rating, Relevance) (hig:pickers#macOS, hig:sliders#macOS, hig:gauges#macOS).

**Tooltips (Help Tags):** nur das gezeigte Control beschreiben, mit Verb beginnen, Control-Namen nicht wiederholen, Satz-Schreibweise, 60–75 Zeichen (hig:offering-help#macOS-visionOS).

**Pointer & Trackpad:** Standard-Cursor semantisch nutzen (I-Beam, Open/Closed Hand, Crosshair, Drag Copy, Operation not allowed, Resize-Varianten); Sekundärklick = Kontextmenü; Force Click, Smart Zoom, Swipe between pages beachten (hig:pointing-devices#macOS).

**Kontextmenüs:** Mac-Nutzer erwarten zu jedem Objekt ein Kontextmenü mit relevanten Aktionen (hig:mac-catalyst#Menus, hig:context-menus).

**Drag and Drop:** Export in den Finder (Datei oder Clipping), Ziehen aus inaktiven Fenstern ohne Aktivierung, Badge mit Anzahl bei Mehrfachauswahl, passende Cursor, Auswahl+Ziehen in einer Bewegung (hig:drag-and-drop#macOS).

**Dateien:** Standard-Open/Save-Panels; Open-Button umbenennbar (z. B. „Insert“); Save-Dialog mit Formatwahl und optionalem Accessory View; bei deaktiviertem Autosave Punkt im Close-Button und im Window-Menü; „Edited“ im Titel nach Speichern entfernen; Finder Sync Extensions für Sync-Status (hig:file-management#macOS).

**Drucken:** eigene Kategorie im Print-Panel für app-spezifische Optionen; Page Setup nur für dokumentspezifische Seiteneinstellungen; erweiterte Optionen hinter Disclosure „Advanced Options“ (hig:printing#macOS).

**Haptik:** Magic Trackpad – nur Alignment, Level change, Generic (hig:playing-haptics#macOS).

**Datenschutz:** Developer ID für Vertrieb außerhalb des Stores; Sandboxing (Pflicht im Mac App Store); Fast User Switching beachten (hig:privacy#macOS).

**Farben:** dynamische Systemfarben (labelColor, controlAccentColor, selectedContentBackgroundColor, unemphasized-Varianten für Nicht-Key-Fenster usw.) statt fixer Werte (hig:color#macOS).

**Dark Mode / Desktop Tinting:** Bei Graphite-Akzent tönen Fensterhintergründe nach dem Schreibtischbild; eigene Komponenten mit sichtbarem Hintergrund im neutralen Zustand leicht transparent halten, farbige Zustände nicht (hig:dark-mode#macOS).

---

## 6. Liquid Glass, Materialien, aktuelles Design-System

- **Zwei Ebenen:** Liquid Glass für die Funktionsebene (Toolbars, Sidebars, Controls) über dem Inhalt; Standardmaterialien (Blur, Vibrancy, Blending) für Struktur im Inhaltsbereich (hig:materials).
- **Kein Liquid Glass im Content Layer**; Ausnahme: transiente Zustände von Slidern/Toggles beim Bedienen (hig:materials#Liquid-Glass).
- **Varianten:** *regular* (blurrt, Standard für Systemkomponenten, für textlastige Elemente wie Sidebars, Popovers, Alerts); *clear* nur über visuell reichem Medieninhalt; bei hellem Untergrund 35 % dunkle Dimmebene erwägen (hig:materials#Liquid-Glass).
- **Sidebars** schweben auf macOS in der Liquid-Glass-Ebene; Inhalt darunter weiterführen (horizontal scrollen oder Background Extension Effect) (hig:sidebars#Best-practices).
- Liquid Glass ist in großen Elementen wie Sidebars opaker, in Toolbars wechselt es je nach Untergrund zwischen hell und dunkel, Symbole/Text monochrom (hig:color#Liquid-Glass-color).
- **Farbe sparsam:** Akzentfarbe auf den Hintergrund der primären Aktion (prominent), nicht auf mehrere Controls; bei farbigem Inhalt monochrome Toolbar (hig:color#Liquid-Glass-color, hig:toolbars#Best-practices).
- **Toolbar:** keine eigenen Hintergründe/Tönungen; stattdessen Scroll Edge Effect; Standardkomponenten sind konzentrisch zu den Bar-Ecken, eigene Komponenten ebenfalls konzentrisch gestalten; Symbole ohne Rahmen; eine `.prominent`-Aktion am trailing Ende (hig:toolbars#Best-practices, hig:toolbars#Actions).
- **Scroll Edge Effect** (iOS, iPadOS, macOS): automatisch bevorzugen; nur hinter schwebenden Elementen; ein Effekt pro View; in Split Views je Pane, gleiche Höhe (hig:scroll-views#Scroll-edge-effects).
- **Standardmaterialien macOS:** NSVisualEffectView-Materialien semantisch wählen, Blending *behind window* vs. *within window*; Vibrancy in eigenen Views bewusst einsetzen (hig:materials#macOS).
- Inaktive Fenster verlieren Vibrancy – eigene Fenster müssen die Zustandsdarstellung mitmachen (hig:windows#macOS-window-states).
- **App-Icon:** geschichtet, Liquid-Glass-Eigenschaften (Specular, Refraktion, Transluzenz) durch das System; Ebenen in Icon Composer; quadratische, unmaskierte Ebenen; keine eigenen Schatten/Glows; Varianten default, dark, clear light/dark, tinted light/dark (hig:app-icons).

---

## 7. Typografie

- Systemschrift **SF Pro**; **kein Dynamic Type** auf macOS (hig:typography#macOS).
- Default 13 pt, Minimum 10 pt (hig:typography#Ensuring-legibility).
- Leichte Schnitte (Ultralight, Thin, Light) vermeiden (hig:typography#Ensuring-legibility).
- Für Text passend zu Systemcontrols die dynamischen NSFont-Varianten nutzen: controlContentFont, labelFont, menuFont, menuBarFont, messageFont, paletteFont, titleBarFont, toolTipsFont, userFont, userFixedPitchFont, systemFont, boldSystemFont (hig:typography#macOS).
- Systemschriften nicht einbetten, über Font.Design ansprechen (hig:typography#Using-system-fonts).

### macOS Built-in Text Styles (hig:typography#Specifications)

| Style | Weight | Size (pt) | Line height (pt) | Emphasized |
|---|---|---|---|---|
| Large Title | Regular | 26 | 32 | Bold |
| Title 1 | Regular | 22 | 26 | Bold |
| Title 2 | Regular | 17 | 22 | Bold |
| Title 3 | Regular | 15 | 20 | Semibold |
| Headline | Bold | 13 | 16 | Heavy |
| Body | Regular | 13 | 16 | Semibold |
| Callout | Regular | 12 | 15 | Semibold |
| Subheadline | Regular | 11 | 14 | Semibold |
| Footnote | Regular | 10 | 13 | Semibold |
| Caption 1 | Regular | 10 | 13 | Medium |
| Caption 2 | Medium | 10 | 13 | Semibold |

Punktgrößen bezogen auf 144 ppi bei @2x-Designs. Tracking-Tabelle für Mockups: (hig:typography#Tracking-values), z. B. 12 pt → 0, 13 pt → −6/1000 em.

---

## 8. Systemintegration

- **Menu Bar Extras:** Symbol (SF Symbol oder Template-Icon, schwarz/klar, System färbt); Menü statt Popover; vom Nutzer aktivierbar (Setting, ggf. im Setup anbieten); nicht auf Sichtbarkeit verlassen – System blendet Extras bei Platzmangel aus; Funktionen zusätzlich anders erreichbar machen (hig:the-menu-bar#Menu-bar-extras).
- **Dock-Menü:** hochwertige Einträge (offene/zuletzt genutzte Fenster, Aktionen für den Fall „App nicht vorn“, z. B. Mail: Neue Mail abrufen, Neue Nachricht); jeder Eintrag auch anderswo verfügbar (hig:dock-menus).
- **Vollbild:** systemeigenes Vollbild (berücksichtigt Kameraaussparung); Einstieg per Fensterknopf, View-Menü, Control-Command-F; Dock erreichbar lassen (außer Spiele); kein Auto-Exit; beim Zurückkehren Zustand fortsetzen (hig:going-full-screen).
- **Services:** Eintrag im App-Menü (macOS only) (hig:the-menu-bar#App-menu).
- **Widgets:** auf dem Desktop und im Notification Center; Größen small, medium, large, extra large (hig:widgets#System-family-widgets).
- **Live Activities** eines gekoppelten iPhones erscheinen in der Mac-Menüleiste (compact/minimal/expanded); Klick öffnet iPhone Mirroring; iOS-Maße verwenden (hig:live-activities#macOS).
- **Notifications:** keine macOS-Sonderregeln; allgemeine Regeln: knapp, keine sensiblen Daten, max. 4 Aktionen, keine Aktion „nur App öffnen“, Badge nur für ungelesene Mitteilungen; Notification-Sounds mischen sich auf macOS standardmäßig mit anderem Audio (hig:notifications, hig:playing-audio#macOS).
- **App Shortcuts** werden auf macOS nicht unterstützt, App-Intents-Aktionen aber in der Kurzbefehle-App (hig:app-shortcuts#macOS).
- **Hilfe:** Help-Menü mit Help Book (automatisches Suchfeld), Command-? öffnet Help-Menü (hig:the-menu-bar#Help-menu, hig:keyboards).
- **SharePlay:** geteiltes Video läuft in einem Fenster weiter (hig:shareplay).

---

## 9. Umsetzung: SwiftUI / AppKit-Mapping

| Konzept | SwiftUI | AppKit |
|---|---|---|
| Hauptfenster / mehrere Fenster | `WindowGroup`, `Window`, `DocumentGroup`, `openWindow` (OpenWindowAction) | `NSWindow`, `NSWindowController` |
| Menüleistenbefehle | `.commands { CommandMenu(...) ; CommandGroup(...) }`, `.keyboardShortcut(...)` | `NSMenu`, `NSMenuItem` (Alternates: `isAlternate`) |
| Settings-Fenster | `Settings { ... }` Scene (öffnet via Command-Komma) | eigenes Fenster mit Toolbar-Panes |
| Menu Bar Extra | `MenuBarExtra` | `NSStatusBar` / `NSStatusItem` |
| Sidebar + Detail | `NavigationSplitView` | `NSSplitViewController` mit Sidebar-Item |
| Inspector | `.inspector(isPresented:)` | trailing Split-View-Item / Panel |
| Split View (frei) | `HSplitView`, `VSplitView` | `NSSplitView` (`dividerStyle` thin) |
| Tabelle | `Table` (sortierbar, mehrspaltig) | `NSTableView` |
| Outline | `List(children:)` / `OutlineGroup`, `Table` mit Children | `NSOutlineView` |
| Column View | – (kein direktes SwiftUI-Pendant bekannt) | `NSBrowser` |
| Toolbar | `.toolbar { ToolbarItem(placement:) }`, `.toolbarRole`, Anpassung über `id`-basierte Items | `NSToolbar` (customizable) |
| Suche | `.searchable(...)` | `NSSearchField` / `NSSearchToolbarItem` |
| Tooltip | `.help("...")` | `toolTip` |
| Kontextmenü | `.contextMenu { }` | `menu(for:)` |
| Popover / Sheet | `.popover`, `.sheet` | `NSPopover` (detachable), `beginSheet` |
| Panel / HUD | – | `NSPanel`, Stil `hudWindow` |
| Vollbild | Systemverhalten von `WindowGroup` | `toggleFullScreen(_:)` |
| Dock-Menü | – | `applicationDockMenu(_:)` im App-Delegate |
| Liquid Glass eigene Controls | `.glassEffect()`; Hintergrund-Spiegelung `.backgroundExtensionEffect()`; `.scrollEdgeEffectStyle(...)` | `NSGlassEffectView`, `NSBackgroundExtensionView` |
| Materialien | `.background(.regularMaterial)` usw. | `NSVisualEffectView` (Material, BlendingMode) |
| Dynamische Systemfarben | `Color(nsColor: .labelColor)` u. ä. | `NSColor.labelColor`, `.controlAccentColor` … |
| Haptik Trackpad | – | `NSHapticFeedbackPerformer` |

Hinweis: Im Spiegel verlinkt und damit belegt sind MenuBarExtra, NSStatusBar, CommandMenu, VSplitView/HSplitView, NSSplitView.DividerStyle, NSVisualEffectView (Material/BlendingMode), backgroundExtensionEffect(), ScrollEdgeEffectStyle, toggleFullScreen(_:), NSHapticFeedbackPerformer, help(_:), OpenWindowAction, hudWindow, NSDatePicker, NSTabView, isAlternate. Alle anderen Zuordnungen (u. a. `.inspector`, `Table`, `Settings`, `NSBrowser`, `applicationDockMenu(_:)`, `glassEffect`, `NSGlassEffectView`) sind Standard-API ohne Beleg im Spiegel – vor Verwendung in Code gegen die aktuelle Developer-Dokumentation prüfen.

---

## 10. Review-Checkliste

**Menüleiste & Tastatur**
- [ ] Menüs vorhanden und in Standardreihenfolge: App, File, Edit, (Format), View, App-spezifisch, Window, Help (hig:the-menu-bar#Anatomy)
- [ ] Jede Toolbar-Aktion und jeder Kontextmenübefehl auch als Menübefehl (hig:toolbars#macOS)
- [ ] Nicht anwendbare Menüpunkte deaktiviert statt ausgeblendet (hig:the-menu-bar#Best-practices)
- [ ] About an erster Stelle mit Trenner; Settings… im App-Menü; Quit/Hide mit kurzem App-Namen (hig:the-menu-bar#App-menu)
- [ ] View-Menü mit zustandsabhängigen Show/Hide-Titeln und Enter/Exit Full Screen (hig:the-menu-bar#View-menu)
- [ ] Window-Menü mit Minimize, Zoom, Bring All to Front; Panels nicht in der Fensterliste (hig:the-menu-bar#Window-menu, hig:panels)
- [ ] Standardkürzel funktionieren (Cmd-N/O/S/W/Q/Z/C/V/X/A/F/P/Komma/?) und sind nicht umgewidmet (hig:keyboards#Standard-keyboard-shortcuts)
- [ ] Eigene Kürzel sparsam, Command-basiert, ohne Control, Modifier-Reihenfolge Control-Option-Shift-Command (hig:keyboards#Custom-keyboard-shortcuts)
- [ ] Full Keyboard Access: alle Controls per Tastatur erreichbar (hig:keyboards#Best-practices)
- [ ] Menüpunkte mit weiterer Eingabe enden auf „…“ (hig:menus)

**Fenster & Layout**
- [ ] Fenster frei skalierbar; Layout bricht bei kleinen und großen Größen nicht (hig:windows#Best-practices)
- [ ] Systemvollbild unterstützt, nicht erzwungen; Dock erreichbar (hig:going-full-screen)
- [ ] Keine eigenen Fensterrahmen/-knöpfe; key/main/inactive sichtbar unterscheidbar (hig:windows#macOS)
- [ ] Nichts Kritisches am unteren Fenster-/Sidebar-Rand (hig:layout#macOS)
- [ ] Fenstertitel aussagekräftig, nicht der App-Name, unter 15 Zeichen (hig:toolbars#Titles)
- [ ] Default Text 13 pt, nichts unter 10 pt; Kontrast 4.5:1 bzw. 3:1 (hig:typography, hig:accessibility)
- [ ] Controls mindestens 20x20 pt, Default 28x28 pt (hig:accessibility#Mobility)

**Navigation & Komponenten**
- [ ] Sidebar max. zwei Ebenen, ein-/ausblendbar (Button + View-Menü), standardmäßig sichtbar (hig:sidebars)
- [ ] Sidebar-Icons folgen der System-Akzentfarbe, fixe Farben nur mit Bedeutung (hig:sidebars#Best-practices)
- [ ] Toolbar: max. drei Gruppen, Symbole ohne Rahmen, eine prominente Aktion trailing, Suche trailing, anpassbar bei vielen Items (hig:toolbars)
- [ ] Keine Switches/Checkboxes/Square/Image/Help Buttons/Path Controls im Fensterrahmen (hig:toggles#macOS, hig:buttons#macOS, hig:path-controls)
- [ ] Tabellen: sortierbare Spaltenköpfe, skalierbare Spalten; hierarchische Daten im Outline View (hig:lists-and-tables#macOS)
- [ ] Settings-Fenster: nicht anpassbare Toolbar, aktiver Pane markiert, Titel = Pane, letzter Pane wiederhergestellt, Minimize/Zoom gedimmt (hig:settings#macOS)
- [ ] Sheets lassen andere App-Fenster bedienbar; wiederholte Eingaben im Panel statt Sheet (hig:sheets#macOS)
- [ ] Tooltips für Icon-only-Controls, ≤ 60–75 Zeichen (hig:offering-help#macOS-visionOS)
- [ ] Kontextmenü auf allen relevanten Objekten (hig:mac-catalyst#Menus)

**Material & System**
- [ ] Liquid Glass nur auf Funktionsebene, nicht im Inhalt; keine eigenen Toolbar-Hintergründe (hig:materials#Liquid-Glass, hig:toolbars)
- [ ] Inhalte laufen unter Sidebar/Toolbar weiter bzw. Background Extension Effect (hig:layout#Visual-hierarchy)
- [ ] Dynamische Systemfarben, Light/Dark/Increased Contrast getestet (hig:color)
- [ ] Menu Bar Extra (falls vorhanden): Template-Symbol, Menü, optional, Funktionen auch im Dock-Menü/App (hig:the-menu-bar#Menu-bar-extras)
- [ ] App-Icon aus Icon Composer, quadratische unmaskierte Ebenen, Dark/Clear/Tinted geprüft (hig:app-icons)
- [ ] Autosave-Status korrekt signalisiert (Punkt im Close-Button nur bei deaktiviertem Autosave) (hig:file-management#macOS)

---

## 11. Häufige Fehler / Anti-Patterns

- **iPad-/iPhone-Port ohne Mac-Anpassung:** Tab Bar unten, Buttons an Seiten-/Unterkante, Popover statt Inspector, Aktionen nur in der UI statt im Menü. Auf dem Mac: Sidebar oder Segmented Control statt Tab Bar, Top-Level-Bereiche zusätzlich im View-Menü, Controls in die Fenster-Toolbar, Next/Previous zusätzlich zu Swipe (hig:mac-catalyst#Navigation, hig:mac-catalyst#Layout).
- **Fehlende Menübefehle/Kürzel:** Befehle nur in Toolbar oder Kontextmenü – Toolbar ist ausblend-/anpassbar, also nie einziger Ort (hig:toolbars#macOS).
- **Settings-Zahnrad in der Toolbar** statt App-Menü + Command-Komma (hig:settings#macOS).
- **Eigene Fensterchrome** oder nachgebaute Ampelknöpfe (hig:windows#Best-practices).
- **Kritische Aktionen in der Bottom Bar** (hig:windows#macOS).
- **Standardkürzel umgewidmet** oder neue Kürzel durch Modifier-Zusatz zu fremden Befehlen (Shift-Cmd-Z für Nicht-Redo) (hig:keyboards#Custom-keyboard-shortcuts).
- **Menu Bar Extra öffnet Popover** oder wird ungefragt installiert (hig:the-menu-bar#Menu-bar-extras).
- **Liquid Glass im Inhalt** oder auf vielen eigenen Controls; mehrere farbig getönte Toolbar-Buttons (hig:materials#Liquid-Glass, hig:color#Liquid-Glass-color).
- **Segmented Control zum View-Wechsel im Hauptbereich** statt Tab View (hig:segmented-controls#macOS).
- **Hover-/Pointer-Feedback fehlt**, falsche Cursor (z. B. Pointing Hand ohne Link) (hig:pointing-devices#Pointers).
- **Automatisches Vollbild** oder eigenes Fenstermodus-Menü; Zoom-Button für Vollbild missbraucht (hig:going-full-screen#macOS, hig:the-menu-bar#Window-menu).
- **Panels im Window-Menü-Dokumentenliste** oder mit aktivem Minimize (hig:panels).
- **„Save As“/„Export“ statt „Duplicate“** für einfache Kopien (hig:the-menu-bar#File-menu).
- **Touch-Maße unverändert übernommen** (44-pt-Ziele, große Abstände) – ergibt auf dem Mac unnötig geringe Informationsdichte; Mac-Default für Controls ist 28x28 pt, große Displays sollen mehr Inhalt in weniger Ebenen zeigen (hig:accessibility#Mobility, hig:designing-for-macos).

---

## Widersprüche und Unklarheiten im Spiegel

- **Trefferflächen:** (hig:buttons#Best-practices) nennt allgemein mindestens 44x44 pt, (hig:accessibility#Mobility) für macOS 28x28 pt Default und 20x20 pt Minimum. Für Mac-Controls gilt die plattformspezifische Tabelle; die 44-pt-Regel ist touch-geprägt.
- **App-Icon:** (hig:mac-catalyst#App-icons, Stand 2023) verlangt eine eigene macOS-Version im „lifelike rendering style“; (hig:app-icons, Stand 2026) behandelt iOS/iPadOS/macOS einheitlich (quadratisch, Icon Composer, Liquid Glass) und nennt keine macOS-Besonderheiten. Aktuellere Seite (app-icons) hat Vorrang. Ebenso spricht app-icons bei Erscheinungsvarianten von „Home Screen“, obwohl macOS mitgemeint ist.
- **Settings:** (hig:mac-catalyst) listet „App-spezifische Settings in der System-Settings-App“ als Catalyst-Feature; (hig:settings#macOS) beschreibt ein eigenes Settings-Fenster über das App-Menü. Für native Mac-Apps das eigene Fenster verwenden.
- **Widget-Rendering:** (hig:widgets#Appearances) sagt, Accented Rendering gelte für System-Family-Widgets „auf allen Plattformen“; die Tabelle daneben nennt für Mac „Accented: Not supported“.
- **Tab Views:** „nicht mehr als sechs Tabs“ und im selben Absatz „wenn Sie sechs oder mehr Tabs brauchen“ (hig:tab-views#Best-practices).
- **Tastaturkürzel-Tabelle:** Command-I doppelt (Italic und Info-Fenster), F12 „Dashboard“ (Funktion existiert in aktuellem macOS nicht mehr) (hig:keyboards#Standard-keyboard-shortcuts). Kontextabhängig auflösen, Dashboard ignorieren.
- **New York:** (hig:typography#macOS) nennt NY nur für Mac-Catalyst-Apps, die allgemeine Developer-Note verweist auf `Font.Design.serif` plattformübergreifend. Verfügbarkeit in nativen Mac-Apps im Zweifel prüfen.
- **Größere Schrift:** macOS hat kein Dynamic Type, (hig:accessibility#Vision) empfiehlt dennoch Vergrößerung auf mindestens 200 % – auf dem Mac also über eigene UI (z. B. Schriftgrößen-Einstellung, Zoom-Befehle).
- **Settings-Fenster:** HIG spricht von „maximize button“, auf macOS heißt das Element Zoom-Button (hig:settings#macOS).
- **Keine Fenstermaße:** Weder Default- noch Mindestgrößen für Mac-Fenster sind im Spiegel enthalten.
