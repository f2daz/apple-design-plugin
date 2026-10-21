# Writing, Privacy und Branding

Quellen (HIG-Spiegel, Stand 2026-10-21): `writing` (Update 2025-12-16: Sprachmuster, Possessivpronomen), `privacy` (2023-06-21), `branding` (2026-09-09: Markenfarbe), `inclusion` (Welcoming language, Gender identity), `onboarding` (2024-06-10), `alerts` (2024-02-02), ergänzend `buttons#Content`, `notifications`, `launching`, `progress-indicators`.

## Einordnung

Texte sind Teil der UX: Onboarding, Alerts, Fehlermeldungen, Accessibility-Beschreibungen (hig:writing). Privacy ist bei Apple Gestaltungsthema, nicht nur Recht: Transparenz über benötigte Daten, minimale Anforderungen, Schutz der freigegebenen Daten; App-Store-Produktseite zeigt die Privacy-Angaben aus App Store Connect (hig:privacy). Branding soll die App wiedererkennbar machen, aber **dem Inhalt den Vortritt lassen** und vertraute Plattformmuster beibehalten (hig:branding).

## Kernregeln

### Stimme und Ton
- Lege die Stimme der App fest (Zielgruppe, Vokabular, gewünschtes Gefühl) und führe eine Begriffsliste für Konsistenz (hig:writing#Getting-started).
- Passe den Ton an die Situation an: sachlich-direkt bei Ernstem (Zahlungsfehler), leicht bei Erfolgen (Ziel erreicht) (hig:writing#Getting-started).
- Schreibe klar und knapp; jedes Wort prüfen, im Zweifel laut vorlesen (hig:writing#Getting-started).
- Schreibe für alle: einfache Sprache, kein Jargon, keine gegenderten Begriffe; Lokalisierung und VoiceOver mitdenken (hig:writing#Getting-started).
- Prüfe den Ton aus verschiedenen Perspektiven; akademischer Ton wirkt ausschließend (hig:inclusion#Welcoming-language).
- Sprich Menschen direkt an („du/Sie“, „dein/Ihr“) statt „der Nutzer“/„der Spieler“ (hig:inclusion#Welcoming-language).
- Fachbegriffe nur mit Definition; Redewendungen durch Klartext ersetzen; Humor nur mit Bedacht (Übersetzbarkeit, Ermüdung, Missverständnis) (hig:inclusion#Welcoming-language).
- Vermeide unnötige Geschlechtsbezüge („Abonnenten können Rezepte posten“ statt „…seine oder ihre Rezepte“); Geschlecht nur abfragen, wenn nötig, dann mit Optionen wie nichtbinär, Selbstbeschreibung, keine Angabe (hig:inclusion#Gender-identity).
- Vermeide kontextspezifische Annahmen (z. B. Sicherheitsfragen zu Studium oder erstem Auto) – universelle Erfahrungen wählen (hig:inclusion#Avoiding-stereotypes).
- Prüfe Farben auf kulturelle Bedeutung je Locale (hig:inclusion#Languages).

### Struktur und Sprachmuster
- Wichtigstes zuerst; mehrere Ideen ggf. auf mehrere Screens verteilen (hig:writing#Best-practices).
- Handlungsorientiert: aktive Sprache, Buttons und Links mit Verb („Senden“ statt „Los geht’s!“); keine „Hier klicken“-Links, sondern beschreibender Linktext (wichtig für Screenreader) (hig:writing#Best-practices).
- Baue wiederkehrende Sprachmuster auf (hig:writing#Best-practices).
- Wähle je UI-Elementtyp eine Großschreibungsregel und halte sie durch (hig:writing#Best-practices).
- Mehrstufige Flows: Start mit „Los geht’s/Get Started“, Fortschritt konsistent mit „Weiter/Continue“ oder „Next“ bzw. Vorschau auf den nächsten Schritt, Abschluss mit „Fertig/Done“ (hig:writing#Best-practices).
- Possessivpronomen sparsam („Favoriten“ statt „Deine Favoriten“), Perspektive nicht wechseln; **„wir“ vermeiden** („Inhalt kann nicht geladen werden“ statt „Wir haben Probleme …“) (hig:writing#Best-practices).
- Gesten gerätegerecht benennen (Touch: „tippen“, nicht „klicken“) (hig:writing#Best-practices).
- Kleine Displays (iPhone, Watch) und große (TV, mehrere Zuschauer) verlangen Kürze (hig:writing#Best-practices).
- Leere Zustände: nächste Schritte nennen, Button/Link anbieten, keine kritische Info, die später verschwindet (hig:writing#Best-practices).
- Einstellungen: praktisch benennen; Beschreibung erklärt den eingeschalteten Zustand; auf Settings per direktem Link/Button verweisen statt Pfad zu beschreiben (hig:writing#Best-practices).
- Textfelder: klare Labels, Hint/Platzhalter mit Format-Beispiel („name@example.com“) (hig:writing#Best-practices).
- Wähle den Zustellkanal nach Dringlichkeit: Inline, Notification, Alert, Action Sheet (hig:writing#Best-practices).

### Fehlermeldungen
- Fehler möglichst vermeiden; wenn nötig, **nah am Problem** anzeigen (hig:writing#Best-practices).
- Keine Schuldzuweisung; sagen, was zu tun ist („Wähle ein Passwort mit mindestens 8 Zeichen“ statt „Passwort zu kurz“) (hig:writing#Best-practices).
- Keine Interjektionen wie „Hoppla!“/„Oops“ (hig:writing#Best-practices).
- Positiv formulieren („Nur Buchstaben verwenden“ statt „Keine Zahlen oder Symbole“); keine Roboter-Meldungen wie „Ungültiger Name“ (hig:writing#Best-practices).
- Fehler, die viele trifft und Sprache nicht löst → Interaktion überdenken (hig:writing#Best-practices).
- Fehler per Alert, nicht per Notification (hig:notifications).

### Alerts – Text und Buttons
- Ton direkt, neutral, zugänglich; nichts verschleiern, nichts vorwerfen (hig:alerts#Content).
- Titel beschreibt die Situation konkret (was, Kontext, warum); kein „Fehler“ oder „Fehler 329347“; maximal zwei Zeilen (hig:alerts#Content).
- Titel als ganzer Satz → Satz-Großschreibung + Satzzeichen; als Fragment → Title Case ohne Endzeichen (hig:alerts#Content).
- Informativer Text nur mit Mehrwert, kurz, vollständige Sätze (hig:alerts#Content).
- Buttons nicht erklären; falls doch, „wählen“ verwenden und exakten Button-Titel ohne Anführungszeichen (hig:alerts#Content).
- Button-Titel: ein bis zwei Wörter, Verb, Ergebnis beschreibend („Alle anzeigen“, „Antworten“, „Ignorieren“); Title Case, ohne Endzeichen (hig:alerts#Buttons).
- „OK“ nur in rein informativen Alerts; „Ja/Nein“ vermeiden; konkretes Verb statt OK (Apple-Beispiele: Erase, Convert, Clear, Delete) (hig:alerts#Buttons).
- Abbrechen-Button heißt immer **„Abbrechen/Cancel“**; nie Default-Button; Einzelbutton, der Default ist → „Fertig/Done“, nicht Cancel (hig:alerts#Buttons).
- Destruktiver Stil nur für destruktive Aktionen, die nicht bewusst gewählt wurden (Papierkorb leeren nach bewusster Wahl → kein destruktiver Stil) (hig:alerts#Buttons).
- Primary Role nie auf destruktiver Aktion (hig:buttons#Content).
- Kein Alert für reine Info, für häufige rückgängig machbare Aktionen oder beim App-Start (hig:alerts#Best-practices).

### Permission Requests und Purpose Strings
- Fordere nur Daten an, die ein Feature wirklich braucht, so spezifisch wie möglich (hig:privacy#Best-practices).
- Frage erst, wenn das Feature genutzt wird; beim Start nur, wenn die App ohne die Freigabe nicht funktioniert (Navigation + Standort) (hig:privacy#Requesting-permission).
- Purpose String: kurzer, vollständiger, aktiver Satz, konkret, Satz-Großschreibung, Punkt am Ende (hig:privacy#Requesting-permission).
- Pre-Alert-Screen nur, wenn Kontext nicht reicht: **genau ein Button**, der den System-Alert öffnet, betitelt „Weiter/Continue“ oder „Next“ – **nicht** „Erlauben/Allow“; keine Schließen-/Abbrechen-Option, keine Zusatzaktionen außer für rechtlich notwendige Einwilligung (hig:privacy#Requesting-permission, Abschnitt „Pre-alert screens, windows, or views“).
- Tracking (ATT): System-Alert **vor** jeder Erhebung von Tracking-Daten; keine irreführenden Vorschaltseiten. Verboten (führt zur Ablehnung): Anreize, Screens, die wie eine Anfrage aussehen, Bild des Alerts, Annotationen hinter dem Alert. Erlaubt: Einwilligungsscreen vor/nach dem ATT-Alert zur Erfüllung lokaler Datenschutzgesetze (App Review Guideline 5.1.1 (iv)) (hig:privacy#Tracking-requests).
- Respektiere Hide My Email, Mail Privacy Protection; kenne Tracking-Pflichten (hig:privacy#Best-practices).
- Integriere notwendige Freigaben ggf. ins Onboarding, um den Nutzen zu erklären; sonst beim ersten Zugriff auf die Funktion (hig:onboarding#Additional-requests).
- Nutze den **Location Button** (iOS, iPadOS, watchOS) für einmalige, situative Standortfreigabe (hig:privacy#Location-button).

### Datenschutz-Umsetzung
- Daten möglichst auf dem Gerät verarbeiten (hig:privacy#Best-practices).
- Systemschutz nutzen (z. B. CloudKit-Verschlüsselung ab iOS 15) (hig:privacy#Best-practices).
- Passkeys statt Passwörter; sonst 2FA; Face ID / Touch ID / Optic ID für eingeloggte Apps (hig:privacy#Protecting-data).
- Sensibles in den Keychain, nie in Klartextdateien (hig:privacy#Protecting-data).
- Keine eigenen Authentifizierungsverfahren; Passkeys, Sign in with Apple, Password AutoFill (hig:privacy#Protecting-data).
- Keine sensiblen/persönlichen Daten in Notifications; generischen Text für ausgeblendete Vorschauen hinterlegen (hig:notifications).

### Branding
- Markenstimme in allen Texten (z. B. einfache Worte, gelegentlich Ausrufezeichen und Emoji, wenn es zur Marke passt) (hig:branding#Best-practices).
- Akzentfarbe sparsam: primäre Aktionen, Status-Indikatoren (Badges, gewählter Tab); Markenfarbe eher in den Content-Layer unter Liquid-Glass-Controls verlagern (hig:branding#Best-practices).
- Custom Font nur, wenn lesbar in allen Größen und mit Bold Text und Dynamic Type; Muster: Custom Font für Headlines, System Font für Body/Captions (hig:branding#Best-practices).
- Marke über vertraute Komponenten ausdrücken; Größe, Platzierung, Verhalten plattformtypisch lassen (hig:branding#Best-practices).
- Branding tritt hinter Inhalt zurück; keine Flächen nur für Markenassets (hig:branding#Best-practices).
- Logo nicht durchgängig zeigen (hig:branding#Best-practices).
- Launch Screen ist kein Branding-Ort; Marke ggf. im Willkommens-/Onboarding-Screen (hig:branding#Best-practices, hig:launching#Launch-screens).
- Apple-Marken dürfen weder im App-Namen noch in Bildern erscheinen; Apple Trademark Guidelines befolgen (hig:branding#Best-practices).
- Keine SF Symbols in Logos/App-Icons, keine Apple-Hardware-Nachbildungen (hig:sf-symbols, hig:app-icons#Design).

### Onboarding (kurz)
- Erst nach dem Launch, nicht Teil davon; schnell, unterhaltsam, optional (hig:onboarding).
- Durch Ausprobieren lehren; kontextbezogene Tipps (TipKit) statt langem Flow (hig:onboarding#Best-practices).
- Tutorial überspringbar, danach nicht erneut zeigen, aber auffindbar (Hilfe/Einstellungen) (hig:onboarding#Best-practices).
- Nur die App erklären, nicht das System (hig:onboarding#Best-practices).
- Splash Screen nur kurz; keine großen Downloads vor dem Start; keine Lizenztexte im Onboarding (App Store zeigt sie) (hig:onboarding#Additional-content).
- Setup aufschieben, sinnvolle Defaults; Bewertungs- und Kaufaufforderungen erst nach echter Nutzung (hig:onboarding#Additional-requests).

## Kennwerte und Beispiele

### Purpose Strings (hig:privacy#Requesting-permission, sinngemäß)

| Bewertung | Beispiel (deutsch) | Warum |
|---|---|---|
| gut | „Die App nimmt nachts Geräusche auf, um Schnarchen zu erkennen.“ | Aktiv, konkret: wie und wozu |
| schlecht | „Mikrofonzugriff wird für ein besseres Erlebnis benötigt.“ | Passiv, vage Begründung |
| schlecht | „Mikrofonzugriff einschalten.“ | Imperativ, keine Begründung |

Der System-Alert zeigt den Purpose String nach dem App-Namen und vor den Buttons; Nutzer sehen und ändern ihn später unter Einstellungen > Datenschutz.

### Was eine Erlaubnis erfordert (hig:privacy#Requesting-permission)

| Kategorie | Beispiele |
|---|---|
| Persönliche Daten | Standort, Gesundheit, Finanzen, Kontakte, sonstige identifizierende Daten |
| Nutzerinhalte | E-Mails, Nachrichten, Kalender, Kontakte, Spielstände, Apple-Music-Aktivität, HomeKit-Daten, Audio, Video, Fotos |
| Geschützte Ressourcen | Bluetooth-Peripherie, Home-Automation, WLAN, lokales Netzwerk |
| Gerätefunktionen | Kamera, Mikrofon |
| visionOS Full Space | ARKit-Daten (Hand Tracking, Plane Estimation, Image Anchoring, World Tracking) |
| Tracking | Advertising Identifier |

### Alert-Buttons (hig:alerts#Buttons)

| Situation | Titel | Position |
|---|---|---|
| Reine Information | OK | – |
| Bestätigung einer Aktion | Konkretes Verb (Löschen, Konvertieren, Leeren) | Default = trailing (Zeile) bzw. oben (Stapel) |
| Abbruch | Abbrechen/Cancel (immer exakt so) | leading (Zeile) bzw. unten (Stapel); nie Default |
| Nur ein Button, der Default ist | Fertig/Done | – |
| Nutzer soll lesen statt Return drücken | keinen Button als Default | – |

Alternative Abbruchwege: Home Screen (iOS/iPadOS), Esc oder Cmd-. (iOS, iPadOS, macOS, visionOS mit Tastatur), Menu-Taste (tvOS). Alerts haben überall Titel, optionalen Text und bis zu drei Buttons; Textfeld möglich in iOS, iPadOS, macOS, visionOS.

### Location Button – anpassbar vs. fix (hig:privacy#Location-button)

| Anpassbar | Nicht anpassbar |
|---|---|
| Systemtitel (z. B. „Current Location“, „Share My Current Location“) | übrige Gestaltung |
| Glyph gefüllt oder Outline | – |
| Hintergrund-, Titel- und Glyph-Farbe | – |
| Eckenradius | – |

Text muss bei allen Accessibility-Größen und Übersetzungen ungekürzt passen; bei wiederholten Problemen (Kontrast, Transparenz) liefert das System keinen Standort mehr.

## Plattform-Unterschiede

| Thema | iOS / iPadOS | macOS | watchOS |
|---|---|---|---|
| Gesten-Verben | tippen, wischen | klicken | tippen, Digital Crown drehen |
| Alerts | Action Sheet statt Alert für Optionen zu bewusster Aktion; scrollende Alerts vermeiden (große Schrift) | App-Icon automatisch im Alert; Unterdrücken-Checkbox, Accessory View, Help-Button; Warnsymbol `exclamationmark.triangle` sparsam (nicht bei Sichern/Papierkorb) | knapp, wenig Platz |
| Privacy | Location Button | Developer ID signieren (außerhalb Store); Sandbox (Pflicht im Mac App Store); Fast User Switching – keine Annahme über angemeldete Person | Location Button verfügbar |
| Texte | Kurz (kleines Display) | mehr Raum, aber gleiche Klarheit | sehr kurz, Notification-Titel besonders knapp |

visionOS: ARKit-Daten nur im Full Space nach Erlaubnis; Blickrichtung bleibt privat (Hover-Effekte systemseitig); Rückkamera liefert leeres Bild – Kamera-Features ersetzen (z. B. Import) (hig:privacy#visionOS).

## Umsetzung

### Purpose Strings (Info.plist, lokalisiert über `InfoPlist.strings`/String Catalog)
```text
NSCameraUsageDescription           – Kamera
NSMicrophoneUsageDescription       – Mikrofon
NSLocationWhenInUseUsageDescription – Standort bei Nutzung
NSPhotoLibraryUsageDescription     – Fotos
NSContactsUsageDescription         – Kontakte
NSCalendarsFullAccessUsageDescription – Kalender (neuere Systeme; ältere: NSCalendarsUsageDescription)
NSUserTrackingUsageDescription     – App Tracking Transparency
NSBluetoothAlwaysUsageDescription  – Bluetooth
NSLocalNetworkUsageDescription     – Lokales Netzwerk
NSFaceIDUsageDescription           – Face ID
```
Schlüsselnamen stammen aus dem Apple-SDK, nicht aus dem HIG-Spiegel; je Ziel-OS in der Doku prüfen.

### SwiftUI
```swift
.alert("Entwurf löschen?", isPresented: $showAlert) {
    Button("Löschen", role: .destructive) { delete() }
    Button("Abbrechen", role: .cancel) { }
} message: {
    Text("Der Entwurf kann nicht wiederhergestellt werden.")
}

LocationButton(.shareCurrentLocation) { manager.requestLocation() }   // CoreLocationUI
    .symbolVariant(.fill)
    .foregroundStyle(.white)
    .tint(.blue)

TipView(FavoriteTip())   // TipKit für kontextuelles Onboarding
```

### UIKit / AppKit
```swift
let alert = UIAlertController(title: "Entwurf löschen?",
                              message: "Der Entwurf kann nicht wiederhergestellt werden.",
                              preferredStyle: .alert)
alert.addAction(UIAlertAction(title: "Abbrechen", style: .cancel))
alert.addAction(UIAlertAction(title: "Löschen", style: .destructive) { _ in delete() })

let ns = NSAlert()
ns.messageText = "Entwurf löschen?"
ns.informativeText = "Der Entwurf kann nicht wiederhergestellt werden."
ns.addButton(withTitle: "Löschen")
ns.addButton(withTitle: "Abbrechen")
ns.showsSuppressionButton = true   // nur bei wiederkehrenden Alerts
```

## Review-Checkliste

**Text**
- [ ] Begriffsliste vorhanden; gleiche Dinge heißen überall gleich.
- [ ] Ton passt zur Situation; kein Humor in Fehler-/Zahlungskontexten.
- [ ] Buttons/Links mit Verb; keine „Hier klicken“-Links; keine Cute-Labels.
- [ ] Einheitliche Großschreibung je Elementtyp (Deutsch: Rechtschreibregeln statt englischem Title Case anwenden).
- [ ] Anrede konsistent (du oder Sie) – keine Mischung; kein „wir“ in Fehlermeldungen.
- [ ] Possessivpronomen nur, wo nötig.
- [ ] Gesten-Verben je Gerät korrekt.
- [ ] Leere Zustände mit nächstem Schritt + Aktion.
- [ ] Fehlermeldungen nah am Feld, lösungsorientiert, ohne Schuld, ohne „Hoppla“.
- [ ] Platzhalter mit Formatbeispiel; Einstellungen mit Beschreibung des Ein-Zustands.
- [ ] Inklusiv: keine Geschlechtsannahmen, kein Jargon ohne Erklärung, keine Redewendungen.

**Alerts**
- [ ] Nur für kritische, handlungsrelevante Fälle; keiner beim Start.
- [ ] Titel konkret, ≤ 2 Zeilen; kein „Fehler“ ohne Inhalt.
- [ ] Buttons: 1–2 Wörter, Verb; „OK“ nur informativ; „Abbrechen“ exakt so und nicht Default.
- [ ] Destruktiver Stil korrekt (nur bei nicht bewusst gewählter Zerstörung); Primary Role nie destruktiv.

**Privacy**
- [ ] Jede Erlaubnis begründet und auf Feature-Zeitpunkt verschoben (Ausnahme: App funktioniert sonst nicht).
- [ ] Purpose Strings: aktiver, konkreter Satz mit Punkt; lokalisiert.
- [ ] Pre-Alert-Screen: genau ein Button „Weiter“, kein „Erlauben“, kein Schließen.
- [ ] ATT-Alert vor jeder Tracking-Erhebung; keine Anreize oder Alert-Imitationen.
- [ ] Location Button statt Daueranfrage, wo situativ.
- [ ] Keychain für Geheimnisse; Passkeys/Sign in with Apple; keine Eigenbau-Auth.
- [ ] Keine sensiblen Inhalte in Notifications.
- [ ] Privacy-Angaben in App Store Connect aktuell.
- [ ] macOS: Sandbox, Developer ID (außerhalb Store).

**Branding / Onboarding**
- [ ] Akzentfarbe nur für primäre Aktionen und Status.
- [ ] Custom Font unterstützt Dynamic Type und Bold Text; Body in Systemschrift.
- [ ] Kein Logo auf jedem Screen, keine Brand-only-Flächen.
- [ ] Launch Screen ohne Logo/Text.
- [ ] Keine Apple-Marken in App-Name oder Bildern.
- [ ] Onboarding kurz, überspringbar, interaktiv; Tutorial später auffindbar; keine Lizenztexte.
- [ ] Rating-/Kauf-Prompts erst nach Nutzung.

## Anti-Patterns

- „Ups! Da ist etwas schiefgelaufen. Wir kümmern uns darum.“ – Interjektion, „wir“, keine Handlungsoption.
- Alert-Titel „Fehler“ mit Button „OK“ für eine Lösch-Bestätigung.
- Ja/Nein-Buttons.
- Purpose String „Wird für ein besseres Erlebnis benötigt.“
- Pre-Permission-Screen mit „Erlauben“ und „Später“.
- Alle Berechtigungen gesammelt beim ersten Start abfragen.
- Gutschein/Belohnung für Tracking-Zustimmung.
- Logo-Splash als Launch Screen; Markenfarbe auf allen Controls.
- Eigenes Login mit Passwort im Klartext-Cache.
- Notification mit Kontostand oder Diagnose im Vorschautext.
- „Klicke auf …“ in einer iPhone-App.
- Settings-Hinweis „Gehe zu Einstellungen > Datenschutz > …“ statt Direktlink.

## Unklarheiten / Widersprüche im Spiegel

- **„wir“:** `writing#Best-practices` rät, „we“ **ganz** zu vermeiden; `inclusion#Welcoming-language` empfiehlt, „we/our“ für die eigene Software oder Firma zu **reservieren**. Strengere Regel (writing, neuer: 2025-12-16) gilt für UI-Texte, besonders Fehlermeldungen.
- **Großschreibung:** `writing` überlässt die Wahl (Title vs. Sentence Case) dem App-Stil; `alerts` und `buttons` schreiben Title Case für Buttons und Fragment-Titel vor. Für deutsche Lokalisierung sind beides englische Konventionen – im Deutschen gelten die normalen Rechtschreibregeln (eigene Einschätzung, nicht im Spiegel).
- **Ausrufezeichen/Emoji:** `branding` nennt sie als mögliches Stilmittel der Markenstimme; `writing` und `alerts` verlangen neutralen, direkten Ton. Auflösung: Markenstimme in Erfolgs-/Leerzuständen, nie in Fehlern und Alerts.
- **Pre-Alert-Screen ohne Schließen:** `privacy` verbietet Schließen/Abbrechen im Pre-Alert-Screen; erlaubt aber Zusatzaktionen, wenn rechtlich für Einwilligung nötig (z. B. DSGVO). Rechtliche Prüfung liegt außerhalb der HIG.
- **Location-Button-Titel** „Share My Current Location“ verwendet ein Possessivpronomen – Systemvorgabe, kein Verstoß gegen `writing`.
