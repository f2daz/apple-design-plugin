# iPadOS (iPad) – Platform reference

> Source: local HIG mirror `~/.apple-design/hig/pages/<slug>.md` (as of 2026-10-21). Sources cited as `(hig:<slug>)` or `(hig:<slug>#Anchor)`.
> Paraphrased and condensed. Numbers only where they appear in the mirror. Many rules apply to iOS and iPadOS alike – see `ios.md`; this file covers the iPad-specific points, and the shared ones only where they work differently on iPad.

---

## 1. Profile

- **Display:** large, high resolution; the app runs **full screen** or **windowed** (freely resizable windows, several at once) (hig:designing-for-ipados, hig:windows#iPadOS).
- **Ergonomics:** handheld, on a table or in a stand; viewing distance usually within about three feet. Align density and size with viewing distance and input method (hig:designing-for-ipados).
- **Input:** Multi-Touch, virtual or hardware keyboard, trackpad/mouse (pointer), Apple Pencil, voice; often combined (hig:designing-for-ipados).
- **Usage:** short actions up to hours-long productivity, creative and media sessions; several apps visible, drag and drop between apps (hig:designing-for-ipados).
- **System features:** multitasking/windows, widgets (including extra large), drag and drop, menu bar (hig:designing-for-ipados, hig:the-menu-bar#iPadOS).
- **Goal:** use the large screen for content, minimize modals and full-screen transitions, keep controls reachable but out of the way; also run seamlessly on the Mac (hig:designing-for-ipados).

---

## 2. Non-negotiable

1. **Design windows to resize fluidly.** Every width from narrow (compact) through medium widths to full must work; the app is not told which multitasking configuration was chosen (hig:multitasking#iPadOS, hig:windows#Best-practices).
2. **Layout by size class, not by device/orientation**; functionality stays the same at every size, only the visible amount changes (hig:layout#Size-classes).
3. **Do not cover window controls:** move leading toolbar items inward when window controls appear (hig:windows#iPadOS).
4. **Do not rebuild custom window frames/window controls**; in UI text say "window", not "scene" (hig:windows#Best-practices).
5. **Prefer a tab bar** (top, optionally convertible to a sidebar); sidebar only for complex structures or via `sidebarAdaptable` (hig:tab-bars#iPadOS, hig:sidebars#iOS-iPadOS).
6. **Do not hide the sidebar by default**, respect the edge swipe for showing/hiding it, max. two hierarchy levels (hig:sidebars#Best-practices).
7. **Split view: persistently highlight the current selection in every column**; navigation between columns stays logical even in narrow windows (hig:split-views).
8. **The pointer supports touch, it does not replace it**; system pointer effects (highlight/lift/hover) for standard and standard-like elements (hig:pointing-devices#iPadOS).
9. **Do not redefine standard keyboard shortcuts**; support Full Keyboard Access; no custom keyboard navigation for buttons/switches/segmented controls (hig:keyboards).
10. **All functions reachable without the menu bar** – the menu bar is usually hidden and only fully usable with a hardware keyboard (hig:the-menu-bar#iPadOS).
11. **Popovers for regular width, sheets in form/page sheet style**; automatically a sheet in compact (hig:popovers#iOS-iPadOS, hig:sheets#iOS-iPadOS).
12. **Hit targets 44×44 pt default / 28×28 pt minimum** – also with a pointer (hig:accessibility#Mobility).
13. **Liquid Glass only for the functional layer**; let content run under the sidebar/toolbar (hig:materials#Liquid-Glass, hig:sidebars#Best-practices).
14. **Apple Pencil: mark immediately, no forced mode; hover/double tap/squeeze never destructive** (hig:apple-pencil-and-scribble).
15. **Dynamic Type, Dark Mode, orientation and multitasking modes seamless** (hig:designing-for-ipados).

---

## 3. Layout & dimensions

### 3.1 Documented values

| Metric | Value | Source |
|---|---|---|
| Control size default / minimum | 44×44 pt / 28×28 pt | (hig:accessibility#Mobility) |
| Pointer hit region: padding around element with a bezel | approx. 12 pt | (hig:pointing-devices#Standard-pointers-and-effects) |
| Pointer hit region: padding without a bezel | approx. 24 pt around visible edges | (hig:pointing-devices#Standard-pointers-and-effects) |
| Text default / minimum | 17 pt / 11 pt | (hig:typography#Ensuring-legibility) |
| Toolbar title | under 15 characters | (hig:toolbars#Titles) |
| Toolbar groups | max. approx. 3 (on iPad too) | (hig:toolbars#Item-groupings) |
| Customizable tab bar: default tabs | 5 or fewer | (hig:tab-bars#iPadOS) |
| Sidebar hierarchy | max. 2 levels, otherwise split view with a content list | (hig:sidebars#Best-practices) |
| Split view columns | 2 (e.g., Mail) or 3 (e.g., Keynote) | (hig:split-views#iPadOS) |
| Drag image from | approx. 3 pt of movement | (hig:drag-and-drop#Providing-feedback) |
| App icon | 1024×1024 px, square, system mask | (hig:app-icons#Specifications) |

### 3.2 Device sizes / safe areas

**Not contained in the mirror.** `layout.md` (updated 2026-09-09) contains no device table and no safe area insets (the change log mentions earlier specifications for iPad 11", iPad Air 11"/13", iPad mini 8.3", iPad Air 10.9"). Obtain safe areas at runtime, do not hard-code them (hig:layout#Guides-and-safe-areas).

iPad screen sizes documented indirectly (portrait, pt) from the widget table, **without device mapping**: 768×1024, 744×1133, 810×1080, 820×1180, 834×1112, 834×1194, 1024×1366; with Display Zoom "More Space": 954×1373, 970×1389, 1192×1590 (hig:widgets#Specifications).

### 3.3 Size classes on iPad
(hig:layout#Size-classes)
- Windows can appear in **any** combination of compact/regular in width and height (narrow-short, narrow-tall, wide-short, wide-tall).
- Do not design only for landscape iPhone (regular width/compact height) or portrait compact; use the vertical space in regular height.
- With more space: tab bar → sidebar, expand overflow items. The idiom stays the same → the layout remains recognizably iPad-like.
- Very wide/flat and narrow/tall windows: extend background artwork beyond the "standard" crop (hig:layout#Adaptability).
- Test with Device Hub among others, especially the smallest and largest windows (hig:layout#Adaptability).

### 3.4 Visual hierarchy
- Important items at the top/leading; elevate content, keep controls out of the way (hig:layout#Visual-hierarchy, hig:designing-for-ipados).
- Full-bleed backgrounds under the sidebar, toolbar, tab bar; optionally the background extension effect under the sidebar/inspector (hig:layout#Visual-hierarchy).

---

## 4. Navigation & structure

### 4.1 Decision matrix

| Situation | Pattern | Source |
|---|---|---|
| Few main sections | **Tab bar at the top** (fixed, `tabBarOnly`) | (hig:tab-bars#iPadOS) |
| Many sections, more complex app | **Tab bar, convertible to a sidebar** (`sidebarAdaptable`), customizable | (hig:tab-bars#iPadOS, hig:sidebars#iOS-iPadOS) |
| Sidebar only, without switching | **NavigationSplitView / UISplitViewController** | (hig:sidebars#iOS-iPadOS, hig:tab-bars#iPadOS) |
| Hierarchy > 2 levels | **Split view** with 2–3 columns (sidebar – list – detail) | (hig:sidebars#Best-practices, hig:split-views#iPadOS) |
| Main sections + full width for content | **Tab bar + toolbar in the same row at the top** | (hig:toolbars#iPadOS) |
| Narrowly scoped subtask | **Sheet** (form/page sheet) | (hig:sheets#iOS-iPadOS) |
| Contextual options for an element (regular) | **Popover** | (hig:popovers#iOS-iPadOS) |
| Self-contained task alongside the context | **new window** (e.g., Mail compose) | (hig:windows#Best-practices, hig:modality) |
| Create a new object "in empty space" | **Context menu** (long press / secondary click) | (hig:context-menus#iOS-iPadOS) |
| Option selection in a popover/modal for a list item | **Pop-up button** instead of a disclosure drill-down | (hig:pop-up-buttons#iPadOS) |

### 4.2 Tab bar (iPadOS)
(hig:tab-bars, hig:tab-bars#iPadOS)
- Sits at the **top**; either fixed or with a button to convert it into a sidebar.
- **Make it customizable** when there are many sections (e.g., the user pins a playlist as a tab); default ≤ 5 tabs for continuity between compact and regular.
- In regular: icon and label side by side; in compact: icon above label.
- General rules as on iOS: navigation only, keep visible, do not disable, labels, badges sparingly.
- In the menu bar: each tab as an item in the View menu, optionally with a keyboard shortcut (hig:the-menu-bar#iPadOS).

### 4.3 Sidebar
(hig:sidebars)
- Leading, floats in the Liquid Glass layer; let content scroll underneath or use the background extension effect.
- Content customizable by the user; groups with disclosure controls; SF Symbols or custom symbols instead of bitmaps.
- Icons in the accent color; fixed colors only sparingly and with meaning (e.g., VIP yellow).
- Two levels with concise group titles; deeper → split view with a content list.
- Hide via the system edge swipe; not hidden by default.
- Without SwiftUI: `UICollectionLayoutListConfiguration.Appearance.sidebar` (hig:sidebars#iOS-iPadOS).
- Search at the top of the sidebar if it filters the sidebar (Settings pattern) (hig:search-fields#iPadOS-macOS).

### 4.4 Split view
(hig:split-views)
- 2 or 3 vertical columns; keep the selection in each column visible; drag and drop between columns.
- Run through **narrow, medium, wide window widths** – columns must collapse and remain logically navigable.
- A separate scroll edge effect per column, keep heights consistent (hig:scroll-views#Scroll-edge-effects).

### 4.5 Toolbar (iPadOS)
(hig:toolbars)
- Toolbar and tab bar can share the same row at the top.
- **The system creates the overflow menu automatically**, do not build it manually; avoid layouts that overflow by default. Center items collapse into the overflow when shrinking; trailing items always stay visible; leading items are not customizable.
- Offer **toolbar customization** with many items or long sessions.
- Leading: Back, sidebar toggle, title, document menu (Duplicate, Rename, Move, Export). Trailing: inspector buttons, search, More, primary action.
- Window controls appear in windowed mode at the leading edge of the toolbar → indent leading buttons (hig:windows#iPadOS).
- Title: meaningful per window so multiple windows can be told apart; not the app name (hig:toolbars#Titles).

### 4.6 Windows & multitasking
(hig:windows#iPadOS, hig:multitasking#iPadOS)
- **Full screen:** windows fill the screen, switching via the app switcher. **Windowed:** freely resizable, several visible, movable; the system remembers size/position. System controls for tiling, full screen, minimize, close; frontmost window with colored controls and a shadow.
- Picture in Picture for video/FaceTime in both modes.
- Primary vs. auxiliary windows: auxiliary windows without app navigation, with a close button (hig:windows).
- Open new windows deliberately (compose, document), not by default; "Open in New Window" via context menu or File menu; consider pinch to open in a new window (hig:windows).
- Tip in the mirror: an app that only wants to display a file can use Quick Look, **but must support multiple windows** (hig:windows#iPadOS).
- Multitasking basics: save context, pause media/games, handle audio interruptions correctly, finish background tasks, use notifications sparingly (hig:multitasking#Best-practices).

### 4.7 Sheets & modality (iPadOS)
- Prefer a **page or form sheet** (default size, centered, dimmed background) (hig:sheets#iOS-iPadOS).
- Buttons as on iOS: Cancel leading, Done trailing; multi-step with Back (hig:sheets#iOS-iPadOS).
- Nonmodal sheets are possible when the parent is being edited (hig:sheets#Anatomy).
- Minimize modals; prefer windows for parallel tasks (hig:designing-for-ipados, hig:modality).
- Dark Mode: foreground modals automatically use *elevated* backgrounds, also to separate windows/apps (hig:dark-mode#iOS-iPadOS).

### 4.8 Search (iPadOS)
(hig:search-fields#iPadOS-macOS)
- Default: search field **trailing in the toolbar** (split view apps such as Mail, Notes).
- At the top of the sidebar if the search filters the sidebar.
- A dedicated section (sidebar item/tab) when search is combined with discovery (Music, TV); focus the field there immediately – **unless** only the virtual keyboard is available.
- The field scales with the window; in compact, place it above the content list.
- Keep it consistent with the Mac version.

---

## 5. Component specifics (platform considerations iPadOS)

### 5.1 Pointer (trackpad/mouse)
(hig:pointing-devices#iPadOS)
- The pointer is an addition to touch. Default shape is a circle; I-beam over text automatically.
- **Content effects:** *highlight* (small elements with a transparent background; default for bar buttons, tab bars, segmented controls, edit menus), *lift* (small elements with an opaque background; app icons, Control Center buttons), *hover* (large elements; define scale/tint/shadow yourself).
- **Magnetism** with highlight/lift and text areas, not with hover.
- Hit regions: approx. 12 pt padding with a bezel, approx. 24 pt without; adjacent bar buttons with **gapless** hit regions.
- With lift on non-standard-shaped elements, specify the corner radius.
- Implement band selection (dragging across multiple items) yourself in custom views.
- Distinguish pointer vs. finger only when it adds value (e.g., precise scrubbing).
- No decorative pointer effects, no instructional text at the pointer; annotations with real benefit (e.g., X/Y values) are fine.
- Hover effects: scale only with space around it; never a shadow without scaling; table rows only tint.
- Pointer accessories: simple images, transitions for state changes (e.g., `plus` → `circle.slash`).

### 5.2 Keyboard & focus
- Focus system with **focus groups**: Tab moves between groups (sidebar, grid, list), arrow keys within a group; order leading→trailing, top→bottom (hig:focus-and-selection#iPadOS).
- Focus indicator: halo (focus ring, customizable via `UIFocusHaloEffect`) or highlight in the accent color; primary item via priority (hig:focus-and-selection#iPadOS).
- Keyboard navigation in text fields, text views, sidebars, collections; **not** for buttons, segmented controls, switches – use Full Keyboard Access for those (hig:keyboards).
- Respect standard shortcuts; custom ones only for frequent commands; modifier order Control, Option, Shift, Command; no Shift for characters that already require Shift (hig:keyboards#Custom-keyboard-shortcuts).
- On drop, check the Option key (forces a copy) (hig:drag-and-drop#Accepting-drops).

### 5.3 Menu bar (iPadOS)
(hig:the-menu-bar#iPadOS)
- Appears when the pointer moves to the top edge or on a swipe down from the top; occupies the height of the status bar; centered; no menu bar extras, no Apple menu; app menu without About/Services; window controls in the menu bar when the app runs full screen.
- Not a catch-all for functions that cannot be placed elsewhere; dynamic menu items always reachable another way too.
- *App > Settings* opens the app's page in iPadOS Settings; put your own settings in a separate item below it.
- Use submenus more often than on the Mac (menu rows are taller on iPad).

### 5.4 Apple Pencil & Scribble
(hig:apple-pencil-and-scribble)
- Mark immediately, without tool selection or mode; controls also operable with Pencil.
- Use tilt, pressure, azimuth, barrel roll for expression; direct, immediate feedback.
- Left- and right-handed users: controls not under the hand; movable if needed.
- **Hover:** preview only (stroke size/color), never trigger an action; preview only for Pencil, not the pointer.
- **Double tap:** respect the user setting (default: tool ↔ eraser); never modify content.
- **Squeeze:** a single discrete action, UI near the Pencil tip, nondestructive/undoable.
- **Barrel roll:** only modify stroke behavior, no navigation.
- **Scribble:** works in standard text components (not password fields); do not move the field while writing, no autoscroll, no distracting autocompletion, enough writing space.
- PencilKit: the tool picker has undo/redo only in regular; in compact provide your own undo/redo buttons.

### 5.5 Other components

| Component | iPad-specific rule | Source |
|---|---|---|
| Context menu | Long press or secondary click; good for creating new objects in empty space | (hig:context-menus#iOS-iPadOS) |
| Edit menu | vertical style with keyboard/pointer, horizontal with touch – check both | (hig:edit-menus#iOS-iPadOS) |
| Drag and drop | several simultaneous drags; add items during a drag (flocking), accept multiple drops; spring loading | (hig:drag-and-drop#iOS-iPadOS, hig:drag-and-drop) |
| Page control | The pointer can select individual indicators | (hig:page-controls#iOS-iPadOS) |
| Pop-up button | in a popover/modal instead of disclosure for small sets of options | (hig:pop-up-buttons#iPadOS) |
| Popover | only in regular width | (hig:popovers#iOS-iPadOS) |
| Gestures | Four-finger swipe = app switching (system, do not assign); three-finger undo/copy as on iOS | (hig:gestures#iOS-iPadOS) |
| Menus | small/medium/large layout as on iOS | (hig:menus#iOS-iPadOS) |
| Toolbars | Customization by the user, system overflow | (hig:toolbars) |
| Files | Document launcher (iPadOS 18 and later); File Provider extension without its own top toolbar | (hig:file-management#iOS-iPadOS) |
| SharePlay | Continue playing shared video in Picture in Picture | (hig:shareplay#iOS-iPadOS-macOS) |
| Other shared rules | Action sheets, alerts, toggles, sliders, text fields, pickers, refresh, haptics → see `ios.md` section 5 | |

---

## 6. Liquid Glass & materials

- Liquid Glass = functional layer (tab bar, toolbar, **sidebar**); standard materials (ultraThin, thin, regular, thick) for the content layer (hig:materials, hig:materials#iOS-iPadOS).
- The **sidebar** is a larger glass element → appears more opaque for legibility; tab bar/toolbar switch light/dark automatically with monochrome symbols (hig:color#Liquid-Glass-color).
- Let content run under the sidebar and toolbar; mirror image backgrounds with the **background extension effect** (hig:sidebars#Best-practices, hig:layout#Visual-hierarchy).
- Regular variant for text-rich elements (sidebars, popovers, alerts); clear only over media, 35 % dimming over bright content (hig:materials#Liquid-Glass).
- Scroll edge effect: in split views **one per column**, align heights; prefer automatic (hig:scroll-views#Scroll-edge-effects).
- No custom toolbar backgrounds/tints; one prominent action with a tinted background (hig:toolbars#Best-practices, hig:color#Liquid-Glass-color).
- Vibrancy: labels label…quaternaryLabel (quaternary not on thin/ultraThin), fills, separator (hig:materials#iOS-iPadOS).
- Custom components in bars: concentric corner radii (hig:toolbars#Best-practices).
- App icon layered with glass effects, variants default/dark/clear/tinted (hig:app-icons).

---

## 7. Typography & Dynamic Type

- SF Pro and New York; default 17 pt, minimum 11 pt; Dynamic Type with the same tables as iOS (`typography.md` lists "iOS, iPadOS" together) (hig:typography#iOS-iPadOS, hig:typography#Specifications).
- Greater viewing distance (up to approx. three feet) → choose size and density deliberately, do not simply scale up iPhone dimensions (hig:designing-for-ipados).
- At large text sizes, reduce the number of columns (multi-column layouts are more common on iPad) (hig:typography#Supporting-Dynamic-Type).
- Do not scale everything: e.g., tab titles do not need to grow, content does (hig:typography#Conveying-hierarchy).

### Default "Large" (pt)
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

Size progression xSmall–AX5: see `ios.md` section 7.2 (identical source).

---

## 8. System integration

### 8.1 Widgets
(hig:widgets)
- Home Screen / Today View: small, medium, large, **extra large**; Lock Screen: small (system) as well as accessory circular, rectangular, inline.
- iPad Lock Screen: monochrome **without** tint.
- Home Screen: light, dark, clear, tinted.
- iPadOS renders widgets large and then scales them down → design for the canvas size (hig:widgets#Choosing-margins-and-padding).
- Margins 16 pt (tight 11 pt), text ≥ 11 pt, animations ≤ 2 s, deep links, no app-like layouts.
- Extra large not as an inflated smaller size – only with real added value (hig:widgets#Best-practices).

**Widget sizes iPad (pt; canvas = design, device = display)** (hig:widgets#Specifications)

| Screen (portrait) | Target | Small | Medium | Large | Extra large |
|---|---|---|---|---|---|
| 768×1024 | Canvas | 141×141 | 305.5×141 | 305.5×305.5 | 634.5×305.5 |
|  | Device | 120×120 | 260×120 | 260×260 | 540×260 |
| 744×1133 | Canvas | 141×141 | 305.5×141 | 305.5×305.5 | 634.5×305.5 |
|  | Device | 120×120 | 260×120 | 260×260 | 540×260 |
| 810×1080 | Canvas | 146×146 | 320.5×146 | 320.5×320.5 | 669×320.5 |
|  | Device | 124×124 | 272×124 | 272×272 | 568×272 |
| 820×1180 | Canvas | 155×155 | 342×155 | 342×342 | 715.5×342 |
|  | Device | 136×136 | 300×136 | 300×300 | 628×300 |
| 834×1112 | Canvas | 150×150 | 327.5×150 | 327.5×327.5 | 682×327.5 |
|  | Device | 132×132 | 288×132 | 288×288 | 600×288 |
| 834×1194 | Canvas | 155×155 | 342×155 | 342×342 | 715.5×342 |
|  | Device | 136×136 | 300×136 | 300×300 | 628×300 |
| 954×1373 * | Canvas/Device | 162×162 | 350×162 | 350×350 | 726×350 |
| 970×1389 * | Canvas/Device | 162×162 | 350×162 | 350×350 | 726×350 |
| 1024×1366 | Canvas | 170×170 | 378.5×170 | 378.5×378.5 | 795×378.5 |
|  | Device | 160×160 | 356×160 | 356×356 | 748×356 |
| 1192×1590 * | Canvas/Device | 188×188 | 412×188 | 412×412 | 860×412 |

\* Display Zoom "More Space".

### 8.2 Live Activities
(hig:live-activities)
- On iPad: **Lock Screen and Home Screen**; Dynamic Island and StandBy are iPhone-only.
- Rules as on iOS: beginning/end, max. approx. 8 h, no advertising, no sensitive data, Lock Screen margin 14 pt, ends immediately (visible on the Lock Screen for up to 4 h).

**Lock Screen dimensions iPad (pt)** (hig:live-activities#Specifications)

| Screen (per mirror "portrait") | Lock Screen (width × height) |
|---|---|
| 1366×1024 | 500 × 84–160 |
| 1194×834 | 425 × 84–160 |
| 1012×834 | 425 × 84–160 |
| 1080×810 | 425 × 84–160 |
| 1024×768 | 425 × 84–160 |

### 8.3 Controls, App Shortcuts, notifications, quick actions
- Controls for Control Center and the Lock Screen (the Action button is iPhone-specific): self-explanatory symbol, state animation, redaction while locked, authentication for security actions (hig:controls).
- Order App Shortcuts by importance in Spotlight and the Shortcuts app (hig:app-shortcuts#iOS-iPadOS).
- Notifications: concise, no duplicates, no sensitive data; badge only for unread items (hig:notifications).
- Home Screen quick actions: max. 4 (hig:home-screen-quick-actions).
- Keyboard shortcuts and the menu bar as system integration for power users (hig:the-menu-bar#iPadOS).

---

## 9. Implementation: SwiftUI / UIKit

Legend: **[S]** = API referenced in the mirror; **[K]** = common API, framework knowledge, not documented in the mirror – verify before use.

| Pattern | SwiftUI | UIKit |
|---|---|---|
| Tab bar at the top, fixed | `TabView` + `.tabViewStyle(.tabBarOnly)` – `tabBarOnly` [S] | `UITabBarController` [K] |
| Tab bar ↔ sidebar | `sidebarAdaptable` [S] | `UITab.Placement` [S] |
| Tab customization | `TabViewCustomization` [S] | `UITab.Placement` [S] |
| Sidebar only / split view | `NavigationSplitView` [S] | `UISplitViewController` [S], `UICollectionLayoutListConfiguration.Appearance.sidebar` [S] |
| Toolbar | `.toolbar`, `ToolbarItem` [K], `ToolbarItemGroup` [S], customization via `.toolbar(id:)` [K] | `UIToolbar` [S], `UIBarButtonItem` [S] |
| Sheet styles | `.sheet` [S], `.presentationSizing(.form/.page)` [K] | `UIModalPresentationStyle` (`.formSheet`, `.pageSheet`) [S] |
| Popover | `.popover` [K] | `UIPopoverPresentationController` [K] |
| Windows | `WindowGroup` [K], `OpenWindowAction` [S] | `UIWindowScene.ActivationInteraction` [S], `collectionView(_:sceneActivationConfigurationForItemAt:point:)` [S] |
| Quick Look in its own window | – | `QLPreviewSceneActivationConfiguration` [S] |
| Pointer effects | `.hoverEffect(.highlight/.lift)` [K] | `UIPointerInteraction` [K], `UIPointerShape.roundedRect(_:radius:)` [S], `UIPointerAccessory` [S] |
| Band selection | – | `UIBandSelectionInteraction` [S] |
| Focus | `.focusable`, `.focusSection` [K] | `focusGroupIdentifier` [S], `UIFocusGroupPriority` [S], `UIFocusHaloEffect` [S] |
| Keyboard shortcuts / menu bar | `.keyboardShortcut` [K], `.commands { CommandMenu }` [K] | `UIKeyCommand` [K], `UIMenuBuilder` [K] |
| Background extension | `backgroundExtensionEffect()` [S] | `UIBackgroundExtensionView` [S] |
| Custom Liquid Glass | `.glassEffect(_:in:)` [S], `Glass.regular/.clear` [S] | `UIGlassEffect` [K] |
| Scroll edge effect | `ScrollEdgeEffectStyle` [S] | `UIScrollEdgeEffect.Style` [S] |
| Size classes | `UserInterfaceSizeClass` [S] | `UITraitChangeObservable` [S] |
| Pencil | PencilKit [K] | `UIPencilInteraction` [K] |
| Widgets / Live Activities | WidgetKit, ActivityKit [S], `ContainerRelativeShape` [S] | – |

---

## 10. Review checklist (iPadOS)

- [ ] App works in full screen **and** windowed; smallest and largest window size tested (hig:windows#iPadOS, hig:layout#Adaptability)
- [ ] All size class combinations (compact/regular × compact/regular) sensible; no decisions based on `idiom`/orientation (hig:layout#Size-classes)
- [ ] Medium window widths: split view collapses logically, navigation between columns possible (hig:split-views#iPadOS)
- [ ] Same functionality at every size; only visibility varies (hig:layout#Size-classes)
- [ ] Leading toolbar items are not covered by window controls (hig:windows#iPadOS)
- [ ] No custom window frames/controls; "window" instead of "scene" in the UI (hig:windows#Best-practices)
- [ ] Multiple windows supported; new windows only deliberately (context menu / File menu) (hig:windows)
- [ ] Tab bar at the top or `sidebarAdaptable`; default ≤ 5 tabs when customizable (hig:tab-bars#iPadOS)
- [ ] Sidebar: not hidden by default, max. 2 levels, SF Symbols, edge swipe works (hig:sidebars)
- [ ] Selection persistently highlighted in every split view column (hig:split-views#Best-practices)
- [ ] No manual overflow menu; toolbar does not overflow in its normal state; customizable if appropriate (hig:toolbars)
- [ ] One prominent action trailing; max. approx. 3 toolbar groups (hig:toolbars)
- [ ] Sheets as form/page sheet; popovers only in regular, otherwise a sheet (hig:sheets#iOS-iPadOS, hig:popovers#iOS-iPadOS)
- [ ] Modals minimized; parallel tasks preferably as windows (hig:designing-for-ipados)
- [ ] Pointer: standard effects active; custom buttons with highlight/lift; gapless hit regions in bars; padding 12/24 pt (hig:pointing-devices#iPadOS)
- [ ] No decorative pointer effects, no instructional text at the pointer (hig:pointing-devices#Customizing-pointers)
- [ ] Hit targets ≥ 44×44 pt for touch too, even when a pointer is present (hig:accessibility#Mobility)
- [ ] Keyboard: standard shortcuts unchanged, Tab/arrow focus sensible in lists/sidebars/grids; Full Keyboard Access tested (hig:keyboards, hig:focus-and-selection#iPadOS)
- [ ] Menu bar: all functions also reachable in the UI; Settings item correct; tabs in the View menu (hig:the-menu-bar#iPadOS)
- [ ] Context menus via long press **and** secondary click; edit menu checked horizontally and vertically (hig:context-menus#iOS-iPadOS, hig:edit-menus#iOS-iPadOS)
- [ ] Drag and drop: between columns and apps, multi-item, undo, Option copy (hig:drag-and-drop)
- [ ] Apple Pencil (if relevant): immediate marking, hover only for preview, double tap/squeeze not destructive, Scribble in text fields without jumping (hig:apple-pencil-and-scribble)
- [ ] Liquid Glass only in bars/sidebar; content runs under the sidebar/toolbar; one scroll edge effect per column (hig:materials, hig:scroll-views#Scroll-edge-effects)
- [ ] Dynamic Type including AX sizes; columns reduced at large sizes (hig:typography#Supporting-Dynamic-Type)
- [ ] Dark Mode with base/elevated system backgrounds (hig:dark-mode#iOS-iPadOS)
- [ ] Search: trailing in the toolbar or at the top of the sidebar; do not autofocus when only the virtual keyboard is available (hig:search-fields#iPadOS-macOS)
- [ ] Widgets including extra large with real added value; Lock Screen monochrome checked (hig:widgets)
- [ ] Multitasking: context saved, media pauses, audio interruptions handled correctly (hig:multitasking#Best-practices)

---

## 11. Common mistakes ("web port" or "iPhone port smell")

- **Scaled-up iPhone app**: single-column lists across the full 13" width, huge rows, tab bar at the bottom (hig:tab-bars#iPadOS, hig:split-views).
- **Fixed breakpoints by device width** (e.g., "> 768 = tablet") instead of size classes; layout breaks at medium window widths (hig:layout#Size-classes, hig:split-views#iPadOS).
- **Functions disappear in a narrow window** instead of moving into the overflow/tab bar (hig:layout#Size-classes).
- **Custom window chrome, fake traffic lights, custom resize handles** (hig:windows#Best-practices).
- **Buttons at the far left of the toolbar** that end up under the window controls in windowed mode (hig:windows#iPadOS).
- **Hamburger drawer** instead of a sidebar/split view; sidebar closed by default (hig:sidebars).
- **Home-made "…" overflow** in the toolbar although the system provides it (hig:toolbars).
- **Full-screen modals for everything** (settings, detail views) instead of popover/sheet/window (hig:designing-for-ipados, hig:modality).
- **Hover-only interaction** (menus that open only on mouseover; tooltips as the only explanation) – the pointer does not replace touch (hig:pointing-devices#iPadOS).
- **CSS-like hover effects** (scaling on table rows, shadows without scaling) (hig:pointing-devices#Customizing-pointers).
- **Gaps between bar buttons**, the pointer snaps back to the circle (hig:pointing-devices#Standard-pointers-and-effects).
- **Custom keyboard navigation for buttons** instead of Full Keyboard Access; redefined Cmd standard shortcuts (hig:keyboards).
- **Functions only in the menu bar** (hig:the-menu-bar#iPadOS).
- **Pencil mode switch** before the first stroke; double tap deletes content (hig:apple-pencil-and-scribble).
- **Opaque brand-color sidebar** instead of Liquid Glass with content running underneath (hig:sidebars, hig:materials).

---

## Contradictions & gaps in the mirror

- **No device table/safe area values** in `layout.md` (although the change log mentions them). Screen sizes only from the widget/Live Activity tables.
- **The iPadOS Live Activity table** is labeled "portrait" but lists landscape dimensions (e.g., 1366×1024), while the widget table lists 1024×1366 as portrait. The orientation of the LA values is unclear.
- **Multitasking terms:** `layout.md` still mentions "Slide Over", `multitasking.md#iPadOS` describes only full screen vs. windowed (plus PiP). For new designs, assume the window model.
- **Tab bar vs. sidebar:** `sidebars.md` advises "consider a tab bar first", `tab-bars.md#iPadOS` "prefer a tab bar, convertible for complexity". That is consistent, but `split-views.md` and `sidebars.md` recommend a split view with a content list for hierarchies deeper than two levels. So for deep hierarchies, split view rather than tab bar.
- **Overflow:** iPadOS provides the system overflow automatically (toolbars.md); on iOS a More menu should be created manually. Handle this differently in universal apps.
- **Keyboard:** focus navigation via Tab/arrows is desired (focus-and-selection), but explicitly not for controls (keyboards) – only Full Keyboard Access there.
- **Sheet sizes** (form/page) are described in the mirror without numeric values.
