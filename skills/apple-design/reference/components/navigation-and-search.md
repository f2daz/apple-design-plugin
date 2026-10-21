# Navigation and search – components
> Source: Apple HIG, local mirror (as of 2026-10-21). Paraphrased. Sources: `(hig:<slug>)`, `(hig:<slug>#Anchor)`.

Components for top-level navigation (Tab bar, Sidebar), for search (Search field incl. scope bar and tokens), and two macOS-specific fields (Path control, Token field). Key decision for iOS/iPadOS: tab bar first; for complex structures, tab bar with sidebar adaptation; sidebar only via `NavigationSplitView` (hig:sidebars#iOS-iPadOS).

Contents: [Tab bars](#tab-bars) · [Sidebars](#sidebars) · [Tab bar vs. Sidebar](#distinguishing-tab-bar-vs-sidebar) · [Search fields](#search-fields) · [Token fields](#token-fields) · [Path controls](#path-controls)

## Tab bars
**Purpose:** Switching between an app's top-level areas, with each area preserving its navigation state (hig:tab-bars). **Platforms:** ios, ipados, macos (per the platform line; no macOS-specific guidance), (tvos, visionos); not supported in watchOS.
**Use when:** a few, equally ranked main areas should be permanently reachable. **Don't use when:** actions on the current content are needed → Toolbar (hig:tab-bars#Best-practices); very complex information structure → Sidebar or adaptive tab bar.
**Core rules:**
- Use a tab bar only for navigation, never for actions (hig:tab-bars#Best-practices).
- Keep the tab bar visible while navigating; exception: a modal view covers it (hig:tab-bars#Best-practices).
- Keep the number of tabs small; fewer tabs are easier to navigate (hig:tab-bars#Best-practices).
- Avoid overflow – otherwise the last tab in iOS/iPadOS becomes a "More" tab whose contents are hard to discover (hig:tab-bars#Best-practices).
- Never disable or hide tabs; explain an empty area instead (hig:tab-bars#Best-practices).
- Label every tab, ideally with one word (hig:tab-bars#Best-practices).
- Use SF Symbols, preferably filled variants; they adapt to compact (icon above label) and regular (side by side) (hig:tab-bars#Best-practices).
- Badges (red oval, white number or exclamation point) only for critical information (hig:tab-bars#Best-practices).
- Make the tab label color stand out clearly from colorful content; prefer a monochrome tab bar over colorful content (hig:tab-bars#Best-practices).
**Platform considerations:**
- iOS: floats at the bottom on Liquid Glass. With an accessory (e.g., MiniPlayer), the tab bar can minimize on scroll; it returns via a tab tap or scrolling to the top. A dedicated search tab at the trailing end is possible (hig:tab-bars#iOS).
- iPadOS: sits at the top; fixed (`tabBarOnly`) or with a button to convert it into a sidebar (`sidebarAdaptable`). Prefer the tab bar; allow customization by people (hig:tab-bars#iPadOS).
- visionOS: always vertical at the leading edge, expands when looked at; symbol and short label per tab; sidebar within a tab possible, sidebar selection must not switch the tab (hig:tab-bars#visionOS).
- tvOS: highly customizable, translucent; scrolls offscreen in a single view, stays fixed in a split view; live-viewing order: Live, Recordings, Other (hig:tab-bars#tvOS).
- macOS: no additional guidance in the mirror.
**Key values:** iPadOS: for customizable tabs, a default list of five or fewer (hig:tab-bars#iPadOS). tvOS: height 68 pt, top edge 46 pt from the screen edge, not changeable (hig:tab-bars#tvOS). Icon dimensions for custom icons: not in the mirror, refers to Apple Design Resources.
**Implementation:** SwiftUI `TabView` (styles `tabBarOnly`, `sidebarAdaptable`), `TabViewCustomization`, `TabBarMinimizeBehavior`, `TabViewBottomAccessoryPlacement`; UIKit `UITabBar`/`UITabBarController` (`UITabBarController.MinimizeBehavior`, `UITab.Placement`).
**Common mistakes:**
- "Create new" tab or similar as an action instead of a toolbar button.
- Graying out/removing tabs depending on state.
- Too many tabs → More tab on iPhone.
- Badge as a marketing hint instead of for critical info.

## Sidebars
**Purpose:** Navigation at the leading edge between app areas or top-level collections (folders, playlists) (hig:sidebars). **Platforms:** ios, ipados, macos, (tvos without additional guidance, visionos); not supported in watchOS.
**Use when:** many areas or user-defined collections, enough space (requires a lot of vertical and horizontal space). **Don't use when:** space is limited or content takes priority → Tab bar (hig:sidebars); hierarchy > 2 levels → Split view with a content list (hig:sidebars#Best-practices).
**Core rules:**
- Extend visually rich content beneath the (Liquid Glass) sidebar – via horizontal scrolling or the background extension effect (hig:sidebars#Best-practices).
- Let people customize content and order where possible (hig:sidebars#Best-practices).
- Group a lot of content with disclosure controls (hig:sidebars#Best-practices).
- Use SF Symbols or custom symbols instead of bitmaps (hig:sidebars#Best-practices).
- Allow hiding (iPadOS edge swipe, macOS button or View menu "Show/Hide Sidebar"), but don't hide it by default (hig:sidebars#Best-practices).
- At most two hierarchy levels; group titles short and descriptive (hig:sidebars#Best-practices).
- Icon color = accent color (macOS: follows the system accent); fixed colors only sparingly with clear meaning (hig:sidebars#Best-practices).
**Platform considerations:**
- iOS/iPadOS: consider a tab bar first; `sidebarAdaptable` offers a sidebar↔tab bar toggle and adapts to rotation/window size. Without SwiftUI: list appearance `.sidebar` of the collection view list (hig:sidebars#iOS-iPadOS).
- macOS: row height/text/glyph size depend on sidebar size (small/medium/large, also via system setting); automatically show/hide when the window is resized; don't place anything critical at the bottom (hig:sidebars#macOS).
- visionOS: the window grows for the sidebar, hiding rarely needed; for deep hierarchies, sidebar within a tab (hig:sidebars#visionOS).
**Key values:** max. two hierarchy levels (recommendation) (hig:sidebars#Best-practices). No dimensions in the mirror.
**Implementation:** SwiftUI `NavigationSplitView` (sidebar only), `TabView` with `.sidebarAdaptable`, `List` with `.listStyle(.sidebar)`, `backgroundExtensionEffect()`; UIKit `UISplitViewController`, `UICollectionLayoutListConfiguration` (appearance `.sidebar`); AppKit `NSSplitViewController`.
**Common mistakes:**
- Sidebar on iPhone/iPad although few areas justify a tab bar.
- Three or more nested levels in the sidebar.
- Colorful icons that ignore the chosen macOS accent.
- Important actions at the bottom edge of the sidebar (macOS).

## Distinguishing tab bar vs. sidebar
| Situation | Choice | Source |
|---|---|---|
| iPhone, few main areas | Tab bar | (hig:tab-bars) |
| iPad, default | Tab bar at the top (`tabBarOnly`) | (hig:tab-bars#iPadOS) |
| iPad, many/user-defined areas | `sidebarAdaptable`: tab bar with a toggle to the sidebar; initial state selectable | (hig:tab-bars#iPadOS), (hig:sidebars#iOS-iPadOS) |
| Sidebar only, without toggling | `NavigationSplitView` / `UISplitViewController` | (hig:tab-bars#iPadOS), (hig:sidebars#iOS-iPadOS) |
| Hierarchy > 2 levels | Split view with a content list between sidebar and detail | (hig:sidebars#Best-practices) |
| macOS | Sidebar (tab bar without macOS guidance in the mirror) | (hig:sidebars#macOS) |
| visionOS, deep hierarchy | Sidebar within a tab | (hig:sidebars#visionOS) |
| watchOS | neither (both not supported) | (hig:tab-bars#Platform-considerations), (hig:sidebars#Platform-considerations) |

Note: For customizability, the mirror specifies a default tab list of at most five for iPadOS to keep compact and regular consistent (hig:tab-bars#iPadOS).

## Search fields
**Purpose:** Editable text field with a magnifying glass, Clear button, and placeholder for searching a collection of content (hig:search-fields). **Platforms:** ios, ipados, macos, watchos, (tvos: dedicated search screen; visionos without additional guidance).
**Use when:** sets of content are searched or filtered in a targeted way. **Don't use when:** it's about system-wide search → pattern "Searching" (hig:searching); fixed categories without free text → consider a scope bar/segmented control.
**Core rules:**
- Use the placeholder to explain the search scope/content type (hig:search-fields#Best-practices).
- Start searching while people type, where possible (hig:search-fields#Best-practices).
- Show suggestions: recent searches beforehand, predictions during input (hig:search-fields#Best-practices).
- Most relevant results first, categorized if appropriate (hig:search-fields#Best-practices).
- Scope bar for clearly delineated categories; choose a broad scope by default, leave narrowing to the person (hig:search-fields#Scope-bars-and-tokens).
- Tokens for frequent search terms/filters (e.g., contact, "Photos") and combine them with search suggestions so tokens are discoverable (hig:search-fields#Scope-bars-and-tokens).
- iPad/Mac: keep the search experience consistent between both platforms (hig:search-fields#iPadOS-macOS).
**Placement:**
- iOS – three locations: tab in the tab bar, toolbar (bottom or top), inline with the content (hig:search-fields#iOS).
  - Search as a tab: *standard tab* → dedicated landing page with suggestions/discovery (e.g., Apple TV); *button appearance* → separate button, keyboard immediately, then back to the previous tab – for quick, transient searching (hig:search-fields#Search-as-a-tab).
  - Toolbar: prefer the bottom if there is space (field or button, opens above the keyboard); top (navigation bar, as a button) if content at the bottom takes priority or there is no bottom toolbar (hig:search-fields#Search-in-a-toolbar).
  - Inline: when search affects only this view (e.g., library filter); place above the list, pin to the top toolbar on scroll if needed (hig:search-fields#Search-as-an-inline-field).
- iPadOS/macOS: default at the trailing end of the toolbar (especially split-view apps, results in the detail); at the top of the sidebar when the sidebar/navigation is filtered (e.g., Settings); as a dedicated sidebar or tab item for discovery areas (Music, TV). In a dedicated area, focus the field immediately – except on iPad with only a virtual keyboard. In compact windows, place search above the content list column (hig:search-fields#iPadOS-macOS).
**Platform considerations:**
- tvOS: specialized keyboard screen with freely designable results; offer suggestions and recent searches (hig:search-fields#tvOS).
- watchOS: a tap opens full-screen text input; returns only after Cancel/Search (hig:search-fields#watchOS).
**Key values:** none in the mirror.
**Implementation:** SwiftUI `.searchable(text:placement:prompt:)` (scopes/tokens: see "Scoping a search operation"); UIKit `UISearchBar`, `UISearchTextField`, `UISearchController` (tvOS); AppKit `NSSearchField`.
**Common mistakes:**
- Search at the top on iPhone although there is space at the bottom and search has priority.
- Standard tab style for quick lookup search (or button style for discovery apps).
- Automatically focusing the field on iPad so that the virtual keyboard covers the view.
- Scope bar with a narrow default scope; tokens without suggestions, therefore undiscovered.

## Token fields
**Purpose:** Text field that converts input into selectable, movable tokens (e.g., recipients in Mail) (hig:token-fields). **Platforms:** macos; not supported in iOS, iPadOS, tvOS, visionOS, watchOS.
**Use when:** multiple discrete entries (recipients, tags) are edited as units, reordered, or dragged between fields. **Don't use when:** free text without units → Text field (hig:text-fields); search filters in iOS/iPadOS → search tokens (hig:search-fields#Scope-bars-and-tokens).
**Core rules:**
- Enhance tokens with a context menu (info, editing) (hig:token-fields#Best-practices).
- Consider additional triggers for token conversion (default: comma; e.g., also Return) (hig:token-fields#Best-practices).
- Adjust the delay for suggestions – the default is immediate, which can be distracting while typing (hig:token-fields#Best-practices).
- Offer a suggestion list during input, insert the selection as a token (hig:token-fields).
**Platform considerations:** macOS only.
**Key values:** none in the mirror.
**Implementation:** AppKit `NSTokenField`. SwiftUI equivalent not named in the mirror (for search: tokens in `.searchable`).
**Common mistakes:**
- Tokens without a context menu although additional info would be useful.
- Only comma as a separator – people often expect Return.
- Suggestions that pop up immediately and disrupt input.

## Path controls
**Purpose:** Shows the file system path of a selected item (hig:path-controls). **Platforms:** macos; not supported in iOS, iPadOS, tvOS, visionOS, watchOS.
**Use when:** the location of a file/folder should be visible and navigable (e.g., Finder path bar). **Don't use when:** placement in a toolbar or status bar is planned (hig:path-controls#Best-practices).
**Styles:** *Standard* – linear list (volume, parent folders, item) with icon and name; when space is limited, middle names are hidden. *Pop up* – shows only the item, a click opens a menu with the path, editable with an additional "Choose" command. Both editable via drag and drop (hig:path-controls).
**Core rules:**
- Place in the window body, not in the window frame (toolbar/status bar) (hig:path-controls#Best-practices).
- Choose the style based on space: Standard for full visibility, Pop up for compact display (hig:path-controls).
- Make it editable if people should choose items via drag or "Choose" (hig:path-controls).
- Without a selection, show the path of the window's folder (Finder behavior) (hig:path-controls).
**Platform considerations:** macOS only.
**Key values:** none in the mirror.
**Implementation:** AppKit `NSPathControl`. No SwiftUI type in the mirror.
**Common mistakes:**
- Placing a path control in the toolbar or status bar.
- Planning a path control for iOS/iPadOS – not supported there.
- Standard style with very little space: middle names are hidden, Pop up would be clearer.

## Observations / ambiguities
- Tab bars: the platform line lists macOS, but the page contains no macOS guidance ("No additional considerations for macOS"). Whether/how a tab bar looks on the Mac is not described in the mirror; for Mac window tabs, see Tab views (hig:tab-views).
- Search fields: iOS terms were updated on 2026-06-08 ("Standard tab" vs. "Button appearance"); older sources use different names.
