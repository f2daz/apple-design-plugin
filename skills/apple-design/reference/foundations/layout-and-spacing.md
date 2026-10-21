# Layout and Spacing

> Source: HIG mirror `layout.md` (Apple update 2026-09-09 "Updated guidance to reflect current best practices"), `right-to-left.md`, peripherally `spatial-layout.md`; specifications supplemented from `accessibility`, `widgets`, `live-activities`, `buttons`, `toolbars`, `sidebars`, `tab-bars`, `scroll-views`. Mirrored 2026-10-21. Paraphrased.

## Overview

Layout structures content by importance and must adapt to display sizes, orientation, window sizes, multitasking, text size and reading direction. The foundation is **safe areas**, **layout guides/margins** and **size classes** – not device type or orientation. With Liquid Glass, the following also applies: controls float in their own layer above the content; content extends beneath them to the window edges.

> **Important – device specifications:** The current version of `layout.md` in the mirror (as of Apple update 2026-09-09) **no longer** contains device tables (iPhone/iPad/Mac/Watch: resolution, point size, safe area insets, size classes per model) – even though the change log lists earlier additions up to iPhone 17 / Apple Watch Series 11 / Ultra 3. Therefore no model tables are added here from memory. Substitute specifications available from other pages are listed under "Specifications". Current device data (pt, px, scale, corner radius per model): `python3 -I scripts/device_specs.py [--family iphone|ipad|watch]` – reads the simulator profiles from Xcode. Safe area insets are not included there → measure in the Simulator/Preview or use `safeAreaInsets` at runtime.

## Core rules

### Visual hierarchy
- Order by importance: important items at the top and on the leading side; for RTL, use system components that mirror automatically. (hig:layout#Visual-hierarchy)
- Align elements and use indentation to express subordination. (hig:layout#Visual-hierarchy)
- Group related items using white space, container shapes or separator lines. (hig:layout#Visual-hierarchy)
- Use progressive disclosure (disclosure triangles, menus, nested views, scrollable sections). (hig:layout#Visual-hierarchy)
- Separate controls from content using Liquid Glass – no solid or semi-transparent background areas beneath controls; use a scroll edge effect instead. (hig:layout#Visual-hierarchy)
- Let full-screen background content extend beneath sidebars, toolbars and tab bars; if sidebars/inspectors cover important parts of an image, use the background extension effect (mirrors and blurs the image beneath). (hig:layout#Visual-hierarchy, hig:sidebars#Best-practices)

### Adaptability
- Support: size classes (horizontal/vertical, compact/regular), screen sizes, orientations and aspect ratios, Dynamic Island, external displays, Display Zoom, freely resizable windows on iPad and Mac, text sizes, localization (LTR/RTL, formats, text lengths). (hig:layout#Adaptability)
- Respect safe areas, margins and guides; fine-tune with layout modifiers. (hig:layout#Adaptability)
- Even orientation-locked apps (e.g. landscape games) must scale cleanly across devices and window sizes. (hig:layout#Adaptability)
- Plan for text size changes: side-by-side views stack, rows/containers grow in height, single-line rows become multiline. (hig:layout#Adaptability)
- Test with the largest and smallest layouts, different size classes, localizations and text sizes (Device Hub, including iPad resizing and iPhone Mirroring on the Mac). (hig:layout#Adaptability)
- Scale background artwork for other aspect ratios (fill), don't distort it; for very wide/tall windows, extend it beyond the usual visible area. (hig:layout#Adaptability)

### Size classes
- Decide layout by size class, **not** by device type (idiom) or orientation. (hig:layout#Size-classes)
- Consider all combinations of compact/regular × compact/regular in portrait and landscape. (hig:layout#Size-classes)
- Functionality stays the same when the size class changes; only the visible amount changes (e.g. tab bar → sidebar, resolving an overflow menu). (hig:layout#Size-classes)
- The idiom stays the same during resizing – the layout must remain recognizable as typical for the platform. (hig:layout#Size-classes)

### Guides and safe areas
- **Layout guide**: rectangular region for positioning/aligning; the system provides guides for standard margins and readable text width, custom guides are possible. (hig:layout#Guides-and-safe-areas)
- **Safe area**: the area not obscured by hardware (Dynamic Island, camera housing) or bars (toolbar, tab bar, status bar). Always keep controls and critical content within it; backgrounds may extend beyond it. (hig:layout#Guides-and-safe-areas)

### Spacing and grouping
- Spacing between controls is as important as their size: approx. **12 pt** padding around elements with a bezel, approx. **24 pt** around elements without a bezel (measured from visible edges). (hig:accessibility)
- Standard components in toolbars have corner radii concentric with the bar's corners; design custom components to be concentric as well. (hig:toolbars#Best-practices)
- Group toolbar items by function and frequency: leading (back, sidebar, title, document menu – not customizable), center (frequently used controls, customizable, collapse into the overflow menu), trailing (important items, inspectors, search, More menu, primary action – always visible). (hig:toolbars#Item-groupings)
- Scroll edge effect only behind floating elements, one per view; in split views one per pane, at equal height. (hig:scroll-views#Scroll-edge-effects)

### Right-to-left (hig:right-to-left)
- System frameworks mirror standard components automatically; update your own components deliberately.
- Align text with the interface direction; but align paragraphs (≥ 3 lines) according to **their language**; align lists consistently.
- Never reverse the digit order of a number (phone, card number); do reverse the order of progress/counting sequences – never mirror the digits themselves.
- Mirror: sliders, progress indicators, back/forward, icons with a reading or movement direction, ordered image sequences.
- Don't mirror: photos/illustrations, logos, universal signs (checkmark), real-world objects (clock), controls with a real direction ("to the right").
- Set Arabic/Hebrew approx. 2 pt larger next to Latin capitals.
- Check complex icons component by component (badge, slash, tool handedness); SF Symbols provide RTL and localized variants.

## Specifications

### Control sizes (hig:accessibility, hig:buttons#Best-practices)

| Platform | Default control | Minimum |
|---|---|---|
| iOS, iPadOS | 44×44 pt | 28×28 pt |
| macOS | 28×28 pt | 20×20 pt |
| tvOS | 66×66 pt | 56×56 pt |
| visionOS | 60×60 pt | 28×28 pt |
| watchOS | 44×44 pt | 28×28 pt |

Buttons: hit region at least 44×44 pt (visionOS 60×60 pt). visionOS: button centers at least 60 pt apart; button sizes Mini 28 / Small 32 / Regular 44 / Large 52 / Extra large 64 pt. (hig:buttons, hig:layout#visionOS)

Note: `accessibility` gives a minimum of 28×28 pt for visionOS, `buttons` a hit region of at least 60×60 pt – minimum = smallest permissible control size, 60×60 = recommended hit region.

### Screen sizes (points, portrait) – only indirectly in the mirror

The mirror lists screen sizes only as a reference for widget specifications, **without model mapping**. Don't use as a complete device list.

| iPhone (pt, portrait) according to `widgets#Specifications` |
|---|
| 430×932 · 428×926 · 414×896 · 414×736 · 393×852 · 390×844 · 375×812 · 375×667 · 360×780 · 320×568 |

| iPad (pt, portrait) according to `widgets#Specifications` |
|---|
| 768×1024 · 744×1133 · 810×1080 · 820×1180 · 834×1112 · 834×1194 · 1024×1366 · with Display Zoom "More Space": 954×1373 · 970×1389 · 1192×1590 |

`live-activities#Specifications` lists some iPad dimensions under "portrait" in landscape orientation (1366×1024, 1194×834, 1012×834, 1080×810, 1024×768) – a contradiction in the source; 1012×834 does not appear in the widget list.

| Apple Watch case | Smart Stack widget (pt) |
|---|---|
| 40 mm | 152×69.5 |
| 41 mm | 165×72.5 |
| 42 mm | 176×72.5 |
| 44 mm | 173×76.5 |
| 45 mm | 184×80.5 |
| 46 mm | 194×80.5 |
| 49 mm (Ultra 3, 4) | 198×81.5 (only in `live-activities`, missing in `widgets`) |

Mac: no screen or window sizes in the mirror. watchOS display resolutions: not in the mirror.

### tvOS (peripheral)
Safe area: inset content 60 pt at top/bottom, 80 pt at the sides. Grids (unfocused width / horizontal spacing 40 pt / vertical at least 100 pt): 2 columns 860 pt · 3: 560 · 4: 410 · 5: 320 · 6: 260 · 7: 217 · 8: 184 · 9: 160 pt. (hig:layout#tvOS)

## Platform differences

### iOS
- Size classes are primary; iPhone in landscape can have compact height. Respect the Dynamic Island and bars via the safe area. (hig:layout)
- The tab bar floats at the bottom on Liquid Glass; it can minimize when scrolling (accessory inline). (hig:tab-bars#iOS)
- Large title in the toolbar, changes to the standard title when scrolling. (hig:toolbars#iOS)

### iPadOS
- Windows freely resizable, all size class combinations possible; tab bar at the top, optionally convertible into a sidebar (`sidebarAdaptable`); toolbar and tab bar can share the top row. (hig:tab-bars#iPadOS, hig:toolbars#iPadOS)
- Sidebar: max. two hierarchy levels, otherwise a split view with a content list. (hig:sidebars)
- Default sheet presentation: page or form sheet. (hig:sheets#iOS-iPadOS)

### macOS
- No controls or critical information at the bottom edge of the window (windows are often moved partly below the screen edge) – this also applies to sidebars. (hig:layout#macOS, hig:sidebars#macOS)
- No content behind the camera housing at the top edge (`NSPrefersDisplaySafeAreaCompatibilityMode`). (hig:layout#macOS)
- Collapse the sidebar automatically in small windows if appropriate; row height depends on the sidebar size (system setting). (hig:sidebars#macOS)
- Also offer every toolbar item as a menu command. (hig:toolbars#macOS)

### watchOS
- At most three glyph buttons or two text buttons side by side; text buttons are best at full width; two side by side only without scrolling. (hig:layout#watchOS)
- Autorotation in views that people show to others (image, QR code). (hig:layout#watchOS)
- Toolbar buttons at the top in the corners or at the bottom; content scrolls beneath. (hig:toolbars#watchOS)

### visionOS (peripheral)
- Keep windows/volumes resizable, center content horizontally at large sizes; use min/max sizes only to prevent overlap, not to prevent resizing. (hig:layout#visionOS)
- Use 3D in windows sparingly and inset; put additional content in an adjacent window instead of an ornament. (hig:layout#visionOS)
- Center important content in the field of view, don't anchor content to the head, use depth for hierarchy but not for text. In visionOS, points are angular measurements (Dynamic Scale). (hig:spatial-layout)

## Implementation

**SwiftUI**
```swift
@Environment(\.horizontalSizeClass) var hSize      // UserInterfaceSizeClass
var body: some View {
    if hSize == .compact { TabView { … } } else { NavigationSplitView { … } detail: { … } }
}
// Adaptive navigation in one step
TabView { … }.tabViewStyle(.sidebarAdaptable)
// Safe area: background may extend beyond it, content stays inside
content.background { Image("hero").resizable().scaledToFill().ignoresSafeArea() }
// "Extend" content beneath the sidebar
Image("hero").backgroundExtensionEffect()
// Scroll edge effect (change the style only when needed)
ScrollView { … }.scrollEdgeEffectStyle(.soft, for: .top)
// Text size → stacking
ViewThatFits { HStack { … }; VStack { … } }
```
- `safeAreaInset(edge:)` / `safeAreaPadding` for custom floating bars; `ContainerRelativeShape` for concentric corners (mentioned in `live-activities`).
- RTL: `.leading/.trailing` instead of `.left/.right`; `Image(systemName:)` mirrors automatically, custom assets with direction "Left to Right, Mirrors" in the asset catalog. Preview with `\.layoutDirection`.

**UIKit**
- `safeAreaLayoutGuide`, `layoutMarginsGuide`, `readableContentGuide` (readable text width), `UILayoutGuide`; trait changes via `UITraitChangeObservable` / `registerForTraitChanges`.
- `UIBackgroundExtensionView`, `UIScrollEdgeEffect.Style`, `UITabBarController.MinimizeBehavior`.
- Leading/trailing constraints instead of left/right; `semanticContentAttribute` for special cases.

**AppKit**
- `NSLayoutGuide`, Auto Layout; `NSScrollEdgeEffectStyle`; split view with collapsible sidebar.

> API names from the mirror: `backgroundExtensionEffect()`, `UIBackgroundExtensionView`, `SafeAreaRegions`, `UILayoutGuide`, `NSLayoutGuide`, `UITraitChangeObservable`, `UserInterfaceSizeClass`, `ScrollEdgeEffectStyle`, `TabBarMinimizeBehavior`, `sidebarAdaptable`, `isAutorotating`, `defaultWindowPlacement(_:)`. Remaining names (`readableContentGuide`, `safeAreaInset`, `ViewThatFits`, `scrollEdgeEffectStyle(_:for:)`) are framework knowledge.

## Review checklist

- [ ] Most important content at the top/leading; alignment and indentation reflect hierarchy
- [ ] Groups clearly recognizable via white space/containers/separators
- [ ] Layout decided by size class, not by device/orientation
- [ ] All four size class combinations checked; functionality identical
- [ ] Controls and text within the safe area; backgrounds edge to edge
- [ ] No areas behind bars; scroll edge effect only behind floating elements, one per view
- [ ] Background content extends beneath sidebar/toolbar/tab bar (background extension effect if needed)
- [ ] Hit regions ≥ platform default (iOS 44×44 pt), never below the minimum
- [ ] Padding ~12 pt (with bezel) / ~24 pt (without bezel)
- [ ] Largest Dynamic Type size: stacking instead of overlapping
- [ ] iPad: free resizing tested (narrow to wide), tab bar ↔ sidebar
- [ ] macOS: nothing critical at the bottom edge of the window, nothing behind the camera housing
- [ ] watchOS: max. 3 glyph / 2 text buttons per row
- [ ] RTL: mirrored where direction carries meaning; numbers, logos, photos unchanged
- [ ] Tested on the smallest and largest device/window, with long localizations

## Anti-patterns

- `if UIDevice.current.userInterfaceIdiom == .pad` as a layout decision.
- Fixed frames for screens of a specific iPhone size.
- A semi-transparent bar under a toolbar "for legibility" instead of a scroll edge effect.
- Content ends abruptly at the sidebar edge instead of extending beneath it.
- Features disappear in compact width without a replacement.
- Save button at the bottom left of a Mac window.
- `.left/.right` constraints; mirrored logos or phone numbers in RTL mode.
- More than three icon buttons side by side on the Watch.
- Taking device specifications for mockups from memory instead of from `device_specs.py` or the UI kits of the Apple Design Resources.
