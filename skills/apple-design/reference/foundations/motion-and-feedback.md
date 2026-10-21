# Motion, Haptics, and Feedback

Sources (HIG mirror, as of 2026-10-21): `motion` (updated 2025-09-09, Liquid Glass), `playing-haptics` (2024-05-07, Apple Pencil Pro), `feedback`, `loading` (2025-06-09), `launching` (2024-06-10), `progress-indicators`, `accessibility#Cognitive` (Reduce Motion), `sf-symbols#Animations`, `digital-crown`, `alerts`.

## Overview

Motion, haptics, sound, and status indicators form one shared feedback system: they show status, confirm results, warn about consequences, and help with corrections (hig:feedback). Principle: **weight of the feedback = weight of the information** – status passive and close to the object, impending data loss interrupting (hig:feedback). System components already include motion and haptics and adapt them to the input method and accessibility settings (e.g. Liquid Glass responds more strongly to direct touch than to a trackpad) (hig:motion). Custom motion only as a supplement.

**Important:** The HIG specifies **no duration or curve values** (ms, spring parameters) for app animations. The only numbers in the mirror: 30–60 fps for games (hig:motion#Leveraging-platform-capabilities) and ~0.2 Hz as an oscillation frequency to avoid in visionOS (hig:motion#visionOS). Don't invent millisecond values – use system animations/default springs.

## Core rules

### Motion
- Use motion purposefully; no animation for its own sake – excessive animation is distracting and can cause physical discomfort (hig:motion#Best-practices).
- Make motion optional: never convey important information through motion alone; add haptics and audio (hig:motion#Best-practices).
- Feedback motion follows the gesture and expectations (what slides in from the top doesn't exit to the side) (hig:motion#Providing-feedback).
- Keep feedback animations brief and precise (hig:motion#Providing-feedback).
- Don't add extra motion to frequent UI interactions in apps; the system already animates standard elements (hig:motion#Providing-feedback).
- Make motion cancelable; nobody should have to wait for an animation to finish, especially when it repeats (hig:motion#Providing-feedback).
- Use animated SF Symbols where they convey information efficiently (SF Symbols 5 and later) (hig:motion#Providing-feedback, hig:sf-symbols#Animations).
- Games: target a consistent 30–60 fps, sensible default graphics settings per device, selectable performance/battery modes (hig:motion#Leveraging-platform-capabilities).

### Reduce Motion (hig:accessibility#Cognitive)
- When Reduce Motion is on, reduce automatic and repetitive animations, particularly zoom, scaling, peripheral motion.
- Tighten springs (less bounce).
- Tie animations directly to the gesture.
- Don't animate depth changes in z-planes.
- Replace x/y/z transitions with fades.
- Don't animate into/out of blur.
- Be careful with fast and flashing animations (dizziness, in extreme cases epileptic seizures) – regardless of Reduce Motion.

### Haptics
- Use system haptics only in their documented meaning; if none fits, use a generic or custom pattern (hig:playing-haptics#Best-practices).
- Use haptics consistently and causally: same pattern = same kind of event (never the same pattern for success and failure) (hig:playing-haptics#Best-practices).
- Use haptics to complement visuals and sound; match intensity and sharpness to the accompanying animation (hig:playing-haptics#Best-practices).
- Don't overdo it – the best haptics are barely noticeable, but missed when turned off (hig:playing-haptics#Best-practices).
- In apps, prefer short haptics for discrete events; long/continuous ones rather in games (be especially restrained on Apple Pencil Pro) (hig:playing-haptics#Best-practices).
- Make haptics optional; the app must be fully usable without them (hig:playing-haptics#Best-practices).
- Check interactions with the camera, gyroscope, microphone (hig:playing-haptics#Best-practices).
- Combine audio cues with matching haptics for people who can't perceive sound (hig:accessibility#Hearing).

### Feedback in general
- Make feedback accessible through multiple channels: color, text, sound, haptics – it then also works when muted, when looking away, and with VoiceOver (hig:feedback#Best-practices).
- Integrate status information close to the affected element (e.g. Mail: unread count in the toolbar) (hig:feedback#Best-practices).
- Use alerts only for critical, ideally actionable information (hig:feedback#Best-practices, hig:alerts#Best-practices).
- Warn about **unexpected and irreversible** data loss – not when loss is the expected outcome (Finder doesn't warn on every delete) (hig:feedback#Best-practices).
- Confirm completion only for truly significant actions (e.g. an Apple Pay payment); otherwise report only failure (hig:feedback#Best-practices).
- Explain why a command can't be carried out (hig:feedback#Best-practices).

### Loading and progress
- Show something as early as possible (placeholder, skeleton) instead of an empty area (hig:loading#Best-practices).
- Let people do other things while loading; load content in the background (hig:loading#Best-practices).
- For unavoidably long waits: show tips, hints, new features; estimate remaining time realistically (hig:loading#Best-practices).
- Load large assets (e.g. game levels) with **Background Assets** after installation/update (hig:loading#Best-practices).
- Prefer determinate progress; switch from indeterminate to determinate as soon as the duration is known (hig:progress-indicators#Best-practices).
- Report progress honestly and evenly; keep the indicator moving, explain stalls (hig:progress-indicators#Best-practices).
- Don't switch between spinner and bar (hig:progress-indicators#Best-practices).
- Avoid vague labels like "Loading…" / "Authenticating…" (hig:progress-indicators#Best-practices).
- Allow canceling when there are no side effects; if there is loss (e.g. partial download), ask for confirmation via an alert (hig:progress-indicators#Best-practices).

### Launch
- Launch instantly; avoid waits longer than a few seconds (hig:launching#Best-practices).
- Launch screen (iOS, iPadOS, tvOS) = nearly identical to the first screen, no text, no logo/advertising, matching orientation and appearance (hig:launching#Launch-screens).
- macOS, visionOS, watchOS don't need a launch screen (hig:launching#Best-practices).
- Splash screen, if any, at the beginning of onboarding – not as the launch screen (hig:launching#Best-practices).
- Restore state (scroll position, window placement) (hig:launching#Best-practices).

## Haptics per platform

### iOS – UIFeedbackGenerator categories (hig:playing-haptics#iOS)

| Category (HIG) | Meaning according to the HIG | UIKit class / types (SDK) |
|---|---|---|
| Notification | Result of a task/action (e.g. check deposited, vehicle unlocked) | `UINotificationFeedbackGenerator` – `.success`, `.warning`, `.error` |
| Impact | Physical metaphor: snapping into place, collision | `UIImpactFeedbackGenerator` – `.light`, `.medium`, `.heavy`, `.soft`, `.rigid` |
| Selection | Values of an element change (picker detents) | `UISelectionFeedbackGenerator` |

Standard controls (toggles, sliders, pickers) already play system haptics themselves. The types in column 3 come from the UIKit SDK; the HIG names only the three categories.

### watchOS – WKHapticType (hig:playing-haptics#watchOS)

| HIG name | Meaning | `WKHapticType` |
|---|---|---|
| Notification | Important/unusual event; identical to an incoming notification | `.notification` |
| Up | Important value has risen above a threshold | `.directionUp` |
| Down | Important value has fallen below a threshold | `.directionDown` |
| Success | Action succeeded | `.success` |
| Failure | Action failed | `.failure` |
| Retry | Failed, retry possible | `.retry` |
| Start | Activity started (timer or similar); usually followed by Stop | `.start` |
| Stop | Previously started activity ended | `.stop` |
| Click | Detented dial, progress in fixed increments; avoid overlaps | `.click` |

watchOS combines haptics with a sound. Digital Crown: linear detents by default (Apple Watch Series 4 and later), lists provide detents while scrolling; turn off detents if they don't fit your own animation (hig:playing-haptics#watchOS, hig:digital-crown).

### macOS – Force Touch trackpad (hig:playing-haptics#macOS)

| Pattern | Use | `NSHapticFeedbackManager.FeedbackPattern` |
|---|---|---|
| Alignment | Dragged object snaps into alignment; target dimension, preferred position, start/end of a scrubber | `.alignment` |
| Level change | Change between discrete pressure levels (e.g. fast-forward speed via Force Click) | `.levelChange` |
| Generic | General feedback when the others don't fit | `.generic` |

Only during drag or Force Click on a trackpad with haptics; output via `NSHapticFeedbackPerformer`.

### Custom haptics (Core Haptics) (hig:playing-haptics#Custom-haptics)

| Building block | Character |
|---|---|
| Transient | Brief, compact, tap/impulse |
| Continuous | Sustained vibration |
| Sharpness | Character: soft/organic ↔ crisp/mechanical |
| Intensity | Strength |

Can be combined with audio. External haptics: game controllers (iPadOS, macOS, tvOS, visionOS), Apple Pencil Pro, and certain trackpads on compatible iPads.

## Platform differences

| Topic | iOS / iPadOS | macOS | watchOS |
|---|---|---|---|
| Haptics hardware | Taptic Engine (supported iPhones); iPad via Pencil Pro/trackpad/controller | Force Touch trackpad, game controllers | Taptic Engine + sound, Digital Crown detents |
| API | `UIFeedbackGenerator` family, Core Haptics | `NSHapticFeedbackManager`, Core Haptics (controllers) | `WKInterfaceDevice.play(_:)` with `WKHapticType` |
| Launch screen | Required (static, like the first screen) | none | none |
| Loading indicator | Determinate preferred; refresh control with automatic updates | Spinner for background operations, without label | avoid where possible (see below) |
| Easing | customizable | customizable | WatchKit layout/appearance animations have built-in easing that can't be turned off (hig:motion#watchOS) |

visionOS (brief overview): no motion in the peripheral field of view, move large objects translucent or with less contrast, change location via fade, don't rotate the virtual world, provide a stationary frame of reference, no sustained oscillations around ~0.2 Hz (hig:motion#visionOS).

## Implementation

### SwiftUI
```swift
@Environment(\.accessibilityReduceMotion) private var reduceMotion

// Motion → fade with Reduce Motion
.transition(reduceMotion ? .opacity : .move(edge: .bottom))
withAnimation(reduceMotion ? nil : .spring) { isExpanded.toggle() }

// Symbol animations (SF Symbols 5+)
Image(systemName: "arrow.down.circle")
    .symbolEffect(.bounce, value: downloads)

// Declarative haptics (iOS 17 / macOS 14 / watchOS 10)
.sensoryFeedback(.success, trigger: didSave)
.sensoryFeedback(.selection, trigger: selectedIndex)
```
`.sensoryFeedback` is available from iOS 17 / macOS 14 / watchOS 10. Which `SensoryFeedback` cases are actually perceptible on which platform (e.g. macOS only with a haptic trackpad) is not documented in the HIG mirror – check the Apple developer documentation before use.

### UIKit
```swift
let generator = UINotificationFeedbackGenerator()
generator.prepare()                       // shortly before the event
generator.notificationOccurred(.success)

UIImpactFeedbackGenerator(style: .rigid).impactOccurred()
UISelectionFeedbackGenerator().selectionChanged()

if UIAccessibility.isReduceMotionEnabled { /* crossfade instead of slide */ }
```

### AppKit
```swift
NSHapticFeedbackManager.defaultPerformer
    .perform(.alignment, performanceTime: .default)
if NSWorkspace.shared.accessibilityDisplayShouldReduceMotion { ... }
```

### watchOS (WatchKit)
```swift
WKInterfaceDevice.current().play(.success)
```

API note: Class names and enum cases come from the Apple SDKs; the HIG references only `UIFeedbackGenerator`, `NSHapticFeedbackPerformer`, `WKHapticType`, Core Haptics.

## Choosing a feedback channel

| Situation | Channel | Source |
|---|---|---|
| Ongoing status (sync, unread) | Passive, inline close to the element | hig:feedback#Best-practices |
| Expected action succeeded | No extra feedback (or subtle haptic/symbol animation) | hig:feedback#Best-practices |
| Significant completion (payment) | Confirmation + notification haptic Success | hig:feedback, hig:playing-haptics#iOS |
| Failure | Inline explanation + notification haptic Error/Failure | hig:feedback, hig:writing#Best-practices |
| Unexpected, irreversible data loss | Alert with Cancel | hig:feedback, hig:alerts |
| Expected, undoable loss | No alert, offer Undo | hig:alerts#Best-practices |
| Value detents (picker, slider) | Selection haptic (automatic with standard controls) | hig:playing-haptics#iOS |
| Snapping/aligning (drag) | Impact (iOS) / Alignment (macOS) | hig:playing-haptics |
| Brief loading | Placeholder; indicator only after "more than a moment" | hig:loading#Showing-progress |

## Review checklist

**Motion**
- [ ] Every custom animation has a nameable purpose (orientation, status, feedback).
- [ ] Animations interruptible; no mandatory waiting time.
- [ ] No extra animation on frequent standard interactions.
- [ ] Directions consistent (entry/exit mirror each other).
- [ ] Reduce Motion: fades instead of slides/zooms, no parallax, no blur transitions, no z-depth animation, springs tightened.
- [ ] No fast blinking/flashing effects.
- [ ] System animations/default springs instead of invented timing values.

**Haptics**
- [ ] Every haptic matches its documented meaning (Success ≠ Failure).
- [ ] Haptics in sync with visuals/sound, intensity matching the animation.
- [ ] No continuous haptics in non-game apps.
- [ ] In-app switch to turn them off (or system setting respected); app fully usable without haptics.
- [ ] No haptics during camera/microphone/gyro use.
- [ ] watchOS: Click not overused, Start/Stop in pairs.

**Feedback, loading, launch**
- [ ] Feedback on at least two channels (e.g. text + haptics).
- [ ] Status inline instead of alert.
- [ ] Alerts only for critical, actionable cases.
- [ ] Placeholder instead of an empty screen; background loading.
- [ ] Determinate progress where possible, honest progress, cancelable.
- [ ] No "Loading…" phrase as the only information.
- [ ] Launch screen = first screen without text/logo; state is restored.
- [ ] watchOS: content immediately; for background work, notification instead of spinner.

## Anti-patterns

- Bounce/wiggle on every button tap.
- Sideways dismiss animation for a panel that appeared from the top.
- Success haptic on failure, or the same impact for everything.
- Haptics as the only feedback for an error.
- Splash logo as the launch screen, artificial launch delay.
- "Saved!" alert after every save.
- Spinner that turns into a bar.
- Progress bar that sits at 90 % for minutes.
- Parallax/zoom transitions without a Reduce Motion path.
- Endlessly pulsing decorative animation in the idle state.

## Ambiguities / contradictions in the mirror

- **watchOS loading indicator:** `feedback#watchOS` advises showing **no** indeterminate indicator and instead promising a notification on completion; `loading#watchOS` says that for a load time of one to two seconds an indicator is **better than an empty screen**. Resolution: short wait → indicator is fine; longer background operations → notification instead of spinner.
- **Duration values:** No millisecond, curve, or spring specifications in the HIG; "brief and precise" is the only statement.
- **iOS haptic subtypes** (success/warning/error, light/medium/heavy/soft/rigid) are not in the mirror, only in the SDK.
- **Haptics availability on iPad:** For iPad, the HIG names only Apple Pencil Pro, certain trackpads, and game controllers – no built-in Taptic Engine.
