# watchOS – Platform reference

Source: local HIG mirror (`~/.apple-design/hig/pages`, as of 2026-10-21). Sources cited as `(hig:<slug>)` or `(hig:<slug>#Anchor)`. All numbers come from the mirror; missing values are marked as gaps, not estimated.

---

## 1. Profile

- **Usage context:** on the wrist, often on the move; interactions mostly under a minute, many glances per day; complications, notifications, and Siri are used more often than the app itself (hig:designing-for-watchos).
- **Ergonomics:** viewing distance at most about one foot; operated with the other hand; Always On shows content dimmed when the wrist is lowered (hig:designing-for-watchos, hig:always-on).
- **Input:** Digital Crown (primary navigation since watchOS 10), tap/swipe/drag, double tap (watchOS 11+), Action button (Ultra), Siri/Shortcuts, dictation/Scribble; no physical keyboard (hig:digital-crown, hig:gestures#watchOS, hig:action-button#watchOS, hig:keyboards).
- **Display:** small, high-resolution, circularly masked icons; several case sizes (38–49 mm in the tables) (hig:designing-for-watchos, hig:app-icons).
- **Sensors:** GPS, blood oxygen, heart function, altimeter, accelerometer, gyroscope (hig:designing-for-watchos).
- **No dark/light toggle:** Dark Mode is not supported on watchOS (hig:dark-mode).
- **The app should work independently** and add detail to complications/notifications (hig:designing-for-watchos).

---

## 2. Non-negotiable

1. Glanceable: the most important information at a glance, goal reachable with one or two gestures (hig:designing-for-watchos).
2. Flat hierarchy; anchor vertical navigation to the Digital Crown, each with a touch alternative (hig:designing-for-watchos, hig:digital-crown).
3. Respond visibly to Digital Crown rotation, respect the speed of rotation; Crown presses are reserved for the system (hig:digital-crown).
4. Multiple detail pages as a vertically paginated tab view, not horizontal and not deeply nested (hig:page-controls#watchOS, hig:split-views#watchOS).
5. Per row max. three glyph buttons or two text buttons; primary actions full width (hig:layout#watchOS, hig:buttons#watchOS).
6. Avoid loading/progress indicators; show content immediately (hig:loading#watchOS, hig:feedback#watchOS).
7. Always On: hide sensitive data, keep the layout stable, dim secondary elements, let motion wind down gently (hig:always-on).
8. Complications with dynamic, relevant data; ideally all families; each with its own deep link; plan for tinted mode (hig:complications).
9. Never use the Short Look as the only channel for important information, no sensitive data in the title (hig:notifications#watchOS).
10. Don't set a primary action for double tap in views with lists, scroll views, or vertical tabs (hig:gestures#watchOS).
11. Text no smaller than 12 pt (default 16 pt); allow enlargement to at least 140 % (hig:typography#Ensuring-legibility, hig:accessibility#Vision).
12. Controls default 44x44 pt, minimum 28x28 pt (hig:accessibility#Mobility).
13. Activity rings only for one person's Move/Exercise/Stand, unaltered, on black (hig:activity-rings).
14. No custom entries in the system Settings app; a few options at the bottom of the main view or in the More menu (hig:settings#watchOS).
15. App icon background not black (hig:app-icons#watchOS).

---

## 3. Layout & dimensions

### General values

| Item | Value | Source |
|---|---|---|
| Text default / minimum | 16 pt / 12 pt | (hig:typography#Ensuring-legibility) |
| Control default / minimum | 44x44 pt / 28x28 pt | (hig:accessibility#Mobility) |
| Spacing around elements with / without bezel | approx. 12 pt / approx. 24 pt | (hig:accessibility#Mobility) |
| Text enlargement | at least 140 % | (hig:accessibility#Vision) |
| Buttons side by side | max. 3 with glyphs, max. 2 with text | (hig:layout#watchOS) |
| Action sheet | max. 4 buttons incl. Cancel | (hig:action-sheets#watchOS) |
| Notification actions (Long Look) | up to 4 custom + system Dismiss | (hig:notifications#watchOS) |
| Long Look background like the system | white at 18 % opacity | (hig:notifications#watchOS) |
| Map annotations | up to 5 | (hig:maps#watchOS) |
| Complication line weight | 2 pt or more | (hig:complications#Visual-design) |
| Widget text | 11 pt or larger | (hig:widgets#Displaying-text-in-widgets) |
| Widget margins | 16 pt standard, 11 pt tight | (hig:widgets#Choosing-margins-and-padding) |
| Widget update animation | up to 2 seconds | (hig:widgets#Updating-widget-content) |
| App icon | 1088x1088 px, square, system masks to a circle | (hig:app-icons#Specifications) |
| Video | max. 30 s; H.264 High Profile; 160 kbps up to 30 fps; full screen 208x260 px (portrait), 16:9 320x180 px | (hig:playing-video#watchOS) |
| Audio | 64 kbps HE-AAC | (hig:playing-audio#watchOS) |

### Device sizes – what the mirror actually provides

**Gap:** The mirror contains no screen resolutions (pt/px) for the Apple Watch models. (hig:layout) mentions added Watch specifications in its change log, but the tables are missing from the current page version. Only size-related derivations are available:

| Case | Widget / Live Activity in the Smart Stack (pt) | PDF autoscaling | Dynamic Type default |
|---|---|---|---|
| 38 mm | – | 90 % | Small |
| 40 mm | 152x69.5 | 100 % | Large |
| 41 mm | 165x72.5 | 106 % | Large |
| 42 mm | 176x72.5 | 100 % (see note) | Large |
| 44 mm | 173x76.5 | 110 % | xLarge |
| 45 mm | 184x80.5 | 119 % | xLarge |
| 46 mm | 194x80.5 | – | – (not specified) |
| 49 mm (Ultra 3, 4) | 198x81.5 | 119 % | xLarge |
| 49 mm (Ultra 1, 2) | 191x81.5 | 119 % | xLarge |

Sources: (hig:widgets#Specifications), (hig:live-activities#watchOS), (hig:images#watchOS), (hig:typography#Specifications). Create images as autoscaling PDFs for 40/42 mm @2x (hig:images#watchOS).

**Note on 42 mm:** The image scaling table and the complication tables ("40mm/42mm") apparently refer to the older 42-mm case; the widget table (176x72.5 pt) to the newer one. The mirror doesn't distinguish this explicitly – for 42 mm and 46 mm, clarify the generation in each case.

### Complication image sizes (excerpt, current families)

| Layout | 40 mm | 41 mm | 44 mm | 45/49 mm |
|---|---|---|---|---|
| Circular Image | 42x42 pt | 44.5x44.5 pt | 47x47 pt | 50x50 pt |
| Circular Closed Gauge | 27x27 pt | 28.5x28.5 pt | 31x31 pt | 32x32 pt |
| Extra Large Circular Image | 120x120 pt | 127x127 pt | 132x132 pt | 143x143 pt |
| Corner Circular | 32x32 pt | 34x34 pt | 36x36 pt | 38x38 pt |
| Corner Gauge/Text | 20x20 pt | 21x21 pt | 22x22 pt | 24x24 pt |
| Rectangular Large Image with title | 150x47 pt | 159x50 pt | 171x54 pt | 178.5x56 pt |
| Rectangular Large Image without title | 162x69 pt | 171.5x73 pt | 184x78 pt | 193x82 pt |

Complete tables incl. Open Gauge, Stack, Placeholder, Inline (Utilitarian), and legacy templates: (hig:complications). Large-image layouts automatically get a 4 pt corner radius; circular images are masked to a circle (hig:complications#Rectangular, hig:complications#Circular).

**Default text values of the SwiftUI complication layouts** (all Rounded) (hig:complications):
- Circular (regular): Medium, 12 / 12.5 / 13 / 14.5 pt (40 / 41 / 44 / 45–49 mm)
- Extra Large Circular: Medium, 34.5 / 36.5 / 36.5 / 41 pt
- Corner: Semibold, 10 / 10.5 / 11 / 12 pt
- Rectangular: Medium, 16.5 / 17.5 / 18 / 19.5 pt

### Layout rules
- Limit pages to one screen height where possible; variable heights only sparingly and after the fixed pages (hig:page-controls#watchOS, hig:scroll-views#watchOS).
- Keep detail views short if vertical page navigation between list items is to work – scrolling details break it (hig:lists-and-tables#watchOS).
- Keep lists short; for long lists, most relevant items first plus "show more" (hig:lists-and-tables#watchOS).
- Autorotation only for content people show to others (image, QR code) (hig:layout#watchOS).
- Maps fully visible without scrolling, smallest region that includes all points (hig:maps#watchOS).
- No full-screen background color in views that stay visible for a long time (workout, audio) (hig:color#watchOS).

---

## 4. Navigation & structure

| Situation | Pattern | Source |
|---|---|---|
| A single list or piece of content | Vertical scrolling, Digital Crown scrolls | (hig:scroll-views#watchOS) |
| Several peer views | Vertical tab view (pages), page indicator next to the Crown | (hig:page-controls#watchOS, hig:tab-views#watchOS) |
| List → detail | Split view shows list or detail in full screen; at launch show the most relevant detail | (hig:split-views#watchOS) |
| Several detail pages for one item | Details in a vertical tab view | (hig:split-views#watchOS) |
| Hierarchy | as flat as possible; horizontal pagination and deep hierarchies are worse than vertical pages | (hig:page-controls#watchOS, hig:designing-for-watchos) |
| Short modal task with its own title/content | Sheet (full screen, material behind it) | (hig:sheets#watchOS) |
| Important info or choice | Alert or action sheet instead of a sheet | (hig:sheets#watchOS) |
| Related action for a view | Toolbar button in the top corners or at the bottom; a scrolling toolbar button appears when scrolling up | (hig:toolbars#watchOS) |

- The page indicator switches between page position and scroll position within a long page (hig:page-controls#watchOS, hig:scroll-views#watchOS).
- Don't use sheets for navigation; don't make the close label look like a page title, use an SF Symbol if appropriate (hig:sheets#watchOS).
- Pickers are operated with the Crown; long lists as a navigation-link picker (button that opens the list, Crown scrubs directly) (hig:pickers#watchOS).
- Text fields only when necessary; prefer selection lists. Keyboard only on sufficiently large displays, otherwise dictation/Scribble; input also via the paired iPhone (hig:text-fields#watchOS, hig:virtual-keyboards#watchOS).
- A search field opens full-screen text input, returning only after Cancel/Search (hig:search-fields#watchOS).

---

## 5. Component specifics (Platform considerations)

- **Buttons:** inline buttons are capsules with a contrasting material; primary action full width; two side by side only with the same height and short content; stacked one-/two-line text buttons of equal height (hig:buttons#watchOS).
- **Toolbar:** buttons in the top corners or at the bottom, stay visible over scrolling content; the system moves the time and title; toolbar buttons get Liquid Glass; for navigating to related areas or contextual actions (hig:buttons#watchOS, hig:toolbars#watchOS).
- **Double tap (watchOS 11+):** scrolls lists/scroll views, pages through vertical tabs; optional primary action (button/toggle) in non-scrolling views – the most frequently used action, e.g. play/pause; also for widgets/Live Activities in the Smart Stack (hig:gestures#watchOS).
- **Action button (Ultra):** the secondary function should logically continue the primary action (e.g. mark a segment), not end it; Action + side button = pause (exception: diving) (hig:action-button#watchOS).
- **Action sheets:** default/destructive/cancel style; max. 4 buttons incl. Cancel (hig:action-sheets#watchOS).
- **Sheets:** full screen, semi-transparent with a blurring/desaturating material; short and infrequent (hig:sheets#watchOS).
- **Lists:** limit them; Crown haptics with detents per row, consider linear detents for strongly varying row heights (hig:lists-and-tables#watchOS, hig:digital-crown).
- **Sliders:** horizontal track with +/- buttons, discrete or continuous; custom glyphs if needed (hig:sliders#watchOS).
- **Labels:** system date/timer text adapts itself and updates without the app (hig:labels#watchOS).
- **Charts:** no complex interactions; leave details to the iPhone app (hig:charts#watchOS).
- **Progress:** indicator white by default, can be colored via tint; avoid indeterminate, instead promise a notification on completion (hig:progress-indicators#watchOS, hig:feedback#watchOS).
- **Maps:** static snapshots, tap opens the Maps app (hig:maps#watchOS).
- **Media:** audio managed by the system, background audio possible, offer a Now Playing view; video only in the foreground, short, poster image must not look like a control (hig:playing-audio#watchOS, hig:playing-video#watchOS).
- **Images:** avoid transparency (file size), except for template images (complications, menu icons); animations preferably with SwiftUI (hig:images#watchOS, hig:image-views#watchOS).
- **Motion:** layout/appearance animations have built-in easing that can't be turned off (hig:motion#watchOS).
- **Sharing:** ShareLink for the system share sheet (hig:collaboration-and-sharing#watchOS).
- **Accounts:** iCloud Keychain sync for autofill and settings (hig:managing-accounts#watchOS).
- **In-app purchase:** same required information as on other platforms; clearly state differences of the Watch version; modal sheet with Close; options compactly comparable (one button per option or list + button) (hig:apple-in-app-purchase#watchOS).
- **Game Center:** no system UI on the Watch; appears on the iPhone (hig:game-center#watchOS).
- **Nearby Interaction:** distance only, app must be in the foreground (hig:nearby-interactions#watchOS).
- **Wallet:** passes appear even without a Watch app; strip image is cropped (hig:wallet#watchOS).

---

## 6. Liquid Glass, materials, current design system

- Liquid Glass is the functional layer above the content; never in the content layer; sparingly on custom controls; *clear* only over rich media backgrounds (cross-platform, also applies to watchOS) (hig:materials#Liquid-Glass).
- **Toolbar buttons** automatically get Liquid Glass and thus stand out from the content (hig:buttons#watchOS).
- **Inline buttons** get a contrasting material (hig:buttons#watchOS).
- **Use materials in full-screen modals** for orientation; don't remove or replace the system-provided material backgrounds of sheets (hig:materials#watchOS).
- **Background color with meaning:** color as an information carrier (e.g. Activity infographics in ring color), not as decoration (hig:color#watchOS, hig:designing-for-watchos).
- **Smart Stack widgets:** default background black; consider a meaningful background color (Stocks: red/green) (hig:widgets#watchOS).
- **Accented rendering:** On Apple Watch, primary content becomes white, accented content is tinted in the watch face color; in the clear appearance, a Liquid Glass background replaces the widget background (hig:widgets#Appearances, hig:widgets#Rendering-modes).
- **Tinted mode for complications:** the system desaturates and tints in one color; never convey information through color alone; provide a custom tinted variant if needed (hig:complications#Visual-design, hig:widgets#Using-color).
- **App icon:** layered, Liquid Glass effects applied by the system, layers in Icon Composer, square unmasked layers, content centered (circular mask), no custom shadows/glows, no black background (hig:app-icons).

---

## 7. Typography

- System font **SF Compact**; **SF Compact Rounded** in complications; New York is also available (hig:typography#watchOS).
- Default 16 pt, minimum 12 pt; avoid light weights; Dynamic Type is supported (hig:typography).
- On the move (workouts): large text, high contrast, most important first (hig:workouts).

### watchOS Dynamic Type – default sizes per case (hig:typography#Specifications)

| Style | Small (default 38 mm) | Large (default 40/41/42 mm) | xLarge (default 44/45/49 mm) | Weight | Emphasized |
|---|---|---|---|---|---|
| Large Title | 32 / 34.5 | 36 / 38.5 | 40 / 42.5 | Regular | Bold |
| Title 1 | 30 / 32.5 | 34 / 36.5 | 38 / 40.5 | Regular | Semibold |
| Title 2 | 26 / 28.5 | 28 / 30.5 | 30 / 32.5 | Regular | Semibold |
| Title 3 | 18 / 20.5 | 19 / 21.5 | 20 / 22.5 | Regular | Semibold |
| Headline | 15 / 17.5 | 16 / 18.5 | 17 / 19.5 | Semibold | Semibold |
| Body | 15 / 17.5 | 16 / 18.5 | 17 / 19.5 | Regular | Semibold |
| Caption 1 | 14 / 16.5 | 15 / 17.5 | 16 / 18.5 | Regular | Semibold |
| Caption 2 | 13 / 15.5 | 14 / 16.5 | 15 / 17.5 | Regular | Semibold |
| Footnote 1 | 12 / 14.5 | 13 / 15.5 | 14 / 16.5 | Regular | Semibold |
| Footnote 2 | 11 / 13.5 | 12 / 14.5 | 13 / 15.5 | Regular | Semibold |

Values: size / leading in pt. Further sizes in the mirror: xSmall, xxLarge, xxxLarge as well as AX1–AX3 (e.g. Body AX3 = 23/25.5 pt). Tracking values for SF Compact and SF Compact Rounded: (hig:typography#Tracking-values).

---

## 8. System integration

**Complications** (hig:complications, hig:widgets#Accessory-widgets)
- Families since watchOS 9 (WidgetKit accessories): circular, corner, inline, rectangular; plus extra-large circular for the X-Large watch face; legacy templates (ClockKit) only for older watchOS versions.
- Content: essential, dynamic data; static "app launcher" complications are more likely to be removed; if a family doesn't allow meaningful data, use an app-icon-like image for launching.
- Multiple complications per family, each with its own deep link; timeline updates are limited – choose times deliberately.
- Gauges: closed (fraction of a whole), open (arbitrary range), segmented (rapid value changes).
- Provide static placeholder images for each complication.
- The inline accessory offers only one tap target (hig:widgets#Adding-interactivity).

**Watch faces** (hig:watch-faces): curate shareable watch faces with your own complications, provide a preview with bezel, offer variants for all devices, for an incompatible watch face offer an alternative instead of an error.

**Smart Stack / widgets** (hig:widgets#watchOS, hig:complications#Rectangular)
- Rectangular and circular accessory widgets appear in the Smart Stack; turning the Crown on the watch face opens it (hig:digital-crown).
- Signal relevance (location, ongoing activity such as a workout) so the system ranks the widget higher (RelevanceKit).
- Consider a dedicated layout optimized for the Smart Stack and a meaningful background color.

**Live Activities** (hig:live-activities#watchOS)
- The iPhone Live Activity appears at the top of the Smart Stack; by default it combines leading/trailing of the compact presentation.
- Consider a custom Watch layout (more info, button/toggle) – but this layout also applies in CarPlay, where interaction is disabled; for driving scenarios, no buttons/toggles.
- Focus: progress, controls (timer), significant updates. Sizes as for widgets (table in section 3).

**Notifications** (hig:notifications#watchOS)
- Short Look appears when the wrist is raised, disappears when lowered – discreet, no sensitive title.
- Long Look: sash at the top (app icon + name, color or blur), freely designable content area, up to 4 actions, system Dismiss at the bottom; at least a static interface, preferably an additional dynamic one; ship the resources of the static interface.
- Double tap triggers the first non-destructive action – most frequent action first.
- iPhone notification settings also apply to the Watch by default (hig:managing-notifications#watchOS).
- Titles especially short (hig:notifications#Content).

**Always On** (hig:always-on): the app stays visible as long as it is frontmost or a background session is running; hide sensitive data; convert interactive elements to an "unavailable" appearance instead of removing them; infrequent, subtle updates.

**Workouts** (hig:workouts)
- Use a workout session: the app stays visible between wrist raises; relevant metrics (time, calories, distance) and controls (lap, interval).
- No irrelevant content during the workout; a distinct, clearly recognizable appearance for the active session.
- Pause/Resume/Stop easy to reach, clear start/stop feedback.
- Explain missing sensor data (e.g. heart rate in water) in language similar to the Workout app.
- Summary at the end, possibly with activity rings; discard very short sessions or ask.

**Activity rings** (hig:activity-rings): always three rings on watchOS; only one person's Move/Exercise/Stand; never change colors or opacity; black background with visible margin; minimum outer margin = spacing between the rings; not decorative, not in notifications, not in the icon/marketing; no notifications that duplicate Activity app messages.

**Haptics** (hig:playing-haptics#watchOS): Notification, Up, Down, Success, Failure, Retry, Start, Stop, Click – use only for their meaning; Click sparingly. Crown detents: use the default or turn them off if they don't match the animation (hig:digital-crown).

---

## 9. Implementation: SwiftUI mapping

| Concept | API | Source |
|---|---|---|
| Vertical pages | `TabView { … }.tabViewStyle(.verticalPage)` | TabView linked (hig:tab-views#watchOS); style name standard API |
| Hierarchical navigation | `NavigationStack`, `NavigationLink` | Standard API |
| List → detail | `NavigationSplitView` (shows list or detail in full screen) | Behavior (hig:split-views#watchOS) |
| Toolbar positions | `ToolbarItem(placement: .topBarLeading / .topBarTrailing / .bottomBar)` | linked (hig:toolbars#watchOS) |
| Scrolling toolbar button | `ToolbarItem(placement: .primaryAction)` | linked (hig:toolbars#watchOS) |
| Double-tap primary action | `.handGestureShortcut(.primaryAction)` | linked (hig:gestures#watchOS) |
| Crown input | `.digitalCrownRotation(...)` with `.focusable()` | Standard API |
| Picker | `Picker`, `DatePicker`; `.pickerStyle(.navigationLink)` | linked (hig:pickers#watchOS) |
| Text content type | `.textContentType(_:)` | linked (hig:virtual-keyboards#watchOS) |
| Sharing | `ShareLink` | linked (hig:collaboration-and-sharing#watchOS) |
| Date/timer labels | `Text(date, style: .timer)` and similar | `Text` linked (hig:labels#watchOS) |
| Video | `VideoPlayer` | linked (hig:playing-video#watchOS) |
| Complications / Smart Stack | WidgetKit, `WidgetFamily.accessoryCircular / .accessoryCorner / .accessoryInline / .accessoryRectangular` | accessoryRectangular linked (hig:complications#Rectangular) |
| Accent group | `.widgetAccentable()`; `WidgetRenderingMode` | linked (hig:widgets#Rendering-modes) |
| Placeholder | `placeholder(in:)` in the timeline provider | linked (hig:complications#Visual-design) |
| Relevance | RelevanceKit | linked (hig:widgets#watchOS) |
| Always On | `@Environment(\.isLuminanceReduced)` | Standard API |
| Workouts | HealthKit `HKWorkoutSession` | Standard API |
| Haptics | `WKInterfaceDevice.current().play(_:)` with `WKHapticType` | WKHapticType linked (hig:playing-haptics#watchOS) |
| Autorotation | `isAutorotating` (WatchKit) | linked (hig:layout#watchOS) |

Entries marked "Standard API" are not linked in the mirror – verify against the current developer documentation before use. ClockKit only for complications before watchOS 9 (hig:complications).

---

## 10. Review checklist

**Glanceability & navigation**
- [ ] Core task in one or two gestures; most important info visible without scrolling (hig:designing-for-watchos)
- [ ] Navigation vertical and Crown-driven, touch alternative available (hig:digital-crown)
- [ ] Multiple views as a vertical tab view instead of horizontal pagination or a deep hierarchy (hig:page-controls#watchOS)
- [ ] Pages one screen height where possible; variable heights only after fixed pages (hig:scroll-views#watchOS)
- [ ] At launch, most relevant detail instead of an empty overview (hig:split-views#watchOS)
- [ ] Sheets only for short modal tasks; alerts/action sheets (≤ 4 buttons) for decisions (hig:sheets#watchOS, hig:action-sheets#watchOS)
- [ ] Crown rotation produces a visible response; no logic on Crown press (hig:digital-crown)
- [ ] Double-tap primary action only in non-scrolling views (hig:gestures#watchOS)

**Layout & legibility**
- [ ] Max. 3 glyph or 2 text buttons per row; primary action full width (hig:layout#watchOS, hig:buttons#watchOS)
- [ ] Controls ≥ 28x28 pt, target 44x44 pt (hig:accessibility#Mobility)
- [ ] Text ≥ 12 pt, Dynamic Type incl. AX sizes tested, enlargement ≥ 140 % (hig:typography, hig:accessibility#Vision)
- [ ] Tested on the smallest and largest case (38/40 mm to 49 mm) (hig:layout#Adaptability)
- [ ] No loading spinners for normal interactions; for 1–2 s wait time, an indicator instead of an empty screen (hig:loading#watchOS)
- [ ] Text fields only when necessary; selection lists preferred (hig:text-fields#watchOS)
- [ ] No full-screen background color in views that stay visible for a long time (hig:color#watchOS)

**Material & appearance**
- [ ] Liquid Glass only on system toolbar/controls, not in content (hig:materials#Liquid-Glass, hig:buttons#watchOS)
- [ ] Standard material of sheets/modals not removed (hig:materials#watchOS)
- [ ] App icon: no black background, motif centered for the circular mask, 1088x1088 px (hig:app-icons)

**System integration**
- [ ] Complications for as many families as possible, dynamic data, each with its own deep link (hig:complications)
- [ ] Complications understandable in tinted mode, lines ≥ 2 pt, placeholder present (hig:complications#Visual-design)
- [ ] Smart Stack widget with relevance signals and a meaningful background color if appropriate (hig:widgets#watchOS)
- [ ] Live Activity: Watch layout without buttons if use while driving is likely (hig:live-activities#watchOS)
- [ ] Notifications: Short Look without sensitive data; Long Look static + dynamic; ≤ 4 actions, most frequent first (hig:notifications#watchOS)
- [ ] Always On: sensitive data hidden, layout stable, secondary elements dimmed (hig:always-on)
- [ ] Workout: session active, relevant metrics, easily reachable Pause/Stop, summary (hig:workouts)
- [ ] Activity rings unaltered, on black, only for one person's Move/Exercise/Stand (hig:activity-rings)
- [ ] Haptics match their meaning (hig:playing-haptics#watchOS)
- [ ] No custom entries in the system Settings app (hig:settings#watchOS)

---

## 11. Common mistakes / anti-patterns

- **Shrunken iPhone app:** too much content per screen, tab bar/horizontal pages, deep navigation stacks – instead of focused, vertically paginated core tasks (hig:designing-for-watchos, hig:page-controls#watchOS).
- **Loading spinners and waiting screens** – Watch interactions last seconds; better to promise the result via notification (hig:feedback#watchOS).
- **Static complication** as a pure app launcher, all complications with the same destination (hig:complications#Best-practices).
- **Color as the only carrier of meaning** in complications/widgets – lost in tinted mode and with inverted colors (hig:complications#Visual-design, hig:widgets#Using-color).
- **Sensitive data in the Short Look, on the watch face, or in Always On** (hig:notifications#watchOS, hig:complications, hig:always-on).
- **Primary action in scrolling views** – conflicts with double-tap scrolling (hig:gestures#watchOS).
- **Nested sheets / sheets as navigation** (hig:sheets#watchOS).
- **Activity rings recolored, decorative, or used for other data** (hig:activity-rings).
- **Complex chart interactions** instead of glanceable information (hig:charts#watchOS).
- **Long videos** (> 30 s) or upscaled clips (hig:playing-video#watchOS).
- **Simply removing interactive elements when Always On begins** – show them as unavailable instead (hig:always-on).
- **Action button as "Stop"** instead of a continuing secondary function (hig:action-button#watchOS).
- **Custom settings bundles** for the system Settings app (hig:settings#watchOS).

---

## Contradictions and ambiguities in the mirror

- **No Watch screen dimensions:** (hig:layout) refers in its change log to Watch specifications (incl. Series 10/11, SE 3, Ultra 3), but the tables are missing from the mirrored page version. Don't state resolutions until they are sourced.
- **Inconsistent size grids:** complication tables know 38, 40/42, 41, 44, 45/49 mm; widget tables 40, 41, 42, 44, 45, 46, 49 mm (Ultra 1/2 vs. 3/4); Dynamic Type defaults don't mention 46 mm at all. Complication and typography mappings are missing for 42 mm (new) and 46 mm.
- **Default text size:** the legibility table states 16 pt as default; according to the Dynamic Type tables, 16 pt is the default only on 40/41/42 mm (Large), on 44/45/49 mm Body is 17 pt (xLarge), on 38 mm 15 pt (hig:typography).
- **Minimum vs. text styles:** minimum 12 pt, but Footnote 2 is 10 pt in xSmall and 11 pt in Small (hig:typography#Specifications).
- **Loading indicators:** (hig:feedback#watchOS) advises against indeterminate indicators, (hig:loading#watchOS) considers an indicator better than an empty screen for 1–2 s loading time. Resolution: indicator only as an exception for short unavoidable waits, notification for longer processes.
- **Complication table Utilitarian Small, 41 mm Flat:** "10.5–23.5x21 pt", while Utilitarian Large gives the same value with "x10.5 pt" – probably a typo; 44 mm is "N/A" in each case (hig:complications#Inline).
- **Activity ring colors:** the RGB table for Move/Exercise/Stand is empty in the mirror (values only as an image); don't adopt any values (hig:activity-rings).
- **Watch faces:** device availability refers to Series 3/4 – outdated compared to current models (hig:watch-faces).
- **Haptics:** (hig:playing-haptics#watchOS) mentions Crown haptics from Series 4, (hig:digital-crown) speaks of "most models".
- **Tab views:** the page states "Not supported in iOS, iPadOS", but contains an iOS/iPadOS section (hig:tab-views); irrelevant for watchOS, but an indication of maintenance status.
