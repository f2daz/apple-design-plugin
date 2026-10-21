# Icons, SF Symbols, App Icons, and Image Assets

Sources (HIG mirror, as of 2026-10-21): `sf-symbols` (updated 2025-07-28, SF Symbols 7), `icons` (2025-06-09), `app-icons` (2026-06-08, Liquid Glass), `images` (2025-12-16), plus `dark-mode`, `right-to-left`, `inclusion`.

## Overview

Three levels that are often confused:

| Level | Purpose | Format | Who designs it |
|---|---|---|---|
| **Interface icon / glyph** | Express a concept in the UI (toolbar, tab bar, menu, button) | SF Symbol or custom vector asset (PDF/SVG), template (black + transparent) | Prefer SF Symbols, otherwise a custom symbol |
| **App icon** | Identity of the app on the Home Screen, Spotlight, Settings, notifications, share sheet | Layered source (Icon Composer or image stack) | Your own design; the system applies Liquid Glass effects on top |
| **Image asset** | Content, illustrations, photos | PNG/JPEG/HEIC/PDF/SVG in an asset catalog, scale factors | Your own design |

Tool in the plugin: **`scripts/sf_symbols.py`** for finding suitable symbol names (e.g. by term or category). Before choosing any symbol, use it to check whether a system symbol exists instead of drawing your own icon. Availability depends on the target OS version – symbols and features of a given release are not available on older systems (hig:sf-symbols).

## Core rules

### SF Symbols
- Use SF Symbols for interface icons; they automatically align with San Francisco in all weights and sizes (hig:sf-symbols).
- **Never** use SF Symbols (or similar-looking images) in app icons, logos, or any other trademark-related use – the license terms prohibit it (hig:sf-symbols).
- Check the rendering mode in every context (size, background contrast); "automatic" provides the preferred mode but does not replace a visual check (hig:sf-symbols#Rendering-modes).
- Use system colors for symbols so they adapt to Dark Mode, vibrancy, and accessibility settings (hig:sf-symbols#Rendering-modes).
- Use Variable Color only for changing values (strength, fill level) – not for depth; depth = Hierarchical (hig:sf-symbols#Variable-color).
- Match the symbol weight to the weight of adjacent text; control emphasis via scale rather than weight (hig:sf-symbols#Weights-and-scales, hig:icons#Best-practices).
- Where possible, let the container decide between outline and fill (iOS tab bar → fill, toolbar → outline) (hig:sf-symbols#Design-variants).
- Animate symbols sparingly and only with a clear message; too many animations are overwhelming (hig:sf-symbols#Animations).
- Do **not** modify symbols that depict Apple products or features – they are copyrighted (marked with an info badge in the SF Symbols app) (hig:sf-symbols#Custom-symbols).
- Give custom symbols and custom interface icons an accessibility description (hig:sf-symbols#Custom-symbols, hig:icons#Best-practices).

### Interface icons
- Design in a highly simplified way with familiar metaphors, directly related to the action or content (hig:icons#Best-practices).
- Keep size, level of detail, stroke weight, and perspective consistent across all icons in the app – including when mixing custom and system icons (hig:icons#Best-practices).
- Center optically, not geometrically; store the correction as padding in the asset (hig:icons#Best-practices).
- Provide a selected variant only when needed – standard components (toolbar, tab bar, buttons) generate the selected state themselves (hig:icons#Best-practices).
- Use gender-neutral figures and imagery that is understood across cultures (hig:icons#Best-practices, hig:inclusion#Gender-identity).
- Text in an icon only when it carries meaning (e.g. text formatting); then localize the characters and mirror text-like elements for RTL (hig:icons#Best-practices).
- Provide custom interface icons as vectors (PDF/SVG); PNG only when necessary, and then in all scale factors (hig:icons#Best-practices).
- Do not replicate Apple hardware; if necessary, use only Apple Design Resources or the corresponding SF Symbols (hig:icons#Best-practices).

### App icons
- Build the icon in layers: background + one or more foreground layers (iOS, iPadOS, macOS, watchOS); the system applies Liquid Glass effects (specular highlights, refraction, translucency) on top (hig:app-icons#Layer-design).
- Provide **unmasked, square** layers (tvOS: rectangular); pre-masked corners degrade highlights and produce jagged edges (hig:app-icons#Icon-shape).
- Keep the primary content centered – especially with a circular mask (watchOS, visionOS) (hig:app-icons#Icon-shape).
- Prefer crisp edges in foreground layers, no soft/feathered edges (hig:app-icons#Layer-design).
- Preferably import layers as vectors (SVG/PDF), convert text to outlines; mesh gradients/raster artwork as PNG (hig:app-icons#Layer-design).
- Background: solid color or gradient directly in Icon Composer; imported backgrounds must be full-bleed and opaque (hig:app-icons#Layer-design).
- No custom shadows, glows, bevels, blurs, or specular highlights – the system applies these dynamically (hig:app-icons#Visual-effects).
- Keep the design simple, with few shapes; illustration rather than photo; do not replicate screenshots or standard UI components (hig:app-icons#Design).
- Text only when essential to the experience or brand; no words like "Watch", "Play", "New", "For visionOS" (hig:app-icons#Design).
- Keep the icon visually consistent across all platforms (hig:app-icons#Design).
- Keep core features the same across all appearance variants; do not swap elements per variant (hig:app-icons#Appearances).
- No replicas of Apple hardware (hig:app-icons#Design).

### Image assets
- Provide every bitmap in all scale factors of the supported devices (hig:images#Resolution).
- Design at the lowest resolution and scale up; place control points of vector shapes on whole values so @2x/@3x stay pixel-accurate (hig:images#Resolution).
- Embed a color profile in every image (hig:images#Best-practices).
- Test on real devices (hig:images#Best-practices).

## Key values and tables

### SF Symbols – rendering modes (hig:sf-symbols#Rendering-modes)

| Mode | Behavior | Typical use |
|---|---|---|
| Monochrome | One color for all layers | Default in text-adjacent contexts |
| Hierarchical | One color, opacity per layer level (primary/secondary/tertiary) | Depth/hierarchy with an accent color |
| Palette | One color per layer; with 2 colors for 3 levels, secondary and tertiary share a color | Matching a color scheme |
| Multicolor | Intrinsic meaningful colors (e.g. `leaf` green, `trash.slash` red) | Reinforce meaning through color |

Layer principle: paths are organized into levels, e.g. `cloud.sun.rain.fill` = cloud (primary), sun (secondary), drops (tertiary).

**Gradients** (SF Symbols 7 and later): linear gradient from a single source color, in all modes, for system and custom colors as well as custom symbols; works best at large sizes (hig:sf-symbols#Gradients).

**Variable Color:** Colors layers depending on a threshold between 0 and 100 %. Individual layers can be excluded (e.g. the speaker body in `speaker.wave.3`) (hig:sf-symbols#Variable-color).

### SF Symbols – weights and scales (hig:sf-symbols#Weights-and-scales)

| Attribute | Values |
|---|---|
| Weights | 9, from Ultralight to Black, each corresponding to an SF font weight |
| Scales | Small, Medium (default), Large – relative to the cap height of SF |
| Design variants | Outline (most common), Fill, Slash, Enclosed (circle/square/rectangle); can be combined |
| Language/script variants | Including Latin, Arabic, Hebrew, Hindi, Thai, Chinese, Japanese, Korean, Cyrillic, Devanagari, Indic numeral systems; switch automatically with the device language |

Variant rules of thumb: outline next to text (toolbar, list); enclosed improves legibility at small sizes; fill for more weight (iOS tab bar, swipe actions, selection with accent color); slash for "unavailable".

### SF Symbols – animations (hig:sf-symbols#Animations)

| Effect | Behavior | Use |
|---|---|---|
| Appear / Disappear | Symbol appears/disappears gradually | Showing/hiding |
| Bounce | Brief elastic scaling, returns to original; once by default | "Action has happened / is needed" |
| Scale | Size change, persists until reset | Highlight a selection |
| Pulse | Opacity varies (only annotated layers or all) | Ongoing activity |
| Variable Color | Layer opacity step by step; cumulative or iterative; optionally autoreverse, hide inactive layers; open loop vs. closed loop | Progress, connecting, sending, playback |
| Replace | Swap of two symbols; variants Down-Up, Up-Up (progress), Off-Up (next state emphasized) | State change |
| Magic Replace | Smart transition between related shapes (slash draws, badge appears); default replace, falls back to Down-Up for unrelated symbols | Play/pause, mic/mic-slash |
| Wiggle | Back-and-forth along an axis | Emphasize an easily overlooked call to action |
| Breathe | Opacity **and** size pulse | Ongoing recording, status |
| Rotate | Whole symbol or parts (By Layer, e.g. fan blades) | Ongoing process |
| Draw On / Draw Off | Draws along guide points (SF Symbols 7 and later); all layers, staggered or individually | Progress (download), direction |

Playback is configurable: once or repeating until a condition is met, speed, reverse before repeating. Animations apply to all modes, weights, scales, and custom symbols. Animations only with SF Symbols 5 or later (hig:motion#Providing-feedback).

### Standard symbols for common actions (selection, hig:icons#Standard-icons)

| Action | Symbol |
|---|---|
| Cut / Copy / Paste | `scissors` / `document.on.document` / `document.on.clipboard` |
| Done, Save | `checkmark` |
| Cancel, Close, Deselect | `xmark` |
| Delete | `trash` |
| Undo / Redo | `arrow.uturn.backward` / `arrow.uturn.forward` |
| Compose | `square.and.pencil` |
| Duplicate | `plus.square.on.square` |
| Rename | `pencil` |
| Move to, Folder | `folder` |
| Attach / Add / More | `paperclip` / `plus` / `ellipsis` |
| Select | `checkmark.circle` |
| Bold / Italic / Underline | `bold` / `italic` / `underline` |
| Superscript / Subscript | `textformat.superscript` / `textformat.subscript` |
| Align Left / Center / Justified / Right | `text.alignleft` / `text.aligncenter` / `text.justify` / `text.alignright` |
| Search | `magnifyingglass` |
| Find (incl. Replace, Next, Previous, Use Selection) | `text.page.badge.magnifyingglass` |
| Filter | `line.3.horizontal.decrease` |
| Share, Export | `square.and.arrow.up` |
| Print | `printer` |
| Account, User, Profile | `person.crop.circle` |
| Like / Dislike | `hand.thumbsup` / `hand.thumbsdown` |
| Bring to Front / Send to Back | `square.3.layers.3d.top.filled` / `square.3.layers.3d.bottom.filled` |
| Bring Forward / Send Backward | `square.2.layers.3d.top.filled` / `square.2.layers.3d.bottom.filled` |
| Alarm / Archive / Calendar | `alarm` / `archivebox` / `calendar` |

Note: Several names (`document.on.document`, `text.page.badge.magnifyingglass`) are recent renames; for older deployment targets, check availability with `scripts/sf_symbols.py` or the SF Symbols app.

### App icon specifications (hig:app-icons#Specifications)

| Platform | Layout shape | Shape after masking | Layout size | Style | Appearance variants |
|---|---|---|---|---|---|
| iOS, iPadOS, macOS | Square | Rounded rectangle (square) | 1024x1024 px | Layered | Default, Dark, Clear Light, Clear Dark, Tinted Light, Tinted Dark |
| tvOS | Rectangle (landscape) | Rounded rectangle | 800x480 px | Layered (parallax, 2–5 layers) | – |
| visionOS | Square | Circle | 1024x1024 px | Layered (3D, background + 1–2 layers) | – |
| watchOS | Square | Circle | 1088x1088 px | Layered | – |

- The system automatically scales smaller variants (Settings, notifications).
- Color spaces: sRGB, Gray Gamma 2.2, Display P3 (wide gamut; not visionOS).
- The system generates any appearance variants you don't provide (hig:app-icons#Appearances).
- Alternate app icons (iOS, iPadOS, tvOS, compatible apps in visionOS) each need their own dark, clear, and tinted variants in iOS/iPadOS; all are subject to App Review (hig:app-icons#Appearances).

### Icon Composer – workflow (hig:app-icons#Layer-design)

1. Create foreground layers in your own design tool (vector, crisp edges, fully opaque at first).
2. Import into Icon Composer (part of Xcode, also available separately from Apple Developer).
3. Define the background (color/gradient), adjust layer positions.
4. Apply effects: specular highlights, refraction, translucency; vary the opacity of foreground layers for depth.
5. Group layers when effects should apply at group level (groups offer additional Liquid Glass options).
6. Annotate appearance variants, preview across system versions, export to Xcode.

tvOS/visionOS: layers instead as an image stack in the asset catalog; Parallax Previewer / Parallax Exporter from Apple Design Resources.

The **compose-app-icon** skill is available for creating and validating `.icon` packages.

### Appearance variants (Light/Dark/Clear/Tinted) (hig:app-icons#Appearances)

| Variant | Design guidance |
|---|---|
| Default | Base design |
| Dark | Derive from the light icon; complementary colors, no overly bright images; colored backgrounds usually give the best contrast |
| Clear (Light/Dark) | Even more restrained than Dark; the shape must work without color |
| Tinted (Light/Dark) | Also heavily muted; recognizability via silhouette |

All variants: visible, legible, recognizable; should look cohesive next to system icons and widgets.

### Image resolutions (hig:images#Resolution)

| Platform | Scale factors |
|---|---|
| iOS | @2x and @3x |
| iPadOS, watchOS | @2x |
| macOS, tvOS | @1x and @2x |
| visionOS | @2x or higher; above @6x noticeable performance cost, set high-quality filtering for > @2x |

### Image formats (hig:images#Formats)

| Image type | Format |
|---|---|
| Bitmap/raster | De-interlaced PNG |
| PNG without need for 24-bit | 8-bit palette |
| Photos | JPEG (optimized) or HEIC |
| Stereo/spatial photos | Stereo HEIC |
| Flat icons, interface icons, scalable flat artwork | PDF or SVG |

### macOS – document icons (hig:icons#Document-icons)

| Element | Sizes |
|---|---|
| Background fill | 512x512 @1x / 1024x1024 @2x · 256 / 512 · 128 / 256 · 32 / 64 · 16 / 32 px |
| Center image (half the canvas size) | 256x256 @1x / 512x512 @2x · 128 / 256 · 32 / 64 · 16 / 32 px |
| Margin in the center image | approx. 10 % of the canvas; motif approx. 80 % (e.g. ~205x205 in 256x256) |

- Without a custom document icon, macOS composes the app icon + file extension.
- Keep the top-right corner clear (the system draws the folded corner over it).
- Simplify small sizes (e.g. reduce grid lines, omit them at 16x16).
- Optionally a short term instead of an unfamiliar extension (e.g. "scene" instead of "scn"); the system capitalizes and scales it.

### watchOS – autoscaling PDFs (hig:images#watchOS)

Design for 40 mm and 42 mm at @2x; WatchKit scales:

| Screen | Scaling |
|---|---|
| 38 mm | 90 % |
| 40 mm | 100 % |
| 41 mm | 106 % |
| 42 mm | 100 % |
| 44 mm | 110 % |
| 45 mm | 119 % |
| 49 mm | 119 % |

## Platform differences

| Topic | iOS / iPadOS | macOS | watchOS |
|---|---|---|---|
| App icon mask | Rounded square | Rounded square (same specification as iOS) | Circle – center content strictly |
| App icon size | 1024x1024 px | 1024x1024 px | 1088x1088 px |
| Appearance variants | Default, Dark, Clear, Tinted | Default, Dark, Clear, Tinted | none |
| Special considerations | Alternate app icons possible (with their own variants) | Document icons for custom file types | No black icon background (merges with the display) |
| Image scale | iOS @2x+@3x, iPadOS @2x | @1x+@2x | @2x, autoscaling PDF; transparency only where needed (template images, complications), otherwise bake in the background |
| Symbol variants | Tab bar uses fill | Toolbar/sidebar mostly outline | Compact presentation, enclosed helps at the smallest sizes |

## Implementation

### SwiftUI
```swift
Image(systemName: "cloud.sun.rain.fill")
    .symbolRenderingMode(.hierarchical)      // .monochrome / .palette / .multicolor
    .foregroundStyle(.tint)
    .imageScale(.large)                      // small / medium / large
    .font(.body.weight(.semibold))           // weight follows font

Image(systemName: "wifi", variableValue: signal) // Variable Color 0.0–1.0

Image(systemName: "bell")
    .symbolEffect(.bounce, value: count)     // discrete effect on value change
Image(systemName: isMuted ? "mic.slash" : "mic")
    .contentTransition(.symbolEffect(.replace))

Label("Share", systemImage: "square.and.arrow.up")    // text + symbol, VoiceOver label included
Image("CustomGlyph").accessibilityLabel("Counter")      // label a custom symbol
Image(decorative: "Ornament")                           // purely decorative
```

### UIKit
```swift
let config = UIImage.SymbolConfiguration(textStyle: .body, scale: .large)
    .applying(UIImage.SymbolConfiguration(paletteColors: [.systemBlue, .systemGray]))
imageView.image = UIImage(systemName: "speaker.wave.3", withConfiguration: config)
imageView.addSymbolEffect(.pulse)               // iOS 17+
```

### AppKit
```swift
let config = NSImage.SymbolConfiguration(textStyle: .body, scale: .medium)
let image = NSImage(systemSymbolName: "trash", accessibilityDescription: "Delete")?
    .withSymbolConfiguration(config)
```

Notes: Symbol effects are available from SF Symbols 5 (iOS 17 / macOS 14 / watchOS 10); Draw On/Off and gradients from SF Symbols 7 – check the deployment target. Custom symbols: export the template of a similar system symbol from the SF Symbols app, adapt it in a vector tool, annotate it in the app.

## Custom symbols – process (hig:sf-symbols#Custom-symbols)

- [ ] Export the most similar system symbol as a template; adopt its level of detail, optical weight, alignment, and perspective.
- [ ] Goals: simple, recognizable, inclusive, directly related to the action/content.
- [ ] Annotate layers (color or hierarchy level) for the desired rendering modes.
- [ ] For badges/added width, set negative side margins; naming follows the pattern `left-margin-Regular-M`.
- [ ] For animations, draw whole shapes and annotate gaps as erase layers (instead of cutouts); define the z-order for Variable Color; use layer groups.
- [ ] Test with **all** animation presets.
- [ ] Don't draw enclosures/badges; generate them via the component library of the SF Symbols app.
- [ ] Define directionality for RTL (hig:right-to-left).
- [ ] Assign an accessibility label.
- [ ] Don't replicate Apple products; don't modify Apple feature symbols.

## Review checklist

**Interface icons and symbols**
- [ ] The standard symbol from the table is used for every standard action (cross-checked with `scripts/sf_symbols.py`).
- [ ] Symbol weight matches the adjacent text; emphasis via scale, not via a weight mismatch.
- [ ] Rendering mode checked in Light, Dark, and Increase Contrast and at the smallest size.
- [ ] Variable Color only for changing values.
- [ ] Animations have a clear purpose, few at a time, match the tone; Reduce Motion respected (see `motion-and-feedback.md`).
- [ ] Custom icons: vector (PDF/SVG), optically centered, consistent stroke weight, accessibility label.
- [ ] No SF Symbols in the app icon, logo, or brand.
- [ ] No modified Apple product/feature symbols, no hardware replicas.
- [ ] Icons with reading direction mirrored for RTL, or system variants used.

**App icon**
- [ ] Layered source in Icon Composer (iOS/iPadOS/macOS/watchOS) or image stack (tvOS/visionOS).
- [ ] Layers square, unmasked, vector; text converted to outlines.
- [ ] No baked-in shadows, glows, highlights, blurs.
- [ ] Main motif centered, works in a circular mask (watchOS).
- [ ] Default/Dark/Clear/Tinted variants checked; core features identical.
- [ ] watchOS: no black background.
- [ ] No photos, screenshots, UI replicas, superfluous words.
- [ ] Alternate icons (if any) with their own variants.

**Images**
- [ ] All scale factors per platform present.
- [ ] Color profile embedded; formats as per the table.
- [ ] Light/dark variants where needed (e.g. darken white image backgrounds in Dark Mode) (hig:dark-mode#Icons-and-images).
- [ ] Checked on real devices.

## Anti-patterns

- SF Symbol (e.g. `bolt.fill`) as the app logo or in the app icon.
- Pre-masked, rounded PNG as an app icon layer → jagged edges, broken highlights.
- Baked-in drop shadows/gloss in the icon that clash with Liquid Glass effects.
- Dark icon that swaps elements or shows a different motif.
- Self-drawn variants with badge/circle instead of the component library.
- Variable Color as a decorative gradient for depth.
- Permanently repeating wiggle/bounce effects without meaning.
- Only PNG @1x for an interface icon.
- Different stroke weights between custom and system icons.
- Male default figure for "person".
- Apple hardware replicated in the icon.

## Ambiguities / contradictions in the mirror

- **Appearance variants:** `app-icons#Layer-design` names "default, dark, and mono" for Icon Composer, while the *Appearances* and *Specifications* sections name "default, dark, clear, tinted" (specification: Clear Light/Dark, Tinted Light/Dark). Presumably "mono" is the basis for Clear/Tinted; the specification table is authoritative.
- **watchOS 42 mm = 100 %** in the autoscaling table, although 41 mm is at 106 %; the Apple document names 40 mm and 42 mm as the design basis. Values adopted as-is, not interpolated.
- **App icon macOS:** The platform section states "no additional considerations" for macOS; macOS specifics appear only under document icons (`icons`).
- The HIG does not specify concrete point sizes for symbol scales – they are defined relative to the cap height.
