# macOS – Platform reference

Source: local HIG mirror (`~/.apple-design/hig/pages`, as of 2026-10-21). Sources cited as `(hig:<slug>)` or `(hig:<slug>#Anchor)`. All numbers come from the mirror; where the mirror gives no number, none is given here either.

---

## 1. Profile

- **Usage context:** stationary at a desk, viewing distance approx. 1–3 feet; sessions from a few minutes to hours of focused work; several apps open at once, frequent switching between active and inactive states (hig:designing-for-macos).
- **Input:** physical keyboard (practically always), mouse/trackpad with high precision, game controllers, Siri; trackpad gestures and Force Click (hig:designing-for-macos, hig:pointing-devices#macOS, hig:keyboards).
- **Displays:** large, high-resolution displays, additional monitors incl. iPad; some Macs have a camera housing at the top center (hig:designing-for-macos, hig:layout#macOS, hig:going-full-screen#macOS).
- **System frame:** menu bar, Dock, Finder/file management, full screen in its own Space, windows in three states (main/key/inactive) (hig:designing-for-macos, hig:windows#macOS).
- **Expectations:** more content in fewer hierarchy levels, little modality, freely resizable windows, all commands in the menu bar, keyboard shortcuts, personalization (toolbar, windows, colors, fonts) (hig:designing-for-macos).
- **No Dynamic Type** on macOS (hig:typography#macOS).

---

## 2. Non-negotiable

1. Offer every app command in the menu bar – including rarely used ones and those already in the toolbar or a context menu (hig:the-menu-bar#App-specific-menus, hig:toolbars#macOS).
2. Standard menus in standard order: app menu, File, Edit, Format, View, app-specific menus, Window, Help (hig:the-menu-bar#Anatomy).
3. Don't hide menu items when they don't currently apply – disable them (hig:the-menu-bar#Best-practices).
4. Support standard keyboard shortcuts and don't repurpose them for other actions; custom shortcuts only for the most frequent app commands, Command as the main modifier, avoid Control (hig:keyboards#Standard-keyboard-shortcuts, hig:keyboards#Custom-keyboard-shortcuts).
5. Windows freely resizable, movable, minimizable; offer full screen via the system and let people decide when to enter/exit it (hig:designing-for-macos, hig:going-full-screen#macOS).
6. Don't rebuild custom window frames/controls; preserve the system appearance of window states (key/main/inactive) (hig:windows#Best-practices, hig:windows#macOS).
7. No critical controls or information at the bottom edge of a window or sidebar – windows are often partially moved below the screen edge (hig:layout#macOS, hig:windows#macOS, hig:sidebars#macOS).
8. Open settings via *App Name > Settings…* (Command-Comma), not via a toolbar button (hig:settings#macOS).
9. Always offer a Window menu, even with only one window, with Minimize and Zoom (Full Keyboard Access) (hig:the-menu-bar#Window-menu).
10. Always offer a View menu, even if it only contains Enter/Exit Full Screen; Show/Hide titles reflect the current state (hig:the-menu-bar#View-menu).
11. Undo/Redo at the top of the Edit menu with Command-Z / Shift-Command-Z (hig:undo-and-redo#macOS).
12. Liquid Glass only in the functional layer (toolbar, sidebar, controls), never in the content area; apply sparingly to custom controls (hig:materials#Liquid-Glass).
13. A menu bar extra opens a menu, not a popover (unless the functionality is too complex for a menu); people decide whether it is shown (hig:the-menu-bar#Menu-bar-extras).
14. Don't hard-code colors for elements that depend on the user's accent color (sidebar icons, selection), unless a fixed color carries meaning (hig:sidebars#Best-practices, hig:color#App-accent-colors).
15. Support Full Keyboard Access (hig:keyboards#Best-practices).

---

## 3. Layout & dimensions

### Concrete values from the mirror

| Item | Value | Source |
|---|---|---|
| Menu bar height | 24 pt | (hig:the-menu-bar#Menu-bar-extras) |
| Default text size / minimum | 13 pt / 10 pt | (hig:typography#Ensuring-legibility) |
| Control size default / minimum | 28x28 pt / 20x20 pt | (hig:accessibility#Mobility) |
| Spacing around elements with bezel / without bezel | approx. 12 pt / approx. 24 pt | (hig:accessibility#Mobility) |
| Split view divider (thin, preferred) | 1 pt | (hig:split-views#macOS) |
| Padding image ↔ edge for image buttons | approx. 10 px | (hig:buttons#macOS) |
| Toolbar/window title | under 15 characters | (hig:toolbars#Titles) |
| Toolbar groups | aim for max. 3 | (hig:toolbars#Item-groupings) |
| Tooltip length | max. 60–75 characters | (hig:offering-help#macOS-visionOS) |
| App name in the About menu item | 16 characters or fewer | (hig:the-menu-bar#App-menu) |
| Radio buttons per group | typically 2–5; from approx. 5 options use a pop-up button | (hig:toggles#macOS) |
| Tabs in a tab view | no more than 6 | (hig:tab-views#Best-practices) |
| Stepper Shift-click | larger increments, example: 10× standard | (hig:steppers#macOS) |
| Contrast (WCAG AA) | up to 17 pt: 4.5:1; from 18 pt or bold: 3:1 | (hig:accessibility#Vision) |
| App icon layout size | 1024x1024 px, square, system masks to rounded rectangle | (hig:app-icons#Specifications) |
| Widget text size | 11 pt or larger | (hig:widgets#Displaying-text-in-widgets) |
| Widget margins | 16 pt standard, 11 pt tight; smaller on the Mac desktop (no number) | (hig:widgets#Choosing-margins-and-padding) |
| Mac Catalyst, iPad idiom | scaling to 77 %, e.g. 17 pt → 13 pt | (hig:mac-catalyst#Choose-an-idiom) |
| Document icon background | 512/256/128/32/16 px @1x (each doubled @2x) | (hig:icons#macOS) |
| Document icon center image | half the canvas size; approx. 10 % margin, motif approx. 80 % (e.g. 205x205 in 256x256) | (hig:icons#macOS) |
| Smallest document icon size | 16x16 px | (hig:icons#macOS) |

### Layout rules

- Most important content at the top and on the leading side (reading order); top-down flow, important actions at the top of the window (hig:layout#Visual-hierarchy, hig:mac-catalyst#Layout).
- Extend background content beneath the sidebar and toolbar; if a sidebar/inspector covers parts of an image, use the background extension effect (hig:layout#Visual-hierarchy, hig:sidebars#Best-practices).
- No content behind the camera housing at the top edge of the window (hig:layout#macOS).
- Split view panes: sensible min/max widths so the divider stays visible (hig:split-views#macOS).
- Columns in table/outline/column views resizable by the user (hig:lists-and-tables#macOS, hig:outline-views, hig:column-views).
- Inset a tab view with a margin from the window body on all sides (hig:tab-views#Anatomy).
- In full screen, adjust proportions, but don't resize the window programmatically (hig:going-full-screen#Best-practices).

**Gap in the mirror:** There are no default, minimum, or maximum sizes for macOS windows, no toolbar height, no sidebar widths, and no row heights (sidebar size small/medium/large only qualitative, hig:sidebars#macOS). Don't invent such values; when in doubt, use system components.

---

## 4. Navigation & structure

### Windows
- **Primary window** for main navigation and content; **auxiliary window** for a self-contained task without navigation to other areas (hig:windows).
- Open new windows deliberately (e.g. Compose in Mail), not as default behavior; offer an "Open in New Window" option via context menu or File menu (hig:windows#Best-practices).
- In UI text always say "window", never "scene" (hig:windows#Best-practices).
- States: *main* (frontmost app window), *key* (accepts input, colored window buttons), *inactive* (gray, no vibrancy) (hig:windows#macOS-window-states).
- Bottom bar only for a small amount of contextual info (e.g. Finder status bar); more info → inspector (hig:windows#macOS).

### Menu bar
- Required menus and order see section 2; details on the app, File, Edit, Format, View, Window, and Help menus in (hig:the-menu-bar).
- App menu: About first and alone in a group; Settings…; Services; Hide/Hide Others/Show All; Quit (hig:the-menu-bar#App-menu).
- App-specific menus between View and Window, ordered from general to specific, reflecting the app's hierarchy (Mail: Mailbox → Message → Format) (hig:the-menu-bar#App-specific-menus).
- Menu titles short, ideally one word; title case (hig:the-menu-bar#Best-practices).
- Ellipsis (…) for menu items that require further input (hig:menus, hig:the-menu-bar#File-menu).
- Dynamic menu items (Option variants) only in menu bar menus, only one modifier, never the only way (hig:the-menu-bar#Dynamic-menu-items).
- Prefer Duplicate over Save As/Export/Copy To; Export As only for foreign formats (hig:the-menu-bar#File-menu).

### Sidebar
- Leading side, navigation between areas/top-level collections; max. two hierarchy levels, deeper → additional content list in a split view (hig:sidebars#Best-practices).
- Can be shown/hidden via button and View menu (Show/Hide Sidebar), visible by default (hig:sidebars#Best-practices).
- Can collapse automatically when the window is made smaller (hig:sidebars#macOS).
- Search field at the top of the sidebar if it filters the sidebar (hig:search-fields#iPadOS-macOS).

### Toolbar
- In the window frame at the top, below or integrated with the title bar; items without bezel (hig:toolbars#macOS).
- Leading: back, sidebar toggle, title, document menu if applicable (not customizable). Center: frequent controls, customizable, move into system overflow. Trailing: always visible – inspector buttons, search field, More menu, primary action (hig:toolbars#Item-groupings).
- Search field at the trailing end of the toolbar for many cases (hig:search-fields#iPadOS-macOS).
- Offer toolbar customization with many items or long sessions (hig:toolbars#Best-practices).
- Don't use the app name as the window title (hig:toolbars#Titles).

### Inspector
- Shows details of the current selection and updates with it; as a panel or as a trailing split view pane; an "Info" window with fixed content, by contrast, is a regular window (hig:panels#Best-practices, hig:windows#macOS).
- Inspector next to the content instead of a popover (hig:mac-catalyst#Layout).

### Settings
- Dedicated settings window with a non-customizable, always-visible toolbar for switching panes; active pane highlighted; window title = pane name (without panes: "*App Name* Settings"); restore the most recently used pane; dim Minimize/Maximize (hig:settings#macOS).
- Document-specific options in the File menu (hig:settings#macOS).
- Only infrequent, general settings; task options where the task takes place; no copies of system-wide settings (hig:settings#Best-practices).

### Pattern selection
| Data shape | Pattern | Source |
|---|---|---|
| Flat, multi-column, sortable | Table view | (hig:lists-and-tables#macOS) |
| Hierarchical with attribute columns | Outline view (hierarchy only in column 1) | (hig:outline-views) |
| Deep hierarchy, frequent back/forward, no sorting needed | Column view (browser) | (hig:column-views) |
| Few closely related areas in the window body | Tab view (instead of segmented control) | (hig:tab-views, hig:segmented-controls#macOS) |
| Repeated input while observing results | Panel instead of sheet | (hig:sheets#macOS) |

---

## 5. Component specifics (Platform considerations)

**Buttons**
- Push button is the standard; ellipsis in the title if it opens another window/view/app; flexible-height only for two-line/tall content (hig:buttons#macOS).
- Square (gradient) buttons only in a view (e.g. +/- below a table), not in toolbar/status bar, symbol instead of text, no introductory label (hig:buttons#macOS).
- Help button: the system-provided one, max. one per window, context-specific help topic; position: dialog with OK/Cancel → bottom corner opposite the buttons; settings → bottom left or right corner; never in the toolbar (hig:buttons#macOS).
- Image buttons in a view, not in the window frame; label below (hig:buttons#macOS).
- Consider spring loading (Force Click while dragging) for buttons and segments (hig:buttons#macOS, hig:segmented-controls#macOS).

**Toggles:** switch for weighty group toggles, mini switch in grouped form rows, checkbox for hierarchies and single options (incl. mixed state), radio buttons for exclusive options; never in toolbar/status bar; don't replace existing checkboxes with switches (hig:toggles#macOS).

**Sheets:** card-like above the parent window, parent window dimmed; reasonable default size; other app windows remain usable (hig:sheets#macOS).

**Popovers:** can be detached and then become a panel with as similar an appearance as possible (hig:popovers#macOS).

**Panels:** float above windows, short noun title ("Inspector", "Fonts"); bring all panels to the front when the app activates, hide them when inactive; not in the Window menu's window list; no Minimize; prefer simple controls (slider, stepper); HUD style only for media-heavy apps, small, sparingly colored, few controls (hig:panels).

**Alerts:** app icon automatically; suppression option for repeated alerts, accessory view, help button possible; caution symbol only for a real risk of data loss (hig:alerts#macOS).

**Lists/tables/outline/column:** sort via column header (clicking again reverses), resizable columns, alternating row colors for wide tables; outline: Option-click expands recursively, remember expansion state, column headers as nouns without colon, middle ellipsis when truncating; column view: root in column 1, preview for leaf items (hig:lists-and-tables#macOS, hig:outline-views, hig:column-views).

**Split views:** vertical, horizontal, or combined; panes can be hidden, restore via toolbar button and menu command with shortcut; thin divider (hig:split-views#macOS).

**Scroll views:** scroll bars; in panels possibly small/mini, then all controls in the panel in the same size (hig:scroll-views#macOS).

**Text/input:** combo box for text + suggestion list; expansion tooltip for truncated field content; token fields; path controls only in the window body (hig:text-fields#macOS, hig:entering-data#macOS, hig:token-fields, hig:path-controls).

**Pickers / sliders / gauges:** date picker textual or graphical; slider with tick marks, linear vs. circular (for recurring values), live feedback; level indicator (capacity discrete/continuous, rating, relevance) (hig:pickers#macOS, hig:sliders#macOS, hig:gauges#macOS).

**Tooltips (help tags):** describe only the indicated control, start with a verb, don't repeat the control name, sentence case, 60–75 characters (hig:offering-help#macOS-visionOS).

**Pointer & trackpad:** use standard cursors semantically (I-beam, open/closed hand, crosshair, drag copy, operation not allowed, resize variants); secondary click = context menu; account for Force Click, smart zoom, swipe between pages (hig:pointing-devices#macOS).

**Context menus:** Mac users expect a context menu with relevant actions on every object (hig:mac-catalyst#Menus, hig:context-menus).

**Drag and drop:** export to the Finder (file or clipping), dragging from inactive windows without activating them, badge with count for multiple selection, appropriate cursors, select + drag in one motion (hig:drag-and-drop#macOS).

**Files:** standard Open/Save panels; Open button can be renamed (e.g. "Insert"); Save dialog with format choice and optional accessory view; with autosave disabled, dot in the close button and in the Window menu; remove "Edited" from the title after saving; Finder Sync extensions for sync status (hig:file-management#macOS).

**Printing:** a dedicated category in the Print panel for app-specific options; Page Setup only for document-specific page settings; advanced options behind an "Advanced Options" disclosure (hig:printing#macOS).

**Haptics:** Magic Trackpad – only alignment, level change, generic (hig:playing-haptics#macOS).

**Privacy:** Developer ID for distribution outside the Store; sandboxing (required in the Mac App Store); consider fast user switching (hig:privacy#macOS).

**Colors:** dynamic system colors (labelColor, controlAccentColor, selectedContentBackgroundColor, unemphasized variants for non-key windows, etc.) instead of fixed values (hig:color#macOS).

**Dark Mode / desktop tinting:** with the Graphite accent, window backgrounds are tinted by the desktop picture; keep custom components with a visible background slightly transparent in their neutral state, but not colored states (hig:dark-mode#macOS).

---

## 6. Liquid Glass, materials, current design system

- **Two layers:** Liquid Glass for the functional layer (toolbars, sidebars, controls) above the content; standard materials (blur, vibrancy, blending) for structure in the content area (hig:materials).
- **No Liquid Glass in the content layer**; exception: transient states of sliders/toggles while interacting (hig:materials#Liquid-Glass).
- **Variants:** *regular* (blurs, standard for system components, for text-heavy elements such as sidebars, popovers, alerts); *clear* only over visually rich media content; on a bright background, consider a 35 % dark dimming layer (hig:materials#Liquid-Glass).
- **Sidebars** float in the Liquid Glass layer on macOS; continue content beneath them (horizontal scrolling or background extension effect) (hig:sidebars#Best-practices).
- Liquid Glass is more opaque in large elements such as sidebars; in toolbars it switches between light and dark depending on the background, symbols/text monochrome (hig:color#Liquid-Glass-color).
- **Use color sparingly:** accent color on the background of the primary action (prominent), not on several controls; monochrome toolbar over colorful content (hig:color#Liquid-Glass-color, hig:toolbars#Best-practices).
- **Toolbar:** no custom backgrounds/tints; use the scroll edge effect instead; standard components are concentric with the bar corners, design custom components concentrically as well; symbols without borders; one `.prominent` action at the trailing end (hig:toolbars#Best-practices, hig:toolbars#Actions).
- **Scroll edge effect** (iOS, iPadOS, macOS): prefer the automatic one; only behind floating elements; one effect per view; in split views per pane, same height (hig:scroll-views#Scroll-edge-effects).
- **Standard materials on macOS:** choose NSVisualEffectView materials semantically, blending *behind window* vs. *within window*; use vibrancy deliberately in custom views (hig:materials#macOS).
- Inactive windows lose vibrancy – custom windows must follow the state appearance (hig:windows#macOS-window-states).
- **App icon:** layered, Liquid Glass properties (specular, refraction, translucency) applied by the system; layers in Icon Composer; square, unmasked layers; no custom shadows/glows; variants default, dark, clear light/dark, tinted light/dark (hig:app-icons).

---

## 7. Typography

- System font **SF Pro**; **no Dynamic Type** on macOS (hig:typography#macOS).
- Default 13 pt, minimum 10 pt (hig:typography#Ensuring-legibility).
- Avoid light weights (Ultralight, Thin, Light) (hig:typography#Ensuring-legibility).
- For text matching system controls, use the dynamic NSFont variants: controlContentFont, labelFont, menuFont, menuBarFont, messageFont, paletteFont, titleBarFont, toolTipsFont, userFont, userFixedPitchFont, systemFont, boldSystemFont (hig:typography#macOS).
- Don't embed system fonts; access them via Font.Design (hig:typography#Using-system-fonts).

### macOS built-in text styles (hig:typography#Specifications)

| Style | Weight | Size (pt) | Line height (pt) | Emphasized |
|---|---|---|---|---|
| Large Title | Regular | 26 | 32 | Bold |
| Title 1 | Regular | 22 | 26 | Bold |
| Title 2 | Regular | 17 | 22 | Bold |
| Title 3 | Regular | 15 | 20 | Semibold |
| Headline | Bold | 13 | 16 | Heavy |
| Body | Regular | 13 | 16 | Semibold |
| Callout | Regular | 12 | 15 | Semibold |
| Subheadline | Regular | 11 | 14 | Semibold |
| Footnote | Regular | 10 | 13 | Semibold |
| Caption 1 | Regular | 10 | 13 | Medium |
| Caption 2 | Medium | 10 | 13 | Semibold |

Point sizes based on 144 ppi for @2x designs. Tracking table for mockups: (hig:typography#Tracking-values), e.g. 12 pt → 0, 13 pt → −6/1000 em.

---

## 8. System integration

- **Menu bar extras:** symbol (SF Symbol or template icon, black/clear, system tints it); menu instead of popover; can be enabled by the user (setting, optionally offered during setup); don't rely on visibility – the system hides extras when space is limited; make functions reachable in other ways as well (hig:the-menu-bar#Menu-bar-extras).
- **Dock menu:** high-value items (open/recently used windows, actions for when the app isn't frontmost, e.g. Mail: Get New Mail, New Message); every item also available elsewhere (hig:dock-menus).
- **Full screen:** system full screen (accounts for the camera housing); entry via window button, View menu, Control-Command-F; keep the Dock reachable (except games); no auto-exit; resume state when returning (hig:going-full-screen).
- **Services:** item in the app menu (macOS only) (hig:the-menu-bar#App-menu).
- **Widgets:** on the desktop and in Notification Center; sizes small, medium, large, extra large (hig:widgets#System-family-widgets).
- **Live Activities** of a paired iPhone appear in the Mac menu bar (compact/minimal/expanded); clicking opens iPhone Mirroring; use iOS dimensions (hig:live-activities#macOS).
- **Notifications:** no macOS-specific rules; general rules: concise, no sensitive data, max. 4 actions, no action that only opens the app, badge only for unread notifications; on macOS, notification sounds mix with other audio by default (hig:notifications, hig:playing-audio#macOS).
- **App Shortcuts** are not supported on macOS, but App Intents actions are, in the Shortcuts app (hig:app-shortcuts#macOS).
- **Help:** Help menu with Help Book (automatic search field), Command-? opens the Help menu (hig:the-menu-bar#Help-menu, hig:keyboards).
- **SharePlay:** shared video continues playing in a window (hig:shareplay).

---

## 9. Implementation: SwiftUI / AppKit mapping

| Concept | SwiftUI | AppKit |
|---|---|---|
| Main window / multiple windows | `WindowGroup`, `Window`, `DocumentGroup`, `openWindow` (OpenWindowAction) | `NSWindow`, `NSWindowController` |
| Menu bar commands | `.commands { CommandMenu(...) ; CommandGroup(...) }`, `.keyboardShortcut(...)` | `NSMenu`, `NSMenuItem` (alternates: `isAlternate`) |
| Settings window | `Settings { ... }` scene (opens via Command-Comma) | custom window with toolbar panes |
| Menu bar extra | `MenuBarExtra` | `NSStatusBar` / `NSStatusItem` |
| Sidebar + detail | `NavigationSplitView` | `NSSplitViewController` with sidebar item |
| Inspector | `.inspector(isPresented:)` | trailing split view item / panel |
| Split view (free) | `HSplitView`, `VSplitView` | `NSSplitView` (`dividerStyle` thin) |
| Table | `Table` (sortable, multi-column) | `NSTableView` |
| Outline | `List(children:)` / `OutlineGroup`, `Table` with children | `NSOutlineView` |
| Column view | – (no direct SwiftUI equivalent known) | `NSBrowser` |
| Toolbar | `.toolbar { ToolbarItem(placement:) }`, `.toolbarRole`, customization via `id`-based items | `NSToolbar` (customizable) |
| Search | `.searchable(...)` | `NSSearchField` / `NSSearchToolbarItem` |
| Tooltip | `.help("...")` | `toolTip` |
| Context menu | `.contextMenu { }` | `menu(for:)` |
| Popover / sheet | `.popover`, `.sheet` | `NSPopover` (detachable), `beginSheet` |
| Panel / HUD | – | `NSPanel`, style `hudWindow` |
| Full screen | system behavior of `WindowGroup` | `toggleFullScreen(_:)` |
| Dock menu | – | `applicationDockMenu(_:)` in the app delegate |
| Liquid Glass custom controls | `.glassEffect()`; background mirroring `.backgroundExtensionEffect()`; `.scrollEdgeEffectStyle(...)` | `NSGlassEffectView`, `NSBackgroundExtensionView` |
| Materials | `.background(.regularMaterial)` etc. | `NSVisualEffectView` (Material, BlendingMode) |
| Dynamic system colors | `Color(nsColor: .labelColor)` and similar | `NSColor.labelColor`, `.controlAccentColor` … |
| Trackpad haptics | – | `NSHapticFeedbackPerformer` |

Note: Linked in the mirror and therefore sourced are MenuBarExtra, NSStatusBar, CommandMenu, VSplitView/HSplitView, NSSplitView.DividerStyle, NSVisualEffectView (Material/BlendingMode), backgroundExtensionEffect(), ScrollEdgeEffectStyle, toggleFullScreen(_:), NSHapticFeedbackPerformer, help(_:), OpenWindowAction, hudWindow, NSDatePicker, NSTabView, isAlternate. All other mappings (incl. `.inspector`, `Table`, `Settings`, `NSBrowser`, `applicationDockMenu(_:)`, `glassEffect`, `NSGlassEffectView`) are standard API without a source in the mirror – verify against the current developer documentation before using them in code.

---

## 10. Review checklist

**Menu bar & keyboard**
- [ ] Menus present and in standard order: App, File, Edit, (Format), View, app-specific, Window, Help (hig:the-menu-bar#Anatomy)
- [ ] Every toolbar action and every context menu command also available as a menu command (hig:toolbars#macOS)
- [ ] Inapplicable menu items disabled instead of hidden (hig:the-menu-bar#Best-practices)
- [ ] About first with separator; Settings… in the app menu; Quit/Hide with short app name (hig:the-menu-bar#App-menu)
- [ ] View menu with state-dependent Show/Hide titles and Enter/Exit Full Screen (hig:the-menu-bar#View-menu)
- [ ] Window menu with Minimize, Zoom, Bring All to Front; panels not in the window list (hig:the-menu-bar#Window-menu, hig:panels)
- [ ] Standard shortcuts work (Cmd-N/O/S/W/Q/Z/C/V/X/A/F/P/Comma/?) and are not repurposed (hig:keyboards#Standard-keyboard-shortcuts)
- [ ] Custom shortcuts sparing, Command-based, without Control, modifier order Control-Option-Shift-Command (hig:keyboards#Custom-keyboard-shortcuts)
- [ ] Full Keyboard Access: all controls reachable via keyboard (hig:keyboards#Best-practices)
- [ ] Menu items requiring further input end in "…" (hig:menus)

**Windows & layout**
- [ ] Windows freely resizable; layout doesn't break at small and large sizes (hig:windows#Best-practices)
- [ ] System full screen supported, not forced; Dock reachable (hig:going-full-screen)
- [ ] No custom window frames/buttons; key/main/inactive visibly distinguishable (hig:windows#macOS)
- [ ] Nothing critical at the bottom edge of the window/sidebar (hig:layout#macOS)
- [ ] Window title meaningful, not the app name, under 15 characters (hig:toolbars#Titles)
- [ ] Default text 13 pt, nothing below 10 pt; contrast 4.5:1 or 3:1 (hig:typography, hig:accessibility)
- [ ] Controls at least 20x20 pt, default 28x28 pt (hig:accessibility#Mobility)

**Navigation & components**
- [ ] Sidebar max. two levels, can be shown/hidden (button + View menu), visible by default (hig:sidebars)
- [ ] Sidebar icons follow the system accent color, fixed colors only when meaningful (hig:sidebars#Best-practices)
- [ ] Toolbar: max. three groups, symbols without borders, one prominent action trailing, search trailing, customizable with many items (hig:toolbars)
- [ ] No switches/checkboxes/square/image/help buttons/path controls in the window frame (hig:toggles#macOS, hig:buttons#macOS, hig:path-controls)
- [ ] Tables: sortable column headers, resizable columns; hierarchical data in an outline view (hig:lists-and-tables#macOS)
- [ ] Settings window: non-customizable toolbar, active pane highlighted, title = pane, last pane restored, Minimize/Zoom dimmed (hig:settings#macOS)
- [ ] Sheets keep other app windows usable; repeated input in a panel instead of a sheet (hig:sheets#macOS)
- [ ] Tooltips for icon-only controls, ≤ 60–75 characters (hig:offering-help#macOS-visionOS)
- [ ] Context menu on all relevant objects (hig:mac-catalyst#Menus)

**Material & system**
- [ ] Liquid Glass only in the functional layer, not in content; no custom toolbar backgrounds (hig:materials#Liquid-Glass, hig:toolbars)
- [ ] Content continues beneath sidebar/toolbar or uses the background extension effect (hig:layout#Visual-hierarchy)
- [ ] Dynamic system colors, Light/Dark/Increased Contrast tested (hig:color)
- [ ] Menu bar extra (if present): template symbol, menu, optional, functions also in Dock menu/app (hig:the-menu-bar#Menu-bar-extras)
- [ ] App icon from Icon Composer, square unmasked layers, Dark/Clear/Tinted checked (hig:app-icons)
- [ ] Autosave status signaled correctly (dot in the close button only with autosave disabled) (hig:file-management#macOS)

---

## 11. Common mistakes / anti-patterns

- **iPad/iPhone port without Mac adaptation:** tab bar at the bottom, buttons at side/bottom edges, popover instead of inspector, actions only in the UI instead of the menu. On the Mac: sidebar or segmented control instead of tab bar, top-level areas additionally in the View menu, controls in the window toolbar, Next/Previous in addition to swipe (hig:mac-catalyst#Navigation, hig:mac-catalyst#Layout).
- **Missing menu commands/shortcuts:** commands only in toolbar or context menu – the toolbar can be hidden/customized, so it is never the only place (hig:toolbars#macOS).
- **Settings gear in the toolbar** instead of app menu + Command-Comma (hig:settings#macOS).
- **Custom window chrome** or rebuilt traffic-light buttons (hig:windows#Best-practices).
- **Critical actions in the bottom bar** (hig:windows#macOS).
- **Repurposed standard shortcuts** or new shortcuts created by adding a modifier to unrelated commands (Shift-Cmd-Z for something other than Redo) (hig:keyboards#Custom-keyboard-shortcuts).
- **Menu bar extra opens a popover** or is installed without asking (hig:the-menu-bar#Menu-bar-extras).
- **Liquid Glass in content** or on many custom controls; several color-tinted toolbar buttons (hig:materials#Liquid-Glass, hig:color#Liquid-Glass-color).
- **Segmented control for switching views in the main area** instead of a tab view (hig:segmented-controls#macOS).
- **Missing hover/pointer feedback**, wrong cursors (e.g. pointing hand without a link) (hig:pointing-devices#Pointers).
- **Automatic full screen** or a custom window-mode menu; zoom button misused for full screen (hig:going-full-screen#macOS, hig:the-menu-bar#Window-menu).
- **Panels in the Window menu's document list** or with Minimize enabled (hig:panels).
- **"Save As"/"Export" instead of "Duplicate"** for simple copies (hig:the-menu-bar#File-menu).
- **Touch dimensions adopted unchanged** (44-pt targets, large spacing) – results in unnecessarily low information density on the Mac; the Mac default for controls is 28x28 pt, large displays should show more content in fewer levels (hig:accessibility#Mobility, hig:designing-for-macos).

---

## Contradictions and ambiguities in the mirror

- **Hit targets:** (hig:buttons#Best-practices) generally specifies at least 44x44 pt, (hig:accessibility#Mobility) for macOS 28x28 pt default and 20x20 pt minimum. For Mac controls, the platform-specific table applies; the 44-pt rule is touch-oriented.
- **App icon:** (hig:mac-catalyst#App-icons, as of 2023) requires a separate macOS version in the "lifelike rendering style"; (hig:app-icons, as of 2026) treats iOS/iPadOS/macOS uniformly (square, Icon Composer, Liquid Glass) and names no macOS specifics. The more recent page (app-icons) takes precedence. Likewise, app-icons speaks of the "Home Screen" for appearance variants, although macOS is included.
- **Settings:** (hig:mac-catalyst) lists "app-specific settings in the System Settings app" as a Catalyst feature; (hig:settings#macOS) describes a dedicated settings window via the app menu. For native Mac apps, use the dedicated window.
- **Widget rendering:** (hig:widgets#Appearances) says accented rendering applies to system-family widgets "on all platforms"; the adjacent table lists "Accented: Not supported" for Mac.
- **Tab views:** "no more than six tabs" and in the same paragraph "if you need six or more tabs" (hig:tab-views#Best-practices).
- **Keyboard shortcut table:** Command-I appears twice (Italic and Info window), F12 "Dashboard" (feature no longer exists in current macOS) (hig:keyboards#Standard-keyboard-shortcuts). Resolve by context, ignore Dashboard.
- **New York:** (hig:typography#macOS) names NY only for Mac Catalyst apps, the general developer note refers to `Font.Design.serif` across platforms. When in doubt, verify availability in native Mac apps.
- **Larger text:** macOS has no Dynamic Type, yet (hig:accessibility#Vision) recommends enlargement to at least 200 % – on the Mac, therefore, via custom UI (e.g. a font size setting, zoom commands).
- **Settings window:** the HIG speaks of a "maximize button"; on macOS the element is called the zoom button (hig:settings#macOS).
- **No window dimensions:** Neither default nor minimum sizes for Mac windows are contained in the mirror.
