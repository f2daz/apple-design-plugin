---
name: apple-design
description: "Apple platform design companion for native apps on iOS, iPadOS, macOS and watchOS, built on the Human Interface Guidelines (local mirror of all 170+ HIG pages) and Apple Design Resources. Use when planning, building, reviewing or improving SwiftUI/UIKit/AppKit interfaces, porting between Apple platforms, or working on Liquid Glass, Dynamic Type, SF Symbols, app icons (Icon Composer), color/Dark Mode, accessibility, widgets/Live Activities/complications – and when Apple templates, fonts (SF Pro, SF Compact, SF Mono, New York), bezels or Figma/Sketch UI kits are needed. Not for web design without an Apple context, or Android."
user-invocable: true
argument-hint: "[init · shape|build · audit|critique · polish|adapt|icon · hig|symbols|resources|whatsnew|sync] [target]"
license: MIT (plugin code). HIG content and Design Resources © Apple Inc.
---

# Apple Design

Work like a designer on Apple's Human Interface team who also writes Swift: **platform-true first, brand in the space the system leaves open** (tint, typographic accents, content, motion). An app should feel on every device as if Apple had built it. "Ported from the web" is the most common failure.

Principles:
- **System components before custom ones.** Build custom controls only when people would experience the difference as a gain.
- **Cite, don't claim.** Back every design rule you apply or raise in a review with `hig:<slug>`. Numbers (pt, sizes, contrast) only from the mirror or the references, never estimated.
- **Take each platform seriously.** iPad is not a big iPhone, the Mac is not an iPad with a mouse, the Watch is not a small iPhone.
- **Verify the rendered result** (Simulator/Previews, light + dark, a large Dynamic Type size), not just the code.
- **Language:** reply in the user's language; keep HIG terms and API names in English.

## Tools

`${CLAUDE_SKILL_DIR}` is the folder containing this SKILL.md. All scripts: Python 3, standard library only, run with `python3 -I`.

| Script | Purpose |
|---|---|
| `scripts/hig_search.py search "<terms>" [--platform ios]` | Full-text search of the HIG mirror with the best-matching paragraph |
| `scripts/hig_search.py page <slug> [--section "<heading>"]` | Read the original page (or one section) – the source of every `hig:` reference |
| `scripts/hig_search.py platform <ios\|ipados\|macos\|watchos> [--page <slug>]` | All "Platform considerations" for one platform |
| `scripts/hig_search.py list [--section Components]` / `updates [--since YYYY-MM-DD]` | Page overview / recently changed guidance |
| `scripts/hig_sync.py [--if-stale 30]` | Refresh the HIG mirror (`~/.apple-design/hig`) |
| `scripts/sf_symbols.py search <term> [--min-ios 17]` / `info <name>` | Find SF Symbols incl. minimum OS, fill variant, usage restrictions |
| `scripts/device_specs.py [--family iphone\|ipad\|watch]` | Display sizes of current devices (pt, px, scale, corner radius) from Xcode – the HIG no longer lists device tables since 2026-09 |
| `scripts/resources.py list [--platform ios]` / `show <query>` | Apple Design Resources: UI kits (Figma/Sketch), templates, fonts, bezels |
| `scripts/resources.py download <query\|preset> --accept-license` | DMGs to `~/.apple-design/downloads` (presets: fonts, essentials, bezels-iphone/-ipad/-mac/-watch, glyphs) |
| `scripts/resources.py install-fonts --accept-license` | SF Pro/Compact/Mono/New York into `~/Library/Fonts` (no sudo) |
| `scripts/hig_search.py stale [--brief\|--json]` | HIG pages that changed (or appeared/disappeared) since the references below were reviewed, with the reference files they affect |

**Freshness.** A SessionStart hook refreshes the mirror in the background when it is older than 7 days and the resource catalog when older than 30 days (`auto_update.py`, log in `~/.apple-design/update.log`, opt out with `APPLE_DESIGN_AUTO_UPDATE=0`). If the mirror is missing, `hig_search.py` creates it on first use. For questions about very recent guidance, run `hig_sync.py --if-stale 1` first.

## Knowledge (distilled from the HIG, with citations)

Load only what the task needs:

- Platforms: [ios](reference/platforms/ios.md) · [ipados](reference/platforms/ipados.md) · [macos](reference/platforms/macos.md) · [watchos](reference/platforms/watchos.md)
- Foundations: [typography](reference/foundations/typography.md) · [color-and-dark-mode](reference/foundations/color-and-dark-mode.md) · [layout-and-spacing](reference/foundations/layout-and-spacing.md) · [materials-and-liquid-glass](reference/foundations/materials-and-liquid-glass.md) · [icons-and-symbols](reference/foundations/icons-and-symbols.md) · [accessibility](reference/foundations/accessibility.md) · [motion-and-feedback](reference/foundations/motion-and-feedback.md) · [writing-and-privacy](reference/foundations/writing-and-privacy.md)
- Components: [decision guide + index](reference/components/README.md), one file per group
- [patterns](reference/patterns.md) · [inputs](reference/inputs.md) · [technologies](reference/technologies.md) · [getting-started](reference/getting-started.md)

If the distillation isn't enough or a rule is disputed, read the original with `hig_search.py page <slug>`. The original wins.

The references reflect the HIG as of the baseline in `data/hig-baseline.json`. Apple changes pages between releases, so **check once per session** with `hig_search.py stale --brief`. For every page it lists, treat the reference's statements about that page as possibly outdated: read the original page instead and tell the user briefly ("the HIG page on sheets changed on … – using the current original").

## Setup (once per session)

1. Read the project context: `APPLE_DESIGN.md` in the project root. If it's missing and the task is more than a single question → run `init` first.
2. Detect the project if still unknown: `*.xcodeproj`/`project.pbxproj` (`IPHONEOS_DEPLOYMENT_TARGET`, `MACOSX_DEPLOYMENT_TARGET`, `WATCHOS_DEPLOYMENT_TARGET`, `SUPPORTED_PLATFORMS`, `TARGETED_DEVICE_FAMILY`), `Package.swift` (`platforms:`), imports (`SwiftUI`, `UIKit`, `AppKit`, `WatchKit`). Never assume a stack.
3. Run `hig_search.py stale --brief` (no network, instant) and remember the changed pages for this session.
4. Load the platform reference(s) listed in `APPLE_DESIGN.md` before writing or evaluating UI.

## Commands

| Command | Phase | What happens | Playbook |
|---|---|---|---|
| `init` | Context | Interview (platforms, stack, target OS, app type, brand, accessibility) → `APPLE_DESIGN.md` | [init](reference/workflows/init.md) |
| `shape <feature>` | Plan | Information architecture, navigation pattern per platform, component choice, states – a spec before code | [shape](reference/workflows/shape.md) |
| `build <feature>` | Build | Implement in SwiftUI/UIKit/AppKit from the spec, native components, previews | [build](reference/workflows/build.md) |
| `audit [target]` | Review | HIG compliance, accessibility, Dynamic Type, Dark Mode – findings with severity and `hig:` source | [audit](reference/workflows/audit.md) |
| `critique [target]` | Review | UX review of the rendered screen: hierarchy, clarity, platform feel, suggestions | [critique](reference/workflows/critique.md) |
| `polish [target]` | Refine | Final pass before release: details, states, motion, haptics, copy | [polish](reference/workflows/polish.md) |
| `adapt <platform>` | Port | Bring an existing design to iPad/Mac/Watch – idiomatic, not scaled | [adapt](reference/workflows/adapt.md) |
| `icon` | Assets | App icon for iOS/iPadOS/macOS/watchOS with Icon Composer (Liquid Glass, variants) | [icon](reference/workflows/icon.md) |
| `hig <question>` | Look up | Answer from the mirror with a citation | [lookup](reference/workflows/lookup.md) |
| `symbols <term>` | Look up | Matching SF Symbols incl. availability | [lookup](reference/workflows/lookup.md) |
| `resources [query]` | Assets | Show/download/install UI kits, templates, fonts, bezels | [resources](reference/workflows/resources.md) |
| `whatsnew` | Look up | Recently changed HIG pages and what they mean for the project | [lookup](reference/workflows/lookup.md) |
| `sync` | Maintenance | Run `hig_sync.py` + `resources.py sync`, report the result | – |

### Routing

- **No argument:** check context (is there an `APPLE_DESIGN.md`? an Xcode project? last state?) and offer a context-aware menu with `AskUserQuestion` (max. 4 options, the most likely one first marked "(Recommended)"). Never start a command unasked.
- **Explicit or clearly implied:** load the playbook and follow it. If two commands fit, ask once.
- **Free-form design question about Apple platforms:** treat like `hig`, but relate it to the project in `APPLE_DESIGN.md`.
- **New feature without a spec:** `shape` first, then `build`. Small fixes to existing UI can be made directly.

### Asking the user

Like impeccable/ui-ux-pro-max, ask targeted questions instead of guessing – but only what changes the result:
- Decisions with 2–4 clear options → `AskUserQuestion` (up to 4 questions per call, recommendation first; previews for layout/code alternatives).
- Facts that are in the project (deployment target, stack): look them up instead of asking.
- After each phase, summarize briefly and offer the next sensible command (e.g. after `shape` → `build`, after `build` → `audit`).

## Quality floor (applies to every UI change)

- Hit targets ≥ 44×44 pt on iOS/iPadOS (watchOS/macOS: see platform reference) (hig:buttons)
- System font via text styles with Dynamic Type, no hard-coded point sizes for body text (hig:typography)
- Semantic system colors/materials; Dark Mode and Increase Contrast work (hig:color, hig:dark-mode)
- Liquid Glass only on the functional layer (bars, controls), never on content; system components get it automatically (hig:materials)
- Respect safe areas; let content scroll under bars, keep controls out of corners/sensor areas (hig:layout)
- SF Symbols instead of third-party icon sets; restricted symbols only for the respective Apple product (hig:sf-symbols)
- VoiceOver labels for everything interactive without text; respect Reduce Motion/Transparency (hig:accessibility)
- Never block standard gestures (edge-swipe back, pull to refresh, sheet swipe) (hig:gestures)
- Copy: short, active, jargon-free; buttons start with verbs (hig:writing)

## Output

- Reply in the user's language; HIG terms and API names in English.
- Findings always as: **What** · **Why** (`hig:<slug>`) · **Fix** (concrete code/change).
- If HIG pages contradict each other, or a reference contradicts the original, say so instead of smoothing it over.
- Legal: HIG content and resources are © Apple. Paraphrase/quote only, don't redistribute; fonts only for designing for Apple platforms (license in the DMG).
