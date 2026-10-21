# Status – Components
> Source: Apple HIG, local mirror (as of 2026-10-21). Paraphrased. Sources: `(hig:<slug>)`, `(hig:<slug>#Anchor)`.

Components that show a state or progress: activity goals (activity rings), a value within a range (gauges, macOS level indicator), ongoing operations (progress indicators), and ratings (rating indicators, macOS only) (hig:status).

- [Activity rings](#activity-rings) – `activity-rings`
- [Gauges](#gauges) – `gauges`
- [Progress indicators](#progress-indicators) – `progress-indicators`
- [Rating indicators](#rating-indicators) – `rating-indicators`

## Activity rings
**Purpose:** Show a person's daily progress toward Move, Exercise, and Stand (hig:activity-rings). **Platforms:** ios, ipados, watchos; not supported in macOS (nor tvOS, visionOS).
**Use when:** the app is health/fitness-related, especially when contributing to HealthKit – e.g. a workout metrics screen or workout summary (hig:activity-rings#Best-practices). **Don't use when:** other data, multiple people, decoration, branding, app icon, marketing, or notifications are involved (hig:activity-rings#Best-practices).

**Core rules:**
- Show only Move, Exercise, and Stand data; never other data in activity rings and never this data in other ring elements (hig:activity-rings#Best-practices).
- Show the progress of exactly one person and make clear whose via a label, photo, or avatar (hig:activity-rings#Best-practices).
- Never alter the appearance: no color changes/filters/opacity, always a black background, rounding via corner radius instead of a circular mask, black border around the outer ring visible (thin black stroke if needed, no gradients/shadows/effects), scale appropriately; adapt the surroundings to the rings, not the other way around (hig:activity-rings#Best-practices).
- Use the ring colors for related labels/values (Move/Exercise/Stand, current/goal value) (hig:activity-rings#Best-practices).
- Keep an outer margin of at least the ring spacing clear; nothing may overlap or clip the rings or margin (hig:activity-rings#Best-practices).
- Clearly separate other ring-like elements via padding, lines, labels, color, or size (hig:activity-rings#Best-practices).
- Don't send notifications that repeat system information from the Activity app; no activity rings in notifications (hig:activity-rings#Best-practices).

**Platform specifics:**
- iOS: `HKActivityRingView`; with a paired Apple Watch three rings, without one only the Move ring (approximated from steps and workouts from other apps); history can mix both presentations (hig:activity-rings#iOS).
- watchOS: always three rings in the colors/meanings of the Activity app (hig:activity-rings).
- iPadOS, watchOS: no additional guidance.

**Key values:** label/value colors (RGB, in the mirror as alt text of the color swatches): Move R 250, G 17, B 79; Exercise R 166, G 255, B 0; Stand R 0, G 255, B 246 (hig:activity-rings#Best-practices). Minimum outer margin = spacing between the rings (relative, no absolute number).
**Implementation:** HealthKitUI `HKActivityRingView` (UIKit). No SwiftUI equivalent named in the mirror.
**Common mistakes:**
- Using rings for custom goals/metrics or as decoration/logo.
- Rings on a light/colored background or with a circular mask that clips the black border.
- Rings of multiple people side by side without clear attribution, or group values in one ring.

## Gauges
**Purpose:** Show a specific numeric value within a range, optionally with context about the range (min/max text, color gradient) (hig:gauges). **Platforms:** ios, ipados, macos, watchos (also visionos); not supported in tvOS.
**Use when:** a value relative to a scale is relevant (e.g. temperature, fill level). **Don't use when:** showing the progress of an ongoing operation (→ progress indicator) or time series (→ chart).

**Anatomy/styles:** circular or linear path; standard style with an indicator at the value position, capacity style with a fill up to the value; "accessory" variant in the look of watchOS complications, suitable for iOS Lock Screen widgets (hig:gauges#Anatomy).

**Core rules:**
- Write concise labels for the current value and both endpoints – VoiceOver reads visible labels (hig:gauges#Best-practices).
- Consider a color gradient along the path that supports the meaning (e.g. hot → cold) (hig:gauges#Best-practices).
- Use the accessory variant for Lock Screen widgets or a complication look (hig:gauges#Anatomy).
- macOS: for large ranges use the continuous rather than the discrete capacity style (hig:gauges#macOS).
- macOS: change the fill color at meaningful thresholds (very low/high, midpoint passed) – entirely or as a tiered state with a color sequence (hig:gauges#macOS).

**Platform specifics:**
- macOS: additionally a level indicator with styles capacity (continuous: translucent track with a fill bar; discrete: equally sized segments = total capacity, only completely filled), rating (→ rating indicators), and rarely relevance (shaded bar, e.g. search results) (hig:gauges#macOS).
- iOS, iPadOS, watchOS: no additional guidance.

**Key values:** no numbers in the mirror. Default fill color of macOS capacity indicators: green (hig:gauges#macOS).
**Implementation:** SwiftUI `Gauge`; AppKit `NSLevelIndicator`. No UIKit equivalent named in the mirror.
**Common mistakes:**
- Missing endpoint labels – value without range context, poor for VoiceOver.
- Discrete capacity indicator for a large range (tiny segments).
- Gauge misused as a progress indicator for loading.

## Progress indicators
**Purpose:** Show that the app isn't stalled during loading or lengthy operations, possibly with an estimate of the remaining time; visible only while the operation is running (hig:progress-indicators). **Platforms:** ios, ipados, macos, watchos (also tvos, visionos).
**Types:** determinate (known duration; progress bar fills from leading to trailing, circular fills clockwise) and indeterminate/activity indicator/spinner (unknown duration; macOS additionally an indeterminate bar) (hig:progress-indicators).
**Use when:** operations take noticeable time. **Don't use when:** showing a static value within a range (→ gauge).

**Core rules:**
- Prefer determinate so users can decide whether to wait, come back later, or cancel (hig:progress-indicators#Best-practices).
- Report progress as accurately and evenly as possible; an uneven pace seems stalled or misleading (hig:progress-indicators#Best-practices).
- Keep indicators moving; if stalled, give feedback about the problem and how to fix it (hig:progress-indicators#Best-practices).
- Switch from indeterminate to determinate as soon as the duration can be determined – but never from a spinner to a bar (hig:progress-indicators#Best-practices).
- Add a precise, concise description if needed; avoid vague terms like "Loading" (hig:progress-indicators#Best-practices).
- Place indicators in a consistent location (hig:progress-indicators#Best-practices).
- Offer Cancel if canceling has no side effects; with a risk of loss additionally Pause; if progress would be lost, confirm cancellation via an alert or offer to resume (hig:progress-indicators#Best-practices).

**Platform specifics:**
- iOS, iPadOS – refresh control: pull-to-refresh as a hidden activity element (typically in table views); still update automatically and periodically; title only if it adds value (e.g. last update), never as operating instructions (hig:progress-indicators#Refresh-content-controls).
- macOS: indeterminate as a bar or spinner; spinner for background operations or tight spaces (in a text field, next to a button); don't label spinners (hig:progress-indicators#macOS).
- watchOS: white over the scene background by default; color changeable via tint (hig:progress-indicators#watchOS).

**Key values:** no binding values in the mirror (90 %/10 % only as a negative example of uneven pace).
**Implementation:** SwiftUI `ProgressView`; UIKit `UIProgressView`, `UIActivityIndicatorView`, `UIRefreshControl` (SwiftUI counterpart `refreshable` – not mentioned in the mirror); AppKit `NSProgressIndicator`.
**Common mistakes:**
- Spinner although progress would be measurable; switching spinner → bar mid-operation.
- Progress jumps to 90 % and then hangs.
- "Loading…" labels without information; labeled spinner on macOS.
- No Cancel for long operations; cancellation with data loss without confirmation.

## Rating indicators
**Purpose:** Show a rank via a horizontal row of symbols (stars by default) (hig:rating-indicators). **Platforms:** macos; not supported in iOS, iPadOS, watchOS (nor tvOS, visionOS).
**Use when:** items are rated/ranked in macOS. **Don't use when:** on iOS/iPadOS/watchOS – the component doesn't exist there (custom solution required; for App Store ratings see `ratings-and-reviews`).

**Core rules:**
- Allow changing the rank inline in lists, without a separate editing screen (hig:rating-indicators#Best-practices).
- Replace the star only with a symbol whose rating purpose is unambiguous (hig:rating-indicators#Best-practices).
- Expect whole symbols: values are rounded, no partial symbols (hig:rating-indicators).
- Plan for fixed symbol spacing; symbols don't scale with the width (hig:rating-indicators).

**Platform specifics:** macOS: no additional guidance; technically a style of the level indicator (see Gauges).
**Key values:** none in the mirror.
**Implementation:** AppKit `NSLevelIndicator.Style.rating`.
**Common mistakes:**
- Expecting/trying to display half stars.
- Rating changeable only via a detail/edit screen.
- Unclear replacement symbol (not recognizable as a scale).
