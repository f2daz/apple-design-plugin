# watchOS – Plattformreferenz

Quelle: lokaler HIG-Spiegel (`~/.apple-design/hig/pages`, Stand 2026-10-21). Belege als `(hig:<slug>)` bzw. `(hig:<slug>#Anker)`. Alle Zahlen stammen aus dem Spiegel; fehlende Werte sind als Lücke markiert, nicht geschätzt.

---

## 1. Kurzprofil

- **Nutzungskontext:** am Handgelenk, oft in Bewegung; Interaktionen meist unter einer Minute, viele Blicke pro Tag; Complications, Notifications und Siri werden häufiger genutzt als die App selbst (hig:designing-for-watchos).
- **Ergonomie:** Sichtabstand höchstens etwa ein Fuß; Bedienung mit der anderen Hand; Always On zeigt Inhalte bei gesenktem Handgelenk gedimmt (hig:designing-for-watchos, hig:always-on).
- **Eingabe:** Digital Crown (primäre Navigation seit watchOS 10), Tap/Swipe/Drag, Double Tap (watchOS 11+), Action Button (Ultra), Siri/Shortcuts, Diktat/Scribble; keine physische Tastatur (hig:digital-crown, hig:gestures#watchOS, hig:action-button#watchOS, hig:keyboards).
- **Display:** klein, hochauflösend, rund maskierte Icons; mehrere Gehäusegrößen (38–49 mm in den Tabellen) (hig:designing-for-watchos, hig:app-icons).
- **Sensorik:** GPS, Blutsauerstoff, Herzfunktion, Höhenmesser, Beschleunigung, Gyroskop (hig:designing-for-watchos).
- **Kein Dark/Light-Umschalter:** Dark Mode wird auf watchOS nicht unterstützt (hig:dark-mode).
- **App soll eigenständig funktionieren** und Complications/Notifications um Details ergänzen (hig:designing-for-watchos).

---

## 2. Nicht verhandelbar

1. Glanceable: das Wichtigste auf einen Blick, Ziel mit ein bis zwei Gesten erreichbar (hig:designing-for-watchos).
2. Flache Hierarchie; vertikale Navigation an der Digital Crown verankern, jeweils mit Touch-Alternative (hig:designing-for-watchos, hig:digital-crown).
3. Auf Drehungen der Digital Crown sichtbar reagieren, Tempo der Drehung respektieren; Crown-Drücke sind für das System reserviert (hig:digital-crown).
4. Mehrere Detailseiten als vertikal paginierte Tab View, nicht horizontal und nicht tief verschachtelt (hig:page-controls#watchOS, hig:split-views#watchOS).
5. Pro Zeile max. drei Glyph-Buttons oder zwei Text-Buttons; primäre Aktionen als volle Breite (hig:layout#watchOS, hig:buttons#watchOS).
6. Lade-/Fortschrittsindikatoren vermeiden; Inhalte sofort zeigen (hig:loading#watchOS, hig:feedback#watchOS).
7. Always On: sensible Daten verbergen, Layout stabil halten, Nebensächliches dimmen, Bewegung sanft auslaufen lassen (hig:always-on).
8. Complications mit dynamischen, relevanten Daten; möglichst alle Familien; jede mit eigenem Deep Link; Tinted Mode einplanen (hig:complications).
9. Short Look nie als einzigen Kanal für Wichtiges, keine sensiblen Daten im Titel (hig:notifications#watchOS).
10. Primary Action für Double Tap nicht in Views mit Listen, Scroll Views oder vertikalen Tabs setzen (hig:gestures#watchOS).
11. Text nicht kleiner als 12 pt (Default 16 pt); Vergrößerung auf mindestens 140 % ermöglichen (hig:typography#Ensuring-legibility, hig:accessibility#Vision).
12. Controls Default 44x44 pt, Minimum 28x28 pt (hig:accessibility#Mobility).
13. Activity Rings nur für Move/Exercise/Stand einer Person, unverändert, auf Schwarz (hig:activity-rings).
14. Keine eigenen Einträge in der System-Settings-App; wenige Optionen unten in der Hauptansicht oder im More-Menü (hig:settings#watchOS).
15. App-Icon-Hintergrund nicht schwarz (hig:app-icons#watchOS).

---

## 3. Layout & Maße

### Allgemeine Werte

| Größe | Wert | Quelle |
|---|---|---|
| Text Default / Minimum | 16 pt / 12 pt | (hig:typography#Ensuring-legibility) |
| Control Default / Minimum | 44x44 pt / 28x28 pt | (hig:accessibility#Mobility) |
| Abstand um Elemente mit / ohne Bezel | ca. 12 pt / ca. 24 pt | (hig:accessibility#Mobility) |
| Textvergrößerung | mindestens 140 % | (hig:accessibility#Vision) |
| Buttons nebeneinander | max. 3 mit Glyphen, max. 2 mit Text | (hig:layout#watchOS) |
| Action Sheet | max. 4 Buttons inkl. Cancel | (hig:action-sheets#watchOS) |
| Notification-Aktionen (Long Look) | bis zu 4 eigene + System-Dismiss | (hig:notifications#watchOS) |
| Long-Look-Hintergrund wie System | Weiß mit 18 % Deckkraft | (hig:notifications#watchOS) |
| Karten-Annotationen | bis zu 5 | (hig:maps#watchOS) |
| Complication-Linienstärke | 2 pt oder mehr | (hig:complications#Visual-design) |
| Widget-Text | 11 pt oder größer | (hig:widgets#Displaying-text-in-widgets) |
| Widget-Ränder | 16 pt Standard, 11 pt eng | (hig:widgets#Choosing-margins-and-padding) |
| Widget-Update-Animation | bis zu 2 Sekunden | (hig:widgets#Updating-widget-content) |
| App-Icon | 1088x1088 px, quadratisch, System maskiert kreisförmig | (hig:app-icons#Specifications) |
| Video | max. 30 s; H.264 High Profile; 160 kbps bis 30 fps; Vollbild 208x260 px (Hochformat), 16:9 320x180 px | (hig:playing-video#watchOS) |
| Audio | 64 kbps HE-AAC | (hig:playing-audio#watchOS) |

### Gerätegrößen – was der Spiegel tatsächlich hergibt

**Lücke:** Der Spiegel enthält keine Bildschirmauflösungen (pt/px) der Apple-Watch-Modelle. (hig:layout) erwähnt im Change Log hinzugefügte Watch-Spezifikationen, die Tabellen fehlen aber im aktuellen Seitenstand. Verfügbar sind nur größenbezogene Ableitungen:

| Gehäuse | Widget / Live Activity im Smart Stack (pt) | PDF-Autoskalierung | Dynamic-Type-Default |
|---|---|---|---|
| 38 mm | – | 90 % | Small |
| 40 mm | 152x69.5 | 100 % | Large |
| 41 mm | 165x72.5 | 106 % | Large |
| 42 mm | 176x72.5 | 100 % (siehe Hinweis) | Large |
| 44 mm | 173x76.5 | 110 % | xLarge |
| 45 mm | 184x80.5 | 119 % | xLarge |
| 46 mm | 194x80.5 | – | – (nicht genannt) |
| 49 mm (Ultra 3, 4) | 198x81.5 | 119 % | xLarge |
| 49 mm (Ultra 1, 2) | 191x81.5 | 119 % | xLarge |

Quellen: (hig:widgets#Specifications), (hig:live-activities#watchOS), (hig:images#watchOS), (hig:typography#Specifications). Bilder als autoskalierende PDFs für 40/42 mm @2x anlegen (hig:images#watchOS).

**Hinweis 42 mm:** Die Bild-Skalierungstabelle und die Complication-Tabellen („40mm/42mm“) beziehen sich offenbar auf das ältere 42-mm-Gehäuse; die Widget-Tabelle (176x72.5 pt) auf das neuere. Der Spiegel unterscheidet das nicht explizit – bei 42 mm und 46 mm jeweils Generation klären.

### Complication-Bildgrößen (Auszug, aktuelle Familien)

| Layout | 40 mm | 41 mm | 44 mm | 45/49 mm |
|---|---|---|---|---|
| Circular Image | 42x42 pt | 44.5x44.5 pt | 47x47 pt | 50x50 pt |
| Circular Closed Gauge | 27x27 pt | 28.5x28.5 pt | 31x31 pt | 32x32 pt |
| Extra Large Circular Image | 120x120 pt | 127x127 pt | 132x132 pt | 143x143 pt |
| Corner Circular | 32x32 pt | 34x34 pt | 36x36 pt | 38x38 pt |
| Corner Gauge/Text | 20x20 pt | 21x21 pt | 22x22 pt | 24x24 pt |
| Rectangular Large Image mit Titel | 150x47 pt | 159x50 pt | 171x54 pt | 178.5x56 pt |
| Rectangular Large Image ohne Titel | 162x69 pt | 171.5x73 pt | 184x78 pt | 193x82 pt |

Vollständige Tabellen inkl. Open Gauge, Stack, Placeholder, Inline (Utilitarian) und Legacy-Templates: (hig:complications). Großbild-Layouts erhalten automatisch 4 pt Eckenradius; Circular-Bilder werden kreisförmig maskiert (hig:complications#Rectangular, hig:complications#Circular).

**Default-Textwerte der SwiftUI-Complication-Layouts** (alle Rounded) (hig:complications):
- Circular (regulär): Medium, 12 / 12.5 / 13 / 14.5 pt (40 / 41 / 44 / 45–49 mm)
- Extra Large Circular: Medium, 34.5 / 36.5 / 36.5 / 41 pt
- Corner: Semibold, 10 / 10.5 / 11 / 12 pt
- Rectangular: Medium, 16.5 / 17.5 / 18 / 19.5 pt

### Layoutregeln
- Seiten möglichst auf eine Bildschirmhöhe begrenzen; variable Höhen nur sparsam und nach den festen Seiten (hig:page-controls#watchOS, hig:scroll-views#watchOS).
- Detailansichten kurz halten, wenn vertikale Seitennavigation zwischen Listeneinträgen funktionieren soll – scrollende Details brechen sie (hig:lists-and-tables#watchOS).
- Listen kurz halten; bei langen Listen relevanteste Einträge zuerst plus „mehr anzeigen“ (hig:lists-and-tables#watchOS).
- Autorotation nur für Inhalte, die man anderen zeigt (Bild, QR-Code) (hig:layout#watchOS).
- Karten vollständig ohne Scrollen sichtbar, kleinster Ausschnitt, der alle Punkte umfasst (hig:maps#watchOS).
- Vollflächige Hintergrundfarbe nicht in lange sichtbaren Views (Workout, Audio) (hig:color#watchOS).

---

## 4. Navigation & Struktur

| Situation | Muster | Quelle |
|---|---|---|
| Eine Liste oder ein Inhalt | Vertikal scrollend, Digital Crown scrollt | (hig:scroll-views#watchOS) |
| Mehrere gleichrangige Ansichten | Vertikale Tab View (Seiten), Page Indicator neben der Crown | (hig:page-controls#watchOS, hig:tab-views#watchOS) |
| Liste → Detail | Split View zeigt Liste oder Detail im Vollbild; beim Start relevantestes Detail zeigen | (hig:split-views#watchOS) |
| Mehrere Detailseiten zu einem Eintrag | Details in vertikale Tab View | (hig:split-views#watchOS) |
| Hierarchie | so flach wie möglich; horizontale Paginierung und tiefe Hierarchien sind schlechter als vertikale Seiten | (hig:page-controls#watchOS, hig:designing-for-watchos) |
| Kurze modale Aufgabe mit eigenem Titel/Inhalt | Sheet (Vollbild, Material dahinter) | (hig:sheets#watchOS) |
| Wichtige Info oder Auswahl | Alert oder Action Sheet statt Sheet | (hig:sheets#watchOS) |
| Verwandte Aktion zu einer Ansicht | Toolbar-Button oben in den Ecken oder unten; scrollender Toolbar-Button erscheint beim Hochscrollen | (hig:toolbars#watchOS) |

- Page Indicator wechselt zwischen Seitenposition und Scroll-Position innerhalb einer langen Seite (hig:page-controls#watchOS, hig:scroll-views#watchOS).
- Sheets nicht zur Navigation nutzen; Schließen-Label nicht wie Seitentitel aussehen lassen, ggf. SF Symbol (hig:sheets#watchOS).
- Pickers werden mit der Crown bedient; lange Listen als Navigation-Link-Picker (Button, der die Liste öffnet, Crown scrubbt direkt) (hig:pickers#watchOS).
- Textfelder nur wenn nötig; lieber Auswahllisten. Tastatur nur auf ausreichend großen Displays, sonst Diktat/Scribble; Eingabe auch über gekoppeltes iPhone (hig:text-fields#watchOS, hig:virtual-keyboards#watchOS).
- Suchfeld öffnet bildschirmfüllende Texteingabe, Rückkehr erst nach Cancel/Search (hig:search-fields#watchOS).

---

## 5. Komponenten-Besonderheiten (Platform considerations)

- **Buttons:** Inline-Buttons sind Kapseln mit kontrastierendem Material; primäre Aktion über volle Breite; zwei nebeneinander nur mit gleicher Höhe und kurzem Inhalt; gestapelte ein-/zweizeilige Text-Buttons gleich hoch (hig:buttons#watchOS).
- **Toolbar:** Buttons in den oberen Ecken oder unten, bleiben über scrollendem Inhalt sichtbar; System verschiebt Uhrzeit und Titel; Toolbar-Buttons erhalten Liquid Glass; für Navigation zu verwandten Bereichen oder kontextuelle Aktionen (hig:buttons#watchOS, hig:toolbars#watchOS).
- **Double Tap (watchOS 11+):** scrollt Listen/Scroll Views, blättert vertikale Tabs; optionale Primary Action (Button/Toggle) in nicht scrollenden Views – die meistgenutzte Aktion, z. B. Play/Pause; auch für Widgets/Live Activities im Smart Stack (hig:gestures#watchOS).
- **Action Button (Ultra):** Sekundärfunktion soll die Primäraktion logisch fortsetzen (z. B. Segment markieren), nicht beenden; Action + Seitentaste = Pause (Ausnahme Tauchen) (hig:action-button#watchOS).
- **Action Sheets:** Default/Destructive/Cancel-Stil; max. 4 Buttons inkl. Cancel (hig:action-sheets#watchOS).
- **Sheets:** Vollbild, halbtransparent mit blurrendem/entsättigendem Material; kurz und selten (hig:sheets#watchOS).
- **Listen:** begrenzen; Crown-Haptik mit Detents pro Zeile, bei stark unterschiedlichen Zeilenhöhen lineare Detents erwägen (hig:lists-and-tables#watchOS, hig:digital-crown).
- **Slider:** horizontale Spur mit +/- Buttons, diskret oder kontinuierlich; eigene Glyphen bei Bedarf (hig:sliders#watchOS).
- **Labels:** System-Datums-/Timer-Text passt sich selbst an und aktualisiert ohne App (hig:labels#watchOS).
- **Charts:** keine komplexen Interaktionen; Details der iPhone-App überlassen (hig:charts#watchOS).
- **Fortschritt:** Indikator standardmäßig weiß, per Tint färbbar; Indeterminate vermeiden, stattdessen Benachrichtigung bei Abschluss zusagen (hig:progress-indicators#watchOS, hig:feedback#watchOS).
- **Karten:** statische Snapshots, Tap öffnet Karten-App (hig:maps#watchOS).
- **Medien:** Audio vom System verwaltet, Hintergrundaudio möglich, Now Playing View anbieten; Video nur im Vordergrund, kurz, Poster-Bild darf nicht wie ein Control aussehen (hig:playing-audio#watchOS, hig:playing-video#watchOS).
- **Bilder:** Transparenz vermeiden (Dateigröße), außer bei Template-Bildern (Complications, Menü-Icons); Animationen bevorzugt mit SwiftUI (hig:images#watchOS, hig:image-views#watchOS).
- **Motion:** Layout-/Erscheinungs-Animationen haben fest eingebautes Easing, nicht abschaltbar (hig:motion#watchOS).
- **Teilen:** ShareLink für das System-Share-Sheet (hig:collaboration-and-sharing#watchOS).
- **Accounts:** iCloud-Keychain-Sync für Autofill und Einstellungen (hig:managing-accounts#watchOS).
- **In-App-Kauf:** gleiche Pflichtangaben wie auf anderen Plattformen; Unterschiede der Watch-Version klar benennen; modales Sheet mit Close; Optionen kompakt vergleichbar (ein Button pro Option oder Liste + Button) (hig:apple-in-app-purchase#watchOS).
- **Game Center:** keine System-UI auf der Watch; erscheint auf dem iPhone (hig:game-center#watchOS).
- **Nearby Interaction:** nur Distanz, App muss im Vordergrund sein (hig:nearby-interactions#watchOS).
- **Wallet:** Pässe erscheinen auch ohne Watch-App; Strip-Bild wird zugeschnitten (hig:wallet#watchOS).

---

## 6. Liquid Glass, Materialien, aktuelles Design-System

- Liquid Glass ist die Funktionsebene über dem Inhalt; nie im Content Layer; sparsam bei eigenen Controls; *clear* nur über reichem Medienhintergrund (plattformübergreifend, gilt auch für watchOS) (hig:materials#Liquid-Glass).
- **Toolbar-Buttons** erhalten automatisch Liquid Glass und heben sich so vom Inhalt ab (hig:buttons#watchOS).
- **Inline-Buttons** erhalten ein kontrastierendes Material (hig:buttons#watchOS).
- **Materialien in Vollbild-Modals** zur Orientierung nutzen; vom System gelieferte Material-Hintergründe von Sheets nicht entfernen oder ersetzen (hig:materials#watchOS).
- **Hintergrundfarbe mit Bedeutung:** Farbe als Informationsträger (z. B. Activity-Infografiken in Ringfarbe), nicht als Dekoration (hig:color#watchOS, hig:designing-for-watchos).
- **Smart-Stack-Widgets:** Standard-Hintergrund schwarz; bedeutungstragende Hintergrundfarbe erwägen (Stocks: rot/grün) (hig:widgets#watchOS).
- **Accented Rendering:** Auf Apple Watch werden Primärinhalte weiß, akzentuierte Inhalte in der Zifferblattfarbe getönt; in der Clear-Darstellung ersetzt ein Liquid-Glass-Hintergrund den Widget-Hintergrund (hig:widgets#Appearances, hig:widgets#Rendering-modes).
- **Tinted Mode bei Complications:** System entsättigt und tönt in einer Farbe; Information nie nur über Farbe; ggf. eigene Tinted-Variante liefern (hig:complications#Visual-design, hig:widgets#Using-color).
- **App-Icon:** geschichtet, Liquid-Glass-Effekte durch das System, Ebenen in Icon Composer, quadratische unmaskierte Ebenen, Inhalt zentriert (Kreismaske), keine eigenen Schatten/Glows, kein schwarzer Hintergrund (hig:app-icons).

---

## 7. Typografie

- Systemschrift **SF Compact**; **SF Compact Rounded** in Complications; New York ist zusätzlich nutzbar (hig:typography#watchOS).
- Default 16 pt, Minimum 12 pt; leichte Schnitte vermeiden; Dynamic Type wird unterstützt (hig:typography).
- In Bewegung (Workouts): große Schrift, hoher Kontrast, Wichtigstes zuerst (hig:workouts).

### watchOS Dynamic Type – Default-Größen je Gehäuse (hig:typography#Specifications)

| Style | Small (Default 38 mm) | Large (Default 40/41/42 mm) | xLarge (Default 44/45/49 mm) | Weight | Emphasized |
|---|---|---|---|---|---|
| Large Title | 32 / 34.5 | 36 / 38.5 | 40 / 42.5 | Regular | Bold |
| Title 1 | 30 / 32.5 | 34 / 36.5 | 38 / 40.5 | Regular | Semibold |
| Title 2 | 26 / 28.5 | 28 / 30.5 | 30 / 32.5 | Regular | Semibold |
| Title 3 | 18 / 20.5 | 19 / 21.5 | 20 / 22.5 | Regular | Semibold |
| Headline | 15 / 17.5 | 16 / 18.5 | 17 / 19.5 | Semibold | Semibold |
| Body | 15 / 17.5 | 16 / 18.5 | 17 / 19.5 | Regular | Semibold |
| Caption 1 | 14 / 16.5 | 15 / 17.5 | 16 / 18.5 | Regular | Semibold |
| Caption 2 | 13 / 15.5 | 14 / 16.5 | 15 / 17.5 | Regular | Semibold |
| Footnote 1 | 12 / 14.5 | 13 / 15.5 | 14 / 16.5 | Regular | Semibold |
| Footnote 2 | 11 / 13.5 | 12 / 14.5 | 13 / 15.5 | Regular | Semibold |

Werte: Größe / Leading in pt. Weitere Stufen im Spiegel: xSmall, xxLarge, xxxLarge sowie AX1–AX3 (z. B. Body AX3 = 23/25.5 pt). Tracking-Werte für SF Compact und SF Compact Rounded: (hig:typography#Tracking-values).

---

## 8. Systemintegration

**Complications** (hig:complications, hig:widgets#Accessory-widgets)
- Familien seit watchOS 9 (WidgetKit-Accessories): circular, corner, inline, rectangular; dazu Extra-Large-Circular für das X-Large-Zifferblatt; Legacy-Templates (ClockKit) nur für ältere watchOS-Versionen.
- Inhalt: wesentliche, dynamische Daten; statische „App-Starter“-Complications werden eher entfernt; wenn eine Familie keine sinnvollen Daten zulässt, App-Icon-artiges Bild zum Starten.
- Mehrere Complications pro Familie, je eigener Deep Link; Timeline-Updates sind begrenzt – Zeitpunkte bewusst wählen.
- Gauges: closed (Anteil am Ganzen), open (beliebiger Bereich), segmented (schnelle Wertänderungen).
- Statische Placeholder-Bilder für jede Complication liefern.
- Inline-Accessory bietet nur ein Tap-Ziel (hig:widgets#Adding-interactivity).

**Watch Faces** (hig:watch-faces): teilbare Zifferblätter mit eigenen Complications kuratieren, Vorschau mit Bezel bereitstellen, für alle Geräte Varianten anbieten, bei inkompatiblem Zifferblatt Alternative statt Fehler.

**Smart Stack / Widgets** (hig:widgets#watchOS, hig:complications#Rectangular)
- Rechteckige und runde Accessory-Widgets erscheinen im Smart Stack; Crown-Drehung auf dem Zifferblatt öffnet ihn (hig:digital-crown).
- Relevanz signalisieren (Ort, laufende Aktivität wie Workout), damit das System das Widget hochstuft (RelevanceKit).
- Eigenes, für den Smart Stack optimiertes Layout und bedeutungstragende Hintergrundfarbe erwägen.

**Live Activities** (hig:live-activities#watchOS)
- iPhone-Live-Activity erscheint oben im Smart Stack; Standard kombiniert leading/trailing der Compact-Darstellung.
- Eigenes Watch-Layout erwägen (mehr Info, Button/Toggle) – aber dieses Layout gilt auch in CarPlay, wo Interaktion deaktiviert ist; bei Fahrt-Szenarien keine Buttons/Toggles.
- Fokus: Fortschritt, Steuerung (Timer), signifikante Updates. Größen wie Widgets (Tabelle Abschnitt 3).

**Notifications** (hig:notifications#watchOS)
- Short Look beim Heben des Handgelenks, verschwindet beim Senken – diskret, kein sensibler Titel.
- Long Look: Sash oben (App-Icon + Name, Farbe oder Blur), Inhaltsbereich frei gestaltbar, bis zu 4 Aktionen, System-Dismiss unten; mindestens statisches, bevorzugt zusätzlich dynamisches Interface; Ressourcen des statischen Interface mitliefern.
- Double Tap löst die erste nicht destruktive Aktion aus – häufigste Aktion zuerst.
- iPhone-Notification-Einstellungen gelten standardmäßig auch auf der Watch (hig:managing-notifications#watchOS).
- Titel besonders kurz (hig:notifications#Content).

**Always On** (hig:always-on): App bleibt sichtbar, solange sie vorn ist oder eine Hintergrundsitzung läuft; sensible Daten verbergen; Interaktives in „nicht verfügbar“-Darstellung überführen statt entfernen; seltene, subtile Updates.

**Workouts** (hig:workouts)
- Workout-Session nutzen: App bleibt zwischen Handgelenk-Hebungen sichtbar; relevante Metriken (Zeit, Kalorien, Distanz) und Steuerung (Runde, Intervall).
- Keine irrelevanten Inhalte während des Workouts; eigenes, klar erkennbares Erscheinungsbild der aktiven Session.
- Pause/Resume/Stop leicht erreichbar, klares Start-/Stopp-Feedback.
- Fehlende Sensordaten (z. B. Herzfrequenz im Wasser) in Workout-App-ähnlicher Sprache erklären.
- Zusammenfassung am Ende, ggf. mit Activity Rings; sehr kurze Sessions verwerfen oder nachfragen.

**Activity Rings** (hig:activity-rings): immer drei Ringe auf watchOS; nur Move/Exercise/Stand einer Person; Farben, Deckkraft nie ändern; schwarzer Hintergrund mit sichtbarem Rand; Mindestaußenrand = Abstand zwischen den Ringen; nicht dekorativ, nicht in Notifications, nicht im Icon/Marketing; keine Notifications, die Activity-App-Meldungen wiederholen.

**Haptics** (hig:playing-haptics#watchOS): Notification, Up, Down, Success, Failure, Retry, Start, Stop, Click – nur in ihrer Bedeutung verwenden; Click sparsam. Crown-Detents: Standard nutzen oder abschalten, wenn sie nicht zur Animation passen (hig:digital-crown).

---

## 9. Umsetzung: SwiftUI-Mapping

| Konzept | API | Beleg |
|---|---|---|
| Vertikale Seiten | `TabView { … }.tabViewStyle(.verticalPage)` | TabView verlinkt (hig:tab-views#watchOS); Style-Name Standard-API |
| Hierarchische Navigation | `NavigationStack`, `NavigationLink` | Standard-API |
| Liste → Detail | `NavigationSplitView` (zeigt Liste oder Detail im Vollbild) | Verhalten (hig:split-views#watchOS) |
| Toolbar-Positionen | `ToolbarItem(placement: .topBarLeading / .topBarTrailing / .bottomBar)` | verlinkt (hig:toolbars#watchOS) |
| Scrollender Toolbar-Button | `ToolbarItem(placement: .primaryAction)` | verlinkt (hig:toolbars#watchOS) |
| Double-Tap-Primäraktion | `.handGestureShortcut(.primaryAction)` | verlinkt (hig:gestures#watchOS) |
| Crown-Eingabe | `.digitalCrownRotation(...)` mit `.focusable()` | Standard-API |
| Picker | `Picker`, `DatePicker`; `.pickerStyle(.navigationLink)` | verlinkt (hig:pickers#watchOS) |
| Text-Inhaltstyp | `.textContentType(_:)` | verlinkt (hig:virtual-keyboards#watchOS) |
| Teilen | `ShareLink` | verlinkt (hig:collaboration-and-sharing#watchOS) |
| Datum/Timer-Labels | `Text(date, style: .timer)` u. ä. | `Text` verlinkt (hig:labels#watchOS) |
| Video | `VideoPlayer` | verlinkt (hig:playing-video#watchOS) |
| Complications / Smart Stack | WidgetKit, `WidgetFamily.accessoryCircular / .accessoryCorner / .accessoryInline / .accessoryRectangular` | accessoryRectangular verlinkt (hig:complications#Rectangular) |
| Akzentgruppe | `.widgetAccentable()`; `WidgetRenderingMode` | verlinkt (hig:widgets#Rendering-modes) |
| Placeholder | `placeholder(in:)` im Timeline Provider | verlinkt (hig:complications#Visual-design) |
| Relevanz | RelevanceKit | verlinkt (hig:widgets#watchOS) |
| Always On | `@Environment(\.isLuminanceReduced)` | Standard-API |
| Workouts | HealthKit `HKWorkoutSession` | Standard-API |
| Haptik | `WKInterfaceDevice.current().play(_:)` mit `WKHapticType` | WKHapticType verlinkt (hig:playing-haptics#watchOS) |
| Autorotation | `isAutorotating` (WatchKit) | verlinkt (hig:layout#watchOS) |

Einträge mit „Standard-API“ sind im Spiegel nicht verlinkt – vor Verwendung gegen die aktuelle Developer-Dokumentation prüfen. ClockKit nur noch für Complications vor watchOS 9 (hig:complications).

---

## 10. Review-Checkliste

**Glanceability & Navigation**
- [ ] Kernaufgabe in ein bis zwei Gesten; wichtigste Info ohne Scrollen sichtbar (hig:designing-for-watchos)
- [ ] Navigation vertikal und Crown-gesteuert, Touch-Alternative vorhanden (hig:digital-crown)
- [ ] Mehrere Ansichten als vertikale Tab View statt horizontaler Paginierung oder tiefer Hierarchie (hig:page-controls#watchOS)
- [ ] Seiten möglichst eine Bildschirmhöhe; variable Höhen nur hinter festen Seiten (hig:scroll-views#watchOS)
- [ ] Beim Start relevantestes Detail statt leerer Übersicht (hig:split-views#watchOS)
- [ ] Sheets nur für kurze modale Aufgaben; Alerts/Action Sheets (≤ 4 Buttons) für Entscheidungen (hig:sheets#watchOS, hig:action-sheets#watchOS)
- [ ] Crown-Drehung zeigt sichtbare Reaktion; keine Logik auf Crown-Druck (hig:digital-crown)
- [ ] Double-Tap-Primäraktion nur in nicht scrollenden Views (hig:gestures#watchOS)

**Layout & Lesbarkeit**
- [ ] Max. 3 Glyph- bzw. 2 Text-Buttons pro Zeile; Primäraktion volle Breite (hig:layout#watchOS, hig:buttons#watchOS)
- [ ] Controls ≥ 28x28 pt, Ziel 44x44 pt (hig:accessibility#Mobility)
- [ ] Text ≥ 12 pt, Dynamic Type inkl. AX-Größen getestet, Vergrößerung ≥ 140 % (hig:typography, hig:accessibility#Vision)
- [ ] Getestet auf kleinstem und größtem Gehäuse (38/40 mm bis 49 mm) (hig:layout#Adaptability)
- [ ] Keine Lade-Spinner bei normalen Interaktionen; bei 1–2 s Wartezeit Indikator statt leerem Screen (hig:loading#watchOS)
- [ ] Textfelder nur wenn nötig; Auswahllisten bevorzugt (hig:text-fields#watchOS)
- [ ] Keine vollflächige Hintergrundfarbe in lang sichtbaren Views (hig:color#watchOS)

**Material & Optik**
- [ ] Liquid Glass nur über System-Toolbar/Controls, nicht im Inhalt (hig:materials#Liquid-Glass, hig:buttons#watchOS)
- [ ] Standard-Material von Sheets/Modals nicht entfernt (hig:materials#watchOS)
- [ ] App-Icon: kein schwarzer Hintergrund, Motiv zentriert für Kreismaske, 1088x1088 px (hig:app-icons)

**Systemintegration**
- [ ] Complications für möglichst alle Familien, dynamische Daten, je eigener Deep Link (hig:complications)
- [ ] Complications im Tinted Mode verständlich, Linien ≥ 2 pt, Placeholder vorhanden (hig:complications#Visual-design)
- [ ] Smart-Stack-Widget mit Relevanzsignalen und ggf. bedeutungstragender Hintergrundfarbe (hig:widgets#watchOS)
- [ ] Live Activity: Watch-Layout ohne Buttons, falls Nutzung beim Fahren wahrscheinlich (hig:live-activities#watchOS)
- [ ] Notifications: Short Look ohne sensible Daten; Long Look statisch + dynamisch; ≤ 4 Aktionen, häufigste zuerst (hig:notifications#watchOS)
- [ ] Always On: sensible Daten verborgen, Layout stabil, Nebensächliches gedimmt (hig:always-on)
- [ ] Workout: Session aktiv, relevante Metriken, leicht erreichbares Pause/Stop, Zusammenfassung (hig:workouts)
- [ ] Activity Rings unverändert, schwarz hinterlegt, nur für Move/Exercise/Stand einer Person (hig:activity-rings)
- [ ] Haptiken entsprechen ihrer Bedeutung (hig:playing-haptics#watchOS)
- [ ] Keine eigenen Einträge in der System-Settings-App (hig:settings#watchOS)

---

## 11. Häufige Fehler / Anti-Patterns

- **iPhone-App verkleinert:** zu viel Inhalt pro Screen, Tab Bar/horizontale Seiten, tiefe Navigationsstapel – statt fokussierter, vertikal paginierter Kernaufgaben (hig:designing-for-watchos, hig:page-controls#watchOS).
- **Lade-Spinner und Wartebildschirme** – Watch-Interaktionen sind Sekunden lang; lieber Ergebnis per Notification zusagen (hig:feedback#watchOS).
- **Statische Complication** als reiner App-Starter, alle Complications mit demselben Ziel (hig:complications#Best-practices).
- **Farbe als einziger Bedeutungsträger** in Complications/Widgets – geht im Tinted Mode und bei invertierten Farben verloren (hig:complications#Visual-design, hig:widgets#Using-color).
- **Sensible Daten im Short Look, auf dem Zifferblatt oder im Always On** (hig:notifications#watchOS, hig:complications, hig:always-on).
- **Primary Action in scrollenden Views** – kollidiert mit Double-Tap-Scrollen (hig:gestures#watchOS).
- **Verschachtelte Sheets / Sheets als Navigation** (hig:sheets#watchOS).
- **Activity Rings umgefärbt, dekorativ oder für fremde Daten** (hig:activity-rings).
- **Komplexe Chart-Interaktionen** statt Blick-Information (hig:charts#watchOS).
- **Lange Videos** (> 30 s) oder hochskalierte Clips (hig:playing-video#watchOS).
- **Interaktive Elemente einfach entfernen, wenn Always On beginnt** – stattdessen als nicht verfügbar darstellen (hig:always-on).
- **Action Button als „Stopp“** statt fortsetzender Sekundärfunktion (hig:action-button#watchOS).
- **Eigene Settings-Bündel** für die System-Settings-App (hig:settings#watchOS).

---

## Widersprüche und Unklarheiten im Spiegel

- **Keine Watch-Bildschirmmaße:** (hig:layout) verweist im Change Log auf Watch-Spezifikationen (u. a. Series 10/11, SE 3, Ultra 3), die Tabellen fehlen im gespiegelten Seitenstand. Keine Auflösungen nennen, bis sie belegt sind.
- **Uneinheitliche Größenraster:** Complication-Tabellen kennen 38, 40/42, 41, 44, 45/49 mm; Widget-Tabellen 40, 41, 42, 44, 45, 46, 49 mm (Ultra 1/2 vs. 3/4); Dynamic-Type-Defaults nennen 46 mm gar nicht. Für 42 mm (neu) und 46 mm fehlen Complication- und Typo-Zuordnungen.
- **Default-Textgröße:** Legibility-Tabelle nennt 16 pt Default; laut Dynamic-Type-Tabellen ist 16 pt nur auf 40/41/42 mm (Large) Default, auf 44/45/49 mm ist Body 17 pt (xLarge), auf 38 mm 15 pt (hig:typography).
- **Minimum vs. Text Styles:** Minimum 12 pt, aber Footnote 2 hat in xSmall 10 pt und in Small 11 pt (hig:typography#Specifications).
- **Ladeindikatoren:** (hig:feedback#watchOS) rät von Indeterminate-Indikatoren ab, (hig:loading#watchOS) hält bei 1–2 s Ladezeit einen Indikator für besser als einen leeren Screen. Auflösung: Indikator nur als Ausnahme für kurze unvermeidbare Wartezeit, bei längeren Prozessen Notification.
- **Complication-Tabelle Utilitarian Small, 41 mm Flat:** „10.5–23.5x21 pt“, während Utilitarian Large denselben Wert mit „x10.5 pt“ angibt – vermutlich Tippfehler; 44 mm steht jeweils auf „N/A“ (hig:complications#Inline).
- **Activity-Ring-Farben:** Die RGB-Tabelle für Move/Exercise/Stand ist im Spiegel leer (Werte nur als Bild); keine Werte übernehmen (hig:activity-rings).
- **Watch Faces:** Geräteverfügbarkeit bezieht sich auf Series 3/4 – veraltet gegenüber aktuellen Modellen (hig:watch-faces).
- **Haptik:** (hig:playing-haptics#watchOS) nennt Crown-Haptik ab Series 4, (hig:digital-crown) spricht von „den meisten Modellen“.
- **Tab Views:** Seite gibt an „Not supported in iOS, iPadOS“, enthält aber einen iOS/iPadOS-Abschnitt (hig:tab-views); für watchOS irrelevant, aber ein Hinweis auf Pflegezustand.
