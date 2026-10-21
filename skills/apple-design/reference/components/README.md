# Komponenten-Katalog (Apple HIG)

> Quelle: Apple HIG, lokaler Spiegel `~/.apple-design/hig/pages/<slug>.md` (Stand 2026-10-21). Paraphrasiert. Belege: `(hig:<slug>)`, `(hig:<slug>#Anchor)`, Anchor = Überschrift mit Bindestrichen, ohne Kommas.
> Fokus: iOS, iPadOS, macOS, watchOS. tvOS und visionOS sind nur erwähnt, wenn es relevant ist.

Die Komponenten sind nach den HIG-Untergruppen auf acht Dateien verteilt. Je Komponente gibt es diese Abschnitte: Zweck · Plattformen · Verwenden/Nicht verwenden · Kernregeln · Plattform-Besonderheiten · Kennwerte · Umsetzung · Typische Fehler.

## Entscheidungshilfe: Ich will X, also nehme ich Y

### Auswahl aus wenigen Optionen
| Situation | Komponente | Beleg |
|---|---|---|
| Wenige (iPhone ca. 5, breite UI ca. 5–7) eng verwandte Optionen, Auswahl soll dauerhaft sichtbar sein | Segmented control (nicht auf watchOS) | (hig:segmented-controls#Best-practices) |
| Kurze Liste exklusiver Optionen, Platz knapp, aktuelle Auswahl im Button sichtbar | Pop-up button (SwiftUI `Picker` mit Menu-Stil) | (hig:pop-up-buttons#Best-practices), (hig:pickers#Best-practices) |
| Befehle bzw. Aktionen, die eine Aktion präzisieren (Add, Sort) | Pull-down button bzw. Menu | (hig:pull-down-buttons#Best-practices) |
| Mittlere bis lange, logisch geordnete Werteliste, Datum oder Uhrzeit | Picker / Date picker | (hig:pickers#Best-practices) |
| Sehr lange Liste | List/Table, ggf. mit Index | (hig:pickers#Best-practices) |
| macOS, 2–5 exklusive Optionen, alle sichtbar | Radio buttons, ab mehr als ca. 5 Pop-up button | (hig:toggles#Radio-buttons) |
| Wechsel zwischen getrennten App-Bereichen | Tab bar, nicht Segmented control | (hig:segmented-controls#iOS-iPadOS) |

### Ein/Aus und Werte
| Situation | Komponente | Beleg |
|---|---|---|
| iOS/iPadOS Ein/Aus in einer Liste | Switch (`Toggle`) | (hig:toggles#iOS-iPadOS) |
| iOS/iPadOS Ein/Aus außerhalb einer Liste | Button mit Toggle-Verhalten | (hig:toggles#iOS-iPadOS) |
| macOS: einzelnes Setting / betonte oder gruppensteuernde Setting | Checkbox bzw. Switch | (hig:toggles#Checkboxes), (hig:toggles#Switches) |
| Kontinuierlicher Wert in einem Bereich | Slider | (hig:sliders#Best-practices) |
| Kleine schrittweise Änderung | Stepper, bei großen Sprüngen zusätzlich Text field | (hig:steppers#Best-practices) |
| Wert relativ zu einer Skala anzeigen (nicht eingeben) | Gauge | (hig:gauges) |
| Fortschritt eines laufenden Vorgangs | Progress indicator | (hig:progress-indicators) |

### Bestätigung und Rückfrage
| Situation | Komponente | Beleg |
|---|---|---|
| Unerwartetes Problem, kritische Info, seltene nicht rückgängig machbare Datenvernichtung | Alert (`alert`) | (hig:alerts#Best-practices) |
| Optionen zu einer Aktion, die die Person bewusst ausgelöst hat (Löschen/Sichern) | Action sheet, in SwiftUI `confirmationDialog` | (hig:action-sheets#Best-practices) |
| Optionen, die die Person selbst aufruft | Menu, kein Action sheet | (hig:action-sheets#iOS-iPadOS) |
| Häufige, rückgängig machbare Aktion | keine Rückfrage, stattdessen Undo | (hig:alerts#Best-practices) |
| Fehler, während die App im Hintergrund ist | kein Fehler-Push; Fehler gehören in einen Alert | (hig:notifications#Best-practices) |

„Confirmation dialog“ ist keine eigene HIG-Komponente, sondern die SwiftUI-API für Action sheets (siehe presentation.md).

### Nebenaufgabe und modale Darstellung
| Situation | Komponente | Beleg |
|---|---|---|
| Wenig Inhalt, kurzlebig, am auslösenden Control verankert (regular width, macOS) | Popover | (hig:popovers#Best-practices) |
| In compact size class | Sheet statt Popover | (hig:popovers#iOS-iPadOS) |
| Abgegrenzte, einfache Aufgabe mit Rückkehr zum Kontext | Sheet (iPhone: Detents) | (hig:sheets#Best-practices) |
| Werkzeuge neben weiterlaufender Hauptaufgabe | iOS/iPadOS nicht-modales Sheet, macOS Panel | (hig:sheets#Best-practices), (hig:panels) |
| Komplexe, lange oder medienlastige Aufgabe | iOS/iPadOS Full-screen-Modal, macOS neues Fenster/Vollbild | (hig:sheets#Best-practices), (hig:modality#Best-practices) |
| Nie | mehrere modale Views oder zwei Alerts gleichzeitig | (hig:modality#Best-practices) |

### Navigation und Struktur
| Situation | Komponente | Beleg |
|---|---|---|
| iPhone: wenige Hauptbereiche | Tab bar | (hig:tab-bars) |
| iPad: viele oder anpassbare Bereiche | Tab bar mit Sidebar-Adaption (`sidebarAdaptable`) | (hig:tab-bars#iPadOS), (hig:sidebars#iOS-iPadOS) |
| macOS: Top-Level-Navigation | Sidebar im Split view | (hig:sidebars#macOS) |
| Hierarchie mit Detailansicht | Split view (`NavigationSplitView`) | (hig:split-views) |
| Häufige Aktionen der aktuellen View | Toolbar, kein Wechsel zwischen App-Bereichen | (hig:toolbars) |
| Textlastige, zeilenbasierte Daten | List/Table | (hig:lists-and-tables#Best-practices) |
| Bildlastige oder unterschiedlich große Elemente | Collection | (hig:collections#Best-practices) |
| macOS: hierarchische Textdaten / tiefe Hierarchie mit Spaltensprüngen | Outline view / Column view | (hig:outline-views#Best-practices), (hig:column-views#Best-practices) |
| macOS: sich ausschließende Panes im Fenster | Tab view (iOS/iPadOS: Segmented control) | (hig:tab-views#iOS-iPadOS) |

### Aktionen, Kontext und Befehle
| Situation | Komponente | Beleg |
|---|---|---|
| Einzelne, sofortige Aktion | Button | (hig:buttons) |
| Häufige objektbezogene Befehle, versteckt | Context menu, nie als einziger Zugang | (hig:context-menus#Best-practices) |
| Vollständiges Befehlsverzeichnis Mac/iPad | Menu bar | (hig:the-menu-bar) |
| Teilen bzw. Übergabe an andere Apps | Activity view (Share Sheet) | (hig:activity-views) |
| Einstieg direkt vom Home Screen | Home Screen quick actions (max. 4) | (hig:home-screen-quick-actions) |

### Außerhalb der App (System experiences)
| Situation | Komponente | Beleg |
|---|---|---|
| Glanceable Info, periodisch aktualisiert | Widget (keine Echtzeitdaten) | (hig:widgets#iOS-iPadOS) |
| Zeitlich begrenzter Vorgang mit Live-Updates, klarer Anfang und klares Ende | Live Activity | (hig:live-activities#Best-practices) |
| Zeitnahe Info, wenn die App nicht vorne ist | Notification, nicht doppelt zur Live Activity | (hig:notifications), (hig:live-activities#Starting-updating-and-ending-a-Live-Activity) |
| Eine Aktion ohne App-Start (Control Center, Lock Screen, Action button) | Control | (hig:controls#Best-practices) |
| Funktion über Siri/Spotlight | App Shortcut, Ergebnis als Snippet | (hig:app-shortcuts), (hig:snippets) |
| Daten auf dem Zifferblatt | Complication | (hig:complications) |

## Index aller Komponenten

Die Plattformangaben stammen aus der Kopfzeile der jeweiligen Spiegelseite. Abkürzungen: i = iOS, iP = iPadOS, m = macOS, w = watchOS, tv = tvOS, v = visionOS.

| Komponente | slug | Plattformen | Datei |
|---|---|---|---|
| Charts | charts | i iP m w tv v | [content.md](content.md) |
| Image views | image-views | i iP m w tv v | [content.md](content.md) |
| Text views | text-views | i iP m w tv v | [content.md](content.md) |
| Web views | web-views | i iP m v | [content.md](content.md) |
| Boxes | boxes | i iP m v | [layout-and-organization.md](layout-and-organization.md) |
| Collections | collections | i iP m tv v | [layout-and-organization.md](layout-and-organization.md) |
| Column views | column-views | m | [layout-and-organization.md](layout-and-organization.md) |
| Disclosure controls | disclosure-controls | i iP m v | [layout-and-organization.md](layout-and-organization.md) |
| Labels | labels | i iP m w tv v | [layout-and-organization.md](layout-and-organization.md) |
| Lists and tables | lists-and-tables | i iP m w tv v | [layout-and-organization.md](layout-and-organization.md) |
| Lockups | lockups | tv | [layout-and-organization.md](layout-and-organization.md) |
| Outline views | outline-views | m | [layout-and-organization.md](layout-and-organization.md) |
| Split views | split-views | i iP m w tv v | [layout-and-organization.md](layout-and-organization.md) |
| Tab views | tab-views | m w | [layout-and-organization.md](layout-and-organization.md) |
| Activity views | activity-views | i iP v | [menus-and-actions.md](menus-and-actions.md) |
| Buttons | buttons | i iP m w tv v | [menus-and-actions.md](menus-and-actions.md) |
| Context menus | context-menus | i iP m tv v | [menus-and-actions.md](menus-and-actions.md) |
| Dock menus | dock-menus | m | [menus-and-actions.md](menus-and-actions.md) |
| Edit menus | edit-menus | i iP m v | [menus-and-actions.md](menus-and-actions.md) |
| Home Screen quick actions | home-screen-quick-actions | i iP | [menus-and-actions.md](menus-and-actions.md) |
| Menus | menus | i iP m w tv v | [menus-and-actions.md](menus-and-actions.md) |
| Ornaments | ornaments | v | [menus-and-actions.md](menus-and-actions.md) |
| Pop-up buttons | pop-up-buttons | i iP m v | [menus-and-actions.md](menus-and-actions.md) |
| Pull-down buttons | pull-down-buttons | i iP m v | [menus-and-actions.md](menus-and-actions.md) |
| The menu bar | the-menu-bar | iP m | [menus-and-actions.md](menus-and-actions.md) |
| Toolbars | toolbars | i iP m w tv v | [menus-and-actions.md](menus-and-actions.md) |
| Path controls | path-controls | m | [navigation-and-search.md](navigation-and-search.md) |
| Search fields | search-fields | i iP m w tv v | [navigation-and-search.md](navigation-and-search.md) |
| Sidebars | sidebars | i iP m tv v | [navigation-and-search.md](navigation-and-search.md) |
| Tab bars | tab-bars | i iP m tv v | [navigation-and-search.md](navigation-and-search.md) |
| Token fields | token-fields | m | [navigation-and-search.md](navigation-and-search.md) |
| Action sheets | action-sheets | i iP m w tv | [presentation.md](presentation.md) |
| Alerts | alerts | i iP m w tv v | [presentation.md](presentation.md) |
| Page controls | page-controls | i iP w tv v | [presentation.md](presentation.md) |
| Panels | panels | m | [presentation.md](presentation.md) |
| Popovers | popovers | i iP m v | [presentation.md](presentation.md) |
| Scroll views | scroll-views | i iP m w tv v | [presentation.md](presentation.md) |
| Sheets | sheets | i iP m w tv v | [presentation.md](presentation.md) |
| Windows | windows | iP m v | [presentation.md](presentation.md) |
| Color wells | color-wells | i iP m v | [selection-and-input.md](selection-and-input.md) |
| Combo boxes | combo-boxes | m | [selection-and-input.md](selection-and-input.md) |
| Digit entry views | digit-entry-views | tv | [selection-and-input.md](selection-and-input.md) |
| Image wells | image-wells | m | [selection-and-input.md](selection-and-input.md) |
| Pickers | pickers | i iP m w tv v | [selection-and-input.md](selection-and-input.md) |
| Segmented controls | segmented-controls | i iP m tv v | [selection-and-input.md](selection-and-input.md) |
| Sliders | sliders | i iP m w v | [selection-and-input.md](selection-and-input.md) |
| Steppers | steppers | i iP m v | [selection-and-input.md](selection-and-input.md) |
| Text fields | text-fields | i iP m w tv v | [selection-and-input.md](selection-and-input.md) |
| Toggles | toggles | i iP m w tv v | [selection-and-input.md](selection-and-input.md) |
| Virtual keyboards | virtual-keyboards | i iP w tv v | [selection-and-input.md](selection-and-input.md) |
| Activity rings | activity-rings | i iP w | [status.md](status.md) |
| Gauges | gauges | i iP m w v | [status.md](status.md) |
| Progress indicators | progress-indicators | i iP m w tv v | [status.md](status.md) |
| Rating indicators | rating-indicators | m | [status.md](status.md) |
| App Shortcuts | app-shortcuts | i iP w v | [system-experiences.md](system-experiences.md) |
| Complications | complications | w | [system-experiences.md](system-experiences.md) |
| Controls | controls | i iP m | [system-experiences.md](system-experiences.md) |
| Live Activities | live-activities | i iP m w | [system-experiences.md](system-experiences.md) |
| Notifications | notifications | i iP m w tv v | [system-experiences.md](system-experiences.md) |
| Snippets | snippets | i iP m | [system-experiences.md](system-experiences.md) |
| Status bars | status-bars | i iP | [system-experiences.md](system-experiences.md) |
| Top Shelf | top-shelf | tv | [system-experiences.md](system-experiences.md) |
| Watch faces | watch-faces | w | [system-experiences.md](system-experiences.md) |
| Widgets | widgets | i iP m w v | [system-experiences.md](system-experiences.md) |

## Bekannte Unklarheiten im Spiegel
- **Tab bars:** Die Kopfzeile nennt macOS, die Seite enthält aber keine macOS-Hinweise (hig:tab-bars#Platform-considerations).
- **Tab views:** Die Höchstzahl der Tabs ist widersprüchlich angegeben, „nicht mehr als sechs“ steht neben „ab sechs“ (hig:tab-views#Best-practices).
- **Pull-down buttons:** Der Spiegel verlinkt `MenuPickerStyle` als SwiftUI-Typ. Gemeint ist vermutlich `Menu`, denn `MenuPickerStyle` entspricht dem Pop-up button.
- **Complications:** Die Seite hat den Stand 2023 und enthält keine Maße für neuere Gehäusegrößen. Ein Inline-Maß ist doppelt und widersprüchlich angegeben (siehe system-experiences.md).
- In den Dateien ist jeweils markiert, wo API-Namen nicht im Spiegel stehen und aus Entwicklerwissen ergänzt wurden. Diese Namen vor Verwendung prüfen.
