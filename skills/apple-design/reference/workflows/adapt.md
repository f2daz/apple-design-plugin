# adapt – bring a design to more Apple platforms

Principle: **same app, idiomatic form.** Content, data and terminology stay; structure, input and density follow the target platform. Scaling is not adapting.

## Steps

1. Clarify source and target platform; load the target reference (`reference/platforms/<target>.md`) and run `hig_search.py platform <target>` for the components in use.
2. AskUserQuestion if open: "What role does the target platform play?" – full-featured (all functions) · companion (core tasks) · glance (status/quick action).
3. Build the mapping table (below), justify deviations, then implement (build.md).

## Mapping guide

| Aspect | iPhone | iPad | Mac | Watch |
|---|---|---|---|---|
| Top-level navigation | Tab bar | Tab bar ↔ sidebar (adaptable) | Sidebar in split view + menu bar | NavigationStack, vertical pages |
| Hierarchy | Push in stack | Split view (2–3 columns) | Split view, possibly multiple windows | Flat stack, few levels |
| Side task | Sheet | Sheet / popover / inspector | Window-modal sheet, panel, inspector | Modal sheet, short |
| Actions | Toolbar, swipe, context menu | + keyboard shortcuts, pointer hover | Menu bar + toolbar + context menu + shortcuts | Toolbar corners, list, Crown |
| Input | Touch | Touch, Pencil, keyboard, trackpad | Mouse/trackpad, keyboard | Touch, Digital Crown, dictation |
| Density | Compact | Medium, uses the width | High, smaller controls | Minimal, one task |
| System locations | Widgets, Live Activities, controls | Widgets, Stage Manager | Menu bar extra, widgets, Dock | Complications, Smart Stack, Live Activities |

Details and numbers are in the platform references; for watchOS in particular, cut content radically.

## Typical traps

- iPad: iPhone layout stretched in the middle; popover without an anchor; no keyboard support; no resizing/multitasking.
- Mac (Catalyst or SwiftUI): no menu bar, touch-sized controls, sheets instead of windows, no undo, no settings in the app menu.
- Watch: shrunken iPhone screens, text input as the main path, too many levels, no complication.
