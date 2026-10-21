# Color and Dark Mode

> Source: HIG mirror `color.md` (Apple update 2025-12-16, Liquid Glass), `dark-mode.md` (2024-08-06), supplemented by `accessibility`, `materials`, `buttons`, `toolbars`, `tab-bars`, `sidebars`, `branding`, `widgets`. Mirrored 2026-10-21. Paraphrased; color values taken over as facts.

## Overview

Color communicates status, interactivity and brand – but only when it is used consistently and sparingly. On Apple platforms the default is **semantic, dynamic system colors** that automatically adapt to Light/Dark, Increase Contrast, vibrancy and Liquid Glass. Custom colors always need four variants (Light, Dark, each + Increased Contrast). Dark Mode is a systemwide setting that apps must respect – no app-specific toggle.

## Core rules

### General
- Never use one color for two meanings (e.g. brand color for interactive buttons **and** for non-interactive text). (hig:color#Best-practices)
- Make sure every color works in Light, Dark and Increased Contrast; create custom colors with a Light/Dark variant and a significantly higher-contrast Increased Contrast variant for each. (hig:color#Best-practices)
- Provide Light **and** Dark variants even if the app uses only one appearance – otherwise Liquid Glass doesn't adapt correctly. (hig:color#Best-practices)
- Test under different lighting conditions and on different devices (True Tone, P3/sRGB profiles on the Mac). (hig:color#Best-practices)
- Consider how artwork and translucency change adjacent colors. (hig:color#Best-practices)
- For user color selection, use the system color picker (`ColorPicker`). (hig:color#Best-practices)

### Inclusive
- Never convey information through color alone – add text, shape or a symbol. (hig:color#Inclusive-color)
- Avoid combinations with too little contrast or that are indistinguishable for people with color blindness. (hig:color#Inclusive-color)
- Check cultural color meanings (e.g. red). (hig:color#Inclusive-color)

### System colors
- Don't hard-code system color values; the table values are a design reference and can change with each release. Reference them via APIs (`Color`, `UIColor`, `NSColor`). (hig:color#System-colors)
- Don't misuse semantic colors (e.g. don't use `separator` as a text color or `secondaryLabel` as a background). (hig:color#System-colors)

### Liquid Glass color
- Liquid Glass is colorless by default and picks up color from the content behind it. Use tinting ("stained glass") only for real emphasis, e.g. a primary action or status. (hig:color#Liquid-Glass-color)
- For primary actions, tint the **background**, not the symbol/text – this is what the system does for prominent buttons (e.g. Done) with the accent color. Don't give multiple controls a colored background. (hig:color#Liquid-Glass-color)
- With colorful content: prefer monochrome toolbars/tab bars or choose a clearly distinguishable accent color; with monochrome content, the brand color makes sense as an accent. (hig:color#Liquid-Glass-color, hig:toolbars#Best-practices, hig:tab-bars#Best-practices, hig:buttons#Style)
- Pay attention to the resting state: don't let similar colors in the content layer and in controls overlap; at least the initial state (top of scroll) must be clearly legible. (hig:color#Liquid-Glass-color)
- Small glass elements (toolbar, tab bar) switch adaptively between light/dark; symbols/text on them are monochrome by default. Large elements (sidebar) are more opaque. (hig:color#Liquid-Glass-color)

### Accent color / tint
- Use the accent color deliberately: primary actions, status indicators (e.g. badges), the selected tab icon – not across all controls. (hig:branding)
- Prefer moving the brand into the content layer, where it shows through beneath Liquid Glass. (hig:branding)
- Reduce toolbar backgrounds and tinted controls; derive color from the content. (hig:toolbars#Best-practices)
- Prominent buttons: at most one or two per view; the destructive role uses system red, the primary role the accent color. (hig:buttons#Style, hig:buttons#Role)
- macOS: the app accent color applies only if the user has selected "Multicolor"; otherwise the chosen system accent color overrides it – except for sidebar icons with an intentionally fixed color. (hig:color#App-accent-colors, hig:sidebars#Best-practices)

### Contrast
- Minimum contrast 4.5:1; aim for 7:1 for custom foreground/background colors, especially for small text. (hig:dark-mode#Dark-Mode-colors)
- Accessibility Inspector checks against the following table; if the default doesn't meet it, provide a higher-contrast scheme at least for Increase Contrast. (hig:accessibility)

| Text size | Weight | Minimum contrast |
|---|---|---|
| up to 17 pt | all | 4.5:1 |
| 18 pt | all | 3:1 |
| all | Bold | 3:1 |

Contradiction: `dark-mode` states a blanket "at least 4.5:1", while `accessibility` allows 3:1 from 18 pt or for bold text. Use 4.5:1 as the lower bound for body text, and 3:1 only for large/bold text.

### Dark Mode
- Don't offer an app-specific light/dark setting; respect the system setting (including "Automatic", which can switch at runtime). (hig:dark-mode#Best-practices)
- Test in Dark Mode with Increase Contrast and Reduce Transparency – individually and combined. (hig:dark-mode#Best-practices)
- Stay permanently dark only in exceptional cases (immersive media). (hig:dark-mode#Best-practices)
- Dark Mode colors are not a simple inversion: darker backgrounds, lighter foregrounds. (hig:dark-mode#Dark-Mode-colors)
- Create custom colors as a color set in the asset catalog with a light/dark variant. (hig:dark-mode#Dark-Mode-colors)
- Slightly darken white image backgrounds so they don't "glow". (hig:dark-mode#Dark-Mode-colors)
- Use SF Symbols; where necessary, separate icons for light/dark (e.g. outline only in Light Mode). Check full-color assets in both modes, with variants in the asset catalog if needed. (hig:dark-mode#Icons-and-images)
- Use the system label colors for labels and system views for text fields/text views. (hig:dark-mode#Text)

## Specifications

### System colors (SwiftUI; RGB, hex converted) (hig:color#Specifications)

| Name | SwiftUI | Light | Dark | Increased Contrast Light | Increased Contrast Dark |
|---|---|---|---|---|---|
| Red | `red` | 255,56,60 (#FF383C) | 255,66,69 (#FF4245) | 233,21,45 (#E9152D) | 255,97,101 (#FF6165) |
| Orange | `orange` | 255,141,40 (#FF8D28) | 255,146,48 (#FF9230) | 197,83,0 (#C55300) | 255,160,86 (#FFA056) |
| Yellow | `yellow` | 255,204,0 (#FFCC00) | 255,214,0 (#FFD600) | 161,106,0 (#A16A00) | 254,223,67 (#FEDF43) |
| Green | `green` | 52,199,89 (#34C759) | 48,209,88 (#30D158) | 0,137,50 (#008932) | 74,217,104 (#4AD968) |
| Mint | `mint` | 0,200,179 (#00C8B3) | 0,218,195 (#00DAC3) | 0,133,117 (#008575) | 84,223,203 (#54DFCB) |
| Teal | `teal` | 0,195,208 (#00C3D0) | 0,210,224 (#00D2E0) | 0,129,152 (#008198) | 59,221,236 (#3BDDEC) |
| Cyan | `cyan` | 0,192,232 (#00C0E8) | 60,211,254 (#3CD3FE) | 0,126,174 (#007EAE) | 109,217,255 (#6DD9FF) |
| Blue | `blue` | 0,136,255 (#0088FF) | 0,145,255 (#0091FF) | 30,110,244 (#1E6EF4) | 92,184,255 (#5CB8FF) |
| Indigo | `indigo` | 97,85,245 (#6155F5) | 109,124,255 (#6D7CFF) | 86,74,222 (#564ADE) | 167,170,255 (#A7AAFF) |
| Purple | `purple` | 203,48,224 (#CB30E0) | 219,52,242 (#DB34F2) | 176,47,194 (#B02FC2) | 234,141,255 (#EA8DFF) |
| Pink | `pink` | 255,45,85 (#FF2D55) | 255,55,95 (#FF375F) | 231,18,77 (#E7124D) | 255,138,196 (#FF8AC4) |
| Brown | `brown` | 172,127,94 (#AC7F5E) | 183,138,102 (#B78A66) | 149,109,81 (#956D51) | 219,166,121 (#DBA679) |

visionOS uses the Dark values. According to the change log, the system color values were updated on June 9, 2025 – don't take over values from older references.

### iOS/iPadOS system grays (UIKit) (hig:color#Specifications)

| Name | UIKit | Light | Dark | Increased Contrast Light | Increased Contrast Dark |
|---|---|---|---|---|---|
| Gray | `systemGray` | 142,142,147 (#8E8E93) | 142,142,147 (#8E8E93) | 108,108,112 (#6C6C70) | 174,174,178 (#AEAEB2) |
| Gray 2 | `systemGray2` | 174,174,178 (#AEAEB2) | 99,99,102 (#636366) | 142,142,147 (#8E8E93) | 124,124,128 (#7C7C80) |
| Gray 3 | `systemGray3` | 199,199,204 (#C7C7CC) | 72,72,74 (#48484A) | 174,174,178 (#AEAEB2) | 84,84,86 (#545456) |
| Gray 4 | `systemGray4` | 209,209,214 (#D1D1D6) | 58,58,60 (#3A3A3C) | 188,188,192 (#BCBCC0) | 68,68,70 (#444446) |
| Gray 5 | `systemGray5` | 229,229,234 (#E5E5EA) | 44,44,46 (#2C2C2E) | 216,216,220 (#D8D8DC) | 54,54,56 (#363638) |
| Gray 6 | `systemGray6` | 242,242,247 (#F2F2F7) | 28,28,30 (#1C1C1E) | 235,235,240 (#EBEBF0) | 36,36,38 (#242426) |

The SwiftUI equivalent of `systemGray` is `Color.gray`; for Gray 2–6 the mirror names no SwiftUI counterpart.

Not in the mirror: concrete RGB values for semantic colors (`label`, `systemBackground` …) – these can only be obtained via APIs.

### Semantic colors iOS/iPadOS (hig:color#iOS-iPadOS)

**Backgrounds** – two sets with three levels each (Primary = entire view, Secondary = grouping within it, Tertiary = grouping within Secondary):

| Context | Primary | Secondary | Tertiary |
|---|---|---|---|
| Standard | `systemBackground` | `secondarySystemBackground` | `tertiarySystemBackground` |
| Grouped table view | `systemGroupedBackground` | `secondarySystemGroupedBackground` | `tertiarySystemGroupedBackground` |

**Foreground:**

| Color | Use | UIKit |
|---|---|---|
| Label | Primary text | `label` |
| Secondary label | Secondary text | `secondaryLabel` |
| Tertiary label | Tertiary text | `tertiaryLabel` |
| Quaternary label | Quaternary text | `quaternaryLabel` |
| Placeholder text | Placeholder in controls/text views | `placeholderText` |
| Separator | Separator that lets content show through | `separator` |
| Opaque separator | Opaque separator | `opaqueSeparator` |
| Link | Text as a link | `link` |

Dark Mode iOS/iPadOS: backgrounds exist as **base** (darker, recedes) and **elevated** (lighter, comes forward, e.g. popover, sheet, multitasking). The system switches automatically – so use system backgrounds instead of custom colors. (hig:dark-mode#iOS-iPadOS)

### Semantic colors macOS (AppKit `NSColor`) (hig:color#macOS)

| Purpose | API |
|---|---|
| Text label (1–4) | `labelColor`, `secondaryLabelColor`, `tertiaryLabelColor`, `quaternaryLabelColor` |
| Document text / background | `textColor`, `textBackgroundColor` |
| Placeholder | `placeholderTextColor` |
| Link | `linkColor` |
| Window / under document | `windowBackgroundColor`, `underPageBackgroundColor` |
| Large elements (browser, table) | `controlBackgroundColor` |
| Alternating rows | `alternatingContentBackgroundColors` |
| Control surface / text / disabled | `controlColor`, `controlTextColor`, `disabledControlTextColor` |
| Selected control / text | `selectedControlColor`, `selectedControlTextColor`, `alternateSelectedControlTextColor` |
| Content selection (key / non-key window) | `selectedContentBackgroundColor`, `unemphasizedSelectedContentBackgroundColor` |
| Text selection (key / non-key) | `selectedTextBackgroundColor`, `selectedTextColor`, `unemphasizedSelectedTextBackgroundColor`, `unemphasizedSelectedTextColor` |
| Menu selection text | `selectedMenuItemTextColor` |
| Accent / tint | `controlAccentColor`, `currentControlTint` |
| Focus ring | `keyboardFocusIndicatorColor` |
| Find highlight | `findHighlightColor` |
| Grid, separator, header | `gridColor`, `separatorColor`, `headerTextColor` |
| Highlight / shadow | `highlightColor`, `shadowColor` |
| Title bar | `windowFrameTextColor` |

macOS **desktop tinting** (with the Graphite accent color): window backgrounds pick up color from the desktop picture. Make custom components with a visible background slightly transparent in the **neutral** state, but not in the colored state. (hig:dark-mode#macOS)

### Color management (hig:color#Color-management)
- Assign color profiles to images; sRGB is correct for most displays.
- Wide color (Display P3) for richer colors: P3 profile, 16 bits per channel, export as PNG; design only on a wide-color display.
- For very similar P3 colors or P3 gradients, consider providing sRGB variants in the asset catalog.

## Platform differences

| Platform | Specifics |
|---|---|
| iOS/iPadOS | Two background sets (system/grouped), base/elevated in Dark Mode, Liquid Glass adapts to content |
| macOS | Extensive `NSColor` semantics, app accent only with "Multicolor", desktop tinting, vibrant variants of all system colors |
| watchOS | No Dark Mode (dark by default). Use background color only to convey meaning (context, orientation), not decoratively; no full-screen color in long-running views (workout, audio). Complications can appear in a single color in tinted mode. (hig:color#watchOS) |
| visionOS | No Dark Mode; use colors on glass sparingly, in bold text and large areas; system colors = Dark values; balance brightness in immersion. (hig:color#visionOS) |
| tvOS | Limited palette matching the logo; don't indicate focus by color alone. (hig:color#tvOS) |

Widgets: can appear full-color, tinted (accented) or clear; never convey meaning through color alone, split elements into an accent group and a primary group (`widgetAccentable`). (hig:widgets)

## Implementation

> The mapping of UIKit/AppKit system color names (`systemRed` …) and SwiftUI semantics (`.primary`, `.secondary`) is framework knowledge, not sourced from the mirror.

| Concept | SwiftUI | UIKit | AppKit |
|---|---|---|---|
| System color | `Color.red`, `.blue` … | `UIColor.systemRed` … | `NSColor.systemRed` … |
| Primary text | `.foregroundStyle(.primary)` | `.label` | `.labelColor` |
| Secondary text | `.foregroundStyle(.secondary)` | `.secondaryLabel` | `.secondaryLabelColor` |
| Tertiary/quaternary | `.tertiary`, `.quaternary` | `.tertiaryLabel`, `.quaternaryLabel` | `.tertiaryLabelColor`, `.quaternaryLabelColor` |
| Background | `Color(uiColor: .systemBackground)` or standard container | `.systemBackground` | `.windowBackgroundColor` |
| Separator | `Divider()` / `Color(uiColor: .separator)` | `.separator` | `.separatorColor` |
| Accent | `.tint(_:)`, `Color.accentColor`, AccentColor in the asset catalog | `tintColor` | `controlAccentColor` |
| Custom color | Color set (Any/Dark + High Contrast) in the asset catalog | `UIColor(named:)` / `UIColor { traits in … }` | `NSColor(name:dynamicProvider:)` |

```swift
// Primary action: tint the background, not the text
Button("Done") { save() }
    .buttonStyle(.borderedProminent)       // System applies the accent color to the background
Button("Delete", role: .destructive) { delete() } // System red via role

// Query the appearance, don't force it
@Environment(\.colorScheme) var scheme
@Environment(\.colorSchemeContrast) var contrast   // .increased with Increase Contrast
```
- No `.preferredColorScheme(.dark)` as an app option; only for intentionally always-dark media views.
- White point: reading/photo/video/game apps can set `UIWhitePointAdaptivityStyle`. (hig:color#Best-practices)

## Review checklist

- [ ] No hard-coded RGB/hex values for system colors
- [ ] Every custom color: Light, Dark, Increased Contrast Light/Dark
- [ ] Light and Dark variants even in single-appearance apps (Liquid Glass adaptivity)
- [ ] Semantic colors used according to purpose (no separator as text, etc.)
- [ ] Information also conveyed via text/shape/symbol, not color alone
- [ ] Contrast ≥ 4.5:1 (body text), target 7:1 for small custom text; 3:1 only for ≥ 18 pt or bold
- [ ] Tested: Light, Dark, Increase Contrast, Reduce Transparency, combinations
- [ ] No app-specific Dark Mode option
- [ ] Liquid Glass: color only for primary action/status, as a background tint, max. one or two prominent controls
- [ ] With colorful content: monochrome bars or a clearly distinct accent color; resting state legible
- [ ] macOS: system accent color respected (sidebar icons), desktop tinting taken into account
- [ ] Images with color profile; P3 assets with sRGB fallback where needed
- [ ] Dark Mode: white image areas darkened, icons visible in both modes
- [ ] iOS: system backgrounds (base/elevated) instead of custom background colors

## Anti-patterns

- Brand color on every button, every icon and as the text color for body text.
- Red/green as the only distinction between error/success.
- A custom "dark theme" toggle in the app settings.
- Dark Mode created by inverting the light palette.
- Tinted, opaque toolbar backgrounds over Liquid Glass.
- Colored labels on glass over similarly colored content.
- Several glass buttons with colored backgrounds side by side.
- `secondaryLabel` as a fill color or `separator` as a text color.
- Taking over hex values from old HIG versions (values changed in 2025).
- Full-screen color backgrounds in watchOS workout views.
