# Materials and Liquid Glass

> Source: HIG mirror `materials.md` (Apple update 2025-09-09), `color.md#Liquid-Glass-color` (2025-12-16), `buttons`, `toolbars`, `tab-bars`, `sidebars`, `scroll-views` (2026-06-08), `layout`, `app-icons` (2026-06-08), `widgets`, `motion`, `branding`, `virtual-keyboards`, `dark-mode`, `sheets`. Mirrored 2026-10-21. Paraphrased.

## Overview

A material creates depth and hierarchy by letting color from the background pass through into the foreground. Apple platforms have two kinds:

| | **Liquid Glass** | **Standard materials** |
|---|---|---|
| Layer | Functional layer (controls, navigation) | Content layer |
| Purpose | Let controls float above content without obscuring it | Structure and separation *within* the content |
| Examples | Tab bar, toolbar, sidebar, buttons in bars, alerts, popovers | App backgrounds, cards, overlays in the content |
| APIs | `glassEffect(_:in:)`, `Glass.regular` / `.clear` | `Material` (`.ultraThin` … `.thick`), `UIBlurEffect`, `UIVibrancyEffect`, `NSVisualEffectView` |

(hig:materials)

**Liquid Glass** is a dynamic material that unifies the design language across platforms: it forms a distinct functional layer above the content, lets content beneath it show through and still keeps controls legible. It has no color of its own, but picks up color from the content behind it, responds to interaction (more strongly with touch, more subtly with a trackpad) and adapts to system settings. (hig:materials#Liquid-Glass, hig:color#Liquid-Glass-color, hig:motion)

## Core rules

### Content layer vs. functional layer
- Do **not** use Liquid Glass in the content layer; use standard materials there. Exception: transient interactive elements in the content (sliders, toggles) briefly take on a glass appearance while being manipulated. (hig:materials#Liquid-Glass)
- Separate controls from content using Liquid Glass – not with solid or semi-transparent background areas; for additional separation, use a scroll edge effect. (hig:layout#Visual-hierarchy)
- Let content extend to the edge beneath sidebars, toolbars and tab bars; use the background extension effect if needed. (hig:layout#Visual-hierarchy, hig:sidebars#Best-practices)

### Restraint, standard vs. custom
- Standard components adopt Liquid Glass automatically – use system components first. (hig:materials#Liquid-Glass)
- On custom controls, use Liquid Glass **sparingly** and only for the most important functional elements; too much glass distracts from the content. (hig:materials#Liquid-Glass)
- Design custom components in bars with corner radii concentric with the bar (standard components already do this). (hig:toolbars#Best-practices)
- No custom toolbar backgrounds/appearances that override the system effects. (hig:toolbars#Best-practices)
- Custom controls above the keyboard: apply glass if the rest of the app uses glass or the bar would otherwise look out of place; a standard toolbar adopts glass automatically. (hig:virtual-keyboards)

### Regular vs. clear
- **Regular** (default for most system components): blurs and adjusts the luminance of the background → legibility. Use it when the background could compromise legibility or the component carries a lot of text (alerts, sidebars, popovers). (hig:materials#Liquid-Glass)
- **Clear**: highly translucent, prioritizes the content behind it. **Only** over visually rich backgrounds (photos, video) for immersive experiences. (hig:materials#Liquid-Glass)
- With clear over bright content, consider a **dark dimming layer at 35% opacity**; not needed with sufficiently dark content or with AVKit standard playback controls (which have their own dimming). (hig:materials#Liquid-Glass)

### Tinting / color on glass
- Use color on glass sparingly: only for primary actions and status indicators. (hig:color#Liquid-Glass-color)
- Emphasize the primary action with a **tinted background** (like system prominent buttons, e.g. Done, with the accent color), not with colored text/symbols. Don't give multiple controls a colored background. (hig:color#Liquid-Glass-color)
- Prominent buttons: one or two per view; in toolbars, exactly one primary action in the `.prominent` style on the trailing side. (hig:buttons#Style, hig:toolbars#Actions)
- With colorful content: keep labels on bars/buttons monochrome or choose a clearly distinct accent color. (hig:color#Liquid-Glass-color, hig:buttons#Style, hig:toolbars#Best-practices, hig:tab-bars#Best-practices)
- Prefer showing the brand in the content layer, where it shows through beneath the glass and is picked up dynamically. (hig:branding)
- Always give custom colors a Light **and** Dark variant, otherwise the glass doesn't adapt correctly. (hig:color#Best-practices)

### Adaptive behavior
- Small glass elements (toolbar, tab bar) switch between a light and dark appearance depending on what's beneath them; symbols/text on them are monochrome by default (dark on light content, light on dark content). (hig:color#Liquid-Glass-color)
- Large glass elements (sidebars) are more opaque to remain legible over complex backgrounds. (hig:color#Liquid-Glass-color)
- The resting state (e.g. top of scroll) must be clearly legible, even if colorful content scrolls beneath it in between. (hig:color#Liquid-Glass-color)

### Scroll edge effects (hig:scroll-views#Scroll-edge-effects)
- Purpose: visual separation between floating elements (e.g. toolbar) and the scrolling content behind them (iOS, iPadOS, macOS). Blurs and reduces the opacity of the content at the edge.
- Prefer the **automatic** style; it becomes more opaque for toolbars with many controls, for text outside of glass controls and for pinned table headers. Styles: automatic, hard, soft – soft only with thorough legibility testing.
- Use only when a scroll view lies behind floating elements – not decoratively, no overlay/dimming.
- One effect per view; in split views one per pane, at equal height.
- Add manually for custom bars if needed.

### Accessibility
- The appearance of regular and clear changes with system settings: preferred Liquid Glass look (device setting), **Reduce Transparency**, **Increase Contrast**. Therefore test custom glass with all combinations. (hig:materials#Liquid-Glass)
- In Dark Mode with Increase Contrast and Reduce Transparency (individually and combined), check for hard-to-read dark text. (hig:dark-mode#Best-practices)
- Motion behavior adapts to the input method and accessibility settings – use system components instead of custom glass animations. (hig:motion)
- The mirror does **not** describe in detail what glass looks like with Reduce Transparency (e.g. opacity values) – make no assumptions; check on the device.

### Standard materials
- Choose a material by its semantic purpose, not by the color it appears to produce. (hig:materials#Standard-materials)
- Use **vibrant colors** on materials (labels, fills, separators). (hig:materials#Standard-materials)
- Thicker = more opaque = better contrast for text/fine details; thinner = more translucent = more context. (hig:materials#Standard-materials)

## Specifications

| Specification | Value | Source |
|---|---|---|
| Dimming under clear glass over bright content | dark layer, 35% opacity | hig:materials#Liquid-Glass |
| Glass variants | regular, clear | hig:materials#Liquid-Glass |
| Scroll edge styles | automatic (default), hard, soft | hig:scroll-views#Scroll-edge-effects |
| Standard materials iOS/iPadOS | ultraThin, thin, regular (default), thick | hig:materials#iOS-iPadOS |
| App icon appearances iOS/iPadOS/macOS | Default, Dark, Clear Light, Clear Dark, Tinted Light, Tinted Dark | hig:app-icons#Specifications |

### Vibrancy on standard materials (iOS/iPadOS) (hig:materials#iOS-iPadOS)

| Type | Levels (`UIVibrancyEffectStyle`) | Restriction |
|---|---|---|
| Label | `label` (default), `secondaryLabel`, `tertiaryLabel`, `quaternaryLabel` | `quaternaryLabel` not on `thin`/`ultraThin` (too little contrast) |
| Fill | `fill` (default), `secondaryFill`, `tertiaryFill` | on all materials |
| Separator | `separator` | on all materials |

## Platform differences

### iOS
- The tab bar floats at the bottom on Liquid Glass; it can minimize on scroll, and an accessory (e.g. mini player) moves inline. (hig:tab-bars#iOS)
- Toolbar buttons get glass automatically; primary action `.prominent`, trailing. (hig:toolbars, hig:buttons)
- Four standard materials for the content layer.

### iPadOS
- Tab bar at the top, optionally as a sidebar; the sidebar floats in the glass layer, content extends beneath it (background extension effect). (hig:tab-bars#iPadOS, hig:sidebars)
- Split views: one scroll edge effect per pane, at equal height.

### macOS
- Sidebars float in the glass layer; toolbar items without a bezel. (hig:sidebars, hig:toolbars#macOS)
- Standard materials via `NSVisualEffectView.Material` with defined purposes; vibrant versions of all system colors. Blending modes: behind window, within window. (hig:materials#macOS)
- Deliberately allow and test vibrancy in custom views.

### watchOS
- Toolbar buttons get a glass appearance to separate them from the content. (hig:buttons)
- Materials in full-screen modals provide context; don't remove the standard material backgrounds of sheets. Sheets are semi-transparent; the background is blurred and desaturated. (hig:materials#watchOS, hig:sheets#watchOS)

### tvOS / visionOS (peripheral)
- tvOS: glass in navigation, Top Shelf, Control Center; image views/buttons become glass when focused. Standard materials: ultraThin/thin (light scheme), regular, thick (dark scheme). (hig:materials#tvOS)
- visionOS: windows use the unmodifiable system material "glass" (no separate Dark Mode). Translucency instead of opacity; thin for interactive elements, regular for sections, thick for dark elements on regular; vibrancy label/secondaryLabel/tertiaryLabel. Buttons on a window: thin, freestanding in space: glass. Toolbar with variable blur. (hig:materials#visionOS, hig:buttons, hig:toolbars#visionOS)

### App icons and widgets
- App icons (iOS, iPadOS, macOS, watchOS) consist of background and foreground layers and receive Liquid Glass attributes (specular highlights, refraction, translucency) automatically. Don't build in your own highlights, shadows, blurs; provide layers unmasked and with clean edges; configure effects in Icon Composer, at group level if appropriate. (hig:app-icons#Layer-design, hig:app-icons#Visual-effects)
- Widgets in the clear appearance: the system desaturates and adds translucency, highlights and Liquid Glass; in the accented rendering mode, glass replaces the background. Define an accent group and a primary group. (hig:widgets)

## Implementation

> **Sourced in the mirror:** `glassEffect(_:in:)`, `Glass.regular`, `Glass.clear`, "Applying Liquid Glass to custom views", "Adopting Liquid Glass", `ScrollEdgeEffectStyle` / `UIScrollEdgeEffect.Style` / `NSScrollEdgeEffectStyle`, `backgroundExtensionEffect()`, `UIBackgroundExtensionView`, `TabBarMinimizeBehavior`, `Material`, `UIVisualEffectView`, `UIBlurEffect`, `UIVibrancyEffect`, `NSVisualEffectView`, `widgetAccentable(_:)`.
> **Framework knowledge (iOS/iPadOS/macOS 26 SDK), not in the mirror:** `GlassEffectContainer`, `.interactive()`, `.tint(_:)` on `Glass`, `glassEffectID(_:in:)`, `.buttonStyle(.glass/.glassProminent)`, `UIGlassEffect`, `NSGlassEffectView`. Verify against the current developer documentation before use.

**SwiftUI**
```swift
// 1. Standard first: system components come with glass
NavigationStack { list }
    .toolbar {
        ToolbarItem(placement: .confirmationAction) {
            Button("Done") { save() }              // Primary action trailing
        }
    }

// 2. Custom control (sparingly!)
Button(action: locate) { Image(systemName: "location") }
    .padding()
    .glassEffect(.regular, in: .circle)         // sourced: glassEffect(_:in:), Glass.regular

// 3. Over photo/video: clear + 35% dimming if needed
ZStack {
    photo
    Color.black.opacity(0.35)                   // only with bright content
    controls.glassEffect(.clear, in: .capsule)
}

// 4. Render/morph several glass elements together (framework knowledge)
GlassEffectContainer(spacing: 20) {
    HStack(spacing: 20) {
        Button("A") {}.glassEffect(.regular.interactive())
        Button("B") {}.glassEffect(.regular.tint(.accentColor).interactive()) // Tint = primary action
    }
}

// Standard material in the content layer
card.background(.thinMaterial, in: .rect(cornerRadius: 16))

// Change the scroll edge effect only when needed
ScrollView { … }.scrollEdgeEffectStyle(.hard, for: .top)

// Check accessibility
@Environment(\.accessibilityReduceTransparency) var reduceTransparency
```

**UIKit:** System bars (`UINavigationBar`, `UITabBar`, `UIToolbar`) adopt glass automatically – don't set `backgroundColor`/`standardAppearance` backgrounds. Custom: `UIVisualEffectView` with a glass effect (framework: `UIGlassEffect`), standard materials with `UIBlurEffect` + `UIVibrancyEffect`. Respect `UIAccessibility.isReduceTransparencyEnabled`.

**AppKit:** Sidebar/toolbar via standard `NSSplitViewController`/`NSToolbar`; standard materials with `NSVisualEffectView` (material + blending mode); custom glass, according to framework knowledge, via `NSGlassEffectView`.

## Review checklist

- [ ] Liquid Glass only in the functional layer (bars, navigation, floating controls), not for cards/backgrounds in the content
- [ ] System components instead of custom builds; custom glass only for a few central controls
- [ ] No solid/semi-transparent areas under bars; content extends beneath bars/sidebar
- [ ] Regular as default; clear only over photo/video, with 35% dimming over bright content
- [ ] Color on glass only for primary action/status, as a background tint, max. one or two prominent controls
- [ ] Monochrome labels on glass with colorful content
- [ ] Resting state (top of scroll) clearly legible
- [ ] Scroll edge effect: only behind floating elements, one per view, automatic preferred
- [ ] Concentric corner radii for custom components in bars
- [ ] Tested with Reduce Transparency, Increase Contrast, Dark Mode, preferred glass look
- [ ] Custom colors with Light and Dark variant
- [ ] Standard materials chosen by purpose; vibrant colors on them; no quaternaryLabel on thin/ultraThin
- [ ] App icon: layers unmasked, without baked-in effects, all appearances (Default/Dark/Clear/Tinted) checked
- [ ] watchOS: material backgrounds of modals/sheets not removed

## Anti-patterns

- "Glass everywhere": cards, list cells, backgrounds in the content with `glassEffect`.
- Clear glass over text or a calm background – legibility breaks down.
- Tinted glass buttons in a row (all colored = none emphasized).
- Colored text/icon on glass instead of a tinted background for the primary action.
- Custom opaque navigation bar color over the system glass.
- Scroll edge effect as decoration or doubled (toolbar + custom gradient).
- Custom blur/gloss effects in the app icon, pre-rounded icon layers.
- Glass look imitated with `.ultraThinMaterial` + border instead of the real API (loses adaptivity and accessibility behavior).
- Material chosen because it "looks light gray" instead of by purpose.

## Anomalies in the mirror

- `sheets.md` doesn't mention Liquid Glass (only the watchOS material background) – no HIG statement on glass sheets available.
- `app-icons.md` names the Icon Composer annotations "default, dark, and mono", elsewhere the appearances "default, dark, clear, tinted" – inconsistent terminology.
- `materials.md` mentions `glassEffect(_:in:)` and `Glass.regular/.clear`, but no container or morphing APIs; these details above are therefore marked as framework knowledge.
- The concrete appearance with Reduce Transparency is not specified in the mirror.
