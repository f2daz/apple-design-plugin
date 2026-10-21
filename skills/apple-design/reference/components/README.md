# Component catalog (Apple HIG)

> Source: Apple HIG, local mirror `~/.apple-design/hig/pages/<slug>.md` (as of 2026-10-21). Paraphrased. Sources: `(hig:<slug>)`, `(hig:<slug>#Anchor)`, Anchor = heading with hyphens, without commas.
> Focus: iOS, iPadOS, macOS, watchOS. tvOS and visionOS are mentioned only where relevant.

The components are split across eight files following the HIG subgroups. Each component has these sections: Purpose · Platforms · Use/Don't use · Core rules · Platform considerations · Key values · Implementation · Common mistakes.

## Decision aid: I want X, so I use Y

### Choosing from a few options
| Situation | Component | Source |
|---|---|---|
| A few (iPhone approx. 5, wide UI approx. 5–7) closely related options, selection should stay visible | Segmented control (not on watchOS) | (hig:segmented-controls#Best-practices) |
| Short list of mutually exclusive options, limited space, current selection visible in the button | Pop-up button (SwiftUI `Picker` with menu style) | (hig:pop-up-buttons#Best-practices), (hig:pickers#Best-practices) |
| Commands or actions that refine an action (Add, Sort) | Pull-down button or Menu | (hig:pull-down-buttons#Best-practices) |
| Medium to long, logically ordered list of values, date or time | Picker / Date picker | (hig:pickers#Best-practices) |
| Very long list | List/Table, with an index if needed | (hig:pickers#Best-practices) |
| macOS, 2–5 mutually exclusive options, all visible | Radio buttons; above approx. 5, Pop-up button | (hig:toggles#Radio-buttons) |
| Switching between separate app areas | Tab bar, not Segmented control | (hig:segmented-controls#iOS-iPadOS) |

### On/off and values
| Situation | Component | Source |
|---|---|---|
| iOS/iPadOS on/off in a list | Switch (`Toggle`) | (hig:toggles#iOS-iPadOS) |
| iOS/iPadOS on/off outside a list | Button with toggle behavior | (hig:toggles#iOS-iPadOS) |
| macOS: single setting / emphasized or group-controlling setting | Checkbox or Switch | (hig:toggles#Checkboxes), (hig:toggles#Switches) |
| Continuous value within a range | Slider | (hig:sliders#Best-practices) |
| Small incremental change | Stepper, plus a Text field for large jumps | (hig:steppers#Best-practices) |
| Display a value relative to a scale (not input) | Gauge | (hig:gauges) |
| Progress of an ongoing operation | Progress indicator | (hig:progress-indicators) |

### Confirmation and prompting
| Situation | Component | Source |
|---|---|---|
| Unexpected problem, critical info, rare irreversible data destruction | Alert (`alert`) | (hig:alerts#Best-practices) |
| Options for an action the person deliberately initiated (Delete/Save) | Action sheet, in SwiftUI `confirmationDialog` | (hig:action-sheets#Best-practices) |
| Options the person opens themselves | Menu, not an Action sheet | (hig:action-sheets#iOS-iPadOS) |
| Frequent, undoable action | no confirmation; offer Undo instead | (hig:alerts#Best-practices) |
| Error while the app is in the background | no error notification; errors belong in an Alert | (hig:notifications#Best-practices) |

"Confirmation dialog" is not a separate HIG component but the SwiftUI API for Action sheets (see presentation.md).

### Secondary task and modal presentation
| Situation | Component | Source |
|---|---|---|
| Little content, short-lived, anchored to the invoking control (regular width, macOS) | Popover | (hig:popovers#Best-practices) |
| In compact size class | Sheet instead of Popover | (hig:popovers#iOS-iPadOS) |
| Scoped, simple task with return to context | Sheet (iPhone: detents) | (hig:sheets#Best-practices) |
| Tools alongside an ongoing main task | iOS/iPadOS nonmodal sheet, macOS panel | (hig:sheets#Best-practices), (hig:panels) |
| Complex, long, or media-heavy task | iOS/iPadOS full-screen modal, macOS new window/full screen | (hig:sheets#Best-practices), (hig:modality#Best-practices) |
| Never | multiple modal views or two alerts at the same time | (hig:modality#Best-practices) |

### Navigation and structure
| Situation | Component | Source |
|---|---|---|
| iPhone: a few main areas | Tab bar | (hig:tab-bars) |
| iPad: many or customizable areas | Tab bar with sidebar adaptation (`sidebarAdaptable`) | (hig:tab-bars#iPadOS), (hig:sidebars#iOS-iPadOS) |
| macOS: top-level navigation | Sidebar in a split view | (hig:sidebars#macOS) |
| Hierarchy with detail view | Split view (`NavigationSplitView`) | (hig:split-views) |
| Frequent actions for the current view | Toolbar, not for switching between app areas | (hig:toolbars) |
| Text-heavy, row-based data | List/Table | (hig:lists-and-tables#Best-practices) |
| Image-heavy or variably sized items | Collection | (hig:collections#Best-practices) |
| macOS: hierarchical text data / deep hierarchy with column jumps | Outline view / Column view | (hig:outline-views#Best-practices), (hig:column-views#Best-practices) |
| macOS: mutually exclusive panes in a window | Tab view (iOS/iPadOS: Segmented control) | (hig:tab-views#iOS-iPadOS) |

### Actions, context, and commands
| Situation | Component | Source |
|---|---|---|
| Single, immediate action | Button | (hig:buttons) |
| Frequent object-related commands, hidden | Context menu, never as the only access | (hig:context-menus#Best-practices) |
| Complete command directory on Mac/iPad | Menu bar | (hig:the-menu-bar) |
| Sharing or handing off to other apps | Activity view (Share Sheet) | (hig:activity-views) |
| Entry point directly from the Home Screen | Home Screen quick actions (max. 4) | (hig:home-screen-quick-actions) |

### Outside the app (system experiences)
| Situation | Component | Source |
|---|---|---|
| Glanceable info, periodically updated | Widget (no real-time data) | (hig:widgets#iOS-iPadOS) |
| Time-bound activity with live updates, clear start and clear end | Live Activity | (hig:live-activities#Best-practices) |
| Timely info when the app is not in the foreground | Notification, not duplicating the Live Activity | (hig:notifications), (hig:live-activities#Starting-updating-and-ending-a-Live-Activity) |
| One action without launching the app (Control Center, Lock Screen, Action button) | Control | (hig:controls#Best-practices) |
| Functionality via Siri/Spotlight | App Shortcut, result as a snippet | (hig:app-shortcuts), (hig:snippets) |
| Data on the watch face | Complication | (hig:complications) |

## Index of all components

Platform information comes from the header of each mirror page. Abbreviations: i = iOS, iP = iPadOS, m = macOS, w = watchOS, tv = tvOS, v = visionOS.

| Component | slug | Platforms | File |
|---|---|---|---|
| Charts | charts | i iP m w tv v | [content.md](content.md) |
| Image views | image-views | i iP m w tv v | [content.md](content.md) |
| Text views | text-views | i iP m w tv v | [content.md](content.md) |
| Web views | web-views | i iP m v | [content.md](content.md) |
| Boxes | boxes | i iP m v | [layout-and-organization.md](layout-and-organization.md) |
| Collections | collections | i iP m tv v | [layout-and-organization.md](layout-and-organization.md) |
| Column views | column-views | m | [layout-and-organization.md](layout-and-organization.md) |
| Disclosure controls | disclosure-controls | i iP m v | [layout-and-organization.md](layout-and-organization.md) |
| Labels | labels | i iP m w tv v | [layout-and-organization.md](layout-and-organization.md) |
| Lists and tables | lists-and-tables | i iP m w tv v | [layout-and-organization.md](layout-and-organization.md) |
| Lockups | lockups | tv | [layout-and-organization.md](layout-and-organization.md) |
| Outline views | outline-views | m | [layout-and-organization.md](layout-and-organization.md) |
| Split views | split-views | i iP m w tv v | [layout-and-organization.md](layout-and-organization.md) |
| Tab views | tab-views | m w | [layout-and-organization.md](layout-and-organization.md) |
| Activity views | activity-views | i iP v | [menus-and-actions.md](menus-and-actions.md) |
| Buttons | buttons | i iP m w tv v | [menus-and-actions.md](menus-and-actions.md) |
| Context menus | context-menus | i iP m tv v | [menus-and-actions.md](menus-and-actions.md) |
| Dock menus | dock-menus | m | [menus-and-actions.md](menus-and-actions.md) |
| Edit menus | edit-menus | i iP m v | [menus-and-actions.md](menus-and-actions.md) |
| Home Screen quick actions | home-screen-quick-actions | i iP | [menus-and-actions.md](menus-and-actions.md) |
| Menus | menus | i iP m w tv v | [menus-and-actions.md](menus-and-actions.md) |
| Ornaments | ornaments | v | [menus-and-actions.md](menus-and-actions.md) |
| Pop-up buttons | pop-up-buttons | i iP m v | [menus-and-actions.md](menus-and-actions.md) |
| Pull-down buttons | pull-down-buttons | i iP m v | [menus-and-actions.md](menus-and-actions.md) |
| The menu bar | the-menu-bar | iP m | [menus-and-actions.md](menus-and-actions.md) |
| Toolbars | toolbars | i iP m w tv v | [menus-and-actions.md](menus-and-actions.md) |
| Path controls | path-controls | m | [navigation-and-search.md](navigation-and-search.md) |
| Search fields | search-fields | i iP m w tv v | [navigation-and-search.md](navigation-and-search.md) |
| Sidebars | sidebars | i iP m tv v | [navigation-and-search.md](navigation-and-search.md) |
| Tab bars | tab-bars | i iP m tv v | [navigation-and-search.md](navigation-and-search.md) |
| Token fields | token-fields | m | [navigation-and-search.md](navigation-and-search.md) |
| Action sheets | action-sheets | i iP m w tv | [presentation.md](presentation.md) |
| Alerts | alerts | i iP m w tv v | [presentation.md](presentation.md) |
| Page controls | page-controls | i iP w tv v | [presentation.md](presentation.md) |
| Panels | panels | m | [presentation.md](presentation.md) |
| Popovers | popovers | i iP m v | [presentation.md](presentation.md) |
| Scroll views | scroll-views | i iP m w tv v | [presentation.md](presentation.md) |
| Sheets | sheets | i iP m w tv v | [presentation.md](presentation.md) |
| Windows | windows | iP m v | [presentation.md](presentation.md) |
| Color wells | color-wells | i iP m v | [selection-and-input.md](selection-and-input.md) |
| Combo boxes | combo-boxes | m | [selection-and-input.md](selection-and-input.md) |
| Digit entry views | digit-entry-views | tv | [selection-and-input.md](selection-and-input.md) |
| Image wells | image-wells | m | [selection-and-input.md](selection-and-input.md) |
| Pickers | pickers | i iP m w tv v | [selection-and-input.md](selection-and-input.md) |
| Segmented controls | segmented-controls | i iP m tv v | [selection-and-input.md](selection-and-input.md) |
| Sliders | sliders | i iP m w v | [selection-and-input.md](selection-and-input.md) |
| Steppers | steppers | i iP m v | [selection-and-input.md](selection-and-input.md) |
| Text fields | text-fields | i iP m w tv v | [selection-and-input.md](selection-and-input.md) |
| Toggles | toggles | i iP m w tv v | [selection-and-input.md](selection-and-input.md) |
| Virtual keyboards | virtual-keyboards | i iP w tv v | [selection-and-input.md](selection-and-input.md) |
| Activity rings | activity-rings | i iP w | [status.md](status.md) |
| Gauges | gauges | i iP m w v | [status.md](status.md) |
| Progress indicators | progress-indicators | i iP m w tv v | [status.md](status.md) |
| Rating indicators | rating-indicators | m | [status.md](status.md) |
| App Shortcuts | app-shortcuts | i iP w v | [system-experiences.md](system-experiences.md) |
| Complications | complications | w | [system-experiences.md](system-experiences.md) |
| Controls | controls | i iP m | [system-experiences.md](system-experiences.md) |
| Live Activities | live-activities | i iP m w | [system-experiences.md](system-experiences.md) |
| Notifications | notifications | i iP m w tv v | [system-experiences.md](system-experiences.md) |
| Snippets | snippets | i iP m | [system-experiences.md](system-experiences.md) |
| Status bars | status-bars | i iP | [system-experiences.md](system-experiences.md) |
| Top Shelf | top-shelf | tv | [system-experiences.md](system-experiences.md) |
| Watch faces | watch-faces | w | [system-experiences.md](system-experiences.md) |
| Widgets | widgets | i iP m w v | [system-experiences.md](system-experiences.md) |

## Known ambiguities in the mirror
- **Tab bars:** The header lists macOS, but the page contains no macOS guidance (hig:tab-bars#Platform-considerations).
- **Tab views:** The maximum number of tabs is stated inconsistently; "no more than six" appears next to "six or more" (hig:tab-views#Best-practices).
- **Pull-down buttons:** The mirror links `MenuPickerStyle` as the SwiftUI type. `Menu` is probably meant, because `MenuPickerStyle` corresponds to the Pop-up button.
- **Complications:** The page dates from 2023 and contains no dimensions for newer case sizes. One inline dimension is given twice with conflicting values (see system-experiences.md).
- Each file marks where API names are not in the mirror and were added from developer knowledge. Verify these names before use.
