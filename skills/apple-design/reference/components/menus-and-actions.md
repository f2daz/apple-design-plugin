# Menus and actions – components

> Source: Apple HIG, local mirror (as of 2026-10-21). Paraphrased. Sources: `(hig:<slug>)`, `(hig:<slug>#Anchor)`.

Components people use to trigger actions: directly (Button, toolbar item), via expandable menus (Pop-up, Pull-down, Context, Edit, Menu bar, Dock), or system-wide (Share Sheet, Home Screen quick actions). Basic rule across all of them: menu commands are shortcuts – every function must also be reachable in the main UI or the menu bar (hig:context-menus#Best-practices) (hig:toolbars#macOS).

Contents: [Activity views](#activity-views) · [Buttons](#buttons) · [Context menus](#context-menus) · [Dock menus](#dock-menus) · [Edit menus](#edit-menus) · [Home Screen quick actions](#home-screen-quick-actions) · [Menus](#menus) · [Ornaments](#ornaments) · [Pop-up buttons](#pop-up-buttons) · [Pull-down buttons](#pull-down-buttons) · [The menu bar](#the-menu-bar) · [Toolbars](#toolbars)

---

## Activity views

**Purpose:** System-wide "Share Sheet" that offers sharing and action activities (Message, Copy, Print, app actions) for the current context. **Platforms:** ios, ipados (visionos); not supported in macOS, tvOS, watchOS – on the Mac, use share/action extensions instead (hig:activity-views).

**Use when:** content should be shared or handed off to other apps/services; custom, app-specific actions should be added in context. **Don't use when:** you want to build a custom sharing UI parallel to the system's, or you would duplicate system actions (e.g., Print).

**Core rules:**
- Don't duplicate system actions; name a similar custom action in a clearly distinguishing way (e.g., "Print Transaction") (hig:activity-views#Best-practices).
- Represent a custom activity with an SF Symbol (hig:activity-views#Best-practices).
- Action titles short, verb-based, without company/product names (hig:activity-views#Best-practices).
- Exclude system activities that don't fit; the order of system actions cannot be changed (hig:activity-views#Best-practices).
- Open the activity view via the Share button; don't invent an alternative path (hig:activity-views#Best-practices).
- Extensions: limit interaction to a few steps, no additional modals on top of the extension (alerts excepted) (hig:activity-views#Share-and-action-extensions).
- For share extensions, prefer the system composition view; identify action extensions with the app name (hig:activity-views#Share-and-action-extensions).
- Continue long operations in the background, show status in the main app; don't notify merely to report completion (hig:activity-views#Share-and-action-extensions).

**Platform considerations:**
- iOS/iPadOS: appears as a sheet or popover depending on device/orientation (hig:activity-views).
- macOS: no activity view; share extensions via the Share button in the toolbar or a context menu, action extensions via hovering over content, a toolbar button, or a Finder Quick Action (hig:activity-views#Share-and-action-extensions).

**Key values:** Center a custom interface icon in an area of approx. 70×70 px (hig:activity-views#Best-practices).

**Implementation:** UIKit `UIActivityViewController`, `UIActivity`; Foundation App Extension Support (hig:activity-views). SwiftUI: `ShareLink` (not mentioned in the mirror).

**Common mistakes:**
- Custom "Print" item next to the system Print.
- Custom share icon/menu instead of the Share button.
- Notification only because an extension task finished.

---

## Buttons

**Purpose:** Initiates an immediate action; defined by style, content, and role. **Platforms:** ios, ipados, macos, watchos (tvos, visionos) (hig:buttons).

**Use when:** a single, immediate action is offered. **Don't use when:** a state is toggled (→ Toggle), a choice is made among options (→ Pop-up button / Segmented control), or a menu of actions should be shown (→ Pull-down button) (hig:buttons).

**Core rules:**
- Provide sufficient spacing and hit area (see key values) (hig:buttons#Best-practices).
- Always give custom buttons a pressed state (hig:buttons#Best-practices).
- Prominent style for the most likely action; at most one or two prominent buttons per view (hig:buttons#Style).
- Emphasize the preferred option through style, not size; options in a set have the same size (hig:buttons#Style).
- Don't match the button label color to colorful content backgrounds; use monochrome labels over colorful content (Liquid Glass) (hig:buttons#Style).
- Familiar actions with familiar symbols; text in title case, ideally starting with a verb ("Add to Cart") (hig:buttons#Content).
- Use roles: normal, primary (default, accent color, responds to Return), cancel, destructive (system red) (hig:buttons#Role).
- Never assign the primary role to a destructive action, even if it is the most likely one (hig:buttons#Role).

**Platform considerations:**
- iOS/iPadOS: for delayed actions, a button can show an activity indicator plus alternative label text ("Checking out…") (hig:buttons#iOS-iPadOS).
- macOS: *Push button* = standard, can be the default button; flexible-height only for tall/multiline content; title with an ellipsis if another window/view opens; consider spring loading (hig:buttons#Push-buttons). *Square (gradient) buttons*: symbols only, only in views (not toolbar/status bar), without an introductory label (hig:buttons#Square-buttons). *Help button*: system Help button, max. one per window, context-specific help topic; in dialogs with dismiss buttons in the opposite bottom corner, otherwise bottom left/right (hig:buttons#Help-buttons). *Image buttons*: only in views, label below (hig:buttons#Image-buttons).
- visionOS: shapes circle (icon only), roundedRectangle/capsule (text), capsule (icon+text); no custom hover effects; white fill with black content is reserved for the toggled state; rounded rectangle in vertical stacks, capsule in rows (hig:buttons#visionOS).
- watchOS: inline buttons always capsule; corner buttons via toolbar (Liquid Glass); primary actions full-width; equal height for buttons placed side by side/stacked (hig:buttons#watchOS).
- tvOS: no additional considerations.

**Key values:**
- Hit area at least 44×44 pt; visionOS 60×60 pt (hig:buttons#Best-practices).
- macOS image button: approx. 10 px padding between image and button edge (hig:buttons#Image-buttons).
- visionOS sizes: Mini 28 pt, Small 32 pt, Regular 44 pt, Large 52 pt, Extra large 64 pt; centers at least 60 pt apart; for button size 60 pt and above, 4 pt padding (hig:buttons#visionOS).

**Implementation:** SwiftUI `Button` (roles via `ButtonRole`, styles via `buttonStyle`, visionOS shapes via `ButtonBorderShape`); UIKit `UIButton`; AppKit `NSButton` (`BezelStyle.flexiblePush`, `.smallSquare`, `isBordered`) (hig:buttons).

**Common mistakes:**
- Multiple prominent buttons compete in one view.
- "Delete" as the default/primary button.
- Preferred option only larger instead of styled differently.
- Square/image/help buttons placed in the toolbar (macOS).

---

## Context menus

**Purpose:** Hidden menu with the most important commands directly related to an item. **Platforms:** ios, ipados, macos (tvos, visionos); not supported in watchOS (hig:context-menus).

**Use when:** frequent, object-related commands should be quickly reachable without cluttering the UI. **Don't use when:** commands are rare/advanced or would exist only there – context menus are never the only access (hig:context-menus#Best-practices).

**Core rules:**
- Only relevant, frequent commands; few items (hig:context-menus#Best-practices).
- Offer them consistently throughout the app (hig:context-menus#Best-practices).
- Make every item also available in the main UI (toolbar, menu bar) (hig:context-menus#Best-practices).
- Submenus at most one level deep (hig:context-menus#Best-practices).
- Hide unavailable items instead of dimming them (macOS exception: Cut/Copy/Paste) (hig:context-menus#Best-practices).
- Most frequent items near the point of invocation; reverse the order if needed when the menu opens upward (hig:context-menus#Best-practices).
- Don't show keyboard shortcuts; max. approx. three groups (hig:context-menus#Best-practices).
- Destructive items (iOS/iPadOS/visionOS) at the end, marked as destructive (hig:context-menus#Best-practices).
- Title only if it clarifies the effect (e.g., number of selected items); system icons for standard actions (hig:context-menus#Content).

**Platform considerations:**
- iOS/iPadOS: either a context menu or an edit menu per item, not both; iPadOS: context menu also for creating new objects in empty space; design the preview meaningfully, match the clipping path to the shape of the preview (hig:context-menus#iOS-iPadOS).
- macOS: also called *contextual menu* there (hig:context-menus#macOS).
- visionOS: consider instead of a panel/inspector; keep the menu height from exceeding the window height where possible (hig:context-menus#visionOS).

**Key values:** "no more than about three groups" (hig:context-menus#Best-practices); otherwise none.

**Implementation:** SwiftUI `contextMenu(menuItems:)`; UIKit `UIContextMenuInteraction` (+ `UIContextMenuInteractionDelegate` for preview), `UIMenuElement.Attributes.destructive`; AppKit `NSMenu.popUpContextMenu(_:with:for:)` (hig:context-menus).

**Common mistakes:**
- Functions exclusively in the context menu.
- Dimmed instead of hidden items.
- Shortcuts in the context menu.
- Context and edit menu on the same item (iOS).

---

## Dock menus

**Purpose:** Menu opened by secondary-clicking the app icon in the Dock, with system and custom items. **Platforms:** macos; not supported in iOS, iPadOS, tvOS, visionOS, watchOS (iOS/iPadOS counterpart: Home Screen quick actions) (hig:dock-menus).

**Use when:** high-value actions are useful while the app is not frontmost or has no open window (e.g., New Message, open windows). **Don't use when:** the command would not be reachable anywhere else.

**Core rules:**
- Name items concisely, order them logically (general menu rules) (hig:dock-menus#Best-practices).
- Also offer custom Dock items in the menu bar or UI (hig:dock-menus#Best-practices).
- Only valuable items: open/recently opened windows, a few actions for the background case (hig:dock-menus#Best-practices).
- No dynamic menu items (modifier variants) in the Dock menu (hig:the-menu-bar#Dynamic-menu-items).

**Platform considerations:** macOS only.

**Key values:** none in the mirror.

**Implementation:** AppKit `NSApplicationDelegate.applicationDockMenu(_:)` (hig:dock-menus).

**Common mistakes:** Dock menu as the only access to a function; overloaded Dock menu with everyday commands.

---

## Edit menus

**Purpose:** Editing commands (Copy, Paste, Select, Translate, Look Up …) for selected content in the current view. **Platforms:** ios, ipados, macos (visionos); not supported in tvOS, watchOS (hig:edit-menus).

**Use when:** text or other selectable content (images, files, contacts, locations) is edited/copied. **Don't use when:** you want to build a custom menu with the same standard commands.

**Core rules:**
- Use the system edit menu, no custom rebuild (hig:edit-menus#Best-practices).
- Open it with the familiar system gestures (touch and hold, pinch and hold, secondary click) (hig:edit-menus#Best-practices).
- Only commands that fit the context; e.g., no Copy without a selection, no Paste with an empty pasteboard (hig:edit-menus#Best-practices).
- Place custom commands next to related system commands, sparingly (hig:edit-menus#Best-practices).
- Allow copying non-editable content text, but not control labels (hig:edit-menus#Best-practices).
- Support undo/redo, since there is no confirmation (hig:edit-menus#Best-practices).
- No redundant controls for edit functions; clearly distinguish Delete vs. Cut (hig:edit-menus#Best-practices).
- Name custom commands briefly, verb-based (hig:edit-menus#Content).

**Platform considerations:**
- iOS: compact horizontal bar; chevron expands to a context menu (hig:edit-menus).
- iPadOS: touch → horizontal; keyboard/pointer → directly as a (vertical) context menu; support both styles; position adjustable (not shape/arrow) (hig:edit-menus#iOS-iPadOS).
- macOS: via the context menu and the Edit menu in the menu bar (hig:edit-menus#macOS) (hig:the-menu-bar#Edit-menu).
- visionOS: pinch and hold → horizontal bar or context menu (hig:edit-menus).

**Key values:** none in the mirror.

**Implementation:** UIKit `UIEditMenuInteraction`, standard commands via `UIResponderStandardEditActions`; AppKit `NSMenu` (hig:edit-menus).

**Common mistakes:** custom Copy/Paste buttons in addition to the edit menu; Paste despite an empty pasteboard; edit and context menu on the same item.

---

## Home Screen quick actions

**Purpose:** App-specific quick actions via touch and hold on the app icon. **Platforms:** ios, ipados; not supported in macOS, tvOS, visionOS, watchOS (hig:home-screen-quick-actions).

**Use when:** valuable entry tasks should start directly from the Home Screen (e.g., "New Message", "Directions Home"). **Don't use when:** actions change unpredictably or are trivial.

**Core rules:**
- Only compelling, high-value tasks; at least one useful action is expected (hig:home-screen-quick-actions#Best-practices).
- Change dynamic actions only in predictable ways (location, recent activity, time of day) (hig:home-screen-quick-actions#Best-practices).
- Title short, describing the result, without the app name; optional subtitle; consider localization (hig:home-screen-quick-actions#Best-practices).
- Familiar interface icon (SF Symbols); custom icons with the Quick Action Icon Template (hig:home-screen-quick-actions#Best-practices).
- No emoji instead of a symbol (monochrome + Dark Mode) (hig:home-screen-quick-actions#Best-practices).

**Platform considerations:** Icon on the left or right depending on the icon's position; title/subtitle always left-aligned in LTR (hig:home-screen-quick-actions).

**Key values:** max. 4 quick actions in total (hig:home-screen-quick-actions#Best-practices).

**Implementation:** UIKit "Add Home Screen quick actions" (`UIApplicationShortcutItem`) (hig:home-screen-quick-actions).

**Common mistakes:** app name in the title; emojis as icons; constantly changing actions.

---

## Menus

**Purpose:** Space-saving list of commands, options, or states that opens on interaction; the rules apply to all menu types. **Platforms:** ios, ipados, macos, watchos (tvos, visionos) (hig:menus).

**Use when:** several related commands/options are offered in a space-saving way. **Don't use when:** primary actions must be immediately visible (→ Button/Toolbar).

**Core rules:**
- Labels clear and concise, actions with a verb; title case; omit articles (hig:menus#Labels).
- Dim unavailable items; the menu itself remains openable even if all items are inactive (hig:menus#Labels) – exception context menus: hide (hig:context-menus#Best-practices).
- Append an ellipsis (…) when further input is needed (hig:menus#Labels).
- Icons sparingly and purposefully; within a group, all or none (hig:menus#Icons).
- Important items first, group related items (separator), keep related commands together (hig:menus#Organization).
- Limit menu length; exception: user-generated/dynamic lists (History, Bookmarks) (hig:menus#Organization).
- Submenus sparingly, one level; with more than approx. five items, a separate menu; submenu instead of indentation (hig:menus#Submenus).
- Toggled items: changing label (Show/Hide Map), with a verb if needed; checkmark for active attributes; "Plain" to reset if needed (hig:menus#Toggled-items).

**Platform considerations:**
- iOS/iPadOS: layouts *small* (row of 4 symbols without labels), *medium* (3 symbols with short labels), *large* (default, list). Medium for three important actions, small only for closely related groups (e.g., Bold/Italic/Underline/Strikethrough) (hig:menus#iOS-iPadOS).
- visionOS: small/large; menu near the content it controls; prefer breakthrough effect `subtle` (hig:menus#visionOS).
- macOS, tvOS, watchOS: no additional considerations. Games: the platform's standard interaction, legible sizes (hig:menus#In-game-menus).

**Key values:** reconsider a submenu at approx. 5 items or more (hig:menus#Submenus); iOS layouts 4 / 3 items (hig:menus#iOS-iPadOS).

**Implementation:** SwiftUI `Menu`; UIKit Menus and shortcuts (`UIMenu`, `preferredElementSize`); AppKit Menus (`NSMenu`) (hig:menus). visionOS: `presentationBreakthroughEffect(_:)` (hig:menus#visionOS).

**Common mistakes:** icons only on individual items in a group; multilevel submenus; indented items instead of a submenu; completely hidden menu when everything is inactive.

---

## Ornaments

**Purpose:** visionOS element that presents controls/info related to a window, floating parallel in front of it without obscuring the content. **Platforms:** visionos only; not supported in iOS, iPadOS, macOS, tvOS, watchOS (hig:ornaments).

**Use when:** frequently needed controls should sit at a consistent location on the window (e.g., Now Playing). **Don't use when:** a system toolbar or tab bar is sufficient – they appear as ornaments in visionOS anyway (hig:ornaments#Best-practices).

**Core rules:**
- Use for frequent controls at a fixed position (hig:ornaments#Best-practices).
- Generally keep visible; hide only for immersion (video, photo) (hig:ornaments#Best-practices).
- Use multiple ornaments sparingly, pay attention to visual balance (hig:ornaments#Best-practices).
- Width ≤ window width (hig:ornaments#Best-practices).
- Consider borderless buttons on the glass background (hover effect automatic) (hig:ornaments#Best-practices).
- System toolbars/tab bars instead of a custom ornament where possible (hig:ornaments#Best-practices).

**Platform considerations:** visionOS only.

**Key values:** none in the mirror.

**Implementation:** SwiftUI `ornament(visibility:attachmentAnchor:contentAlignment:ornament:)` (hig:ornaments).

**Common mistakes:** ornament wider than the window; custom ornament as a toolbar rebuild.

---

## Pop-up buttons

**Purpose:** Button with a menu of mutually exclusive options that shows the current selection. **Platforms:** ios, ipados, macos (visionos); not supported in tvOS, watchOS (hig:pop-up-buttons).

**Use when:** flat list of exclusive options/states, limited space, not all options need to be visible all the time. **Don't use when:** actions, multiple selection, or a submenu are needed → Pull-down button (hig:pop-up-buttons#Best-practices).

**Core rules:**
- Only for flat, exclusive option lists (hig:pop-up-buttons#Best-practices).
- Set a sensible default (hig:pop-up-buttons#Best-practices).
- Make options predictable (introductory label or descriptive button text) (hig:pop-up-buttons#Best-practices).
- Use as a compact alternative when space is limited (hig:pop-up-buttons#Best-practices).
- If needed, a "Custom" option for rare cases, possibly with explanatory text below the list (hig:pop-up-buttons#Best-practices).

**Platform considerations:**
- iPadOS: in a popover/modal view instead of a disclosure indicator for small, well-defined option sets of a list item (hig:pop-up-buttons#iPadOS).

**Key values:** none in the mirror.

**Implementation:** SwiftUI `Picker` with `MenuPickerStyle` (`.menu`); UIKit `UIButton.changesSelectionAsPrimaryAction`; AppKit `NSPopUpButton` (hig:pop-up-buttons).

**Common mistakes:** actions in the pop-up; no default; pop-up without context whose options can't be anticipated.

---

## Pull-down buttons

**Purpose:** Button whose menu shows commands/items directly related to the button's action. **Platforms:** ios, ipados, macos (visionos); not supported in tvOS, watchOS (hig:pull-down-buttons).

**Use when:** an action should be refined (Add → what to add; Sort → by which attribute; Back → where to). **Don't use when:** exclusive selection without commands (→ Pop-up button) or only 1–2 items (→ Buttons/Toggles) (hig:pull-down-buttons#Best-practices).

**Core rules:**
- Only commands that belong directly to the button's action (hig:pull-down-buttons#Best-practices).
- Don't hide all of a view's actions in one pull-down (hig:pull-down-buttons#Best-practices).
- At least three items, but not too many (hig:pull-down-buttons#Best-practices).
- Menu title only if it adds meaning (hig:pull-down-buttons#Best-practices).
- Mark destructive items (red) and require confirmation – the system shows an action sheet (iOS) or popover (iPadOS) (hig:pull-down-buttons#Best-practices).
- Icons after the label only if they add value, preferably SF Symbols (hig:pull-down-buttons#Best-practices).

**Platform considerations:**
- iOS/iPadOS: pull-down also possible via a gesture (e.g., touch and hold on a button); More button (ellipsis) for secondary actions – weigh space vs. discoverability (hig:pull-down-buttons#iOS-iPadOS).
- visionOS: avoid pull-downs in toolbars (hig:toolbars#visionOS).

**Key values:** at least 3 menu items recommended (hig:pull-down-buttons#Best-practices).

**Implementation:** SwiftUI `Menu` (the mirror names `MenuPickerStyle` here – probably a mirror/Apple inaccuracy; `MenuPickerStyle` is the pop-up case); UIKit `UIControl.showsMenuAsPrimaryAction`; AppKit `NSPopUpButton.pullsDown` (hig:pull-down-buttons).

**Common mistakes:** primary actions only in the More menu; pull-down with one item; destructive action without confirmation.

---

## The menu bar

**Purpose:** Bar at the top edge of the screen with all of the app's top-level menus. **Platforms:** macos, ipados; not supported in iOS, tvOS, visionOS, watchOS (hig:the-menu-bar).

**Use when:** Mac or iPad app – practically always; the menu bar is the complete command directory. **Don't use as:** a catch-all for functions that don't fit anywhere else (iPadOS) (hig:the-menu-bar#iPadOS).

**Order:** *AppName* · File · Edit · Format · View · app-specific menus · Window · Help; macOS additionally the Apple menu (left) and menu bar extras (right) (hig:the-menu-bar#Anatomy).

**Core rules:**
- Adopt the system menus and their order (hig:the-menu-bar#Best-practices).
- Always show the same items; disable, don't hide, what can't be performed (hig:the-menu-bar#Best-practices).
- Support standard keyboard shortcuts, custom ones only when needed (hig:the-menu-bar#Best-practices).
- Short, one-word menu titles (hig:the-menu-bar#Best-practices).
- List all custom commands in app-specific menus (even if available elsewhere); order reflects the app hierarchy, from general to specific (hig:the-menu-bar#App-specific-menus).
- Provide the View and Window menus even with minimal functionality or only one window (hig:the-menu-bar#View-menu) (hig:the-menu-bar#Window-menu).
- Never use dynamic menu items (modifier variants) as the only way; only in menu bar menus; only one modifier (hig:the-menu-bar#Dynamic-menu-items).

**Standard menus at a glance:**

| Menu | Key rules |
|---|---|
| App (hig:the-menu-bar#App-menu) | About first, alone in its group; app name short, without version number; Settings… only app-wide settings (document settings → File); custom configuration items directly after Settings; Hide/Quit with the same short name. |
| File (hig:the-menu-bar#File-menu) | Omit/rename if there are no files. New *Item* with a specific type; Open Recent without paths, newest first; autosave instead of constant Save; Duplicate instead of Save As/Export/Copy To; Export As… only for foreign formats; Page Setup only for document-specific print parameters. |
| Edit (hig:the-menu-bar#Edit-menu) | Name Undo/Redo with the target ("Undo Typing"); Delete instead of Erase/Clear; Find possibly in the File menu if it concerns files/objects; the system appends Start Dictation and Emoji & Symbols. |
| Format (hig:the-menu-bar#Format-menu) | Only for formatted text; submenus Font and Text. |
| View (hig:the-menu-bar#View-menu) | Window presentation (tab bar, toolbar, sidebar, full screen); Show/Hide titles reflect the current state; no window navigation. |
| Window (hig:the-menu-bar#Window-menu) | Always Minimize and Zoom (Full Keyboard Access); Zoom not for full screen; open windows alphabetically, no panels; consider showing/hiding panels (except Font/Color – they are in the Format menu). |
| Help (hig:the-menu-bar#Help-menu) | Far right; Help Book provides the search field automatically; separate additional items with a separator, keep them few. |

**Platform considerations:**
- iPadOS: hidden until revealed (pointer to the top edge/swipe), centered, no menu bar extras, no Apple menu, app menu without About/Services/visibility items; offer all functions in the UI as well (dynamic items only with a hardware keyboard); *AppName > Settings* opens the app's page in iPadOS Settings, in-app settings as a separate item below it; consider tabs as items in the View menu; use submenus more often (hig:the-menu-bar#iPadOS).
- macOS: Apple menu fixed; when space is limited, title spacing is reduced/truncated; hidden in full screen (hig:the-menu-bar#macOS). *Menu bar extras*: symbol (template image black/transparent), a menu on click instead of a popover, the person decides whether it is shown, don't rely on its presence, offer functions in other ways too (e.g., Dock menu) (hig:the-menu-bar#Menu-bar-extras).

**Key values:** menu bar height 24 pt (hig:the-menu-bar#Menu-bar-extras); About name ≤ 16 characters (hig:the-menu-bar#App-menu).

**Implementation:** SwiftUI `CommandMenu` (+ `CommandGroup`, `MenuBarExtra`); UIKit "Adding menus and shortcuts to the menu bar" (`UIMenuBuilder`); AppKit `NSMenu`, `NSStatusBar` (menu bar extras), `NSMenuItem.isAlternate`, `NSHelpManager` (hig:the-menu-bar). `CommandGroup`/`UIMenuBuilder` not mentioned in the mirror.

**Common mistakes:** hiding/showing items depending on context; "Save As" instead of "Duplicate"; Zoom as a full-screen toggle; menu bar extra opens a popover; functions only via modifier variants.

---

## Toolbars

**Purpose:** Bar at the top/bottom with title, navigation, search, and frequent actions for the current view. **Platforms:** ios, ipados, macos, watchos (tvos, visionos) (hig:toolbars).

**Use when:** frequent commands, navigation (Back/Close), or search for the current view. **Don't use when:** switching between the app's main areas → Tab bar (hig:toolbars).

**Core rules:**
- Choose items deliberately, avoid overcrowding; define overflow behavior, no manual overflow menu (the system does this in macOS/iPadOS) (hig:toolbars#Best-practices).
- More menu only when needed, for less important actions (hig:toolbars#Best-practices).
- Reduce custom backgrounds/tinted controls, use `ScrollEdgeEffectStyle` if needed; monochrome items over colorful content (Liquid Glass) (hig:toolbars#Best-practices).
- Use standard components (concentric corner radii) (hig:toolbars#Best-practices).
- Give every window a useful, short title, not the app name (hig:toolbars#Titles).
- Standard Back and Close buttons with system symbols, no "Back"/"Close" text label (hig:toolbars#Navigation).
- Symbols instead of text, without borders; text only where symbols are weak (e.g., Edit) (hig:toolbars#Actions).
- Exactly one primary action (Done/Submit) with the `.prominent` style at the trailing end (hig:toolbars#Actions).
- Groups: leading (Back, sidebar, title, document menu; not customizable), center (frequent controls, customizable, collapses into overflow), trailing (always visible: inspector, search, More, primary action); max. three groups (hig:toolbars#Item-groupings).
- Separate text buttons from each other and from symbol buttons with fixed spacing (hig:toolbars#Item-groupings).

**Platform considerations:**
- iOS: only the most important items, the rest in the More menu; large title that turns into the standard title on scrolling (navigation bar) (hig:toolbars#iOS).
- iPadOS: toolbar and tab bar can share the top row; consider customizability (hig:toolbars#iPadOS) (hig:toolbars#Best-practices).
- macOS: in the window frame, items without bezel; every toolbar item also as a menu bar command (hig:toolbars#macOS).
- visionOS: at the bottom of the window as an ornament; symbol or text, label appears when looked at; no vertical toolbar; window not narrower than the toolbar; no pull-downs (hig:toolbars#visionOS).
- watchOS: buttons in the top corners or at the bottom; scrolling toolbar button (`primaryAction`) for an important non-primary function (hig:toolbars#watchOS).

**Key values:** title under 15 characters; max. three groups (hig:toolbars#Titles) (hig:toolbars#Item-groupings).

**Implementation:** SwiftUI `toolbar` / `ToolbarItem` (placements `topBarLeading`, `topBarTrailing`, `bottomBar`, `primaryAction`); UIKit `UIToolbar`, `UINavigationBar.prefersLargeTitles`, `UIBarButtonItem.SystemItem.fixedSpace`; AppKit `NSToolbar` (hig:toolbars).

**Common mistakes:** app name as window title; multiple `.prominent` actions; "Back" as text; toolbar-only commands without a menu bar counterpart (macOS); tab bar navigation crammed into the toolbar.
