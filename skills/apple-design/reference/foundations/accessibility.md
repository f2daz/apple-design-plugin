# Accessibility

Sources (HIG mirror, as of 2026-10-21): `accessibility` (updated 2025-06-09: Assistive Access, Switch Control, Accessibility Nutrition Labels), `voiceover` (2025-03-07), `inclusion`, `typography` (Dynamic Type), `color`, `dark-mode`, `materials`, `motion`, `buttons`, `right-to-left`.

## Overview

Apple describes an accessible interface as **intuitive** (familiar, consistent interactions), **perceivable** (information never conveyed through only one channel), and **adaptable** (system accessibility features and personal settings are respected) (hig:accessibility). The HIG is organized into Vision, Hearing, Mobility, Speech, Cognitive. Disability is a spectrum and can be permanent, temporary, or situational (hig:inclusion#Accessibility).

Testing tool: **Accessibility Inspector** (Xcode). The result can be declared on the App Store via **Accessibility Nutrition Labels** (App Store Connect) (hig:accessibility).

## Core rules

### Vision
- Support larger text sizes: aim for at least **200 %** enlargement (watchOS **140 %**), via Dynamic Type or your own UI (hig:accessibility#Vision).
- Respect the platform-specific default and minimum font sizes, including with custom fonts; choose larger sizes for thin weights (hig:accessibility#Vision, hig:typography#Ensuring-legibility).
- Avoid Ultralight, Thin, Light – especially for small text (hig:typography#Ensuring-legibility).
- Meet minimum contrast ratios (table below) in Light **and** Dark; if the default isn't sufficient, provide a higher-contrast scheme at least for **Increase Contrast** (hig:accessibility#Vision).
- Prefer system colors – they include variants for Dark Mode and Increase Contrast; custom colors need Light, Dark, and an increased-contrast variant for each (hig:color#Best-practices).
- Never convey information through color alone; add shape, symbol, text (problematic: red-green, blue-orange). Where appropriate, offer customizable color schemes (charts, game pieces) (hig:accessibility#Vision, hig:color#Inclusive-color).
- Describe UI and content for VoiceOver (hig:voiceover).
- Test Dark Mode with Increase Contrast and Reduce Transparency – individually and combined (hig:dark-mode#Best-practices).
- Check Liquid Glass (regular/clear) with Reduce Transparency and Increase Contrast; the appearance changes with these settings (hig:materials).
- Let interface-relevant icons scale with the font size (SF Symbols scale automatically) (hig:typography#Supporting-Dynamic-Type).
- Custom fonts must support Dynamic Type and **Bold Text** themselves; system fonts do this automatically (hig:typography#Using-custom-fonts).

### VoiceOver
- Provide labels for all essential elements; replace default labels of system controls with ones that describe the function, always label custom elements, keep labels up to date (hig:voiceover#Descriptions).
- Describe meaningful images – only what the image itself conveys, not the adjacent caption (hig:voiceover#Descriptions).
- Make charts/infographics fully accessible: concise overall description, interactive details also reachable via VoiceOver (hig:voiceover#Descriptions).
- Hide purely decorative images (hig:voiceover#Descriptions).
- Provide unique screen titles and correct headings (hig:voiceover#Navigation).
- Group related elements (image + caption) and define order/relationships where they are only visually apparent (hig:voiceover#Navigation).
- Announce visible content and layout changes to VoiceOver (hig:voiceover#Navigation).
- Support the rotor (headings, links, custom content types) (hig:voiceover#Navigation).

### Hearing
- Never convey dialogue and important information through audio alone; offer captions, subtitles, audio descriptions, transcripts depending on the medium (hig:accessibility#Hearing).
- Combine audio cues with haptics; in iOS/iPadOS Music Haptics and Audio Graphs are also available (hig:accessibility#Hearing).
- Supplement audio cues with visual cues, especially for content outside the screen (games, spatial) (hig:accessibility#Hearing).

### Mobility
- Respect minimum control sizes (table below); buttons need a hit target of at least 44x44 pt, 60x60 pt in visionOS (hig:accessibility#Mobility, hig:buttons#Best-practices).
- Spacing is as important as size: approx. **12 pt** padding around elements with a bezel, approx. **24 pt** around elements without a bezel (hig:accessibility#Mobility).
- Use the simplest gesture for frequent interactions; no custom multi-finger/multi-hand gestures (hig:accessibility#Mobility).
- Provide an on-screen alternative for every gesture (e.g. a button in addition to swipe-to-dismiss) (hig:accessibility#Mobility).
- Label elements so that **Voice Control** can address them by voice (hig:accessibility#Mobility).
- Integrate Siri and Shortcuts for recurring tasks (including the Action button) (hig:accessibility#Mobility).
- Test with VoiceOver, AssistiveTouch, Full Keyboard Access, Pointer Control, Switch Control (hig:accessibility#Mobility).

### Speech / input
- Enable complete operation via keyboard (**Full Keyboard Access**); don't override system-wide keyboard shortcuts (hig:accessibility#Speech).
- Support **Switch Control** (external switches, game controllers, sounds) for selecting, tapping, typing text, drawing (hig:accessibility#Speech).

### Cognitive
- Keep actions simple and consistent; system gestures before custom ones (hig:accessibility#Cognitive).
- Avoid UI that disappears on a timer; dismiss via an explicit action (hig:accessibility#Cognitive).
- No autoplay of audio/video without start/stop controls; consider a global opt-out setting (hig:accessibility#Cognitive).
- Respond to **Dim Flashing Lights** during video playback (hig:accessibility#Cognitive).
- Respond to **Reduce Motion**: reduce automatic and repeating animations (zoom, scaling, peripheral motion) (hig:accessibility#Cognitive) – details in `motion-and-feedback.md`.
- Optimize for **Assistive Access** (iOS/iPadOS): identify core functions, remove secondary paths, split multistep flows into one step per screen, require double confirmation for actions that are hard to undo (hig:accessibility#Cognitive).
- In games, offer difficulty adjustments (criteria, reaction time, control assistance) (hig:accessibility#Cognitive).

### Inclusion
- No images/language that exclude people with disabilities or use disability as a negative metaphor; write people-first (hig:inclusion#Accessibility).
- Don't assume that a disability prevents someone from using the app (hig:inclusion#Accessibility).

## Key values

### Font sizes default / minimum (hig:accessibility#Vision, hig:typography#Ensuring-legibility)

| Platform | Default | Minimum |
|---|---|---|
| iOS, iPadOS | 17 pt | 11 pt |
| macOS | 13 pt | 10 pt |
| tvOS | 29 pt | 23 pt |
| visionOS | 17 pt | 12 pt |
| watchOS | 16 pt | 12 pt |

### Contrast (Accessibility Inspector, WCAG Level AA) (hig:accessibility#Vision)

| Text size | Weight | Minimum contrast |
|---|---|---|
| up to 17 pt | all | 4.5:1 |
| 18 pt and above | all | 3:1 |
| all | Bold | 3:1 |

Addition from `dark-mode#Dark-Mode-colors`: at least 4.5:1; with custom foreground/background colors **aim for 7:1**, especially for small text. Apple names WCAG and APCA as measurement methods.

### Control sizes (hig:accessibility#Mobility)

| Platform | Default | Minimum |
|---|---|---|
| iOS, iPadOS | 44x44 pt | 28x28 pt |
| macOS | 28x28 pt | 20x20 pt |
| tvOS | 66x66 pt | 56x56 pt |
| visionOS | 60x60 pt | 28x28 pt |
| watchOS | 44x44 pt | 28x28 pt |

Spacing: ~12 pt around elements with a bezel, ~24 pt around bezel-less elements (measured from the visible edge).

### Dynamic Type – Body style as reference (hig:typography#Specifications)

| Size | iOS/iPadOS Body (pt / leading) | watchOS Body (pt / leading) |
|---|---|---|
| xSmall | 14 / 19 | 14 / 16.5 |
| Small | 15 / 20 | 15 / 17.5 (default 38 mm) |
| Medium | 16 / 21 | – |
| Large | **17 / 22 (default)** | 16 / 18.5 (default 40/41/42 mm) |
| xLarge | 19 / 24 | 17 / 19.5 (default 44/45/49 mm) |
| xxLarge | 21 / 26 | 18 / 20.5 |
| xxxLarge | 23 / 29 | 19 / 21.5 |
| AX1 | 28 / 34 | 21 / 23.5 |
| AX2 | 33 / 40 | 22 / 24.5 |
| AX3 | 40 / 48 | 23 / 25.5 |
| AX4 | 47 / 56 | – |
| AX5 | 53 / 62 | – |

Complete style tables: `typography` reference. Dynamic Type is available in iOS, iPadOS, tvOS, visionOS, watchOS – **not in macOS** (hig:typography#macOS).

### System settings an app must respond to

| Setting | Expected response | Source |
|---|---|---|
| Larger Text / Dynamic Type incl. AX sizes | Layout scales, minimal truncation, stacked layout if needed, fewer columns | hig:typography#Supporting-Dynamic-Type |
| Bold Text | Custom fonts provide a bolder weight | hig:typography#Using-custom-fonts |
| Increase Contrast | Custom colors with increased-contrast variants; system colors adapt | hig:color#Best-practices |
| Reduce Transparency | Materials/Liquid Glass become more opaque; check legibility | hig:materials, hig:dark-mode#Best-practices |
| Reduce Motion | Reduce motion, fades instead of movement | hig:accessibility#Cognitive |
| Dim Flashing Lights | Video playback responds | hig:accessibility#Cognitive |
| Dark Mode | Both appearances legible, check contrast in both | hig:dark-mode |
| VoiceOver | Labels, order, groups, notifications, rotor | hig:voiceover |
| Voice Control | Visible, unique labels | hig:accessibility#Mobility |
| Switch Control, Full Keyboard Access, AssistiveTouch, Pointer Control | All functions reachable without touch gestures | hig:accessibility#Mobility, #Speech |
| Assistive Access | Reduced, single-step interface | hig:accessibility#Cognitive |

Not covered in the mirror, but present in the system: Button Shapes, Smart Invert, Differentiate Without Color, On/Off Labels – the HIG pages give no specific rules for these; in practice, query them via the APIs listed below and avoid relying on color alone.

## Platform differences

| Topic | iOS / iPadOS | macOS | watchOS |
|---|---|---|---|
| Dynamic Type | yes, 7 standard + 5 AX sizes | **no** – custom scaling or system font sizes/variants (`NSFont` dynamic variants) | yes, 6 standard + 3 AX sizes; default depends on case size |
| Enlargement target | 200 % | 200 % (via your own UI) | 140 % |
| Default/min text | 17 / 11 pt | 13 / 10 pt | 16 / 12 pt |
| Control default/min | 44 / 28 pt | 28 / 20 pt | 44 / 28 pt |
| Dark Mode | yes (base/elevated backgrounds) | yes (desktop tinting) | no Dark Mode (always dark) |
| Input alternatives | Voice Control, Switch Control, AssistiveTouch, Full Keyboard Access | Full Keyboard Access, Voice Control, Switch Control, Pointer Control | VoiceOver, Siri/Shortcuts, Action button, Digital Crown |
| Assistive Access | yes | – | – |
| Special considerations | Music Haptics, Audio Graphs | Keyboard navigation is central, don't override system shortcuts | Short interactions, no time-critical UIs |

visionOS (for completeness): Pointer Control (head/hand), Zoom; prioritize comfort (content within the field of view, horizontal rather than vertical layouts, no head-anchored content, no large repetitive gestures); with VoiceOver, custom gestures don't receive hand input by default (Direct Gesture Mode) (hig:accessibility#visionOS, hig:voiceover#visionOS).

## Implementation

### SwiftUI
```swift
// Labels, values, hints
Button(action: share) { Image(systemName: "square.and.arrow.up") }
    .accessibilityLabel("Share")
    .accessibilityHint("Opens sharing options")        // use sparingly
Slider(value: $volume).accessibilityValue("\(Int(volume * 100)) percent")
Image(decorative: "Background")                        // hide from VoiceOver
Text("Settings").accessibilityAddTraits(.isHeader)

// Grouping / order
VStack { Image(photo); Text(caption) }
    .accessibilityElement(children: .combine)
.accessibilitySortPriority(1)

// Voice Control: alternative voice commands
.accessibilityInputLabels(["Send", "Submit"])

// Custom actions instead of swipe-only
.accessibilityAction(named: "Delete") { delete() }

// Rotor
.accessibilityRotor("Headings") { ... }

// Announce changes
AccessibilityNotification.Announcement("Download complete").post()

// Query settings
@Environment(\.dynamicTypeSize) var typeSize          // typeSize.isAccessibilitySize
@Environment(\.accessibilityReduceMotion) var reduceMotion
@Environment(\.accessibilityReduceTransparency) var reduceTransparency
@Environment(\.colorSchemeContrast) var contrast       // .increased
@Environment(\.legibilityWeight) var weight            // .bold with Bold Text
@Environment(\.accessibilityDifferentiateWithoutColor) var noColorOnly

// Custom font with Dynamic Type
.font(.custom("BrandSans", size: 17, relativeTo: .body))
@ScaledMetric(relativeTo: .body) var iconSize = 24
```

### UIKit
```swift
button.accessibilityLabel = "Share"
imageView.isAccessibilityElement = false                 // decorative
label.font = UIFontMetrics(forTextStyle: .body).scaledFont(for: brandFont)
label.adjustsFontForContentSizeCategory = true
label.numberOfLines = 0                                  // avoid truncation
if traitCollection.preferredContentSizeCategory.isAccessibilityCategory { /* stacked layout */ }
UIAccessibility.post(notification: .layoutChanged, argument: firstElement)
UIAccessibility.isReduceMotionEnabled / .isReduceTransparencyEnabled
UIAccessibility.isBoldTextEnabled / .isDarkerSystemColorsEnabled
view.shouldGroupAccessibilityChildren = true
let rotor = UIAccessibilityCustomRotor(name: "Headings") { ... }
```

### AppKit
```swift
button.setAccessibilityLabel("Share")
NSWorkspace.shared.accessibilityDisplayShouldReduceMotion
NSWorkspace.shared.accessibilityDisplayShouldReduceTransparency
NSWorkspace.shared.accessibilityDisplayShouldIncreaseContrast
NSAccessibility.post(element: view, notification: .layoutChanged)
NSAccessibilityCustomRotor(label: "Headings", itemSearchDelegate: self)
```

Note: The API names above come from the Apple SDK, not from the HIG mirror; the mirror references `accessibilityHidden(_:)`, `accessibilityElement`, `isAccessibilityElement`, `shouldGroupAccessibilityChildren`, `AccessibilityNotification`, `AccessibilityRotorEntry`, `UIAccessibilityCustomRotor`, `NSAccessibilityCustomRotor`, `isAccessibilityCategory`, `numberOfLines`.

## Audit checklist

**Vision**
- [ ] All text uses text styles / scaled fonts; AX5 (iOS) or AX3 (watchOS) without truncated core content.
- [ ] Layout switches to stacked at AX sizes; column count reduced; hierarchy stays at the top.
- [ ] No text below the platform minimum; no Light/Thin weights for small text.
- [ ] Contrast ≥ 4.5:1 (≤ 17 pt) or ≥ 3:1 (≥ 18 pt or Bold) in Light **and** Dark; custom colors target 7:1.
- [ ] Increase Contrast provides visibly stronger differentiation (custom colors with HC variant).
- [ ] Reduce Transparency: text on materials/Liquid Glass remains legible.
- [ ] Bold Text also takes effect with custom fonts.
- [ ] States/errors not conveyed by color alone (additionally symbol, text, shape).
- [ ] Meaningful icons scale with the font size.

**VoiceOver**
- [ ] Every interactive element has a functional label (no "Button", no file name).
- [ ] Decorative images hidden; content images described.
- [ ] Title unique per screen, headings marked as headers.
- [ ] Reading order logical; image + caption grouped.
- [ ] Dynamic changes (loading finished, errors, layout changes) are announced.
- [ ] Charts with summary and navigable data points.
- [ ] Custom controls with value, traits, and adjustable/custom actions.

**Mobility / input**
- [ ] Hit targets ≥ 44x44 pt (iOS/iPadOS/watchOS), ≥ 28x28 pt (macOS default), ≥ 60x60 pt (visionOS); minimums not undercut.
- [ ] Spacing ~12 pt (with bezel) / ~24 pt (without bezel).
- [ ] Every gesture has a visible alternative (button, menu, custom action).
- [ ] No mandatory multi-finger gestures for core functions.
- [ ] Voice Control: all elements reachable via "Tap <name>".
- [ ] Full Keyboard Access / tab order complete; system shortcuts not overridden.
- [ ] Switch Control reaches all functions.

**Hearing**
- [ ] Subtitles/captions/transcripts for audio and video content.
- [ ] Audio signals additionally visual and haptic.

**Cognitive / motion**
- [ ] No automatically disappearing notices that require action.
- [ ] No autoplay without controls.
- [ ] Reduce Motion: no zoom/parallax/bounce effects, fades instead of slides.
- [ ] Dim Flashing Lights respected during video playback.
- [ ] Assistive Access (if relevant): core flows single-step, destructive actions double-confirmed.

**Process**
- [ ] Accessibility Inspector audit without open findings.
- [ ] Test with real settings (Larger Text, Bold Text, Increase Contrast, Reduce Transparency, Reduce Motion, VoiceOver) – individually and combined.
- [ ] Accessibility Nutrition Labels maintained in App Store Connect.

## Anti-patterns

- Fixed font sizes (`.system(size: 15)`) without `relativeTo`/`UIFontMetrics`.
- `lineLimit(1)` on content text → truncation at large sizes.
- Icon buttons without a label ("Button, image" in VoiceOver).
- Status only as a red/green dot.
- Gray text on Liquid Glass without checking with Reduce Transparency.
- Swipe-to-delete as the only way to delete.
- Toasts/banners that disappear after a few seconds and contain an action.
- App-specific light/dark toggle instead of the system setting (hig:dark-mode#Best-practices).
- Small tap targets packed closely together (e.g. 24-pt icons without padding).
- Decorative images with alt text that slow down VoiceOver users.
- Overriding system shortcuts (e.g. Cmd-Tab-like bindings) in macOS.

## Ambiguities / contradictions in the mirror

- **Hit target macOS:** `buttons#Best-practices` generally states at least 44x44 pt (visionOS 60x60), while `accessibility#Mobility` states 28x28 pt default and 20x20 pt minimum for macOS. For macOS the platform-specific table applies; the 44-pt rule is geared toward touch.
- **Contrast:** `accessibility` states 4.5:1 or 3:1 (WCAG AA), `dark-mode` additionally 7:1 as a target for custom colors. Not a contradiction, but two levels: 4.5:1 = mandatory minimum, 7:1 = recommendation.
- **17/18 pt threshold:** The table jumps from "up to 17 pt" to "18 pt"; intermediate values (e.g. 17.5 pt) are not covered.
- **200 % target vs. actual scale:** iOS Body grows from 17 to 53 pt (AX5), watchOS Body from 16 to 23 pt (AX3) – the 200 % / 140 % targets are minimum requirements for custom solutions, not system limits.
