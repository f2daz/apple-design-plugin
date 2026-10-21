# Status – Komponenten
> Quelle: Apple HIG, lokaler Spiegel (Stand 2026-10-21). Paraphrasiert. Belege: `(hig:<slug>)`, `(hig:<slug>#Anchor)`.

Komponenten, die einen Zustand oder Fortschritt anzeigen: Aktivitätsziele (Activity rings), Wert in einem Bereich (Gauges, macOS Level indicator), laufende Vorgänge (Progress indicators) und Bewertungen (Rating indicators, nur macOS) (hig:status).

- [Activity rings](#activity-rings) – `activity-rings`
- [Gauges](#gauges) – `gauges`
- [Progress indicators](#progress-indicators) – `progress-indicators`
- [Rating indicators](#rating-indicators) – `rating-indicators`

## Activity rings
**Zweck:** Den Tagesfortschritt einer Person bei Move, Exercise und Stand zeigen (hig:activity-rings). **Plattformen:** ios, ipados, watchos; nicht unterstützt in macOS (auch nicht tvOS, visionOS).
**Verwenden, wenn:** die App Health-/Fitness-bezogen ist, insbesondere bei HealthKit-Beiträgen – z. B. Workout-Metrikscreen oder Workout-Zusammenfassung (hig:activity-rings#Best-practices). **Nicht verwenden, wenn:** andere Daten, mehrere Personen, Dekoration, Branding, App-Icon, Marketing oder Notifications im Spiel sind (hig:activity-rings#Best-practices).

**Kernregeln:**
- Zeige nur Move-, Exercise- und Stand-Daten; nie andere Daten in Activity rings und diese Daten nie in anderen Ring-Elementen (hig:activity-rings#Best-practices).
- Zeige Fortschritt genau einer Person und mach per Label, Foto oder Avatar klar, wessen (hig:activity-rings#Best-practices).
- Verändere das Aussehen nie: keine Farbänderung/Filter/Opazität, immer schwarzer Hintergrund, Rundung über Corner Radius statt Kreismaske, schwarzer Rand um den äußeren Ring sichtbar (ggf. dünner schwarzer Stroke, keine Verläufe/Schatten/Effekte), passend skalieren; die Umgebung an die Ringe anpassen, nicht umgekehrt (hig:activity-rings#Best-practices).
- Nutze für zugehörige Labels/Werte (Move/Exercise/Stand, Ist-/Zielwert) die Ringfarben (hig:activity-rings#Best-practices).
- Halte einen Außenrand von mindestens dem Ringabstand frei; nichts darf Ringe oder Rand überdecken oder beschneiden (hig:activity-rings#Best-practices).
- Grenze andere ringartige Elemente per Padding, Linien, Labels, Farbe oder Größe deutlich ab (hig:activity-rings#Best-practices).
- Sende keine Notifications, die Systeminfos der Activity-App wiederholen; keine Activity rings in Notifications (hig:activity-rings#Best-practices).

**Plattform-Besonderheiten:**
- iOS: `HKActivityRingView`; mit gekoppelter Apple Watch drei Ringe, ohne nur der Move-Ring (Näherung aus Schritten und Workouts anderer Apps); Verlauf kann beide Darstellungen mischen (hig:activity-rings#iOS).
- watchOS: immer drei Ringe in den Farben/Bedeutungen der Activity-App (hig:activity-rings).
- iPadOS, watchOS: keine zusätzlichen Hinweise.

**Kennwerte:** Label-/Wertfarben (RGB, im Spiegel als Alt-Text der Farbmuster): Move R 250, G 17, B 79; Exercise R 166, G 255, B 0; Stand R 0, G 255, B 246 (hig:activity-rings#Best-practices). Mindest-Außenrand = Abstand zwischen den Ringen (relativ, keine absolute Zahl).
**Umsetzung:** HealthKitUI `HKActivityRingView` (UIKit). SwiftUI-Entsprechung im Spiegel nicht genannt.
**Typische Fehler:**
- Ringe für eigene Ziele/Metriken oder als Deko/Logo verwenden.
- Ringe auf hellem/farbigem Hintergrund oder mit Kreismaske, die den schwarzen Rand abschneidet.
- Ringe mehrerer Personen nebeneinander ohne eindeutige Zuordnung bzw. Gruppenwerte in einem Ring.

## Gauges
**Zweck:** Einen konkreten numerischen Wert innerhalb eines Bereichs anzeigen, optional mit Kontext zum Bereich (Min/Max-Text, Farbverlauf) (hig:gauges). **Plattformen:** ios, ipados, macos, watchos (auch visionos); nicht unterstützt in tvOS.
**Verwenden, wenn:** ein Wert relativ zu einer Skala relevant ist (z. B. Temperatur, Füllstand). **Nicht verwenden, wenn:** Fortschritt eines laufenden Vorgangs gezeigt wird (→ Progress indicator) oder Zeitverläufe (→ Chart).

**Anatomie/Stile:** kreisförmiger oder linearer Pfad; Standard-Stil mit Indikator an der Wertposition, Capacity-Stil mit Füllung bis zum Wert; Variante „accessory“ im Look von watchOS-Complications, passend für iOS-Lock-Screen-Widgets (hig:gauges#Anatomy).

**Kernregeln:**
- Schreibe knappe Labels für aktuellen Wert und beide Endpunkte – VoiceOver liest sichtbare Labels (hig:gauges#Best-practices).
- Erwäge einen Farbverlauf entlang des Pfads, der die Bedeutung stützt (z. B. heiß → kalt) (hig:gauges#Best-practices).
- Nutze die Accessory-Variante für Lock-Screen-Widgets bzw. Complication-Optik (hig:gauges#Anatomy).
- macOS: Nimm bei großen Bereichen den kontinuierlichen statt den diskreten Capacity-Stil (hig:gauges#macOS).
- macOS: Ändere die Füllfarbe an bedeutsamen Schwellen (sehr niedrig/hoch, Mitte überschritten) – ganz oder als Tiered-State mit Farbfolge (hig:gauges#macOS).

**Plattform-Besonderheiten:**
- macOS: zusätzlich Level indicator mit Stilen Capacity (continuous: transluzente Spur mit Füllbalken; discrete: gleich große Segmente = Gesamtkapazität, nur ganz gefüllt), Rating (→ Rating indicators) und selten Relevance (schattierter Balken, z. B. Suchergebnisse) (hig:gauges#macOS).
- iOS, iPadOS, watchOS: keine zusätzlichen Hinweise.

**Kennwerte:** keine Zahlen im Spiegel. Standard-Füllfarbe der macOS-Capacity-Indikatoren: grün (hig:gauges#macOS).
**Umsetzung:** SwiftUI `Gauge`; AppKit `NSLevelIndicator`. UIKit-Entsprechung im Spiegel nicht genannt.
**Typische Fehler:**
- Fehlende Endpunkt-Labels – Wert ohne Bereichskontext, schlecht für VoiceOver.
- Diskreter Capacity-Indikator bei großem Bereich (winzige Segmente).
- Gauge als Fortschrittsanzeige für Ladevorgänge missbraucht.

## Progress indicators
**Zweck:** Zeigen, dass die App bei Laden oder langen Operationen nicht hängt, ggf. mit Abschätzung der Restdauer; nur sichtbar, solange der Vorgang läuft (hig:progress-indicators). **Plattformen:** ios, ipados, macos, watchos (auch tvos, visionos).
**Typen:** Determinate (bekannte Dauer; Progress bar füllt von leading nach trailing, Circular füllt im Uhrzeigersinn) und Indeterminate/Activity indicator/Spinner (unbekannte Dauer; macOS zusätzlich indeterminate Bar) (hig:progress-indicators).
**Verwenden, wenn:** Vorgänge spürbare Zeit dauern. **Nicht verwenden, wenn:** ein statischer Wert in einem Bereich gezeigt wird (→ Gauge).

**Kernregeln:**
- Bevorzuge Determinate, damit Nutzer über Warten, Später oder Abbruch entscheiden können (hig:progress-indicators#Best-practices).
- Melde Fortschritt möglichst genau und gleichmäßig; ungleichmäßiges Tempo wirkt hängend oder irreführend (hig:progress-indicators#Best-practices).
- Halte Indikatoren in Bewegung; bei Stillstand Feedback zu Problem und Abhilfe geben (hig:progress-indicators#Best-practices).
- Wechsle von indeterminate zu determinate, sobald die Dauer bestimmbar ist – aber nie vom Spinner zur Bar (hig:progress-indicators#Best-practices).
- Ergänze bei Bedarf eine präzise, knappe Beschreibung; vage Begriffe wie „Loading“ vermeiden (hig:progress-indicators#Best-practices).
- Platziere Indikatoren an konsistenter Stelle (hig:progress-indicators#Best-practices).
- Biete Cancel an, wenn Abbruch folgenlos ist; bei Verlustrisiko zusätzlich Pause; bei Fortschrittsverlust per Alert Abbruch bestätigen oder Fortsetzen anbieten lassen (hig:progress-indicators#Best-practices).

**Plattform-Besonderheiten:**
- iOS, iPadOS – Refresh control: Pull-to-refresh als verstecktes Activity-Element (typisch in Table views); trotzdem automatisch periodisch aktualisieren; Titel nur, wenn er Mehrwert liefert (z. B. letzte Aktualisierung), nie als Bedienanleitung (hig:progress-indicators#Refresh-content-controls).
- macOS: Indeterminate als Bar oder Spinner; Spinner für Hintergrundoperationen oder enge Stellen (in Text field, neben Button); Spinner nicht beschriften (hig:progress-indicators#macOS).
- watchOS: standardmäßig weiß über Szenenhintergrund; Farbe per Tint änderbar (hig:progress-indicators#watchOS).

**Kennwerte:** keine verbindlichen Werte im Spiegel (90 %/10 % nur als Negativbeispiel für ungleichmäßiges Tempo).
**Umsetzung:** SwiftUI `ProgressView`; UIKit `UIProgressView`, `UIActivityIndicatorView`, `UIRefreshControl` (SwiftUI-Pendant `refreshable` – im Spiegel nicht erwähnt); AppKit `NSProgressIndicator`.
**Typische Fehler:**
- Spinner, obwohl Fortschritt messbar wäre; Wechsel Spinner → Bar mitten im Vorgang.
- Fortschritt springt auf 90 % und hängt dann.
- „Loading…“-Labels ohne Information; beschrifteter Spinner auf macOS.
- Kein Cancel bei langen Vorgängen; Abbruch mit Datenverlust ohne Rückfrage.

## Rating indicators
**Zweck:** Einen Rang über eine horizontale Reihe von Symbolen (standardmäßig Sterne) darstellen (hig:rating-indicators). **Plattformen:** macos; nicht unterstützt in iOS, iPadOS, watchOS (auch tvOS, visionOS).
**Verwenden, wenn:** Elemente in macOS bewertet/gereiht werden. **Nicht verwenden, wenn:** auf iOS/iPadOS/watchOS – dort existiert die Komponente nicht (eigene Lösung nötig; App-Store-Bewertungen siehe `ratings-and-reviews`).

**Kernregeln:**
- Ermögliche Rangänderung inline in Listen, ohne separaten Bearbeitungsscreen (hig:rating-indicators#Best-practices).
- Ersetze den Stern nur durch ein Symbol, dessen Bewertungszweck eindeutig ist (hig:rating-indicators#Best-practices).
- Rechne mit ganzen Symbolen: Werte werden gerundet, keine Teilsymbole (hig:rating-indicators).
- Plane festen Symbolabstand ein; Symbole skalieren nicht mit der Breite (hig:rating-indicators).

**Plattform-Besonderheiten:** macOS: keine zusätzlichen Hinweise; technisch ein Stil des Level indicator (siehe Gauges).
**Kennwerte:** keine im Spiegel.
**Umsetzung:** AppKit `NSLevelIndicator.Style.rating`.
**Typische Fehler:**
- Halbe Sterne erwarten/darstellen wollen.
- Bewertung nur über Detail-/Editierscreen änderbar.
- Unklares Ersatzsymbol (nicht als Skala erkennbar).
