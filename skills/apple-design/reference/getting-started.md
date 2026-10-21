# Getting started – Design principles and platform fundamentals

Condensed reference for the HIG section "Getting started": Design principles, the "Designing for …" pages per platform, Games, iPhone Duo. Source: local HIG mirror (`~/.apple-design/hig/pages/`, sync 2026-10-21). Sources cited as `(hig:<slug>)` or `(hig:<slug>#Anchor)`. Everything is paraphrased.

## Contents

1. [Design principles](#design-principles)
2. [Platform comparison iOS / iPadOS / macOS / watchOS](#platform-comparison-ios--ipados--macos--watchos)
3. [Designing for iOS](#designing-for-ios)
4. [Designing for iPadOS](#designing-for-ipados)
5. [Designing for macOS](#designing-for-macos)
6. [Designing for watchOS](#designing-for-watchos)
7. [iPhone Duo](#iphone-duo)
8. [Designing for games](#designing-for-games)
9. [tvOS and visionOS (brief)](#tvos-and-visionos-brief)
10. [Observations and ambiguities](#observations-and-ambiguities)

---

## Design principles

Status in the mirror: page "reintroduced" on **2026-06-08** (hig:design-principles). The HIG names **eight** principles. They are not recipes but tools for weighing competing priorities (hig:design-principles).

> Note: Terms like "Hierarchy, Harmony, Consistency" do **not** appear as principle headings in the mirror. "Establish hierarchy" and "consistency" appear only as individual rules under Simplicity and Familiarity respectively. Anyone referring to this triad is relying on a different (older/other) source.

| Principle | Guiding statement (paraphrased) | Core |
|---|---|---|
| Purpose | Create something meaningful | What matters to people – make that great |
| Agency | Let people act their own way | Freedom, keep people informed, mistakes easy to correct |
| Responsibility | Act in people's interest | Safety, privacy, transparency |
| Familiarity | Build on the familiar | Established physical/digital patterns, applied consistently |
| Flexibility | Adapt to contexts and needs | Support many devices, inputs, perspectives |
| Simplicity | Be clear and direct | Remove the unnecessary, structure logically |
| Craft | Care about every detail | Quality as an attitude |
| Delight | Design for humans | Fitting emotion, pleasant to use |

### Rules per principle

**Purpose** (hig:design-principles#Purpose)
- Create value: at every stage, check what the product is for and whether the design serves that.
- Stay focused: prioritize the most important features and make them excellent.
- Solve problems anew: don't copy existing solutions; work out what makes yours distinctive.

**Agency** (hig:design-principles#Agency)
- Don't get in the way: lead directly to the task/content; unobtrusive, but present when needed.
- Freedom to explore: no forced flows/modes; make guided flows skippable.
- Make mistakes correctable: undo/back must be easy and must not cost any work.

**Responsibility** (hig:design-principles#Responsibility)
- Be transparent: make the app's intent clear from the start; justify permission requests; disclose data collection.
- Protect data: collect only what's needed; anticipate and prevent misuse.

**Familiarity** (hig:design-principles#Familiarity)
- Use familiar concepts (real world, other software).
- Keep visuals and interaction consistent – once a behavior is defined, it's the same everywhere.
- Clear feedback: show control availability and content changes; use system patterns for alerts and selection.

**Flexibility** (hig:design-principles#Flexibility)
- Design for everyone; prioritize accessibility from the start; be inclusive.
- Preserve context: content/controls in consistent, predictable positions across platforms and configurations; natural transition animations.
- Account for many input methods (voice, touch, keyboard …).
- Treat every platform with the same care.

**Simplicity** (hig:design-principles#Simplicity)
- Only what's essential – simplicity is not minimalism.
- Be concise; use exactly the words needed for concepts and labels.
- Establish hierarchy: recognizable controls, consistent structure that shows where you are and what comes next.

**Craft** (hig:design-principles#Craft)
- Quality sets the tone (visuals, animation, wording, audio).
- Prototype early, iterate, let go of what's discarded; test in the real environment.
- Maintenance after release: adopt current platform capabilities and patterns.

**Delight** (hig:design-principles#Delight)
- Define the target emotion (fitness: energizing, meditation: calming, game: exciting).
- Design defining moments – from a button press to an error message.
- Delight is not decoration; the task takes precedence.
- Delight comes from the sum: freedom to act, confidence while exploring, familiar metaphors, flexible context switches.

---

## Platform comparison iOS / iPadOS / macOS / watchOS

Basis: the respective "Designing for …" page. Distances as the pages state them (feet in the original; 1 ft ≈ 0.3 m).

| Attribute | iOS (iPhone) | iPadOS | macOS | watchOS |
|---|---|---|---|---|
| Display | medium-size, high-resolution | large, high-resolution | typically large, high-resolution; extendable with additional displays incl. iPad | small, on the wrist, high-resolution; Always On |
| Posture/ergonomics | one- or two-handed, portrait/landscape | handheld, on a surface or stand | stationary on a desk | worn; raise the wrist, other hand operates |
| Viewing distance | no more than one to two feet | mostly within about 3 feet | about 1 to 3 feet | no more than about one foot |
| Primary input | Multi-Touch, virtual keyboard, voice | Multi-Touch, virtual keyboard; additionally hardware keyboard, pointer, Apple Pencil, voice – often combined | physical keyboard, pointing device, game controls, Siri | Digital Crown (vertical navigation, inspecting data), tap/swipe/drag, Action button, Shortcuts |
| Sensors/data | gyro/accelerometer, personal data, nearby interactions | – (not mentioned separately) | – | GPS, blood oxygen, heart sensors, altimeter, accelerometer, gyro |
| Typical session | 1–2 minutes (updates, messages) to over an hour (web, games, media) | a few quick actions to hours of immersion (games, media, creation, productivity) | a few minutes to several hours of focused work | glances, often under a minute; many times a day |
| Multitasking | several apps open, frequent switching | several apps visible at once, drag and drop between apps | many apps in parallel, fluid active/inactive switching | complications, notifications, Siri often more important than the app itself |
| Navigation (best practices) | few controls, secondary items discoverable; interaction in the middle/bottom area; swipe back, swipe actions in rows | use the large screen for content, little modality and few full-screen transitions; controls reachable, not in the way | more content in fewer levels, less modality; menu bar with all commands; freely resizable windows | flat hierarchy, single-screen interactions; Crown for vertical scrolling/switching |
| System features (per page) | Widgets, Home Screen quick actions, Spotlight, Shortcuts, Activity views | Multitasking, Widgets, Drag and drop | Menu bar, File management, Going full screen, Dock menus | Complications, Notifications, Always On, Watch faces |

Sources: (hig:designing-for-ios), (hig:designing-for-ipados), (hig:designing-for-macos), (hig:designing-for-watchos).

Minimum sizes (from the games perspective; per the page, they apply platform-wide as a recommendation; hig:designing-for-games#Look-stunning-on-every-display):

| Platform | Text default / minimum | Button default / minimum |
|---|---|---|
| iOS, iPadOS | 17 pt / 11 pt | 44x44 pt / 28x28 pt |
| macOS | 13 pt / 10 pt | 28x28 pt / 20x20 pt |
| watchOS | 16 pt / 12 pt | 44x44 pt / 28x28 pt |
| tvOS | 29 pt / 23 pt | 66x66 pt / 56x56 pt |
| visionOS | 17 pt / 12 pt | 60x60 pt / 28x28 pt |

---

## Designing for iOS

Context: iPhone as a companion on the go – staying connected, gaming, media, tasks, personal data (hig:designing-for-ios).

- Focus on the primary task and content: few controls on screen, secondary items reachable with minimal interaction.
- Adapt seamlessly to orientation, Dark Mode, and Dynamic Type; people choose the configuration.
- Design for how the device is held: controls in the middle/bottom are easier to reach; swiping to navigate back and for row actions is especially important.
- With permission, use platform data instead of requiring input (Apple Pay, biometric authentication, location).

(all: hig:designing-for-ios#Best-practices)

## Designing for iPadOS

Context: power, mobility, flexibility – media, games, detailed productivity, creation (hig:designing-for-ipados).

- Use the large screen for content; minimize modal interfaces and full-screen transitions; controls reachable but not in the way.
- Determine size and density based on viewing distance and input mode.
- Support Multi-Touch, hardware keyboard/trackpad, and Apple Pencil; consider interactions that combine inputs.
- Adapt to orientation, multitasking modes, Dark Mode, Dynamic Type, and also run cleanly on macOS.

(all: hig:designing-for-ipados#Best-practices)

## Designing for macOS

Context: power, space, flexibility for deep productivity, media, games – often with several apps at once (hig:designing-for-macos).

- Use large displays for more content in fewer nested levels and with less modality, at a comfortable information density.
- Let windows resize, hide/show, move; support full screen for distraction-free work.
- Make all commands reachable through the menu bar.
- Support high-precision input for pixel-accurate selection and editing.
- Support keyboard shortcuts and keyboard-only workflows.
- Allow personalization: customize toolbars, configure window views, choose colors/fonts.

(all: hig:designing-for-macos#Best-practices)

## Designing for watchOS

Context: a glance at the wrist – essential information and simple, timely tasks, even on the move (hig:designing-for-watchos).

- Design quick, glanceable single-screen interactions with one or two gestures.
- Keep the navigation hierarchy flat; use the Digital Crown for vertical scrolling and screen switching.
- Personalize proactively with on-device data: relevant now or soon.
- Use complications for dynamic data directly on the watch face (tap leads into the app).
- Use notifications for time-critical, valuable information and actions without launching the app.
- Use background color for supporting information and materials for hierarchy and a sense of place.
- Build the app to function on its own, complementing notifications and complications.

(all: hig:designing-for-watchos#Best-practices)

---

## iPhone Duo

Page new since **2026-09-09** (hig:designing-for-iphone-duo). iPhone with two displays (outer, inner), each with its own front camera, central hinge; everything from "Designing for iOS" still applies.

- **Anatomy:** The outer display (closed) is wider and shorter than on other iPhones → the system places toolbars/tab bars **at the side**. The inner display in landscape keeps the side position; only the inner display in portrait keeps horizontal bars (hig:designing-for-iphone-duo#Anatomy, #Vertical-controls).
- **Poses:** folded like a book, lying flat, standing on its edge. No separate layout per pose – size classes: compact width outside, regular width inside. Test in Xcode via Device Hub (hig:designing-for-iphone-duo#Device-poses).
- Build resizable: size classes, layout margins, safe area insets; no fixed widths (hig:designing-for-iphone-duo#Best-practices).
- Same functions and states on both displays and in all poses; on the inner display, optionally show one more hierarchy level (example Mail: list + message side by side) (hig:designing-for-iphone-duo#Best-practices).
- Games: playable in every pose; locking orientation is allowed, but fill the screen; adapt the aspect ratio instead of letterboxing/pillarboxing (hig:designing-for-iphone-duo#Best-practices).
- **Reserved regions:** outer camera (always, expands into the Dynamic Island), inner camera (only when active), fold area (when the device is partially open). APIs `ReservedRegion` (SwiftUI) / `UIView.ReservedRegion` (UIKit) (hig:designing-for-iphone-duo#Reserved-regions).
- When folding: prefer self-adapting containers; grids with an even number of columns; no drastic restructuring (hig:designing-for-iphone-duo#Reserved-regions).
- **Arrangement views** (`ArrangementView` / `UIArrangementViewController`): *split* (splits horizontally/vertically depending on aspect ratio) and *overlay* (stacked; when folded, one per side). Place navigation containers outside (hig:designing-for-iphone-duo#Arrangement-views).
- **Vertical controls:** don't override the default placement; Back/Close at the top, then the prominent action (Done); overflow from bottom to top, controllable via `ToolbarItemVisibilityPriority` / `UIBarButtonItemVisibilityPriority`; title + symbol for every item; minimize text buttons; system overflow menu instead of a custom one; ellipsis only for overflow (hig:designing-for-iphone-duo#Vertical-controls).
- Lack of space: navigation-oriented → toolbar items into overflow (default); task-oriented → minimize the tab bar (`ToolbarVerticalCompressionBehavior` / `UIVerticalBarCompressionBehavior`) (hig:designing-for-iphone-duo#Vertical-controls).
- Controls stay on the same side in RTL (hardware-bound); in Split View each app has its controls at its outer edge (hig:designing-for-iphone-duo#Vertical-controls).

---

## Designing for games

For games across all platforms (hig:designing-for-games):

- Playable immediately after installation; download of the base content **no more than 30 minutes**, the rest in the background (hig:designing-for-games#Jump-into-gameplay).
- Good defaults from device information (resolution, paired controllers, accessibility settings) (hig:designing-for-games#Jump-into-gameplay).
- Teach through play; written tutorial only as a reference (hig:designing-for-games#Jump-into-gameplay).
- Request permissions at the fitting moment in the game; ask for ratings only after sufficient play time (hig:designing-for-games#Jump-into-gameplay).
- Text and button sizes per the table above; resolution-independent assets; safe areas; menus for 16:10, 19.5:9, 4:3 and both orientations (hig:designing-for-games#Look-stunning-on-every-display).
- Support each platform's default input; controllers optional with alternatives; touch controls on iPhone/iPad (hig:designing-for-games#Enable-intuitive-interactions).
- Perceivability, personalization (text size, mapping, motion intensity, sound balance), self-expression, no stereotypes (hig:designing-for-games#Welcome-everyone).
- Game Center, GameSave (iCloud), Core Haptics (iOS, iPadOS, tvOS, visionOS), Spatial Audio (hig:designing-for-games#Adopt-Apple-technologies).

---

## tvOS and visionOS (brief)

**tvOS** (hig:designing-for-tvos): very large display, distance often 8 feet or more; Siri Remote, controllers, voice, apps on other devices; hours-long sessions, Picture-in-Picture. Focus system, edge-to-edge artwork, multi-user profiles with simple, infrequent sign-in.

**visionOS** (hig:designing-for-visionos): unlimited space (windows, volumes, 3D); Shared Space (default) vs. Full Space; passthrough via Digital Crown; eyes + indirect gestures; comfort has priority (field of view, calm motion, hands can rest); minimal necessary immersion level per moment; use from age 13, not while driving/moving in a hazardous environment.

---

## Observations and ambiguities

- **Design principles:** The page (update 2026-06-08, "Reintroduced") names eight principles – Purpose, Agency, Responsibility, Familiarity, Flexibility, Simplicity, Craft, Delight. A "Hierarchy / Harmony / Consistency" triad does not exist as a principle in the mirror; it may come from an earlier HIG version or Apple communication. Cannot be sourced from the mirror.
- **iPhone Duo** is a new Getting started page (2026-09-09); other pages (e.g. hig:designing-for-ios) don't mention the device yet.
- **Viewing distances** are given only in feet and partly vaguely ("one to two feet", "about 3 feet") – do not convert them into exact meters.
- **Default input in hig:designing-for-games:** visionOS and watchOS are listed as "Touch"; this deviates from hig:designing-for-visionos (eyes + hands) and hig:digital-crown (Crown as primary navigation since watchOS 10).
- The iOS/iPadOS/tvOS pages partly link with full URLs instead of `hig:` slugs; hig:designing-for-ios refers to the outdated slug `spatial-interactions` (now nearby-interactions).
- The size tables for text and buttons are on the Games page; whether they apply identically to non-games is not stated explicitly there (the iOS 44x44 pt minimum does, however, refer to hig:buttons).
- The iOS, iPadOS, and macOS pages have no update note; watchOS last updated 2023-06-05, Games 2025-06-09.
