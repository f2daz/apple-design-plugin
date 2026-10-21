# Inputs – Eingabemethoden (HIG-Section „Inputs“)

Verdichtete Referenz zu allen Eingabe-Seiten der Apple HIG. Quelle: lokaler HIG-Spiegel (`~/.apple-design/hig/pages/`, Sync 2026-10-21). Belege als `(hig:<slug>)` bzw. `(hig:<slug>#Anker)`. Regeln paraphrasiert; Tabellen mit Gesten und Shortcuts sind Faktenübersichten.

Schreibweise Shortcuts: Symbole in HIG-Reihenfolge ⌃ Control, ⌥ Option, ⇧ Shift, ⌘ Command (hig:keyboards#Custom-keyboard-shortcuts).

## Inhalt

1. [Plattform-Matrix](#plattform-matrix)
2. [Touch und Gesten](#touch-und-gesten)
3. [Keyboards](#keyboards)
4. [Pointing devices](#pointing-devices)
5. [Digital Crown](#digital-crown)
6. [Apple Pencil und Scribble](#apple-pencil-und-scribble)
7. [Game controls](#game-controls)
8. [Focus and selection](#focus-and-selection)
9. [Action button](#action-button)
10. [Camera Control](#camera-control)
11. [Gyroscope/Accelerometer, Nearby interactions](#gyroscopeaccelerometer-nearby-interactions)
12. [Remotes (tvOS)](#remotes-tvos)
13. [Eyes (visionOS)](#eyes-visionos)
14. [Auffälligkeiten und Unklarheiten](#auffälligkeiten-und-unklarheiten)

---

## Plattform-Matrix

Laut Plattformangabe der jeweiligen Seite („Not supported in …“):

| Eingabe | iOS | iPadOS | macOS | watchOS | tvOS | visionOS | Slug |
|---|---|---|---|---|---|---|---|
| Gestures | ja | ja | ja (Trackpad/Magic Mouse) | ja | ja | ja | gestures |
| Keyboards (physisch) | ja | ja | ja | nein | ja | ja | keyboards |
| Pointing devices | ja | ja | ja | nein | nein | ja | pointing-devices |
| Digital Crown | nein | nein | nein | ja | nein | ja (nur System) | digital-crown |
| Apple Pencil & Scribble | nein | ja | nein | nein | nein | nein | apple-pencil-and-scribble |
| Game controls | ja | ja | ja | nein | ja | ja | game-controls |
| Focus and selection | nein | ja | ja | nein | ja | ja | focus-and-selection |
| Action button | ja | nein | nein | ja | nein | nein | action-button |
| Camera Control | ja | nein | nein | nein | nein | nein | camera-control |
| Gyro/Accelerometer | ja | ja | (gelistet) | ja | Siri Remote | (gelistet) | gyro-and-accelerometer |
| Nearby interactions | ja | ja | nein | ja | nein | nein | nearby-interactions |
| Remotes | – | – | – | – | ja | – | remotes |
| Eyes | – | – | – | – | – | ja | eyes |

Standard-Eingabe je Plattform (aus Spiele-Sicht, hig:designing-for-games#Enable-intuitive-interactions):

| Plattform | Standard | Zusätzlich |
|---|---|---|
| iOS | Touch | Game controller |
| iPadOS | Touch | Game controller, Keyboard, Maus, Trackpad, Apple Pencil |
| macOS | Keyboard, Maus, Trackpad | Game controller |
| tvOS | Remote | Game controller, Keyboard, Maus, Trackpad |
| visionOS | Touch (lt. Tabelle; faktisch Eyes + Hands) | Game controller, Keyboard, Maus, Trackpad, Spatial game controller |
| watchOS | Touch | – |

---

## Touch und Gesten

Zweck: Physische Bewegung, die ein Objekt direkt beeinflusst – auf Touchscreen, in der Luft (visionOS) oder über Trackpad, Maus, Remote, Controller mit Touch-Fläche (hig:gestures).

### Kernregeln

- Biete immer mehr als einen Interaktionsweg (Voice, Keyboard, Switch Control); setze nie voraus, dass jemand eine bestimmte Geste ausführen kann (hig:gestures#Best-practices).
- Nutze vertraute Gesten nur für ihre erwartete Bedeutung; belege Tap/Swipe nicht mit app-eigenen Sonderaktionen und erfinde keine eigene Geste für Standardaktionen wie Button-Aktivierung oder Scrollen (hig:gestures#Best-practices).
- Reagiere sofort und gib während der Geste Feedback, das Ergebnis und nötigen Bewegungsumfang erkennbar macht (hig:gestures#Best-practices).
- Zeige an, wenn eine Geste nicht verfügbar ist (z. B. gesperrtes Objekt, deaktivierter Button klar unterscheidbar) – sonst wirkt die App eingefroren (hig:gestures#Best-practices).
- Custom gestures nur wenn nötig (häufige Spezialaufgaben, Spiele, Zeichen-Apps); sie müssen auffindbar, leicht ausführbar, unterscheidbar und nie der einzige Weg zu einer wichtigen Aktion sein (hig:gestures#Custom-gestures).
- Shortcut-Gesten ergänzen Standard-Steuerung, ersetzen sie nicht – z. B. Edge-Swipe zurück **plus** Back-Button in der Toolbar (hig:gestures#Custom-gestures).
- Kollidiere nicht mit System-Gesten (Edge-Swipe in watchOS, Hand-Roll für System-Overlays in visionOS); Aufschieben der System-Geste nur in Spielen/immersiven Erlebnissen (hig:gestures#Custom-gestures).

### Standard-Gesten (alle Plattformen)

| Geste | Unterstützt in | Übliche Aktion |
|---|---|---|
| Tap | iOS, iPadOS, macOS, tvOS, visionOS, watchOS | Control aktivieren, Element auswählen |
| Swipe | iOS, iPadOS, macOS, tvOS, visionOS, watchOS | Aktionen/Controls einblenden, Views schließen, scrollen |
| Drag | iOS, iPadOS, macOS, tvOS, visionOS, watchOS | UI-Element bewegen |
| Touch (bzw. Pinch) and hold | iOS, iPadOS, tvOS, visionOS, watchOS | Zusätzliche Controls/Funktionen zeigen |
| Double tap | iOS, iPadOS, macOS, tvOS, visionOS, watchOS | Zoom rein/raus; Primäraktion auf Apple Watch Series 9 / Ultra 2 |
| Zoom | iOS, iPadOS, macOS, tvOS, visionOS | View zoomen, Inhalt vergrößern |
| Rotate | iOS, iPadOS, macOS, tvOS, visionOS | Ausgewähltes Element drehen |

(hig:gestures#Standard-gestures)

### Zusätzliche Gesten iOS/iPadOS

| Geste | Aktion |
|---|---|
| Drei-Finger-Swipe | links: Undo, rechts: Redo |
| Drei-Finger-Pinch | zusammen: Text kopieren, auseinander: einfügen |
| Vier-Finger-Swipe (nur iPadOS) | Zwischen Apps wechseln |
| Shake | Undo / Redo |

(hig:gestures#iOS-iPadOS)

- Erlaube gleichzeitige Erkennung mehrerer Gesten nur, wenn es hilft – typisch in Spielen (Joystick + Feuertasten) (hig:gestures#iOS-iPadOS).

### Plattform-Unterschiede

- **macOS:** Primär Keyboard + Maus; Standard-Gesten über Magic Trackpad, Magic Mouse oder Controller mit Touch-Fläche (hig:gestures#macOS). Details siehe [Pointing devices](#pointing-devices).
- **watchOS – Double tap (ab watchOS 11):** scrollt Listen/Scroll-Views, wechselt vertikale Tabs; App, Widget oder Live Activity (im Smart Stack) kann einen Toggle/Button als Primäraktion festlegen; in Notifications wirkt er auf die erste nicht-destruktive Aktion (hig:gestures#watchOS).
  - Setze keine Primäraktion in Views mit Listen, Scroll-Views oder vertikalen Tabs (Konflikt mit Navigation) (hig:gestures#watchOS).
  - Wähle als Primäraktion den meistgenutzten Button einer nicht scrollenden View (z. B. Play/Pause); API `handGestureShortcut(_:isEnabled:)`, `.primaryAction` (hig:gestures#watchOS).
- **tvOS:** Standard-Gesten über Siri Remote/Controller (hig:gestures#tvOS).
- **visionOS (kurz):** indirekte Gesten (hinschauen + Finger-Tap) bevorzugt für UI; direkte Gesten (Berühren) für Objekte in Reichweite und seltene Nutzung; Custom gestures nur im Full Space mit Hand-Tracking-Erlaubnis; Bereich um die Hand für System-Overlays freihalten (hig:gestures#visionOS).

---

## Keyboards

Zweck: Physische Tastatur für Text, Spiele und App-Steuerung; an jedem Gerät außer Apple Watch anschließbar. Mac-Nutzer fast immer, iPad-Nutzer oft (hig:keyboards).

### Kernregeln

- Unterstütze Full Keyboard Access (iOS, iPadOS, macOS, visionOS); teste über Bedienungshilfen in Settings (hig:keyboards#Best-practices).
- iPadOS: Keyboard-Navigation für Text fields, Text views, Sidebars und Collections – **nicht** für Buttons, Segmented controls, Switches; die erreicht man über Full Keyboard Access (hig:keyboards#Best-practices).
- Respektiere Standard-Shortcuts; erstelle für häufige App-Aktionen eigene Shortcuts statt Standard-Shortcuts umzuwidmen (hig:keyboards#Standard-keyboard-shortcuts).
- Umwidmung nur, wenn die Standardaktion in der App sinnlos ist (Beispiel: ⌘I als „Get Info“ in einer App ohne Textbearbeitung) (hig:keyboards#Standard-keyboard-shortcuts).
- Custom Shortcuts nur für die meistgenutzten app-spezifischen Befehle – zu viele machen die App schwer erlernbar (hig:keyboards#Custom-keyboard-shortcuts).
- Modifier erwartungskonform: ⌘ beim Ziehen = Gruppe bewegen; ⇧ beim Resize = Seitenverhältnis halten; gehaltene Pfeiltaste = kleinste App-Einheit verschieben (hig:keyboards#Custom-keyboard-shortcuts).
- Modifier-Reihenfolge in der Anzeige immer: Control, Option, Shift, Command (hig:keyboards#Custom-keyboard-shortcuts).
- Kein ⇧ bei oberem Zeichen einer Doppeltaste – zeige direkt das obere Zeichen (Help = ⌘?, nicht ⇧⌘/) (hig:keyboards#Custom-keyboard-shortcuts).
- Lass das System Shortcuts lokalisieren und bei RTL spiegeln (hig:keyboards#Custom-keyboard-shortcuts).
- Bilde keinen neuen Shortcut, indem du einem bestehenden einen Modifier für einen fremden Befehl hinzufügst (z. B. ⇧⌘Z nur für Redo) (hig:keyboards#Custom-keyboard-shortcuts).
- Zusatz-Modifier nur mit Buchstaben kombinieren; manche Layouts brauchen Modifier für Sonderzeichen (frz. Tastatur: ⌥5 = „{“) (hig:keyboards#Custom-keyboard-shortcuts).

### Modifier-Empfehlung

| Modifier | Symbol | Empfehlung |
|---|---|---|
| Command | ⌘ | Haupt-Modifier für Custom Shortcuts |
| Shift | ⇧ | Sekundär, ergänzt einen verwandten Shortcut |
| Option | ⌥ | Sparsam, für seltene Befehle/Power-Features |
| Control | ⌃ | Vermeiden – systemweit belegt (Fokus, Screenshots) |

(hig:keyboards#Custom-keyboard-shortcuts)

### Standard-Tastaturkurzbefehle (vollständig laut HIG-Tabelle)

Die HIG führt **eine** Tabelle ohne Plattform-Trennung; viele Einträge sind macOS-Systemfunktionen (Dock, Force Quit, Eject). Eine separate iPadOS-Liste existiert im Spiegel nicht (hig:keyboards#Standard-keyboard-shortcuts).

| Taste | Shortcut | Aktion |
|---|---|---|
| Space | ⌘Space | Spotlight-Suchfeld ein-/ausblenden |
| | ⇧⌘Space | variiert |
| | ⌥⌘Space | Spotlight-Ergebnisfenster zeigen |
| | ⌃⌘Space | Fenster „Sonderzeichen“ zeigen |
| Tab | ⇧Tab | Rückwärts durch Controls navigieren |
| | ⌘Tab | Zur nächst-zuletzt benutzten offenen App |
| | ⇧⌘Tab | Rückwärts durch offene Apps (nach Nutzung sortiert) |
| | ⌃Tab | Fokus zur nächsten Control-Gruppe im Dialog bzw. nächsten Tabelle (wenn Tab zur nächsten Zelle springt) |
| | ⌃⇧Tab | Fokus zur vorherigen Control-Gruppe |
| Esc | Esc | Aktuelle Aktion/Prozess abbrechen |
| | ⌥⌘Esc | Dialog „Sofort beenden“ öffnen |
| Eject | ⌃⌘Eject | Alle Apps beenden (nach Sichern) und neu starten |
| | ⌃⌥⌘Eject | Alle Apps beenden (nach Sichern) und ausschalten |
| F1 | ⌃F1 | Full Keyboard Access ein/aus |
| F2 | ⌃F2 | Fokus auf Menüleiste |
| F3 | ⌃F3 | Fokus auf Dock |
| F4 | ⌃F4 | Fokus auf aktives (bzw. nächstes) Fenster |
| | ⌃⇧F4 | Fokus auf zuvor aktives Fenster |
| F5 | ⌃F5 | Fokus auf Toolbar |
| | ⌘F5 | VoiceOver ein/aus |
| F6 | ⌃F6 | Fokus auf erstes (bzw. nächstes) Panel |
| | ⌃⇧F6 | Fokus auf vorheriges Panel |
| F7 | ⌃F7 | Aktuellen Keyboard-Access-Modus in Fenstern/Dialogen temporär übersteuern |
| F8 | – | variiert |
| F9 | – | variiert |
| F10 | – | variiert |
| F11 | – | Schreibtisch zeigen |
| F12 | – | Dashboard ein-/ausblenden |
| ` (Gravis) | ⌘` | Nächstes offenes Fenster der vordersten App aktivieren |
| | ⇧⌘` | Vorheriges offenes Fenster der vordersten App aktivieren |
| | ⌥⌘` | Fokus auf Fenster-Drawer |
| - (Bindestrich) | ⌘- | Auswahl verkleinern |
| | ⌥⌘- | Herauszoomen (bei aktivem Bildschirmzoom) |
| { (linke Klammer) | ⌘{ | Auswahl linksbündig |
| } (rechte Klammer) | ⌘} | Auswahl rechtsbündig |
| \| (Pipe) | ⌘\| | Auswahl zentrieren |
| : (Doppelpunkt) | ⌘: | Fenster „Rechtschreibung“ zeigen |
| ; (Semikolon) | ⌘; | Falsch geschriebene Wörter im Dokument finden |
| , (Komma) | ⌘, | Einstellungsfenster der App öffnen |
| | ⌃⌥⌘, | Bildschirmkontrast verringern |
| . (Punkt) | ⌘. | Vorgang abbrechen |
| | ⌃⌥⌘. | Bildschirmkontrast erhöhen |
| ? (Fragezeichen) | ⌘? | Hilfe-Menü der App öffnen |
| / (Schrägstrich) | ⌥⌘/ | Schriftglättung ein/aus |
| = (Gleich) | ⇧⌘= | Auswahl vergrößern |
| | ⌥⌘= | Hineinzoomen (bei aktivem Bildschirmzoom) |
| 3 | ⇧⌘3 | Bildschirm als Datei sichern |
| | ⌃⇧⌘3 | Bildschirm in Zwischenablage |
| 4 | ⇧⌘4 | Auswahl als Datei sichern |
| | ⌃⇧⌘4 | Auswahl in Zwischenablage |
| 8 | ⌥⌘8 | Bildschirmzoom ein/aus |
| | ⌃⌥⌘8 | Bildschirmfarben invertieren |
| A | ⌘A | Alles auswählen (Dokument/Fenster bzw. alle Zeichen im Textfeld) |
| | ⇧⌘A | Auswahl aufheben |
| B | ⌘B | Fett (umschalten) |
| C | ⌘C | Auswahl kopieren |
| | ⇧⌘C | Fenster „Farben“ zeigen |
| | ⌥⌘C | Stil des ausgewählten Texts kopieren |
| | ⌃⌘C | Formatierung der Auswahl kopieren (Zwischenablage) |
| D | ⌥⌘D | Dock ein-/ausblenden |
| | ⌃⌘D | Definition des gewählten Worts im Lexikon zeigen |
| E | ⌘E | Auswahl für Suche verwenden |
| F | ⌘F | Suchfenster öffnen |
| | ⌥⌘F | Zum Suchfeld springen |
| | ⌃⌘F | Vollbild aktivieren |
| G | ⌘G | Nächstes Vorkommen finden |
| | ⇧⌘G | Vorheriges Vorkommen finden |
| H | ⌘H | Fenster der aktuellen App ausblenden |
| | ⌥⌘H | Fenster aller anderen Apps ausblenden |
| I | ⌘I | Kursiv (umschalten) |
| | ⌘I | Info-Fenster zeigen (doppelt belegt, s. Auffälligkeiten) |
| | ⌥⌘I | Inspector-Fenster zeigen |
| J | ⌘J | Zur Auswahl scrollen |
| M | ⌘M | Aktives Fenster ins Dock minimieren |
| | ⌥⌘M | Alle Fenster der aktiven App minimieren |
| N | ⌘N | Neues Dokument |
| O | ⌘O | Öffnen-Dialog |
| P | ⌘P | Drucken-Dialog |
| | ⇧⌘P | Dialog „Papierformat“ |
| Q | ⌘Q | App beenden |
| | ⇧⌘Q | Benutzer abmelden |
| | ⌥⇧⌘Q | Benutzer ohne Bestätigung abmelden |
| S | ⌘S | Sichern (neues Dokument bzw. Version) |
| | ⇧⌘S | Duplizieren bzw. „Sichern unter“ |
| T | ⌘T | Fenster „Schriften“ zeigen |
| | ⌥⌘T | Toolbar ein-/ausblenden |
| U | ⌘U | Unterstreichen (umschalten) |
| V | ⌘V | Einfügen an Einfügemarke |
| | ⇧⌘V | Einfügen als … (z. B. als Zitat) |
| | ⌥⌘V | Stil eines Objekts auf Auswahl anwenden |
| | ⌥⇧⌘V | Einfügen und Stil des umgebenden Texts übernehmen |
| | ⌃⌘V | Formatierung auf Auswahl anwenden |
| W | ⌘W | Aktives Fenster schließen |
| | ⇧⌘W | Datei samt zugehöriger Fenster schließen |
| | ⌥⌘W | Alle Fenster der App schließen |
| X | ⌘X | Ausschneiden |
| Z | ⌘Z | Undo |
| | ⇧⌘Z | Redo (wenn Undo/Redo getrennte Befehle sind) |
| → | ⌘→ | Tastaturlayout auf aktuelles Layout der lateinischen Schrift |
| | ⇧⌘→ | Auswahl bis zur nächsten semantischen Einheit (meist Zeilenende) erweitern |
| | ⇧→ | Auswahl um ein Zeichen nach rechts |
| | ⌥⇧→ | Auswahl bis Wortende, dann Ende des nächsten Worts |
| | ⌃→ | Fokus auf anderen Wert/Zelle in View (z. B. Tabelle) |
| ← | ⌘← | Tastaturlayout auf aktuelles Layout der Systemschrift |
| | ⇧⌘← | Auswahl bis zur vorherigen semantischen Einheit (meist Zeilenanfang) |
| | ⇧← | Auswahl um ein Zeichen nach links |
| | ⌥⇧← | Auswahl bis Wortanfang, dann Anfang des vorherigen Worts |
| | ⌃← | Fokus auf anderen Wert/Zelle in View |
| ↑ | ⇧⌘↑ | Auswahl nach oben bis zur nächsten semantischen Einheit (meist Dokumentanfang) |
| | ⇧↑ | Auswahl zur Zeile darüber (gleiche horizontale Position) |
| | ⌥⇧↑ | Auswahl bis Absatzanfang, dann Anfang des nächsten Absatzes |
| | ⌃↑ | Fokus auf anderen Wert/Zelle in View |
| ↓ | ⇧⌘↓ | Auswahl nach unten bis zur nächsten semantischen Einheit (meist Dokumentende) |
| | ⇧↓ | Auswahl zur Zeile darunter (gleiche horizontale Position) |
| | ⌥⇧↓ | Auswahl bis Absatzende, dann Ende des nächsten Absatzes (inkl. Absatzende-Zeichen bei Cut/Copy/Paste) |
| | ⌃↓ | Fokus auf anderen Wert/Zelle in View |

Shortcuts für Eingabequellen (nicht an Menübefehle gebunden):

| Shortcut | Aktion |
|---|---|
| ⌃Space | Zwischen aktueller und letzter Eingabequelle wechseln |
| ⌃⌥Space | Nächste Eingabequelle der Liste |
| [Modifier]⌘Space | variiert |
| ⌘→ | Layout der lateinischen Schrift |
| ⌘← | Layout der Systemschrift |

(hig:keyboards#Standard-keyboard-shortcuts)

### Plattform-Unterschiede

- **iOS, iPadOS, macOS, tvOS:** keine Zusatzhinweise; watchOS nicht unterstützt (hig:keyboards#Platform-considerations).
- **iPadOS/macOS Menüs:** Shortcuts erscheinen in Menüleisten-Menüs (siehe hig:the-menu-bar).
- **visionOS (kurz):** Halten von ⌘ zeigt eine Shortcut-Übersicht nach Menükategorien (File, Edit, View …) als flache Liste – Shortcut-Titel müssen ohne Untermenü-Kontext verständlich sein (`discoverabilityTitle`); bei physischer Tastatur blendet das System ein virtuelles Overlay mit Vervollständigung ein (hig:keyboards#visionOS).
- **Spiele:** Key bindings, Single-Key-Befehle, frei belegbar – siehe [Game controls](#game-controls) (hig:game-controls#Keyboards).

---

## Pointing devices

Zweck: Trackpad/Maus für präzise Navigation. Auf dem Mac Standard zusammen mit Keyboard; auf iPad und Vision Pro zusätzlicher Weg, ersetzt Touch/Eyes/Gesten nicht (hig:pointing-devices).

### Kernregeln

- Reagiere konsistent auf Maus-/Trackpad-Gesten (z. B. „Swipe between pages“ überall gleich) (hig:pointing-devices#Best-practices).
- Definiere systemweite Trackpad-Gesten nicht um (Dock, Mission Control); Nutzer können sie anpassen (hig:pointing-devices#Best-practices).
- Gleiches Verhalten über Gesten, Eyes, Pointer, Keyboard hinweg (hig:pointing-devices#Best-practices).
- Lass Pointer automatisch minimierte Controls einblenden (Safari-Toolbar auf iPad, Video-Controls im Vollbild) (hig:pointing-devices#Best-practices).
- Modifier-Verhalten (z. B. ⌥ beim Ziehen = duplizieren) muss bei Touch und Pointer gleich wirken (hig:pointing-devices#Best-practices).

### iPadOS

- Mehrfachauswahl per Rahmenziehen (ab iPadOS 15) in Custom Views selbst implementieren (`UIBandSelectionInteraction`); Standard-Collection-Views (nicht Listen) können es (hig:pointing-devices#iPadOS).
- Unterscheide Pointer und Finger nur bei echtem Mehrwert (z. B. präziser Klick auf Scrubber-Position) (hig:pointing-devices#iPadOS).
- Pointer standardmäßig Kreis; I-Beam über Texteingabe (hig:pointing-devices#Pointer-shape-and-content-effects).
- Content effects:

| Effekt | Wirkung | Einsatz | System-Standard für |
|---|---|---|---|
| Highlight | Pointer wird transluzentes Rounded Rect hinter dem Control, leichte Parallaxe | kleines Element, transparenter Hintergrund | Bar buttons, Tab bars, Segmented controls, Edit menus |
| Lift | Element skaliert hoch, Schatten + Glanz, wirkt schwebend | kleines Element, opaker Hintergrund | App-Icons, Control-Center-Buttons |
| Hover | Eigene Werte für Scale, Tint, Shadow; Pointer-Form bleibt | große Elemente | – |

(hig:pointing-devices#Standard-pointers-and-effects)

- Pointer magnetism: automatisch bei Lift/Highlight und Texteingabe, nicht bei Hover (hig:pointing-devices#Pointer-magnetism).
- Hit regions: ca. **12 pt** Padding um Elemente mit Bezel, ca. **24 pt** um Elemente ohne Bezel (hig:pointing-devices#Standard-pointers-and-effects).
- Lückenlose Hit regions bei Custom bar buttons (sonst springt der Pointer zur Grundform) (hig:pointing-devices#Standard-pointers-and-effects).
- Bei Lift auf nicht standardmäßigen Formen Corner radius angeben (`UIPointerShape.roundedRect(_:radius:)`) (hig:pointing-devices#Standard-pointers-and-effects).
- Custom pointer: systemische Effekte für standardähnliche Elemente, konsistent, keine dekorativen Effekte, einfache Formen, nützliche Annotationen (z. B. X/Y-Werte) ja, Anleitungstexte am Pointer nein (hig:pointing-devices#Customizing-pointers).
- Scale nur, wo Platz ist (nicht bei Table rows); Schatten nie ohne Scale (hig:pointing-devices#Customizing-pointers).
- Pointer accessories (`UIPointerAccessory`): einfache Bilder; Zustandswechsel per Accessory-Transition (z. B. `plus` → `circle.slash`) (hig:pointing-devices#Pointer-accessories).

### macOS – Klicks und Gesten

| Klick/Geste | Erwartetes Verhalten | Maus | Trackpad |
|---|---|---|---|
| Primary click | Auswählen/aktivieren | ja | ja |
| Secondary click | Kontextmenü | ja | ja |
| Scrolling | Inhalt verschieben | ja | ja |
| Smart zoom | Zoom auf Inhalt (Web, PDF) | ja | ja |
| Swipe between pages | Seitenweise vor/zurück | ja | ja |
| Swipe between full-screen apps | Zwischen Vollbild-Apps/Spaces | ja | ja |
| Mission Control (Maus: Zwei-Finger-Doppeltipp; Trackpad: 3/4 Finger nach oben) | Mission Control | ja | ja |
| Lookup/Data detectors (Force click 1 Finger oder Tipp 3 Finger) | Lookup-Fenster | – | ja |
| Tap to click | Tippen statt Klicken | – | ja |
| Force click | Quick Look/Lookup; druckabhängige Controls | – | ja |
| Pinch (2 Finger) | Zoom | – | ja |
| Rotate (2 Finger kreisend) | Drehen | – | ja |
| Notification Center (Swipe vom Trackpad-Rand) | Mitteilungszentrale | – | ja |
| App Exposé (3/4 Finger nach unten) | Fenster der App in Exposé | – | ja |
| Launchpad (Pinch Daumen + 3 Finger) | Launchpad | – | ja |
| Show Desktop (Spread Daumen + 3 Finger) | Schreibtisch freilegen | – | ja |

(hig:pointing-devices#macOS)

### macOS – Standard-Pointer (`NSCursor`)

| Pointer | Bedeutung | API |
|---|---|---|
| Arrow | Standard | `arrow` |
| Closed hand | Inhalt in View wird verschoben (z. B. Karte) | `closedHand` |
| Open hand | Verschieben möglich | `openHand` |
| Contextual menu | Kontextmenü verfügbar (meist nur bei gedrücktem ⌃) | `contextualMenu` |
| Crosshair | Präzise Rechteckauswahl | `crosshair` |
| Disappearing item | Gezogenes Element verschwindet beim Ablegen (Original bleibt) | `disappearingItem` |
| Drag copy | Kopieren statt Bewegen (⌥ beim Ziehen) | `dragCopy` |
| Drag link | Alias erzeugen (⌥⌘ beim Ziehen) | `dragLink` |
| Horizontal I-beam | Textauswahl horizontal | `iBeam` |
| Vertical I-beam | Textauswahl vertikal | `iBeamCursorForVerticalLayout` |
| Operation not allowed | Ablegen hier nicht möglich | `operationNotAllowed` |
| Pointing hand | Link | `pointingHand` |
| Resize up/down/left/right, left/right, up/down | Größe/Position ändern in Richtung | `resizeUp`, `resizeDown`, `resizeLeft`, `resizeRight`, `resizeLeftRight`, `resizeUpDown` |

(hig:pointing-devices#Pointers)

- **visionOS (kurz):** Blickziel bestimmt Pointer-Kontext; Pointer verschwindet während Trackpad-Gesten (hig:pointing-devices#visionOS). iOS: keine Zusatzhinweise; tvOS/watchOS nicht unterstützt.

---

## Digital Crown

Zweck: Hardware-Eingabe auf Apple Watch (System + Apps) und Vision Pro (nur System) (hig:digital-crown).

### Apple Watch

- Ab watchOS 10 primäre Navigationseingabe: Smart Stack auf dem Watch Face, Home Screen, vertikal paginierte Tabs, Listen, Seiten variabler Höhe (hig:digital-crown#Apple-Watch).
- Apps erhalten **keine** Crown-Drücke – reserviert fürs System (Home Screen) (hig:digital-crown#Apple-Watch).
- Verankere die App-Navigation an der Crown (vertikale List/Tab/Scroll-Views) und biete parallel Touch-Äquivalente (hig:digital-crown#Apple-Watch).
- Nutze die Crown zum Inspizieren von Daten, wo keine Navigation nötig ist (Beispiel World Clock: Tageszeit vorspulen) (hig:digital-crown#Apple-Watch).
- Gib sichtbares Feedback auf jede Drehung; sonst wirkt die Crown funktionslos (hig:digital-crown#Apple-Watch).
- Koppel Änderungsgeschwindigkeit an die Drehgeschwindigkeit; Werte müssen gezielt wählbar bleiben (hig:digital-crown#Apple-Watch).
- Nutze Standard-Haptik (lineare Detents); abschalten, wenn sie nicht zur Animation passt; Tabellen mit stark unterschiedlichen Zeilenhöhen ggf. lineare statt zeilenbasierte Detents (hig:digital-crown#Apple-Watch).

### Vision Pro (kurz)

Lautstärke, Immersionsgrad (Portal, Environment, Full Space), Recenter, Bedienungshilfen, App verlassen. Apps erhalten keine direkten Crown-Informationen (hig:digital-crown#Apple-Vision-Pro).

---

## Apple Pencil und Scribble

Zweck: Präzises Zeichnen, Schreiben, Markieren auf iPad; Scribble = Handschrift in jedem Textfeld, on-device erkannt. Nur iPadOS (hig:apple-pencil-and-scribble).

### Kernregeln

- Unterstütze, was Menschen von echten Stiften erwarten (z. B. in Ränder schreiben) (hig:apple-pencil-and-scribble#Best-practices).
- Alle Controls müssen auch auf Pencil reagieren – kein Wechsel zum Finger erzwingen (hig:apple-pencil-and-scribble#Best-practices).
- Markieren sofort beim Aufsetzen, ohne Modus/Button vorher (hig:apple-pencil-and-scribble#Best-practices).
- Nutze Tilt (Altitude), Force, Azimuth, Barrel roll für Strichcharakter; Druck für kontinuierliche Eigenschaften (Deckkraft, Pinselgröße) (hig:apple-pencil-and-scribble#Best-practices).
- Direkte Verbindung zum Inhalt; keine entfernten Effekte auslösen (hig:apple-pencil-and-scribble#Best-practices).
- Links- und Rechtshänder: keine verdeckbaren Controls bzw. verschiebbar machen (hig:apple-pencil-and-scribble#Best-practices).

### Interaktionen

| Interaktion | Regeln |
|---|---|
| Hover | Vorschau der kommenden Markierung; nicht mit Höhe variieren; keine Aktionen auslösen; Vorschau mit mittlerem Wert dynamischer Bereiche; Hover-Vorschau nur für Pencil, nicht für Pointer (hig:apple-pencil-and-scribble#Hover) |
| Double tap | Nutzer-Einstellung respektieren (Standard: Werkzeug ↔ Radierer; Alternativen: vorheriges Werkzeug, Farbwähler, nichts); Custom-Verhalten nur optional und nicht Default; keine inhaltsverändernden/destruktiven Aktionen (hig:apple-pencil-and-scribble#Double-tap) |
| Squeeze (Pencil Pro) | Einzelne, diskrete Aktion; Ergebnis nahe der Stiftspitze; nicht-destruktiv, rückgängig machbar; Nutzer können Squeeze auf ein App Shortcut legen; nur bei eingeschaltetem Display und ohne Kontakt (hig:apple-pencil-and-scribble#Squeeze) |
| Barrel roll (Pencil Pro) | Nur Markierverhalten ändern (z. B. Strichwinkel), nie Navigation/Controls (hig:apple-pencil-and-scribble#Barrel-roll) |

### Scribble

- Funktioniert standardmäßig in allen Standard-Textkomponenten außer Passwortfeldern; Custom Fields nicht erst antippen lassen (hig:apple-pencil-and-scribble#Scribble).
- Scribble überall anbieten, wo Text naheliegt, auch ohne sichtbares Feld (`UIIndirectScribbleInteraction`, Beispiel Reminders) (hig:apple-pencil-and-scribble#Scribble).
- Während des Schreibens: keine Autovervollständigung einblenden, Platzhalter sofort ausblenden, Feld nicht bewegen/skalieren, kein Autoscroll (hig:apple-pencil-and-scribble#Scribble).
- Genug Schreibfläche: Feld vor Beginn oder in Pausen vergrößern (`UIScribbleInteraction`) (hig:apple-pencil-and-scribble#Scribble).

### Custom drawing (PencilKit)

- Beim Zeichnen auf PDF/Foto dynamische Dark-Mode-Farbanpassung abschalten (hig:apple-pencil-and-scribble#Custom-drawing).
- In compact environments eigene Undo/Redo-Buttons (Tool picker hat dort keine); Drei-Finger-Undo unterstützen (hig:apple-pencil-and-scribble#Custom-drawing).

---

## Game controls

Zweck: Präzise Spielsteuerung über Touch, physische Controller, Keyboard (hig:game-controls).

### Touch controls (iOS/iPadOS, Framework `TouchController`)

- Virtuelle Controls nur, wenn sinnvoll; wo möglich direkte Interaktion mit Spielobjekten (hig:game-controls#Touch-controls).
- Platzierung: Safe areas beachten, nicht über Home indicator/Dynamic Island; häufige Buttons am Daumen, sekundäre (Menüs) oben (hig:game-controls#Touch-controls).
- Mindestgrößen: häufige Controls **44x44 pt**, weniger wichtige (Menüs) **28x28 pt** (hig:game-controls#Touch-controls).
- Sichtbarer (auch unter dem Finger, z. B. Glow) und taktiler Press-State plus Sound/Haptik (hig:game-controls#Touch-controls).
- Symbole, die die Aktion zeigen – keine Controller-Namen wie A, X, R1 (hig:game-controls#Touch-controls).
- Controls kontextabhängig ein-/ausblenden; Aktionen zusammenlegen (Double tap, Touch and hold für Varianten) (hig:game-controls#Touch-controls).
- Bewegung links, Kamera rechts; Thumbstick dort erscheinen lassen, wo der Daumen landet; Kamera per direktem Pan statt Thumbstick (hig:game-controls#Touch-controls).

### Physische Controller

- Immer Fallback auf die Standard-Eingabe der Plattform (hig:game-controls#Physical-controllers).
- tvOS/visionOS dürfen Controller voraussetzen (App-Store-Badge „Game Controller Required“, `GCRequiresControllerUserInteraction`); fehlenden Controller erkennen und freundlich zum Verbinden auffordern (hig:game-controls#Physical-controllers).
- Controller automatisch erkennen; Beschriftung/Glyphen des tatsächlich verbundenen Controllers zeigen (`GCControllerElement`); bei mehreren Controllern den aktiven verwenden (hig:game-controls#Physical-controllers).
- SF Symbols statt Text für Controller-Elemente (hig:game-controls#Physical-controllers).

UI-Mapping außerhalb des Gameplays (alle Apple-Plattformen):

| Button | Verhalten in UI |
|---|---|
| A | Control aktivieren |
| B | Abbrechen / zurück |
| X, Y | – |
| Left/Right shoulder | Zu anderem Screen/Abschnitt links/rechts |
| Left/Right trigger | – |
| Thumbsticks, D-Pad | Auswahl bewegen |
| Home/Logo | System reserviert |
| Menu | Spieleinstellungen / Pause |

(hig:game-controls#Physical-controllers)

### Keyboard (Spiele)

- Single-Key-Befehle bevorzugen (I = Inventory, M = Map, Space = Hauptaktion) (hig:game-controls#Keyboards).
- Auf Apple-Tastatur testen (⌃ ggf. auf ⌘ legen, liegt neben Space) (hig:game-controls#Keyboards).
- Nähe zu WASD und Gruppierung verwandter Aktionen (Zahlentasten) beachten; Key bindings frei belegbar machen (hig:game-controls#Keyboards).

- **visionOS (kurz):** Spatial game controller (z. B. PlayStation VR2 Sense) wie Hände behandeln: Blick + Trigger = indirekt, hingreifen + Trigger = direkt (hig:game-controls#visionOS). watchOS: keine Controller.

---

## Focus and selection

Zweck: Fokus zeigt, worauf eine Interaktion zielt; Navigation per Keyboard, Remote, Controller. Fokus wählt oft auch aus, außer wenn das einen störenden Kontextwechsel auslösen würde (hig:focus-and-selection).

### Kernregeln

- Nutze systemseitige Fokuseffekte; Custom nur wenn zwingend (hig:focus-and-selection#Best-practices).
- Ändere Fokus nicht ohne Nutzeraktion. Ausnahme: diskrete Richtungs-Eingabe und das fokussierte Element verschwindet → zu benachbartem Element; sonst Fokusindikator ausblenden (hig:focus-and-selection#Best-practices).
- iPadOS/macOS: Fokus nur für Content-Elemente (Listeneinträge, Text-/Suchfelder), nicht für Buttons, Slider, Toggles (das deckt Full Keyboard Access ab). tvOS: jedes Element fokussierbar (hig:focus-and-selection#Best-practices).
- Focus ring für Text-/Suchfelder, Highlight für Listen/Collections; fokussierte Listeneinträge: weißer Text + Akzentfarb-Hintergrund, unfokussiert grau (hig:focus-and-selection#Best-practices).

### Plattform-Unterschiede

- **iPadOS (ab 15):** Focus groups. Tab springt zwischen Gruppen (Sidebar, Grid, Liste), Pfeiltasten innerhalb einer Gruppe; Reihenfolge leading→trailing, oben→unten. Halo (Focus ring) anpassbar (`UIFocusHaloEffect`); Gruppen via `focusGroupIdentifier`, Primär-Element via `UIFocusGroupPriority`. Highlight (Akzentfarb-Text) ist kein Fokuseffekt (hig:focus-and-selection#iPadOS).
- **macOS:** Focus ring / Highlight wie oben; Full Keyboard Access deckt Controls ab (hig:focus-and-selection#Best-practices).
- **tvOS (kurz):** Directional focus, Parallax; bis zu fünf Zustände (unfocused, focused, highlighted, selected, unavailable); Assets in vergrößerter Fokusgröße liefern; kein Pointer; im Vollbild Gesten auf Inhalt, nicht auf Fokus (hig:focus-and-selection#tvOS).
- **visionOS (kurz):** Gleiches Fokus-System für externe Eingabegeräte; Blick-Hervorhebung ist der Hover effect, kein Fokus (hig:focus-and-selection#visionOS).
- iOS, watchOS: nicht unterstützt.

---

## Action button

Zweck: Hardware-Taste auf unterstützten iPhone- und Apple-Watch-Modellen für App Shortcuts oder Systemfunktionen; auf Apple Watch Ultra zusätzlich Workout/Dive (hig:action-button).

### Kernregeln

- Biete eine Auswahl essenzieller Funktionen als App Shortcuts an; kein Shortcut nur zum Öffnen der App (macht das System) (hig:action-button#Best-practices).
- Labels (sichtbar in Settings): Title-Case, Verb am Anfang, Präsens, ohne Artikel/Präpositionen, **maximal drei Wörter** („Start Race“) (hig:action-button#Best-practices).
- Keine eigene Anleitung, die die System-Hilfe in Settings wiederholt (hig:action-button#Best-practices).

### Plattform-Unterschiede

- **iOS:** Aktion ohne Kontextverlust ausführen – Live Activities und Snippets statt App-Start (Beispiel „Set Timer“) (hig:action-button#iOS).
- **watchOS:** Erster Druck z. B. Wegpunkt, Tauchgang, Workout; Folgedrücke als logische Sekundärfunktion (Segment markieren, nächste Disziplin) – meist nur eine; Folgedrücke erweitern statt beenden (Stoppen in der UI); Action + Side button gemeinsam = Pause (Ausnahme Tauchen) (hig:action-button#watchOS).
- iPadOS, macOS, tvOS, visionOS: nicht unterstützt.

---

## Camera Control

Zweck: Hardware-Control auf iPhone 16 / iPhone 16 Pro (Stand der Seite), öffnet das Kamera-Erlebnis der App; leichter Druck zeigt Overlay, leichter Doppeldruck zeigt verfügbare Controls, Wischen stellt Werte ein (hig:camera-control).

- Control-Typen: **Slider** (Wertebereich) und **Picker** (diskrete Optionen); System-Controls für Zoom und Belichtung optional einbindbar (hig:camera-control#Anatomy).
- Nur SF Symbols (keine Custom symbols); Symbole zeigen Funktion, nicht Zustand (hig:camera-control#Best-practices).
- Kurze Control-Namen (Dynamic Type, verdecken sonst den Sucher) (hig:camera-control#Best-practices).
- Einheiten an Slider-Werten (EV, %, eigener String; `localizedValueFormat`) und Prominent values definieren (`prominentValues`) (hig:camera-control#Best-practices).
- UI außerhalb der Overlay-Zone (Hoch- und Querformat); keine doppelten Controls in UI und Overlay (hig:camera-control#Best-practices).
- Controls je Kameramodus aktivieren/deaktivieren – zur Laufzeit nicht hinzufügen/entfernen (hig:camera-control#Best-practices).
- Häufige Controls in die Mitte, seltene an die Ränder; System merkt sich zuletzt benutztes Control (hig:camera-control#Best-practices).
- Locked camera capture extension anbieten (Start vom Sperrbildschirm, Home Screen, anderen Apps) (hig:camera-control#Best-practices, hig:controls#Camera-experiences-on-a-locked-device).
- Nur iOS.

---

## Gyroscope/Accelerometer, Nearby interactions

**Gyroscope und Accelerometer** (Core Motion; iOS, iPadOS, watchOS; tvOS über Siri Remote) (hig:gyro-and-accelerometer):
- Bewegungsdaten nur mit konkretem Nutzen erheben (hig:gyro-and-accelerometer#Best-practices).
- Zugriff erfordert Begründungstext im Permission-Dialog (hig:gyro-and-accelerometer#Best-practices).
- Außerhalb aktiven Gameplays keine direkte UI-Manipulation per Bewegung (schwer reproduzierbar, körperlich fordernd, Akku) (hig:gyro-and-accelerometer#Best-practices).

**Nearby interactions** (Ultra Wideband, Framework `NearbyInteraction`; iOS, iPadOS, watchOS) (hig:nearby-interactions):
- Aufgabe aus Sicht der physischen Welt denken (z. B. Audio-Übergabe an HomePod mini durch Annähern) (hig:nearby-interactions#Best-practices).
- Distanz, Richtung, Kontext nutzen; Feedback mit Nähe verändern; kontinuierliches Feedback; visuell, akustisch, haptisch kombinieren (hig:nearby-interactions#Best-practices).
- Nie einziger Weg zu einer Aufgabe (hig:nearby-interactions#Best-practices).
- Hochformat fördern (implizit, nicht per Anweisung); Sensor-Sichtfeld wie Ultra-Wide-Kamera (iPhone 11 und neuer) – außerhalb nur Distanz, keine Richtung; Hindernisse in Onboarding erklären (hig:nearby-interactions#Device-usage).
- iOS: Distanz und Richtung; watchOS: nur Distanz, App muss im Vordergrund sein (hig:nearby-interactions#Platform-considerations).

---

## Remotes (tvOS)

Nur der Vollständigkeit halber (außerhalb des Fokus): Standard-Gesten für Standard-Aktionen; Gesten mit Fokusrichtung koppeln; Press (bewusst) vs. Tap (navigieren) unterscheiden, bei Live-Video keine Taps auswerten; Back öffnet den Parent (im Spiel: Pause-Menü); Play/Pause steuert Wiedergabe; EPG-Tasten erwartungskonform (hig:remotes).

| Taste/Bereich | App | Spiel |
|---|---|---|
| Touch surface (Swipe) | Navigieren, Fokus ändern | D-Pad |
| Touch surface (Press) | Aktivieren, tiefer navigieren | Primärtaste |
| Back | Zurück / Apple TV Home | Pause/Fortsetzen, zurück, Hauptmenü, Home |
| Play/Pause | Wiedergabe starten/pausieren | Sekundärtaste, Intro überspringen |

(hig:remotes#Buttons)

---

## Eyes (visionOS)

Kurzfassung: Blick wählt Ziel, System zeigt Hover effect; App erfährt aus Datenschutzgründen nicht, wohin geschaut wird – nur den Tap (hig:eyes).

- Mehrere Interaktionswege anbieten (Accessibility) (hig:eyes#Best-practices).
- Inhalte im Sichtfeld; Lesestoff mindestens **1 m** entfernt platzieren (hig:eyes#Best-practices).
- Abstand zwischen interaktiven Elementen: mind. **16 pt** Rand um jedes Element oder Mittelpunkte mind. **60 pt** auseinander (hig:eyes#Making-items-easy-to-see).
- Runde Formen bevorzugen; zusammengesetzte Komponenten mit gemeinsamer Hover-Region; keine flächenfüllenden Wiederholmuster; Bewegung nahe dem Blickziel vermeiden (hig:eyes#Making-items-easy-to-see, hig:eyes#Encouraging-interaction).
- Custom hover effects laufen außerhalb des App-Prozesses (kein Code bei Blick); sparsam einsetzen; Delay: keiner (subtil), kurz (Tab-Bar-Expansion), lang (Tooltip); eine Primär-View stabil halten (hig:eyes#Custom-hover-effects).

---

## Auffälligkeiten und Unklarheiten

- **Shortcut-Tabelle ohne Plattformzuordnung:** hig:keyboards enthält nur eine gemeinsame Tabelle, die überwiegend macOS-Systemfunktionen beschreibt; eine eigene iPadOS-Shortcut-Liste gibt es im Spiegel nicht. Für iPadOS sind daher nur die app-bezogenen Einträge (⌘C/V/X/Z, ⌘N, ⌘F, ⌘W, ⌘, …) sinnvoll übertragbar – das ist eine Ableitung, keine HIG-Aussage.
- **⌘I doppelt belegt** (Kursiv und Info-Fenster) – so in der HIG-Tabelle; die Seite nennt ⌘I als Beispiel für zulässige Umwidmung, wenn keine Textbearbeitung existiert.
- **F12 „Dashboard“**: Die Tabelle nennt noch Dashboard, das es in aktuellen macOS-Versionen nicht mehr gibt – Tabelle wirkt in Teilen veraltet; ebenso „window drawer“ (⌥⌘`).
- **⌘←/⌘→** sind in der Tabelle nur als Tastaturlayout-Wechsel geführt; Cursor-Sprung an Zeilenanfang/-ende fehlt. Navigations-Shortcuts ohne ⇧ (⌥←, ⌘↑ usw.) sind generell nicht aufgeführt.
- Tippfehler in der Quelle: „Control- F3“ (Leerzeichen) – hier normalisiert zu ⌃F3.
- **Camera Control** nennt nur iPhone 16 / 16 Pro; ob spätere Modelle gemeint sind, sagt die Seite nicht (Update-Stand 2024-09-09).
- **watchOS-Double-tap**: hig:gestures nennt Apple Watch Series 9 und Ultra 2 in der Gesten-Tabelle, im Fließtext „watchOS 11 and later“ ohne Modellliste.
- **Standard-Eingabe visionOS = „Touch“** in hig:designing-for-games widerspricht der sonstigen Darstellung (Eyes + indirekte Gesten, hig:designing-for-visionos); watchOS = „Touch“ ignoriert die Digital Crown als primäre Navigationseingabe (hig:digital-crown).
- **Gyroscope-Seite** listet macOS und visionOS als Plattform, der Text nennt aber nur iOS, iPadOS, watchOS und tvOS (Siri Remote).
- hig:designing-for-ios verlinkt noch auf den alten Slug `spatial-interactions` (heute `nearby-interactions`, umbenannt 2023-06-21).
