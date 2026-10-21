# Layout and organization – Komponenten
> Quelle: Apple HIG, lokaler Spiegel (Stand 2026-10-21). Paraphrasiert. Belege: `(hig:<slug>)`, `(hig:<slug>#Anchor)`.

Komponenten zum Gruppieren, Gliedern und Navigieren von Inhalten: von einfachen Containern (Box, Label) über datengetriebene Ansichten (List/Table, Collection, Outline, Column) bis zu Strukturcontainern (Split view, Tab view). Mehrere davon sind nur für macOS (Column, Outline, Tab view) bzw. nur tvOS (Lockups) definiert (hig:layout-and-organization).

Inhalt: [Boxes](#boxes) · [Collections](#collections) · [Column views](#column-views) · [Disclosure controls](#disclosure-controls) · [Labels](#labels) · [Lists and tables](#lists-and-tables) · [Lockups](#lockups) · [Outline views](#outline-views) · [Split views](#split-views) · [Tab views](#tab-views)

---

## Boxes
**Zweck:** Grenzt eine Gruppe logisch zusammengehöriger Inhalte und Controls per Rahmen oder Hintergrund sichtbar ab, optional mit Titel. **Plattformen:** ios, ipados, macos (visionos); nicht unterstützt in tvOS, watchOS.

**Verwenden, wenn:** ein überschaubarer Teilbereich einer Ansicht als zusammengehörig erkennbar sein soll (z. B. Optionsgruppe in Settings). **Nicht verwenden, wenn:** die Box fast den ganzen Container füllt oder Untergruppen durch verschachtelte Boxen entstehen sollen.

**Kernregeln:**
- Halte die Box deutlich kleiner als die umgebende Ansicht – nähert sie sich Fenster-/Bildschirmgröße, verliert sie ihre Trennwirkung (hig:boxes#Best-practices).
- Gliedere innerhalb einer Box über Padding und Ausrichtung statt über verschachtelte Boxen (hig:boxes#Best-practices).
- Setze einen knappen Titel, wenn er den Zusammenhang klärt; er hilft auch VoiceOver-Nutzern, den Inhalt vorherzusehen (hig:boxes#Content).
- Formuliere den Titel als kurze beschreibende Phrase in Satzschreibweise (sentence-style capitalization), ohne Schlusszeichen – Ausnahme: in einem Settings-Pane endet der Titel mit Doppelpunkt (hig:boxes#Content).

**Plattform-Besonderheiten:**
- iOS/iPadOS: Standardmäßig secondary bzw. tertiary background color (hig:boxes#iOS-iPadOS).
- macOS: Titel steht standardmäßig über der Box (hig:boxes#macOS).

**Kennwerte:** keine im Spiegel.
**Umsetzung:** SwiftUI `GroupBox`; AppKit `NSBox`.
**Typische Fehler:**
- Box-in-Box-Verschachtelung für Untergruppen → unruhig, eingeengt.
- Box über (fast) die gesamte Fensterfläche.
- Titel mit Punkt oder in Title Case (außerhalb von Settings-Panes auch mit Doppelpunkt).

---

## Collections
**Zweck:** Stellt eine geordnete Menge von Inhalten in anpassbarem, stark visuellem Layout (Zeile oder Raster) dar, ideal für bildbasierte Inhalte. **Plattformen:** ios, ipados, macos (tvos, visionos); nicht unterstützt in watchOS.

**Verwenden, wenn:** primär Bilder/visuelle Elemente oder Elemente stark unterschiedlicher Größe gezeigt werden. **Nicht verwenden, wenn:** überwiegend Text dargestellt wird → List/Table (hig:collections#Best-practices).

**Kernregeln:**
- Nutze nach Möglichkeit das Standard-Zeilen- oder Rasterlayout; vermeide auffällige Custom-Layouts (hig:collections#Best-practices).
- Ziehe für Text eine Tabelle/Liste vor (hig:collections#Best-practices).
- Mache Elemente leicht auswählbar; gib Bildern genug Padding, damit Fokus-/Hover-Effekte sichtbar bleiben und nichts überlappt (hig:collections#Best-practices).
- Ergänze eigene Gesten nur bei Bedarf; Standard: Tippen = Auswahl, Halten = Bearbeiten, Wischen = Scrollen (hig:collections#Best-practices).
- Gib beim Einfügen, Löschen, Umsortieren Feedback per Animation (Standard- oder Custom-Animation) (hig:collections#Best-practices).

**Plattform-Besonderheiten:**
- iOS/iPadOS: Dynamische Layoutwechsel vorsichtig einsetzen, nachvollziehbar halten und möglichst nicht während der Interaktion ändern, außer auf explizite Aktion hin (hig:collections#iOS-iPadOS).
- macOS, tvOS, visionOS: keine zusätzlichen Hinweise.

**Kennwerte:** keine im Spiegel.
**Umsetzung:** UIKit `UICollectionView`; AppKit `NSCollectionView`. SwiftUI: im Spiegel kein Typ genannt (üblich `LazyVGrid`/`LazyHGrid` – nicht aus dem Spiegel belegt).
**Typische Fehler:**
- Textlastige Inhalte im Raster statt in einer Liste.
- Zu wenig Abstand → Fokus-/Hover-Effekte überlappen Nachbarn.
- Layout springt ohne Nutzeraktion um.

---

## Column views
**Zweck:** Navigation durch eine Datenhierarchie über eine Folge vertikaler Spalten (auch *browser*), je Spalte eine Ebene. **Plattformen:** macos; nicht unterstützt in iOS, iPadOS, tvOS, visionOS, watchOS.

**Verwenden, wenn:** eine tiefe Hierarchie vorliegt, in der häufig zwischen Ebenen hin- und hergesprungen wird, und keine Sortierung wie in List/Table nötig ist (Beispiel Finder-Spaltenansicht) (hig:column-views#Best-practices). **Nicht verwenden, wenn:** Sortierung nach Spalten benötigt wird (→ Table/Outline view) oder auf iPadOS/visionOS – dort Split view (hig:column-views).

**Kernregeln:**
- Zeige die Wurzelebene in der ersten Spalte (hig:column-views#Best-practices).
- Zeige Infos/Vorschau zum gewählten Element, wenn es keine Kinder hat (wie Finder: Vorschau, Datum, Typ, Größe) (hig:column-views#Best-practices).
- Lass Spaltenbreiten verändern, besonders bei langen Elementnamen (hig:column-views#Best-practices).
- Kennzeichne Elternelemente mit Kindern durch ein Dreieck-Symbol (Standardverhalten) (hig:column-views).

**Plattform-Besonderheiten:** nur macOS.
**Kennwerte:** keine im Spiegel.
**Umsetzung:** AppKit `NSBrowser`. SwiftUI/UIKit: kein Typ im Spiegel.
**Typische Fehler:**
- Leere letzte Spalte bei Blattelementen statt Detailinformation.
- Feste Spaltenbreiten → abgeschnittene Namen.
- Einsatz für flache, sortierbedürftige Daten.

---

## Disclosure controls
**Zweck:** Blendet Informationen und Funktionen, die zu einem Control oder einer Ansicht gehören, ein und aus. **Plattformen:** ios, ipados, macos (visionos); nicht unterstützt in tvOS, watchOS.

Zwei Varianten:
- **Disclosure triangle:** zeigt bei verborgenem Inhalt von der führenden Kante nach innen, bei sichtbarem nach unten; für Ansichten/Listen (z. B. erweiterte Exportoptionen, Finder-Listenhierarchie) (hig:disclosure-controls#Disclosure-triangles).
- **Disclosure button:** zeigt bei verborgenem Inhalt nach unten, bei sichtbarem nach oben; erweitert Funktionen eines bestimmten Controls (z. B. Save-Sheet in macOS) (hig:disclosure-controls#Disclosure-buttons).

**Verwenden, wenn:** Details/erweiterte Optionen erst bei Bedarf relevant sind (Progressive Disclosure). **Nicht verwenden, wenn:** der Inhalt für die Hauptaufgabe ständig nötig ist.

**Kernregeln:**
- Verstecke Details, bis sie relevant werden; häufig genutzte Controls bleiben oben sichtbar, Fortgeschrittenes ist standardmäßig eingeklappt (hig:disclosure-controls#Best-practices).
- Beschrifte Disclosure triangles beschreibend, sodass klar ist, was ein-/ausgeblendet wird (z. B. „Advanced Options“) (hig:disclosure-controls#Disclosure-triangles).
- Platziere einen Disclosure button nahe dem Inhalt, den er steuert (hig:disclosure-controls#Disclosure-buttons).
- Verwende höchstens einen Disclosure button pro Ansicht (hig:disclosure-controls#Disclosure-buttons).

**Plattform-Besonderheiten:**
- iOS, iPadOS, visionOS: verfügbar über SwiftUI `DisclosureGroup` (hig:disclosure-controls#iOS-iPadOS-visionOS).
- macOS: keine zusätzlichen Hinweise.

**Kennwerte:** keine im Spiegel.
**Umsetzung:** SwiftUI `DisclosureGroup`; AppKit `NSButton.BezelStyle.disclosure` (Triangle) und `NSButton.BezelStyle.pushDisclosure` (Button).
**Typische Fehler:**
- Unbeschriftetes Dreieck, Inhalt nicht vorhersehbar.
- Mehrere Disclosure buttons in einer Ansicht.
- Wichtige Standardoptionen hinter Disclosure versteckt.

---

## Labels
**Zweck:** Statischer, nicht editierbarer (oft kopierbarer) Text in Buttons, Menüeinträgen, Listen und Ansichten. **Plattformen:** ios, ipados, macos, watchos (tvos, visionos).

**Verwenden, wenn:** wenig Text angezeigt wird, der nicht bearbeitet werden muss. **Nicht verwenden, wenn:** Text bearbeitbar sein soll (kurz → Text field) oder viel Text angezeigt/optional bearbeitet wird (→ Text view) (hig:labels#Best-practices).

**Kernregeln:**
- Nutze Labels nur für kurze, nicht editierbare Texte (hig:labels#Best-practices).
- Bevorzuge Systemschriften; Labels unterstützen Dynamic Type standardmäßig (wo verfügbar) – bei Custom-Fonts/Stilen Lesbarkeit sicherstellen (hig:labels#Best-practices).
- Staffle Wichtigkeit über die vier System-Label-Farben statt eigener Grautöne (hig:labels#Best-practices):
  - Label – Primärinformation (`label` / `labelColor`)
  - Secondary label – Unterüberschrift, Ergänzung (`secondaryLabel` / `secondaryLabelColor`)
  - Tertiary label – nicht verfügbares Element/Verhalten (`tertiaryLabel` / `tertiaryLabelColor`)
  - Quaternary label – Wasserzeichen (`quaternaryLabel` / `quaternaryLabelColor`)
- Mache nützlichen Text auswählbar/kopierbar (Fehlermeldung, Ort, IP-Adresse) (hig:labels#Best-practices).

**Plattform-Besonderheiten:**
- macOS: Nicht editierbarer Text über `NSTextField` mit `isEditable = false` (hig:labels#macOS).
- watchOS: System-Text-Komponenten für Datum/Uhrzeit und Countdown/Count-up-Timer; konfigurierbar (Formate, Kalender, Zeitzonen), passen sich automatisch dem Platz an und aktualisieren sich ohne App-Zutun; für Complications empfohlen (hig:labels#watchOS).
- iOS, iPadOS, tvOS, visionOS: keine zusätzlichen Hinweise.

**Kennwerte:** 4 System-Label-Farben (hig:labels#Best-practices).
**Umsetzung:** SwiftUI `Label`, `Text`; UIKit `UILabel`; AppKit `NSTextField`.
**Typische Fehler:**
- Hartkodierte Grautöne statt semantischer Label-Farben (bricht Dark Mode/Kontrast).
- Fehlermeldungen/IDs nicht kopierbar.
- Label für bearbeitbaren Text missbraucht.
- Custom-Font ohne Dynamic-Type-Unterstützung.

---

## Lists and tables
**Zweck:** Daten in Zeilen über eine oder mehrere Spalten darstellen, gruppiert oder hierarchisch, mit Auswahl, Hinzufügen, Löschen, Umsortieren. **Plattformen:** ios, ipados, macos, watchos (tvos, visionos).

**Verwenden, wenn:** Text gut scanbar sein soll, Informationshierarchien navigiert werden (iOS Settings), Optionen gewählt werden oder mehrspaltige, sortierbare Daten (Produktivität) vorliegen. **Nicht verwenden, wenn:** Elemente stark in der Größe variieren oder viele Bilder gezeigt werden → Collection (hig:lists-and-tables#Best-practices); hierarchische Daten auf macOS → Outline view (hig:lists-and-tables#macOS).

**Kernregeln:**
- Stelle Text bevorzugt in Listen/Tabellen dar (hig:lists-and-tables#Best-practices).
- Erlaube Bearbeiten, wo sinnvoll – mindestens Umsortieren wird geschätzt; iOS/iPadOS: Auswahl von Zeilen erst im Edit-Modus (hig:lists-and-tables#Best-practices).
- Gib passendes Auswahl-Feedback: Navigationslisten halten die Auswahl dauerhaft hervorgehoben; Optionslisten heben kurz hervor und setzen dann z. B. ein Häkchen (hig:lists-and-tables#Best-practices).
- Halte Zeilentexte knapp; bei langen Inhalten nur Titel listen und Details in einer Detailansicht zeigen (hig:lists-and-tables#Content).
- Erwäge Mitten-Ellipse bei schmalen Tabellen, um Anfang und Ende erkennbar zu halten (hig:lists-and-tables#Content).
- Benenne Spalten mit Nomen/kurzen Nominalphrasen in Title Case ohne Schlusszeichen; einspaltige Tabelle ohne Header → Kontext per Label/Header (hig:lists-and-tables#Content).
- Wähle Listen-/Tabellenstil passend zu Daten und Plattform (iOS grouped, watchOS elliptical, macOS bordered mit alternierenden Zeilen) (hig:lists-and-tables#Style).
- Nutze eingebaute Zeilenstile (z. B. `UIListContentConfiguration`) (hig:lists-and-tables#Style).

**Plattform-Besonderheiten:**
- iOS, iPadOS, visionOS: Info-Button (in Zeile: *detail disclosure button*) nur für Zusatzinfos, nicht zur Navigation – für Drill-down Disclosure indicator verwenden. Kein Index (Alphabetleiste) bei Tabellen mit Controls am trailing Rand, da Fehlbedienung droht (hig:lists-and-tables#iOS-iPadOS-visionOS).
- macOS: Sortieren per Klick auf Spaltenkopf, erneuter Klick kehrt Richtung um; Spaltenbreiten veränderbar; alternierende Zeilenfarben in mehrspaltigen Tabellen erwägen; Hierarchie → Outline view (hig:lists-and-tables#macOS).
- tvOS: Fokussierte Zeile wird hervorgehoben, leicht vergrößert, ggf. mit runden Ecken – benachbarte Bilder darauf prüfen, keine eigenen Rundungsmasken (hig:lists-and-tables#tvOS).
- watchOS: Zeilenzahl möglichst begrenzen, aber erwartete lange Listen vollständig zugänglich machen (relevanteste zuerst + „mehr“); Detailansichten kurz halten, damit vertikale seitenbasierte Navigation funktioniert – scrollende Details verhindern sie (hig:lists-and-tables#watchOS).

**Kennwerte:** keine im Spiegel.
**Umsetzung:** SwiftUI `List`, `Table` (Tables), `ListStyle`; UIKit `UITableView`, `UIListContentConfiguration`, `UITableViewCell.AccessoryType.disclosureIndicator`; AppKit `NSTableView`.
**Typische Fehler:**
- Detail disclosure button (Info) für Navigation statt Disclosure indicator.
- Alphabet-Index plus Disclosure indicators am selben Rand.
- Überlange Zeilen mit viel Fließtext.
- Navigationsliste ohne persistente Auswahlhervorhebung (iPad/Mac Split view).

---

## Lockups
**Zweck:** Fasst Content view, Header und Footer zu einer interaktiven Einheit zusammen, die bei Fokus gemeinsam wächst. **Plattformen:** nur tvos; nicht unterstützt in iOS, iPadOS, macOS, visionOS, watchOS. Für den Fokus dieses Plugins nur als Referenz relevant.

Typen: Cards (Ratings/Reviews), Caption buttons (Bild oder Text mit Titel/Untertitel), Monograms (Personen, rundes Bild bzw. Initialen), Posters (Bild, Titel/Untertitel erst bei Fokus sichtbar) (hig:lockups).

**Kernregeln:**
- Lass genug Abstand zwischen Lockups, da sie sich bei Fokus vergrößern (hig:lockups#Best-practices).
- Halte Größen innerhalb einer Zeile/Gruppe einheitlich (hig:lockups#Best-practices).
- Lass Caption buttons bei Fokus mit der Wischrichtung kippen (vertikal angeordnet: auf/ab; horizontal: links/rechts; Raster: beide) (hig:lockups#Caption-buttons).
- Bevorzuge bei Monograms Bilder statt Initialen (hig:lockups#Monograms).
- Wähle Poster-Größe passend zum Inhalt (hig:lockups#Posters).

**Plattform-Besonderheiten:** nur tvOS.
**Kennwerte:** 4 Lockup-Typen (hig:lockups).
**Umsetzung:** TVUIKit `TVLockupView`, `TVLockupHeaderFooterView`, `TVCardView`, `TVCaptionButtonView`, `TVMonogramContentView`, `TVPosterView`.
**Typische Fehler:**
- Zu enge Anordnung → fokussiertes Lockup überlappt Nachbarn.
- Gemischte Größen in einer Reihe.

---

## Outline views
**Zweck:** Hierarchische Daten als scrollende, in Spalten und Zeilen organisierte Liste mit Disclosure triangles für Elterncontainer. **Plattformen:** macos; nicht unterstützt in iOS, iPadOS, tvOS, visionOS, watchOS.

**Verwenden, wenn:** textbasierte hierarchische Daten (z. B. Dateisystem im Finder) gezeigt werden, oft im leading Pane eines Split view (hig:outline-views#Best-practices). **Nicht verwenden, wenn:** Daten nicht hierarchisch sind → Table (hig:outline-views#Best-practices).

**Kernregeln:**
- Zeige die Hierarchie nur in der ersten Spalte; weitere Spalten enthalten Attribute (hig:outline-views#Best-practices).
- Vergib in mehrspaltigen Outline views immer Spaltenköpfe (Nomen, Title Case, keine Satzzeichen, insbesondere kein Doppelpunkt); einspaltig ohne Kopf → Kontext anders herstellen (hig:outline-views#Best-practices).
- Erlaube Sortieren per Spaltenkopf; Sortierung über Primärspalte wirkt pro Hierarchieebene, erneuter Klick kehrt um (hig:outline-views#Best-practices).
- Lass Spaltenbreiten anpassen (hig:outline-views#Best-practices).
- Mache Auf-/Zuklappen einfach; Option-Klick auf das Dreieck klappt alle Unterebenen auf (Finder-Konvention) (hig:outline-views#Best-practices).
- Merke dir den Aufklappzustand und stelle ihn beim nächsten Mal wieder her (hig:outline-views#Best-practices).
- Erlaube Bearbeiten, wo sinnvoll: Einfachklick editiert Zelle, Doppelklick kann anders reagieren (z. B. Datei öffnen) (hig:outline-views#Best-practices).
- Kürze Zellentext mit Mitten-Ellipse statt abzuschneiden; erwäge alternierende Zeilenfarben und ein Search field in der Toolbar bei langen Listen (hig:outline-views#Best-practices).

**Plattform-Besonderheiten:** nur macOS.
**Kennwerte:** keine im Spiegel.
**Umsetzung:** SwiftUI `OutlineGroup`; AppKit `NSOutlineView`.
**Typische Fehler:**
- Hierarchie-Einrückung in mehreren Spalten.
- Aufklappzustand geht beim Neustart verloren.
- Fehlende Spaltenköpfe in mehrspaltiger Ansicht.

---

## Split views
**Zweck:** Verwaltet mehrere nebeneinanderliegende Panes (primär, sekundär, optional tertiär), typisch zur gleichzeitigen Anzeige mehrerer Hierarchieebenen, oft mit Sidebar. **Plattformen:** ios, ipados, macos, watchos (tvos, visionos).

**Verwenden, wenn:** Hierarchie-Navigation mit Detailansicht (Mail), ergänzende Funktionsbereiche um eine Hauptfläche (Keynote: Navigator, Notizen, Inspector) oder in visionOS Zusatzinfos ohne neues Fenster gezeigt werden. **Nicht verwenden, wenn:** kompakte Umgebung (iPhone hochkant) – Inhalte würden umbrechen/abgeschnitten (hig:split-views#iOS).

**Kernregeln:**
- Hebe die aktuelle Auswahl in jedem Pane, das zur Detailansicht führt, dauerhaft hervor (hig:split-views#Best-practices).
- Erwäge Drag and Drop zwischen Panes (hig:split-views#Best-practices).
- iOS: Setze Split views bevorzugt in regular, nicht compact size class ein (hig:split-views#iOS).
- iPadOS: Plane für schmale, kompakte und mittlere Fensterbreiten; Navigation zwischen Panes muss in jeder Breite logisch bleiben (hig:split-views#iPadOS).
- macOS: Setze sinnvolle Min-/Max-Pane-Größen, damit der Divider sichtbar bleibt (hig:split-views#macOS).
- macOS: Erlaube das Ausblenden von Panes und biete mehrere Wege zum Wiederherstellen (Toolbar-Button, Menübefehl mit Shortcut) (hig:split-views#macOS).
- macOS: Bevorzuge den dünnen Divider; dicker nur bei konkretem Bedarf (z. B. starke Linien in angrenzenden Tabellen) (hig:split-views#macOS).

**Plattform-Besonderheiten:**
- iOS: nur in regular environment empfohlen (hig:split-views#iOS).
- iPadOS: zwei (Mail) oder drei (Keynote) vertikale Panes; Fenster frei skalierbar → mehrere Breiten berücksichtigen (hig:split-views#iPadOS).
- macOS: Panes vertikal, horizontal oder kombiniert; Divider ziehbar (`VSplitView`/`HSplitView`) (hig:split-views#macOS).
- tvOS: gut zum Filtern (Kategorie links, Ergebnisse rechts); ein gemeinsamer Titel über dem Split view, keine Pane-Titel; Titelausrichtung: zentriert bei Collection im Sekundär-Pane, über Primär-Pane bei Einzelinhalt (hig:split-views#tvOS).
- visionOS: für Zusatzinfos Split view statt neuem Fenster; kurze Pflichtaufgabe → Sheet (hig:split-views#visionOS).
- watchOS: zeigt Liste oder Detail jeweils als Vollbild; beim Start relevanteste Detailansicht zeigen (Ort, Zeit, letzte Aktionen); mehrere Detailseiten als vertikaler Tab view (Digital Crown, Page indicator) (hig:split-views#watchOS).

**Kennwerte:**
- macOS thin divider: 1 pt breit (hig:split-views#macOS).
- tvOS Standardaufteilung: Primär-Pane 1/3, Sekundär-Pane 2/3 der Bildschirmbreite; alternativ 1/2 zu 1/2 (hig:split-views#tvOS).
- iPadOS: 2 oder 3 vertikale Panes (hig:split-views#iPadOS).

**Umsetzung:** SwiftUI `NavigationSplitView` (macOS zusätzlich `VSplitView`, `HSplitView`); UIKit `UISplitViewController`; AppKit `NSSplitViewController`, `NSSplitView.DividerStyle`.
**Typische Fehler:**
- Split view auf iPhone hochkant erzwingen.
- Auswahl im Primär-Pane nicht hervorgehoben → Orientierung geht verloren.
- Pane lässt sich auf Breite null ziehen, Divider „verschwindet“.
- Ausgeblendetes Pane nur über einen einzigen, versteckten Weg wiederherstellbar.

---

## Tab views
**Zweck:** Mehrere sich gegenseitig ausschließende Inhaltsbereiche im selben Bereich, umschaltbar über ein Tab-Control. **Plattformen:** macos, watchos; nicht unterstützt in iOS, iPadOS, tvOS, visionOS. Abgrenzung: nicht zu verwechseln mit der Tab bar (App-Navigation) (hig:tab-bars).

**Verwenden, wenn:** eng verwandte Inhaltsbereiche (z. B. Einstellungsgruppen in einem Fenster) gezeigt werden. **Nicht verwenden, wenn:** auf iOS/iPadOS → Segmented control (hig:tab-views#iOS-iPadOS); sehr viele Panes → Pop-up-Button-Menü (hig:tab-views#Best-practices).

**Kernregeln:**
- Fasse nur eng verwandte Inhalte in Tabs zusammen (hig:tab-views#Best-practices).
- Controls in einem Pane wirken nur auf dieses Pane; Panes sind in sich abgeschlossen (hig:tab-views#Best-practices).
- Beschrifte Tabs mit Nomen/kurzen Nominalphrasen (selten Verben) in Title Case (hig:tab-views#Best-practices).
- Schalte nicht per Pop-up-Button zwischen Tabs um (zwei statt ein Klick, Optionen nicht sichtbar) – außer bei zu vielen Panes (hig:tab-views#Best-practices).
- Begrenze die Tab-Anzahl (siehe Kennwerte) (hig:tab-views#Best-practices).
- Rücke den Tab view mit Rand zum Fensterkörper ein; bis an die Fensterkanten ist unüblich (hig:tab-views#Anatomy).
- Tab-Control sitzt an der Oberkante; Ausblenden nur bei programmatischem Umschalten – Inhalt dann borderless (solid/transparent), bezeled oder mit Linie umrandet (hig:tab-views#Anatomy).

**Plattform-Besonderheiten:**
- iOS/iPadOS: nicht unterstützt; Segmented control als Ersatz (hig:tab-views#iOS-iPadOS).
- watchOS: Tab views werden mit Page controls dargestellt (SwiftUI `TabView`) (hig:tab-views#watchOS).

**Kennwerte:** max. 6 Tabs. **Unklarheit im Spiegel:** Der Abschnitt sagt einerseits „nicht mehr als sechs“, andererseits „bei sechs oder mehr“ Alternativen erwägen – im Zweifel ≤ 5–6 und ab 6 Alternative prüfen (hig:tab-views#Best-practices).
**Umsetzung:** SwiftUI `TabView`; AppKit `NSTabView`.
**Typische Fehler:**
- Controls in einem Tab, die Inhalte anderer Tabs ändern.
- Zu viele Tabs statt Pop-up-Button.
- Tab view auf iOS nachgebaut statt Segmented control.
- Verwechslung mit Tab bar für App-weite Navigation.
