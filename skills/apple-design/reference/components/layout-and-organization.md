# Layout and organization – components
> Source: Apple HIG, local mirror (as of 2026-10-21). Paraphrased. Sources: `(hig:<slug>)`, `(hig:<slug>#Anchor)`.

Components for grouping, structuring, and navigating content: from simple containers (Box, Label) through data-driven views (List/Table, Collection, Outline, Column) to structural containers (Split view, Tab view). Several of them are defined only for macOS (Column, Outline, Tab view) or only for tvOS (Lockups) (hig:layout-and-organization).

Contents: [Boxes](#boxes) · [Collections](#collections) · [Column views](#column-views) · [Disclosure controls](#disclosure-controls) · [Labels](#labels) · [Lists and tables](#lists-and-tables) · [Lockups](#lockups) · [Outline views](#outline-views) · [Split views](#split-views) · [Tab views](#tab-views)

---

## Boxes
**Purpose:** Visually separates a group of logically related content and controls with a border or background, optionally with a title. **Platforms:** ios, ipados, macos (visionos); not supported in tvOS, watchOS.

**Use when:** a manageable subarea of a view should be recognizable as belonging together (e.g., an option group in Settings). **Don't use when:** the box fills almost the entire container or subgroups would be created through nested boxes.

**Core rules:**
- Keep the box clearly smaller than the surrounding view – as it approaches window/screen size, it loses its separating effect (hig:boxes#Best-practices).
- Structure content inside a box with padding and alignment instead of nested boxes (hig:boxes#Best-practices).
- Add a brief title if it clarifies the relationship; it also helps VoiceOver users anticipate the content (hig:boxes#Content).
- Phrase the title as a short descriptive phrase in sentence-style capitalization, without ending punctuation – exception: in a settings pane, the title ends with a colon (hig:boxes#Content).

**Platform considerations:**
- iOS/iPadOS: secondary or tertiary background color by default (hig:boxes#iOS-iPadOS).
- macOS: the title appears above the box by default (hig:boxes#macOS).

**Key values:** none in the mirror.
**Implementation:** SwiftUI `GroupBox`; AppKit `NSBox`.
**Common mistakes:**
- Box-in-box nesting for subgroups → busy, cramped.
- Box spanning (almost) the entire window area.
- Title with a period or in title case (outside of settings panes also with a colon).

---

## Collections
**Purpose:** Presents an ordered set of content in a customizable, highly visual layout (row or grid), ideal for image-based content. **Platforms:** ios, ipados, macos (tvos, visionos); not supported in watchOS.

**Use when:** primarily images/visual items or items of widely varying size are shown. **Don't use when:** mostly text is displayed → List/Table (hig:collections#Best-practices).

**Core rules:**
- Use the standard row or grid layout where possible; avoid flashy custom layouts (hig:collections#Best-practices).
- Prefer a table/list for text (hig:collections#Best-practices).
- Make items easy to select; give images enough padding so focus/hover effects remain visible and nothing overlaps (hig:collections#Best-practices).
- Add custom gestures only when needed; standard: tap = select, touch and hold = edit, swipe = scroll (hig:collections#Best-practices).
- Provide feedback through animation when inserting, deleting, or reordering (standard or custom animation) (hig:collections#Best-practices).

**Platform considerations:**
- iOS/iPadOS: use dynamic layout changes with care, keep them comprehensible, and avoid changing during interaction unless in response to an explicit action (hig:collections#iOS-iPadOS).
- macOS, tvOS, visionOS: no additional considerations.

**Key values:** none in the mirror.
**Implementation:** UIKit `UICollectionView`; AppKit `NSCollectionView`. SwiftUI: no type named in the mirror (commonly `LazyVGrid`/`LazyHGrid` – not sourced from the mirror).
**Common mistakes:**
- Text-heavy content in a grid instead of a list.
- Too little spacing → focus/hover effects overlap neighbors.
- Layout jumps without user action.

---

## Column views
**Purpose:** Navigation through a data hierarchy via a series of vertical columns (also *browser*), one level per column. **Platforms:** macos; not supported in iOS, iPadOS, tvOS, visionOS, watchOS.

**Use when:** there is a deep hierarchy in which people frequently jump back and forth between levels, and no sorting as in List/Table is needed (example: Finder column view) (hig:column-views#Best-practices). **Don't use when:** sorting by columns is needed (→ Table/Outline view) or on iPadOS/visionOS – use a Split view there (hig:column-views).

**Core rules:**
- Show the root level in the first column (hig:column-views#Best-practices).
- Show info/preview for the selected item when it has no children (like Finder: preview, date, type, size) (hig:column-views#Best-practices).
- Let people resize columns, especially for long item names (hig:column-views#Best-practices).
- Mark parent items that have children with a triangle symbol (default behavior) (hig:column-views).

**Platform considerations:** macOS only.
**Key values:** none in the mirror.
**Implementation:** AppKit `NSBrowser`. SwiftUI/UIKit: no type in the mirror.
**Common mistakes:**
- Empty last column for leaf items instead of detail information.
- Fixed column widths → truncated names.
- Use for flat data that needs sorting.

---

## Disclosure controls
**Purpose:** Reveals and hides information and functionality related to a control or a view. **Platforms:** ios, ipados, macos (visionos); not supported in tvOS, watchOS.

Two variants:
- **Disclosure triangle:** points inward from the leading edge when content is hidden, down when it is visible; for views/lists (e.g., advanced export options, Finder list hierarchy) (hig:disclosure-controls#Disclosure-triangles).
- **Disclosure button:** points down when content is hidden, up when it is visible; expands the functionality of a specific control (e.g., Save sheet in macOS) (hig:disclosure-controls#Disclosure-buttons).

**Use when:** details/advanced options are only relevant on demand (progressive disclosure). **Don't use when:** the content is constantly needed for the main task.

**Core rules:**
- Hide details until they become relevant; frequently used controls stay visible at the top, advanced items are collapsed by default (hig:disclosure-controls#Best-practices).
- Label disclosure triangles descriptively so it is clear what is revealed/hidden (e.g., "Advanced Options") (hig:disclosure-controls#Disclosure-triangles).
- Place a disclosure button near the content it controls (hig:disclosure-controls#Disclosure-buttons).
- Use at most one disclosure button per view (hig:disclosure-controls#Disclosure-buttons).

**Platform considerations:**
- iOS, iPadOS, visionOS: available via SwiftUI `DisclosureGroup` (hig:disclosure-controls#iOS-iPadOS-visionOS).
- macOS: no additional considerations.

**Key values:** none in the mirror.
**Implementation:** SwiftUI `DisclosureGroup`; AppKit `NSButton.BezelStyle.disclosure` (triangle) and `NSButton.BezelStyle.pushDisclosure` (button).
**Common mistakes:**
- Unlabeled triangle, content not predictable.
- Multiple disclosure buttons in one view.
- Important default options hidden behind disclosure.

---

## Labels
**Purpose:** Static, non-editable (often copyable) text in buttons, menu items, lists, and views. **Platforms:** ios, ipados, macos, watchos (tvos, visionos).

**Use when:** a small amount of text is displayed that doesn't need to be edited. **Don't use when:** text should be editable (short → Text field) or a lot of text is displayed/optionally edited (→ Text view) (hig:labels#Best-practices).

**Core rules:**
- Use labels only for short, non-editable text (hig:labels#Best-practices).
- Prefer system fonts; labels support Dynamic Type by default (where available) – ensure legibility with custom fonts/styles (hig:labels#Best-practices).
- Convey levels of importance with the four system label colors instead of custom grays (hig:labels#Best-practices):
  - Label – primary information (`label` / `labelColor`)
  - Secondary label – subheading, supplementary text (`secondaryLabel` / `secondaryLabelColor`)
  - Tertiary label – unavailable item/behavior (`tertiaryLabel` / `tertiaryLabelColor`)
  - Quaternary label – watermark (`quaternaryLabel` / `quaternaryLabelColor`)
- Make useful text selectable/copyable (error message, location, IP address) (hig:labels#Best-practices).

**Platform considerations:**
- macOS: non-editable text via `NSTextField` with `isEditable = false` (hig:labels#macOS).
- watchOS: system text components for date/time and countdown/count-up timers; configurable (formats, calendars, time zones), automatically adapt to the available space and update without app involvement; recommended for complications (hig:labels#watchOS).
- iOS, iPadOS, tvOS, visionOS: no additional considerations.

**Key values:** 4 system label colors (hig:labels#Best-practices).
**Implementation:** SwiftUI `Label`, `Text`; UIKit `UILabel`; AppKit `NSTextField`.
**Common mistakes:**
- Hard-coded grays instead of semantic label colors (breaks Dark Mode/contrast).
- Error messages/IDs not copyable.
- Label misused for editable text.
- Custom font without Dynamic Type support.

---

## Lists and tables
**Purpose:** Present data in rows across one or more columns, grouped or hierarchical, with selecting, adding, deleting, and reordering. **Platforms:** ios, ipados, macos, watchos (tvos, visionos).

**Use when:** text should be easy to scan, information hierarchies are navigated (iOS Settings), options are chosen, or multicolumn, sortable data (productivity) is present. **Don't use when:** items vary widely in size or many images are shown → Collection (hig:lists-and-tables#Best-practices); hierarchical data on macOS → Outline view (hig:lists-and-tables#macOS).

**Core rules:**
- Prefer presenting text in lists/tables (hig:lists-and-tables#Best-practices).
- Allow editing where it makes sense – at least reordering is appreciated; iOS/iPadOS: selecting rows only in edit mode (hig:lists-and-tables#Best-practices).
- Provide appropriate selection feedback: navigation lists keep the selection persistently highlighted; option lists highlight briefly and then, e.g., add a checkmark (hig:lists-and-tables#Best-practices).
- Keep row text brief; for long content, list only titles and show details in a detail view (hig:lists-and-tables#Content).
- Consider middle truncation in narrow tables to keep the beginning and end recognizable (hig:lists-and-tables#Content).
- Name columns with nouns/short noun phrases in title case without ending punctuation; single-column table without a header → provide context via a label/header (hig:lists-and-tables#Content).
- Choose a list/table style that fits the data and platform (iOS grouped, watchOS elliptical, macOS bordered with alternating rows) (hig:lists-and-tables#Style).
- Use built-in row styles (e.g., `UIListContentConfiguration`) (hig:lists-and-tables#Style).

**Platform considerations:**
- iOS, iPadOS, visionOS: Info button (in a row: *detail disclosure button*) only for additional info, not for navigation – use a disclosure indicator for drill-down. No index (alphabet strip) in tables with controls at the trailing edge, as accidental taps are likely (hig:lists-and-tables#iOS-iPadOS-visionOS).
- macOS: sort by clicking the column header, clicking again reverses the direction; column widths resizable; consider alternating row colors in multicolumn tables; hierarchy → Outline view (hig:lists-and-tables#macOS).
- tvOS: the focused row is highlighted, slightly enlarged, possibly with rounded corners – check adjacent images for this, no custom rounding masks (hig:lists-and-tables#tvOS).
- watchOS: limit the number of rows where possible, but make expected long lists fully accessible (most relevant first + "more"); keep detail views short so vertical page-based navigation works – scrolling details prevent it (hig:lists-and-tables#watchOS).

**Key values:** none in the mirror.
**Implementation:** SwiftUI `List`, `Table` (Tables), `ListStyle`; UIKit `UITableView`, `UIListContentConfiguration`, `UITableViewCell.AccessoryType.disclosureIndicator`; AppKit `NSTableView`.
**Common mistakes:**
- Detail disclosure button (Info) for navigation instead of a disclosure indicator.
- Alphabet index plus disclosure indicators at the same edge.
- Overly long rows with lots of body text.
- Navigation list without persistent selection highlighting (iPad/Mac split view).

---

## Lockups
**Purpose:** Combines a content view, header, and footer into one interactive unit that grows together on focus. **Platforms:** tvos only; not supported in iOS, iPadOS, macOS, visionOS, watchOS. Relevant to this plugin's focus only as a reference.

Types: Cards (ratings/reviews), Caption buttons (image or text with title/subtitle), Monograms (people, round image or initials), Posters (image, title/subtitle visible only on focus) (hig:lockups).

**Core rules:**
- Leave enough space between lockups, as they enlarge on focus (hig:lockups#Best-practices).
- Keep sizes consistent within a row/group (hig:lockups#Best-practices).
- Let caption buttons tilt with the swipe direction on focus (arranged vertically: up/down; horizontally: left/right; grid: both) (hig:lockups#Caption-buttons).
- For monograms, prefer images over initials (hig:lockups#Monograms).
- Choose a poster size that fits the content (hig:lockups#Posters).

**Platform considerations:** tvOS only.
**Key values:** 4 lockup types (hig:lockups).
**Implementation:** TVUIKit `TVLockupView`, `TVLockupHeaderFooterView`, `TVCardView`, `TVCaptionButtonView`, `TVMonogramContentView`, `TVPosterView`.
**Common mistakes:**
- Arrangement too tight → focused lockup overlaps neighbors.
- Mixed sizes in a row.

---

## Outline views
**Purpose:** Hierarchical data as a scrolling list organized in columns and rows, with disclosure triangles for parent containers. **Platforms:** macos; not supported in iOS, iPadOS, tvOS, visionOS, watchOS.

**Use when:** text-based hierarchical data (e.g., the file system in Finder) is shown, often in the leading pane of a split view (hig:outline-views#Best-practices). **Don't use when:** data is not hierarchical → Table (hig:outline-views#Best-practices).

**Core rules:**
- Show the hierarchy only in the first column; other columns contain attributes (hig:outline-views#Best-practices).
- Always provide column headers in multicolumn outline views (nouns, title case, no punctuation, especially no colon); single-column without a header → establish context another way (hig:outline-views#Best-practices).
- Allow sorting by column header; sorting by the primary column applies per hierarchy level, clicking again reverses (hig:outline-views#Best-practices).
- Let people adjust column widths (hig:outline-views#Best-practices).
- Make expanding/collapsing easy; Option-click on the triangle expands all sublevels (Finder convention) (hig:outline-views#Best-practices).
- Remember the expansion state and restore it next time (hig:outline-views#Best-practices).
- Allow editing where it makes sense: single click edits a cell, double click can respond differently (e.g., open a file) (hig:outline-views#Best-practices).
- Truncate cell text with a middle ellipsis instead of clipping; consider alternating row colors and a search field in the toolbar for long lists (hig:outline-views#Best-practices).

**Platform considerations:** macOS only.
**Key values:** none in the mirror.
**Implementation:** SwiftUI `OutlineGroup`; AppKit `NSOutlineView`.
**Common mistakes:**
- Hierarchy indentation in multiple columns.
- Expansion state lost on relaunch.
- Missing column headers in a multicolumn view.

---

## Split views
**Purpose:** Manages multiple adjacent panes (primary, secondary, optionally tertiary), typically to show multiple hierarchy levels at the same time, often with a sidebar. **Platforms:** ios, ipados, macos, watchos (tvos, visionos).

**Use when:** hierarchy navigation with a detail view (Mail), supplementary functional areas around a main area (Keynote: navigator, notes, inspector), or in visionOS additional info without a new window is shown. **Don't use when:** compact environment (iPhone portrait) – content would wrap/be truncated (hig:split-views#iOS).

**Core rules:**
- Persistently highlight the current selection in every pane that leads to the detail view (hig:split-views#Best-practices).
- Consider drag and drop between panes (hig:split-views#Best-practices).
- iOS: prefer using split views in a regular, not compact, size class (hig:split-views#iOS).
- iPadOS: plan for narrow, compact, and intermediate window widths; navigation between panes must remain logical at every width (hig:split-views#iPadOS).
- macOS: set sensible min/max pane sizes so the divider stays visible (hig:split-views#macOS).
- macOS: let people hide panes and offer multiple ways to restore them (toolbar button, menu command with keyboard shortcut) (hig:split-views#macOS).
- macOS: prefer the thin divider; thicker only for a concrete need (e.g., strong lines in adjacent tables) (hig:split-views#macOS).

**Platform considerations:**
- iOS: recommended only in a regular environment (hig:split-views#iOS).
- iPadOS: two (Mail) or three (Keynote) vertical panes; windows freely resizable → account for multiple widths (hig:split-views#iPadOS).
- macOS: panes vertical, horizontal, or combined; divider draggable (`VSplitView`/`HSplitView`) (hig:split-views#macOS).
- tvOS: good for filtering (category on the left, results on the right); one shared title above the split view, no pane titles; title alignment: centered for a collection in the secondary pane, above the primary pane for single content (hig:split-views#tvOS).
- visionOS: for additional info, a split view instead of a new window; short required task → Sheet (hig:split-views#visionOS).
- watchOS: shows list or detail each in full screen; at launch, show the most relevant detail view (location, time, recent actions); multiple detail pages as a vertical tab view (Digital Crown, page indicator) (hig:split-views#watchOS).

**Key values:**
- macOS thin divider: 1 pt wide (hig:split-views#macOS).
- tvOS default split: primary pane 1/3, secondary pane 2/3 of the screen width; alternatively 1/2 to 1/2 (hig:split-views#tvOS).
- iPadOS: 2 or 3 vertical panes (hig:split-views#iPadOS).

**Implementation:** SwiftUI `NavigationSplitView` (macOS additionally `VSplitView`, `HSplitView`); UIKit `UISplitViewController`; AppKit `NSSplitViewController`, `NSSplitView.DividerStyle`.
**Common mistakes:**
- Forcing a split view on iPhone portrait.
- Selection in the primary pane not highlighted → orientation is lost.
- Pane can be dragged to zero width, the divider "disappears".
- Hidden pane restorable only via a single, hidden path.

---

## Tab views
**Purpose:** Multiple mutually exclusive content areas in the same area, switchable via a tab control. **Platforms:** macos, watchos; not supported in iOS, iPadOS, tvOS, visionOS. Distinction: not to be confused with the tab bar (app navigation) (hig:tab-bars).

**Use when:** closely related content areas (e.g., settings groups in a window) are shown. **Don't use when:** on iOS/iPadOS → Segmented control (hig:tab-views#iOS-iPadOS); very many panes → pop-up button menu (hig:tab-views#Best-practices).

**Core rules:**
- Group only closely related content in tabs (hig:tab-views#Best-practices).
- Controls in a pane affect only that pane; panes are self-contained (hig:tab-views#Best-practices).
- Label tabs with nouns/short noun phrases (rarely verbs) in title case (hig:tab-views#Best-practices).
- Don't switch between tabs with a pop-up button (two clicks instead of one, options not visible) – except when there are too many panes (hig:tab-views#Best-practices).
- Limit the number of tabs (see key values) (hig:tab-views#Best-practices).
- Inset the tab view with a margin from the window body; extending to the window edges is unusual (hig:tab-views#Anatomy).
- The tab control sits at the top edge; hide it only for programmatic switching – content is then borderless (solid/transparent), bezeled, or outlined with a line (hig:tab-views#Anatomy).

**Platform considerations:**
- iOS/iPadOS: not supported; Segmented control as a replacement (hig:tab-views#iOS-iPadOS).
- watchOS: tab views are displayed with page controls (SwiftUI `TabView`) (hig:tab-views#watchOS).

**Key values:** max. 6 tabs. **Ambiguity in the mirror:** The section says "no more than six" on the one hand and to consider alternatives "with six or more" on the other – when in doubt, ≤ 5–6, and from 6 on, consider an alternative (hig:tab-views#Best-practices).
**Implementation:** SwiftUI `TabView`; AppKit `NSTabView`.
**Common mistakes:**
- Controls in a tab that change content in other tabs.
- Too many tabs instead of a pop-up button.
- Tab view rebuilt on iOS instead of a Segmented control.
- Confusion with the tab bar for app-wide navigation.
