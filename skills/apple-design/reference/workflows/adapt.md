# adapt – auf weitere Apple-Plattformen übertragen

Grundsatz: **Gleiche App, idiomatische Gestalt.** Inhalte, Daten und Begriffe bleiben; Struktur, Eingabe und Dichte folgen der Zielplattform. Skalieren ist kein Adaptieren.

## Ablauf

1. Quell- und Zielplattform klären; Ziel-Referenz laden (`reference/platforms/<ziel>.md`) und `hig_search.py platform <ziel>` für die verwendeten Komponenten.
2. AskUserQuestion, falls offen: „Welche Rolle hat die Zielplattform?“ – Vollwertig (alle Funktionen) · Begleiter (Kernaufgaben) · Glance (Status/Schnellaktion).
3. Mapping-Tabelle erstellen (unten), Abweichungen begründen, dann umsetzen (build.md).

## Mapping-Hilfe

| Aspekt | iPhone | iPad | Mac | Watch |
|---|---|---|---|---|
| Top-Level-Navigation | Tab bar | Tab bar ↔ Sidebar (adaptiv) | Sidebar in Split View + Menüleiste | NavigationStack, vertikale Seiten |
| Hierarchie | Push im Stack | Split View (2–3 Spalten) | Split View, ggf. mehrere Fenster | flacher Stack, wenige Ebenen |
| Nebenaufgabe | Sheet | Sheet / Popover / Inspector | Sheet am Fenster, Panel, Inspector | Modal-Sheet, kurz |
| Aktionen | Toolbar, Swipe, Kontextmenü | + Tastenkürzel, Pointer-Hover | Menüleiste + Toolbar + Kontextmenü + Shortcuts | Toolbar-Ecken, Liste, Crown |
| Eingabe | Touch | Touch, Pencil, Tastatur, Trackpad | Maus/Trackpad, Tastatur | Touch, Digital Crown, Diktat |
| Dichte | kompakt | mittel, nutzt Breite | hoch, kleinere Controls | minimal, eine Aufgabe |
| Systemorte | Widgets, Live Activities, Controls | Widgets, Stage Manager | Menüleisten-Extra, Widgets, Dock | Complications, Smart Stack, Live Activities |

Details und Zahlen stehen in den Plattform-Referenzen; vor allem für watchOS die Inhalte radikal kürzen.

## Typische Fallen

- iPad: iPhone-Layout mittig gestreckt; Popover ohne Anker; fehlende Tastaturunterstützung; keine Größenänderung/Multitasking.
- Mac (Catalyst oder SwiftUI): keine Menüleiste, Touch-große Controls, Sheets statt Fenster, fehlendes Undo, keine Einstellungen im App-Menü.
- Watch: iPhone-Screens verkleinert, Text-Eingabe als Hauptweg, zu viele Ebenen, keine Complication.
