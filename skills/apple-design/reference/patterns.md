# Patterns – verdichtete Regeln aus der Apple HIG

Zweck: Nachschlagewerk für wiederkehrende Interaktionsmuster (Laden, Modalität, Undo, Settings, Medienwiedergabe usw.) beim Entwurf und Review von Apps für iOS, iPadOS, macOS und watchOS. tvOS/visionOS nur am Rand.

- Quelle: lokaler HIG-Spiegel `~/.apple-design/hig/pages/<slug>.md`, Sync-Stand 2026-10-21 (Section "Patterns", 25 Seiten plus Übersicht `hig:patterns`).
- Belegkonvention: `(hig:<slug>)` bzw. `(hig:<slug>#Anker)`. Anker entsprechen den Überschriften der Seite.
- Zahlen und Grenzwerte stehen nur, wenn sie wörtlich auf der Seite vorkommen. Paraphrase, kein Originaltext.

## Inhalt

1. [Charting data](#charting-data)
2. [Collaboration and sharing](#collaboration-and-sharing)
3. [Drag and drop](#drag-and-drop)
4. [Entering data](#entering-data)
5. [Feedback](#feedback)
6. [File management](#file-management)
7. [Going full screen](#going-full-screen)
8. [Launching](#launching)
9. [Live-viewing apps](#live-viewing-apps)
10. [Loading](#loading)
11. [Managing accounts](#managing-accounts)
12. [Managing notifications](#managing-notifications)
13. [Modality](#modality)
14. [Multitasking](#multitasking)
15. [Offering help](#offering-help)
16. [Onboarding](#onboarding)
17. [Playing audio](#playing-audio)
18. [Playing haptics](#playing-haptics)
19. [Playing video](#playing-video)
20. [Printing](#printing)
21. [Ratings and reviews](#ratings-and-reviews)
22. [Searching](#searching)
23. [Settings](#settings)
24. [Undo and redo](#undo-and-redo)
25. [Workouts](#workouts)
26. [Auffälligkeiten/Unklarheiten](#auffälligkeitenunklarheiten)

---

## Charting data

**Zweck:** Charts sollen Aussagen über Daten vermitteln (Trends, Zustand, Vergleich), nicht bloß Daten ablegen. Reine Datenausgabe gehört eher in eine durchsuch- und sortierbare Liste oder Tabelle (hig:charting-data).

**Kernregeln**
- Setze einen Chart nur ein, wenn eine wichtige Aussage über den Datensatz hervorgehoben werden soll; Charts ziehen Aufmerksamkeit (hig:charting-data#Best-practices).
- Halte Charts schlicht; biete Details schrittweise an (Detailstufen, Teilmengen, ggf. mehrere Chart-Versionen mit wachsender Funktionalität) (hig:charting-data#Best-practices).
- Mache jeden Chart barrierefrei: Accessibility-Labels für Werte und Komponenten plus Accessibility-Elemente zur Interaktion; eine beschreibende Überschrift ersetzt die Labels nicht (hig:charting-data#Best-practices).
- Bevorzuge gängige Typen (Bar, Line); erkläre neuartige Darstellungen aktiv, z. B. per Einführungsanimation (hig:charting-data#Designing-effective-charts).
- Betrachte die Daten auf Makro-, Mittel- und Einzelpunkt-Ebene, um Summen, Durchschnitte, Teilmengen oder auffällige Werte anzuzeigen (hig:charting-data#Designing-effective-charts).
- Ergänze Titel, Untertitel, Annotationen oder eine Zusammenfassungszeile mit der handlungsrelevanten Kernaussage (hig:charting-data#Designing-effective-charts).
- Wähle die Größe nach Funktion und Detailgrad: groß für Interaktion, klein für Glanceables oder Vorschau einer größeren Ansicht (hig:charting-data#Designing-effective-charts).
- Halte Charts mit ähnlichem Zweck konsistent; weiche nur ab, um Unterschiede zu betonen (hig:charting-data#Designing-effective-charts).
- Wahre Kontinuität bei mehreren Charts desselben Datensatzes: gleicher Typ, gleiche Farben, Annotationen, Layout (hig:charting-data#Designing-effective-charts).

**Plattform-Unterschiede:** keine zusätzlichen Hinweise für iOS, iPadOS, macOS, watchOS (hig:charting-data#Platform-considerations).

## Collaboration and sharing

**Zweck:** Teilen und Zusammenarbeit über System-Share-Sheet, Sharing-Popover, Collaboration-Button und Messages-Integration; funktioniert mit CloudKit, iCloud Drive oder eigener Infrastruktur (dann Universal Links nötig) (hig:collaboration-and-sharing).

**Kernregeln**
- Platziere den Share-Button gut erreichbar, z. B. in der Toolbar; in SwiftUI `ShareLink` (hig:collaboration-and-sharing#Best-practices).
- Passe Share-Sheet bzw. Sharing-Popover an die unterstützten Freigabearten an ("send copy" je nach CloudKit/iCloud Drive/Custom) (hig:collaboration-and-sharing#Best-practices).
- Formuliere die Berechtigungszusammenfassung als kurze Phrase; das System nutzt sie als Button für die Freigabeoptionen (hig:collaboration-and-sharing#Best-practices).
- Halte eigene Freigabeoptionen minimal und übersichtlich gruppiert (Zugriff, Lesen/Bearbeiten, Teilnehmer hinzufügen) (hig:collaboration-and-sharing#Best-practices).
- Zeige den Collaboration-Button prominent, sobald die Zusammenarbeit beginnt, idealerweise neben dem Share-Button (hig:collaboration-and-sharing#Best-practices).
- Füge im Collaboration-Popover (drei Bereiche: Teilnehmer/Kommunikation, eigene Items, Verwaltungsbutton) nur wirklich nötige Custom-Actions hinzu (hig:collaboration-and-sharing#Best-practices).
- Benenne den Verwaltungsbutton (Default "Manage Shared File") bei Bedarf um; ohne CloudKit-Sharing musst du die Verwaltungsansicht selbst bauen (hig:collaboration-and-sharing#Best-practices).
- Erwäge Collaboration-Events (Änderung, Mitglieder, Erwähnung) als Messages-Benachrichtigung mit Universal Link (`SWHighlightEvent`) (hig:collaboration-and-sharing#Best-practices).

**Plattform-Unterschiede**
- iOS: Share-Sheet mit Freigabemethode und Berechtigungen ab iOS 16. iPadOS 16 und macOS 13: vergleichbares Sharing-Popover. Sonst keine zusätzlichen Hinweise (hig:collaboration-and-sharing#Best-practices).
- watchOS: `ShareLink` in SwiftUI präsentiert das System-Share-Sheet (hig:collaboration-and-sharing#watchOS).
- visionOS: Screen-Sharing im Shared Space; Wechsel in Full Space pausiert den Stream. tvOS: nicht verfügbar.

## Drag and drop

**Zweck:** Inhalte von einer Quelle zu einem Ziel verschieben oder kopieren. Faustregel: gleicher Container = Move, anderer Container = Copy, zwischen Apps immer Copy (hig:drag-and-drop).

**Kernregeln**
- Unterstütze Drag and Drop möglichst überall; Systemkomponenten (Text Field, Text View) bringen es mit (hig:drag-and-drop#Best-practices).
- Biete Alternativen (Menübefehle, Accessibility-APIs `accessibilityDragSourceDescriptors`/`accessibilityDropPointDescriptors`) (hig:drag-and-drop#Best-practices).
- Lege Move/Copy nach Nutzererwartung fest; wähle im Zweifel das Verhalten mit dem geringsten Datenverlustrisiko (hig:drag-and-drop#Best-practices).
- Unterstütze Multi-Item-Drag, wo sinnvoll (hig:drag-and-drop#Best-practices).
- Ermögliche Undo; bei nicht rückgängig machbaren Drops vorher bestätigen lassen oder eine Rücknahme anbieten (hig:drag-and-drop#Best-practices).
- Biete mehrere Repräsentationen von höchster zu niedrigster Fidelity an (z. B. PDF, PNG, JPEG); nimm beim Drop die reichhaltigste unterstützte (hig:drag-and-drop#Accepting-drops).
- Erwäge Spring Loading (Controls aktivieren sich beim Darüberziehen) (hig:drag-and-drop#Best-practices).
- Zeige ein halbtransparentes Drag-Image, sobald etwa drei Punkte gezogen wurden; verändere es nur zur Klärung, nicht ständig (hig:drag-and-drop#Providing-feedback).
- Signalisiere, ob ein Ziel annimmt (Insertion Point, Highlight; sonst nichts oder `circle.slash`); Hinweise nur, solange über dem Ziel (hig:drag-and-drop#Providing-feedback).
- Gib bei ungültigem oder gescheitertem Drop sichtbares Feedback (Zurückfliegen oder Verpuffen) (hig:drag-and-drop#Providing-feedback).
- Scrolle Ziele automatisch, extrahiere nur relevante Teile, prüfe Option-Taste beim Drop (erzwingt Copy), zeige Fortschritt/Platzhalter bei langen Transfers (hig:drag-and-drop#Accepting-drops).
- Übernimm Textstile, wenn beide Seiten sie unterstützen, sonst Zielstil; halte die Auswahl im Ziel, hebe sie in der Quelle passend auf (hig:drag-and-drop#Accepting-drops).

**Plattform-Unterschiede**
- iOS/iPadOS: Touch, Zeigegerät und Full Keyboard Access. iPadOS: Items während eines laufenden Drags hinzufügen (Flocking) und mehrere gleichzeitige Drops annehmen (hig:drag-and-drop#iOS-iPadOS).
- macOS: Drag in den Finder (in wieder öffnenbarem Format, ggf. als Clipping); Drag aus inaktiven Fenstern ohne Aktivierung (Background Selection); Badge mit Anzahl bei Multi-Item; Pointer-Varianten (copy, drag link, disappearing item, operation not allowed); Auswahl und Drag in einer Bewegung (hig:drag-and-drop#macOS). Universal Control zwischen Mac und iPad.
- watchOS: nicht unterstützt (ebenso tvOS). visionOS: Drop in leeren Raum kann App/Szene starten.

## Entering data

**Zweck:** Eingaben minimieren und fehlerarm gestalten; alle Eingabemethoden unterstützen (hig:entering-data).

**Kernregeln**
- Hole Informationen vom System (Settings, Berechtigungen für Ort/Kalender), statt sie abzufragen (hig:entering-data#Best-practices).
- Mache den Bedarf klar: Placeholder, Label, sinnvolle Vorbelegung (hig:entering-data#Best-practices).
- Nutze für sensible Daten ein Secure Field (`SecureField`) (hig:entering-data#Best-practices).
- Befülle Passwortfelder nie vor; nutze Eingabe, Biometrie oder Keychain (hig:entering-data#Best-practices).
- Biete Auswahl (Picker, Menu) statt Freitext, wo möglich (hig:entering-data#Best-practices).
- Erlaube Eingabe per Drag and Drop und Paste (hig:entering-data#Best-practices).
- Validiere dynamisch direkt bei Eingabe; nutze Number Formatter für numerische Felder (hig:entering-data#Best-practices).
- Aktiviere Next/Continue erst, wenn Pflichtdaten vorliegen (hig:entering-data#Best-practices).

**Plattform-Unterschiede**
- macOS: Expansion Tooltip für abgeschnittenen Feldinhalt (gilt auch für iOS/iPadOS-Apps auf dem Mac) (hig:entering-data#macOS).
- iOS, iPadOS, watchOS: keine zusätzlichen Hinweise. tvOS: Digit Entry View kann Ziffern verbergen; visionOS: Secure Field wird bei AirPlay-Streaming geblurrt.

## Feedback

**Zweck:** Status, Erfolg/Misserfolg, Warnungen und Korrekturmöglichkeiten vermitteln; Art der Zustellung an die Bedeutung anpassen (passiv für Status, unterbrechend bei Datenverlust) (hig:feedback).

**Kernregeln**
- Mache Feedback zugänglich und mehrkanalig (Farbe, Text, Ton, Haptik) (hig:feedback#Best-practices).
- Integriere Statusinfos nahe den betroffenen Elementen (z. B. Toolbar-Status in Mail) (hig:feedback#Best-practices).
- Nutze Alerts nur für kritische, idealerweise handlungsrelevante Informationen; Überbenutzung entwertet sie (hig:feedback#Best-practices).
- Warne nur vor unerwartetem, irreversiblem Datenverlust, nicht wenn Löschen das erwartete Ergebnis ist (hig:feedback#Best-practices).
- Bestätige Abschluss nur bei wirklich bedeutenden Aktionen (z. B. Zahlung) (hig:feedback#Best-practices).
- Erkläre, warum ein Befehl nicht ausführbar ist (hig:feedback#Best-practices).

**Plattform-Unterschiede**
- watchOS: Vermeide indeterminierte Fortschrittsanzeigen (Loading Indicator); kündige stattdessen eine Benachrichtigung bei Abschluss an (hig:feedback#watchOS).
- iOS, iPadOS, macOS: keine zusätzlichen Hinweise.

## File management

**Zweck:** Dokumentbasierte Apps beim Erstellen, Öffnen, Sichern und Vorschauen von Dateien systemkonform gestalten (Finder, Files) (hig:file-management).

**Kernregeln**
- Biete New/Open über App-Menüs und Tastaturkürzel an, zusätzlich immer einen Add-Button (+); unter macOS die Add-Aktion ins File-Menü (hig:file-management#Creating-and-opening-files).
- Lass einen Custom File Browser das gesamte Dateisystem zugänglich machen, auch wenn er mit einem relevanten Ort startet (hig:file-management#Creating-and-opening-files).
- Sichere automatisch und periodisch sowie beim Schließen und App-Wechsel; vermeide explizite Speicherzwänge (hig:file-management#Saving-work).
- Blende Dateiendungen standardmäßig aus, mache sie aber einblendbar und konsistent in allen Open/Save-Dialogen (hig:file-management#Saving-work).
- Nutze einen Quick-Look-Viewer für nicht unterstützte Dateien und einen Quick-Look-Generator für eigene Dateitypen (hig:file-management#Quick-Look-previews).

**Plattform-Unterschiede**
- iOS/iPadOS (ab 18): Document Launcher (`DocumentGroupLaunchScene`) mit Title Card (App-Name + Primär-/Sekundärbutton), Hintergrund + Accessories, Sheet mit File Browser. Primärbutton = neues Dokument; Hintergrund klar abgesetzt und ruhig; Accessories nicht überladen und auf allen Größen/Orientierungen testen; Animation sparsam (hig:file-management#Document-launcher).
- iOS/iPadOS: File Provider Extension – nur kontextpassende Dokumente zeigen, Zielwahl beim Export/Verschieben, keine eigene obere Toolbar (Modal hat bereits eine) (hig:file-management#File-provider-app-extension).
- macOS: Standard-Dateibrowser bevorzugen; Custom-Open mit "open recent", Filter, Mehrfachauswahl, umbenennbarem Open-Button; Save-Dialog für Name/Format/Ort (Default "Untitled"), ggf. Accessory View (hig:file-management#Custom-file-management).
- macOS: Finder Sync Extension für Sync-Status-Badges, Kontextmenüs, Toolbar-Buttons. Bei deaktiviertem Autosave ("Ask to keep changes when closing documents"): ungesicherte Änderungen per Punkt im Close-Button und im Window-Menü anzeigen und beim Schließen/Beenden Save-Dialog zeigen; bei aktivem Autosave kein Punkt. Suffix "Edited" im Titel nach Sicherung entfernen (hig:file-management#Finder-Sync-extensions).
- watchOS: kein Dokument-Browsing im System; keine zusätzlichen Hinweise.

## Going full screen

**Zweck:** Ablenkungsfreie Vollbilddarstellung auf iPhone, iPad und Mac (Spiele, Medien, vertiefte Aufgaben) (hig:going-full-screen).

**Kernregeln**
- Biete Vollbild an, wenn es der Erfahrung dient (hig:going-full-screen#Best-practices).
- Passe das Layout im Vollbild dezent an, ändere die Fenstergröße aber nicht programmatisch (hig:going-full-screen#Best-practices).
- Halte essenzielle Controls erreichbar (z. B. Playback-Controls dauerhaft oder leicht einblendbar) (hig:going-full-screen#Best-practices).
- Lass außer in Spielen das Dock in iPadOS/macOS erreichbar (hig:going-full-screen#Best-practices).
- Pausiere beim Wegwechseln und setze beim Zurückkehren fort (hig:going-full-screen#Best-practices).
- Lass Nutzer entscheiden, wann sie Vollbild verlassen; kein automatisches Beenden (hig:going-full-screen#Best-practices).
- Blende Toolbars/Navigation temporär aus, wenn Inhalt im Fokus steht; Wiederherstellen per Tippen, Swipe nach unten oder Cursor oben; essenzielle Controls sichtbar lassen (hig:going-full-screen#Best-practices).

**Plattform-Unterschiede**
- iOS/iPadOS: Home-Indicator-Verhalten möglichst beibehalten; nur bei ungewollten Exits zwei Swipes verlangen (`preferredScreenEdgesDeferringSystemGestures`). iPadOS-Spiele können ersten Swipe vom unteren Rand ignorieren lassen (hig:going-full-screen#iOS-iPadOS).
- macOS: System-Vollbild nutzen (`toggleFullScreen(_:)`, berücksichtigt Kameragehäuse); in Spielen Display-Modus nicht ändern; Eintritt nur durch Nutzer (Fensterbutton, View-Menü, Control-Command-F), kein eigenes Fenstermodus-Menü; in Spielen optional Toggle; Dock in Spielen per `hideDock` ausblendbar (hig:going-full-screen#macOS).
- watchOS: nicht unterstützt (Apps füllen ohnehin den Bildschirm). tvOS/visionOS: nicht unterstützt.

## Launching

**Zweck:** Vom Öffnen (inkl. Initial-Download) bis zum ersten bereiten Screen; Onboarding folgt danach (hig:launching).

**Kernregeln**
- Starte sofort; Nutzer wollen teils nicht länger als ein paar Sekunden warten (hig:launching#Best-practices).
- Stelle einen Launch Screen bereit, wo die Plattform ihn verlangt (iOS, iPadOS, tvOS) (hig:launching#Best-practices).
- Zeige einen Splash Screen, falls nötig, am Anfang des Onboardings bzw. direkt nach dem Launch (hig:launching#Best-practices).
- Stelle den vorherigen Zustand granular wieder her (Scrollposition, Fensterzustand und -position) (hig:launching#Best-practices).
- Gestalte den Launch Screen fast identisch zum ersten Screen (gleiche Grundfarbe, Orientierung, Appearance Mode) – kein Onboarding, kein Splash, keine Kunst (hig:launching#Launch-screens).
- Vermeide Text im Launch Screen (wird nicht lokalisiert) (hig:launching#Launch-screens).
- Mache keine Werbung; Logos nur, wenn sie fester Teil des ersten Screens sind (hig:launching#Launch-screens).

**Plattform-Unterschiede**
- iOS/iPadOS: In aktueller Geräteorientierung starten; bei nur einer Orientierung in dieser starten; Landscape-only muss links- wie rechtsgedreht korrekt reagieren (hig:launching#iOS-iPadOS).
- macOS, watchOS: kein Launch Screen nötig, keine zusätzlichen Hinweise.
- tvOS: Launch Screen statisch; Live-Viewing-Apps können nach einigen Sekunden Inaktivität automatisch abspielen. visionOS: auch voll immersive Apps im Shared Space starten.

## Live-viewing apps

**Zweck:** Live-Inhalte priorisieren und klar von VOD unterscheiden; inhaltlich stark auf TV-Erfahrungen ausgerichtet (hig:live-viewing-apps).

**Kernregeln**
- Platziere Live-Inhalte prominent, z. B. im ersten Tab (hig:live-viewing-apps#Best-practices).
- Starte Wiedergabe mit höchstens einem Tap (z. B. Watch-Now-Button, der beim Tippen verschwindet) (hig:live-viewing-apps#Best-practices).
- Kennzeichne Live-Inhalte (Badge, Symbol, Sash, Zeile "Live") und zeige ggf. den Fortschritt laufender Sendungen (hig:live-viewing-apps#Best-practices).
- Halte Wiedergabe als Primäraktion; weitere Aktionen in stets gleicher Reihenfolge (z. B. Watch, Start Over, Record, Favorite); weitere Sendetermine anzeigen (hig:live-viewing-apps#Best-practices).
- Nutze ggf. einen Content Footer (abgedunkelt, aktueller Kanal markiert, Kategorien wie im EPG, symmetrisches Ein-/Ausblenden) (hig:live-viewing-apps#Best-practices).
- Gib beim Kanalwechsel sofort visuelles Feedback; passe Audio an den Kontext an (Stopp beim Verlassen des Live-Tabs) (hig:live-viewing-apps#Best-practices).
- EPG: Aktuelles sofort sichtbar, leicht durchblätterbar, vertraute Kategorien, Favoriten, Browsen ohne Wiedergabe-Abbruch (PiP/Hintergrund) (hig:live-viewing-apps#EPG-experience).
- Cloud DVR: Aufnahme aus dem Info-Panel, Einzel-/Serienaufnahme, fein steuerbar, Wiedergabe/Löschen im DVR-Bereich, automatische Speicherverwaltung (hig:live-viewing-apps#Cloud-DVR).

**Plattform-Unterschiede:** keine zusätzlichen Hinweise für iOS, iPadOS, macOS, watchOS (hig:live-viewing-apps#Platform-considerations).

## Loading

**Zweck:** Laden so gestalten, dass es möglichst unbemerkt bleibt (hig:loading).

**Kernregeln**
- Zeige so früh wie möglich etwas (Platzhalter für Text, Grafik, Animation) (hig:loading#Best-practices).
- Lass Nutzer während des Ladens anderes tun; lade im Hintergrund (hig:loading#Best-practices).
- Biete bei unvermeidbar langem Laden etwas Interessantes (Tipps, neue Features) und schätze die Restzeit realistisch (hig:loading#Best-practices).
- Lade große Assets im Hintergrund per Background Assets (nach Installation, bei Updates, zu unkritischen Zeiten) (hig:loading#Best-practices).
- Kommuniziere Laden mit Progress Indicators: determiniert bei bekannter, indeterminiert bei unbekannter Dauer (hig:loading#Showing-progress).
- Erwäge in Spielen eine eigene, stilpassende Loading-Ansicht (hig:loading#Showing-progress).

**Plattform-Unterschiede**
- watchOS: Loading Indicator möglichst vermeiden; braucht Inhalt "eine oder zwei Sekunden", ist ein Indicator besser als ein leerer Screen (hig:loading#watchOS).
- iOS, iPadOS, macOS: keine zusätzlichen Hinweise.

## Managing accounts

**Zweck:** Accounts nur verlangen, wenn die Kernfunktion es erfordert; dann bevorzugt Sign in with Apple (hig:managing-accounts).

**Kernregeln**
- Erkläre Nutzen und Anmeldeweg kurz in der Sign-in-Ansicht (hig:managing-accounts#Best-practices).
- Verzögere Sign-in so lange wie möglich (z. B. erst beim Kauf) (hig:managing-accounts#Best-practices).
- Nutze ohne Sign in with Apple bevorzugt Passkeys (iOS, iPadOS, macOS, visionOS); bei Passwörtern Zwei-Faktor-Authentifizierung (hig:managing-accounts#Best-practices).
- Benenne die Methode konkret ("Sign In with Face ID") und nur, wenn sie auf dem Gerät verfügbar ist (`LABiometryType`) (hig:managing-accounts#Best-practices).
- Vermeide eine In-App-Option für Biometrie-Opt-in und den Begriff "passcode" (hig:managing-accounts#Best-practices).
- Ermögliche echte Account-Löschung (nicht nur Deaktivierung) in der App oder per direktem, leicht auffindbarem Weblink; gleicher Aufwand in App und Web (hig:managing-accounts#Deleting-accounts).
- Erwäge geplante Löschung, biete aber immer auch sofortige Löschung; informiere über Dauer und Abschluss (hig:managing-accounts#Deleting-accounts).
- Erkläre bei In-App-Purchases, dass Abo-Abrechnung über Apple bis zur Kündigung weiterläuft; Löschung auch unterstützen, wenn das Abo nicht in der App gekauft wurde (hig:managing-accounts#Deleting-accounts).
- Bei Sign in with Apple: Tokens bei Löschung widerrufen (hig:managing-accounts#Deleting-accounts).

**Plattform-Unterschiede**
- watchOS: iCloud-Synchronisation für Keychain-Zugriff (Autofill, Einstellungen) nutzen (hig:managing-accounts#watchOS).
- iOS, iPadOS, macOS: keine zusätzlichen Hinweise.
- tvOS: Anmeldung über anderes Gerät, Shared Accounts mit Profilen, minimale Eingaben; TV Provider: kein Sign-out bei System-Anmeldung, nie über Privacy-Controls abmelden lassen.

## Managing notifications

**Zweck:** Benachrichtigungen nur mit Erlaubnis; Dringlichkeit ehrlich über Interruption Levels abbilden und Focus respektieren (hig:managing-notifications).

**Kernregeln**
- Unterscheide Communication Notifications (direkte Kommunikation, SiriKit-Intents) und Noncommunication Notifications (mit Interruption Level) (hig:managing-notifications#Integrating-with-Focus).
- Wähle das Interruption Level realistisch: Passive, Active (Default), Time Sensitive, Critical (hig:managing-notifications#Integrating-with-Focus).
- Beachte: Time Sensitive und Critical übergehen Scheduled Delivery und Focus; nur Critical übergeht den Ring/Silent-Schalter und erfordert ein Entitlement (hig:managing-notifications#Integrating-with-Focus).
- Nutze Time Sensitive nur für Ereignisse, die jetzt oder innerhalb einer Stunde stattfinden; das System fragt Nutzer periodisch, ob sie es beibehalten wollen (hig:managing-notifications#Best-practices).
- Sende Marketing nur nach explizitem Opt-in (eigene Abfrage mit klarer Ja/Nein-Option) und nie als Time Sensitive (hig:managing-notifications#Sending-marketing-notifications).
- Biete einen In-App-Settings-Screen, um Benachrichtigungsentscheidungen zu ändern (hig:managing-notifications#Sending-marketing-notifications).

**Plattform-Unterschiede**
- watchOS: iPhone-Einstellungen gelten standardmäßig auch auf der Watch; Verwaltung in der Watch-App, per Links-Swipe Optionen wie "Mute 1 Hour" oder "Turn off Time Sensitive" (hig:managing-notifications#watchOS).
- iOS, iPadOS, macOS: keine zusätzlichen Hinweise.

## Modality

**Zweck:** Inhalt in einem eigenen Modus, der die Elternansicht blockiert und eine explizite Aktion zum Schließen verlangt (Alert, Sheet, Popover, Action Sheet/Confirmation Dialog, Activity View, Vollbild-Modal) (hig:modality).

**Kernregeln**
- Präsentiere modal nur bei klarem Nutzen (Fokus oder Entscheidungen über Inhalte/Gerät) (hig:modality#Best-practices).
- Halte modale Aufgaben einfach, kurz und geradlinig (hig:modality#Best-practices).
- Vermeide eine "App in der App": bei Unteransichten nur ein Pfad, keine Buttons, die wie der Schließen-Button aussehen (hig:modality#Best-practices).
- Erwäge Vollbild-Modal für Medien, Kamera oder mehrstufige Bearbeitung (hig:modality#Best-practices).
- Biete immer einen offensichtlichen Weg zum Schließen gemäß Plattformkonvention (hig:modality#Best-practices).
- Hole bei drohendem Verlust nutzererzeugter Inhalte eine Bestätigung ein (in iOS z. B. Action Sheet mit Save-Option) – egal ob Geste oder Button (hig:modality#Best-practices).
- Benenne die Aufgabe per Titel oder Hilfetext (hig:modality#Best-practices).
- Lass ein Modal schließen, bevor ein weiteres erscheint; nie mehr als einen Alert gleichzeitig (Alerts dürfen über anderen Modals liegen) (hig:modality#Best-practices).

**Plattform-Unterschiede**
- iOS, iPadOS, watchOS: Schließen-Button in der oberen Toolbar oder Swipe nach unten erwartet (hig:modality#Best-practices).
- macOS: Schließen-Button im Hauptinhalt erwartet; iPadOS/macOS können statt Modal auch ein eigenes Fenster nutzen (hig:modality).
- Platform considerations: keine zusätzlichen Hinweise (hig:modality#Platform-considerations).

## Multitasking

**Zweck:** Apps müssen mit App-Wechsel, Fenstern, PiP und Unterbrechungen umgehen und Kontext jederzeit sichern/wiederherstellen können (hig:multitasking).

**Kernregeln**
- Pausiere aufmerksamkeitspflichtige Aktivitäten (Spiel, Video) beim Wegwechseln und setze nahtlos fort (hig:multitasking#Best-practices).
- Reagiere auf Audio-Unterbrechungen: bei primären (Musik, Podcast) unbegrenzt pausieren; bei kurzen (Navigationsansage) leiser stellen oder pausieren und danach fortsetzen (hig:multitasking#Best-practices).
- Schließe nutzergestartete Aufgaben ohne weitere Eingabe im Hintergrund ab (hig:multitasking#Best-practices).
- Benachrichtige nur bei wichtigen/zeitkritischen Aufgaben, nicht bei Routine (hig:multitasking#Best-practices).

**Plattform-Unterschiede**
- iOS: FaceTime oder Video in PiP neben anderer App (hig:multitasking#iOS).
- iPadOS: Vollbild- oder Fenster-Apps; Fenster frei skalier- und anordenbar (ähnlich macOS), System-Fenstercontrols für Tiling, Vollbild, Minimieren, Schließen; vorderstes Fenster durch farbige Controls und Schatten markiert; PiP in beiden Modi. Apps erfahren die gewählte Konfiguration nicht – Layout muss sich an alle Größen anpassen (hig:multitasking#iPadOS).
- macOS: Multitasking ist Standard; Fenster-Schatten und Fensterzustände (hig:multitasking#macOS).
- watchOS: nicht unterstützt (hig:multitasking#Platform-considerations).
- visionOS: Fensterkanten nicht verändern, Video beim Wegschauen nicht pausieren, mit Audio-Ducking rechnen. tvOS: PiP.

## Offering help

**Zweck:** Kontextbezogene Hilfe, Tips (TipKit) und Tooltips, wenn die Oberfläche allein nicht reicht (hig:offering-help).

**Kernregeln**
- Richte Hilfe an der Aufgabe aus: Inline-Erklärung für ein bis zwei Schritte, Tutorial für komplexe Ziele; leicht ignorier- und schließbar (hig:offering-help#Best-practices).
- Verwende kontext- und plattformkorrekte Sprache/Bilder (kein "click" auf iPhone, kein "tap" auf Mac) (hig:offering-help#Best-practices).
- Halte Hilfe inklusiv; erkläre keine Standardkomponenten, sondern deren Funktion in deiner App (hig:offering-help#Best-practices).
- Wähle den Tip-Typ: Popover Tip (Inhaltsfluss erhalten) oder Inline Tip (Umgebung sichtbar); annotation-style für konkretes UI-Element, hint-style ohne Bezug (hig:offering-help#Creating-tips).
- Nutze Tips nur für einfache Features; mehr als drei Aktionen sind für einen Tip zu komplex (hig:offering-help#Creating-tips).
- Formuliere Tips in ein bis zwei Sätzen, handlungsorientiert, ohne Werbung (hig:offering-help#Creating-tips).
- Steuere Zielgruppe per Parameter-/Event-Regeln und Frequenz (Beispiel: einmal alle 24 Stunden) (hig:offering-help#Creating-tips).
- Nutze bekannte Symbole in gefüllter Variante, aber nicht doppelt zum UI-Element; Buttons führen zu Settings oder weiterführenden Infos (hig:offering-help#Creating-tips).

**Plattform-Unterschiede**
- macOS (auch iPhone/iPad-Apps auf dem Mac): Tooltips (`help(_:)`) beim Verweilen des Pointers. Nur das angezeigte Control beschreiben, mit Verb beginnen, Control-Namen nicht wiederholen, maximal 60–75 Zeichen, Sentence Case, ggf. zustandsabhängiger Text (hig:offering-help#macOS-visionOS).
- iOS, iPadOS, watchOS: keine zusätzlichen Hinweise. visionOS: Tooltips auch per Blick.

## Onboarding

**Zweck:** Schneller, unterhaltsamer, optionaler Einstieg nach dem Launch – nicht Teil davon (hig:onboarding).

**Kernregeln**
- Lehre interaktiv statt durch reines Anschauen (hig:onboarding#Best-practices).
- Erwäge kontextbezogene Tips statt eines einzelnen Onboarding-Flows; Hinweise nahe am betroffenen UI-Bereich (hig:onboarding#Best-practices).
- Halte einen Pflicht-Flow kurz und ohne Merkzwang (hig:onboarding#Best-practices).
- Mache Tutorials optional; nach Überspringen nicht erneut zeigen, aber in Hilfe/Account/Settings auffindbar halten (hig:onboarding#Best-practices).
- Fokussiere auf deine App, nicht auf System- oder Gerätebedienung (hig:onboarding#Best-practices).
- Zeige einen Splash Screen nur kurz, gerade lang genug für einen Blick (hig:onboarding#Additional-content).
- Lass große Downloads das Onboarding nicht blockieren; Lizenztexte dem App Store überlassen (hig:onboarding#Additional-content).
- Verschiebe nicht-essenzielles Setup; wähle sinnvolle Defaults (hig:onboarding#Additional-requests).
- Integriere Berechtigungsanfragen ins Onboarding nur, wenn die App sonst nicht funktioniert; sonst beim ersten Zugriff auf die Funktion (hig:onboarding#Additional-requests).
- Frage nach Bewertungen oder Käufen erst nach echter Nutzung (hig:onboarding#Additional-requests).

**Plattform-Unterschiede:** keine zusätzlichen Hinweise (hig:onboarding#Platform-considerations).

## Playing audio

**Zweck:** Audio muss sich erwartungskonform zu Lautstärke, Stummschaltung, Kopfhörern und Ausgabegerät verhalten (hig:playing-audio).

**Kernregeln**
- Respektiere Silent-Modus: dann nur explizit gestartetes Audio (Medien, Wecker, Calls) (hig:playing-audio).
- Pausiere sofort beim Trennen von Kopfhörern; route beim Verbinden ohne Unterbrechung um (hig:playing-audio).
- Passe nur relative Pegel an, nie die Systemlautstärke (hig:playing-audio#Best-practices).
- Erlaube Audio-Rerouting (AirPlay, Bluetooth) und nutze die System-Volume-View `MPVolumeView` (hig:playing-audio#Best-practices).
- Wähle die passende `AVAudioSession.Category`: Solo ambient, Ambient (beide reagieren auf Silent, kein Hintergrund), Playback, Record, Play and record (ignorieren Silent, Hintergrund möglich) (hig:playing-audio#Best-practices).
- Reagiere auf externe Audio-Controls nur in klarem Audio-Kontext; definiere Controls nicht um; Custom-Player nur für vom System nicht unterstützte Befehle (hig:playing-audio#Best-practices).
- Signalisiere das Ende temporären Audios (`notifyOthersOnDeactivation`) (hig:playing-audio#Best-practices).
- Entscheide bewusst über Unterbrechungsverhalten; z. B. darf eine VoIP-App beim Schließen des Smart Folio das Mikrofon nicht unbemerkt reaktivieren (hig:playing-audio#Handling-interruptions).
- Prüfe nach Unterbrechung `shouldResume` (Medien-Apps); Spiele dürfen automatisch fortsetzen (hig:playing-audio#Handling-interruptions).

**Plattform-Unterschiede**
- iOS/iPadOS: kurze Sounds und Vibrationen über System Sound Services (Audio Services) (hig:playing-audio#iOS-iPadOS).
- macOS: Notification-Sounds mischen sich standardmäßig mit anderem Audio (hig:playing-audio#macOS).
- watchOS: System verwaltet Wiedergabe; kurze Clips im Vordergrund oder längeres Background-Audio; Encoding 64 kbps HE-AAC; Now-Playing-View erwägen (hig:playing-audio#watchOS).
- visionOS: Sound bevorzugen, Spatial Audio, fixed vs. tracked Sound; wichtige Infos nie nur über Ton. tvOS: Audio nur bei Nutzerinitiierung.

## Playing haptics

**Zweck:** Haptik ergänzt visuelles und akustisches Feedback und schafft klare Ursache-Wirkung-Bezüge (hig:playing-haptics).

**Kernregeln**
- Nutze System-Haptikmuster nur gemäß dokumentierter Bedeutung; sonst generisches oder eigenes Muster (hig:playing-haptics#Best-practices).
- Setze Haptik konsistent ein (gleiches Muster nicht für Erfolg und Misserfolg) (hig:playing-haptics#Best-practices).
- Stimme Haptik mit Animation und Ton ab (Intensität, Schärfe) (hig:playing-haptics#Best-practices).
- Vermeide Überbenutzung; in Apps kurze Haptik für diskrete Ereignisse statt Dauervibration (z. B. bei Apple Pencil Pro) (hig:playing-haptics#Best-practices).
- Mache Haptik abschaltbar; App muss ohne sie funktionieren (hig:playing-haptics#Best-practices).
- Achte auf Störungen von Kamera, Gyroskop, Mikrofon (hig:playing-haptics#Best-practices).
- Baue Custom Haptics (Core Haptics) aus Transient- und Continuous-Events mit Sharpness und Intensity, optional mit Audio (hig:playing-haptics#Custom-haptics).

**Plattform-Unterschiede**
- iOS: Standard-Controls (Toggle, Slider, Picker) spielen System-Haptik; `UIFeedbackGenerator` mit Kategorien Notification (success, warning, error), Impact (light, medium, heavy, rigid, soft), Selection (hig:playing-haptics#iOS).
- iPadOS: Haptik über Game Controller, Apple Pencil Pro und manche Trackpads an bestimmten iPads (hig:playing-haptics).
- macOS: mit Force Touch/Magic Trackpad die Muster Alignment, Level change, Generic bei Drag oder Force Click (`NSHapticFeedbackPerformer`) (hig:playing-haptics#macOS).
- watchOS: Digital-Crown-Detents ab Apple Watch Series 4; `WKHapticType`-Muster Notification, Up, Down, Success, Failure, Retry, Start, Stop, Click – Click sparsam (hig:playing-haptics#watchOS).

## Playing video

**Zweck:** Systemplayer für vertraute Wiedergabe; Integration mit der TV-App (hig:playing-video).

**Kernregeln**
- Nutze den System-Videoplayer; Custom-Player am Systemverhalten orientieren (hig:playing-video#Best-practices).
- Zeige Video im Originalseitenverhältnis, ohne eingebettetes Letterbox-/Pillarbox-Padding. Defaults: Aspect-fill für 2:1 bis 2.40:1, Aspect (fit) für Standard (4:3, 16:9, bis 2:1) und Ultrawide über 2.40:1 (hig:playing-video).
- Ergänze Metadaten (Bild, Titel, Beschreibung) ohne die Wiedergabe zu verdecken (`externalMetadata`) (hig:playing-video#Best-practices).
- Unterstütze erwartete Eingaben, z. B. Leertaste für Play/Pause (hig:playing-video#Best-practices).
- Verhindere Audio-Mischung beim Moduswechsel (PiP) über korrektes Secondary-Audio-Handling (`silenceSecondaryAudioHintNotification`) (hig:playing-video#Best-practices).
- TV-App: eigener schwarzer Screen als Übergang, Inhalt sofort zeigen, Fortsetzen ohne Rückfrage an vorheriger Endzeit, korrektes Profil, Leertaste unterstützt (hig:playing-video#Integrating-with-the-TV-app).
- Loading: Ladebildschirm vermeiden; dauert Laden mehr als zwei Sekunden, schwarzer Screen mit zentriertem Spinner; nur bis zum Wiedergabestart (hig:playing-video#Loading-content).
- Nach Beenden: kontextrelevante Detailansicht mit Fortsetzen-Option; Exit-View früh vorbereiten (hig:playing-video#Exiting-playback).

**Plattform-Unterschiede**
- iOS, iPadOS, macOS: keine zusätzlichen Hinweise (hig:playing-video#Platform-considerations).
- watchOS: Clips nur im Vordergrund, höchstens 30 Sekunden; nicht skalieren; Encoding H.264 High Profile, 160 kbps bei bis zu 30 fps, 208x260 px (Hochformat, Vollbild) bzw. 320x180 px (16:9, Querformat), Audio 64 kbps HE-AAC; Poster Image inhaltsbezogen und nicht wie ein Control (hig:playing-video#watchOS).
- tvOS: Overlays dezent; interaktive Overlays mit mindestens 0,5 s Verzögerung. visionOS: Komfort, keine automatisch startende Vollimmersion, Thumbnail-Track mit 160 px Breite.

## Printing

**Zweck:** Systemdruck integrieren und nur relevante Optionen zeigen (hig:printing).

**Kernregeln**
- Mache Drucken auffindbar: macOS im File-Menü, iOS/iPadOS über Toolbar-Button mit Action Sheet (hig:printing#Best-practices).
- Biete Drucken nur an, wenn möglich; sonst Menüeintrag dimmen bzw. Aktion entfernen, Custom-Button dimmen oder ausblenden (hig:printing#Best-practices).
- Zeige Optionen (Seitenbereich, Kopien, Duplex) über die Systemansicht, sofern Drucker sie unterstützt (hig:printing#Best-practices).

**Plattform-Unterschiede**
- macOS: Druck-Button in der Toolbar optional (anpassbar); eigene Print-Panel-Kategorie für App-spezifische Optionen; Page-Setup-Dialog nur für dokumentspezifische Einstellungen ohne Systemfunktionen zu duplizieren; Abhängigkeiten klar machen; erweiterte Optionen per Disclosure als "Advanced Options"; Vorschau von Einstellungen; Einstellungen mindestens bis zum Schließen des Dokuments speichern (hig:printing#macOS).
- iOS, iPadOS: keine zusätzlichen Hinweise. watchOS: nicht unterstützt (ebenso tvOS).

## Ratings and reviews

**Zweck:** Bewertungsanfragen zum richtigen Zeitpunkt; App Store ermöglicht Bewertung jederzeit (hig:ratings-and-reviews).

**Kernregeln**
- Frage erst nach nachgewiesenem Engagement (abgeschlossener Level/Task), nie beim ersten Start oder im Onboarding (hig:ratings-and-reviews#Best-practices).
- Unterbrich keine laufende Aufgabe; nutze natürliche Pausen (hig:ratings-and-reviews#Best-practices).
- Dränge nicht; erwäge mindestens ein bis zwei Wochen Abstand zwischen Anfragen (hig:ratings-and-reviews#Best-practices).
- Bevorzuge den System-Prompt (`RequestReviewAction`); er erscheint höchstens dreimal pro App in 365 Tagen (hig:ratings-and-reviews#Best-practices).
- Wäge das Zurücksetzen der Gesamtbewertung bei neuer Version gegen weniger sichtbare Bewertungen ab (hig:ratings-and-reviews#Best-practices).

**Plattform-Unterschiede:** System-Prompt in iOS, iPadOS, macOS; sonst keine zusätzlichen Hinweise (hig:ratings-and-reviews#Platform-considerations).

## Searching

**Zweck:** Suche in App, Dokument und systemweit (Spotlight); Personalisierung über Verlauf, Vorschläge, Korrekturen; Scopes und Tokens zum Eingrenzen (hig:searching).

**Kernregeln**
- Gib wichtiger Suche eine primäre Position (z. B. Bottom Toolbar wie in Notes oder eigener Tab) (hig:searching#Best-practices).
- Mache Inhalte über einen zentralen Ort durchsuchbar; lokale Suche als Filter nur bei klar getrennten Bereichen (hig:searching#Best-practices).
- Zeige den aktuellen Suchbereich (Placeholder, Scope Bar, Titel) (hig:searching#Best-practices).
- Biete Vorschläge (letzte Suchen, prädiktiv) via `searchSuggestions(_:)` (hig:searching#Best-practices).
- Berücksichtige Privatsphäre bei Suchverlauf und biete Löschen an (hig:searching#Best-practices).
- Mache Inhalte per Metadaten in Spotlight indexierbar; für eigene Dateitypen Spotlight File Importer (`CSImportExtension`) (hig:searching#Systemwide-search).
- Nutze Spotlight für erweiterte Dateisuche in der App; bevorzuge System-Open/Save-Views (mit integrierter Suche); Quick-Look-Generator für eigene Typen (hig:searching#Systemwide-search).

**Plattform-Unterschiede:** Spotlight und Suche in Dokumenten/Fenstern betreffen iOS, iPadOS, macOS; sonst keine zusätzlichen Hinweise (hig:searching#Platform-considerations).

## Settings

**Zweck:** Wenige, gut gewählte Einstellungen; globale Optionen bleiben in der System-Settings-App (hig:settings).

**Kernregeln**
- Wähle Defaults, die für die meisten optimal sind (z. B. Performance automatisch ans Gerät anpassen) (hig:settings#Best-practices).
- Minimiere die Zahl der Einstellungen (hig:settings#Best-practices).
- Öffne Settings auf erwartetem Weg: Command-Komma mit Tastatur, Esc in Spielen (hig:settings#Best-practices).
- Erfrage nichts, was erkennbar ist (Controller, Dark Mode) (hig:settings#Best-practices).
- Dupliziere keine systemweiten Einstellungen (Accessibility, Scrollverhalten, Authentifizierung) (hig:settings#Best-practices).
- Lege selten geänderte, allgemeine Optionen in den eigenen Settings-Bereich (hig:settings#General-settings).
- Biete aufgabenspezifische Optionen (Ein-/Ausblenden, Sortieren, Filtern) direkt im betroffenen Screen an (hig:settings#Task-specific-options).
- Lege nur die seltensten Optionen in die System-Settings-App; ggf. Button, der sie direkt öffnet (hig:settings#System-settings).

**Plattform-Unterschiede**
- macOS: Settings-Item im App-Menü (nicht in der Toolbar); dokumentbezogene Optionen ins File-Menü; Minimize/Maximize dimmen; nicht anpassbare, stets sichtbare Toolbar mit aktivem Pane; Fenstertitel = aktueller Pane bzw. "App Name Settings"; zuletzt genutzten Pane wiederherstellen (hig:settings#macOS).
- watchOS: keine Custom Settings in der System-Settings-App; wenige essenzielle Optionen unten in der Hauptansicht oder per More-Menü (hig:settings#watchOS).
- iOS, iPadOS: keine zusätzlichen Hinweise.

## Undo and redo

**Zweck:** Aktionen umkehrbar machen und Experimentieren erleichtern; Ergebnis vorhersehbar und sichtbar machen (hig:undo-and-redo).

**Kernregeln**
- Mache Ergebnisse vorhersehbar (beschreibende Alert- bzw. Menütexte wie "Undo Typing", "Redo Bold") (hig:undo-and-redo#Best-practices).
- Zeige das Ergebnis, auch außerhalb des sichtbaren Bereichs (z. B. dorthin scrollen) (hig:undo-and-redo#Best-practices).
- Erlaube mehrfaches Undo ohne künstliche Grenzen, mindestens bis zum letzten logischen Schritt (Öffnen, Sichern) (hig:undo-and-redo#Best-practices).
- Erwäge gebündeltes Undo zusammengehöriger Änderungen oder "alles seit Öffnen/Sichern" (hig:undo-and-redo#Best-practices).
- Biete eigene Undo/Redo-Buttons nur bei Bedarf, dann mit System-Symbolen in der Toolbar (hig:undo-and-redo#Best-practices).

**Plattform-Unterschiede**
- iOS/iPadOS: Standardgesten (Drei-Finger-Swipe, Schütteln) nicht umdefinieren; Alert-Titel erhält automatisch Präfix "Undo "/"Redo ", ergänze ein bis zwei beschreibende Wörter (hig:undo-and-redo#iOS-iPadOS).
- macOS: Undo/Redo oben im Edit-Menü; Command-Z und Shift-Command-Z (hig:undo-and-redo#macOS).
- watchOS: nicht unterstützt (ebenso tvOS).

## Workouts

**Zweck:** Fitness-Erlebnisse auf Apple Watch, iPhone und iPad mit Fokus auf aktuelle Aktivität und Fortschritt (hig:workouts).

**Kernregeln**
- Nutze in watchOS Workout Sessions; zeige relevante Daten (Zeit, Kalorien, Distanz) und Controls (Lap, Intervall) (hig:workouts#Best-practices).
- Vermeide Ablenkung durch Irrelevantes während des Trainings (hig:workouts#Best-practices).
- Kennzeichne aktive Workouts visuell eindeutig (live aktualisierte Metriken, eigenes Layout) (hig:workouts#Best-practices).
- Mache Pause/Fortsetzen/Stopp leicht auffindbar und bestätige Start/Stopp klar (hig:workouts#Best-practices).
- Erkläre fehlende Sensordaten (z. B. Herzfrequenz beim Schwimmen) in Workout-App-ähnlicher Sprache (Typen Swimming, Other) (hig:workouts#Best-practices).
- Zeige am Ende eine Zusammenfassung, optional mit Activity Rings (hig:workouts#Best-practices).
- Verwirf extrem kurze Sessions (wenige Sekunden) automatisch oder frage nach (hig:workouts#Best-practices).
- Sorge für Lesbarkeit in Bewegung: große Schrift, hoher Kontrast (hig:workouts#Best-practices).
- Nutze Activity Rings nur für ihren dokumentierten Zweck (hig:workouts#Best-practices).

**Plattform-Unterschiede:** keine zusätzlichen Hinweise für iOS, iPadOS, watchOS; macOS (sowie tvOS, visionOS) nicht unterstützt (hig:workouts#Platform-considerations).

---

## Auffälligkeiten/Unklarheiten

**Widersprüche und Spannungen zwischen Seiten**
- watchOS-Ladeanzeigen: `hig:feedback#watchOS` rät von indeterminierten Indikatoren (explizit inkl. Loading Indicator) ab und empfiehlt den Verweis auf eine Benachrichtigung; `hig:loading#watchOS` hält einen Loading Indicator bei ein bis zwei Sekunden Ladezeit für besser als einen leeren Screen. Auflösung vermutlich über die Dauer (kurz vs. langer Prozess), die Seiten sagen das aber nicht explizit.
- Splash Screen: `hig:launching` und `hig:onboarding` erlauben einen kurzen Splash Screen am Onboarding-Beginn; `hig:playing-video#Integrating-with-the-TV-app` verbietet Splash Screens beim Übergang aus der TV-App. Kontextabhängig, kein echter Widerspruch.
- Workouts: Einleitung nennt Mac und Apple TV für Live-/Aufzeichnungs-Workouts, Platform considerations schließen macOS und tvOS aus (hig:workouts).
- Live-viewing apps: Plattformkopf nennt alle sechs Plattformen inkl. watchOS, Inhalt ist aber durchgehend TV-orientiert (EPG, Cloud DVR, Info-Panel); unklar, wie weit die Regeln für iOS/macOS/watchOS gelten (hig:live-viewing-apps).
- File management: Plattformkopf nennt tvOS und watchOS, der Text sagt, dass diese Systeme kein Dokument-Browsing bieten (hig:file-management).
- Going full screen: Plattformkopf nur iOS, iPadOS, macOS, Best Practice erwähnt trotzdem visionOS-Fenster mit ausblendbaren Toolbars (hig:going-full-screen).

**Doppelungen**
- Quick-Look-Generator für eigene Dateitypen steht sowohl in `hig:file-management#Quick-Look-previews` als auch in `hig:searching#Systemwide-search`.
- Audio-Unterbrechungen: `hig:multitasking#Best-practices` und `hig:playing-audio#Handling-interruptions` behandeln dasselbe Thema mit unterschiedlicher Tiefe.

**Update-Vermerke (Kopfzeile der Seiten)**
- 2026-06-08 searching: Terminologie aktualisiert, Best Practices verfeinert (jüngster Vermerk; Vorversion 2025-06-09 übernahm Inhalte aus Search fields).
- 2025-06-09 going-full-screen: Ausblenden von Toolbars/Navigation, Aufschieben von Home-Indicator-Gesten.
- 2025-06-09 loading: Hintergrund-Download großer Assets (Background Assets).
- 2025-06-09 multitasking: Plattformteil neu gegliedert, iPadOS-Mehrfenster-Multitasking ergänzt.
- 2024-06-10 file-management (Document Launcher), launching (Splash Screen), onboarding (Ansätze, Splash Screen), settings (Neugliederung, Spielbeispiele).
- 2024-05-07 playing-haptics: Apple Pencil Pro.
- 2023-12-05 collaboration-and-sharing (Artwork), modality (Vollbild-Modals, mehrere Modals), offering-help (visionOS-Tooltips).
- 2023-10-24 drag-and-drop, 2023-09-12 ratings-and-reviews (jeweils nur Artwork); 2023-09-12 playing-video (Thumbnail-Breite visionOS korrigiert); 2023-06-21 entering-data, playing-audio (visionOS).
- Ohne Update-Vermerk: patterns, charting-data, feedback, live-viewing-apps, managing-accounts, managing-notifications, printing, undo-and-redo, workouts. live-viewing-apps, managing-accounts, managing-notifications, printing, undo-and-redo, workouts und feedback haben auch keinen Change log.

**Fehlende Infos**
- `hig:playing-video#Best-practices` verweist auf "Keyboards and Remotes" ohne Link.
- `hig:entering-data#macOS` verlinkt Offering help per Web-URL statt `hig:`-Slug.
- Keine konkreten Zeit- oder Mengenangaben für Autosave-Intervalle, Undo-Tiefe oder Splash-Screen-Dauer; nur qualitative Vorgaben.
- Modality nennt Schließkonventionen (Toolbar-Button/Swipe vs. Button im Inhalt), Platform considerations melden aber "keine zusätzlichen Hinweise"; die Plattformregeln stehen also nur im Best-Practice-Teil.
