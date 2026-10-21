# Motion, Haptics und Feedback

Quellen (HIG-Spiegel, Stand 2026-10-21): `motion` (Update 2025-09-09, Liquid Glass), `playing-haptics` (2024-05-07, Apple Pencil Pro), `feedback`, `loading` (2025-06-09), `launching` (2024-06-10), `progress-indicators`, `accessibility#Cognitive` (Reduce Motion), `sf-symbols#Animations`, `digital-crown`, `alerts`.

## Einordnung

Bewegung, Haptik, Ton und Statusanzeigen sind ein gemeinsames Feedback-System: Sie zeigen Status, bestätigen Ergebnisse, warnen vor Folgen und helfen beim Korrigieren (hig:feedback). Grundsatz: **Gewicht der Rückmeldung = Gewicht der Information** – Status passiv und nah am Objekt, drohender Datenverlust unterbrechend (hig:feedback). Systemkomponenten bringen Bewegung und Haptik bereits mit und passen sie an Eingabemethode und Accessibility-Einstellungen an (z. B. reagiert Liquid Glass auf direkte Berührung stärker als auf Trackpad) (hig:motion). Eigene Motion nur ergänzend.

**Wichtig:** Die HIG nennt **keine Dauer- oder Kurvenwerte** (ms, Spring-Parameter) für App-Animationen. Einzige Zahlen im Spiegel: 30–60 fps für Spiele (hig:motion#Leveraging-platform-capabilities) und ~0,2 Hz als zu vermeidende Oszillationsfrequenz in visionOS (hig:motion#visionOS). Keine Millisekunden-Vorgaben erfinden – Systemanimationen/Default-Springs verwenden.

## Kernregeln

### Motion
- Setze Bewegung zweckgebunden ein; keine Animation um ihrer selbst willen – übermäßige Animation lenkt ab und kann körperliches Unbehagen auslösen (hig:motion#Best-practices).
- Mache Motion optional: Wichtige Information nie nur über Bewegung, zusätzlich Haptik und Audio (hig:motion#Best-practices).
- Feedback-Bewegung folgt Geste und Erwartung (was von oben hereingleitet, geht nicht seitlich hinaus) (hig:motion#Providing-feedback).
- Halte Feedback-Animationen kurz und präzise (hig:motion#Providing-feedback).
- Füge häufigen UI-Interaktionen in Apps keine zusätzliche Motion hinzu; das System animiert Standardelemente bereits (hig:motion#Providing-feedback).
- Lass Bewegung abbrechbar sein; niemand soll auf das Ende einer Animation warten müssen, besonders bei Wiederholung (hig:motion#Providing-feedback).
- Nutze animierte SF Symbols, wo sie Information effizient transportieren (ab SF Symbols 5) (hig:motion#Providing-feedback, hig:sf-symbols#Animations).
- Spiele: konstante 30–60 fps als Ziel, sinnvolle Default-Grafikeinstellungen je Gerät, Performance-/Akkumodi wählbar (hig:motion#Leveraging-platform-capabilities).

### Reduce Motion (hig:accessibility#Cognitive)
- Reduziere bei aktivem Reduce Motion automatische und repetitive Animationen, insbesondere Zoom, Skalierung, periphere Bewegung.
- Straffe Springs (weniger Nachfedern).
- Koppele Animationen direkt an die Geste.
- Animiere keine Tiefenänderungen in z-Ebenen.
- Ersetze x-/y-/z-Übergänge durch Fades.
- Animiere nicht in/aus Blur.
- Sei vorsichtig mit schnellen und blinkenden Animationen (Schwindel, im Extremfall epileptische Anfälle) – unabhängig von Reduce Motion.

### Haptics
- Nutze System-Haptics nur in ihrer dokumentierten Bedeutung; passt keine, nimm ein generisches oder eigenes Muster (hig:playing-haptics#Best-practices).
- Verwende Haptics konsistent und kausal: gleiches Muster = gleiche Art Ereignis (nie dasselbe Muster für Erfolg und Misserfolg) (hig:playing-haptics#Best-practices).
- Setze Haptics ergänzend zu Bild und Ton ein; Intensität und Schärfe an die begleitende Animation anpassen (hig:playing-haptics#Best-practices).
- Übertreibe nicht – die beste Haptik fällt kaum auf, fehlt aber, wenn sie aus ist (hig:playing-haptics#Best-practices).
- Bevorzuge in Apps kurze Haptics für diskrete Ereignisse; lange/kontinuierliche eher in Spielen (auf Apple Pencil Pro besonders zurückhaltend) (hig:playing-haptics#Best-practices).
- Mache Haptics abschaltbar; die App muss ohne sie voll nutzbar sein (hig:playing-haptics#Best-practices).
- Prüfe Wechselwirkungen mit Kamera, Gyroskop, Mikrofon (hig:playing-haptics#Best-practices).
- Kombiniere Audio-Cues mit passender Haptik für Menschen, die Ton nicht wahrnehmen (hig:accessibility#Hearing).

### Feedback allgemein
- Mache Feedback mehrkanalig zugänglich: Farbe, Text, Ton, Haptik – funktioniert dann auch stumm, beim Wegschauen und mit VoiceOver (hig:feedback#Best-practices).
- Integriere Statusinformation nah am betroffenen Element (z. B. Mail: Ungelesen-Zahl in der Toolbar) (hig:feedback#Best-practices).
- Nutze Alerts nur für kritische, idealerweise handlungsrelevante Information (hig:feedback#Best-practices, hig:alerts#Best-practices).
- Warne vor **unerwartetem und irreversiblem** Datenverlust – nicht, wenn Verlust das erwartete Ergebnis ist (Finder warnt nicht bei jedem Löschen) (hig:feedback#Best-practices).
- Bestätige Abschluss nur bei wirklich bedeutsamen Aktionen (z. B. Apple-Pay-Zahlung); sonst nur Misserfolg melden (hig:feedback#Best-practices).
- Erkläre, warum ein Befehl nicht ausführbar ist (hig:feedback#Best-practices).

### Laden und Fortschritt
- Zeige so früh wie möglich etwas (Platzhalter, Skeleton), statt leerer Fläche (hig:loading#Best-practices).
- Lass Nutzer während des Ladens anderes tun; Inhalte im Hintergrund laden (hig:loading#Best-practices).
- Bei unvermeidbar langen Wartezeiten: Tipps, Hinweise, neue Features zeigen; Restzeit realistisch schätzen (hig:loading#Best-practices).
- Große Assets (z. B. Spiellevel) mit **Background Assets** nach Installation/Update laden (hig:loading#Best-practices).
- Determinate Progress bevorzugen; von indeterminate auf determinate wechseln, sobald Dauer bekannt (hig:progress-indicators#Best-practices).
- Fortschritt ehrlich und gleichmäßig melden; Indikator in Bewegung halten, Stocken erklären (hig:progress-indicators#Best-practices).
- Nicht zwischen Spinner und Balken wechseln (hig:progress-indicators#Best-practices).
- Vage Beschriftungen wie „Laden…“ / „Authentifizieren…“ vermeiden (hig:progress-indicators#Best-practices).
- Abbrechen ermöglichen, wenn ohne Nebenwirkung; bei Verlust (z. B. Teil-Download) per Alert bestätigen lassen (hig:progress-indicators#Best-practices).

### Launch
- Starte sofort; Wartezeiten über ein paar Sekunden vermeiden (hig:launching#Best-practices).
- Launch Screen (iOS, iPadOS, tvOS) = nahezu identisch mit erstem Screen, ohne Text, ohne Logo/Werbung, passend zu Orientierung und Appearance (hig:launching#Launch-screens).
- macOS, visionOS, watchOS brauchen keinen Launch Screen (hig:launching#Best-practices).
- Splash Screen, falls überhaupt, an den Anfang des Onboardings – nicht als Launch Screen (hig:launching#Best-practices).
- Zustand wiederherstellen (Scrollposition, Fensterlage) (hig:launching#Best-practices).

## Haptics je Plattform

### iOS – UIFeedbackGenerator-Kategorien (hig:playing-haptics#iOS)

| Kategorie (HIG) | Bedeutung laut HIG | UIKit-Klasse / Typen (SDK) |
|---|---|---|
| Notification | Ergebnis einer Aufgabe/Aktion (z. B. Scheck eingereicht, Fahrzeug entriegelt) | `UINotificationFeedbackGenerator` – `.success`, `.warning`, `.error` |
| Impact | Physische Metapher: Einrasten, Aufprall | `UIImpactFeedbackGenerator` – `.light`, `.medium`, `.heavy`, `.soft`, `.rigid` |
| Selection | Werte eines Elements ändern sich (Picker-Rasterung) | `UISelectionFeedbackGenerator` |

Standard-Controls (Toggles, Slider, Picker) spielen System-Haptics bereits selbst. Die Typen in Spalte 3 stammen aus dem UIKit-SDK; die HIG nennt nur die drei Kategorien.

### watchOS – WKHapticType (hig:playing-haptics#watchOS)

| HIG-Name | Bedeutung | `WKHapticType` |
|---|---|---|
| Notification | Wichtiges/außergewöhnliches Ereignis; identisch mit eingehender Notification | `.notification` |
| Up | Wichtiger Wert über Schwelle gestiegen | `.directionUp` |
| Down | Wichtiger Wert unter Schwelle gefallen | `.directionDown` |
| Success | Aktion erfolgreich | `.success` |
| Failure | Aktion fehlgeschlagen | `.failure` |
| Retry | Fehlgeschlagen, erneuter Versuch möglich | `.retry` |
| Start | Aktivität gestartet (Timer o. ä.); Stop folgt üblicherweise | `.start` |
| Stop | Zuvor gestartete Aktivität beendet | `.stop` |
| Click | Rastendes Drehrad, Fortschritt in festen Schritten; Überlappungen vermeiden | `.click` |

watchOS kombiniert Haptics mit einem Ton. Digital Crown: lineare Detents per Default (Apple Watch Series 4 und neuer), Listen geben Detents beim Scrollen; Detents abschalten, wenn sie nicht zur eigenen Animation passen (hig:playing-haptics#watchOS, hig:digital-crown).

### macOS – Force Touch Trackpad (hig:playing-haptics#macOS)

| Muster | Einsatz | `NSHapticFeedbackManager.FeedbackPattern` |
|---|---|---|
| Alignment | Gezogenes Objekt rastet an Ausrichtung ein; Ziel-Abmessung, bevorzugte Position, Anfang/Ende eines Scrubbers | `.alignment` |
| Level change | Wechsel zwischen diskreten Druckstufen (z. B. Spulgeschwindigkeit per Force Click) | `.levelChange` |
| Generic | Allgemeines Feedback, wenn die anderen nicht passen | `.generic` |

Nur bei Drag oder Force Click auf einem Trackpad mit Haptik; Ausgabe über `NSHapticFeedbackPerformer`.

### Custom Haptics (Core Haptics) (hig:playing-haptics#Custom-haptics)

| Baustein | Charakter |
|---|---|
| Transient | Kurz, kompakt, Tap/Impuls |
| Continuous | Anhaltende Vibration |
| Sharpness | Charakter: weich/organisch ↔ knackig/mechanisch |
| Intensity | Stärke |

Kombinierbar mit Audio. Externe Haptik: Game Controller (iPadOS, macOS, tvOS, visionOS), Apple Pencil Pro und bestimmte Trackpads an kompatiblen iPads.

## Plattform-Unterschiede

| Thema | iOS / iPadOS | macOS | watchOS |
|---|---|---|---|
| Haptik-Hardware | Taptic Engine (unterstützte iPhones); iPad über Pencil Pro/Trackpad/Controller | Force Touch Trackpad, Game Controller | Taptic Engine + Ton, Digital-Crown-Detents |
| API | `UIFeedbackGenerator`-Familie, Core Haptics | `NSHapticFeedbackManager`, Core Haptics (Controller) | `WKInterfaceDevice.play(_:)` mit `WKHapticType` |
| Launch Screen | Pflicht (statisch, wie erster Screen) | keiner | keiner |
| Lade-Indikator | Determinate bevorzugt; Refresh Control mit automatischen Updates | Spinner für Hintergrundvorgänge, ohne Label | möglichst vermeiden (siehe unten) |
| Easing | anpassbar | anpassbar | WatchKit-Layout-/Appearance-Animationen haben fest eingebautes Easing, nicht abschaltbar (hig:motion#watchOS) |

visionOS (Kurzüberblick): keine Bewegung im peripheren Sichtfeld, große Objekte translucent bzw. kontrastärmer bewegen, Ortswechsel per Fade, virtuelle Welt nicht rotieren, stationären Bezugsrahmen geben, keine anhaltenden Oszillationen um ~0,2 Hz (hig:motion#visionOS).

## Umsetzung

### SwiftUI
```swift
@Environment(\.accessibilityReduceMotion) private var reduceMotion

// Bewegung → Fade bei Reduce Motion
.transition(reduceMotion ? .opacity : .move(edge: .bottom))
withAnimation(reduceMotion ? nil : .spring) { isExpanded.toggle() }

// Symbol-Animationen (SF Symbols 5+)
Image(systemName: "arrow.down.circle")
    .symbolEffect(.bounce, value: downloads)

// Haptik deklarativ (iOS 17 / macOS 14 / watchOS 10)
.sensoryFeedback(.success, trigger: didSave)
.sensoryFeedback(.selection, trigger: selectedIndex)
```
`.sensoryFeedback` existiert ab iOS 17 / macOS 14 / watchOS 10. Welche `SensoryFeedback`-Fälle auf welcher Plattform tatsächlich spürbar sind (z. B. macOS nur mit haptischem Trackpad), ist im HIG-Spiegel nicht dokumentiert – vor Einsatz in der Apple-Entwicklerdoku prüfen.

### UIKit
```swift
let generator = UINotificationFeedbackGenerator()
generator.prepare()                       // kurz vor dem Ereignis
generator.notificationOccurred(.success)

UIImpactFeedbackGenerator(style: .rigid).impactOccurred()
UISelectionFeedbackGenerator().selectionChanged()

if UIAccessibility.isReduceMotionEnabled { /* Crossfade statt Slide */ }
```

### AppKit
```swift
NSHapticFeedbackManager.defaultPerformer
    .perform(.alignment, performanceTime: .default)
if NSWorkspace.shared.accessibilityDisplayShouldReduceMotion { ... }
```

### watchOS (WatchKit)
```swift
WKInterfaceDevice.current().play(.success)
```

API-Hinweis: Klassennamen und Enum-Fälle stammen aus den Apple-SDKs; die HIG verweist nur auf `UIFeedbackGenerator`, `NSHapticFeedbackPerformer`, `WKHapticType`, Core Haptics.

## Entscheidungshilfe Feedback-Kanal

| Situation | Kanal | Beleg |
|---|---|---|
| Laufender Status (Sync, ungelesen) | Passiv, inline nah am Element | hig:feedback#Best-practices |
| Erwartete Aktion erfolgreich | Kein extra Feedback (oder dezente Haptik/Symbolanimation) | hig:feedback#Best-practices |
| Bedeutsamer Abschluss (Zahlung) | Bestätigung + Notification-Haptik Success | hig:feedback, hig:playing-haptics#iOS |
| Fehlschlag | Inline-Erklärung + Notification-Haptik Error/Failure | hig:feedback, hig:writing#Best-practices |
| Unerwarteter, irreversibler Datenverlust | Alert mit Cancel | hig:feedback, hig:alerts |
| Erwartbarer, rückgängig machbarer Verlust | Kein Alert, Undo anbieten | hig:alerts#Best-practices |
| Wert-Rasterung (Picker, Slider) | Selection-Haptik (bei Standard-Controls automatisch) | hig:playing-haptics#iOS |
| Einrasten/Ausrichten (Drag) | Impact (iOS) / Alignment (macOS) | hig:playing-haptics |
| Kurzer Ladevorgang | Platzhalter; Indikator erst nach „mehr als einem Moment“ | hig:loading#Showing-progress |

## Review-Checkliste

**Motion**
- [ ] Jede eigene Animation hat einen benennbaren Zweck (Orientierung, Status, Feedback).
- [ ] Animationen unterbrechbar; keine Pflicht-Wartezeit.
- [ ] Keine Zusatzanimation auf häufigen Standardinteraktionen.
- [ ] Richtungen konsistent (Ein-/Ausgang spiegelbildlich).
- [ ] Reduce Motion: Fades statt Slides/Zooms, keine Parallax, keine Blur-Übergänge, keine z-Tiefenanimation, Springs gestrafft.
- [ ] Keine schnellen Blink-/Flash-Effekte.
- [ ] Systemanimationen/Default-Springs statt erfundener Zeitwerte.

**Haptics**
- [ ] Jede Haptik entspricht ihrer dokumentierten Bedeutung (Success ≠ Failure).
- [ ] Haptik synchron zu Bild/Ton, Intensität passend zur Animation.
- [ ] Keine Dauer-Haptik in Nicht-Spiel-Apps.
- [ ] In-App-Schalter zum Abschalten (bzw. Systemeinstellung respektiert); App ohne Haptik vollständig nutzbar.
- [ ] Keine Haptik während Kamera-/Mikrofon-/Gyro-Nutzung.
- [ ] watchOS: Click nicht inflationär, Start/Stop paarweise.

**Feedback, Laden, Launch**
- [ ] Feedback auf mindestens zwei Kanälen (z. B. Text + Haptik).
- [ ] Status inline statt Alert.
- [ ] Alerts nur für kritische, handlungsrelevante Fälle.
- [ ] Platzhalter statt leerem Screen; Hintergrundladen.
- [ ] Determinate Progress wo möglich, ehrlicher Fortschritt, abbrechbar.
- [ ] Keine „Laden…“-Floskel als einzige Info.
- [ ] Launch Screen = erster Screen ohne Text/Logo; Zustand wird wiederhergestellt.
- [ ] watchOS: Inhalte sofort; bei Hintergrundarbeit Notification statt Spinner.

## Anti-Patterns

- Bounce/Wiggle auf jedem Button-Tap.
- Seitliche Dismiss-Animation für ein von oben eingeblendetes Panel.
- Success-Haptik bei Fehlschlag oder derselbe Impact für alles.
- Haptik als einzige Rückmeldung eines Fehlers.
- Splash-Logo als Launch Screen, künstliche Startverzögerung.
- Alert „Gespeichert!“ nach jedem Speichern.
- Spinner, der zum Balken wird.
- Fortschrittsbalken, der bei 90 % minutenlang steht.
- Parallax-/Zoom-Übergänge ohne Reduce-Motion-Pfad.
- Endlos pulsierende Deko-Animation im Ruhezustand.

## Unklarheiten / Widersprüche im Spiegel

- **watchOS-Ladeanzeige:** `feedback#watchOS` rät, **keinen** indeterminate Indikator zu zeigen und stattdessen eine Notification bei Abschluss zuzusagen; `loading#watchOS` sagt, bei ein bis zwei Sekunden Ladezeit sei ein Indikator **besser als ein leerer Screen**. Auflösung: kurze Wartezeit → Indikator ok; längere Hintergrundvorgänge → Notification statt Spinner.
- **Dauerwerte:** Keine Millisekunden-, Kurven- oder Spring-Vorgaben in der HIG; „kurz und präzise“ ist die einzige Aussage.
- **iOS-Haptik-Untertypen** (success/warning/error, light/medium/heavy/soft/rigid) stehen nicht im Spiegel, nur im SDK.
- **Haptics-Verfügbarkeit iPad:** Die HIG nennt für iPad nur Apple Pencil Pro, bestimmte Trackpads und Game Controller – keine eingebaute Taptic Engine.
