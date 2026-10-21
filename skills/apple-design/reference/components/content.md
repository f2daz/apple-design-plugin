# Content – components
> Source: Apple HIG, local mirror (as of 2026-10-21). Paraphrased. Sources: `(hig:<slug>)`, `(hig:<slug>#Anchor)`.

Components that present content rather than trigger actions: charts, images, multiline text, and embedded web content. All four are primarily passive; interaction (tap, click) belongs in buttons or dedicated controls (hig:content).

- [Charts](#charts) – `charts`
- [Image views](#image-views) – `image-views`
- [Text views](#text-views) – `text-views`
- [Web views](#web-views) – `web-views`

## Charts
**Purpose:** Visualize data so that a few key messages are quickly understood and support decisions (hig:charts). **Platforms:** ios, ipados, macos, watchos (also tvos, visionos).
**Use when:** trends, comparisons between categories, proportions, or outliers need to be shown; for detailed design see also `charting-data` (Patterns). **Don't use when:** a single number or a value within a range is enough (→ Gauge), or the key message would only be reachable through interaction.

**Anatomy (terms):** Mark (representation of a value), Plot area, Scale, Axis, Ticks, Grid lines, Labels, Legend, Title/Subtitle/Annotations (hig:charts#Anatomy).

**Core rules:**
- Choose the mark type by message: Bar for category comparison/proportions/totals per period, Line for progressions/trends, Point for individual values, correlations, clusters, and outliers; combine types (e.g., Line + Point) when it clarifies (hig:charts#Marks).
- Decide deliberately between a fixed and a dynamic axis range: fixed when min/max are meaningful for all data (e.g., battery 0–100 %), dynamic when values vary widely and the plot area should be filled (hig:charts#Axes).
- Set the lower bound by mark type: zero for bar charts, not necessarily zero when relevant differences lie far from zero (e.g., heart rate) (hig:charts#Axes).
- Use familiar tick sequences (0, 5, 10 instead of 1, 6, 11) and dose grid lines/labels according to usage context (hig:charts#Axes).
- Describe purpose and main message up front in title/subtitle; summarize the key message in plain language (hig:charts#Descriptive-content).
- Keep the data visually dominant; axes and text only provide context (hig:charts#Best-practices).
- Make every chart accessible (VoiceOver, Audio Graphs) and never hide critical information behind interaction (hig:charts#Best-practices).
- For small marks, enlarge the hit area to the entire plot area (scrubbing); give keyboard/Switch Control a logical path (e.g., along the x-axis or through subsets) (hig:charts#Best-practices).
- Never rely on color alone; add shapes/patterns and separate adjacent color areas (e.g., stacked bars) with gaps (hig:charts#Color).
- Write accessibility labels with purpose: context + concrete value, no subjective words, no ambiguous formats/abbreviations, describe meaning instead of appearance; hide visible axis/tick labels from assistive technologies (hig:charts#Enhancing-the-accessibility-of-a-chart).

**Platform considerations:**
- watchOS: no complex chart interactions; show glanceable info, offer details in the app on another platform (hig:charts#watchOS).
- iOS, iPadOS, macOS, tvOS, visionOS: no additional considerations. In compact contexts, maximize plot width, keep y-axis labels short, move units into the title if needed (hig:charts#Best-practices).

**Key values:** none in the mirror (0 %/100 % only as an example of a fixed axis range).
**Implementation:** Swift Charts (`Chart`, mark types such as `BarMark`, `LineMark`, `PointMark`) – provides Audio Graphs and accessibility elements per mark by default (hig:charts#Enhancing-the-accessibility-of-a-chart). Change notification for assistive technologies: `UIAccessibility.Notification` (UIKit), `NSAccessibility.Notification` (AppKit); navigation path via, among others, `accessibilityRespondsToUserInteraction(_:)` (SwiftUI).
**Common mistakes:**
- Bar chart without a zero baseline, or heart-rate chart with a forced zero baseline.
- Data series distinguished only by color; accessibility labels describe colors instead of meaning.
- Key value reachable only by scrubbing; data changes only animated, not signaled otherwise (hig:charts#Best-practices).
- Too many grid lines / long y-labels that eat plot width in compact layouts.

## Image views
**Purpose:** Display a single image (or an animated image sequence) on a transparent or opaque background; typically not interactive (hig:image-views). **Platforms:** ios, ipados, macos, watchos (also tvos, visionos).
**Use when:** the main purpose is pure image display (PNG, JPEG, PDF, etc.) (hig:image-views#Content). **Don't use when:** the image should be clickable (→ button with image / Image button), an icon is needed (→ SF Symbols / interface icon), or it should be editable in macOS (→ Image well) (hig:image-views#Best-practices).

**Core rules:**
- Use image views only for pure display; for rare interactive images, configure a system button with an image instead of rebuilding button behavior (hig:image-views#Best-practices).
- Use SF Symbols or template icons for icons – they adopt accent colors (hig:image-views#Best-practices).
- Ensure contrast for text over images (e.g., text shadow or background layer) (hig:image-views#Content).
- Keep all images in an animation sequence the same size, ideally prescaled to the view size (hig:image-views#Content).

**Platform considerations:**
- iOS, iPadOS: no additional considerations.
- macOS: editable image → Image well; clickable image → Image button (hig:image-views#macOS).
- watchOS: prefer SwiftUI for animations; alternatively WatchKit (`WKImageAnimatable`) (hig:image-views#watchOS).
- (tvOS: layered images with depth effect; visionOS: 2D, stereoscopic, and spatial photos, RealityKit `ImagePresentationComponent`) (hig:image-views#tvOS), (hig:image-views#visionOS).

**Key values:** none in the mirror.
**Implementation:** SwiftUI `Image`; UIKit `UIImageView`; AppKit `NSImageView`.
**Common mistakes:**
- Tap gesture on an image view instead of a button.
- Bitmap icons instead of SF Symbols (no tint, no scaling).
- Illegible text on a busy photo without contrast measures.

## Text views
**Purpose:** Display multiline, styled text, optionally editable, with scrolling when it overflows (hig:text-views). **Platforms:** ios, ipados, macos, watchos (also tvos, visionos).
**Use when:** text is long, editable, or specially formatted (hig:text-views#Best-practices). **Don't use when:** only a small amount of text is displayed (→ Label) or short input is needed (→ Text field).

**Core rules:**
- Choose a text view only for long/formatted/editable text; otherwise a label or text field (hig:text-views#Best-practices).
- Keep text legible despite styling freedom; support Dynamic Type and test with accessibility settings such as bold text (hig:text-views#Best-practices).
- Make useful text (error message, serial number, IP address) selectable and copyable (hig:text-views#Best-practices).
- In iOS/iPadOS, show the keyboard type that matches the content (hig:text-views#iOS-iPadOS).
- Default: leading alignment and system label color; for an editable view, the keyboard appears on selection in iOS/iPadOS/visionOS (hig:text-views).

**Platform considerations:**
- iOS, iPadOS: choose the appropriate keyboard type, see `virtual-keyboards` (hig:text-views#iOS-iPadOS).
- macOS, watchOS: no additional considerations.
- (tvOS: text view for display only; editable text via text fields) (hig:text-views#tvOS).

**Key values:** none in the mirror.
**Implementation:** SwiftUI `Text` (display; named as the equivalent in the mirror – for editable multiline text, `TextEditor` is common in SwiftUI, not mentioned in the mirror); UIKit `UITextView`; AppKit `NSTextView`.
**Common mistakes:**
- Text view for single-line input instead of a text field.
- Fixed font sizes without Dynamic Type.
- Error codes/IDs not copyable.

## Web views
**Purpose:** Load and display rich web content (embedded HTML, websites) directly in the app, e.g., HTML emails (hig:web-views). **Platforms:** ios, ipados, macos (also visionos); not supported in tvOS, watchOS.
**Use when:** people should briefly see web content without leaving the app context. **Don't use when:** you want to rebuild your own browser – Safari is the primary way to browse the web (hig:web-views#Best-practices).

**Core rules:**
- Provide back/forward navigation with controls when multiple pages can be visited – it is not enabled by default (hig:web-views#Best-practices).
- Don't build a Safari replacement with web views (hig:web-views#Best-practices).
- Use web views for brief, context-bound web content (hig:web-views#Best-practices).
- Don't plan web views for watchOS/tvOS (hig:web-views#Platform-considerations).

**Platform considerations:** iOS, iPadOS, macOS, visionOS: no additional considerations; tvOS/watchOS not supported.
**Key values:** none in the mirror.
**Implementation:** WebKit `WKWebView` (per the mirror). Unclear/not in the mirror: a SwiftUI-native web view API.
**Common mistakes:**
- Multipage navigation without a back button.
- In-app browser with address bar/tabs instead of handing off to Safari.
