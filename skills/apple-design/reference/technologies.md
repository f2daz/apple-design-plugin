# Technologien (HIG-Sektion "Technologies")

Zweck: Verdichtete Designregeln für Apple-Technologien, die eine App integriert (Zahlung, Login, Wallet, Siri, Health, Karten usw.). Schwerpunkt iOS, iPadOS, macOS, watchOS. Für Formulierungen, Marken- und Buttonregeln vor der Umsetzung immer die HIG-Seite selbst prüfen.

- Quelle: lokaler HIG-Spiegel `~/.apple-design/hig/pages/<slug>.md`, Sync 2026-10-21.
- Belege: `(hig:<slug>)` bzw. `(hig:<slug>#Anker)`; Anker entsprechen den Überschriften der HIG-Seite (Leerzeichen als `-`).
- Zahlen und Maße stehen nur dort, wo die Seite sie wörtlich nennt. Fehlt eine Zahl, nennt die Seite keine.
- "Plattformen" = Kopfzeile der Seite; "nicht unterstützt" = Abschnitt *Platform considerations*.
- Die Regeln sind paraphrasiert, nicht zitiert. Bilder und Assets liegen in den Apple Design Resources und werden hier nicht eingebettet.

## Übersicht

| Technologie | Plattformen laut Seite | Slug |
|---|---|---|
| AirPlay | iOS, iPadOS, macOS, tvOS, visionOS (watchOS nicht unterstützt) | `airplay` |
| Always On | iOS, watchOS | `always-on` |
| App Clips | iOS, iPadOS | `app-clips` |
| Apple In-App Purchase | iOS, iPadOS, macOS, tvOS, visionOS, watchOS | `apple-in-app-purchase` |
| Apple Pay | iOS, iPadOS, macOS, visionOS, watchOS, Web (nicht tvOS) | `apple-pay` |
| Augmented reality | iOS, iPadOS, visionOS | `augmented-reality` |
| CareKit | iOS, iPadOS | `carekit` |
| CarPlay | iOS | `carplay` |
| Game Center | iOS, iPadOS, macOS, tvOS, visionOS, watchOS | `game-center` |
| Generative AI | alle sechs | `generative-ai` |
| HealthKit | iOS, iPadOS, watchOS | `healthkit` |
| HomeKit | alle sechs | `homekit` |
| iCloud | alle sechs | `icloud` |
| ID Verifier | iOS | `id-verifier` |
| iMessage apps and stickers | iOS, iPadOS | `imessage-apps-and-stickers` |
| Live Photos | iOS, iPadOS, macOS, tvOS, visionOS (nur ansehen) | `live-photos` |
| Mac Catalyst | iPadOS, macOS | `mac-catalyst` |
| Machine learning | alle sechs | `machine-learning` |
| Maps | alle sechs (watchOS statisch) | `maps` |
| NFC | iOS, iPadOS | `nfc` |
| Photo editing | iOS, iPadOS, macOS | `photo-editing` |
| ResearchKit | iOS, iPadOS | `researchkit` |
| SharePlay | iOS, iPadOS, macOS, tvOS, visionOS (watchOS nicht unterstützt) | `shareplay` |
| ShazamKit | alle sechs | `shazamkit` |
| Sign in with Apple | alle sechs, auch Web und Nicht-Apple-Plattformen | `sign-in-with-apple` |
| Siri | alle sechs | `siri` |
| Tap to Pay on iPhone | iOS | `tap-to-pay-on-iphone` |
| VoiceOver | alle sechs | `voiceover` |
| Wallet | iOS, iPadOS, macOS, visionOS, watchOS (nicht tvOS) | `wallet` |
| Querverweis: Widgets | iOS, iPadOS, macOS, watchOS, visionOS | `widgets` |
| Querverweis: Live Activities | iOS, iPadOS, macOS, watchOS | `live-activities` |
| Querverweis: App Shortcuts | iOS, iPadOS, visionOS, watchOS (nicht tvOS; macOS nur App Intents) | `app-shortcuts` |

"Alle sechs" = iOS, iPadOS, macOS, tvOS, visionOS, watchOS.

---

## AirPlay
Kabelloses Streamen von Medien auf Apple TV, HomePod und AirPlay-fähige Geräte.
- Den systemeigenen Media Player (`AVPlayerViewController`) verwenden. Einen eigenen Player nur bauen, wenn der Systemplayer nicht reicht (hig:airplay#Best-practices).
- Im HLS-Playlist das volle Auflösungsspektrum anbieten, sonst wirkt der Inhalt auf großen Displays minderwertig (hig:airplay).
- Nur erwartete Inhalte streamen, keine Hintergrundloops. Streaming und Mirroring unterstützen, Remote-Control-Events unterstützen (hig:airplay).
- Wiedergabe im Hintergrund und bei gesperrtem Gerät fortsetzen. Nicht automatisch spiegeln und fremde Wiedergabe nur für immersive Inhalte unterbrechen (hig:airplay).
- Bei eigenem Player: Buttons, die dem System optisch und im Verhalten entsprechen, nur Apple-Symbole, AirPlay-Icon unten rechts (ab iOS 16/iPadOS 16) (hig:airplay).
- **Ressourcen/Marke:** AirPlay-Icon (schwarz, weiß, Custom-Farbe passend zu anderen Technologie-Icons) aus den Apple Design Resources. Icon und Name nicht interaktiv verwenden und das Icon nicht im Fließtext einsetzen. Die eigene App soll prominenter erscheinen als AirPlay (hig:airplay#Using-AirPlay-icons).
- **Schreibweise:** *AirPlay* ein Wort, A und P groß, nur als Substantiv ("Use AirPlay to …", nicht "AirPlay to your speaker"). Formulierungen wie "works with", "compatible with" sind erlaubt, "Apple AirPlay" ebenfalls (hig:airplay#Referring-to-AirPlay).

## Always On
Das System zeigt bei ruhendem Gerät gedimmte, datensparsame Inhalte (iPhone: Lock-Screen-Widgets und Live Activities; Watch: App im Vordergrund oder mit Background-Session).
- Sensible Daten (Kontostände, Gesundheitsdaten) ausblenden, auch in Notifications (hig:always-on#Best-practices).
- Nützliche, unkritische Infos glanceable lassen, z. B. Pace und Puls im Workout (hig:always-on).
- Wichtiges lesbar halten und Sekundäres dimmen. Bilder und große Farbflächen eher entfernen bzw. dimmen (hig:always-on).
- Layout stabil halten: interaktive Elemente auf "unavailable" umstellen statt sie zu entfernen, selten und dezent aktualisieren (hig:always-on).
- Bewegung sanft in einen Ruhezustand überführen und nicht abrupt stoppen (hig:always-on).
- Plattformen: iOS und watchOS. Auf dem iPhone wirkt Bewegung besonders störend, weil das Gerät oft offen liegt.

## App Clips
Leichtgewichtige, sofort verfügbare Teilversion einer App für eine Aufgabe unterwegs oder als Demo. Start per App Clip Code, NFC, QR, Maps, Safari, Messages oder Siri Suggestions.
- Aufgabe oder Demo vollständig im App Clip abschließbar machen und keine Installation der Voll-App erzwingen (hig:app-clips#Designing-your-App-Clip).
- Auf Kernfunktionen beschränken: linear, ohne Tab Bar, komplexe Navigation oder Settings. Keine Web Views, keine Werbung, kein reines Marketing (hig:app-clips).
- Sofort nutzbar: keine Splash Screens, alle Assets enthalten, klein halten (hig:app-clips).
- Kein Account vor dem Nutzen verlangen. Apple Pay und Sign in with Apple anbieten. Gespeicherte Daten können zwischen Starts gelöscht sein (hig:app-clips#Preserving-privacy).
- Voll-App erst an natürlichen Pausen per `SKOverlay` empfehlen, nicht wiederholt und nicht per Push (hig:app-clips#Showcasing-your-app).
- Notifications sind bis 8 Stunden nach dem Start möglich. Längere Zeiträume nur mit ausdrücklicher Erlaubnis und nur aufgabenbezogen (hig:app-clips#Limiting-notifications).
- App-Clip-Karte: Bild 1800x1200 px, PNG/JPEG ohne Transparenz, kein Text und keine Screenshots. Titel höchstens 30 Zeichen, Untertitel höchstens 56. Button-Verb *View*, *Play* oder *Open* (hig:app-clips#Creating-content-for-an-App-Clip-card).
- **Ressourcen – App Clip Code:** nur generierte Codes (App Store Connect oder App Clip Code Generator) verwenden, nichts verändern, nicht rotieren, animieren oder dimmen. Varianten: scan-only (Kamera-Glyph) und NFC-integrated (iPhone-Glyph). Badge mit App-Clip-Logo, wenn der Platz reicht. Das Logo nie allein verwenden (hig:app-clips#App-Clip-Codes).
- **Maße App Clip Code:** Druck mindestens 3/4 inch (1,9 cm) Durchmesser, digital mindestens 256×256 px (PNG/SVG). Der NFC-Tag braucht mindestens 35 mm, der Code dann mindestens 1,37 inch (3,48 cm). Abstand zu Codegröße höchstens 20:1, besser 10:1. Schutzraum entspricht dem Abstand zwischen Glyph und Ring. Auf einem Zylinder höchstens 1/6 des Umfangs (hig:app-clips#Displaying-App-Clip-Codes).
- **Druck:** matt, Rasterung mindestens 600 ppi, Druck mindestens 300 dpi, sRGB→CMYK relativ farbmetrisch, Delta E 2,5, NFC-Tags Type 5. Mit Apples Kalibrier-Testbögen prüfen (hig:app-clips#Printing-guidelines).
- **Marke:** *App Clips*/*App Clip Code* in Title Case, Apple-Marken nicht übersetzen, Codes inaktiver Clips nicht mehr zeigen (hig:app-clips#Legal-requirements).

## Apple In-App Purchase
Verkauf digitaler Güter und Abos in der App (consumable, non-consumable, auto-renewable, non-renewing). Physische Güter und Dienstleistungen laufen dagegen über Apple Pay.
- Die App erst erleben lassen, dann verkaufen. Den Shop im Stil der App integrieren und kurze, nicht umbrechende Produktnamen verwenden (hig:apple-in-app-purchase#Best-practices).
- Für jeden Kauf den Gesamtpreis zeigen. Den Shop nur zeigen, wenn Zahlungen möglich sind (`canMakePayments`). Das System-Bestätigungssheet weder ändern noch nachbauen (hig:apple-in-app-purchase).
- Family Sharing prominent erwähnen (z. B. "Family" im Namen) und Texte für Käufer und Familienmitglieder formulieren. Geteilt wird mit bis zu fünf weiteren Familienmitgliedern (hig:apple-in-app-purchase#Supporting-Family-Sharing).
- Erstattung: eigene Hilfeseite vor dem System-Refund-Flow anbieten, Aktion schlicht benennen ("Refund"/"Request a Refund"), Apples Erstattungspolitik nicht kommentieren und den Refund-Button ohne Scrollen erreichbar machen (hig:apple-in-app-purchase#Providing-help).
- Sign-up-Screen muss enthalten: Abo-Name, Dauer, Leistungsumfang, lokalisierten Preis und einen Weg zum Anmelden bzw. Wiederherstellen. Testphasen und automatische Abbuchung klar erklären (hig:apple-in-app-purchase#Making-signup-effortless).
- Bestehenden Abonnenten keine Neuabschluss-Werbung zeigen. Kündigen muss immer leicht auffindbar sein. Für die Verwaltung die System-UI nutzen (`showManageSubscriptions`) (hig:apple-in-app-purchase#Helping-people-manage-their-subscriptions).
- Offer Codes (iOS/iPadOS): Custom Codes nur alphanumerisches ASCII. Erklären, dass sie per URL oder in der App einzulösen sind. Ein "Redeem Code"-Button reicht, den Rest übernimmt das System (hig:apple-in-app-purchase#Supporting-offer-codes).
- watchOS: dieselben Pflichtangaben wie auf anderen Plattformen, am besten im Modal Sheet mit Close-Button. Optionen kompakt vergleichbar machen, als Button je Option oder als Liste plus Button (hig:apple-in-app-purchase#watchOS). tvOS: Anmeldung über ein zweites Gerät ermöglichen.
- **Schreibweise:** seit 2026-09-17 heißt die Technologie "Apple In-App Purchase".

## Apple Pay
Sichere Zahlung für physische Güter, Dienstleistungen, Spenden und Abos in Apps und in jedem Browser.
- Apple Pay überall anbieten, wo es unterstützt wird. Wenn per API eine aktive Karte erkannt wird, Apple Pay als primäre (nicht zwingend einzige) Option zeigen und nicht in einen eigenen Schritt auslagern (hig:apple-pay#Offering-Apple-Pay).
- Apple-Pay-Buttons nur zum Bezahlen bzw. zum Einrichten verwenden. Den Button nie verstecken oder deaktiviert darstellen, fehlende Angaben erst nach dem Tippen erklären (hig:apple-pay).
- Checkout: Express-Checkout und Buttons auf Produktseiten nutzen. Varianten, optionale Angaben, mehrere Lieferziele und Abholort vor dem Payment Sheet abfragen. Keinen Account vor dem Kauf verlangen, Registrierung auf der Bestätigungsseite anbieten (hig:apple-pay#Streamlining-checkout).
- Payment Sheet: nur nötige Angaben. Line Items für Zuschläge, Rabatte, Spenden und wiederkehrende Zahlungen verwenden, nicht für eine Produktliste. Die Total-Zeile lautet "Pay [Händlername]", bei Marktplätzen "Pay [Endhändler] (via [Plattform])". Kein eigener Spinner (hig:apple-pay#Customizing-the-payment-sheet).
- Fehlermeldungen präzise und feldbezogen formulieren, als Nominalphrase ohne Schlusspunkt, höchstens 128 Zeichen. Eingaben tolerant validieren, z. B. ZIP+4 akzeptieren (hig:apple-pay#Data-validation-errors).
- Abos: Abrechnungsintervall, Testphase ($0) und Startdatum als Line Items. Das Sheet nur bei Mehrkosten erneut zeigen (hig:apple-pay#Supporting-subscriptions). Spenden: Line Item "Donation" und vordefinierte Beträge plus "Other Amount" (hig:apple-pay#Supporting-donations).
- Website-Icon für Apple Pay: 60x60 pt (120x120 px @2x, 180x180 px @3x) (hig:apple-pay#Displaying-a-website-icon).
- **Ressourcen – Buttons:** nur per API erzeugen (`PKPaymentButtonType`/`PKPaymentButtonStyle`, `WKInterfacePaymentButton`, Web-API). Typen: Buy, Pay, Check Out, Continue, Book, Donate, Subscribe, Reload, Add Money, Top Up, Order, Rent, Support, Contribute, Tip, plain "Apple Pay" und "Set Up Apple Pay". Stile: automatic, Black (helle Flächen), White with outline (helle Flächen mit wenig Kontrast), White (dunkle Flächen). Der Corner Radius ist anpassbar (hig:apple-pay#Using-Apple-Pay-buttons).
- **Größe/Position:** nicht kleiner als andere Zahlbuttons und ohne Scrollen sichtbar. Nebeneinander rechts vom Add-to-Cart-Button, gestapelt darüber. Minimum: Apple Pay 100pt × 30pt, Book with Apple Pay 140pt × 30pt, Rand jeweils 1/10 der Buttonhöhe. Passt der übersetzte Titel nicht, ersetzt das System ihn durch den plain Button (gilt nicht für Set Up) (hig:apple-pay#Button-size-and-position).
- **Ressourcen – Apple Pay mark:** zeigt nur die Akzeptanz an und ist nie ein Button. Nur Apple-Artwork verwenden, das einzig in der Höhe angepasst wird (mindestens so hoch wie andere Zahlungsmarken). Schutzraum 1/10 der Höhe, keine Effekte, nicht drehen oder animieren. Download über die Apple Pay Marketing Guidelines (hig:apple-pay#Apple-Pay-mark). Ein eigener Startbutton darf weder "Apple Pay" noch das Logo tragen, dann gehört der Mark auf dieselbe Seite.
- **Schreibweise:** *Apple Pay* zwei Wörter, A und P groß, nie Plural oder Possessiv, nie das Apple-Logo statt "Apple", nicht übersetzen. In den USA ® bei der ersten Nennung im Fließtext, aber nicht in der Zahlartauswahl. Reiner Text in der Zahlartauswahl nur, wenn alle Optionen textuell sind. Auf der Bestätigungsseite z. B. "1234 (Apple Pay)" (hig:apple-pay#Referring-to-Apple-Pay).
- Websites mit Apple Pay brauchen eine Datenschutzerklärung und müssen die Acceptable-use-Regeln einhalten (hig:apple-pay).

## Augmented reality
ARKit-Erlebnisse, die virtuelle Objekte in die Kamerasicht einblenden. Die Seite behandelt iOS/iPadOS, für visionOS verweist sie auf ARKit.
- AR-Funktionen nur auf fähigen Geräten anbieten und auf anderen Geräten ausblenden statt Fehler zu zeigen (hig:augmented-reality).
- Den ganzen Bildschirm für die Szene nutzen. Steuerung als indirekte Controls im Screen Space, gern transluzent. Szene mit 60 Updates pro Sekunde, damit nichts springt (hig:augmented-reality#Best-practices).
- Komfort und Sicherheit beachten: kurze Sessions, Bewegung schrittweise einführen, keine abrupten großen Bewegungen fordern (hig:augmented-reality).
- System-Coaching-View (`ARCoachingOverlayView`) für Initialisierung und Relokalisierung nutzen und dabei andere UI ausblenden (hig:augmented-reality#Providing-coaching).
- Objekte sofort platzieren und später nachjustieren. Plane Classification nutzen und Objekte nicht exakt an Flächenkanten ausrichten (hig:augmented-reality#Helping-people-place-objects).
- Direkte Manipulation mit Standardgesten. Skalieren nur, wenn es sinnvoll ist, und nie als Ersatz für Distanz (hig:augmented-reality#Designing-object-interactions).
- Verständlich formulieren ("surface" statt "plane", keine Begriffe wie ARKit oder tracking). Reset und Abbruch der Relokalisierung ermöglichen. Höchstens 100 aktive Referenzbilder (hig:augmented-reality#Communicating-with-people).
- **Ressourcen:** AR-Glyph und AR-Badges (mit Text bzw. nur Glyph, collapsed/expanded) aus den Apple Design Resources. Nur für ARKit-Erlebnisse verwenden. Den Glyph nur in Größe und Farbe ändern, die Badges gar nicht. Schutzraum jeweils 10 % der Höhe. Badges nur, wenn nicht alle Objekte AR-fähig sind, und immer in derselben Ecke (hig:augmented-reality#Icons-and-badges).

## CareKit
Framework für Care-Plan-Apps (chronische Krankheiten, Reha, Wellness), bestehend aus CareKit UI und CareKit Store.
- Eine Datenschutzerklärung (URL) ist Pflicht. Health-Daten nur im Kontext anfragen, den Standard-Permission-Screen mit Erklärtext nutzen und keine eigenen Freigabe-Screens bauen (hig:carekit#Data-and-privacy).
- View-Kategorien zweckgebunden einsetzen: Tasks, Charts, Contact views (hig:carekit#CareKit-views).
- Task-Stile: simple (ein Schritt), instructions, log (Ereignisse mit Zeitstempel), checklist, grid (kompakt, erlaubt eigene UI). Pflichtfelder sind Titel und Schedule (hig:carekit#Tasks).
- Charts (bar, scatter, line): knappe Labels, klar unterscheidbare Farben mit Kontrast, ggf. Legende, Zeiteinheiten angeben, große Datensätze verdichten (hig:carekit#Charts).
- Farbe nie als einziges Informationsmittel. Medikamente mit Marketingnamen bezeichnen (hig:carekit).
- Notifications sparsam einsetzen und bündeln, Detailansicht mit Aktionen anbieten (hig:carekit#Notifications).
- Eigene Symbole sinnvoll (SF Symbols), kein Firmenlogo als Symbol, Branding dezent (hig:carekit#Symbols-and-branding).
- Plattformen: iOS, iPadOS (nicht macOS, tvOS, visionOS, watchOS).

## CarPlay
Apps auf dem Fahrzeugdisplay, gebaut aus systemdefinierten Templates (Audio, Kommunikation, Navigation usw.).
- Bei aktivem CarPlay keine Interaktion am iPhone verlangen und nie wegen nötiger iPhone-Eingaben aussperren. Muss bei gesperrtem iPhone funktionieren (hig:carplay#iPhone-interactions).
- Audio: Wiedergabe nicht automatisch starten (Ausnahmen: Einzelquelle oder Fortsetzung). Audio-Session erst kurz vor der Wiedergabe öffnen. Now Playing sofort zeigen. Nur nach temporären Unterbrechungen fortsetzen. Nie die Gesamtlautstärke ändern (hig:carplay#Audio).
- Layout: klar und vom Fahrersitz aus scanbar. Wichtiges groß und in der oberen Bildschirmhälfte. Gängige Displays: 800x480 (5:3), 960x540 und 1280x720 (16:9), 1920x720 (8:3) (hig:carplay#Layout).
- Farbe: begrenzte Palette. Interaktive und nicht-interaktive Elemente farblich trennen. Im echten Auto bei verschiedenen Lichtverhältnissen testen. Light und Dark unterstützen (hig:carplay#Color).
- Icons: iPhone-App-Icon übernehmen, keinen schwarzen Hintergrund verwenden. Größen 120x120 (@2x) und 180x180 (@3x) px. Alle Artwork-Dateien in @2x und @3x (hig:carplay#Icons-and-images).
- Fehler in CarPlay melden und nie aufs iPhone verweisen (hig:carplay#Error-handling).
- Plattformen: nur iOS. Audio- und Video-Apps laufen laut Seite ohne Anpassung auch auf Apple HomeView.

## Game Center
Apples soziales Gaming-Netzwerk (GameKit): Achievements, Leaderboards, Challenges, Multiplayer.
- Beim Spielstart den Anmeldestatus prüfen und ggf. sofort initialisieren (hig:game-center#Accessing-Game-Center).
- Access Point nur in Menüs zeigen (nicht im Gameplay, in Tutorials oder Cinematics), keine Controls in seiner Nähe, beide Größen berücksichtigen. Das Spiel pausieren, während Game Overlay bzw. Dashboard offen ist (hig:game-center#Integrating-the-access-point).
- Eigene UI: offizielles Artwork unverändert. Begriffe korrekt: "Game Center" (nicht GameKit/GameCenter), "Game Center Profile", "Achievements", "Leaderboards", "Challenges", "Add Friends" (hig:game-center#Using-custom-UI).
- Achievements: vier Zustände (locked, in-progress, hidden, completed). Titel und Beschreibung je höchstens zwei Zeilen, Titel in Title Case, Beschreibung in Sentence Case. Bild 512x512 pt (1024x1024 px @2x), kreisförmige Maske mit 512 pt Durchmesser, tvOS 320x320 pt mit 200-pt-Maske (hig:game-center#Achievements).
- Leaderboards: classic oder recurring, Sets zur Gruppierung. Bild iOS/iPadOS/macOS 512x512 pt mit Ausschnitt 512x312 pt. tvOS 659x371 pt mit Fokus-Layern (hig:game-center#Leaderboards).
- Challenges: 1–5 Minuten, einzeln spielbar, letzten Versuch statt Bestwert werten. Per Deep Link direkt zum Level. Artwork 1920x1080 pt mit Ausschnitt 1465x767 pt (hig:game-center#Challenges).
- Multiplayer: Party Codes (meist acht Zeichen) im Spiel anzeigen und manuell eingeben lassen. Spätes Einsteigen und Wiederkommen erlauben. Activity-Artwork wie Challenges (hig:game-center#Multiplayer-activities).
- watchOS: keine System-UI für Game Center, Inhalte erscheinen auf dem iPhone (hig:game-center#watchOS). tvOS: optionales Dashboard-Bild 600x180 pt, kein App-Icon.

## Generative AI
Modelle, die Text, Bilder und andere Inhalte erzeugen oder transformieren.
- Verantwortungsvoll gestalten: Menschen behalten die Kontrolle (verwerfen, zurücknehmen, erneut versuchen). KI-Einsatz kennzeichnen. Wo möglich eine Variante ohne KI anbieten (hig:generative-ai#Best-practices).
- Transparenz: nie als menschlich verfasst ausgeben. Fähigkeiten und Grenzen vorab erklären, z. B. mit kuratierten Beispiel-Prompts (hig:generative-ai#Transparency).
- Datenschutz: On-Device-Modell bevorzugen und Serververarbeitung offenlegen. Vor Nutzung persönlicher Daten fragen, minimal erheben, Opt-out anbieten (hig:generative-ai#Privacy).
- Halluzinationen eindämmen: Aufgaben eng zuschneiden, keine unsicheren Fakten abfragen, auf mögliche Fehler hinweisen (hig:generative-ai#Inputs).
- Vor irreversiblen oder heiklen Aktionen (Löschen, Kaufen) bestätigen lassen (hig:generative-ai#Inputs).
- Ausgaben: Edit, Undo, Retry und Adjust nahe am Ergebnis anbieten und Korrekturen sichtbar quittieren. Bei blockierten Anfragen Hinweise zur Formulierung geben. Mehrere Varianten anbieten (hig:generative-ai#Outputs).
- Latenz einplanen: konkrete Statusmeldungen ("Summarizing key themes…") statt "Processing…" (hig:generative-ai#Outputs).
- Freiwilliges, unaufdringliches Feedback (z. B. Daumen hoch/runter). Das Modell austauschbar von der UX trennen (hig:generative-ai#Continuous-improvement).
- Der Foundation-Models-Framework setzt ein kompatibles Gerät mit aktivierter Apple Intelligence voraus (hig:generative-ai#Models-and-datasets).

## HealthKit
Zentrale Ablage für Gesundheits- und Fitnessdaten.
- Ohne Gesundheitsfunktion keinen Zugriff auf Health-Daten anfragen (hig:healthkit).
- Datenschutzerklärung ist Pflicht. Zugriff kontextbezogen und bei jedem Bedarf anfragen. Den Standard-Permission-Screen mit kurzer Begründung nutzen und nicht nachbauen. Freigaben nur über die Systemeinstellungen verwalten (hig:healthkit#Privacy-protection).
- Activity Rings nur für Move, Exercise und Stand und nur für eine Person (klar zugeordnet). Nicht als Deko oder Branding, Farben und Hintergrund nicht verändern. Außenabstand mindestens der Ringabstand. Keine Ringe in Notifications (hig:healthkit#Activity-rings).
- **Ressourcen – Apple Health icon:** nur das Apple-Icon (Apple Design Resources) mit dem Namen *Apple Health* in der Nähe. Nicht kleiner als andere Icons, kein Button, nicht maskieren oder verändern, Schutzraum 1/10 der Höhe, nicht im Text. Keine Screenshots der Health-App. Für Marketing gibt es das Badge "Works with Apple Health" (hig:healthkit#Apple-Health-icon).
- **Schreibweise:** in der UI *Apple Health* bzw. *the Apple Health app* schreiben, nie *HealthKit* (Entwicklerbegriff). Die systemseitige Übersetzung von "Health" verwenden (hig:healthkit#Editorial-guidelines).
- Plattformen: iOS, iPadOS, watchOS (nicht macOS, tvOS, visionOS).

## HomeKit
Steuerung vernetzter Zubehörgeräte über Siri und Apple Home.
- HomeKit-Objektmodell und -Begriffe übernehmen: home, room, zone, accessory, service, characteristic, service group, scene, automation. In der UI weder "service" noch "characteristic" verwenden. "Scene" statt "action set" (hig:homekit#Terminology-and-layout).
- Mehrere Homes berücksichtigen, keine doppelten Home-Settings, HomeKit-Details im Zubehör-Detail zeigen (hig:homekit).
- Setup: System-Setup-Flow nutzen und eine Purpose-String-Begründung liefern. Keinen Account und keine persönlichen Daten verlangen, eigene Setup-Schritte erst danach (hig:homekit#Setup).
- Servicenamen: nur alphanumerisch, Leerzeichen und Apostroph, alphanumerisch beginnen und enden, keine Emojis, keine Firmen- oder Modellnamen, keine Raumangaben im Namen (hig:homekit#Help-people-choose-useful-names).
- Siri: nach dem Setup Beispielphrasen mit dem gewählten Namen zeigen. Shortcuts nur für Funktionen, die HomeKit nicht abdeckt (hig:homekit#Siri-interactions).
- Nur mit Erlaubnis in die HomeKit-Datenbank schreiben und bei Konflikten HomeKit folgen. Kamerabilder nicht verdecken, Mikrofon-Button nur bei bidirektionalem Audio (hig:homekit#Custom-functionality).
- **Ressourcen:** HomeKit-Icon (schwarz, weiß, Custom-Farbe) und Apple-Home-App-Icon nur von Apple. Das HomeKit-Icon nicht interaktiv verwenden, das Home-Icon darf zur App-Store-Seite führen (hig:homekit#Using-HomeKit-icons).
- **Schreibweise:** *HomeKit* ein Wort (H und K groß), *Apple Home* zwei Wörter. HomeKit nicht als Adjektiv ("HomeKit lightbulbs" ist falsch), HomeKit handelt nicht selbst. Bei der ersten Nennung "Apple Home app", nicht übersetzen, keine Gerätekategorien ("iPad", nicht "tablet") (hig:homekit#Referring-to-HomeKit).

## iCloud
Transparente Synchronisation von Inhalten über alle Geräte.
- iCloud automatisch nutzen. Falls eine Wahl nötig ist, einmalig beim ersten Start "alles oder nichts" anbieten (hig:icloud#Best-practices).
- Nicht pro Dokument fragen. Inhalte aktuell halten, bei großen Dateien den Download steuerbar machen und Fortschritt dezent zeigen (hig:icloud).
- Speicher respektieren: nur nutzergenerierte Inhalte ablegen, keine regenerierbaren Ressourcen. Der Documents-Ordner landet im Backup (hig:icloud).
- Ohne iCloud kein Alert, nur ein dezenter Hinweis. App-State und geräteübergreifende Settings in iCloud ablegen (hig:icloud).
- Vor dem Löschen warnen, denn es löscht auf allen Geräten. Konflikte möglichst automatisch lösen, sonst unaufdringlich zur Wahl stellen. iCloud-Inhalte in die Suche einbeziehen (hig:icloud).
- Spiele: Spielstände per GameSave-Framework synchronisieren (hig:icloud).

## ID Verifier
iPhone-App liest mobile IDs (ISO18013-5) vor Ort ohne Zusatzhardware, ab iOS 17.
- Display Only Request (Daten bleiben in der System-UI) bevorzugen. Data Transfer Request nur bei rechtlicher Pflicht und mit zusätzlichem Entitlement (hig:id-verifier).
- Nur nötige Daten anfragen, z. B. eine Altersschwelle (`ageAtLeast`) statt Geburtsdatum (hig:id-verifier#Best-practices).
- Bei Apple Business Register registrieren, damit Name und Logo der Organisation erscheinen (hig:id-verifier).
- Startbutton "Verify Age" bzw. "Verify Identity". Kein NFC- oder QR-Symbol, nie das Apple-Logo (hig:id-verifier).
- Bei Display Only Buttons wie "Matches Person"/"Doesn't Match Person" für die Rückmeldung anbieten (hig:id-verifier).
- Plattformen: nur iOS.

## iMessage apps and stickers
iMessage-Apps und Sticker-Packs in Messages und FaceTime-Effekten.
- Ein primäres Erlebnis pro iMessage-App. Inhalte aus der Haupt-App teilbar machen (hig:imessage-apps-and-stickers#Best-practices).
- Kernfunktionen in der Compact View. Texteingabe nur in der Expanded View (hig:imessage-apps-and-stickers).
- Sticker: ausdrucksstark, inklusiv, auf allen Hintergründen und gedreht oder skaliert lesbar. Pro Sticker eine lokalisierte Alternativbeschreibung für VoiceOver (hig:imessage-apps-and-stickers).
- Icon eckig liefern, das System maskiert. Größen u. a. Messages 148x110/143x100/120x90 (@3x 180x135)/64x48 (@3x 96x72)/54x40 (@3x 81x60), Settings 58x58/87x87, App Store 1024x1024 px (hig:imessage-apps-and-stickers#Icon-sizes).
- Sticker @3x: small 300x300, regular 408x408, large 618x618 px. Keine gemischten Größen im Pack, höchstens 500 KB pro Datei. PNG/APNG mit 8-Bit-Transparenz, GIF einfarbig transparent, JPEG ohne (hig:imessage-apps-and-stickers#Sticker-sizes).
- Plattformen: iOS, iPadOS.

## Live Photos
Fotos mit Ton und Bewegung vor und nach der Aufnahme.
- Bearbeitungen auf alle Frames anwenden, sonst Umwandlung in ein Standbild anbieten. Live Photos nie in Einzelframes oder Audio zerlegen (hig:live-photos#Best-practices).
- Beim Teilen eine Vorschau des ganzen Inhalts zeigen und immer auch das Teilen als normales Foto erlauben (hig:live-photos).
- Download-Fortschritt und Abspielbereitschaft anzeigen. Wo nicht unterstützt, als Standbild zeigen (hig:live-photos).
- Live Photos durch angedeutete Bewegung kenntlich machen. Sonst das System-Badge (mit oder ohne Text) immer an derselben Stelle zeigen, typischerweise in einer Ecke. Kein Play-Button wie bei Video (hig:live-photos).
- Plattformen: iOS, iPadOS, macOS, tvOS. visionOS nur Anzeige, keine Aufnahme. watchOS nicht unterstützt.

## Mac Catalyst
Mac-Version einer iPad-App.
- Gute Kandidaten unterstützen bereits Drag and Drop, Tastaturnavigation und Shortcuts, Multitasking und mehrere Fenster. Apps mit Kernabhängigkeit von Gyroskop, Rückkamera, HealthKit oder ARKit eignen sich eher nicht (hig:mac-catalyst#Before-you-start).
- Idiom: Das iPad-Idiom skaliert auf 77 % (17pt werden zu 13pt). Das Mac-Idiom rendert mit 100 %. Danach Layout prüfen, Schriftgrößen anpassen, Text Styles statt fester Größen nutzen und ggf. einen eigenen Asset-Katalog anlegen (hig:mac-catalyst#Choose-an-idiom).
- Tab Bar durch eine Split View mit Sidebar (bevorzugt) oder ein Segmented Control ersetzen. Top-Level-Einträge ins View-Menü aufnehmen. Next- und Previous-Buttons zusätzlich zu Swipes anbieten (hig:mac-catalyst#Navigation).
- Mac-eigenes App-Icon gestalten (hig:mac-catalyst#App-icons).
- Layout: mehrspaltig, Inspector statt Popover. Controls in die Toolbar verlegen, Top-down-Fluss, Buttons vom unteren und seitlichen Rand wegnehmen (hig:mac-catalyst#Layout).
- Alle Befehle in die Menüleiste (`UIKeyCommand`, `UIMenuBuilder`) und Kontextmenüs großzügig anbieten (hig:mac-catalyst#Menus).
- Plattformen: iPadOS und macOS.

## Machine learning
Modelle für personalisierte, lernende Funktionen. Für generative Fälle siehe Generative AI.
- Rolle klären: kritisch oder ergänzend, privat oder öffentlich, proaktiv oder reaktiv, sichtbar oder unsichtbar, dynamisch oder statisch (hig:machine-learning#The-role-of-machine-learning-in-your-app).
- Explizites Feedback nur bei Bedarf und freiwillig, Optionen mit Folgen beschreiben ("Suggest less pop music" statt "dislike"). Sofort umsetzen und dauerhaft merken (hig:machine-learning#Explicit-feedback).
- Implizites Feedback: Daten schützen, Kontrolle geben, Entdecken nicht einschränken, aktuelle Signale priorisieren, sensible Empfehlungen zurückhalten (hig:machine-learning#Implicit-feedback).
- Kalibrierung nur, wenn sie unverzichtbar ist: einmalig, kurz, mit Fortschrittsanzeige, jederzeit abbrechbar, Daten später änderbar (hig:machine-learning#Calibration).
- Fehler einplanen. Korrekturen vertraut und sofort wirksam machen, geführte Korrekturen bevorzugen. Bei proaktiven Funktionen besonders vorsichtig sein (hig:machine-learning#Mistakes).
- Mehrere Optionen: divers, nicht zu viele, wahrscheinlichste zuerst (hig:machine-learning#Multiple-options).
- Confidence in verständliche Konzepte übersetzen ("Because you listen to pop music" statt "97% match"). Bei niedriger Confidence nichts anzeigen (hig:machine-learning#Confidence).
- Attributions sachlich ("Because you've read …", nicht "… love …") und ohne Statistik-Jargon. Grenzen vorab kommunizieren (hig:machine-learning#Attribution).

## Maps
Karten (MapKit) in App oder Website.
- Karten interaktiv halten. Emphasis Style *default* (gesättigt) oder *muted* (entsättigt, für viel eigenen Inhalt) wählen (hig:maps#Best-practices).
- Suche mit Kategoriefiltern anbieten, Auswahl klar markieren, überlappende POIs clustern (hig:maps).
- Apple-Logo und Legal-Link nicht dauerhaft verdecken: z. B. 7 pt seitlich, 10 pt oben und unten, 10 pt über der tiefsten Ruheposition einer Karte. Unter 200x100 px werden sie nicht gezeigt (hig:maps).
- Annotations im App-Stil. Icon-Strings mit 2–3 Zeichen. Overlays *above roads* (Standard) oder *above labels*. Custom Controls kontrastreich gestalten (hig:maps#Custom-information).
- Place Cards: Stil (automatic, callout full/compact, caption, sheet) passend zur Kartengröße wählen und keine Infos doppeln. Den Ort sichtbar halten. Außerhalb einer Karte muss die Place Card eine Karte enthalten (hig:maps#Place-cards).
- Indoor Maps: Detailgrad nach Zoom, Floor Picker mit Nummern, Umgebung gedimmt, Scrollen begrenzen, Apple Maps nicht kopieren (hig:maps#Indoor-maps).
- watchOS: statische Snapshots, höchstens fünf Annotations, ohne Scrollen sichtbar, kleinster Ausschnitt mit allen POIs (hig:maps#watchOS).

## NFC
Lesen von NFC-Tags in der Nähe (Core NFC).
- Nicht zum Berühren auffordern: "scan" und "hold near" statt "tap" und "touch" (hig:nfc#In-app-tag-reading).
- Keine Fachbegriffe (NFC, Core NFC, tag). Stattdessen das Objekt benennen ("Scan the [object]") (hig:nfc).
- Scanning-Sheet-Text: ein vollständiger Satz in Sentence Case mit Punkt, kurz, bei Folgescans angepasst (hig:nfc).
- Background Tag Reading und In-App-Scan beide anbieten (hig:nfc#Background-tag-reading).
- Plattformen: iOS, iPadOS.

## Photo editing
Photo-Editing-Extensions in der Fotos-App.
- Abbrechen nur nach Rückfrage verwerfen, aber nur wenn bereits bearbeitet wurde (hig:photo-editing#Best-practices).
- Keine eigene obere Toolbar, das Modal hat bereits eine (hig:photo-editing).
- Vorschau vor dem Zurückkehren ermöglichen. Das App-Icon als Extension-Icon verwenden (hig:photo-editing).
- Plattformen: iOS, iPadOS, macOS.

## ResearchKit
Apps für medizinische Studien.
- Onboarding immer in der Reihenfolge Einführung, Eignung, Einwilligung, Datenzugriff (hig:researchkit#Creating-the-onboarding-experience).
- Eignung früh prüfen. Die Einwilligung in Abschnitte gliedern (mit "Learn More"), ggf. ein Verständnisquiz, danach Unterschrift und Kontakt (hig:researchkit).
- Nur studienkritische Daten anfragen und die Begründung erklären (hig:researchkit).
- Surveys: Anzahl und Dauer nennen, eine Frage pro Screen, Fortschritt zeigen, kurz halten, Abschluss melden (hig:researchkit#Conducting-research).
- Active Tasks klar erklären, Voraussetzungen nennen, Ende erkennbar machen (hig:researchkit).
- Profil-Screen (Daten, Austritt, Einwilligung) und Dashboard zur Motivation dauerhaft erreichbar halten (hig:researchkit#Managing-personal-information-and-providing-encouragement).
- Die Seite weist darauf hin, dass sie keine Rechtsberatung ist. Plattformen: iOS, iPadOS.

## SharePlay
Gemeinsame Echtzeit-Aktivitäten über FaceTime und Messages.
- Für Echtzeit nutzen. Für asynchrone Zusammenarbeit danach Teilen oder Speichern anbieten (hig:shareplay#Best-practices).
- Klarer Einstieg, z. B. ein Button mit SharePlay-Symbol. Beitritt ohne Hürden: Sign-in und Abo in einer selbst schließenden View, provisorischer Zugang oder Family Sharing (hig:shareplay).
- Aktivitäten knapp beschreiben (Titel, Kurztext, Bild). Bei Änderungen durch andere zeigen, wer was tut (hig:shareplay).
- **Schreibweise:** *SharePlay* als Substantiv oder Verb ("Join SharePlay", "SharePlay Movie"), ohne Adjektive (nicht "spatial"/"virtual") und ohne Abwandlungen (SharePlayed usw.) (hig:shareplay).
- iOS/iPadOS/macOS: Picture in Picture für geteiltes Video unterstützen (hig:shareplay#iOS-iPadOS-macOS).
- visionOS: Start aus einem Fenster. Spatial Templates (side-by-side, surround, conversational) bzw. eigene Templates. Bis zu fünf spatial Personas, Sitze mindestens einen Meter auseinander, Rollen unabhängig von Sitzen (hig:shareplay#visionOS).
- Plattformen: nicht watchOS.

## ShazamKit
Audioerkennung gegen den Shazam- oder einen eigenen Katalog.
- Mikrofonzugriff mit verständlicher Begründung anfragen (hig:shazamkit, siehe hig:privacy).
- Aufnahme so früh wie möglich beenden (hig:shazamkit#Best-practices).
- Speichern erkannter Songs in der iCloud-Bibliothek nur per Opt-in (hig:shazamkit).
- Plattformen: alle sechs. Die Seite ist sehr kurz (zwei Regeln).

## Sign in with Apple
Anmeldung mit dem Apple Account, optional mit privater Relay-E-Mail.
- Anmeldung nur gegen Mehrwert und so spät wie möglich verlangen. Wenn ein Account Pflicht ist, zuerst begründen. Verknüpfen mit bestehenden Accounts anbieten. Im Commerce erst nach dem Kauf fragen (hig:sign-in-with-apple#Offering-Sign-in-with-Apple).
- Nach dem Login sofort begrüßen. Den Status anzeigen ("Using Sign in with Apple") (hig:sign-in-with-apple).
- Daten: Pflicht und optional kennzeichnen, kein Passwort verlangen, bei Relay-Adresse nicht nach der privaten E-Mail fragen, optionale Daten später erfragen (hig:sign-in-with-apple#Collecting-data).
- Den Button prominent platzieren, nicht kleiner als andere Login-Buttons und ohne Scrollen sichtbar (hig:sign-in-with-apple#Displaying-buttons).
- **Ressourcen – System-Buttons:** `ASAuthorizationAppleIDButton` bzw. `WKInterfaceAuthorizationAppleIDButton`. Titel "Sign in with Apple", "Sign up with Apple", "Continue with Apple". watchOS nur "Sign in". Stile White (alle, für dunkle Flächen), White with outline (iOS, macOS, Web, für helle Flächen), Black (alle, für helle Flächen). watchOS nutzt Dunkelgrau statt Schwarz. Minimum 140pt × 30pt, Rand 1/10 der Höhe, Corner Radius anpassbar (hig:sign-in-with-apple#Using-the-system-provided-buttons).
- **Custom Buttons** (iOS, macOS, Web): Logo nur aus den Apple Design Resources (PNG, SVG, PDF). Nur die drei Titel, Logo und Titel nur schwarz oder weiß. Titelschrift etwa 43 % der Buttonhöhe. Rechter Rand mindestens 8 % der Breite. PNG nur bei 44 pt Höhe bzw. 44x44 pt für Logo-only. Logo-only im Verhältnis 1:1, Form per Maske. App Review prüft alle Custom Buttons (hig:sign-in-with-apple#Creating-a-custom-Sign-in-with-Apple-button).

## Siri
Systemassistent, mit Siri AI (Apple Intelligence) für kontextbewusste App-Aktionen.
- Funktionen und Inhalte per App Intents (intents, entities) bereitstellen. In gängigen Domänen App Schemas nutzen. Onscreen-Inhalte annotieren, Entities an Spotlight und Aktionen als Intents donieren (hig:siri#Getting-your-app-to-work-with-Siri).
- Die häufigsten Aktionen und ihren Kontext ermitteln. Vertraute Begriffe verwenden, relevante statt aller Inhalte anbieten, keine Werbung (hig:siri#Best-practices).
- Eigene Responses nur, wenn die eingebauten nicht reichen. Dann klar, knapp, akustisch und visuell eigenständig, geräteunabhängig, ohne App-Namen und ohne Humor (hig:siri#Customizing-your-app's-experience-with-Siri).
- Inklusiv formulieren ("Who should I send it to?"). Lange Listen durch offene Rückfragen ersetzen. Fehler konkret benennen (hig:siri).
- Für Funktionen außerhalb der Schemas App Shortcuts verwenden (hig:siri, hig:app-shortcuts).
- **Schreibweise:** Siri beim Namen nennen, keine Pronomen. Siri nicht imitieren, keine reservierten Phrasen ("Hey Siri", Notruf). In Übersetzungen nur "Hey" übersetzen. Die Seite listet die zulässigen Formen je Locale, z. B. de_DE "Hey Siri", fr_FR "Dis Siri" (hig:siri#Editorial-guidelines).

## Tap to Pay on iPhone
Kontaktloses Bezahlen am iPhone des Händlers ohne Zusatzhardware (ProximityReader, über einen PSP).
- AGB vor dem Kundenkontakt annehmen lassen, nur durch Admins. Ggf. vorher ein iOS-Update veranlassen (hig:tap-to-pay-on-iphone#Enabling-Tap-to-Pay-on-iPhone).
- Tutorial zu allen Zahlarten (eigenes oder `ProximityReaderDiscovery`). Es muss Checkout, Kartenhaltung und PIN-Eingabe inkl. Accessibility-Modus zeigen (hig:tap-to-pay-on-iphone#Educating-merchants).
- Die Option im Checkout immer anbieten, auch bei laufender Konfiguration (dann mit Fortschrittsanzeige). Beim Start und bei jedem Wechsel in den Vordergrund vorbereiten (`prepare`) (hig:tap-to-pay-on-iphone#Checking-out).
- **Button-Label:** "Tap to Pay on iPhone" oder bei Platzmangel "Tap to Pay". Icon `wave.3.right.circle(.fill)`, nie das Apple-Logo. Form und Farbe passend zur App. Bei einziger Zahlart darf der vorhandene Charge- oder Checkout-Button bleiben (hig:tap-to-pay-on-iphone).
- Endbetrag inkl. Trinkgeld vor dem Tap festlegen. Ergebnis (erfolgreich oder abgelehnt) klar zeigen, digitalen Beleg anbieten, Alternativen bei Fehlschlag (hig:tap-to-pay-on-iphone#Displaying-results).
- Ohne Betrag (Look Up, Store Card, Verify, Refund) und bei Loyalty-Karten generische Labels ohne "Tap to Pay" verwenden (hig:tap-to-pay-on-iphone#Additional-interactions).
- **Ressourcen:** Apple-freigegebene Assets in den Tap to Pay on iPhone Marketing Guidelines. Plattformen: nur iOS.

## VoiceOver
Screenreader für alle Plattformen, auch in Unity-Apps über Apples Plug-ins.
- Alle wichtigen Elemente mit aktuellen, beschreibenden Labels versehen, auch Custom Elements (hig:voiceover#Descriptions).
- Aussagekräftige Bilder beschreiben, dekorative ausblenden (`accessibilityHidden`). Charts mit Kurzbeschreibung und zugänglichen Interaktionen ausstatten (hig:voiceover).
- Eindeutige Titel und korrekte Überschriften verwenden. Gruppierung, Reihenfolge und Bezüge explizit machen, z. B. Bild und Bildunterschrift gruppieren (hig:voiceover#Navigation).
- Inhalts- und Layoutänderungen melden (`AccessibilityNotification`). Den Rotor unterstützen (hig:voiceover).
- visionOS: Bei VoiceOver erhalten Custom Gestures standardmäßig keinen Hand-Input (Direct Gesture mode als Opt-out) (hig:voiceover#visionOS).

## Wallet
Pässe, Bestellverfolgung und Identitätsprüfung in Apple Wallet.
- Neue Pässe direkt anbieten, wiederkehrende nach einmaliger Erlaubnis im Hintergrund hinzufügen. Zusammengehörige Pässe als Gruppe. Abgelehnte Vorschläge nicht wiederholen (hig:wallet#Passes).
- "Add to Apple Wallet"-Button (`PKAddPassButton`) für bestehende, nicht hinzugefügte Pässe. Link "View in Wallet". Ablauf korrekt setzen, Löschen nur mit Erlaubnis, Relevanz für Lock Screen und Live Activity angeben (hig:wallet).
- Change Messages nur für zeitkritische Änderungen, nie für Marketing (hig:wallet).
- Gestaltung: aufgeräumte Vorderseite, Wichtiges in Header-Feldern, Kontrast prüfen, geräteneutrale Sprache ("Slide to view" ist falsch). Bilder nicht polstern, weil watchOS Weißraum beschneidet (hig:wallet#Designing-passes).
- Pass-Stile: boarding, coupon, event ticket (auch poster), store card, poster generic, generic. Poster-Pässe und semantische Boarding Passes brauchen Semantic Tags plus Pass Fields für ältere iOS-Versionen (hig:wallet#Pass-styles).
- Bilder als PNG @2x/@3x ohne eingebetteten Text oder Barcodes. logo 50 pt hoch (Breite 50–160), primaryLogo 30 pt (30–126), secondaryLogo 12 pt (12–135), icon 38x38 pt, strip 375x144 pt, thumbnail 90 pt hoch (60–90), background 343x503 pt, artwork (Poster) 358x448 pt, footer 268x15 pt (hig:wallet#Pass-images).
- Order Tracking: sofort nach Bestellung bereitstellen, Status aktuell halten. Logo und Produktbilder 300x300 px, nicht transparent. Kontaktwege und Tracking-Link angeben, keine doppelten Notifications. Button "Track with Apple Wallet" (`AddOrderToWalletButton`, ab iOS 17) (hig:wallet#Order-tracking).
- Identitätsprüfung: nur bei Geräteunterstützung und nur im Moment des Bedarfs. Purpose String als vollständiger Satz. Minimale Daten, Aufbewahrungsdauer angeben. Buttons "Verify Age/Identity with Apple Wallet", "Continue with Apple Wallet", "Verify with Apple Wallet", immer weiß auf schwarz, optional mit Outline (hig:wallet#Identity-verification).
- **Ressourcen:** Pass Designer (Mac-App mit Templates), Add-to-Apple-Wallet-Badge für E-Mail und Web (Add to Apple Wallet guidelines). Plattformen: nicht tvOS. watchOS zeigt Pässe als Karussell und beschneidet Strip-Bilder (hig:wallet#watchOS).

---

## Querverweise (liegen in der HIG unter Components / System experiences)

### Widgets
Glanceable Inhalte und fokussierte Interaktionen auf Home Screen, Lock Screen, StandBy, Desktop, Smart Stack, visionOS und Apple HomeView. Liegt in der HIG unter Components / System experiences.
- Eine einfache, zum App-Zweck passende Idee mit dynamischen Inhalten. Mehrere Größen nur bei Mehrwert, Infodichte ausbalancieren (hig:widgets#Best-practices).
- Standardrand 16 pt, enger 11 pt. Text mindestens 11 pt, nicht rastern (hig:widgets).
- Animationen für Updates höchstens zwei Sekunden. Datum und Zeit vom System aktualisieren lassen (hig:widgets).
- Interaktion schlicht halten, Deep Link an die passende Stelle (hig:widgets#Adding-interactivity).
- Für Echtzeit-Updates Live Activities nutzen, weil Widgets nicht in Echtzeit aktualisieren (hig:widgets#iOS-iPadOS).

### Live Activities
Fortschritt eines zeitlich begrenzten Ereignisses in Dynamic Island, Lock Screen, StandBy, CarPlay, Mac-Menüleiste und Smart Stack. Liegt in der HIG unter Components / System experiences.
- Nur für Aufgaben mit Anfang und Ende, höchstens acht Stunden. Keine Werbung, keine sensiblen Daten (hig:live-activities#Best-practices).
- Compact und Minimal müssen bei begrenzter Breite in einen Kreis mit 28 pt Durchmesser passen (hig:live-activities#Creating-Live-Activity-layouts).
- Lock-Screen-Rand 14 pt. Kontrast in Dark Mode, Always On und StandBy Night Mode prüfen (hig:live-activities#Lock-Screen-presentation).
- Nur bei neuen Inhalten aktualisieren und nur bei Wesentlichem alarmieren. Sofort beenden, Dismissal meist nach 15–30 Minuten (System höchstens vier Stunden) (hig:live-activities#Starting-updating-and-ending-a-Live-Activity).
- In CarPlay sind interaktive Elemente deaktiviert (hig:live-activities#CarPlay).

### App Shortcuts
Zentrale App-Funktionen für Siri, Spotlight, Shortcuts, Action Button und Apple Pencil (squeeze). Liegt in der HIG unter Components / System experiences.
- In gängigen Domänen zuerst App Schemas prüfen, App Shortcuts für alles Übrige (hig:app-shortcuts#Best-practices).
- Höchstens 10 App Shortcuts pro App. Häufigste Aufgaben, höchstens ein optionaler Parameter mit vorhersehbaren Werten (hig:app-shortcuts).
- Kurze, einprägsame Phrasen mit App-Namen. Alle kritischen Infos auch für Audio-only-Geräte im Dialogtext (hig:app-shortcuts#Editorial-guidelines).
- Schreibweise: *App Shortcuts* und *Shortcuts* (App) in Title Case und Plural, einzelne "shortcuts" klein (hig:app-shortcuts).
- In App und Spotlight nach Wichtigkeit ordnen. macOS unterstützt keine App Shortcuts, nur App Intents (hig:app-shortcuts#macOS).

---

## Auffälligkeiten/Unklarheiten

**Widersprüche und Fehler in den Quellen**
- **Tap to Pay on iPhone:** Der Kopf nennt "Update 2025-01-17", der Change log "January 17, 2024" (steht über "May 7, 2024"). Vermutlich ein Tippfehler im Change log.
- **CarPlay:** Die Seite erwähnt Apple HomeView, obwohl der letzte Change-log-Eintrag von 2023-05-02 ist. Inhalt wurde also ohne Change-log-Eintrag geändert. HomeView wurde laut Widgets-Seite erst am 2026-10-13 ergänzt.
- **HomeKit:** Die Kopfzeile nennt alle sechs Plattformen, der Einleitungstext nur "iOS, tvOS, or watchOS app".
- **HealthKit vs. CareKit:** Bei wiederholten Zugriffsanfragen heißt es einmal "needs to", einmal "good idea". Die Verbindlichkeit unterscheidet sich.
- **Wallet:**
  - Der Abschnitt "Generic passes" verlinkt auf "Creating a Poster Generic Pass".
  - Die Begriffe "Verify with Wallet" und "Verify with Apple Wallet" stehen gemischt nebeneinander.
- **Apple Pay:** In der Mindestgrößen-Tabelle sind die Zeilen Buy, Check Out, Donate, Set Up und Subscribe leer. Vermutlich gelten die 140pt × 30pt aus der Zeile darüber (verbundene Zellen). Vor Verwendung im Original prüfen.

**Veraltete oder auffällig dünne Seiten**
- **Always On:** nennt nur iPhone 14 Pro/Pro Max. Der letzte inhaltliche Stand ist von 2022, das Update von 2023 betraf nur das Artwork.
- **Wenig Inhalt:** ShazamKit (zwei Regeln), Photo editing (vier Regeln), NFC, Live Photos. Ohne Change log oder Update-Vermerk sind Live Photos, NFC, Photo editing, ShazamKit, HealthKit, Augmented reality und Sign in with Apple (dieses nur mit Change-log-Eintrag 2022). Siri hat keinen Abschnitt "Platform considerations".

**Update-Vermerke 2025/2026**
- Apple In-App Purchase, 2026-09-17: Umbenennung von "In-App Purchase" und Überarbeitung.
- SharePlay, 2026-09-09: neue Struktur, mehr visionOS-Inhalte, Custom Templates.
- Apple Pay, Wallet (iOS 27, Pass Designer), Siri (Siri AI), Generative AI und Machine learning, jeweils 2026-06-08.
- iCloud (GameSave), App Clips (Demo-App-Clips) und Game Center (Challenges, Multiplayer, Games-App), jeweils 2025-06-09.
- VoiceOver, 2025-03-07: neue Seite.
- Querverweise: Widgets und Live Activities 2026-10-13, App Shortcuts 2026-06-08 (App Schemas).
