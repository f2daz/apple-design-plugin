# System experiences – Komponenten
> Quelle: Apple HIG, lokaler Spiegel (Stand 2026-10-21). Paraphrasiert. Belege: `(hig:<slug>)`, `(hig:<slug>#Anchor)`.

Oberflächen, über die eine App **außerhalb ihres eigenen Fensters** im System auftaucht: Home/Lock Screen, Dynamic Island, Control Center, Smart Stack, Zifferblatt, Siri/Spotlight. Gemeinsamer Nenner: glanceable, knapp, deep-linkend, meist über WidgetKit / ActivityKit / App Intents umgesetzt.

Inhalt: [App Shortcuts](#app-shortcuts) · [Complications](#complications) · [Controls](#controls) · [Live Activities](#live-activities) · [Notifications](#notifications) · [Snippets](#snippets) · [Status bars](#status-bars) · [Top Shelf](#top-shelf) · [Watch faces](#watch-faces) · [Widgets](#widgets)

**Schnellwahl**
| Bedarf | Komponente |
|---|---|
| Periodisch aktualisierte Info + einfache Aktion auf Home/Lock Screen, Desktop, Smart Stack | Widget |
| Laufender Vorgang mit Anfang/Ende (≤ 8 h), häufige Updates | Live Activity |
| Einmaliges, zeitkritisches Ereignis, Nutzer nicht in der App | Notification |
| Ein Knopf/Schalter in Control Center, Lock Screen, Action button | Control |
| Funktion per Siri/Spotlight/Action button ohne App-Öffnen | App Shortcut (+ Snippet als visuelle Antwort) |
| Daten auf dem Zifferblatt (watchOS) | Complication (= Accessory-Widget) |

---

## App Shortcuts
**Zweck:** Macht zentrale Funktionen/Inhalte der App systemweit (Siri, Spotlight, Shortcuts-App, Action button, Apple Pencil squeeze) verfügbar, ab Installation. **Plattformen:** ios, ipados, watchos (visionos ohne Besonderheiten). Nicht in tvOS; in macOS keine App Shortcuts, aber App-Intents-Aktionen für eigene Shortcuts (hig:app-shortcuts#macOS).

**Verwenden, wenn:** häufige, wichtige Aufgaben, idealerweise ohne Kontextwechsel erledigbar; Mehrschritt-Aufgaben dürfen die App öffnen (hig:app-shortcuts#Best-practices).
**Nicht verwenden, wenn:** die Funktion in eine Domäne fällt, die **app schemas** abdecken – dann diese bevorzugen, damit Apple Intelligence/Siri sie kontextuell anbietet (hig:app-shortcuts#Best-practices).

**Kernregeln:**
- Beschränke dich auf die häufigsten und wichtigsten Aufgaben (hig:app-shortcuts#Best-practices).
- Biete höchstens **einen** optionalen Parameter mit vorhersehbaren, vertrauten Werten an – Nutzer sehen die Liste beim Sprechen nicht (hig:app-shortcuts#Best-practices).
- Frage bei fehlendem optionalem Wert nach; schlage einen wahrscheinlichen Default plus kurze Alternativliste vor (hig:app-shortcuts#Best-practices).
- Halte Sprachphrasen kurz und laut aussprechbar; zusätzliche Pflichtangaben in einem Folgeschritt erfragen (hig:app-shortcuts#Best-practices).
- Mache Shortcuts in der App auffindbar, z. B. mit gelegentlichen Siri-Tipps nach passenden Aktionen (hig:app-shortcuts#Best-practices).
- Antworte mit Snippet (statisch/Bestätigung) oder Live Activity (fortlaufend, z. B. Timer) (hig:app-shortcuts#Responding-to-App-Shortcuts).
- Lege alle kritischen Infos in den vollständigen Dialogtext – Antworten können auf reinen Audiogeräten (AirPods, HomePod) ankommen (hig:app-shortcuts#Responding-to-App-Shortcuts).
- Phrasen müssen den App-Namen enthalten; definiere natürliche Varianten (hig:app-shortcuts#Editorial-guidelines).
- Schreibweise: „App Shortcuts“/„Shortcuts“ in Title Case und Plural; einzelne „shortcuts“ klein (hig:app-shortcuts#Editorial-guidelines).

**Plattform-Besonderheiten:**
- iOS/iPadOS: Erscheinen in Spotlight (Top Hit bzw. Shortcuts-Bereich) mit SF Symbol oder Vorschaubild; Reihenfolge nach Wichtigkeit festlegen – das System priorisiert später nach Nutzung (hig:app-shortcuts#iOS-iPadOS).
- macOS: keine App Shortcuts; App Intents trotzdem in der Shortcuts-App nutzbar (hig:app-shortcuts#macOS).

**Kennwerte:** max. 10 App Shortcuts pro App (hig:app-shortcuts).
**Umsetzung:** App Intents – `AppIntent`, `AppShortcutsProvider`/`AppShortcut`, `AppShortcutPhrase`, Parameter via `@Parameter`; Tipps mit `SiriTipView` (SwiftUI) / `SiriTipUIView` (UIKit); Dialog `IntentDialog(full:supporting:…)`.
**Typische Fehler:** mehrere Parameter in einer Phrase; Infos nur visuell statt im Dialog; Shortcut für eine Funktion, die ein app schema bereits abdeckt; Shortcuts nie in der App beworben.

---

## Complications
**Zweck:** Zeigt aktuelle, relevante Daten direkt auf dem Zifferblatt, sichtbar bei jedem Handgelenkheben. **Plattformen:** watchos (nur).

**Verwenden, wenn:** es wesentliche, sich ändernde Daten gibt, die man auf einen Blick sehen will (hig:complications#Best-practices).
**Nicht verwenden, wenn:** nur ein statischer App-Starter ohne Daten entstünde – solche Complications behalten Nutzer selten (hig:complications#Best-practices).

**Kernregeln:**
- Unterstütze möglichst alle Familien; wo keine sinnvollen Daten passen, zeige ein App-repräsentierendes Bild als Starter (hig:complications#Best-practices).
- Biete mehrere Complications je Familie, jede mit eigenem Deep Link (hig:complications#Best-practices).
- Schütze sensible Daten – mit Always-On sind sie für Umstehende sichtbar (hig:complications#Best-practices).
- Plane die Timeline bewusst: Updates pro Tag und gespeicherte Einträge sind begrenzt (hig:complications#Best-practices).
- Wähle Ring/Gauge passend: closed = Anteil am Ganzen, open = beliebiger Bereich, segmented = schnelle Änderungen im App-Bereich (hig:complications#Visual-design).
- Teste Tinted Mode: Farbe nie als einzigen Informationsträger; ggf. eigene Tinted-Variante für Vollfarbbilder liefern (hig:complications#Visual-design).
- Linienstärken ≥ 2 pt (hig:complications#Visual-design).
- Liefere statische Placeholder-Bilder je unterstützter Complication (hig:complications#Visual-design).

**Plattform-Besonderheiten:** Familien ab watchOS 9: Circular (inkl. Extra Large, Bezel-Text), Corner, Inline (utilitarian small/large), Rectangular; Rectangular kann ab watchOS 10 im Smart Stack erscheinen (Hintergrundfarbe, Relevanz-Intents, eigenes Layout) (hig:complications#Rectangular). Legacy-Templates (Circular small, Modular small/large, Extra large) nur für ältere watchOS-Versionen (hig:complications#Legacy-templates).

**Kennwerte** (pt @2x-Assets; Auszug, vollständig inkl. 38 mm/Placeholder/Legacy siehe Anchors):
| Element | 40 mm | 41 mm | 44 mm | 45/49 mm |
|---|---|---|---|---|
| Circular Image | 42×42 | 44.5×44.5 | 47×47 | 50×50 |
| Circular Extra Large Image | 120×120 | 127×127 | 132×132 | 143×143 |
| Corner Circular | 32×32 | 34×34 | 36×36 | 38×38 |
| Rectangular Large image mit Titel | 150×47 | 159×50 | 171×54 | 178.5×56 |
| Rectangular Large image ohne Titel | 162×69 | 171.5×73 | 184×78 | 193×82 |
- Default-Text (SwiftUI, Rounded): Circular Medium 12/12.5/13/14.5 pt; Corner Semibold 10/10.5/11/12 pt; Rectangular Medium 16.5/17.5/18/19.5 pt (je 40/41/44/45–49 mm) (hig:complications#Circular, #Corner, #Rectangular).
- Bezel-Text füllt fast 180° vor Kürzung; Large-Image-Rectangular mit automatisch 4 pt Eckenradius; System maskiert Circular-Bilder kreisförmig (hig:complications#Circular, hig:complications#Rectangular).
- Weitere Tabellen: (hig:complications#Inline), (hig:complications#Legacy-templates).

**Umsetzung:** WidgetKit (ab watchOS 9 bevorzugt) mit `WidgetFamily.accessoryCircular/.accessoryCorner/.accessoryInline/.accessoryRectangular`, `TimelineProvider` inkl. `placeholder(in:)`, `WidgetRenderingMode`; Legacy: ClockKit `CLKComplicationDataSource`.
**Typische Fehler:** statische Complication ohne Daten; alle Complications öffnen denselben Screen; Info nur über Farbe (bricht im Tinted Mode); Haarlinien < 2 pt.
**Unklarheit:** Die Seite (Stand 2023) nennt keine Größen für 42 mm (neu)/46 mm, während Widgets/Live Activities sie führen. In „Inline“ steht für 41 mm Flat einmal `…x21 pt`, einmal `…x10.5 pt` – vermutlich Tippfehler im Original.

---

## Controls
**Zweck:** Button oder Toggle, der eine App-Funktion aus Control Center, Lock Screen oder per Action button erreichbar macht. **Plattformen:** ios, ipados, macos. Nicht in watchOS, tvOS, visionOS.

**Verwenden, wenn:** eine Aktion den größten Nutzen bringt, ohne die App zu starten – z. B. Live Activity starten, Gerät schalten, Kamera öffnen (hig:controls#Best-practices).
**Nicht verwenden, wenn:** Informationen dargestellt werden sollen (→ Widget) oder die Aufgabe mehrere Schritte in der App braucht.

**Anatomie:** Symbol + Titel + optionaler Wert. Control Center zeigt Symbol (größer: + Titel/Wert), Lock Screen nur Symbol, Action button zeigt Symbol + Wert in der Dynamic Island (hig:controls#Anatomy).

**Kernregeln:**
- Wähle ein Symbol, das das Verhalten allein trägt; für Toggles je ein Symbol für an/aus (hig:controls#Best-practices).
- Animiere Zustandswechsel per Symbol-Animation; bei laufenden Aktionen animiert lassen bis Abschluss (hig:controls#Best-practices).
- Aktualisiere den Control bei Interaktion, Abschluss oder per Push (hig:controls#Best-practices).
- Wähle eine markenkonforme Tint-Farbe (färbt Toggle-„an“ und Dynamic-Island-Darstellung) (hig:controls#Best-practices).
- Fordere nötige Konfiguration (z. B. welche Lampe) direkt beim Hinzufügen an (hig:controls#Best-practices).
- Liefere Hinweistext für den Action button, verbbasiert (hig:controls#Best-practices).
- Gib Platzhalter an, wenn Titel/Wert situativ sind (hig:controls#Best-practices).
- Lass Titel/Wert bei gesperrtem Gerät redigieren; sicherheitsrelevante Aktionen (Tür, Auto) nur nach Entsperren (hig:controls#Best-practices).
- Kamera-Control (ab iOS 18 auf gesperrtem Gerät): gleiche Kamera-UI wie in der App, Anleitung zum Hinzufügen geben (hig:controls#Camera-experiences-on-a-locked-device).

**Plattform-Besonderheiten:** keine zusätzlichen für iOS/iPadOS/macOS (hig:controls#Platform-considerations).
**Kennwerte:** keine im Spiegel.
**Umsetzung:** WidgetKit/SwiftUI `ControlWidget`, `ControlWidgetButton`, `ControlWidgetToggle`; `promptsForUserConfiguration()`, `controlWidgetActionHint(_:)`; App Intents `IntentAuthenticationPolicy`; `LockedCameraCapture`; `SymbolEffect`.
**Typische Fehler:** Symbol unverständlich ohne Titel; Toggle mit nur einem Symbol; Zustand nach Aktion nicht aktualisiert; sensible Werte auf dem Lock Screen sichtbar.

---

## Live Activities
**Zweck:** Zeigt den Fortschritt eines zeitlich begrenzten Vorgangs (Lieferung, Spiel, Workout) laufend und glanceable an. **Plattformen:** ios, ipados, macos (Menüleiste, gespiegelt vom iPhone), watchos (Smart Stack); zusätzlich CarPlay. Nicht in tvOS, visionOS.

**Verwenden, wenn:** Aufgabe/Ereignis mit klarem Anfang und Ende, kurze bis mittlere Dauer ≤ 8 h, häufige Updates (hig:live-activities#Best-practices).
**Nicht verwenden, wenn:** Werbung/Promotion; dauerhafte Info ohne Ende (→ Widget); Einmal-Ereignis (→ Notification).

**Präsentationen (alle Pflicht):** Compact (Dynamic Island, leading + trailing um TrueDepth-Kamera), Minimal (bei mehreren Activities), Expanded (Touch-and-hold), Lock Screen (Banner unten; auf Geräten ohne Dynamic Island auch als Overlay-Banner), dazu StandBy (hig:live-activities#Anatomy).

**Kernregeln:**
- Zeige nur das Wichtigste; Details per Tap in der App, direkt an der richtigen Stelle (hig:live-activities#Best-practices, hig:live-activities#Offering-interactivity).
- Keine sensiblen Daten offen anzeigen – harmlose Zusammenfassung oder Redaction (hig:live-activities#Best-practices).
- Text groß und mindestens Medium-Gewicht; Logo ohne Container, nie das ganze App-Icon (hig:live-activities#Best-practices).
- Unterstütze limited width: Compact/Minimal passen in einen 28-pt-Kreis, notfalls nur leading View (hig:live-activities#Creating-Live-Activity-layouts).
- Nutze konzentrische Ränder und `ContainerRelativeShape` statt hart codierter Radien; Höhe dynamisch an Inhalt anpassen (hig:live-activities#Creating-Live-Activity-layouts).
- Höchstens ein interaktives Element, nur für Kernfunktionen (Pause/Resume, Kontakt) (hig:live-activities#Offering-interactivity).
- Update nur bei neuem Inhalt; Alerts nur für wirklich Wichtiges, nicht parallel Push-Notifications für dasselbe (hig:live-activities#Starting-updating-and-ending-a-Live-Activity).
- Mehrere Ereignisse in **einer** rotierenden Activity bündeln (hig:live-activities#Starting-updating-and-ending-a-Live-Activity).
- Beende sofort bei Ereignisende; Dismissal-Zeit proportional wählen, meist 15–30 min (hig:live-activities#Starting-updating-and-ending-a-Live-Activity).
- Erst iPhone-Design, dann für StandBy/CarPlay/watchOS verfeinern; Lock Screen nicht wie eine Notification gestalten (hig:live-activities#Presentation, hig:live-activities#Lock-Screen-presentation).

**Plattform-Besonderheiten:**
- iOS StandBy: Minimal → Tap → Lock-Screen-Präsentation 2× skaliert; Default-Hintergrund empfohlen; Night Mode = Rot-Tint prüfen (hig:live-activities#StandBy-presentation).
- Dynamic Island: Hintergrund immer schwarz-opak, nicht anpassbar (nur Lock Screen erlaubt eigenen Hintergrund); Key-Line-Farbe passend tinten (hig:live-activities#Choosing-colors).
- macOS: erscheint automatisch in der Menüleiste (compact/minimal/expanded), Klick öffnet iPhone Mirroring (hig:live-activities#macOS).
- watchOS: oben im Smart Stack, Default = kombiniertes Compact-Layout; eigenes Layout möglich, gilt aber auch für CarPlay (dort Interaktion deaktiviert) (hig:live-activities#watchOS).
- CarPlay: eigenes Layout über `ActivityFamily.small`; Buttons/Toggles werden deaktiviert (hig:live-activities#CarPlay).

**Kennwerte:**
- Dauer ≤ 8 h; nach Ende bis zu 4 h sichtbar (Lock Screen, Mac-Menüleiste, Smart Stack), Dynamic Island/CarPlay sofort entfernt (hig:live-activities#Best-practices, hig:live-activities#Starting-updating-and-ending-a-Live-Activity).
- Animationen max. 2 s; keine Animation auf Always-On mit reduzierter Helligkeit (hig:live-activities#Adding-transitions-and-animating-content-updates).
- Minimal: bis zu drei Activities in der Dynamic Island (hig:live-activities#Minimal).
- Lock-Screen-Standardrand 14 pt (hig:live-activities#Lock-Screen-presentation).

| iPhone (pt, portrait) | Compact | Minimal | Expanded | Lock Screen | Limited width |
|---|---|---|---|---|---|
| 430×932 | 62.33×36.67 | 36.67–45×36.67 | 408×84–160 | 408×84–160 | 28×28 |
| 393×852 | 52.33×36.67 | 36.67–45×36.67 | 371×84–160 | 371×84–160 | 28×28 |
- iPad Lock Screen: 500×84–160 (1366×1024) bzw. 425×84–160 (übrige gelistete Größen); macOS nutzt iOS-Maße; CarPlay 240×78, 240×100, 170×78; watchOS = Widget-Smart-Stack-Maße (hig:live-activities#Specifications).

**Umsetzung:** ActivityKit (`Activity`, `ActivityAttributes`) + WidgetKit `ActivityConfiguration` mit `DynamicIsland { … }`; `isDynamicIslandLimitedInWidth`; `activitySystemActionForegroundColor(_:)`; `supplementalActivityFamilies([.small])` für watchOS/CarPlay; Start per App Intents `LiveActivityIntent`.
**Typische Fehler:** Activity ohne Ende/über Tage; leading und trailing wirken wie zwei getrennte Infos; zu viele Alerts + doppelte Push-Notifications; mehrere parallele Activities statt einer rotierenden; Buttons, die im Auto nicht funktionieren.

---

## Notifications
**Zweck:** Liefert zeitnahe, wertvolle Informationen, die auf einen Blick verständlich sind – auch wenn die App nicht im Vordergrund ist. **Plattformen:** ios, ipados, macos, watchos (auch tvos, visionos ohne Besonderheiten).

**Verwenden, wenn:** ein Ereignis für den Nutzer relevant ist und er nicht in der App ist; Einwilligung liegt vor (hig:notifications).
**Nicht verwenden, wenn:** Fehlermeldungen (→ Alert) (hig:notifications#Best-practices); Aufforderungen zu Aufgaben in der App; Werbung.

**Kernregeln:**
- Knapp und informativ; keine Mehrfach-Notifications zum selben Anlass (hig:notifications#Best-practices).
- Keine sensiblen/vertraulichen Inhalte (hig:notifications#Best-practices).
- Im Vordergrund dezent integrieren (Badge, Liste aktualisieren) statt zu unterbrechen (hig:notifications#Best-practices).
- Titel kurz, Title Case, ohne Schlusspunkt; bei generischem Titel lieber App-Namen zeigen lassen (hig:notifications#Content).
- Body in ganzen Sätzen, Sentence Case, nicht selbst kürzen; neutralen Platzhaltertext für ausgeblendete Vorschauen liefern (hig:notifications#Content).
- App-Name/-Icon nicht in den Inhalt – das System zeigt sie (hig:notifications#Content).
- Aktionen: nützlich, kurz (Title Case), mit Interface-Icon; keine „App öffnen“-Aktion; destruktive Aktionen vermeiden bzw. kennzeichnen (hig:notifications#Notification-actions).
- Badge nur für Anzahl ungelesener Notifications, aktuell halten, nie als einzige Informationsquelle, keine badge-ähnlichen Eigenbauten (hig:notifications#Badging).
- Sound optional, kurz und unverwechselbar; nie allein für wichtige Info verlassen (hig:notifications#Content).

**Plattform-Besonderheiten:**
- watchOS: Short Look (kurz, diskret, nichts Kritisches nur dort) → Long Look (scrollbar, statisch oder dynamisch; mindestens statische Variante mitliefern, dynamische bevorzugt); Sash oben anpassbar (Farbe/Blur), Dismiss-Button immer unten (hig:notifications#Short-looks, hig:notifications#Long-looks).
- watchOS Double Tap führt die erste nicht-destruktive Aktion aus → häufigste Aktion zuerst (hig:notifications#Double-tap).

**Kennwerte:** bis zu 4 Aktions-Buttons (Detailansicht; auch watchOS Long Look); Long-Look-Hintergrund wie Systemnotifications: Weiß mit 18 % Opazität (hig:notifications#Notification-actions, hig:notifications#Long-looks).
**Umsetzung:** UserNotifications (`UNUserNotificationCenter`, `requestAuthorization`, `UNNotificationCategory`/`UNNotificationAction`, `hiddenPreviewsBodyPlaceholder`, `UNNotificationSound`); Custom UI: UserNotificationsUI `UNNotificationContentExtension`; watchOS: SwiftUI `WKNotificationScene`.
**Typische Fehler:** Fehler als Notification; „Jetzt öffnen“-Aktion; Badge für Nicht-Notification-Zahlen; private Inhalte im Titel; Erinnerungs-Spam.

---

## Snippets
**Zweck:** Kompakte Ansicht, die nach einer Aktion via Siri, Spotlight oder Shortcuts ein Ergebnis zeigt oder eine Bestätigung einholt. **Plattformen:** ios, ipados, macos. Nicht in tvOS, visionOS, watchOS.

**Typen:** *Confirmation* (Bestätigen/Abbrechen, optional mit Optionen) und *Result* (Info ohne Folgeaktion); jedes Snippet-Intent endet mit Result, Confirmation ist optional (hig:snippets).
**Anatomie:** Dialog (von Siri gesprochen, standardmäßig über der View) · Custom View (darf Buttons enthalten) · System-Buttons: Confirmation = Cancel + Primärbutton, Result = Done (hig:snippets#Anatomy).

**Verwenden, wenn:** leichte, schnelle Interaktion zu einer App-Aktion (Wetter, Bestellung bestätigen, Tagesziel).
**Nicht verwenden, wenn:** umfangreiche Details nötig sind → Deep Link in die App (hig:snippets#Best-practices); fortlaufender Status → Live Activity.

**Kernregeln:**
- Kontrast und einheitliche Ränder in Light und Dark prüfen (hig:snippets#Best-practices).
- Inhalt knapp, Höhe ≤ 400 pt; Dynamic Type beim Textumfang bedenken (hig:snippets#Best-practices).
- Primärbutton beschreibend beschriften („Bestellen“ statt „OK“); ohne Angabe heißt er „Continue“ (hig:snippets#Best-practices).
- Zweck visuell vermitteln, Dialogtext aus der Darstellung möglichst weglassen – er ist für Audio-Nutzung da (hig:snippets#Best-practices).

**Plattform-Besonderheiten:** keine zusätzlichen (hig:snippets#Platform-considerations).
**Kennwerte:** max. Höhe der Custom View 400 pt (hig:snippets#Best-practices).
**Umsetzung:** App Intents (SwiftUI-View als Intent-Ergebnis, Bestätigung mit `ConfirmationActionName`); Details siehe „Displaying static and interactive snippets“.
**Typische Fehler:** zu hohe Views (abgeschnitten); „OK“-Primärbutton; Dialogtext als einzige Bedeutungsquelle.

---

## Status bars
**Zweck:** Leiste am oberen Bildschirmrand mit Gerätestatus (Uhrzeit, Netz, Akku). **Plattformen:** ios, ipados. Nicht in macOS, tvOS, visionOS, watchOS.

**Verwenden/Nicht verwenden:** systemgegeben; Entscheidung betrifft nur Lesbarkeit und temporäres Ausblenden.

**Kernregeln:**
- Inhalt unter der Statusleiste abdecken, damit sie lesbar bleibt und nichts interaktiv wirkt; bevorzugt Scroll-Edge-Effekt mit Blur (hig:status-bars#Best-practices).
- Bei Vollbild-Medien temporär ausblenden (hig:status-bars#Best-practices).
- Nie dauerhaft ausblenden; einfache, auffindbare Geste zum Wiedereinblenden (z. B. Tap) (hig:status-bars#Best-practices).

**Plattform-Besonderheiten:** keine zusätzlichen.
**Kennwerte:** keine im Spiegel.
**Umsetzung:** SwiftUI `statusBarHidden(_:)`, `ScrollEdgeEffectStyle`; UIKit `preferredStatusBarStyle`, `UIStatusBarStyle`, `prefersStatusBarHidden`, `UIScrollEdgeEffect`.
**Typische Fehler:** Controls hinter transparenter Statusleiste; permanent versteckte Statusleiste.

---

## Top Shelf
**Zweck:** Bereich auf dem Apple-TV-Home-Screen, der Inhalte der App im Dock prominent zeigt. **Plattformen:** nur tvos (außerhalb des Fokus dieses Plugins).

**Kernregeln:**
- Direkt in Inhalte führen (Play + More Info bei Carousel-Layouts) und Neues statt bereits Gesehenes zeigen (hig:top-shelf#Best-practices).
- Keine Werbung/Preise; dynamische, geschichtete Bilder bevorzugen (hig:top-shelf#Best-practices).
- Mindestens ein statisches Fallback-Bild (2320×720 pt) liefern, das nicht interaktiv wirkt (hig:top-shelf#Best-practices).
- Scrolling Inset Banner: 3–8 Bilder, Text ins Bild + Accessibility-Label (hig:top-shelf#Scrolling-inset-banner).

**Kennwerte:** Bildgrößen je Layout siehe (hig:top-shelf#Sectioned-content-row), (hig:top-shelf#Scrolling-inset-banner).

---

## Watch faces
**Zweck:** Vom Nutzer gewählte Hauptansicht der Apple Watch; Apps können konfigurierte, teilbare Zifferblätter mit ihren Complications anbieten. **Plattformen:** watchos (nur).

**Verwenden, wenn:** die App mehrere Complications hat und ein kuratiertes, vorkonfiguriertes Erlebnis die Entdeckung fördert (hig:watch-faces#Best-practices).
**Nicht verwenden, wenn:** nur eine einzelne, kaum nützliche Complication existiert.

**Kernregeln:**
- Teile Zifferblätter, die deine Complications zeigen (ggf. mit Akzentfarbe, Bildern, Stilen); fehlt die App, fordert das System zur Installation auf (hig:watch-faces#Best-practices).
- Zeige eine Vorschau je geteiltem Zifferblatt (Bezel illustriert oder aus Apple Design Resources) (hig:watch-faces#Best-practices).
- Biete Varianten für alle Geräte; manche Faces erst ab Series 4 (Explorer ab Series 3 mit Cellular) – Geräte kennzeichnen (hig:watch-faces#Best-practices).
- Bei inkompatiblem Face sofort eine kompatible Alternative anbieten statt Fehler zu zeigen (hig:watch-faces#Best-practices).

**Plattform-Besonderheiten:** nur watchOS; Teilen ab watchOS 7 (hig:watch-faces).
**Kennwerte:** keine im Spiegel.
**Umsetzung:** ClockKit `CLKWatchFaceLibrary` („Sharing an Apple Watch face“).
**Typische Fehler:** Face nur für neue Modelle ohne Alternative; Fehlermeldung statt Fallback; keine Vorschau.

---

## Widgets
**Zweck:** Bietet glanceable, zeitnahe Inhalte und fokussierte Interaktionen der App auf Home/Lock Screen, Desktop, Smart Stack u. a. **Plattformen:** ios, ipados, macos, watchos (auch visionos; Apple HomeView laut Spiegel). Nicht in tvOS.

**Familien:** System small/medium/large/extra large (iPad, Mac, visionOS)/extra large portrait (nur visionOS); Accessory circular/rectangular/inline (Lock Screen iPhone/iPad, Watch), corner (nur Watch) (hig:widgets#System-family-widgets, hig:widgets#Accessory-widgets).
**Rendering modes:** full-color, accented (Akzent-/Primärgruppe, Tinted/Clear-Darstellung mit Liquid Glass), vibrant (Lock Screen, StandBy-Nacht, Mac-Desktop) (hig:widgets#Appearances, hig:widgets#Rendering-modes).

**Verwenden, wenn:** einfache, zum App-Hauptzweck passende Info, die sich im Tagesverlauf ändert, plus Deep Links/einfache Aktionen (hig:widgets#Best-practices).
**Nicht verwenden, wenn:** Echtzeit-Updates nötig (→ Live Activity) (hig:widgets#iOS-iPadOS); nur App-Icon-Ersatz; App-artige Komplexität.

**Kernregeln:**
- Eine Idee je Widget; Größen nur anbieten, wenn sie Mehrwert bringen – kleinen Inhalt nicht aufblasen (hig:widgets#Best-practices).
- Informationsdichte ausbalancieren; nur Inhalte zum Hauptzweck (hig:widgets#Best-practices).
- Marke dezent; Logo höchstens klein oben rechts (hig:widgets#Best-practices).
- Datum/Zeit vom System aktualisieren lassen; Stand-Zeitpunkt anzeigen, wenn Updates seltener sind als Blicke (hig:widgets#Updating-widget-content).
- Interaktion: wenige, ausreichend große Ziele (Buttons/Toggles); Tap öffnet die App an der passenden Stelle (hig:widgets#Adding-interactivity).
- Standardränder nutzen, Eckenradius per `ContainerRelativeShape` angleichen (hig:widgets#Choosing-margins-and-padding).
- Systemschrift, Text Styles, SF Symbols; Text nie rastern (hig:widgets#Displaying-text-in-widgets).
- Bedeutung nie nur über Farbe; Vollfarbbilder sparsam (z. B. Album-Art) (hig:widgets#Using-color).
- Accented: Views in Akzent- und Primärgruppe teilen; Vibrant: opake Graustufen statt Weiß-Opazitäten (hig:widgets#Rendering-modes).
- Realistische Gallery-Vorschau, erkennbare Placeholder, eine Beschreibung pro Widget (beginnt mit Verb), Größen gruppieren (hig:widgets#Previews-and-placeholders).

**Plattform-Besonderheiten:**
- iOS/iPadOS: Lock-Screen-Widgets folgen zusätzlich den Complication-Prinzipien (inline über, circular/rectangular unter der Uhr); Always-On mit ausreichend Grau-Kontrast; StandBy/CarPlay = small ohne Hintergrund, hochskaliert → Hintergrund als removable markieren, wenig Bild/Farbe, große Schrift; StandBy-Nacht = Rot-Tint (hig:widgets#iOS-iPadOS, hig:widgets#StandBy-and-CarPlay).
- macOS: keine zusätzlichen Hinweise; Desktop nutzt kleinere Ränder und Vibrant-Darstellung (hig:widgets#Choosing-margins-and-padding, hig:widgets#Appearances).
- watchOS: Smart Stack standardmäßig schwarzer Hintergrund – bedeutungstragende Hintergrundfarbe erwägen; Relevanz (Ort, Workout) via RelevanceKit liefern (hig:widgets#watchOS).
- visionOS (Randthema): 3D-Objekt auf Flächen, zwei Detailstufen (simplified/default), Mounting elevated/recessed, Treatment paper/glass (hig:widgets#visionOS).

**Kennwerte:**
- Standardrand 16 pt, enger 11 pt für Gruppierungen; Mac-Desktop/Lock Screen kleiner (hig:widgets#Choosing-margins-and-padding).
- Schrift ≥ 11 pt; Dynamic Type Large bis AX5 (iOS, iPadOS, visionOS) (hig:widgets#Displaying-text-in-widgets).
- Update-Animationen bis 2 s (hig:widgets#Updating-widget-content).
- Inline-Accessory: nur ein Tap-Ziel (hig:widgets#Adding-interactivity).
- iPhone (Auszug, pt): 430×932 → small 170×170, medium 364×170, large 364×382, circular 76×76, rectangular 172×76, inline 257×26; 393×852 → 158×158, 338×158, 338×354, 72×72, 160×72, 234×26. Volle iPhone/iPad-Tabellen: (hig:widgets#Specifications).
- Watch Smart Stack (pt): 40 mm 152×69.5 · 41 mm 165×72.5 · 42 mm 176×72.5 · 44 mm 173×76.5 · 45 mm 184×80.5 · 46 mm 194×80.5 · 49 mm Ultra 3/4 198×81.5 · Ultra 1/2 191×81.5 (hig:widgets#watchOS-dimensions).
- visionOS: Skalierung 75–125 % durch Nutzer (hig:widgets#Thresholds-and-sizes).

**Umsetzung:** WidgetKit + SwiftUI: `Widget`, `StaticConfiguration`/`AppIntentConfiguration`, `TimelineProvider`, `supportedFamilies`, `containerBackground(for:)`/`containerBackgroundRemovable`, `widgetAccentable(_:)`, `widgetRenderingMode` (Environment), `Button(intent:)`/`Toggle(isOn:intent:)`, `Link`/`widgetURL`, `Text(_:style:)` für Zeitangaben, `supportedMountingStyles(_:)` (visionOS).
**Typische Fehler:** Widget = App-Icon-Kopie; zu dicht/App-artig; statischer Inhalt; Bedeutung nur über Farbe (bricht in Tinted/Vibrant); Text unter 11 pt; Widget-Optik in der App nachgebaut (hig:widgets#Best-practices).
**Hinweis:** „Apple HomeView“ (small-Widgets, Modular face bis 4 Widgets) ist laut Spiegel ein Update vom 2026-10-13 – keine weiteren Belege außerhalb dieser Seite (hig:widgets#Apple-HomeView).
