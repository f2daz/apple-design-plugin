# apple-design – Claude-Code-Plugin für Apple-Plattform-Design

Ein Design-Begleiter für native Apps auf **iOS, iPadOS, macOS und watchOS** in [Claude Code](https://claude.com/claude-code). Grundlage sind Apples [Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines) (HIG) und die [Apple Design Resources](https://developer.apple.com/design/resources/).

Das Plugin fragt nach, plant, baut und prüft. Jede Designregel ist mit einem Verweis auf die HIG-Seite belegt. Aufbau und Workflow sind inspiriert von [impeccable](https://github.com/pbakaus/impeccable) und [ui-ux-pro-max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill).

---

## Inhalt

- [Was das Plugin kann](#was-das-plugin-kann)
- [Voraussetzungen](#voraussetzungen)
- [Installation](#installation)
- [Ersteinrichtung](#ersteinrichtung)
- [Anleitung: der typische Ablauf](#anleitung-der-typische-ablauf)
- [Alle Befehle](#alle-befehle)
- [Werkzeuge direkt im Terminal](#werkzeuge-direkt-im-terminal)
- [Aufbau des Repos](#aufbau-des-repos)
- [Aktualisieren & Pflege](#aktualisieren--pflege)
- [Fehlerbehebung](#fehlerbehebung)
- [Rechtliches](#rechtliches)

---

## Was das Plugin kann

| Baustein | Inhalt |
|---|---|
| **Skill `apple-design`** | Geführte Workflows: `init · shape · build · audit · critique · polish · adapt · icon · hig · symbols · resources · whatsnew · sync` |
| **Verdichtete HIG** | Rund 7.000 Zeilen auf Deutsch: Plattformen (iOS, iPadOS, macOS, watchOS), Grundlagen (Typografie, Farbe/Dark Mode, Layout, Liquid Glass, Icons/SF Symbols, Barrierefreiheit, Motion/Haptik, Texte/Datenschutz), Katalog aller Komponenten mit Entscheidungshilfe, Patterns, Eingabe, Technologien. Jede Regel ist mit `hig:<seite>` belegt, Widersprüche in der HIG sind benannt. |
| **HIG-Spiegel** | Alle HIG-Seiten (aktuell 173) lokal als Markdown, mit Volltextsuche, Abschnittsauszug, „Platform considerations“ je OS und Änderungsliste |
| **SF-Symbols-Suche** | Namen, Suchbegriffe, Kategorien, Mindest-OS, Fill-Varianten und Nutzungsbeschränkungen, direkt aus den macOS-Systemdaten |
| **Gerätemaße** | Display in pt/px, Scale und Eckenradius aller aktuellen iPhones, iPads und Watches, aus Xcode. Die HIG hat die Gerätetabellen im September 2026 entfernt. |
| **Design Resources** | Katalog aller Ressourcen (UI-Kits für Figma/Sketch, Templates, Fonts, SF Symbols, Icon Composer, Bezels, Glyphen) mit Download und Font-Installation ohne sudo |
| **Agent `hig-reviewer`** | Prüft bei großen Audits jede Plattform parallel |

## Voraussetzungen

- [Claude Code](https://docs.claude.com/en/docs/claude-code) (CLI, Desktop-App oder IDE-Erweiterung)
- **macOS** mit Python 3, das macOS bereits mitbringt. Die Skripte brauchen keine zusätzlichen Pakete.
- **Xcode** für Gerätemaße, Simulator-Screenshots und den Bau der Apps. Ohne Xcode funktioniert alles andere trotzdem.
- Optional: Figma oder Sketch für die UI-Kits

## Installation

### Variante A – aus GitHub (empfohlen)

In Claude Code:

```
/plugin marketplace add f2daz/apple-design-plugin
/plugin install apple-design@apple-design-plugin
```

Oder im Terminal:

```bash
claude plugin marketplace add f2daz/apple-design-plugin
claude plugin install apple-design@apple-design-plugin
```

Danach Claude Code neu starten oder `/reload-plugins` ausführen. `/plugin` zeigt, ob `apple-design` aktiv ist.

### Variante B – lokaler Klon (zum Mitentwickeln)

```bash
git clone https://github.com/f2daz/apple-design-plugin.git
claude plugin marketplace add ./apple-design-plugin
claude plugin install apple-design@apple-design-plugin
```

Änderungen am Klon übernimmst du mit `claude plugin marketplace update apple-design-plugin`.

## Ersteinrichtung

Das Plugin legt seine Daten unter `~/.apple-design/` ab, nicht im Repo. Den HIG-Spiegel lädt es beim ersten `hig`-Aufruf automatisch. Du kannst ihn und den Rest aber auch vorab einrichten. Am bequemsten geht das in Claude Code:

```
/apple-design sync
/apple-design resources
```

Oder im Terminal. Der Pfad unten gilt für die Installation aus GitHub, `claude plugin list` zeigt bei Bedarf den genauen Ort:

```bash
S=$(dirname "$(find ~/.claude/plugins -path '*apple-design/skills/apple-design/SKILL.md' | head -1)")/scripts

# 1. HIG-Spiegel laden (~10 s, ~170 Seiten → ~/.apple-design/hig)
python3 -I "$S/hig_sync.py"

# 2. Ressourcenkatalog aktualisieren
python3 -I "$S/resources.py" sync

# 3. Wichtigste Ressourcen laden: Fonts, SF-Symbols-App, Icon-Templates (~850 MB)
python3 -I "$S/resources.py" download essentials --accept-license

# 4. Fonts installieren: SF Pro, SF Compact, SF Mono, New York → ~/Library/Fonts (ohne sudo)
python3 -I "$S/resources.py" install-fonts --accept-license

# 5. SF Symbols App installieren: DMG öffnen und dem Installer folgen
open ~/.apple-design/downloads/SF-Symbols-*.dmg
```

> `--accept-license` bestätigt, dass du die Apple-Lizenz im jeweiligen DMG akzeptierst. Die Fonts dürfen nur zum Gestalten und Entwickeln von Software für Apple-Plattformen genutzt werden.

## Anleitung: der typische Ablauf

Beispiel: Eine neue SwiftUI-App für iPhone, iPad und Mac bekommt eine Einstellungsseite.

### 1. Projekt kennenlernen – `init`

Starte Claude Code im Projektordner (dort, wo die `.xcodeproj` oder `Package.swift` liegt):

```
/apple-design init
```

Das Plugin liest zuerst selbst aus dem Projekt: Deployment Targets, Gerätefamilien, Frameworks, Asset-Katalog. Dann fragt es per Auswahl nur, was fehlt:

- Plattformen (iOS · iPadOS · macOS · watchOS)
- Stack (SwiftUI · UIKit · AppKit · gemischt)
- Ziel-OS. Das entscheidet, ob Liquid Glass voll nutzbar ist oder Fallbacks nötig sind.
- App-Art, Marke (Akzentfarbe, eigene Schrift), Barrierefreiheitsziel, Systemintegration (Widgets, Live Activities, Complications …)

Ergebnis ist eine `APPLE_DESIGN.md` im Projekt mit Navigationsgerüst je Plattform, Markenregeln und passenden UI-Kits. Alle weiteren Befehle richten sich danach. Committe sie mit.

### 2. Planen – `shape`

```
/apple-design shape Einstellungen
```

Du bekommst eine Spezifikation, bevor Code entsteht:

- wo das Feature in der Navigation sitzt
- welches Muster je Plattform passt, z. B. iPhone: Push in Liste; iPad: Split View; Mac: `Settings`-Fenster
- welche Systemkomponenten es nutzt, jeweils mit Beleg
- Zustände (leer, lädt, Fehler, große Schrift, Dark Mode), Texte und SF Symbols samt Mindest-OS

Bei echten Alternativen legt das Plugin dir Optionen mit ASCII-Vorschau zur Auswahl vor.

### 3. Bauen – `build`

```
/apple-design build Einstellungen
```

Die Umsetzung nutzt Systemkomponenten, Textstile mit Dynamic Type, semantische Farben und Liquid Glass nur auf der Funktionsebene. Jede View bekommt Previews (hell/dunkel, große Schrift). Mit Xcode baut das Plugin die App, macht Simulator-Screenshots und schaut sich das Ergebnis an.

### 4. Prüfen – `audit` und `critique`

```
/apple-design audit              # Regelkonformität: Befunde P0–P3 mit Fundstelle, Beleg und Fix
/apple-design critique           # Gestaltung: Bewertungsraster, Top-3-Hebel, Alternativen
```

Bei mehreren Plattformen startet `audit` je Plattform einen `hig-reviewer` parallel. Danach fragt das Plugin, ob es P0/P1-Befunde direkt beheben soll.

### 5. Feinschliff – `polish`

```
/apple-design polish
```

Letzter Durchgang mit Checkliste: Typografie, Dark Mode/Kontrast, Symbole, Pressed-States, Haptik, Reduce Motion, Leer- und Fehlerzustände, Tastaturkürzel auf iPad und Mac.

### 6. Auf weitere Geräte bringen – `adapt`

```
/apple-design adapt watchos
```

Überträgt das Design idiomatisch statt skaliert, z. B. iPhone-Tab-Bar → Mac-Sidebar mit Menüleiste → Watch mit vertikalen Seiten und Complication.

### Zwischendurch nachschlagen

```
/apple-design hig Wie viele Tabs darf eine Tab Bar haben?
/apple-design symbols Zahlung Karte
/apple-design resources bezels iphone
/apple-design whatsnew
```

Du kannst auch einfach normal fragen, z. B. „Ist das Sheet hier HIG-konform?“. Der Skill springt bei Apple-Design-Themen automatisch an.

## Alle Befehle

| Befehl | Was passiert |
|---|---|
| `/apple-design` | Menü mit Vorschlag passend zum Projektstand |
| `init` | Interview → `APPLE_DESIGN.md` |
| `shape <feature>` | Spezifikation: Struktur, Muster je Plattform, Komponenten, Zustände, Texte |
| `build <feature>` | Umsetzung in SwiftUI/UIKit/AppKit inkl. Previews und Simulator-Check |
| `audit [ziel]` | HIG-Prüfung mit Schweregraden und Belegen, optional Fixes |
| `critique [ziel]` | UX-Review am gerenderten Screen |
| `polish [ziel]` | Feinschliff vor dem Release |
| `adapt <plattform>` | Übertragung auf iPad, Mac oder Watch |
| `icon` | App-Icon mit Icon Composer (Liquid Glass, Varianten Default/Dark/Clear/Tinted) |
| `hig <frage>` | Antwort aus der HIG mit Beleg |
| `symbols <begriff>` | Passende SF Symbols mit Verfügbarkeit |
| `resources [suche]` | UI-Kits, Templates, Fonts, Bezels zeigen, laden, installieren |
| `whatsnew` | Zuletzt geänderte HIG-Seiten und ihre Bedeutung fürs Projekt |
| `sync` | HIG-Spiegel und Ressourcenkatalog aktualisieren |

## Werkzeuge direkt im Terminal

Alle Skripte liegen in `skills/apple-design/scripts/` und kommen ohne zusätzliche Pakete aus. Aufruf jeweils mit `python3 -I <skript> …`:

```bash
# HIG
hig_search.py search "tab bar badge" --platform ios     # Volltext mit bestem Absatz
hig_search.py page buttons --section "Platform considerations"
hig_search.py platform watchos                          # alle watchOS-Besonderheiten
hig_search.py list --section Components
hig_search.py updates --since 2026-06-01
hig_sync.py --if-stale 14                               # nur laden, wenn älter als 14 Tage

# SF Symbols
sf_symbols.py search trash --min-ios 17
sf_symbols.py info heart                                # Kategorien, Fill-Variante, Beschränkungen
sf_symbols.py categories
sf_symbols.py new 2026                                  # neue Symbole eines Jahrgangs

# Geräte (braucht Xcode)
device_specs.py --family iphone

# Ressourcen
resources.py list --platform macos
resources.py show "sign in with apple"
resources.py download bezels-iphone --accept-license    # Presets: fonts, essentials, bezels-iphone,
                                                        # bezels-ipad, bezels-mac, bezels-watch, glyphs, all
resources.py status
```

## Aufbau des Repos

```
.claude-plugin/
  plugin.json            Plugin-Manifest
  marketplace.json       Marketplace-Eintrag (Installation per /plugin marketplace add)
agents/
  hig-reviewer.md        Audit-Agent je Plattform
skills/apple-design/
  SKILL.md               Router, Grundsätze, Qualitätsboden
  reference/
    workflows/           Playbooks: init, shape, build, audit, critique, polish, adapt, icon, lookup, resources
    platforms/           ios, ipados, macos, watchos
    foundations/         typography, color-and-dark-mode, layout-and-spacing, materials-and-liquid-glass,
                         icons-and-symbols, accessibility, motion-and-feedback, writing-and-privacy
    components/          Entscheidungshilfe + 8 Gruppen (64 Komponenten)
    patterns.md · inputs.md · technologies.md · getting-started.md
  scripts/               hig_sync, hig_search, sf_symbols, device_specs, resources
  data/resources.json    Mitgelieferter Ressourcenkatalog (Fallback)
  templates/APPLE_DESIGN.md
```

Lokale Daten liegen außerhalb des Repos:

| Pfad | Inhalt |
|---|---|
| `~/.apple-design/hig/` | HIG-Spiegel (`pages/*.md`, `index.json`) |
| `~/.apple-design/resources.json` | aktueller Ressourcenkatalog |
| `~/.apple-design/downloads/` | heruntergeladene DMGs |

Mit der Umgebungsvariable `APPLE_DESIGN_HOME` lässt sich der Basisordner verlegen.

## Aktualisieren & Pflege

- **Plugin:** `claude plugin marketplace update apple-design-plugin`, danach `/reload-plugins`
- **HIG:** Apple ändert die Guidelines laufend. `/apple-design whatsnew` oder `hig_sync.py --if-stale 14` holt den neuesten Stand.
- **Verdichtungen nachziehen:** `hig_search.py updates --since <letzter Stand>` zeigt geänderte Seiten. Die passenden Dateien unter `reference/` anpassen, die Originalseite gewinnt.

## Fehlerbehebung

| Problem | Lösung |
|---|---|
| `CERTIFICATE_VERIFY_FAILED` (Firmenproxy) | Die Skripte nutzen dann automatisch `curl` mit den System-Zertifikaten. Ist kein `curl` vorhanden: Zertifikat in Python hinterlegen oder ein anderes Netz nutzen. |
| `device_specs.py`: „Xcode nicht gefunden“ | Xcode installieren. Die Command Line Tools allein reichen nicht. Das Skript findet `/Applications/Xcode*.app` auch ohne `xcode-select`. |
| `sf_symbols.py` findet keine Metadaten | Läuft nur auf macOS. Alternativ die SF-Symbols-App installieren. |
| Skill erscheint nicht | `/plugin` prüfen, `/reload-plugins` ausführen, Claude Code neu starten |
| HIG-Spiegel veraltet oder kaputt | `rm -rf ~/.apple-design/hig && python3 -I hig_sync.py` |

## Rechtliches

- **Plugin-Code und eigene Texte:** MIT, siehe [LICENSE](LICENSE).
- **Apple-Inhalte:** Die HIG-Texte und -Bilder, SF-Fonts, SF Symbols und alle Apple Design Resources sind © Apple Inc. Dieses Repository enthält **keine** Apple-Originalinhalte, nur eigene, verdichtete Zusammenfassungen mit Quellenverweisen sowie einen Linkkatalog mit den kurzen Beschreibungen der Ressourcenseite. HIG-Spiegel und Downloads entstehen lokal auf deinem Rechner, direkt von Apple, und sind nicht zur Weitergabe bestimmt.
- **Fonts:** Die SF-Fonts dürfen laut Apple-Lizenz nur zum Gestalten und Entwickeln von Software für Apple-Plattformen genutzt werden. Im App-Code sind sie nicht einzubetten, das System liefert sie mit.
- Apple, iPhone, iPad, Mac, Apple Watch, SF Symbols und Liquid Glass sind Marken von Apple Inc. Dieses Projekt steht in keiner Verbindung zu Apple.
