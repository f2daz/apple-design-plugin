# Getting started – Design principles und Plattform-Grundlagen

Verdichtete Referenz zur HIG-Section „Getting started“: Design principles, „Designing for …“-Seiten je Plattform, Games, iPhone Duo. Quelle: lokaler HIG-Spiegel (`~/.apple-design/hig/pages/`, Sync 2026-10-21). Belege als `(hig:<slug>)` bzw. `(hig:<slug>#Anker)`. Alles paraphrasiert.

## Inhalt

1. [Design principles](#design-principles)
2. [Plattformvergleich iOS / iPadOS / macOS / watchOS](#plattformvergleich-ios--ipados--macos--watchos)
3. [Designing for iOS](#designing-for-ios)
4. [Designing for iPadOS](#designing-for-ipados)
5. [Designing for macOS](#designing-for-macos)
6. [Designing for watchOS](#designing-for-watchos)
7. [iPhone Duo](#iphone-duo)
8. [Designing for games](#designing-for-games)
9. [tvOS und visionOS (kurz)](#tvos-und-visionos-kurz)
10. [Auffälligkeiten und Unklarheiten](#auffälligkeiten-und-unklarheiten)

---

## Design principles

Stand im Spiegel: Seite am **2026-06-08** „wieder eingeführt“ (hig:design-principles). Die HIG nennt **acht** Prinzipien. Sie sind keine Rezepte, sondern Werkzeuge zum Abwägen konkurrierender Prioritäten (hig:design-principles).

> Hinweis: Begriffe wie „Hierarchy, Harmony, Consistency“ kommen im Spiegel **nicht** als Prinzipien-Überschriften vor. „Hierarchie herstellen“ und „Konsistenz“ erscheinen nur als Einzelregeln unter Simplicity bzw. Familiarity. Wer auf diese Trias verweist, bezieht sich auf eine andere (ältere/andere) Quelle.

| Prinzip | Leitsatz (paraphrasiert) | Kern |
|---|---|---|
| Purpose | Etwas Bedeutsames schaffen | Was ist den Menschen wichtig – das großartig machen |
| Agency | Menschen auf ihre Art handeln lassen | Freiheit, informiert halten, Fehler leicht korrigierbar |
| Responsibility | Im Interesse der Menschen handeln | Sicherheit, Privatsphäre, Transparenz |
| Familiarity | Auf Bekanntem aufbauen | Etablierte physische/digitale Muster, konsistent angewendet |
| Flexibility | Sich an Kontexte und Bedürfnisse anpassen | Viele Geräte, Eingaben, Perspektiven unterstützen |
| Simplicity | Klar und direkt sein | Unnötiges entfernen, logisch strukturiert |
| Craft | Sich um jedes Detail kümmern | Qualität als Haltung |
| Delight | Menschlich gestalten | Passende Emotion, angenehm im Gebrauch |

### Regeln je Prinzip

**Purpose** (hig:design-principles#Purpose)
- Schaffe Wert: Prüfe in jeder Phase, wofür das Produkt da ist und ob das Design dem dient.
- Bleib fokussiert: Wichtigste Features priorisieren und exzellent machen.
- Löse Probleme neu: Bestehende Lösungen nicht nachbauen; Alleinstellung herausarbeiten.

**Agency** (hig:design-principles#Agency)
- Steh nicht im Weg: Direkt zur Aufgabe/zum Inhalt führen; unaufdringlich, aber präsent wenn nötig.
- Freiheit zum Erkunden: Keine erzwungenen Flows/Modi; geführte Flows überspringbar machen.
- Fehler korrigierbar machen: Rückgängig/Zurück muss leicht sein und darf keine Arbeit kosten.

**Responsibility** (hig:design-principles#Responsibility)
- Transparent sein: Absicht der App von Anfang an klar; Berechtigungsanfragen begründen; Datenerhebung offenlegen.
- Daten schützen: Nur Nötiges erheben; Missbrauch antizipieren und verhindern.

**Familiarity** (hig:design-principles#Familiarity)
- Bekannte Konzepte nutzen (reale Welt, andere Software).
- Visuelles und Interaktion konsistent halten – einmal festgelegtes Verhalten überall gleich.
- Klares Feedback: Verfügbarkeit von Controls, Inhaltsänderungen zeigen; System-Patterns für Alerts und Auswahl nutzen.

**Flexibility** (hig:design-principles#Flexibility)
- Für alle gestalten; Accessibility von Anfang an priorisieren; inklusiv.
- Kontext bewahren: Inhalte/Controls an konsistenten, vorhersehbaren Positionen über Plattformen und Konfigurationen; natürliche Übergangsanimationen.
- Viele Eingabemethoden berücksichtigen (Voice, Touch, Keyboard …).
- Jede Plattform mit gleicher Sorgfalt behandeln.

**Simplicity** (hig:design-principles#Simplicity)
- Nur Notwendiges – Einfachheit ist nicht Minimalismus.
- Knapp formulieren; exakt die nötigen Worte für Konzepte und Labels.
- Hierarchie herstellen: erkennbare Controls, konsistente Struktur, die zeigt, wo man ist und was als Nächstes kommt.

**Craft** (hig:design-principles#Craft)
- Qualität setzt den Ton (Visuals, Animation, Wortwahl, Audio).
- Früh prototypen, iterieren, Verworfenes loslassen; im realen Umfeld testen.
- Pflege nach Release: aktuelle Plattformfähigkeiten und Patterns übernehmen.

**Delight** (hig:design-principles#Delight)
- Zielemotion bestimmen (Fitness: energetisch, Meditation: beruhigend, Spiel: spannend).
- Prägende Momente gestalten – vom Button-Druck bis zur Fehlermeldung.
- Delight ist keine Dekoration; die Aufgabe hat Vorrang.
- Delight entsteht aus der Summe: Handlungsfreiheit, Sicherheit beim Erkunden, vertraute Metaphern, flexible Kontextwechsel.

---

## Plattformvergleich iOS / iPadOS / macOS / watchOS

Grundlage: jeweilige „Designing for …“-Seite. Abstände so, wie die Seiten sie angeben (Fuß-Angaben im Original; 1 ft ≈ 0,3 m).

| Merkmal | iOS (iPhone) | iPadOS | macOS | watchOS |
|---|---|---|---|---|
| Display | mittelgroß, hochauflösend | groß, hochauflösend | typ. groß, hochauflösend; erweiterbar um weitere Displays inkl. iPad | klein, am Handgelenk, hochauflösend; Always On |
| Haltung/Ergonomie | ein- oder beidhändig, Hoch-/Querformat | gehalten, auf Fläche oder Ständer | stationär auf Tisch | getragen; Handgelenk heben, andere Hand bedient |
| Sehabstand | höchstens ein bis zwei Fuß | meist innerhalb etwa 3 Fuß | etwa 1 bis 3 Fuß | höchstens ca. ein Fuß |
| Primäre Eingabe | Multi-Touch, virtuelles Keyboard, Voice | Multi-Touch, virtuelles Keyboard; zusätzlich Hardware-Keyboard, Pointer, Apple Pencil, Voice – oft kombiniert | physisches Keyboard, Pointing device, Game controls, Siri | Digital Crown (vertikale Navigation, Daten inspizieren), Tap/Swipe/Drag, Action button, Shortcuts |
| Sensorik/Daten | Gyro/Accelerometer, persönliche Daten, Nearby interactions | – (nicht separat genannt) | – | GPS, Blutsauerstoff, Herzsensoren, Höhenmesser, Accelerometer, Gyro |
| Typische Session | 1–2 Minuten (Updates, Nachrichten) bis über eine Stunde (Web, Spiele, Medien) | wenige schnelle Aktionen bis stundenlange Vertiefung (Spiele, Medien, Kreation, Produktivität) | wenige Minuten bis mehrere Stunden konzentrierter Arbeit | Blicke, oft unter einer Minute; viele Male am Tag |
| Multitasking | mehrere Apps offen, häufiges Wechseln | mehrere Apps gleichzeitig sichtbar, Drag and drop zwischen Apps | viele Apps parallel, fließende Aktiv-/Inaktiv-Wechsel | Complications, Notifications, Siri oft wichtiger als die App selbst |
| Navigation (Best practices) | wenige Controls, Sekundäres auffindbar; Bedienung im mittleren/unteren Bereich; Swipe zurück, Swipe-Aktionen in Zeilen | großen Screen für Inhalt nutzen, wenig Modalität und Vollbild-Übergänge; Controls erreichbar, nicht im Weg | mehr Inhalt in weniger Ebenen, weniger Modalität; Menüleiste mit allen Befehlen; Fenster frei skalierbar | flache Hierarchie, Single-Screen-Interaktionen; Crown für vertikales Scrollen/Wechseln |
| Systemfeatures (laut Seite) | Widgets, Home Screen quick actions, Spotlight, Shortcuts, Activity views | Multitasking, Widgets, Drag and drop | Menu bar, File management, Going full screen, Dock menus | Complications, Notifications, Always On, Watch faces |

Belege: (hig:designing-for-ios), (hig:designing-for-ipados), (hig:designing-for-macos), (hig:designing-for-watchos).

Mindestgrößen (aus Spiele-Sicht, gelten laut Seite plattformweit als Empfehlung; hig:designing-for-games#Look-stunning-on-every-display):

| Plattform | Text Standard / Minimum | Button Standard / Minimum |
|---|---|---|
| iOS, iPadOS | 17 pt / 11 pt | 44x44 pt / 28x28 pt |
| macOS | 13 pt / 10 pt | 28x28 pt / 20x20 pt |
| watchOS | 16 pt / 12 pt | 44x44 pt / 28x28 pt |
| tvOS | 29 pt / 23 pt | 66x66 pt / 56x56 pt |
| visionOS | 17 pt / 12 pt | 60x60 pt / 28x28 pt |

---

## Designing for iOS

Kontext: iPhone als Begleiter unterwegs – verbunden bleiben, spielen, Medien, Aufgaben, persönliche Daten (hig:designing-for-ios).

- Konzentriere auf Primäraufgabe und Inhalt: wenige Controls auf dem Screen, Sekundäres mit minimaler Interaktion erreichbar.
- Passe dich nahtlos an Orientierung, Dark Mode und Dynamic Type an; Nutzer wählen die Konfiguration.
- Gestalte für die Haltung: Controls in Mitte/unten sind leichter erreichbar; Swipe zum Zurücknavigieren und für Zeilen-Aktionen ist besonders wichtig.
- Nutze mit Erlaubnis Plattformdaten statt Eingaben zu verlangen (Apple Pay, biometrische Authentifizierung, Standort).

(alle: hig:designing-for-ios#Best-practices)

## Designing for iPadOS

Kontext: Leistung, Mobilität, Flexibilität – Medien, Spiele, detaillierte Produktivität, Kreation (hig:designing-for-ipados).

- Nutze den großen Screen für Inhalte; minimiere modale Interfaces und Vollbild-Übergänge; Controls erreichbar, aber nicht im Weg.
- Bestimme Größe und Dichte nach Sehabstand und Eingabemodus.
- Unterstütze Multi-Touch, Hardware-Keyboard/Trackpad und Apple Pencil; erwäge Interaktionen, die Eingaben kombinieren.
- Passe dich an Orientierung, Multitasking-Modi, Dark Mode, Dynamic Type an und laufe sauber auch unter macOS.

(alle: hig:designing-for-ipados#Best-practices)

## Designing for macOS

Kontext: Leistung, Platz, Flexibilität für tiefe Produktivität, Medien, Spiele – oft mit mehreren Apps gleichzeitig (hig:designing-for-macos).

- Nutze große Displays für mehr Inhalt in weniger verschachtelten Ebenen und mit weniger Modalität, bei angenehmer Informationsdichte.
- Lass Fenster skalieren, aus-/einblenden, verschieben; unterstütze Vollbild für ablenkungsfreies Arbeiten.
- Mache alle Befehle über die Menüleiste erreichbar.
- Unterstütze hochpräzise Eingabe für pixelgenaue Auswahl und Bearbeitung.
- Unterstütze Keyboard-Shortcuts und reine Keyboard-Arbeitsweisen.
- Erlaube Personalisierung: Toolbars anpassen, Fenster-Ansichten konfigurieren, Farben/Schriften wählen.

(alle: hig:designing-for-macos#Best-practices)

## Designing for watchOS

Kontext: Ein Blick aufs Handgelenk – wesentliche Infos und einfache, zeitnahe Aufgaben, auch in Bewegung (hig:designing-for-watchos).

- Gestalte schnelle, glanceable Single-Screen-Interaktionen mit einer oder zwei Gesten.
- Halte die Navigationshierarchie flach; nutze die Digital Crown für vertikales Scrollen und Screen-Wechsel.
- Personalisiere proaktiv mit On-Device-Daten: relevant jetzt oder in Kürze.
- Nutze Complications für dynamische Daten direkt auf dem Watch Face (Tap führt in die App).
- Nutze Notifications für zeitkritische, wertvolle Infos und Aktionen ohne App-Start.
- Nutze Hintergrundfarbe für unterstützende Infos und Materials für Hierarchie und Ortsgefühl.
- Baue die App eigenständig funktionsfähig, ergänzend zu Notifications und Complications.

(alle: hig:designing-for-watchos#Best-practices)

---

## iPhone Duo

Seite neu seit **2026-09-09** (hig:designing-for-iphone-duo). iPhone mit zwei Displays (außen, innen), je eigener Frontkamera, Mittelscharnier; es gilt weiterhin alles aus „Designing for iOS“.

- **Anatomie:** Außen-Display (geschlossen) ist breiter und kürzer als bei anderen iPhones → System setzt Toolbars/Tab bars **seitlich**. Innen-Display im Querformat behält die Seitenposition; nur innen im Hochformat bleiben horizontale Bars (hig:designing-for-iphone-duo#Anatomy, #Vertical-controls).
- **Posen:** Buchartig gefaltet, liegend, auf Kante stehend. Kein eigenes Layout je Pose – Size classes: compact width außen, regular width innen. Test in Xcode über Device Hub (hig:designing-for-iphone-duo#Device-poses).
- Baue resizable: Size classes, Layout margins, Safe area insets; keine festen Breiten (hig:designing-for-iphone-duo#Best-practices).
- Gleiche Funktionen und Zustände auf beiden Displays und in allen Posen; innen ggf. eine Hierarchieebene mehr zeigen (Beispiel Mail: Liste + Mail nebeneinander) (hig:designing-for-iphone-duo#Best-practices).
- Spiele: in jeder Pose spielbar; Orientierung sperren erlaubt, aber Screen füllen; Seitenverhältnis anpassen statt Letter-/Pillarboxing (hig:designing-for-iphone-duo#Best-practices).
- **Reserved regions:** äußere Kamera (immer, erweitert sich zur Dynamic Island), innere Kamera (nur aktiv), Faltbereich (bei teilweise geöffnetem Gerät). APIs `ReservedRegion` (SwiftUI) / `UIView.ReservedRegion` (UIKit) (hig:designing-for-iphone-duo#Reserved-regions).
- Beim Falten: sich selbst anpassende Container bevorzugen; Grids mit gerader Spaltenzahl; keine drastischen Umbauten (hig:designing-for-iphone-duo#Reserved-regions).
- **Arrangement views** (`ArrangementView` / `UIArrangementViewController`): *split* (teilt je nach Seitenverhältnis horizontal/vertikal) und *overlay* (übereinander; bei Faltung je Seite). Navigation-Container außerhalb platzieren (hig:designing-for-iphone-duo#Arrangement-views).
- **Vertikale Controls:** Standard-Platzierung nicht überschreiben; oben Back/Close, dann prominente Aktion (Done); Overflow von unten nach oben, steuerbar via `ToolbarItemVisibilityPriority` / `UIBarButtonItemVisibilityPriority`; Title + Symbol für jedes Item; Text-Buttons minimieren; System-Overflow-Menü statt eigenem; Ellipsis nur für Overflow (hig:designing-for-iphone-duo#Vertical-controls).
- Platzmangel: navigationsorientiert → Toolbar-Items in Overflow (Standard); aufgabenorientiert → Tab bar minimieren (`ToolbarVerticalCompressionBehavior` / `UIVerticalBarCompressionBehavior`) (hig:designing-for-iphone-duo#Vertical-controls).
- Controls bleiben bei RTL auf derselben Seite (hardware-gebunden); bei Split View hat jede App die Controls an ihrer Außenkante (hig:designing-for-iphone-duo#Vertical-controls).

---

## Designing for games

Für Spiele über alle Plattformen (hig:designing-for-games):

- Sofort spielbar nach Installation; Download des Grundumfangs **höchstens 30 Minuten**, Rest im Hintergrund (hig:designing-for-games#Jump-into-gameplay).
- Gute Defaults aus Geräteinfos (Auflösung, gekoppelte Controller, Accessibility-Einstellungen) (hig:designing-for-games#Jump-into-gameplay).
- Durch Spielen lehren; schriftliches Tutorial nur als Nachschlagewerk (hig:designing-for-games#Jump-into-gameplay).
- Berechtigungen im passenden Spielmoment anfragen; Bewertung erst nach ausreichend Spielzeit (hig:designing-for-games#Jump-into-gameplay).
- Text- und Buttongrößen gemäß Tabelle oben; auflösungsunabhängige Assets; Safe areas; Menüs für 16:10, 19.5:9, 4:3 und beide Orientierungen (hig:designing-for-games#Look-stunning-on-every-display).
- Standard-Eingabe jeder Plattform unterstützen; Controller optional mit Alternativen; Touch controls auf iPhone/iPad (hig:designing-for-games#Enable-intuitive-interactions).
- Wahrnehmbarkeit, Personalisierung (Textgröße, Mapping, Bewegungsintensität, Klangbalance), Selbstdarstellung, keine Stereotype (hig:designing-for-games#Welcome-everyone).
- Game Center, GameSave (iCloud), Core Haptics (iOS, iPadOS, tvOS, visionOS), Spatial Audio (hig:designing-for-games#Adopt-Apple-technologies).

---

## tvOS und visionOS (kurz)

**tvOS** (hig:designing-for-tvos): sehr großes Display, Abstand oft 8 Fuß oder mehr; Siri Remote, Controller, Voice, Apps auf anderen Geräten; stundenlange Sessions, Picture-in-Picture. Fokus-System, randlose Artwork, Mehrbenutzer-Profile mit einfachem, seltenem Sign-in.

**visionOS** (hig:designing-for-visionos): unbegrenzter Raum (Windows, Volumes, 3D); Shared Space (Standard) vs. Full Space; Passthrough über Digital Crown; Eyes + indirekte Gesten; Komfort hat Priorität (Sichtfeld, ruhige Bewegung, Hände dürfen ruhen); minimal nötige Immersionsstufe je Moment; Nutzung ab 13 Jahren, nicht beim Fahren/Bewegen in gefährlicher Umgebung.

---

## Auffälligkeiten und Unklarheiten

- **Design principles:** Die Seite (Update 2026-06-08, „Reintroduced“) nennt acht Prinzipien – Purpose, Agency, Responsibility, Familiarity, Flexibility, Simplicity, Craft, Delight. Eine Trias „Hierarchy / Harmony / Consistency“ ist im Spiegel nicht als Prinzip vorhanden; ggf. stammt sie aus einer früheren HIG-Fassung oder Apple-Kommunikation. Nicht aus dem Spiegel belegbar.
- **iPhone Duo** ist eine neue Getting-started-Seite (2026-09-09); andere Seiten (z. B. hig:designing-for-ios) erwähnen das Gerät noch nicht.
- **Sehabstände** stehen nur in Fuß und teils vage („ein bis zwei Fuß“, „etwa 3 Fuß“) – nicht in exakte Meter umrechnen.
- **Standard-Eingabe in hig:designing-for-games:** visionOS und watchOS als „Touch“ geführt; das weicht von hig:designing-for-visionos (Eyes + Hands) und hig:digital-crown (Crown als primäre Navigation ab watchOS 10) ab.
- Die iOS-/iPadOS-/tvOS-Seiten verlinken teils mit vollständigen URLs statt `hig:`-Slugs; hig:designing-for-ios verweist auf den veralteten Slug `spatial-interactions` (heute nearby-interactions).
- Die Größentabellen für Text und Buttons stehen in der Games-Seite; ob sie für Nicht-Spiele identisch gelten, ist dort nicht ausdrücklich gesagt (iOS-44x44-pt-Minimum verweist aber auf hig:buttons).
- iOS, iPadOS, macOS-Seiten haben keinen Update-Vermerk; watchOS zuletzt 2023-06-05, Games 2025-06-09.
