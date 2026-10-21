# Navigation and search – Komponenten
> Quelle: Apple HIG, lokaler Spiegel (Stand 2026-10-21). Paraphrasiert. Belege: `(hig:<slug>)`, `(hig:<slug>#Anchor)`.

Komponenten für die Top-Level-Navigation (Tab bar, Sidebar), für Suche (Search field inkl. Scope bar und Tokens) sowie zwei macOS-spezifische Felder (Path control, Token field). Kernentscheidung für iOS/iPadOS: zuerst Tab bar, bei komplexer Struktur Tab bar mit Sidebar-Adaption, nur Sidebar über `NavigationSplitView` (hig:sidebars#iOS-iPadOS).

Inhalt: [Tab bars](#tab-bars) · [Sidebars](#sidebars) · [Tab bar vs. Sidebar](#abgrenzung-tab-bar-vs-sidebar) · [Search fields](#search-fields) · [Token fields](#token-fields) · [Path controls](#path-controls)

## Tab bars
**Zweck:** Wechsel zwischen den Top-Level-Bereichen einer App, wobei jeder Bereich seinen Navigationszustand behält (hig:tab-bars). **Plattformen:** ios, ipados, macos (laut Plattformzeile; keine macOS-spezifischen Hinweise), (tvos, visionos); nicht unterstützt in watchOS.
**Verwenden, wenn:** wenige, gleichrangige Hauptbereiche dauerhaft erreichbar sein sollen. **Nicht verwenden, wenn:** Aktionen auf den aktuellen Inhalt gebraucht werden → Toolbar (hig:tab-bars#Best-practices); sehr komplexe Informationsstruktur → Sidebar bzw. adaptive Tab bar.
**Kernregeln:**
- Tab bar nur für Navigation einsetzen, nie für Aktionen (hig:tab-bars#Best-practices).
- Tab bar beim Navigieren sichtbar lassen; Ausnahme: ein modaler View überdeckt sie (hig:tab-bars#Best-practices).
- Anzahl Tabs knapp halten; weniger Tabs sind leichter zu navigieren (hig:tab-bars#Best-practices).
- Overflow vermeiden – sonst wird der letzte Tab in iOS/iPadOS zum „More“-Tab, dessen Inhalte schlecht auffindbar sind (hig:tab-bars#Best-practices).
- Tabs nie deaktivieren oder ausblenden; leeren Bereich stattdessen erklären (hig:tab-bars#Best-practices).
- Jeden Tab beschriften, möglichst mit einem Wort (hig:tab-bars#Best-practices).
- SF Symbols verwenden, bevorzugt gefüllte Varianten; sie passen sich compact (Icon über Label) und regular (nebeneinander) an (hig:tab-bars#Best-practices).
- Badges (rotes Oval, weiße Zahl oder Ausrufezeichen) nur für kritische Informationen (hig:tab-bars#Best-practices).
- Tab-Label-Farbe deutlich von farbigem Content abheben; bei buntem Content monochrome Tab bar bevorzugen (hig:tab-bars#Best-practices).
**Plattform-Besonderheiten:**
- iOS: schwebt unten auf Liquid Glass. Mit Accessory (z. B. MiniPlayer) kann die Tab bar beim Scrollen minimiert werden; Rückkehr per Tab-Tap oder Scroll nach oben. Dedizierter Search-Tab am trailing Ende möglich (hig:tab-bars#iOS).
- iPadOS: sitzt oben; fest (`tabBarOnly`) oder mit Button zur Umwandlung in eine Sidebar (`sidebarAdaptable`). Tab bar bevorzugen; Anpassung durch Nutzer erlauben (hig:tab-bars#iPadOS).
- visionOS: immer vertikal am leading Rand, expandiert beim Anschauen; Symbol und kurzes Label je Tab; Sidebar innerhalb eines Tabs möglich, Sidebar-Auswahl darf Tab nicht wechseln (hig:tab-bars#visionOS).
- tvOS: stark anpassbar, transluzent; scrollt bei Einzelansicht offscreen, bleibt bei Split view fixiert; Live-Viewing-Reihenfolge: Live, Aufzeichnungen, Sonstiges (hig:tab-bars#tvOS).
- macOS: im Spiegel keine zusätzlichen Hinweise.
**Kennwerte:** iPadOS: bei anpassbaren Tabs Default-Liste von fünf oder weniger (hig:tab-bars#iPadOS). tvOS: Höhe 68 pt, Oberkante 46 pt vom Bildschirmrand, nicht änderbar (hig:tab-bars#tvOS). Icon-Maße für Custom-Icons: nicht im Spiegel, Verweis auf Apple Design Resources.
**Umsetzung:** SwiftUI `TabView` (Styles `tabBarOnly`, `sidebarAdaptable`), `TabViewCustomization`, `TabBarMinimizeBehavior`, `TabViewBottomAccessoryPlacement`; UIKit `UITabBar`/`UITabBarController` (`UITabBarController.MinimizeBehavior`, `UITab.Placement`).
**Typische Fehler:**
- Tab „Neu erstellen“ o. Ä. als Aktion statt Toolbar-Button.
- Tabs je nach Zustand ausgrauen/entfernen.
- Zu viele Tabs → More-Tab auf iPhone.
- Badge als Marketing-Hinweis statt für kritische Info.

## Sidebars
**Zweck:** Navigation am leading Rand zwischen App-Bereichen oder Top-Level-Sammlungen (Ordner, Playlists) (hig:sidebars). **Plattformen:** ios, ipados, macos, (tvos ohne Zusatzhinweise, visionos); nicht unterstützt in watchOS.
**Verwenden, wenn:** viele Bereiche bzw. nutzerdefinierte Sammlungen, genug Platz (benötigt viel vertikalen und horizontalen Raum). **Nicht verwenden, wenn:** Platz knapp ist oder Content Vorrang hat → Tab bar (hig:sidebars); Hierarchie > 2 Ebenen → Split view mit Content-Liste (hig:sidebars#Best-practices).
**Kernregeln:**
- Visuell reichen Content unter die (Liquid-Glass-)Sidebar ziehen – per horizontalem Scrollen oder Background-Extension-Effekt (hig:sidebars#Best-practices).
- Inhalte und Reihenfolge möglichst vom Nutzer anpassbar machen (hig:sidebars#Best-practices).
- Viel Inhalt mit Disclosure controls gruppieren (hig:sidebars#Best-practices).
- SF Symbols bzw. Custom Symbols statt Bitmaps verwenden (hig:sidebars#Best-practices).
- Ausblenden ermöglichen (iPadOS Edge-Swipe, macOS Button bzw. View-Menü „Show/Hide Sidebar“), aber nicht standardmäßig verstecken (hig:sidebars#Best-practices).
- Höchstens zwei Hierarchieebenen; Gruppentitel kurz und beschreibend (hig:sidebars#Best-practices).
- Icon-Farbe = Accent color (macOS: folgt System-Accent); feste Farben nur sparsam mit klarer Bedeutung (hig:sidebars#Best-practices).
**Plattform-Besonderheiten:**
- iOS/iPadOS: Zuerst Tab bar erwägen; `sidebarAdaptable` bietet Umschalter Sidebar↔Tab bar und passt sich Rotation/Fenstergröße an. Ohne SwiftUI: List-Appearance `.sidebar` der Collection-View-Liste (hig:sidebars#iOS-iPadOS).
- macOS: Zeilenhöhe/Text/Glyph-Größe hängen von Sidebar-Größe (small/medium/large, auch per Systemeinstellung) ab; bei Fensterverkleinerung automatisch ein-/ausblenden; nichts Kritisches unten platzieren (hig:sidebars#macOS).
- visionOS: Fenster wächst für Sidebar, Ausblenden selten nötig; bei tiefer Hierarchie Sidebar innerhalb eines Tabs (hig:sidebars#visionOS).
**Kennwerte:** max. zwei Hierarchieebenen (Empfehlung) (hig:sidebars#Best-practices). Keine Maße im Spiegel.
**Umsetzung:** SwiftUI `NavigationSplitView` (nur Sidebar), `TabView` mit `.sidebarAdaptable`, `List` mit `.listStyle(.sidebar)`, `backgroundExtensionEffect()`; UIKit `UISplitViewController`, `UICollectionLayoutListConfiguration` (Appearance `.sidebar`); AppKit `NSSplitViewController`.
**Typische Fehler:**
- Sidebar auf iPhone/iPad, obwohl wenige Bereiche eine Tab bar rechtfertigen.
- Drei und mehr verschachtelte Ebenen in der Sidebar.
- Bunte Icons, die den gewählten macOS-Accent ignorieren.
- Wichtige Aktionen am unteren Sidebar-Rand (macOS).

## Abgrenzung Tab bar vs. Sidebar
| Situation | Wahl | Beleg |
|---|---|---|
| iPhone, wenige Hauptbereiche | Tab bar | (hig:tab-bars) |
| iPad, Standard | Tab bar oben (`tabBarOnly`) | (hig:tab-bars#iPadOS) |
| iPad, viele/nutzerdefinierte Bereiche | `sidebarAdaptable`: Tab bar mit Umschalter zur Sidebar; Startzustand wählbar | (hig:tab-bars#iPadOS), (hig:sidebars#iOS-iPadOS) |
| Nur Sidebar ohne Umschaltung | `NavigationSplitView` / `UISplitViewController` | (hig:tab-bars#iPadOS), (hig:sidebars#iOS-iPadOS) |
| Hierarchie > 2 Ebenen | Split view mit Content-Liste zwischen Sidebar und Detail | (hig:sidebars#Best-practices) |
| macOS | Sidebar (Tab bar ohne macOS-Hinweise im Spiegel) | (hig:sidebars#macOS) |
| visionOS, tiefe Hierarchie | Sidebar innerhalb eines Tabs | (hig:sidebars#visionOS) |
| watchOS | weder noch (beide nicht unterstützt) | (hig:tab-bars#Platform-considerations), (hig:sidebars#Platform-considerations) |

Hinweis: Bei Anpassbarkeit nennt der Spiegel für iPadOS eine Default-Tab-Liste von höchstens fünf, um compact und regular konsistent zu halten (hig:tab-bars#iPadOS).

## Search fields
**Zweck:** Editierbares Textfeld mit Lupe, Clear-Button und Placeholder zum Durchsuchen einer Content-Sammlung (hig:search-fields). **Plattformen:** ios, ipados, macos, watchos, (tvos: eigener Search-Screen; visionos ohne Zusatzhinweise).
**Verwenden, wenn:** Content-Mengen gezielt durchsucht oder gefiltert werden. **Nicht verwenden, wenn:** es um systemweite Suche geht → Pattern „Searching“ (hig:searching); feste Kategorien ohne Freitext → Scope bar/Segmented control erwägen.
**Kernregeln:**
- Placeholder nutzen, um Suchumfang/Inhaltstyp zu erklären (hig:search-fields#Best-practices).
- Suche möglichst bereits beim Tippen starten (hig:search-fields#Best-practices).
- Vorschläge zeigen: letzte Suchen vorher, Vorhersagen während der Eingabe (hig:search-fields#Best-practices).
- Relevanteste Treffer zuerst, ggf. kategorisiert (hig:search-fields#Best-practices).
- Scope bar für klar abgegrenzte Kategorien; standardmäßig breiten Scope wählen, Verengung dem Nutzer überlassen (hig:search-fields#Scope-bars-and-tokens).
- Tokens für häufige Suchbegriffe/Filter (z. B. Kontakt, „Fotos“) und mit Suchvorschlägen kombinieren, damit Tokens entdeckbar sind (hig:search-fields#Scope-bars-and-tokens).
- iPad/Mac: Sucherlebnis zwischen beiden Plattformen konsistent halten (hig:search-fields#iPadOS-macOS).
**Platzierung:**
- iOS – drei Orte: Tab in der Tab bar, Toolbar (unten oder oben), inline beim Content (hig:search-fields#iOS).
  - Search als Tab: *Standard-Tab* → eigene Landing-Page mit Vorschlägen/Entdecken (z. B. Apple TV); *Button-Appearance* → separater Button, Tastatur sofort, danach zurück zum vorherigen Tab – für schnelles, transientes Suchen (hig:search-fields#Search-as-a-tab).
  - Toolbar: unten bevorzugen, wenn Platz (Feld oder Button, öffnet über der Tastatur); oben (Navigation bar, als Button), wenn Content unten Vorrang hat oder keine Bottom-Toolbar existiert (hig:search-fields#Search-in-a-toolbar).
  - Inline: wenn Suche nur diesen View betrifft (z. B. Library-Filter); oberhalb der Liste platzieren, beim Scrollen ggf. an Top-Toolbar pinnen (hig:search-fields#Search-as-an-inline-field).
- iPadOS/macOS: Standard am trailing Ende der Toolbar (v. a. Split-View-Apps, Ergebnisse im Detail); oben in der Sidebar, wenn Sidebar/Navigation gefiltert wird (z. B. Settings); als eigenes Sidebar- oder Tab-Item für Entdecken-Bereiche (Music, TV). Im dedizierten Bereich Feld sofort fokussieren – außer iPad nur mit virtueller Tastatur. Bei compact-Fenstern Suche über die Content-Listen-Spalte legen (hig:search-fields#iPadOS-macOS).
**Plattform-Besonderheiten:**
- tvOS: spezialisierter Tastatur-Screen mit frei gestaltbaren Ergebnissen; Vorschläge und letzte Suchen anbieten (hig:search-fields#tvOS).
- watchOS: Tap öffnet bildschirmfüllende Texteingabe; Rückkehr erst nach Cancel/Search (hig:search-fields#watchOS).
**Kennwerte:** keine im Spiegel.
**Umsetzung:** SwiftUI `.searchable(text:placement:prompt:)` (Scopes/Tokens: siehe „Scoping a search operation“); UIKit `UISearchBar`, `UISearchTextField`, `UISearchController` (tvOS); AppKit `NSSearchField`.
**Typische Fehler:**
- Suche auf iPhone oben, obwohl unten Platz ist und Suche Priorität hat.
- Standard-Tab-Stil für schnelle Nachschlagesuche (oder Button-Stil für Entdecken-Apps).
- Feld auf iPad automatisch fokussieren, sodass virtuelle Tastatur den View verdeckt.
- Scope bar mit schmalem Default-Scope; Tokens ohne Vorschläge, daher unentdeckt.

## Token fields
**Zweck:** Textfeld, das Eingaben in auswählbare, verschiebbare Tokens umwandelt (z. B. Empfänger in Mail) (hig:token-fields). **Plattformen:** macos; nicht unterstützt in iOS, iPadOS, tvOS, visionOS, watchOS.
**Verwenden, wenn:** mehrere diskrete Einträge (Empfänger, Tags) als Einheiten bearbeitet, umsortiert oder zwischen Feldern gezogen werden. **Nicht verwenden, wenn:** Freitext ohne Einheiten → Text field (hig:text-fields); Suchfilter in iOS/iPadOS → Search-Tokens (hig:search-fields#Scope-bars-and-tokens).
**Kernregeln:**
- Tokens mit Context menu aufwerten (Infos, Bearbeiten) (hig:token-fields#Best-practices).
- Weitere Auslöser für Token-Umwandlung erwägen (Standard: Komma; z. B. zusätzlich Return) (hig:token-fields#Best-practices).
- Verzögerung für Vorschläge anpassen – Standard ist sofort, was beim Tippen ablenken kann (hig:token-fields#Best-practices).
- Vorschlagsliste während der Eingabe anbieten, Auswahl als Token einfügen (hig:token-fields).
**Plattform-Besonderheiten:** nur macOS.
**Kennwerte:** keine im Spiegel.
**Umsetzung:** AppKit `NSTokenField`. SwiftUI-Äquivalent im Spiegel nicht genannt (für Suche: Tokens in `.searchable`).
**Typische Fehler:**
- Tokens ohne Context menu, obwohl Zusatzinfos sinnvoll wären.
- Nur Komma als Trenner – Nutzer erwarten oft Return.
- Sofort aufpoppende Vorschläge, die die Eingabe stören.

## Path controls
**Zweck:** Zeigt den Dateisystempfad eines gewählten Elements (hig:path-controls). **Plattformen:** macos; nicht unterstützt in iOS, iPadOS, tvOS, visionOS, watchOS.
**Verwenden, wenn:** Ort einer Datei/eines Ordners sichtbar und navigierbar sein soll (z. B. Finder-Pfadleiste). **Nicht verwenden, wenn:** Platzierung in Toolbar oder Status bar geplant ist (hig:path-controls#Best-practices).
**Stile:** *Standard* – lineare Liste (Volume, Elternordner, Element) mit Icon und Name; bei Platzmangel werden mittlere Namen ausgeblendet. *Pop up* – zeigt nur das Element, Klick öffnet Menü mit dem Pfad, editierbar mit zusätzlichem „Choose“-Befehl. Beide editierbar per Drag-and-drop (hig:path-controls).
**Kernregeln:**
- Im Fensterinhalt platzieren, nicht im Fensterrahmen (Toolbar/Status bar) (hig:path-controls#Best-practices).
- Stil nach Platz wählen: Standard für volle Sichtbarkeit, Pop up für kompakte Darstellung (hig:path-controls).
- Editierbar machen, wenn Nutzer Elemente per Drag oder „Choose“ wählen sollen (hig:path-controls).
- Ohne Auswahl den Pfad des Fensterordners zeigen (Finder-Verhalten) (hig:path-controls).
**Plattform-Besonderheiten:** nur macOS.
**Kennwerte:** keine im Spiegel.
**Umsetzung:** AppKit `NSPathControl`. Kein SwiftUI-Typ im Spiegel.
**Typische Fehler:**
- Path control in die Toolbar oder Status bar setzen.
- Path control für iOS/iPadOS einplanen – dort nicht unterstützt.
- Standard-Stil bei sehr wenig Platz: mittlere Namen werden ausgeblendet, Pop up wäre klarer.

## Auffälligkeiten / Unklarheiten
- Tab bars: Plattformzeile nennt macOS, die Seite enthält aber keine macOS-Hinweise („No additional considerations for macOS“). Ob/wie eine Tab bar auf dem Mac aussieht, beschreibt der Spiegel nicht; für Mac-Fenster-Tabs siehe Tab views (hig:tab-views).
- Search fields: iOS-Begriffe wurden 2026-06-08 aktualisiert („Standard tab“ vs. „Button appearance“); ältere Quellen nennen andere Bezeichnungen.
