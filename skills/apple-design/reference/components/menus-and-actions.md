# Menus and actions – Komponenten

> Quelle: Apple HIG, lokaler Spiegel (Stand 2026-10-21). Paraphrasiert. Belege: `(hig:<slug>)`, `(hig:<slug>#Anchor)`.

Komponenten, mit denen Nutzer Aktionen auslösen: direkt (Button, Toolbar-Item), über ausklappbare Menüs (Pop-up, Pull-down, Context, Edit, Menu bar, Dock) oder systemweit (Share Sheet, Home Screen quick actions). Grundregel quer über alle: Menü-Befehle sind Abkürzungen – jede Funktion muss auch im Haupt-UI bzw. in der Menüleiste erreichbar sein (hig:context-menus#Best-practices) (hig:toolbars#macOS).

Inhalt: [Activity views](#activity-views) · [Buttons](#buttons) · [Context menus](#context-menus) · [Dock menus](#dock-menus) · [Edit menus](#edit-menus) · [Home Screen quick actions](#home-screen-quick-actions) · [Menus](#menus) · [Ornaments](#ornaments) · [Pop-up buttons](#pop-up-buttons) · [Pull-down buttons](#pull-down-buttons) · [The menu bar](#the-menu-bar) · [Toolbars](#toolbars)

---

## Activity views

**Zweck:** Systemweites „Share Sheet“, das Teilen- und Aktions-Aktivitäten (Nachricht, Kopieren, Drucken, App-Aktionen) für den aktuellen Kontext anbietet. **Plattformen:** ios, ipados (visionos); nicht unterstützt in macOS, tvOS, watchOS – auf dem Mac stattdessen Share-/Action-Extensions (hig:activity-views).

**Verwenden, wenn:** Inhalte geteilt oder an andere Apps/Dienste übergeben werden sollen; eigene, app-spezifische Aktionen kontextbezogen ergänzt werden sollen. **Nicht verwenden, wenn:** man eine eigene Teilen-UI parallel zum System bauen will oder Systemaktionen (z. B. Print) dupliziert.

**Kernregeln:**
- Systemaktionen nicht duplizieren; ähnliche eigene Aktion klar abgrenzend benennen (z. B. „Print Transaction“) (hig:activity-views#Best-practices).
- Eigene Aktivität mit SF Symbol darstellen (hig:activity-views#Best-practices).
- Aktionstitel kurz, verbbasiert, ohne Firmen-/Produktnamen (hig:activity-views#Best-practices).
- Nicht passende Systemaktivitäten ausschließen; Reihenfolge der Systemaktionen ist nicht änderbar (hig:activity-views#Best-practices).
- Activity view über den Share-Button öffnen, keinen alternativen Weg erfinden (hig:activity-views#Best-practices).
- Extensions: Interaktion auf wenige Schritte begrenzen, keine weiteren Modals über der Extension (Alert ausgenommen) (hig:activity-views#Share-and-action-extensions).
- Für Share-Extensions die System-Composition-View bevorzugen; Action-Extensions mit App-Namen kennzeichnen (hig:activity-views#Share-and-action-extensions).
- Lange Vorgänge im Hintergrund fortsetzen, Status in der Haupt-App zeigen; nicht bloß zur Fertigmeldung benachrichtigen (hig:activity-views#Share-and-action-extensions).

**Plattform-Besonderheiten:**
- iOS/iPadOS: Erscheint je nach Gerät/Ausrichtung als Sheet oder Popover (hig:activity-views).
- macOS: Kein Activity view; Share-Extensions über Share-Button in Toolbar oder Context menu, Action-Extensions über Hover auf Inhalt, Toolbar-Button oder Finder Quick Action (hig:activity-views#Share-and-action-extensions).

**Kennwerte:** Eigenes Interface-Icon in einem Bereich von ca. 70×70 px zentrieren (hig:activity-views#Best-practices).

**Umsetzung:** UIKit `UIActivityViewController`, `UIActivity`; Foundation App Extension Support (hig:activity-views). SwiftUI: `ShareLink` (nicht im Spiegel genannt).

**Typische Fehler:**
- Eigener „Drucken“-Eintrag neben dem System-Print.
- Eigenes Teilen-Icon/-Menü statt Share-Button.
- Benachrichtigung nur weil eine Extension-Aufgabe fertig ist.

---

## Buttons

**Zweck:** Löst eine sofortige Aktion aus; definiert durch Style, Content und Role. **Plattformen:** ios, ipados, macos, watchos (tvos, visionos) (hig:buttons).

**Verwenden, wenn:** eine einzelne, unmittelbare Aktion angeboten wird. **Nicht verwenden, wenn:** Zustand umgeschaltet (→ Toggle), aus Optionen gewählt (→ Pop-up button / Segmented control) oder ein Menü von Aktionen gezeigt werden soll (→ Pull-down button) (hig:buttons).

**Kernregeln:**
- Ausreichend Abstand und Trefferfläche vorsehen (siehe Kennwerte) (hig:buttons#Best-practices).
- Eigene Buttons immer mit Press-State (hig:buttons#Best-practices).
- Prominenten Stil für die wahrscheinlichste Aktion; höchstens ein bis zwei prominente Buttons pro View (hig:buttons#Style).
- Bevorzugte Option über Stil, nicht über Größe hervorheben; Optionen eines Sets gleich groß (hig:buttons#Style).
- Button-Label-Farbe nicht an farbige Content-Hintergründe angleichen; bei buntem Content monochrome Labels (Liquid Glass) (hig:buttons#Style).
- Bekannte Aktionen mit bekannten Symbolen; Text in Title-Case, möglichst mit Verb beginnend („Add to Cart“) (hig:buttons#Content).
- Rollen nutzen: normal, primary (Default, Accent color, reagiert auf Return), cancel, destructive (System-Rot) (hig:buttons#Role).
- Primary-Rolle nie einer destruktiven Aktion geben, selbst wenn sie die wahrscheinlichste ist (hig:buttons#Role).

**Plattform-Besonderheiten:**
- iOS/iPadOS: Button kann für verzögerte Aktionen einen Activity indicator plus alternativen Label-Text zeigen („Checking out…“) (hig:buttons#iOS-iPadOS).
- macOS: *Push button* = Standard, kann Default-Button sein; Flexible-height nur für hohen/mehrzeiligen Inhalt; Titel mit Ellipse, wenn weiteres Fenster/View öffnet; Spring loading erwägen (hig:buttons#Push-buttons). *Square (gradient) buttons*: nur Symbole, nur in Views (nicht Toolbar/Statusleiste), ohne einführendes Label (hig:buttons#Square-buttons). *Help button*: System-Help-Button, max. einer pro Fenster, kontextbezogenes Hilfethema; in Dialogen mit Dismiss-Buttons in der unteren Ecke gegenüber, sonst unten links/rechts (hig:buttons#Help-buttons). *Image buttons*: nur in Views, Label darunter (hig:buttons#Image-buttons).
- visionOS: Formen circle (nur Icon), roundedRectangle/capsule (Text), capsule (Icon+Text); keine Custom-Hover-Effekte; Weiß-Fläche mit schwarzem Inhalt ist für den Toggled-State reserviert; in vertikalen Stacks rounded rectangle, in Reihen capsule (hig:buttons#visionOS).
- watchOS: Inline-Buttons immer capsule; Ecken-Buttons über Toolbar (Liquid Glass); Primäraktionen bildschirmbreit; gleiche Höhe bei nebeneinander/übereinander stehenden Buttons (hig:buttons#watchOS).
- tvOS: keine zusätzlichen Hinweise.

**Kennwerte:**
- Trefferfläche mind. 44×44 pt; visionOS 60×60 pt (hig:buttons#Best-practices).
- macOS Image button: ca. 10 px Padding zwischen Bild und Button-Kante (hig:buttons#Image-buttons).
- visionOS-Größen: Mini 28 pt, Small 32 pt, Regular 44 pt, Large 52 pt, Extra large 64 pt; Mittelpunkte mind. 60 pt auseinander; ab 60 pt Buttongröße 4 pt Padding (hig:buttons#visionOS).

**Umsetzung:** SwiftUI `Button` (Rollen via `ButtonRole`, Stile via `buttonStyle`, visionOS-Formen via `ButtonBorderShape`); UIKit `UIButton`; AppKit `NSButton` (`BezelStyle.flexiblePush`, `.smallSquare`, `isBordered`) (hig:buttons).

**Typische Fehler:**
- Mehrere prominente Buttons konkurrieren in einer View.
- „Löschen“ als Default-/Primary-Button.
- Bevorzugte Option nur größer statt anders gestylt.
- Square/Image/Help buttons in die Toolbar gesetzt (macOS).

---

## Context menus

**Zweck:** Verstecktes Menü mit den wichtigsten, direkt auf ein Element bezogenen Befehlen. **Plattformen:** ios, ipados, macos (tvos, visionos); nicht unterstützt in watchOS (hig:context-menus).

**Verwenden, wenn:** häufige, objektbezogene Befehle schnell erreichbar sein sollen, ohne UI zu überladen. **Nicht verwenden, wenn:** Befehle selten/fortgeschritten sind oder nur dort existieren würden – Context menus sind nie der einzige Zugang (hig:context-menus#Best-practices).

**Kernregeln:**
- Nur relevante, häufige Befehle; wenige Einträge (hig:context-menus#Best-practices).
- Konsistent in der ganzen App anbieten (hig:context-menus#Best-practices).
- Jeden Eintrag auch im Haupt-UI (Toolbar, Menüleiste) verfügbar machen (hig:context-menus#Best-practices).
- Submenüs höchstens eine Ebene tief (hig:context-menus#Best-practices).
- Nicht verfügbare Einträge ausblenden statt dimmen (macOS-Ausnahme: Cut/Copy/Paste) (hig:context-menus#Best-practices).
- Häufigste Einträge nahe dem Auslösepunkt; ggf. Reihenfolge umkehren, wenn das Menü oberhalb öffnet (hig:context-menus#Best-practices).
- Keine Tastaturkürzel anzeigen; max. ca. drei Gruppen (hig:context-menus#Best-practices).
- Destruktive Einträge (iOS/iPadOS/visionOS) ans Ende, als destructive markieren (hig:context-menus#Best-practices).
- Titel nur, wenn er die Wirkung klärt (z. B. Anzahl ausgewählter Elemente); System-Icons für Standardaktionen (hig:context-menus#Content).

**Plattform-Besonderheiten:**
- iOS/iPadOS: Entweder Context menu oder Edit menu pro Element, nicht beide; iPadOS: Context menu auch zum Anlegen neuer Objekte im Leerraum; Vorschau (Preview) sinnvoll gestalten, Clipping-Pfad an Form der Vorschau anpassen (hig:context-menus#iOS-iPadOS).
- macOS: heißt dort auch *contextual menu* (hig:context-menus#macOS).
- visionOS: statt Panel/Inspector erwägen; Menühöhe möglichst nicht über Fensterhöhe (hig:context-menus#visionOS).

**Kennwerte:** „nicht mehr als etwa drei Gruppen“ (hig:context-menus#Best-practices); sonst keine.

**Umsetzung:** SwiftUI `contextMenu(menuItems:)`; UIKit `UIContextMenuInteraction` (+ `UIContextMenuInteractionDelegate` für Preview), `UIMenuElement.Attributes.destructive`; AppKit `NSMenu.popUpContextMenu(_:with:for:)` (hig:context-menus).

**Typische Fehler:**
- Funktionen exklusiv im Context menu.
- Gedimmte statt ausgeblendete Einträge.
- Shortcuts im Context menu.
- Context und Edit menu am selben Element (iOS).

---

## Dock menus

**Zweck:** Menü per Sekundärklick auf das App-Icon im Dock mit System- und eigenen Einträgen. **Plattformen:** macos; nicht unterstützt in iOS, iPadOS, tvOS, visionOS, watchOS (Pendant iOS/iPadOS: Home Screen quick actions) (hig:dock-menus).

**Verwenden, wenn:** hochwertige Aktionen nützlich sind, während die App nicht vorne ist oder kein Fenster offen hat (z. B. Neue Nachricht, offene Fenster). **Nicht verwenden, wenn:** der Befehl sonst nirgends erreichbar wäre.

**Kernregeln:**
- Einträge knapp benennen, logisch ordnen (allgemeine Menüregeln) (hig:dock-menus#Best-practices).
- Eigene Dock-Einträge auch in Menüleiste oder UI anbieten (hig:dock-menus#Best-practices).
- Nur wertvolle Einträge: offene/zuletzt geöffnete Fenster, wenige Aktionen für den Hintergrundfall (hig:dock-menus#Best-practices).
- Keine Dynamic menu items (Modifier-Varianten) im Dock menu (hig:the-menu-bar#Dynamic-menu-items).

**Plattform-Besonderheiten:** nur macOS.

**Kennwerte:** keine im Spiegel.

**Umsetzung:** AppKit `NSApplicationDelegate.applicationDockMenu(_:)` (hig:dock-menus).

**Typische Fehler:** Dock menu als einziger Zugang zu einer Funktion; überfrachtetes Dock menu mit Alltagsbefehlen.

---

## Edit menus

**Zweck:** Bearbeitungsbefehle (Copy, Paste, Select, Translate, Look Up …) für ausgewählten Inhalt in der aktuellen View. **Plattformen:** ios, ipados, macos (visionos); nicht unterstützt in tvOS, watchOS (hig:edit-menus).

**Verwenden, wenn:** Text oder andere auswählbare Inhalte (Bilder, Dateien, Kontakte, Orte) bearbeitet/kopiert werden. **Nicht verwenden, wenn:** man ein eigenes Menü mit denselben Standardbefehlen bauen will.

**Kernregeln:**
- System-Edit-Menu verwenden, kein Custom-Nachbau (hig:edit-menus#Best-practices).
- Mit den bekannten Systemgesten öffnen (Touch and hold, Pinch and hold, Sekundärklick) (hig:edit-menus#Best-practices).
- Nur zum Kontext passende Befehle; z. B. kein Copy ohne Auswahl, kein Paste bei leerer Zwischenablage (hig:edit-menus#Best-practices).
- Eigene Befehle neben verwandte Systembefehle setzen, sparsam (hig:edit-menus#Best-practices).
- Kopieren nicht editierbaren Inhaltstexts erlauben, nicht aber von Control-Labels (hig:edit-menus#Best-practices).
- Undo/Redo unterstützen, da keine Bestätigung erfolgt (hig:edit-menus#Best-practices).
- Keine redundanten Controls für Edit-Funktionen; Delete vs. Cut klar unterscheiden (hig:edit-menus#Best-practices).
- Eigene Befehle kurz, verbbasiert benennen (hig:edit-menus#Content).

**Plattform-Besonderheiten:**
- iOS: kompakte horizontale Leiste; Chevron erweitert zum Context menu (hig:edit-menus).
- iPadOS: Touch → horizontal; Tastatur/Zeiger → direkt als (vertikales) Context menu; beide Stile unterstützen; Position anpassbar (nicht Form/Pfeil) (hig:edit-menus#iOS-iPadOS).
- macOS: über Context menu und das Edit-Menü der Menüleiste (hig:edit-menus#macOS) (hig:the-menu-bar#Edit-menu).
- visionOS: Pinch and hold → horizontale Leiste oder Context menu (hig:edit-menus).

**Kennwerte:** keine im Spiegel.

**Umsetzung:** UIKit `UIEditMenuInteraction`, Standardbefehle über `UIResponderStandardEditActions`; AppKit `NSMenu` (hig:edit-menus).

**Typische Fehler:** eigene Copy/Paste-Buttons zusätzlich zum Edit menu; Paste trotz leerer Zwischenablage; Edit- und Context menu am selben Element.

---

## Home Screen quick actions

**Zweck:** App-spezifische Schnellaktionen per Touch-and-hold auf das App-Icon. **Plattformen:** ios, ipados; nicht unterstützt in macOS, tvOS, visionOS, watchOS (hig:home-screen-quick-actions).

**Verwenden, wenn:** wertvolle Einstiegsaufgaben direkt vom Home Screen starten sollen (z. B. „Neue Nachricht“, „Route nach Hause“). **Nicht verwenden, wenn:** Aktionen sich unvorhersehbar ändern oder trivial sind.

**Kernregeln:**
- Nur überzeugende, hochwertige Aufgaben; mind. eine nützliche Aktion wird erwartet (hig:home-screen-quick-actions#Best-practices).
- Dynamische Aktionen nur auf vorhersehbare Weise ändern (Ort, letzte Aktivität, Tageszeit) (hig:home-screen-quick-actions#Best-practices).
- Titel kurz, ergebnisbeschreibend, ohne App-Namen; optional Untertitel; Lokalisierung bedenken (hig:home-screen-quick-actions#Best-practices).
- Vertrautes Interface-Icon (SF Symbols); eigene Icons mit Quick Action Icon Template (hig:home-screen-quick-actions#Best-practices).
- Kein Emoji statt Symbol (monochrom + Dark Mode) (hig:home-screen-quick-actions#Best-practices).

**Plattform-Besonderheiten:** Icon links oder rechts je nach Icon-Position; Titel/Untertitel bei LTR immer linksbündig (hig:home-screen-quick-actions).

**Kennwerte:** max. 4 Quick actions insgesamt (hig:home-screen-quick-actions#Best-practices).

**Umsetzung:** UIKit „Add Home Screen quick actions“ (`UIApplicationShortcutItem`) (hig:home-screen-quick-actions).

**Typische Fehler:** App-Name im Titel; Emojis als Icon; ständig wechselnde Aktionen.

---

## Menus

**Zweck:** Platzsparende Liste von Befehlen, Optionen oder Zuständen, die sich bei Interaktion öffnet; Regeln gelten für alle Menütypen. **Plattformen:** ios, ipados, macos, watchos (tvos, visionos) (hig:menus).

**Verwenden, wenn:** mehrere zusammengehörige Befehle/Optionen platzsparend angeboten werden. **Nicht verwenden, wenn:** Primäraktionen sofort sichtbar sein müssen (→ Button/Toolbar).

**Kernregeln:**
- Labels klar und knapp, Aktionen mit Verb; Title-Case; Artikel weglassen (hig:menus#Labels).
- Nicht verfügbare Einträge dimmen; Menü selbst bleibt öffnbar, auch wenn alle Einträge inaktiv sind (hig:menus#Labels) – Ausnahme Context menus: ausblenden (hig:context-menus#Best-practices).
- Ellipse (…) anhängen, wenn weitere Eingaben nötig sind (hig:menus#Labels).
- Icons sparsam und gezielt; innerhalb einer Gruppe alle oder keine (hig:menus#Icons).
- Wichtiges zuerst, Verwandtes gruppieren (Separator), verwandte Befehle zusammenlassen (hig:menus#Organization).
- Menülänge begrenzen; Ausnahme nutzergenerierte/dynamische Listen (History, Bookmarks) (hig:menus#Organization).
- Submenüs sparsam, eine Ebene, bei mehr als ca. fünf Einträgen eigenes Menü; Submenü statt Einrückung (hig:menus#Submenus).
- Toggle-Einträge: wechselndes Label (Show/Hide Map), ggf. mit Verb; Checkmark für aktive Attribute; ggf. „Plain“ zum Zurücksetzen (hig:menus#Toggled-items).

**Plattform-Besonderheiten:**
- iOS/iPadOS: Layouts *small* (Reihe mit 4 Symbolen ohne Label), *medium* (3 Symbole mit kurzem Label), *large* (Default, Liste). Medium für drei wichtige Aktionen, small nur für eng verwandte Gruppen (z. B. Bold/Italic/Underline/Strikethrough) (hig:menus#iOS-iPadOS).
- visionOS: small/large; Menü nahe dem gesteuerten Inhalt; Breakthrough effect `subtle` bevorzugen (hig:menus#visionOS).
- macOS, tvOS, watchOS: keine Zusatzhinweise. Spiele: Standard-Interaktion der Plattform, lesbare Größen (hig:menus#In-game-menus).

**Kennwerte:** Submenü ab ca. 5 Einträgen überdenken (hig:menus#Submenus); iOS-Layouts 4 / 3 Elemente (hig:menus#iOS-iPadOS).

**Umsetzung:** SwiftUI `Menu`; UIKit Menus and shortcuts (`UIMenu`, `preferredElementSize`); AppKit Menus (`NSMenu`) (hig:menus). visionOS: `presentationBreakthroughEffect(_:)` (hig:menus#visionOS).

**Typische Fehler:** Icons nur an einzelnen Einträgen einer Gruppe; mehrstufige Submenüs; eingerückte Einträge statt Submenü; komplett ausgeblendetes Menü, wenn alles inaktiv ist.

---

## Ornaments

**Zweck:** visionOS-Element, das Controls/Infos zu einem Fenster parallel davor schwebend anzeigt, ohne den Inhalt zu verdecken. **Plattformen:** nur visionos; nicht unterstützt in iOS, iPadOS, macOS, tvOS, watchOS (hig:ornaments).

**Verwenden, wenn:** häufig benötigte Controls an konsistenter Stelle am Fenster stehen sollen (z. B. Now-Playing). **Nicht verwenden, wenn:** System-Toolbar oder Tab bar genügen – die erscheinen in visionOS ohnehin als Ornament (hig:ornaments#Best-practices).

**Kernregeln:**
- Für häufige Controls an fester Position einsetzen (hig:ornaments#Best-practices).
- In der Regel sichtbar lassen; ausblenden nur bei Immersion (Video, Foto) (hig:ornaments#Best-practices).
- Mehrere Ornaments sparsam, auf visuelle Balance achten (hig:ornaments#Best-practices).
- Breite ≤ Fensterbreite (hig:ornaments#Best-practices).
- Borderless Buttons auf dem Glass-Hintergrund erwägen (Hover-Effekt automatisch) (hig:ornaments#Best-practices).
- System-Toolbars/Tab bars statt Custom-Ornament, wo möglich (hig:ornaments#Best-practices).

**Plattform-Besonderheiten:** nur visionOS.

**Kennwerte:** keine im Spiegel.

**Umsetzung:** SwiftUI `ornament(visibility:attachmentAnchor:contentAlignment:ornament:)` (hig:ornaments).

**Typische Fehler:** Ornament breiter als Fenster; eigenes Ornament als Toolbar-Nachbau.

---

## Pop-up buttons

**Zweck:** Button mit Menü sich gegenseitig ausschließender Optionen, der die aktuelle Auswahl anzeigt. **Plattformen:** ios, ipados, macos (visionos); nicht unterstützt in tvOS, watchOS (hig:pop-up-buttons).

**Verwenden, wenn:** flache Liste exklusiver Optionen/Zustände, Platz knapp, nicht alle Optionen dauernd sichtbar nötig. **Nicht verwenden, wenn:** Aktionen, Mehrfachauswahl oder Submenü nötig sind → Pull-down button (hig:pop-up-buttons#Best-practices).

**Kernregeln:**
- Nur für flache, exklusive Optionslisten (hig:pop-up-buttons#Best-practices).
- Sinnvollen Default setzen (hig:pop-up-buttons#Best-practices).
- Optionen vorhersehbar machen (einleitendes Label oder beschreibender Button-Text) (hig:pop-up-buttons#Best-practices).
- Bei Platzmangel als kompakte Alternative einsetzen (hig:pop-up-buttons#Best-practices).
- Ggf. Option „Custom“ für seltene Fälle, evtl. mit Erklärtext unter der Liste (hig:pop-up-buttons#Best-practices).

**Plattform-Besonderheiten:**
- iPadOS: In Popover/modaler View statt Disclosure indicator für kleine, klar definierte Optionsmengen eines Listeneintrags (hig:pop-up-buttons#iPadOS).

**Kennwerte:** keine im Spiegel.

**Umsetzung:** SwiftUI `Picker` mit `MenuPickerStyle` (`.menu`); UIKit `UIButton.changesSelectionAsPrimaryAction`; AppKit `NSPopUpButton` (hig:pop-up-buttons).

**Typische Fehler:** Aktionen im Pop-up; kein Default; Pop-up ohne Kontext, dessen Optionen man nicht erahnen kann.

---

## Pull-down buttons

**Zweck:** Button, dessen Menü Befehle/Elemente zeigt, die direkt mit der Button-Aktion zusammenhängen. **Plattformen:** ios, ipados, macos (visionos); nicht unterstützt in tvOS, watchOS (hig:pull-down-buttons).

**Verwenden, wenn:** eine Aktion präzisiert werden soll (Add → was hinzufügen; Sort → nach welchem Attribut; Back → wohin). **Nicht verwenden, wenn:** exklusive Auswahl ohne Befehle (→ Pop-up button) oder nur 1–2 Einträge (→ Buttons/Toggles) (hig:pull-down-buttons#Best-practices).

**Kernregeln:**
- Nur direkt zur Button-Aktion gehörige Befehle (hig:pull-down-buttons#Best-practices).
- Nicht alle Aktionen einer View in einem Pull-down verstecken (hig:pull-down-buttons#Best-practices).
- Mind. drei Einträge, aber nicht zu viele (hig:pull-down-buttons#Best-practices).
- Menütitel nur, wenn er Bedeutung ergänzt (hig:pull-down-buttons#Best-practices).
- Destruktive Einträge kennzeichnen (rot) und bestätigen lassen – System zeigt Action sheet (iOS) bzw. Popover (iPadOS) (hig:pull-down-buttons#Best-practices).
- Icons hinter dem Label nur bei Mehrwert, bevorzugt SF Symbols (hig:pull-down-buttons#Best-practices).

**Plattform-Besonderheiten:**
- iOS/iPadOS: Pull-down auch per Geste (z. B. Touch and hold auf Button) möglich; More-Button (Ellipse) für Nebenaktionen – Abwägung Platz vs. Auffindbarkeit (hig:pull-down-buttons#iOS-iPadOS).
- visionOS: Pull-downs in Toolbars vermeiden (hig:toolbars#visionOS).

**Kennwerte:** mind. 3 Menüeinträge empfohlen (hig:pull-down-buttons#Best-practices).

**Umsetzung:** SwiftUI `Menu` (Spiegel nennt hier `MenuPickerStyle` – vermutlich Spiegel-/Apple-Ungenauigkeit, `MenuPickerStyle` ist der Pop-up-Fall); UIKit `UIControl.showsMenuAsPrimaryAction`; AppKit `NSPopUpButton.pullsDown` (hig:pull-down-buttons).

**Typische Fehler:** Primäraktionen nur im More-Menü; Pull-down mit einem Eintrag; destruktive Aktion ohne Bestätigung.

---

## The menu bar

**Zweck:** Leiste am oberen Bildschirmrand mit allen Top-Level-Menüs der App. **Plattformen:** macos, ipados; nicht unterstützt in iOS, tvOS, visionOS, watchOS (hig:the-menu-bar).

**Verwenden, wenn:** Mac- oder iPad-App – praktisch immer; die Menüleiste ist das vollständige Befehlsverzeichnis. **Nicht verwenden als:** Sammelbecken für Funktionen, die sonst nirgends passen (iPadOS) (hig:the-menu-bar#iPadOS).

**Reihenfolge:** *AppName* · File · Edit · Format · View · app-spezifische Menüs · Window · Help; macOS zusätzlich Apple-Menü (links) und Menu bar extras (rechts) (hig:the-menu-bar#Anatomy).

**Kernregeln:**
- Systemmenüs und deren Reihenfolge übernehmen (hig:the-menu-bar#Best-practices).
- Immer dieselben Einträge zeigen; Nicht-Ausführbares deaktivieren, nicht ausblenden (hig:the-menu-bar#Best-practices).
- Standard-Tastaturkürzel unterstützen, eigene nur wenn nötig (hig:the-menu-bar#Best-practices).
- Kurze, einwörtige Menütitel (hig:the-menu-bar#Best-practices).
- Alle eigenen Befehle in app-spezifischen Menüs listen (auch wenn anderswo verfügbar), Ordnung spiegelt App-Hierarchie, von allgemein zu speziell (hig:the-menu-bar#App-specific-menus).
- View- und Window-Menü auch bei minimalem Funktionsumfang bzw. nur einem Fenster bereitstellen (hig:the-menu-bar#View-menu) (hig:the-menu-bar#Window-menu).
- Dynamic menu items (Modifier-Varianten) nie als einzigen Weg; nur in Menüleisten-Menüs; nur ein Modifier (hig:the-menu-bar#Dynamic-menu-items).

**Standardmenüs kompakt:**

| Menü | Wichtigste Regeln |
|---|---|
| App (hig:the-menu-bar#App-menu) | About zuerst, allein in Gruppe; App-Name kurz, ohne Versionsnummer; Settings… nur App-weite Einstellungen (Dokument-Settings → File); eigene Konfig-Einträge direkt nach Settings; Hide/Quit mit gleichem Kurznamen. |
| File (hig:the-menu-bar#File-menu) | Entfällt/umbenennbar ohne Dateien. New *Item* mit konkretem Typ; Open Recent ohne Pfade, neueste zuerst; Autosave statt ständig Save; Duplicate statt Save As/Export/Copy To; Export As… nur für fremde Formate; Page Setup nur für dokumentbezogene Druckparameter. |
| Edit (hig:the-menu-bar#Edit-menu) | Undo/Redo mit Ziel benennen („Undo Typing“); Delete statt Erase/Clear; Find ggf. ins File-Menü, wenn es um Dateien/Objekte geht; Start Dictation und Emoji & Symbols fügt das System an. |
| Format (hig:the-menu-bar#Format-menu) | Nur bei formatiertem Text; Submenüs Font und Text. |
| View (hig:the-menu-bar#View-menu) | Fensterdarstellung (Tab bar, Toolbar, Sidebar, Full Screen); Show/Hide-Titel spiegeln den aktuellen Zustand; keine Fensternavigation. |
| Window (hig:the-menu-bar#Window-menu) | Minimize und Zoom immer (Full Keyboard Access); Zoom nicht für Full Screen; offene Fenster alphabetisch, keine Panels; Panels ein-/ausblenden erwägen (außer Font/Color – stehen im Format-Menü). |
| Help (hig:the-menu-bar#Help-menu) | Ganz rechts; Help Book liefert Suchfeld automatisch; Zusatzeinträge per Separator abtrennen, wenige halten. |

**Plattform-Besonderheiten:**
- iPadOS: verborgen bis zum Aufdecken (Zeiger an oberen Rand/Wischen), zentriert, keine Menu bar extras, kein Apple-Menü, App-Menü ohne About/Services/Sichtbarkeitseinträge; alle Funktionen auch im UI anbieten (Dynamic items nur mit Hardware-Tastatur); *AppName > Settings* öffnet die App-Seite in den iPadOS-Einstellungen, interne Einstellungen als separater Eintrag darunter; Tabs als Einträge im View-Menü erwägen; häufiger Submenüs nutzen (hig:the-menu-bar#iPadOS).
- macOS: Apple-Menü fix; bei Platzmangel werden Titelabstände verkleinert/abgeschnitten; im Vollbild versteckt (hig:the-menu-bar#macOS). *Menu bar extras*: Symbol (Template-Bild schwarz/transparent), bei Klick Menü statt Popover, Nutzer entscheidet über Anzeige, nicht auf Vorhandensein verlassen, Funktionen auch anders anbieten (z. B. Dock menu) (hig:the-menu-bar#Menu-bar-extras).

**Kennwerte:** Menüleistenhöhe 24 pt (hig:the-menu-bar#Menu-bar-extras); About-Name ≤ 16 Zeichen (hig:the-menu-bar#App-menu).

**Umsetzung:** SwiftUI `CommandMenu` (+ `CommandGroup`, `MenuBarExtra`); UIKit „Adding menus and shortcuts to the menu bar“ (`UIMenuBuilder`); AppKit `NSMenu`, `NSStatusBar` (Menu bar extras), `NSMenuItem.isAlternate`, `NSHelpManager` (hig:the-menu-bar). `CommandGroup`/`UIMenuBuilder` nicht im Spiegel genannt.

**Typische Fehler:** Einträge kontextabhängig aus-/einblenden; „Save As“ statt „Duplicate“; Zoom als Vollbild-Schalter; Menu bar extra öffnet Popover; Funktionen nur über Modifier-Varianten.

---

## Toolbars

**Zweck:** Leiste oben/unten mit Titel, Navigation, Suche und häufigen Aktionen für die aktuelle View. **Plattformen:** ios, ipados, macos, watchos (tvos, visionos) (hig:toolbars).

**Verwenden, wenn:** häufige Befehle, Navigation (Back/Close) oder Suche für die aktuelle View. **Nicht verwenden, wenn:** zwischen Hauptbereichen der App gewechselt wird → Tab bar (hig:toolbars).

**Kernregeln:**
- Items bewusst wählen, Überfüllung vermeiden; Overflow-Verhalten definieren, kein manuelles Overflow-Menü (System macht das in macOS/iPadOS) (hig:toolbars#Best-practices).
- More-Menü nur wenn nötig, für weniger wichtige Aktionen (hig:toolbars#Best-practices).
- Eigene Hintergründe/getönte Controls reduzieren, ggf. `ScrollEdgeEffectStyle`; bei buntem Content monochrome Items (Liquid Glass) (hig:toolbars#Best-practices).
- Standardkomponenten nutzen (konzentrische Eckradien) (hig:toolbars#Best-practices).
- Jedem Fenster einen nützlichen, kurzen Titel geben, nicht den App-Namen (hig:toolbars#Titles).
- Standard-Back- und Close-Buttons mit Systemsymbolen, kein Textlabel „Back“/„Close“ (hig:toolbars#Navigation).
- Symbole statt Text, ohne Rahmen; Text nur wo Symbole schwach sind (z. B. Edit) (hig:toolbars#Actions).
- Genau eine Primäraktion (Done/Submit) mit `.prominent`-Stil am trailing Ende (hig:toolbars#Actions).
- Gruppen: leading (Back, Sidebar, Titel, Dokumentmenü; nicht anpassbar), center (häufige Controls, anpassbar, kollabiert ins Overflow), trailing (immer sichtbar: Inspector, Suche, More, Primäraktion); max. drei Gruppen (hig:toolbars#Item-groupings).
- Textbuttons mit fixem Abstand voneinander und von Symbolbuttons trennen (hig:toolbars#Item-groupings).

**Plattform-Besonderheiten:**
- iOS: nur das Wichtigste, Rest ins More-Menü; Large title, der beim Scrollen zum Standardtitel wird (navigation bar) (hig:toolbars#iOS).
- iPadOS: Toolbar und Tab bar können sich die obere Zeile teilen; Anpassbarkeit erwägen (hig:toolbars#iPadOS) (hig:toolbars#Best-practices).
- macOS: im Fensterrahmen, Items ohne Bezel; jedes Toolbar-Item auch als Menüleisten-Befehl (hig:toolbars#macOS).
- visionOS: unten am Fenster als Ornament; Symbol oder Text, Label erscheint beim Anschauen; keine vertikale Toolbar; Fenster nicht schmaler als Toolbar; keine Pull-downs (hig:toolbars#visionOS).
- watchOS: Buttons in oberen Ecken oder unten; scrollender Toolbar-Button (`primaryAction`) für wichtige Nicht-Primärfunktion (hig:toolbars#watchOS).

**Kennwerte:** Titel unter 15 Zeichen; max. drei Gruppen (hig:toolbars#Titles) (hig:toolbars#Item-groupings).

**Umsetzung:** SwiftUI `toolbar` / `ToolbarItem` (Placements `topBarLeading`, `topBarTrailing`, `bottomBar`, `primaryAction`); UIKit `UIToolbar`, `UINavigationBar.prefersLargeTitles`, `UIBarButtonItem.SystemItem.fixedSpace`; AppKit `NSToolbar` (hig:toolbars).

**Typische Fehler:** App-Name als Fenstertitel; mehrere `.prominent`-Aktionen; „Back“ als Text; Toolbar-only-Befehle ohne Menüleisten-Pendant (macOS); Tab bar-Navigation in die Toolbar gepackt.
