# apple-design – a Claude Code plugin for Apple platform design

A design companion for native apps on **iOS, iPadOS, macOS and watchOS** in [Claude Code](https://claude.com/claude-code). It is built on Apple's [Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines) (HIG) and the [Apple Design Resources](https://developer.apple.com/design/resources/).

The plugin asks questions, plans, builds and reviews. Every design rule it applies is backed by a reference to the HIG page. Structure and workflow are inspired by [impeccable](https://github.com/pbakaus/impeccable) and [ui-ux-pro-max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill). It replies in whatever language you write in.

---

## Contents

- [What it does](#what-it-does)
- [Requirements](#requirements)
- [Installation](#installation)
- [First-time setup](#first-time-setup)
- [Walkthrough: the typical flow](#walkthrough-the-typical-flow)
- [All commands](#all-commands)
- [Using the tools from the terminal](#using-the-tools-from-the-terminal)
- [Repository layout](#repository-layout)
- [Updating & maintenance](#updating--maintenance)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [Legal](#legal)

---

## What it does

| Building block | Content |
|---|---|
| **Skill `apple-design`** | Guided workflows: `init · shape · build · audit · critique · polish · adapt · icon · hig · symbols · resources · whatsnew · sync` |
| **Condensed HIG** | About 7,000 lines covering the platforms (iOS, iPadOS, macOS, watchOS), foundations (typography, color/Dark Mode, layout, Liquid Glass, icons/SF Symbols, accessibility, motion/haptics, writing/privacy), a catalog of all components with a decision guide, patterns, inputs and technologies. Every rule is cited as `hig:<page>`; contradictions within the HIG are called out. |
| **HIG mirror** | All HIG pages (currently 173) as local Markdown, with full-text search, section extraction, per-platform "Platform considerations" and a change list |
| **SF Symbols search** | Names, keywords, categories, minimum OS, fill variants and usage restrictions, read directly from macOS system data |
| **Device specs** | Display size in pt/px, scale and corner radius of current iPhones, iPads and Watches, read from Xcode. The HIG dropped its device tables in September 2026. |
| **Design Resources** | Catalog of all resources (UI kits for Figma/Sketch, templates, fonts, SF Symbols, Icon Composer, bezels, glyphs) with downloader and a font installer that needs no sudo |
| **Agent `hig-reviewer`** | Reviews each platform in parallel during large audits |

## Requirements

- [Claude Code](https://docs.claude.com/en/docs/claude-code) (CLI, desktop app or IDE extension)
- **macOS** with Python 3 (preinstalled). The scripts need no extra packages.
- **Xcode** for device specs, Simulator screenshots and building apps. Everything else works without it.
- Optional: Figma or Sketch for the UI kits

## Installation

### Option A – from GitHub (recommended)

In Claude Code:

```
/plugin marketplace add f2daz/apple-design-plugin
/plugin install apple-design@apple-design-plugin
```

Or in the terminal:

```bash
claude plugin marketplace add f2daz/apple-design-plugin
claude plugin install apple-design@apple-design-plugin
```

Then restart Claude Code or run `/reload-plugins`. `/plugin` shows whether `apple-design` is enabled.

### Option B – local clone (for contributing)

```bash
git clone https://github.com/f2daz/apple-design-plugin.git
claude plugin marketplace add ./apple-design-plugin
claude plugin install apple-design@apple-design-plugin
```

Pick up changes in your clone with `claude plugin marketplace update apple-design-plugin`.

## First-time setup

The plugin keeps its data in `~/.apple-design/`, not in the repo. The HIG mirror is created automatically on the first `hig` call, but you can set everything up in advance. The easiest way is inside Claude Code:

```
/apple-design sync
/apple-design resources
```

Or in the terminal. First locate the plugin's script folder:

```bash
S=$(find ~/.claude/plugins -type d -path '*/skills/apple-design/scripts' | head -1)
echo "$S"   # must print a path, e.g. ~/.claude/plugins/cache/apple-design-plugin/apple-design/0.1.0/skills/apple-design/scripts

# 1. Build the HIG mirror (~10 s, ~170 pages → ~/.apple-design/hig)
python3 -I "$S/hig_sync.py"

# 2. Refresh the resource catalog
python3 -I "$S/resources.py" sync

# 3. Download the essentials: fonts, SF Symbols app, icon templates (~850 MB)
python3 -I "$S/resources.py" download essentials --accept-license

# 4. Install fonts: SF Pro, SF Compact, SF Mono, New York → ~/Library/Fonts (no sudo)
python3 -I "$S/resources.py" install-fonts --accept-license

# 5. Install the SF Symbols app: open the DMG and follow the installer
open ~/.apple-design/downloads/SF-Symbols-*.dmg
```

> `--accept-license` confirms that you accept Apple's license inside each DMG. The fonts may only be used to design and develop software for Apple platforms.

## Walkthrough: the typical flow

Example: a new SwiftUI app for iPhone, iPad and Mac gets a settings screen.

### 1. Get to know the project – `init`

Start Claude Code in the project folder (where the `.xcodeproj` or `Package.swift` lives):

```
/apple-design init
```

The plugin first reads what it can from the project: deployment targets, device families, frameworks, asset catalog. Then it asks multiple-choice questions only for what's missing:

- Platforms (iOS · iPadOS · macOS · watchOS)
- Stack (SwiftUI · UIKit · AppKit · mixed)
- Target OS. This decides whether Liquid Glass is fully available or needs fallbacks.
- App type, brand (accent color, custom typeface), accessibility goal, system integration (widgets, Live Activities, complications …)

The result is an `APPLE_DESIGN.md` in your project with a navigation skeleton per platform, brand rules and the matching UI kits. Every later command follows it. Commit it.

### 2. Plan – `shape`

```
/apple-design shape Settings
```

You get a spec before any code is written:

- where the feature sits in the navigation
- which pattern fits each platform, e.g. iPhone: push from a list; iPad: split view; Mac: a `Settings` window
- which system components it uses, each with a source
- states (empty, loading, error, large text, Dark Mode), copy and SF Symbols with their minimum OS

For real alternatives the plugin presents options with an ASCII preview for you to choose from.

### 3. Build – `build`

```
/apple-design build Settings
```

The implementation uses system components, text styles with Dynamic Type, semantic colors, and Liquid Glass only on the functional layer. Every view gets previews (light/dark, large text). With Xcode installed, the plugin builds the app, takes Simulator screenshots and looks at the result.

### 4. Review – `audit` and `critique`

```
/apple-design audit              # rule compliance: findings P0–P3 with location, source and fix
/apple-design critique           # design quality: rubric, top 3 levers, alternatives
```

With several platforms, `audit` launches one `hig-reviewer` per platform in parallel. Afterwards it asks whether to fix the P0/P1 findings right away.

### 5. Final pass – `polish`

```
/apple-design polish
```

A last checklist pass: typography, Dark Mode/contrast, symbols, pressed states, haptics, Reduce Motion, empty and error states, keyboard shortcuts on iPad and Mac.

### 6. Bring it to more devices – `adapt`

```
/apple-design adapt watchos
```

Transfers the design idiomatically instead of scaling it, e.g. iPhone tab bar → Mac sidebar with menu bar → Watch with vertical pages and a complication.

### Look things up anytime

```
/apple-design hig How many tabs can a tab bar have?
/apple-design symbols card payment
/apple-design resources bezels iphone
/apple-design whatsnew
```

You can also just ask normally, e.g. "Is this sheet HIG-compliant?". The skill kicks in automatically for Apple design topics.

## All commands

| Command | What happens |
|---|---|
| `/apple-design` | Context-aware menu with a recommendation |
| `init` | Interview → `APPLE_DESIGN.md` |
| `shape <feature>` | Spec: structure, pattern per platform, components, states, copy |
| `build <feature>` | Implementation in SwiftUI/UIKit/AppKit incl. previews and a Simulator check |
| `audit [target]` | HIG review with severities and sources, optional fixes |
| `critique [target]` | UX review of the rendered screen |
| `polish [target]` | Final pass before release |
| `adapt <platform>` | Bring the design to iPad, Mac or Watch |
| `icon` | App icon with Icon Composer (Liquid Glass, default/dark/clear/tinted variants) |
| `hig <question>` | Answer from the HIG with a citation |
| `symbols <term>` | Matching SF Symbols with availability |
| `resources [query]` | Show, download and install UI kits, templates, fonts, bezels |
| `whatsnew` | Recently changed HIG pages and what they mean for your project |
| `sync` | Refresh the HIG mirror and the resource catalog |

## Using the tools from the terminal

All scripts live in `skills/apple-design/scripts/` and need no extra packages. Run each with `python3 -I <script> …`:

```bash
# HIG
hig_search.py search "tab bar badge" --platform ios     # full text with the best paragraph
hig_search.py page buttons --section "Platform considerations"
hig_search.py platform watchos                          # all watchOS specifics
hig_search.py list --section Components
hig_search.py updates --since 2026-06-01
hig_sync.py --if-stale 14                               # only sync if older than 14 days

# SF Symbols
sf_symbols.py search trash --min-ios 17
sf_symbols.py info heart                                # categories, fill variant, restrictions
sf_symbols.py categories
sf_symbols.py new 2026                                  # symbols added in a given year

# Devices (requires Xcode)
device_specs.py --family iphone

# Resources
resources.py list --platform macos
resources.py show "sign in with apple"
resources.py download bezels-iphone --accept-license    # presets: fonts, essentials, bezels-iphone,
                                                        # bezels-ipad, bezels-mac, bezels-watch, glyphs, all
resources.py status
```

## Repository layout

```
.claude-plugin/
  plugin.json            plugin manifest
  marketplace.json       marketplace entry (install via /plugin marketplace add)
agents/
  hig-reviewer.md        per-platform audit agent
skills/apple-design/
  SKILL.md               router, principles, quality floor
  reference/
    workflows/           playbooks: init, shape, build, audit, critique, polish, adapt, icon, lookup, resources
    platforms/           ios, ipados, macos, watchos
    foundations/         typography, color-and-dark-mode, layout-and-spacing, materials-and-liquid-glass,
                         icons-and-symbols, accessibility, motion-and-feedback, writing-and-privacy
    components/          decision guide + 8 groups (64 components)
    patterns.md · inputs.md · technologies.md · getting-started.md
  scripts/               hig_sync, hig_search, sf_symbols, device_specs, resources
  data/resources.json    bundled resource catalog (fallback)
  templates/APPLE_DESIGN.md
```

Local data lives outside the repo:

| Path | Content |
|---|---|
| `~/.apple-design/hig/` | HIG mirror (`pages/*.md`, `index.json`) |
| `~/.apple-design/resources.json` | current resource catalog |
| `~/.apple-design/downloads/` | downloaded DMGs |

Set the `APPLE_DESIGN_HOME` environment variable to move the base folder.

## Updating & maintenance

- **Plugin:** `claude plugin marketplace update apple-design-plugin`, then `/reload-plugins`
- **HIG:** Apple updates the guidelines continuously. `/apple-design whatsnew` or `hig_sync.py --if-stale 14` fetches the latest state.
- **Keeping the condensed references current:** `hig_search.py updates --since <last review>` lists changed pages. Update the matching files under `reference/`; the original page always wins.

## Troubleshooting

| Problem | Fix |
|---|---|
| `CERTIFICATE_VERIFY_FAILED` (corporate proxy) | The scripts then fall back to `curl` with the system certificates automatically. Without `curl`: add the certificate to Python or use another network. |
| `device_specs.py`: "Xcode not found" | Install Xcode; the Command Line Tools alone are not enough. The script finds `/Applications/Xcode*.app` even without `xcode-select`. |
| `sf_symbols.py` finds no metadata | macOS only. Alternatively install the SF Symbols app. |
| Skill doesn't show up | Check `/plugin`, run `/reload-plugins`, restart Claude Code |
| HIG mirror outdated or broken | `rm -rf ~/.apple-design/hig && python3 -I hig_sync.py` |

## Contributing

Issues and pull requests are welcome, especially:
- corrections where a condensed reference diverges from the current HIG (cite the `hig:` page),
- coverage for tvOS and visionOS,
- better heuristics for the audit greps.

Please never commit Apple originals (HIG text, images, fonts, templates) to the repo.

## Legal

- **Plugin code and original texts:** MIT, see [LICENSE](LICENSE).
- **Apple content:** HIG text and images, SF fonts, SF Symbols and all Apple Design Resources are © Apple Inc. This repository contains **no** Apple original content, only original condensed summaries with source references, plus a link catalog with the short descriptions from the resources page. The HIG mirror and downloads are created locally on your machine, directly from Apple, and are not meant for redistribution.
- **Fonts:** under Apple's license the SF fonts may only be used to design and develop software for Apple platforms. Don't embed them in app code; the system provides them.
- Apple, iPhone, iPad, Mac, Apple Watch, SF Symbols and Liquid Glass are trademarks of Apple Inc. This project is not affiliated with Apple.
