# iOS (iPhone) – Platform reference

> Source: local HIG mirror `~/.apple-design/hig/pages/<slug>.md` (as of 2026-10-21). Sources cited as `(hig:<slug>)` or `(hig:<slug>#Anchor)`.
> Paraphrased and condensed, no original text. Numbers only where they appear in the mirror.

---

## 1. Profile

- **Display:** medium-sized, high resolution; hardware features such as the Dynamic Island and the status bar limit the usable area (hig:designing-for-ios, hig:layout#Guides-and-safe-areas).
- **Ergonomics:** held in one or both hands, portrait and landscape, viewing distance roughly one to two feet. The middle and lower part of the screen are the easiest to reach (hig:designing-for-ios).
- **Input:** Multi-Touch, virtual keyboard, voice (Siri); plus sensors (gyroscope/accelerometer), personal data with permission (hig:designing-for-ios).
- **Usage patterns:** very short sessions (minutes) as well as long ones (hours); frequent app switching, several apps open (hig:designing-for-ios).
- **Multitasking on iPhone:** Picture in Picture (video, FaceTime) over other apps (hig:multitasking#iOS). Special case **iPhone Duo** (two displays, hinge, Split View multitasking on the inner display) – see section 4.4 (hig:designing-for-iphone-duo).
- **System surfaces:** widgets, Home Screen quick actions, Spotlight, Shortcuts, activity views, Live Activities, Control Center (hig:designing-for-ios, hig:controls).

---

## 2. Non-negotiable

1. **Decide layout by size class, never by device type or orientation**; plan for every compact/regular combination (hig:layout#Size-classes).
2. **Respect safe areas and system margins** – the Dynamic Island, status bar, toolbars and tab bar must not obscure content/controls (hig:layout#Guides-and-safe-areas).
3. **Fully support Dynamic Type**, including accessibility sizes (AX1–AX5); the layout must wrap/stack instead of truncating (hig:typography#Supporting-Dynamic-Type, hig:layout#Adaptability).
4. **Hit targets: default 44×44 pt, minimum 28×28 pt** (hig:accessibility#Mobility, hig:buttons#Best-practices).
5. **Tab bar for navigation only, never for actions**; actions belong in a toolbar (hig:tab-bars#Best-practices).
6. **Keep the tab bar visible in every section** (exception: a modal covers it); never disable or hide tabs (hig:tab-bars#Best-practices).
7. **Liquid Glass only in the functional layer** (bars, controls), not in the content layer; use sparingly on custom controls (hig:materials#Liquid-Glass).
8. **No custom bar backgrounds/tints**; separate via the scroll edge effect instead of an opaque surface (hig:toolbars#Best-practices, hig:layout#Visual-hierarchy).
9. **Use the standard Back and Close buttons**, no text labels "Back"/"Close" (hig:toolbars#Navigation).
10. **Every modal must be obviously dismissible** – a button in the top toolbar or swipe down; if data loss is imminent, confirm via an action sheet (hig:modality#Best-practices, hig:sheets#iOS-iPadOS).
11. **Only one sheet at a time**, never more than one alert at a time (hig:sheets#Best-practices, hig:modality#Best-practices).
12. **Support Light, Dark and Increased Contrast** – even single-appearance apps should supply both color variants (Liquid Glass adaptivity) (hig:color).
13. **Do not override system gestures** (edge swipes, Home indicator, three-finger undo, shake) (hig:gestures#Custom-gestures, hig:undo-and-redo#iOS-iPadOS).
14. **Launch screen = nearly identical to the first screen**, no text, no branding/advertising (hig:launching#Launch-screens).
15. **Save and restore context** – the app can be interrupted at any time (hig:multitasking#Best-practices, hig:launching#Best-practices).

---

## 3. Layout & dimensions

### 3.1 Documented values

| Metric | Value | Source |
|---|---|---|
| Control size default / minimum | 44×44 pt / 28×28 pt | (hig:accessibility#Mobility) |
| Button hit region at least | 44×44 pt | (hig:buttons#Best-practices) |
| Padding around elements with a bezel | approx. 12 pt | (hig:accessibility#Mobility) |
| Padding around elements without a bezel | approx. 24 pt (around visible edges) | (hig:accessibility#Mobility) |
| Text size default / minimum | 17 pt / 11 pt | (hig:typography#Ensuring-legibility) |
| Offer text enlargement | at least 200 % | (hig:accessibility) |
| Toolbar/window title | under 15 characters | (hig:toolbars#Titles) |
| Toolbar groups | max. approx. 3 | (hig:toolbars#Item-groupings) |
| Sign in with Apple button height (default iOS) | 44 pt | (hig:sign-in-with-apple) |
| Show drag image after | approx. 3 pt of movement | (hig:drag-and-drop#Providing-feedback) |
| Dimming behind clear Liquid Glass over bright content | 35 % opacity, dark | (hig:materials#Liquid-Glass) |
| Home Screen quick actions | max. 4 | (hig:home-screen-quick-actions) |
| App icon layout size | 1024×1024 px, square, system mask | (hig:app-icons#Specifications) |

### 3.2 Device sizes / safe area insets

**Not contained in the mirror.** The page `layout.md` (updated 2026-09-09) no longer contains a device table or safe area insets, even though the change log mentions earlier specifications (iPhone 14–17, iPhone Air, 16e). Therefore **never hard-code** safe area values; obtain them at runtime via `safeAreaInsets`/layout guides; take values for mockups from Apple Design Resources (hig:layout, hig:designing-for-iphone-duo#Dynamic-layouts).

iPhone screen sizes documented indirectly (portrait, pt) from the widget and Live Activity tables, **without device mapping in the mirror**: 430×932, 428×926, 414×896, 414×736, 393×852, 390×844, 375×812, 375×667, 360×780, 320×568 (hig:widgets#Specifications, hig:live-activities#Specifications).

### 3.3 Adaptability – what the app must handle
(hig:layout#Adaptability)
- compact/regular on both axes, portrait/landscape, different aspect ratios
- Dynamic Island, Display Zoom, iPhone Mirroring on the Mac (freely resizable window size)
- text size changes, RTL layout, localized date/number formats, text lengths
- Even orientation-locked apps (e.g., landscape games) must scale cleanly; scale background artwork instead of distorting/letterboxing it.
- Landscape-only: handle both landscape orientations (rotated left/right) correctly; launch in the current device orientation (hig:launching#iOS-iPadOS).

### 3.4 Visual hierarchy
- Most important at the top and leading; alignment for scanning, indentation for subordination (hig:layout#Visual-hierarchy).
- Group related items (white space, containers, separators); progressive disclosure (hig:layout#Visual-hierarchy).
- Let full-bleed backgrounds extend under the toolbar and tab bar (hig:layout#Visual-hierarchy).

---

## 4. Navigation & structure

### 4.1 Decision matrix

| Situation | Pattern | Source |
|---|---|---|
| 2+ peer top-level sections | **Tab bar** (bottom, floating, Liquid Glass) | (hig:tab-bars#iOS) |
| Hierarchical drill-down | **Navigation stack** with toolbar (navigation bar), large title, Back button | (hig:toolbars#Navigation, hig:toolbars#iOS) |
| Several levels side by side | **Split view only in regular width** (e.g., large iPhone model in landscape, iPhone Duo inner display); compact → single column | (hig:split-views#iOS) |
| Narrowly scoped subtask | **Sheet** (detents medium/large) | (hig:sheets) |
| Complex/long task, media, camera | **Full-screen modal** | (hig:sheets#Best-practices, hig:modality) |
| Choices related to an action just initiated | **Action sheet** (not a menu, not an alert) | (hig:action-sheets#iOS-iPadOS, hig:alerts#iOS-iPadOS) |
| Critical info/confirmation | **Alert** | (hig:alerts) |
| Switching between closely related subviews | **Segmented control** (not a tab bar) | (hig:segmented-controls#iOS-iPadOS) |
| Additional information in compact width | **no popover**, use a sheet instead | (hig:popovers#iOS-iPadOS) |
| Paging (Weather-style) | Paged scroll view + page control; then no scroll indicator on the same axis | (hig:scroll-views#iOS-iPadOS) |

### 4.2 Tab bar (iOS)
- Floats at the bottom above the content on Liquid Glass (hig:tab-bars#iOS).
- Optional **bottom accessory** (e.g., MiniPlayer); the tab bar can minimize when scrolling down, the accessory moves inline. Restored by tapping a tab or scrolling up (hig:tab-bars#iOS).
- Optional **search tab** at the trailing end (hig:tab-bars#iOS, hig:search-fields#iOS).
- Always use labels (ideally one word), SF Symbols, preferably filled; in compact, icon above label (hig:tab-bars#Best-practices).
- Avoid the More tab (overflow); explain empty sections instead of disabling the tab (hig:tab-bars#Best-practices).
- Badge only for critical info (red oval) (hig:tab-bars#Best-practices).
- Tab label color must not resemble the content background; monochrome over colorful content (hig:tab-bars#Best-practices, hig:color#Liquid-Glass-color).

### 4.3 Toolbars / navigation bar (iOS)
- Only the most important items in the main area; the rest in a **More menu** (hig:toolbars#iOS).
- **Large title** for orientation; collapses to the standard title when scrolling (hig:toolbars#iOS).
- Three zones: leading (Back, title, document menu), center, trailing (important actions, search, More, primary action) (hig:toolbars#Item-groupings).
- **One** primary action (Done/Submit) in the `.prominent` style, trailing (hig:toolbars#Actions).
- Symbols without borders (no circle outlines); text only where no symbol works (e.g., "Edit"); separate text and symbol buttons with fixed space (hig:toolbars#Actions, hig:toolbars#Item-groupings).
- Do not use the app name as the title (hig:toolbars#Titles).
- Custom components in bars: corner radii concentric with the bar (hig:toolbars#Best-practices).

### 4.4 iPhone Duo (in the mirror since 2026-09-09)
(hig:designing-for-iphone-duo)
- Outer display = compact width, inner display = regular width; cover postures via size classes, **no** custom layout per posture.
- Toolbars, tab bar, status bar and Dynamic Island move **vertically to the side** when the device is closed (and on the inner display in landscape); exception: inner display in portrait. Do not override the standard placement.
- Vertical order: navigation (Back/Close) at the top, then the prominent action (Done), keep remaining groups; overflow runs from bottom to top, controllable via visibility priority.
- **Reserved regions**: outer camera (always; becomes the Dynamic Island for Live Activities), inner camera (only when active), fold area (only when partially folded). Keep custom views clear via `ReservedRegion`; grids with an even number of columns.
- Split view: on the inner display when unfolded, single column on the outer display. **Arrangement views** (split/overlay) for two-part layouts; navigation containers belong outside them.
- Every toolbar action with a title **and** a symbol (the title is used in the overflow); minimize text buttons; move your own overflow menu into the system overflow menu.
- Lack of space: navigation-heavy → toolbar items into the overflow; task-heavy → minimize the tab bar.

### 4.5 Sheets (iOS)
(hig:sheets#iOS-iPadOS, hig:sheets#Best-practices)
- Single view: **Cancel leading, Done trailing** in the top toolbar. Multi-step: step 1 Cancel + (inactive) Done; subsequent steps Back + Done. Never Cancel, Done and Back at the same time.
- Always pair Done with an alternative (Cancel or Back).
- Detents: *large* (full), *medium* (approx. half height), custom possible. Medium for progressive disclosure (share sheet); compose-like tasks only large.
- Show a **grabber** on resizable sheets (also relevant for VoiceOver).
- Support swipe to dismiss; for unsaved changes, confirm with an action sheet.
- Sheets can be **nonmodal** (e.g., the format sheet in Notes) when they affect the parent view.
- Do not stack a second sheet from within a sheet; dismiss first.

### 4.6 Search (iOS)
(hig:search-fields#iOS)
- Three places: **tab** (standard tab with a landing page for discovery; or button appearance for immediate typing), **toolbar** (bottom preferred if there is room; top if content at the bottom takes priority), **inline** (filtering a list; at the top above the list, optionally pinned to the toolbar).

### 4.7 Modality in general
(hig:modality)
- Only when there is a clear benefit; short and simple; no "app within the app" with its own hierarchy.
- The title names the task.

---

## 5. Component specifics (platform considerations iOS)

| Component | Rule | Source |
|---|---|---|
| Action sheet | For choices related to an action; must not scroll | (hig:action-sheets#iOS-iPadOS) |
| Alert | Avoid scrolling where possible (short titles, message only if needed); for errors use an alert instead of a notification | (hig:alerts#iOS-iPadOS, hig:notifications) |
| Buttons | Activity indicator inside the button for delayed actions, optionally label "Checking out…"; 1–2 prominent buttons per view; pressed state mandatory | (hig:buttons#iOS-iPadOS, hig:buttons#Style) |
| Button roles | Primary never for a destructive action; destructive = system red | (hig:buttons#Role) |
| Context menu | Either a context menu or an edit menu per object, not both; graphical preview; destructive items at the end, red | (hig:context-menus#iOS-iPadOS, hig:context-menus) |
| Menus | Layouts small (4 symbols at the top), medium (3 symbols + label), large (list, default) | (hig:menus#iOS-iPadOS) |
| Edit menu | compact horizontal with touch, vertical with keyboard/pointer; adjust position if needed | (hig:edit-menus#iOS-iPadOS) |
| Pull-down | More button (ellipsis) for secondary items, weigh against discoverability | (hig:pull-down-buttons#iOS-iPadOS) |
| Lists | Info button only for additional info, drill-down via disclosure indicator; no index with trailing accessories | (hig:lists-and-tables#iOS-iPadOS-visionOS) |
| Toggles | Switch only in list rows (without extra label); elsewhere a toggle button; change green only if needed | (hig:toggles#iOS-iPadOS) |
| Slider | Never for volume – use a volume view | (hig:sliders#iOS-iPadOS) |
| Date picker | Styles compact/inline/wheels/automatic; countdown max. 23 h 59 min; compact when space is tight | (hig:pickers#iOS-iPadOS) |
| Text fields | Clear button trailing; leading = purpose, trailing = additional function | (hig:text-fields#iOS-iPadOS) |
| Text views | Show the appropriate keyboard type | (hig:text-views#iOS-iPadOS) |
| Virtual keyboard | Keyboard layout guide; input accessory controls only if task-relevant, if needed Liquid Glass or a standard toolbar | (hig:virtual-keyboards#iOS-iPadOS) |
| Page control | Background automatic/prominent/minimal; no scrubbing with minimal; no animation while scrubbing | (hig:page-controls#iOS-iPadOS) |
| Refresh control | Refresh automatically; title only if it adds value (e.g., last update) | (hig:progress-indicators#iOS-iPadOS) |
| Collections | Do not change layout during interaction | (hig:collections#iOS-iPadOS) |
| Status bar | Dim/obscure content beneath it; hide temporarily only for full-screen media, never permanently | (hig:status-bars) |
| Full screen | Keep Home indicator behavior; switch to two-swipe exit only in case of accidental exits | (hig:going-full-screen#iOS-iPadOS) |
| Gestures | Three-finger swipe undo/redo, three-finger pinch copy/paste, shake to undo; simultaneous gestures mainly for games | (hig:gestures#iOS-iPadOS) |
| Undo/redo | Alert title "Undo <object>" precise; do not redefine standard gestures | (hig:undo-and-redo#iOS-iPadOS) |
| Haptics | Standard controls use system haptics; feedback generator: notification (success/warning/error), impact (light/medium/heavy/rigid/soft), selection | (hig:playing-haptics#iOS) |
| Audio | System Sound Services for short sounds/vibrations | (hig:playing-audio#iOS-iPadOS) |
| Colors | Background sets *system* and *grouped* (primary/secondary/tertiary); label hierarchy label…quaternaryLabel, separator, link | (hig:color#iOS-iPadOS) |
| Dark Mode | base vs. elevated backgrounds; prefer system background colors | (hig:dark-mode#iOS-iPadOS) |
| Files | Document launcher (iOS 18 and later) with title card (2 buttons), background, accessories; File Provider extension without its own top toolbar | (hig:file-management#iOS-iPadOS) |
| Action button | Actions without launching the app (Live Activity, snippets) | (hig:action-button#iOS) |

---

## 6. Liquid Glass & materials

- **Two layers:** Liquid Glass = functional layer (tab bar, toolbars, sidebars, controls), floats above the content layer; standard materials = differentiation *within* the content layer (hig:materials).
- **No Liquid Glass in the content layer.** Exception: transient controls (slider, toggle) take on the glass look while being operated (hig:materials#Liquid-Glass).
- **Variants:** *regular* (blurs/adjusts luminance, default for most system components, for text-heavy elements such as alerts, sidebars, popovers) and *clear* (highly transparent, only over visually rich media). With clear over bright content, a dark dimming layer of 35 %; not needed over dark content or with AVKit controls (hig:materials#Liquid-Glass).
- **Use sparingly on custom controls**; standard components adopt glass automatically (hig:materials#Liquid-Glass).
- **Color:** glass is colorless and picks up color from the background. Tint only for emphasis (primary action, status), and then on the control's **background**, not on the symbol/text; not several tinted controls. Small elements (tab bar, toolbar) automatically switch light/dark with monochrome symbols (hig:color#Liquid-Glass-color).
- **Scroll edge effect** instead of opaque bar backgrounds: prefer *automatic*; *hard* = more opaque with an edge, *soft* = gentle gradient (test it); only when scrolling content sits under floating elements; one per view (hig:scroll-views#Scroll-edge-effects).
- **Background extension effect** when a background image should continue mirrored and blurred under a sidebar/inspector (hig:layout#Visual-hierarchy).
- **Standard materials iOS:** ultraThin, thin, regular (default), thick; plus vibrancy for labels (label…quaternaryLabel; quaternary not on thin/ultraThin), fills (fill…tertiaryFill), separator (one level) (hig:materials#iOS-iPadOS).
- **Choose material by semantics, not by color effect**; thicker materials for fine text, thinner ones for context (hig:materials#Standard-materials).
- **App icons** are layered and receive Liquid Glass effects (reflections, refraction); appearances default, dark, clear light/dark, tinted light/dark; unmasked square layers, vector preferred, design in Icon Composer (hig:app-icons).

---

## 7. Typography & Dynamic Type

- System font **SF Pro**, plus **New York** (serif) (hig:typography#iOS-iPadOS). Do not embed system fonts; access them via `Font.Design` (hig:typography#Using-system-fonts).
- Default 17 pt, minimum 11 pt; avoid light weights (Ultralight/Thin/Light) (hig:typography#Ensuring-legibility).
- Use built-in text styles → Dynamic Type including AX sizes for free; custom fonts must support Dynamic Type and Bold Text themselves (hig:typography#Using-custom-fonts).
- At large sizes: stack instead of side by side, reduce columns, minimize truncation, scale icons too, maintain hierarchy (hig:typography#Supporting-Dynamic-Type).
- Tracking is automatic in the running system; for mockups use the tracking tables (hig:typography#Tracking-values).

### 7.1 Default size "Large" (pt; weight / leading / emphasized)
(hig:typography#Specifications)

| Style | Weight | Size | Leading | Emphasized |
|---|---|---|---|---|
| Large Title | Regular | 34 | 41 | Bold |
| Title 1 | Regular | 28 | 34 | Bold |
| Title 2 | Regular | 22 | 28 | Bold |
| Title 3 | Regular | 20 | 25 | Semibold |
| Headline | Semibold | 17 | 22 | Semibold |
| Body | Regular | 17 | 22 | Semibold |
| Callout | Regular | 16 | 21 | Semibold |
| Subhead | Regular | 15 | 20 | Semibold |
| Footnote | Regular | 13 | 18 | Semibold |
| Caption 1 | Regular | 12 | 16 | Semibold |
| Caption 2 | Regular | 11 | 13 | Semibold |

### 7.2 Size progression of selected styles (pt)
(hig:typography#Specifications)

| Style | xS | S | M | **L** | xL | xxL | xxxL | AX1 | AX2 | AX3 | AX4 | AX5 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Large Title | 31 | 32 | 33 | **34** | 36 | 38 | 40 | 44 | 48 | 52 | 56 | 60 |
| Title 1 | 25 | 26 | 27 | **28** | 30 | 32 | 34 | 38 | 43 | 48 | 53 | 58 |
| Body/Headline | 14 | 15 | 16 | **17** | 19 | 21 | 23 | 28 | 33 | 40 | 47 | 53 |
| Subhead | 12 | 13 | 14 | **15** | 17 | 19 | 21 | 25 | 30 | 36 | 42 | 49 |
| Footnote | 12 | 12 | 12 | **13** | 15 | 17 | 19 | 23 | 27 | 33 | 38 | 44 |
| Caption 2 | 11 | 11 | 11 | **11** | 13 | 15 | 17 | 20 | 24 | 29 | 34 | 40 |

Complete tables (all styles, leading) in the mirror under `typography.md#Specifications`. Point sizes are based on 144 ppi (@2x) or 216 ppi (@3x).

---

## 8. System integration

### 8.1 Widgets
(hig:widgets)
- Home Screen / Today View: system small, medium, large; StandBy, CarPlay, Apple HomeView: small only. Lock Screen: accessory circular, rectangular, inline (above the clock). No extra large on iPhone.
- Think of Lock Screen widgets like complications: information, not an app launcher; Always-On with reduced luminance → enough grayscale contrast.
- Appearances on the Home Screen: light, dark, clear, tinted (the system desaturates; explicitly opt in full-color images). Observe rendering modes full-color / accented / vibrant.
- StandBy: two small widgets side by side, scaled up, background removed → mark the background as removable, enlarge text instead of relying on image colors; night mode red monochrome.
- Margins **16 pt** standard, **11 pt** for tight groupings; text ≥ **11 pt**; do not rasterize text; corner radii via `ContainerRelativeShape` (hig:widgets#Choosing-margins-and-padding, hig:widgets#Displaying-text-in-widgets).
- Animations on updates up to **2 s** (hig:widgets#Updating-widget-content).
- A tap opens the matching location in the app; keep interaction simple, no app-like layout.
- Real-time → Live Activity instead of a widget.

**Widget sizes iPhone (pt)** (hig:widgets#Specifications)

| Screen (portrait) | Small | Medium | Large | Circular | Rectangular | Inline |
|---|---|---|---|---|---|---|
| 430×932 | 170×170 | 364×170 | 364×382 | 76×76 | 172×76 | 257×26 |
| 428×926 | 170×170 | 364×170 | 364×382 | 76×76 | 172×76 | 257×26 |
| 414×896 | 169×169 | 360×169 | 360×379 | 76×76 | 160×72 | 248×26 |
| 414×736 | 159×159 | 348×157 | 348×357 | 76×76 | 170×76 | 248×26 |
| 393×852 | 158×158 | 338×158 | 338×354 | 72×72 | 160×72 | 234×26 |
| 390×844 | 158×158 | 338×158 | 338×354 | 72×72 | 160×72 | 234×26 |
| 375×812 | 155×155 | 329×155 | 329×345 | 72×72 | 157×72 | 225×26 |
| 375×667 | 148×148 | 321×148 | 321×324 | 68×68 | 153×68 | 225×26 |
| 360×780 | 155×155 | 329×155 | 329×345 | 72×72 | 157×72 | 225×26 |
| 320×568 | 141×141 | 292×141 | 292×311 | – | – | – |

### 8.2 Live Activities
(hig:live-activities)
- For tasks with a beginning and an end, max. approx. **8 hours**; no advertising; sensitive data only as a harmless summary.
- Presentations: compact (leading + trailing around the TrueDepth camera, readable as *one* piece of info, snug against the camera), minimal, expanded, Lock Screen, StandBy. Design for iPhone first, then refine.
- **Limited width** (e.g., Dynamic Island in landscape): fit compact/minimal into a circle of **28 pt** diameter.
- Lock Screen margin **14 pt**; adjust height dynamically; do not copy the look of notifications; check the dismiss button color.
- Dynamic Island: black, opaque background, cannot be changed → bold colors, tint the key line. Logo without a container, never the whole app icon. Nothing in the app that points to the Dynamic Island.
- Text: large, at least medium weight.
- End it immediately when done; on the Lock Screen it remains for up to **4 hours**. Alerts only for essential updates. Rotate multiple events within *one* activity.
- Offer an App Shortcut to start it (e.g., via the Action button).

**Live Activity dimensions iPhone (pt)** (hig:live-activities#Specifications)

| Screen (portrait) | Compact (per side) | Minimal (width) | Expanded (height) | Lock Screen (height) | Limited width |
|---|---|---|---|---|---|
| 430×932 | 62.33×36.67 | 36.67–45 × 36.67 | 408 × 84–160 | 408 × 84–160 | 28×28 |
| 393×852 | 52.33×36.67 | 36.67–45 × 36.67 | 371 × 84–160 | 371 × 84–160 | 28×28 |

### 8.3 Controls (Control Center, Lock Screen, Action button)
(hig:controls)
- Button or toggle with symbol, title, optional value; the symbol must be understandable on its own (the Lock Screen shows only the symbol).
- Symbol animation for state changes; tint color matching the brand; hint text for the Action button; placeholder when title/value depend on the situation.
- Redact sensitive values while locked; security-relevant actions only after unlocking.

### 8.4 App Shortcuts / App Intents / Siri
(hig:app-shortcuts)
- Most frequent, most important tasks; at most one optional parameter; short phrases; order by importance in Spotlight (top hit) and the Shortcuts app.
- Consider app schemas for standard domains. Responses must also be understandable audio-only.

### 8.5 Notifications & badges
(hig:notifications)
- Short, no duplicates, no sensitive data, no app name/icon in the text; generic text for hidden previews.
- Actions: time-saving, not "Open app", preferably nondestructive, with a symbol.
- Badge only for the number of unread notifications; never imitate it.

### 8.6 Other
- Home Screen quick actions: max. 4, SF Symbols instead of emoji, stable titles (hig:home-screen-quick-actions).
- System rating prompt; the system limits it to 3× per 365 days (hig:ratings-and-reviews).
- Prefer passkeys when Sign in with Apple is not used (hig:managing-accounts).

---

## 9. Implementation: SwiftUI / UIKit

Legend: **[S]** = API referenced in the mirror; **[K]** = common API, framework knowledge, not documented in the mirror – verify in the developer documentation before use.

| Pattern | SwiftUI | UIKit |
|---|---|---|
| Tab navigation | `TabView` [S], `Tab` [K], `Tab(role: .search)` [K] | `UITabBarController` [K], `UITabBar` [S] |
| Minimize tab bar / accessory | `TabBarMinimizeBehavior` [S], `tabViewBottomAccessory` [K] / `TabViewBottomAccessoryPlacement` [S] | `UITabBarController.MinimizeBehavior` [S] |
| Navigation stack | `NavigationStack` [K], `.navigationTitle` [K] | `UINavigationController` [K], `prefersLargeTitles` [S] |
| Split view | `NavigationSplitView` [S] | `UISplitViewController` [S] |
| Toolbar | `.toolbar` / `ToolbarItem(placement:)` [K], `ToolbarItemGroup` [S], `ToolbarItemPlacement` [S], `ToolbarItemVisibilityPriority` [S], `ToolbarOverflowMenu` [S] | `UIToolbar` [S], `UIBarButtonItemGroup` [S], `fixedSpace` [S], `additionalOverflowItems` [S] |
| Sheet / detents | `.sheet(item:)` [S], `.presentationDetents` [K], `.presentationDragIndicator` [K] | `UISheetPresentationController` [S], `detents` [S], `prefersGrabberVisible` [S] |
| Full-screen modal | `.fullScreenCover` [K] | `UIModalPresentationStyle.fullScreen` [S] |
| Action sheet | `.confirmationDialog` [K] (mirror: "presentation modifier for a confirmation dialog") | `UIAlertController.Style.actionSheet` [S] |
| Search | `.searchable` [K] | `UISearchController` [K] |
| Custom Liquid Glass | `.glassEffect(_:in:)` [S], `Glass.regular` / `Glass.clear` [S], `GlassEffectContainer` [K], `.buttonStyle(.glass/.glassProminent)` [K] | `UIGlassEffect` [K] |
| Scroll edge effect | `ScrollEdgeEffectStyle` [S] | `UIScrollEdgeEffect.Style` [S] |
| Background extension | `backgroundExtensionEffect()` [S] | `UIBackgroundExtensionView` [S] |
| Materials | `Material` (`.ultraThin` … `.thick`) [S] | `UIVisualEffectView`, `UIBlurEffect`, `UIVibrancyEffect` [S] |
| Size classes | `UserInterfaceSizeClass` [S] | `UITraitChangeObservable` [S] |
| Safe area | `SafeAreaRegions` [S], `safeAreaInsets` [S] | `safeAreaInsets` [S], `UILayoutGuide` [S] |
| Keyboard | `ToolbarItemPlacement` (keyboard) [S] | `UIKeyboardLayoutGuide` [S], `inputAccessoryView` [S] |
| iPhone Duo | `ReservedRegion` [S], `ArrangementView` [S], `ToolbarVerticalCompressionBehavior` [S] | `UIView.ReservedRegion` [S], `UIArrangementViewController` [S], `UIVerticalBarCompressionBehavior` [S] |
| Menu layout | – | `UIMenu.preferredElementSize` [S] |
| Refresh | `.refreshable` [K] | `UIRefreshControl` [S] |
| Haptics | `.sensoryFeedback` [K] | `UIFeedbackGenerator` [S] |
| Widgets | WidgetKit, `ContainerRelativeShape` [S], `padding(_:_:)` [S] | – |
| Live Activities | ActivityKit [S], `ActivityFamily.small` (CarPlay) [S], `activitySystemActionForegroundColor(_:)` [S] | – |
| Controls | `ControlWidget` [K], `IntentAuthenticationPolicy` [S] | – |
| Full screen/system gestures | `preferredScreenEdgesDeferringSystemGestures` [S] | same |
| Document launcher | `DocumentGroupLaunchScene` [S] | – |
| Review prompt | `RequestReviewAction` [S] | – |

---

## 10. Review checklist (iOS)

- [ ] Layout decisions depend on size classes, not on `idiom`/orientation/screen width (hig:layout#Size-classes)
- [ ] Tested: smallest and largest iPhone size, landscape and portrait, Display Zoom, iPhone Mirroring (hig:layout#Adaptability)
- [ ] No hard-coded safe area values; nothing obscured under the Dynamic Island/status bar/Home indicator (hig:layout#Guides-and-safe-areas)
- [ ] All tap targets ≥ 44×44 pt (minimum 28×28 pt only as an exception), sufficient spacing (hig:accessibility#Mobility)
- [ ] Dynamic Type up to AX5 without truncation/overlap; horizontal groups stack (hig:typography#Supporting-Dynamic-Type)
- [ ] No text below 11 pt; no Light/Thin weights for body text (hig:typography#Ensuring-legibility)
- [ ] Text styles instead of fixed point sizes; custom fonts support Dynamic Type + Bold Text (hig:typography)
- [ ] Tab bar for navigation only, with labels, SF Symbols, no More overflow, no disabled tabs (hig:tab-bars)
- [ ] Tab bar remains visible in all sections (except under modals) (hig:tab-bars#Best-practices)
- [ ] Navigation stack with standard Back button and swipe back; large title on top-level screens (hig:toolbars, hig:designing-for-ios)
- [ ] Exactly one prominent toolbar action, trailing; symbols without borders (hig:toolbars#Actions)
- [ ] No custom bar background colors/fake blurs; scroll edge effect automatic (hig:toolbars, hig:scroll-views#Scroll-edge-effects)
- [ ] Liquid Glass not in the content layer; custom glass used sparingly; clear only over media, with 35 % dimming if needed (hig:materials#Liquid-Glass)
- [ ] Color on glass only for primary action/status, on the background rather than the symbol (hig:color#Liquid-Glass-color)
- [ ] Sheets: Cancel leading, Done trailing; grabber when resizable; swipe to dismiss with data-loss protection (hig:sheets#iOS-iPadOS)
- [ ] No stacked sheet, never two alerts at the same time (hig:sheets, hig:modality)
- [ ] Popovers only in regular width; sheet in compact (hig:popovers#iOS-iPadOS)
- [ ] Choices related to an action = action sheet, not an alert; action sheets do not scroll (hig:action-sheets#iOS-iPadOS)
- [ ] Switches only in list rows; volume via a volume view (hig:toggles#iOS-iPadOS, hig:sliders#iOS-iPadOS)
- [ ] Destructive menu items at the end and marked as destructive; primary role never destructive (hig:context-menus, hig:buttons#Role)
- [ ] Light/Dark/Increased Contrast checked; system or semantic colors (hig:color, hig:dark-mode#iOS-iPadOS)
- [ ] System gestures (edge swipe, Home indicator, three-finger undo) not overridden (hig:gestures, hig:undo-and-redo#iOS-iPadOS)
- [ ] Status bar not permanently hidden; content beneath it covered legibly (hig:status-bars)
- [ ] Launch screen ≈ first screen, without text/logo; state is restored (hig:launching)
- [ ] App icon: 1024×1024 px, unmasked layers, dark/clear/tinted checked (hig:app-icons)
- [ ] Widgets: 16 pt margins, text ≥ 11 pt, deep link, Always-On/StandBy/tinted checked (hig:widgets)
- [ ] Live Activity: compact as one unit, limited width 28 pt, Lock Screen margin 14 pt, ends immediately (hig:live-activities)
- [ ] Notifications without sensitive data, badge only for unread items (hig:notifications)
- [ ] iPhone Duo (if supported): vertical bars not overridden, reserved regions kept clear, all toolbar items with title + symbol (hig:designing-for-iphone-duo)

---

## 11. Common mistakes ("web port smell")

- **Hamburger menu/drawer** instead of a tab bar for top-level navigation (hig:tab-bars).
- **Actions in the tab bar** (e.g., a "+" tab that opens a form) (hig:tab-bars#Best-practices).
- **Custom top bar** as a `div`-like, opaque color bar with a logo instead of a navigation bar with a title; app name as the title (hig:toolbars#Titles, hig:toolbars#Best-practices).
- **Text button "Back"** or a home-made back arrow without swipe back (hig:toolbars#Navigation).
- **Fixed px layouts** / breakpoints by device width instead of size classes and safe areas (hig:layout).
- **Fixed font sizes** (e.g., 14 px body text), no Dynamic Type, text truncated with "…" (hig:typography).
- **Tiny tap targets** (icons 20–24 pt without hit-area padding) (hig:accessibility#Mobility).
- **Modal dialogs as a centered overlay box** with an "X" at the top right instead of a sheet with Cancel/Done; popover tiles on iPhone (hig:sheets, hig:popovers#iOS-iPadOS).
- **Toasts/snackbars** for errors instead of an alert; in-app badges as fake notifications (hig:notifications).
- **Glass overload**: Liquid Glass on cards, list cells, backgrounds; several color-tinted glass buttons (hig:materials#Liquid-Glass, hig:color#Liquid-Glass-color).
- **Opaque bar backgrounds** in the brand color instead of letting the content underneath show through (hig:toolbars#Best-practices).
- **Checkbox instead of a switch** in settings lists, or a switch floating freely in the layout (hig:toggles#iOS-iPadOS).
- **Dropdown `<select>` look** instead of a menu/picker (hig:menus, hig:pickers).
- **Pull to refresh as the only way to update** (hig:progress-indicators#iOS-iPadOS).
- **Splash screen with logo** as the launch screen (hig:launching#Launch-screens).
- **Emoji as icons** (quick actions, toolbar) instead of SF Symbols (hig:home-screen-quick-actions).
- **Hover-dependent features** (tooltips, hover menus) without a touch equivalent (hig:gestures#Best-practices).

---

## Contradictions & gaps in the mirror

- **No device table/safe area values** in `layout.md`, although the change log mentions such specifications. Device-specific dimensions only indirectly from the widget/Live Activity tables.
- **Overflow:** `toolbars.md` requires a self-created More menu on iOS and says the system adds overflow menus automatically only in macOS/iPadOS; `designing-for-iphone-duo.md`, by contrast, requires moving your own overflow menus into the system overflow (`ToolbarOverflowMenu`). For iPhone Duo the latter applies; for classic iPhones the relationship is unresolved.
- **Split view on iPhone:** `multitasking.md#iOS` mentions only Picture in Picture, whereas `designing-for-iphone-duo.md` mentions Split View multitasking on the inner display.
- **Closing sheets:** the text says Cancel leading; the detent illustrations show a round Close button at the top left. Both are leading; the form (text vs. symbol) is not clearly specified. `toolbars.md` prefers symbols (no "Close" text).
- **Detent medium** is described only as "approximately half height", without a number.
