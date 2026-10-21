# Presentation – Komponenten
> Quelle: Apple HIG, lokaler Spiegel (Stand 2026-10-21). Paraphrasiert. Belege: `(hig:<slug>)`, `(hig:<slug>#Anchor)`.

Komponenten, die Inhalte oder Aufgaben über, neben oder anstelle des aktuellen Kontexts darstellen: modale Unterbrechungen (Alert, Action sheet, Sheet), transiente Overlays (Popover), schwebende Hilfsfenster (Panel), Fenster sowie Scroll- und Paging-Container. Übergreifende Regeln zur Modalität stehen in `(hig:modality)`.

Inhalt: [Action sheets](#action-sheets) · [Alerts](#alerts) · [Page controls](#page-controls) · [Panels](#panels) · [Popovers](#popovers) · [Scroll views](#scroll-views) · [Sheets](#sheets) · [Windows](#windows) · [Abgrenzung](#abgrenzung-bestätigung-und-nebenaufgabe)

**Übergreifend (Modality):** Modal nur bei klarem Nutzen; modale Aufgaben kurz und linear halten, keine „App in der App“ (hig:modality#Best-practices). Immer einen offensichtlichen Weg zum Schließen bieten – iOS/iPadOS/watchOS: Button in der oberen Toolbar oder Wischen nach unten; macOS/tvOS: Button im Inhaltsbereich (hig:modality#Best-practices). Vor Datenverlust beim Schließen bestätigen lassen, in iOS z. B. per Action sheet mit Sichern-Option (hig:modality#Best-practices). Nie mehrere modale Views gleichzeitig; Alerts dürfen über allem liegen, aber nie zwei Alerts zugleich (hig:modality#Best-practices).

---

## Action sheets
**Zweck:** Modale Auswahl von Optionen, die sich auf eine Aktion beziehen, die die Person gerade bewusst ausgelöst hat. **Plattformen:** ios, ipados, macos, watchos (tvos ebenfalls; nicht unterstützt in visionOS).

**Verwenden, wenn:** eine vom Nutzer initiierte Aktion klärende Wahlmöglichkeiten braucht (z. B. Entwurf löschen oder sichern) (hig:action-sheets#Best-practices); Bestätigung vor Verwerfen ungesicherter Änderungen beim Swipe-to-dismiss eines Sheets (hig:sheets#iOS-iPadOS).
**Nicht verwenden, wenn:** über ein unerwartetes Problem informiert werden muss → Alert (hig:action-sheets#Best-practices); Optionen auf Abruf gezeigt werden sollen → Menu (hig:action-sheets#iOS-iPadOS).

**Kernregeln:**
- Action sheet statt Alert für Wahlmöglichkeiten zu einer absichtlichen Aktion einsetzen (hig:action-sheets#Best-practices).
- Sparsam einsetzen – jede Instanz unterbricht die Aufgabe (hig:action-sheets#Best-practices).
- Titel kurz halten, möglichst einzeilig; Message nur, wenn Titel plus Kontext nicht reichen (hig:action-sheets#Best-practices).
- Bei möglicher Datenvernichtung einen Cancel-Button bieten, unten platziert (watchOS: oben links) (hig:action-sheets#Best-practices).
- Destruktive Optionen mit Destructive-Style kennzeichnen und oben anordnen (hig:action-sheets#Best-practices).
- Kein Scrollen zulassen – Anzahl der Buttons begrenzen (hig:action-sheets#iOS-iPadOS).

**Plattform-Besonderheiten:**
- iOS/iPadOS: Action sheet statt Menu für aktionsbezogene Auswahl; nicht scrollen lassen (hig:action-sheets#iOS-iPadOS).
- watchOS: Systemstil mit Titel, optionaler Message, Cancel und weiteren Buttons; Button-Stile Default, Destructive, Cancel (hig:action-sheets#watchOS).
- macOS, tvOS: keine zusätzlichen Hinweise; visionOS: nicht unterstützt (hig:action-sheets#Platform-considerations).

**Kennwerte:** watchOS: max. 4 Buttons inkl. Cancel, also max. 3 zusätzliche Optionen (hig:action-sheets#watchOS).

**Umsetzung:** SwiftUI `confirmationDialog(_:isPresented:titleVisibility:actions:)` (plattformübergreifend, enthält standardmäßig Cancel), Rolle `ButtonRole.destructive`; UIKit `UIAlertController` mit `.actionSheet`, `UIAlertAction.Style.destructive` (hig:action-sheets).

**Typische Fehler:**
- Action sheet für Fehlermeldungen oder reine Infos (gehört in Alert bzw. in den Kontext).
- Lange Optionslisten, die scrollen.
- Destruktive Option unten oder ohne Destructive-Style.
- Action sheet als Ersatz für ein vom Nutzer geöffnetes Menü.

---

## Alerts
**Zweck:** Unterbrechende Darstellung kritischer Informationen, die sofort Aufmerksamkeit oder eine Entscheidung erfordern. **Plattformen:** ios, ipados, macos, watchos (auch tvos, visionos).

**Verwenden, wenn:** ein Problem gemeldet, vor seltener, nicht rückgängig machbarer Datenvernichtung gewarnt oder ein Kauf/eine wichtige selbst ausgelöste Aktion bestätigt werden muss (hig:alerts).
**Nicht verwenden, wenn:** nur informiert wird (nicht handlungsrelevant), für häufige rückgängig machbare Aktionen (auch destruktive), beim App-Start, für Auswahl zu einer bewussten Aktion → Action sheet (hig:alerts#Best-practices, hig:alerts#iOS-iPadOS).

**Kernregeln:**
- Sparsam einsetzen; nur wesentliche Infos und nützliche Aktionen (hig:alerts#Best-practices).
- Titel konkret: was ist passiert, wo, warum – kein „Error“/Fehlercode, max. zwei Zeilen; Satz → Satzzeichen + Sentence case, Fragment → Title case ohne Punkt (hig:alerts#Content).
- Zusatztext nur bei Mehrwert; Buttons nicht erklären (hig:alerts#Content).
- Button-Titel: ein bis zwei Wörter, Verb mit Bezug zum Text; „OK“ nur in rein informativen Alerts; „Yes/No“ vermeiden; Abbrechen heißt immer „Cancel“ (hig:alerts#Buttons).
- Reihenfolge: wahrscheinlichster/Default-Button trailing in einer Zeile bzw. oben im Stapel; Cancel leading bzw. unten (hig:alerts#Buttons).
- Destructive-Style nur für destruktive Aktionen, die die Person **nicht** bewusst gewählt hat (bewusst gewähltes „Papierkorb leeren“ bleibt Default-Stil, damit Return bestätigt) (hig:alerts#Buttons).
- Bei destruktiver Aktion immer Cancel anbieten, Cancel aber nie zum Default machen; soll bewusst gelesen werden → keinen Default-Button; Einzel-Button als Default → „Done“, nicht „Cancel“ (hig:alerts#Buttons).
- Alternative Abbruchwege unterstützen: Home Screen (iOS/iPadOS), Esc bzw. Cmd-. (iOS, iPadOS, macOS, visionOS), Menu-Taste (tvOS) (hig:alerts#Buttons).
- Textfeld nur, wenn Eingabe zur Lösung nötig ist (z. B. Passwort) (hig:alerts#Content).

**Plattform-Besonderheiten:**
- iOS/iPadOS: Für aktionsbezogene Auswahl Action sheet nutzen; Scrollen vermeiden (kann bei großer Schrift auftreten) (hig:alerts#iOS-iPadOS).
- macOS: App-Icon wird automatisch gezeigt (ersetzbar); Suppression-Checkbox für wiederkehrende Alerts, Accessory view, Help-Button möglich; Caution-Symbol (`exclamationmark.triangle`) nur bei echtem Risiko unerwarteten Datenverlusts, nicht bei Sichern/Papierkorb leeren (hig:alerts#macOS).
- visionOS: Shared Space → vor dem Fenster, leicht nach vorn versetzt, bleibt beim Verschieben am Fenster verankert; Full Space → zentriert im Sichtfeld (hig:alerts#visionOS).
- Textfeld möglich in iOS, iPadOS, macOS, visionOS; Icon + Accessory view in macOS, visionOS (hig:alerts#Content).
- tvOS, watchOS: keine zusätzlichen Hinweise.

**Kennwerte:** bis zu 3 Buttons (alle Plattformen) (hig:alerts#Content); visionOS-Accessory-View max. 154 pt hoch, Eckenradius 16 pt (hig:alerts#visionOS).

**Umsetzung:** SwiftUI `alert(_:isPresented:actions:)` mit `Button(role: .cancel/.destructive)`; UIKit `UIAlertController` (`.alert`); AppKit `NSAlert` (`accessoryView`, Suppression) (hig:alerts).

**Typische Fehler:**
- „OK“/„Yes“/„No“ statt handlungsbeschreibender Verben.
- Alert bei jedem Löschen trotz Undo; Alert beim App-Start (z. B. „Kein Netz“ statt Platzhalterdaten + dezentem Hinweis).
- Cancel als Default-Button; Destructive-Style auf bewusst gewählter Aktion.
- Titel „Fehler“ ohne Ursache/Kontext.

---

## Page controls
**Zweck:** Reihe von Indikatoren (Punkte), die Seiten einer flachen, geordneten Liste und die aktuelle Seite zeigt. **Plattformen:** ios, ipados, watchos (auch tvos, visionos; nicht unterstützt in macOS).

**Verwenden, wenn:** zwischen gleichrangigen, sequenziellen Seiten gewechselt wird, auch bei vom Nutzer erzeugten Listen (z. B. Wetter-Orte) (hig:page-controls#Best-practices).
**Nicht verwenden, wenn:** Hierarchie oder nicht-sequenzielle Beziehungen bestehen → Sidebar/Split view; bei sehr vielen Seiten → z. B. Grid (hig:page-controls#Best-practices).

**Kernregeln:**
- Horizontal zentriert nahe dem unteren Rand platzieren (hig:page-controls#Best-practices).
- Nicht zu viele Seiten – ab etwa 10 Punkten nicht mehr auf einen Blick zählbar (hig:page-controls#Best-practices).
- Eigene Indikatorbilder einfach halten (keine Negativräume, Text, Innenlinien); SF Symbols bevorzugen (hig:page-controls#Customizing-indicators).
- Standardbild nur anpassen, wenn es die Bedeutung stärkt; max. zwei verschiedene Indikatorbilder (hig:page-controls#Customizing-indicators).
- Indikatoren nicht einfärben – Systemfarbe sichert Kontrast (hig:page-controls#Customizing-indicators).
- Beim Scrubbing keine animierten Seitenübergänge; Animation nur beim Tippen (hig:page-controls#iOS-iPadOS).
- Kein Scrubbing beim Hintergrundstil Minimal (kein Feedback) (hig:page-controls#iOS-iPadOS).

**Plattform-Besonderheiten:**
- iOS/iPadOS: Tippen links/rechts vom aktuellen Punkt = vorige/nächste Seite, Scrubbing = sequenziell, über den Rand hinaus = erste/letzte Seite; iPadOS: Pointer auf einzelne Punkte. Hintergrundstile: Automatic (nur bei Interaktion; wenn nicht primäre Navigation), Prominent (immer; nur wenn primäre Navigation), Minimal (nie) (hig:page-controls#iOS-iPadOS).
- tvOS: nur für Sammlungen ganzseitiger Seiten (hig:page-controls#tvOS).
- visionOS: nur Anzeige, nicht interaktiv (hig:page-controls#visionOS).
- watchOS: unten bei horizontaler Paginierung oder neben der Digital Crown bei vertikalem Tab view; vertikale Paginierung mit Digital Crown bevorzugen; Seiten möglichst auf eine Bildschirmhöhe begrenzen, variable Höhen nach festen (hig:page-controls#watchOS).

**Kennwerte:** „mehr als etwa 10 Punkte“ schwer erfassbar (hig:page-controls#Best-practices); max. 2 verschiedene Indikatorbilder (hig:page-controls#Customizing-indicators).

**Umsetzung:** SwiftUI `TabView` mit `PageTabViewStyle` (`.tabViewStyle(.page)`); UIKit `UIPageControl` (`preferredIndicatorImage`, `setIndicatorImage(_:forPage:)`, `backgroundStyle`, `InteractionState`) (hig:page-controls).

**Typische Fehler:**
- Page control für hierarchische Navigation.
- Viele bunte/unterschiedliche Indikatorsymbole.
- Scroll-Indikator auf derselben Achse zusätzlich zur Page control (hig:scroll-views#iOS-iPadOS).

---

## Panels
**Zweck:** Schwebendes macOS-Hilfsfenster mit Steuerelementen, Optionen oder Infos zum aktiven Fenster bzw. zur Auswahl. **Plattformen:** macos (nicht unterstützt in iOS, iPadOS, tvOS, visionOS, watchOS).

**Verwenden, wenn:** schneller Zugriff auf Einstellungen zur aktuellen Auswahl nötig ist, v. a. als Inspector (Inhalt folgt der Auswahl) (hig:panels#Best-practices); wiederholte Eingaben mit sichtbarem Ergebnis (z. B. Suchen & Ersetzen) statt Sheet (hig:sheets#macOS).
**Nicht verwenden, wenn:** ein Info-Fenster mit festem Inhalt gebraucht wird → normales Window; das Layout eher einen Split-view-Bereich als Inspector nahelegt (hig:panels#Best-practices). Auf anderen Plattformen stattdessen modale Darstellung erwägen (hig:panels).

**Kernregeln:**
- Einfache Direktsteuerungen (Slider, Stepper) bevorzugen; Texteingabe und Auswahl-dann-Handeln vermeiden (hig:panels#Best-practices).
- Kurzen Substantiv-Titel in Title case vergeben (z. B. „Inspector“) – Titelleiste zum Positionieren nötig (hig:panels#Best-practices).
- Bei App-Aktivierung alle offenen Panels nach vorn holen, bei Inaktivität ausblenden (hig:panels#Best-practices).
- Panels nicht in die Dokumentliste des Window-Menüs aufnehmen (Show/Hide-Befehle dort sind ok) (hig:panels#Best-practices).
- Minimize-Button in der Regel nicht anbieten (hig:panels#Best-practices).
- Im UI per Titel benennen, ohne das Wort „Panel“ („Show Fonts“) (hig:panels#Best-practices).
- HUD-Stil nur in medienorientierten Apps, wenn ein Standard-Panel Inhalt verdecken würde und kaum Controls nötig sind; Standard-Panels bevorzugen (hig:panels#HUD-style-panels).
- HUDs klein halten, Farbe sparsam, Stil beim Moduswechsel (z. B. Vollbild) beibehalten (hig:panels#HUD-style-panels).

**Plattform-Besonderheiten:** nur macOS. Panels werden meist erst durch Klick auf Titelleiste oder ein Texteingabe-Element zum Key window (hig:windows#macOS-window-states). In Panels ggf. kleine/mini Scrollbars, dann alle Controls gleich groß (hig:scroll-views#macOS).

**Kennwerte:** keine im Spiegel.

**Umsetzung:** AppKit `NSPanel`, HUD über `NSWindow.StyleMask.hudWindow` (hig:panels). SwiftUI: im Spiegel kein Panel-Typ genannt; für Inspector-Funktion kommt `inspector(isPresented:content:)` bzw. ein Split-view-Bereich in Frage (nicht aus dem Spiegel belegt).

**Typische Fehler:**
- Panel bleibt sichtbar, während die App inaktiv ist.
- Formularlastige Panels mit vielen Textfeldern.
- HUD ohne inhaltlichen Grund oder mit Standard-Controls, die optisch nicht passen.

---

## Popovers
**Zweck:** Transiente Ansicht über dem Inhalt, die nach Klick/Tipp auf ein Control erscheint und auf dieses zeigt. **Plattformen:** ios, ipados, macos (auch visionos; nicht unterstützt in tvOS, watchOS).

**Verwenden, wenn:** wenig Information oder wenige zusammenhängende Funktionen kurzfristig gebraucht werden (z. B. Termin-Details ändern) und dauerhafte Sidebars/Panels zu viel Platz kosten (hig:popovers#Best-practices).
**Nicht verwenden, wenn:** eine Warnung gezeigt werden muss → Alert; in Compact-Size-Class → Sheet o. ä. Vollbild-Modal (hig:popovers#Best-practices, hig:popovers#iOS-iPadOS).

**Kernregeln:**
- Pfeil möglichst direkt auf das auslösende Element richten; dieses und essenziellen Inhalt nicht verdecken (hig:popovers#Best-practices).
- Close/Cancel/Done nur, wenn es Klarheit schafft (z. B. mit/ohne Sichern); sonst schließt Tipp außerhalb oder eine Auswahl; bei Mehrfachauswahl offen lassen bis explizit geschlossen (hig:popovers#Best-practices).
- Beim automatischen Schließen eines nicht-modalen Popovers Arbeit immer sichern; verwerfen nur über expliziten Cancel (hig:popovers#Best-practices).
- Nur ein Popover gleichzeitig, keine Kaskaden; nichts darüber außer einem Alert (hig:popovers#Best-practices).
- Wechsel zu einem anderen Popover mit einem Klick/Tipp ermöglichen (hig:popovers#Best-practices).
- Größe auf den Inhalt beschränken; Größenwechsel animieren (hig:popovers#Best-practices).
- In Hilfetexten nicht „Popover“ sagen, sondern Aufgabe/Element benennen (hig:popovers#Best-practices).

**Plattform-Besonderheiten:**
- iOS/iPadOS: keine Popovers in kompakten Views; Layout an Size class anpassen, dort Sheet o. ä. nutzen (hig:popovers#iOS-iPadOS).
- macOS: Popover kann durch Ziehen abgelöst werden und wird zum Panel; Ablösen erwägen, abgelöste Form optisch kaum verändern (hig:popovers#macOS).
- visionOS: keine zusätzlichen Hinweise.

**Kennwerte:** keine im Spiegel.

**Umsetzung:** SwiftUI `popover(isPresented:attachmentAnchor:arrowEdge:content:)`; UIKit `UIPopoverPresentationController`; AppKit `NSPopover` (hig:popovers).

**Typische Fehler:**
- Popover auf iPhone in Compact-Breite erzwingen.
- Popover aus Popover öffnen.
- Eingaben beim Tippen außerhalb verwerfen.
- Warnungen im Popover statt Alert.

---

## Scroll views
**Zweck:** Container, der Inhalte größer als die sichtbare Fläche vertikal oder horizontal verschiebbar macht. **Plattformen:** ios, ipados, macos, watchos (auch tvos, visionos).

**Verwenden, wenn:** Inhalt über die Grenzen der View hinausgeht; Paging für seitenweise Inhalte (hig:scroll-views#Best-practices).
**Nicht verwenden, wenn:** dadurch ein Scroll view gleicher Richtung in einem anderen verschachtelt würde (hig:scroll-views#Best-practices).

**Kernregeln:**
- Standard-Scrollgesten und Tastaturkürzel unterstützen; eigene Implementierungen mit elastischem Verhalten (hig:scroll-views#Best-practices).
- Scrollbarkeit sichtbar machen, z. B. angeschnittene Inhalte am Rand (hig:scroll-views#Best-practices).
- Keine verschachtelten Scroll views gleicher Ausrichtung (horizontal in vertikal ist ok) (hig:scroll-views#Best-practices).
- Page-by-page-Scrolling erwägen, ggf. mit Überlappungseinheit (z. B. eine Textzeile) für Kontext (hig:scroll-views#Best-practices).
- Automatisch scrollen, wenn Auswahl/Einfügemarke außer Sicht ist – aber nur so weit wie nötig (hig:scroll-views#Best-practices).
- Bei Zoom sinnvolle Min-/Max-Skalierung setzen (hig:scroll-views#Best-practices).
- Scroll edge effect: Stil Automatic bevorzugen; nur hinter schwebenden Elementen (z. B. Toolbars), nicht dekorativ; ein Effekt pro View, in Split views je Bereich mit gleicher Höhe (hig:scroll-views#Scroll-edge-effects).

**Plattform-Besonderheiten:**
- iOS/iPadOS: Im Paging-Modus Page control erwägen, dann keinen Scroll-Indikator auf derselben Achse (hig:scroll-views#iOS-iPadOS). Scroll edge effects gibt es in iOS, iPadOS, macOS (hig:scroll-views#Scroll-edge-effects).
- macOS: Indikator heißt Scroll bar; in Panels ggf. small/mini, dann einheitliche Control-Größe (hig:scroll-views#macOS).
- tvOS: keine Indikatoren; System scrollt fokussierte Elemente ins Bild (hig:scroll-views#tvOS).
- visionOS: kleiner, fester Indikator an festen Positionen, etwas dicker als iOS → Ränder ggf. vergrößern; Jog-Bar beim Ziehen; Look to Scroll pro Scroll view aktivieren – für Lese-/Browse-Views, nicht für Controls/dichte Infos, konsistent, klare Scrollbereiche, Parallax/Custom-Scroll-Effekte vorher entfernen (hig:scroll-views#visionOS, hig:scroll-views#Look-to-Scroll).
- watchOS: vertikal bevorzugen (Digital Crown); Paging über vertikale Tab views; Seiten möglichst eine Bildschirmhöhe (hig:scroll-views#watchOS).

**Kennwerte:** keine im Spiegel.

**Umsetzung:** SwiftUI `ScrollView`, `PagingScrollTargetBehavior`, `ScrollEdgeEffectStyle`, `ScrollInputKind.look`; UIKit `UIScrollView`, `UIScrollEdgeEffect.Style`; AppKit `NSScrollView`, `NSScrollEdgeEffectStyle`; WatchKit `WKPageOrientation` (hig:scroll-views).

**Typische Fehler:**
- Vertikale Liste in vertikalem ScrollView.
- Scroll edge effect als Deko oder doppelt pro View.
- Custom-Scrolling ohne Bounce/Elastizität.
- Look to Scroll in Listen mit vielen Controls.

---

## Sheets
**Zweck:** Ansicht für eine abgegrenzte Aufgabe mit engem Bezug zum aktuellen Kontext, nach der man zur Ausgangsansicht zurückkehrt. **Plattformen:** ios, ipados, macos, watchos (auch tvos, visionos).

**Verwenden, wenn:** gezielt Informationen abgefragt oder eine einfache Aufgabe erledigt wird (Datei anhängen, Speicherort wählen) (hig:sheets).
**Nicht verwenden, wenn:** der Ablauf komplex/lang ist → iOS/iPadOS Full-screen-Modal, macOS neues Fenster oder Vollbild, visionOS Full Space (hig:sheets#Best-practices); wiederholte Eingabe mit Ergebnisbeobachtung in macOS → Panel (hig:sheets#macOS); watchOS für reine Info/Auswahl → Alert/Action sheet (hig:sheets#watchOS).

**Kernregeln:**
- Nur ein Sheet gleichzeitig aus der Hauptoberfläche; Folge-Sheet erst nach Schließen des ersten (hig:sheets#Best-practices).
- Für ergänzende Elemente, die die Hauptaufgabe beeinflussen, nicht-modal arbeiten: iOS/iPadOS nicht-modales Sheet, macOS Panel, visionOS Split view (hig:sheets#Best-practices).
- Done nie allein: mit Cancel (ohne Sichern schließen) oder Back (vorheriger Schritt) kombinieren; nicht alle drei (Cancel, Done, Back) zugleich (hig:sheets#Best-practices).
- Back dient der Navigation im Sheet, nicht dem Schließen (hig:sheets#Anatomy).
- iOS/iPadOS Einzel-View: Cancel leading in der oberen Toolbar, Done trailing; bei Mehrschritt-Flows variiert die Platzierung pro Schritt (hig:sheets#iOS-iPadOS).
- Detents: large ist automatisch unterstützt; medium ergänzen für Progressive Disclosure (z. B. Share sheet); nur medium verhindert Vollhöhe; volle Höhe für Erstellungsaufgaben (Compose) (hig:sheets#iOS-iPadOS).
- Resizable Sheets mit Grabber (auch VoiceOver-bedienbar; Tippen wechselt Detents) (hig:sheets#iOS-iPadOS).
- Swipe-to-dismiss unterstützen; bei ungesicherten Änderungen per Action sheet bestätigen (hig:sheets#iOS-iPadOS).
- iPadOS: Page- oder Form-sheet-Stil bevorzugen (hig:sheets#iOS-iPadOS).

**Plattform-Besonderheiten:**
- Modalität: macOS, tvOS, visionOS, watchOS immer modal; iOS/iPadOS modal oder nicht-modal (z. B. Notes-Formatierung) (hig:sheets#Anatomy).
- macOS: Karte über dem abgedunkelten Elternfenster; sinnvolle Standardgröße, Resizing bei Bedarf; andere App-Fenster bleiben bedienbar; beim Öffnen Elternfenster (und dessen Dokument-Panels) nach vorn (hig:sheets#macOS).
- visionOS: nicht vom unteren Fensterrand einfahren, zentriert im Sichtfeld; Größe so, dass das Fenster nicht (fast) komplett verdeckt wird (hig:sheets#visionOS).
- watchOS: Vollbild, halbtransparent mit Blur; nur für eigene Titel/Inhalte, kurz und selten, nicht zur Navigation; geänderte Close-Beschriftung bevorzugt als SF Symbol, nicht wie Seitentitel (hig:sheets#watchOS).

**Kennwerte:** medium-Detent ≈ halbe Höhe des voll ausgefahrenen Sheets (Spiegel: „about half“) (hig:sheets#iOS-iPadOS). Sonst keine.

**Umsetzung:** SwiftUI `sheet(item:onDismiss:content:)` / `sheet(isPresented:)`, Detents via `presentationDetents([.medium, .large])`, Grabber via `presentationDragIndicator(.visible)`, Vollbild via `fullScreenCover` (iOS/iPadOS); UIKit `UISheetPresentationController` (`detents`, `prefersGrabberVisible`), `UIModalPresentationStyle` (`.pageSheet`, `.formSheet`, `.fullScreen`); AppKit `NSViewController.presentAsSheet(_:)` (hig:sheets). SwiftUI-Modifier-Namen außer `sheet` nicht aus dem Spiegel.

**Typische Fehler:**
- Sheet öffnet Sheet (Stapel).
- Nur Done-Button, kein Cancel/Back.
- Komplexer Mehrschritt-Editor im Sheet statt Full-screen/Fenster.
- Swipe-down verwirft Änderungen ohne Rückfrage.

---

## Windows
**Zweck:** Rahmen für UI und Inhalte einer App, mit Systemsteuerelementen zum Öffnen, Schließen, Verschieben und Skalieren. **Plattformen:** ipados, macos (auch visionos; nicht unterstützt in iOS, tvOS, watchOS).

**Verwenden, wenn:** Multitasking oder Kontexterhalt profitiert (z. B. Mail-Compose in eigenem Fenster); Primärfenster für Hauptnavigation, Hilfsfenster (auxiliary) für eine abgeschlossene Aufgabe ohne Navigation in andere Bereiche (hig:windows).
**Nicht verwenden, wenn:** neue Fenster standardmäßig und übermäßig geöffnet würden (hig:windows#Best-practices).

**Kernregeln:**
- Fenster fließend an alle Größen anpassen (Multitasking/Multiwindow) (hig:windows#Best-practices).
- Neue Fenster gezielt öffnen; optional „In neuem Fenster öffnen“ per Context menu oder File-Menü anbieten (hig:windows#Best-practices).
- Keine eigenen Fensterrahmen/-controls, System-Look nicht nachbauen (hig:windows#Best-practices).
- Im UI „Fenster/window“ sagen, nicht „Scene“ (hig:windows#Best-practices).
- macOS: Systemdarstellung für Main/Key/Inactive nutzen; eigene Fenster müssen Zustandswechsel selbst abbilden (hig:windows#macOS-window-states).
- macOS: Keine kritischen Infos/Aktionen in die Bottom bar; nur wenig auswahlbezogene Info, sonst Inspector (hig:windows#macOS-window-states).
- iPadOS: Toolbar-Buttons am leading edge einrücken, wenn Window controls erscheinen (hig:windows#iPadOS).
- visionOS: Glass-Hintergrund beibehalten; Startgröße ohne Leerflächen, Form am Inhalt orientiert; Min-/Max-Größe festlegen; 3D-Tiefe im Fenster gering halten, sonst Volume (hig:windows#visionOS-windows).

**Plattform-Besonderheiten:**
- iPadOS: Modus Full screen (App Switcher) oder Windowed (frei skalierbar, System merkt Größe/Position); Geste (Pinch) zum Öffnen in neuem Fenster erwägen; für reine Dateivorschau `QLPreviewSceneActivationConfiguration`, Multiwindow-Support aber Pflicht (hig:windows#iPadOS).
- macOS: Anatomie Frame (Window controls, Toolbar, selten Bottom bar) + Body; Zustände Main (eins pro App), Key (eins systemweit, nimmt Eingaben an), Inactive (ohne Vibrancy) (hig:windows#macOS-window-anatomy, hig:windows#macOS-window-states).
- visionOS: Stile Window (default), Volume, Plain (ohne Glass). Volumes für reiche 3D-Inhalte, meist dynamische Skalierung (fixed ist Default), Baseplate-Glow, max. ein zusätzliches Ornament nicht an derselben Kante wie Toolbar/Tab bar, Ausrichtung parallel zum Boden oder blickfolgend (hig:windows#visionOS, hig:windows#visionOS-volumes).

**Kennwerte:** visionOS-Standardfenster 1280×720 pt; erstes Fenster ca. 2 m vor der Person, scheinbare Breite ca. 3 m (hig:windows#visionOS-windows). Ornaments/Baseplate-Glow ab visionOS 2 (hig:windows#visionOS-volumes).

**Umsetzung:** SwiftUI `WindowGroup`, `OpenWindowAction` (`openWindow`), `DefaultWindowStyle`, `PlainWindowStyle`, `VolumetricWindowStyle`, `ornament(visibility:attachmentAnchor:contentAlignment:ornament:)`; UIKit `UIWindow`, `UIWindowScene.ActivationInteraction`; AppKit `NSWindow` (hig:windows).

**Typische Fehler:**
- Jede Detailansicht öffnet ein neues Fenster.
- Nachgebaute Titelleiste/Ampel-Buttons.
- Wichtige Aktionen in der macOS-Bottom-bar.
- visionOS: opaker Hintergrund statt Glass, zu große leere Startfenster, keine Größengrenzen.

---

## Abgrenzung: Bestätigung und Nebenaufgabe

**Bestätigung / Entscheidung**
| Situation | Komponente | Beleg |
|---|---|---|
| Unerwartetes Problem, kritische Info, seltene nicht rückgängig machbare Datenvernichtung, Kaufbestätigung | Alert (`alert`) | (hig:alerts), (hig:alerts#Best-practices) |
| Wahlmöglichkeiten zu einer vom Nutzer bewusst ausgelösten Aktion (Löschen/Sichern/Weiter bearbeiten) | Action sheet (SwiftUI: `confirmationDialog`) | (hig:action-sheets#Best-practices) |
| Optionen, die die Person selbst aufruft | Menu, nicht Action sheet | (hig:action-sheets#iOS-iPadOS) |
| Häufige, rückgängig machbare Aktion | keine Rückfrage, Undo | (hig:alerts#Best-practices) |
| Reine Info | In-Kontext-Hinweis statt Alert | (hig:alerts#Best-practices) |

„Confirmation dialog“ ist der SwiftUI-Name für die Action-sheet-Funktion, keine eigene HIG-Komponente (hig:action-sheets).

**Nebenaufgabe**
| Situation | Komponente | Beleg |
|---|---|---|
| Wenig Info/Funktion, kurz, am Control verankert, regular width / macOS | Popover | (hig:popovers#Best-practices) |
| Abgegrenzte, einfache Aufgabe mit Rückkehr zum Kontext | Sheet (iPhone: Detents) | (hig:sheets) |
| Ergänzende Werkzeuge bei weiterlaufender Hauptaufgabe | iOS/iPadOS nicht-modales Sheet, macOS Panel, visionOS Split view | (hig:sheets#Best-practices) |
| Komplex, lang, Medien/Kamera, Mehrschritt-Bearbeitung | iOS/iPadOS Full-screen-Modal; macOS neues Fenster/Vollbild; visionOS Full Space | (hig:sheets#Best-practices), (hig:modality#Best-practices) |
| Compact size class | Sheet statt Popover | (hig:popovers#iOS-iPadOS) |

**Unklarheiten im Spiegel:**
- Mail-Beispiel: Action-sheets-Seite nennt zwei Optionen (Entwurf löschen/sichern), Alerts-Seite drei (zusätzlich „weiter bearbeiten“) (hig:action-sheets#Best-practices vs. hig:alerts#iOS-iPadOS).
- Destructive-Style: Action sheets → destruktive Optionen stets hervorheben; Alerts → nur bei nicht bewusst gewählter destruktiver Aktion. Kein Widerspruch im engeren Sinn (verschiedene Komponenten), aber bei Umsetzung beachten.
- Sheet-Buttons in Mehrschritt-Flows: Seite verweist auf Abbildungen (erster/folgender/letzter Schritt), der Text nennt keine konkrete Platzierung (hig:sheets#iOS-iPadOS).
