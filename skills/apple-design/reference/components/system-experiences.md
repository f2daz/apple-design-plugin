# System experiences – Components
> Source: Apple HIG, local mirror (as of 2026-10-21). Paraphrased. Sources: `(hig:<slug>)`, `(hig:<slug>#Anchor)`.

Surfaces through which an app appears in the system **outside its own window**: Home/Lock Screen, Dynamic Island, Control Center, Smart Stack, watch face, Siri/Spotlight. Common denominator: glanceable, concise, deep-linking, usually implemented via WidgetKit / ActivityKit / App Intents.

Contents: [App Shortcuts](#app-shortcuts) · [Complications](#complications) · [Controls](#controls) · [Live Activities](#live-activities) · [Notifications](#notifications) · [Snippets](#snippets) · [Status bars](#status-bars) · [Top Shelf](#top-shelf) · [Watch faces](#watch-faces) · [Widgets](#widgets)

**Quick pick**
| Need | Component |
|---|---|
| Periodically updated information + simple action on Home/Lock Screen, desktop, Smart Stack | Widget |
| Ongoing activity with a start/end (≤ 8 h), frequent updates | Live Activity |
| One-time, time-sensitive event, user not in the app | Notification |
| A button/switch in Control Center, Lock Screen, Action button | Control |
| Function via Siri/Spotlight/Action button without opening the app | App Shortcut (+ snippet as visual response) |
| Data on the watch face (watchOS) | Complication (= accessory widget) |

---

## App Shortcuts
**Purpose:** Makes key app functions/content available systemwide (Siri, Spotlight, Shortcuts app, Action button, Apple Pencil squeeze), starting at installation. **Platforms:** ios, ipados, watchos (visionos without specifics). Not in tvOS; in macOS no App Shortcuts, but App Intents actions for custom shortcuts (hig:app-shortcuts#macOS).

**Use when:** frequent, important tasks, ideally completable without a context switch; multistep tasks may open the app (hig:app-shortcuts#Best-practices).
**Don't use when:** the function falls into a domain covered by **app schemas** – prefer those so Apple Intelligence/Siri can offer them contextually (hig:app-shortcuts#Best-practices).

**Core rules:**
- Limit yourself to the most frequent and important tasks (hig:app-shortcuts#Best-practices).
- Offer at most **one** optional parameter with predictable, familiar values – people don't see the list while speaking (hig:app-shortcuts#Best-practices).
- Ask for a missing optional value; suggest a likely default plus a short list of alternatives (hig:app-shortcuts#Best-practices).
- Keep spoken phrases short and easy to say out loud; request additional required details in a follow-up step (hig:app-shortcuts#Best-practices).
- Make shortcuts discoverable in the app, e.g. with occasional Siri tips after relevant actions (hig:app-shortcuts#Best-practices).
- Respond with a snippet (static/confirmation) or a Live Activity (ongoing, e.g. timer) (hig:app-shortcuts#Responding-to-App-Shortcuts).
- Put all critical information in the full dialog text – responses may arrive on audio-only devices (AirPods, HomePod) (hig:app-shortcuts#Responding-to-App-Shortcuts).
- Phrases must include the app name; define natural variants (hig:app-shortcuts#Editorial-guidelines).
- Spelling: "App Shortcuts"/"Shortcuts" in title case and plural; individual "shortcuts" lowercase (hig:app-shortcuts#Editorial-guidelines).

**Platform specifics:**
- iOS/iPadOS: appear in Spotlight (top hit or Shortcuts section) with an SF Symbol or preview image; set the order by importance – the system later prioritizes by usage (hig:app-shortcuts#iOS-iPadOS).
- macOS: no App Shortcuts; App Intents can still be used in the Shortcuts app (hig:app-shortcuts#macOS).

**Key values:** max. 10 App Shortcuts per app (hig:app-shortcuts).
**Implementation:** App Intents – `AppIntent`, `AppShortcutsProvider`/`AppShortcut`, `AppShortcutPhrase`, parameters via `@Parameter`; tips with `SiriTipView` (SwiftUI) / `SiriTipUIView` (UIKit); dialog `IntentDialog(full:supporting:…)`.
**Common mistakes:** multiple parameters in one phrase; information only visual instead of in the dialog; shortcut for a function an app schema already covers; shortcuts never promoted in the app.

---

## Complications
**Purpose:** Shows current, relevant data directly on the watch face, visible every time the wrist is raised. **Platforms:** watchos (only).

**Use when:** there is essential, changing data people want to see at a glance (hig:complications#Best-practices).
**Don't use when:** the result would only be a static app launcher without data – people rarely keep such complications (hig:complications#Best-practices).

**Core rules:**
- Support as many families as possible; where no meaningful data fits, show an image representing the app as a launcher (hig:complications#Best-practices).
- Offer multiple complications per family, each with its own deep link (hig:complications#Best-practices).
- Protect sensitive data – with Always On it is visible to people nearby (hig:complications#Best-practices).
- Plan the timeline deliberately: updates per day and stored entries are limited (hig:complications#Best-practices).
- Choose the ring/gauge appropriately: closed = fraction of a whole, open = arbitrary range, segmented = rapid changes within the app's range (hig:complications#Visual-design).
- Test tinted mode: never use color as the only carrier of information; provide a custom tinted variant for full-color images if needed (hig:complications#Visual-design).
- Line widths ≥ 2 pt (hig:complications#Visual-design).
- Provide static placeholder images for each supported complication (hig:complications#Visual-design).

**Platform specifics:** Families from watchOS 9: circular (incl. extra large, bezel text), corner, inline (utilitarian small/large), rectangular; rectangular can appear in the Smart Stack from watchOS 10 (background color, relevance intents, custom layout) (hig:complications#Rectangular). Legacy templates (circular small, modular small/large, extra large) only for older watchOS versions (hig:complications#Legacy-templates).

**Key values** (pt, @2x assets; excerpt, complete incl. 38 mm/placeholder/legacy see anchors):
| Element | 40 mm | 41 mm | 44 mm | 45/49 mm |
|---|---|---|---|---|
| Circular Image | 42×42 | 44.5×44.5 | 47×47 | 50×50 |
| Circular Extra Large Image | 120×120 | 127×127 | 132×132 | 143×143 |
| Corner Circular | 32×32 | 34×34 | 36×36 | 38×38 |
| Rectangular Large image with title | 150×47 | 159×50 | 171×54 | 178.5×56 |
| Rectangular Large image without title | 162×69 | 171.5×73 | 184×78 | 193×82 |
- Default text (SwiftUI, Rounded): circular Medium 12/12.5/13/14.5 pt; corner Semibold 10/10.5/11/12 pt; rectangular Medium 16.5/17.5/18/19.5 pt (each 40/41/44/45–49 mm) (hig:complications#Circular, #Corner, #Rectangular).
- Bezel text fills almost 180° before truncation; large-image rectangular with an automatic 4 pt corner radius; the system masks circular images to a circle (hig:complications#Circular, hig:complications#Rectangular).
- Further tables: (hig:complications#Inline), (hig:complications#Legacy-templates).

**Implementation:** WidgetKit (preferred from watchOS 9) with `WidgetFamily.accessoryCircular/.accessoryCorner/.accessoryInline/.accessoryRectangular`, `TimelineProvider` incl. `placeholder(in:)`, `WidgetRenderingMode`; legacy: ClockKit `CLKComplicationDataSource`.
**Common mistakes:** static complication without data; all complications open the same screen; information only via color (breaks in tinted mode); hairlines < 2 pt.
**Ambiguity:** The page (as of 2023) gives no sizes for 42 mm (new)/46 mm, whereas Widgets/Live Activities list them. In "Inline", 41 mm Flat is given once as `…x21 pt` and once as `…x10.5 pt` – probably a typo in the original.

---

## Controls
**Purpose:** Button or toggle that makes an app function reachable from Control Center, the Lock Screen, or via the Action button. **Platforms:** ios, ipados, macos. Not in watchOS, tvOS, visionOS.

**Use when:** an action provides the most value without launching the app – e.g. start a Live Activity, switch a device, open the camera (hig:controls#Best-practices).
**Don't use when:** information should be displayed (→ widget) or the task requires multiple steps in the app.

**Anatomy:** symbol + title + optional value. Control Center shows the symbol (larger sizes: + title/value), Lock Screen only the symbol, the Action button shows symbol + value in the Dynamic Island (hig:controls#Anatomy).

**Core rules:**
- Choose a symbol that conveys the behavior on its own; for toggles one symbol each for on/off (hig:controls#Best-practices).
- Animate state changes with a symbol animation; for ongoing actions keep animating until completion (hig:controls#Best-practices).
- Update the control on interaction, on completion, or via push (hig:controls#Best-practices).
- Choose a brand-appropriate tint color (colors the toggle's "on" state and the Dynamic Island presentation) (hig:controls#Best-practices).
- Request required configuration (e.g. which lamp) directly when the control is added (hig:controls#Best-practices).
- Provide hint text for the Action button, verb-based (hig:controls#Best-practices).
- Provide placeholders when the title/value depend on the situation (hig:controls#Best-practices).
- Let the title/value be redacted when the device is locked; security-relevant actions (door, car) only after unlocking (hig:controls#Best-practices).
- Camera control (from iOS 18 on a locked device): same camera UI as in the app, provide instructions for adding it (hig:controls#Camera-experiences-on-a-locked-device).

**Platform specifics:** no additional ones for iOS/iPadOS/macOS (hig:controls#Platform-considerations).
**Key values:** none in the mirror.
**Implementation:** WidgetKit/SwiftUI `ControlWidget`, `ControlWidgetButton`, `ControlWidgetToggle`; `promptsForUserConfiguration()`, `controlWidgetActionHint(_:)`; App Intents `IntentAuthenticationPolicy`; `LockedCameraCapture`; `SymbolEffect`.
**Common mistakes:** symbol incomprehensible without a title; toggle with only one symbol; state not updated after the action; sensitive values visible on the Lock Screen.

---

## Live Activities
**Purpose:** Shows the progress of a time-limited activity (delivery, game, workout) continuously and at a glance. **Platforms:** ios, ipados, macos (menu bar, mirrored from iPhone), watchos (Smart Stack); additionally CarPlay. Not in tvOS, visionOS.

**Use when:** a task/event with a clear start and end, short to medium duration ≤ 8 h, frequent updates (hig:live-activities#Best-practices).
**Don't use when:** advertising/promotion; permanent information without an end (→ widget); one-time event (→ notification).

**Presentations (all required):** compact (Dynamic Island, leading + trailing around the TrueDepth camera), minimal (with multiple activities), expanded (touch and hold), Lock Screen (banner at the bottom; on devices without Dynamic Island also as an overlay banner), plus StandBy (hig:live-activities#Anatomy).

**Core rules:**
- Show only the most important information; details via tap in the app, directly at the right place (hig:live-activities#Best-practices, hig:live-activities#Offering-interactivity).
- Don't show sensitive data openly – harmless summary or redaction (hig:live-activities#Best-practices).
- Large text with at least Medium weight; logo without a container, never the whole app icon (hig:live-activities#Best-practices).
- Support limited width: compact/minimal fit into a 28 pt circle, if necessary only the leading view (hig:live-activities#Creating-Live-Activity-layouts).
- Use concentric margins and `ContainerRelativeShape` instead of hard-coded radii; adapt the height dynamically to the content (hig:live-activities#Creating-Live-Activity-layouts).
- At most one interactive element, only for core functions (pause/resume, contact) (hig:live-activities#Offering-interactivity).
- Update only for new content; alerts only for truly important things, not parallel push notifications for the same thing (hig:live-activities#Starting-updating-and-ending-a-Live-Activity).
- Bundle multiple events into **one** rotating activity (hig:live-activities#Starting-updating-and-ending-a-Live-Activity).
- End immediately when the event ends; choose a proportional dismissal time, usually 15–30 min (hig:live-activities#Starting-updating-and-ending-a-Live-Activity).
- Design for iPhone first, then refine for StandBy/CarPlay/watchOS; don't design the Lock Screen presentation like a notification (hig:live-activities#Presentation, hig:live-activities#Lock-Screen-presentation).

**Platform specifics:**
- iOS StandBy: minimal → tap → Lock Screen presentation scaled 2×; default background recommended; check Night Mode = red tint (hig:live-activities#StandBy-presentation).
- Dynamic Island: background always opaque black, not customizable (only the Lock Screen allows a custom background); tint the key line color appropriately (hig:live-activities#Choosing-colors).
- macOS: appears automatically in the menu bar (compact/minimal/expanded), a click opens iPhone Mirroring (hig:live-activities#macOS).
- watchOS: at the top of the Smart Stack, default = combined compact layout; a custom layout is possible but also applies to CarPlay (where interaction is disabled) (hig:live-activities#watchOS).
- CarPlay: custom layout via `ActivityFamily.small`; buttons/toggles are disabled (hig:live-activities#CarPlay).

**Key values:**
- Duration ≤ 8 h; after ending visible for up to 4 h (Lock Screen, Mac menu bar, Smart Stack), removed immediately from Dynamic Island/CarPlay (hig:live-activities#Best-practices, hig:live-activities#Starting-updating-and-ending-a-Live-Activity).
- Animations max. 2 s; no animation in Always On with reduced brightness (hig:live-activities#Adding-transitions-and-animating-content-updates).
- Minimal: up to three activities in the Dynamic Island (hig:live-activities#Minimal).
- Lock Screen default margin 14 pt (hig:live-activities#Lock-Screen-presentation).

| iPhone (pt, portrait) | Compact | Minimal | Expanded | Lock Screen | Limited width |
|---|---|---|---|---|---|
| 430×932 | 62.33×36.67 | 36.67–45×36.67 | 408×84–160 | 408×84–160 | 28×28 |
| 393×852 | 52.33×36.67 | 36.67–45×36.67 | 371×84–160 | 371×84–160 | 28×28 |
- iPad Lock Screen: 500×84–160 (1366×1024) or 425×84–160 (other listed sizes); macOS uses iOS dimensions; CarPlay 240×78, 240×100, 170×78; watchOS = widget Smart Stack dimensions (hig:live-activities#Specifications).

**Implementation:** ActivityKit (`Activity`, `ActivityAttributes`) + WidgetKit `ActivityConfiguration` with `DynamicIsland { … }`; `isDynamicIslandLimitedInWidth`; `activitySystemActionForegroundColor(_:)`; `supplementalActivityFamilies([.small])` for watchOS/CarPlay; start via App Intents `LiveActivityIntent`.
**Common mistakes:** activity without an end/lasting days; leading and trailing look like two separate pieces of information; too many alerts + duplicate push notifications; multiple parallel activities instead of one rotating one; buttons that don't work in the car.

---

## Notifications
**Purpose:** Delivers timely, valuable information that can be understood at a glance – even when the app isn't in the foreground. **Platforms:** ios, ipados, macos, watchos (also tvos, visionos without specifics).

**Use when:** an event is relevant to the user and they aren't in the app; consent has been given (hig:notifications).
**Don't use when:** error messages (→ alert) (hig:notifications#Best-practices); prompts for tasks in the app; advertising.

**Core rules:**
- Concise and informative; no multiple notifications for the same occasion (hig:notifications#Best-practices).
- No sensitive/confidential content (hig:notifications#Best-practices).
- In the foreground, integrate subtly (badge, refresh a list) instead of interrupting (hig:notifications#Best-practices).
- Short title, title case, without a closing period; with a generic title, rather let the app name be shown (hig:notifications#Content).
- Body in complete sentences, sentence case, don't truncate it yourself; provide neutral placeholder text for hidden previews (hig:notifications#Content).
- Don't put the app name/icon in the content – the system shows them (hig:notifications#Content).
- Actions: useful, short (title case), with an interface icon; no "Open app" action; avoid or mark destructive actions (hig:notifications#Notification-actions).
- Badge only for the number of unread notifications, keep it current, never as the only source of information, no custom badge-like elements (hig:notifications#Badging).
- Sound optional, short and distinctive; never rely on it alone for important information (hig:notifications#Content).

**Platform specifics:**
- watchOS: short look (brief, discreet, nothing critical only there) → long look (scrollable, static or dynamic; provide at least a static variant, dynamic preferred); sash at the top customizable (color/blur), Dismiss button always at the bottom (hig:notifications#Short-looks, hig:notifications#Long-looks).
- watchOS double tap performs the first nondestructive action → most frequent action first (hig:notifications#Double-tap).

**Key values:** up to 4 action buttons (detail view; also watchOS long look); long look background like system notifications: white at 18 % opacity (hig:notifications#Notification-actions, hig:notifications#Long-looks).
**Implementation:** UserNotifications (`UNUserNotificationCenter`, `requestAuthorization`, `UNNotificationCategory`/`UNNotificationAction`, `hiddenPreviewsBodyPlaceholder`, `UNNotificationSound`); custom UI: UserNotificationsUI `UNNotificationContentExtension`; watchOS: SwiftUI `WKNotificationScene`.
**Common mistakes:** errors as notifications; "Open now" action; badge for non-notification counts; private content in the title; reminder spam.

---

## Snippets
**Purpose:** Compact view that shows a result or requests confirmation after an action via Siri, Spotlight, or Shortcuts. **Platforms:** ios, ipados, macos. Not in tvOS, visionOS, watchOS.

**Types:** *Confirmation* (confirm/cancel, optionally with options) and *Result* (information without a follow-up action); every snippet intent ends with a result, confirmation is optional (hig:snippets).
**Anatomy:** dialog (spoken by Siri, shown above the view by default) · custom view (may contain buttons) · system buttons: confirmation = Cancel + primary button, result = Done (hig:snippets#Anatomy).

**Use when:** lightweight, quick interaction for an app action (weather, confirm an order, daily goal).
**Don't use when:** extensive details are needed → deep link into the app (hig:snippets#Best-practices); ongoing status → Live Activity.

**Core rules:**
- Check contrast and consistent margins in light and dark (hig:snippets#Best-practices).
- Concise content, height ≤ 400 pt; consider Dynamic Type for the amount of text (hig:snippets#Best-practices).
- Label the primary button descriptively ("Order" instead of "OK"); without a label it is called "Continue" (hig:snippets#Best-practices).
- Convey the purpose visually, omit the dialog text from the visual presentation where possible – it's there for audio use (hig:snippets#Best-practices).

**Platform specifics:** no additional ones (hig:snippets#Platform-considerations).
**Key values:** max. height of the custom view 400 pt (hig:snippets#Best-practices).
**Implementation:** App Intents (SwiftUI view as the intent result, confirmation with `ConfirmationActionName`); for details see "Displaying static and interactive snippets".
**Common mistakes:** views too tall (clipped); "OK" primary button; dialog text as the only source of meaning.

---

## Status bars
**Purpose:** Bar at the top edge of the screen with device status (time, network, battery). **Platforms:** ios, ipados. Not in macOS, tvOS, visionOS, watchOS.

**Use/don't use:** provided by the system; the decision concerns only legibility and temporary hiding.

**Core rules:**
- Obscure content under the status bar so it stays legible and nothing appears interactive; preferably a scroll edge effect with blur (hig:status-bars#Best-practices).
- Hide temporarily for full-screen media (hig:status-bars#Best-practices).
- Never hide permanently; a simple, discoverable gesture to show it again (e.g. tap) (hig:status-bars#Best-practices).

**Platform specifics:** no additional ones.
**Key values:** none in the mirror.
**Implementation:** SwiftUI `statusBarHidden(_:)`, `ScrollEdgeEffectStyle`; UIKit `preferredStatusBarStyle`, `UIStatusBarStyle`, `prefersStatusBarHidden`, `UIScrollEdgeEffect`.
**Common mistakes:** controls behind a transparent status bar; permanently hidden status bar.

---

## Top Shelf
**Purpose:** Area on the Apple TV Home Screen that prominently shows the app's content in the Dock. **Platforms:** tvos only (outside the focus of this plugin).

**Core rules:**
- Lead directly into content (Play + More Info in carousel layouts) and show new content rather than already watched content (hig:top-shelf#Best-practices).
- No advertising/prices; prefer dynamic, layered images (hig:top-shelf#Best-practices).
- Provide at least one static fallback image (2320×720 pt) that doesn't appear interactive (hig:top-shelf#Best-practices).
- Scrolling inset banner: 3–8 images, text in the image + accessibility label (hig:top-shelf#Scrolling-inset-banner).

**Key values:** image sizes per layout see (hig:top-shelf#Sectioned-content-row), (hig:top-shelf#Scrolling-inset-banner).

---

## Watch faces
**Purpose:** The user-chosen main view of Apple Watch; apps can offer configured, shareable watch faces with their complications. **Platforms:** watchos (only).

**Use when:** the app has multiple complications and a curated, preconfigured experience promotes discovery (hig:watch-faces#Best-practices).
**Don't use when:** only a single, barely useful complication exists.

**Core rules:**
- Share watch faces that show your complications (possibly with accent color, images, styles); if the app is missing, the system prompts for installation (hig:watch-faces#Best-practices).
- Show a preview for each shared watch face (bezel illustrated or from Apple Design Resources) (hig:watch-faces#Best-practices).
- Offer variants for all devices; some faces only from Series 4 (Explorer from Series 3 with cellular) – indicate the devices (hig:watch-faces#Best-practices).
- For an incompatible face, immediately offer a compatible alternative instead of showing an error (hig:watch-faces#Best-practices).

**Platform specifics:** watchOS only; sharing from watchOS 7 (hig:watch-faces).
**Key values:** none in the mirror.
**Implementation:** ClockKit `CLKWatchFaceLibrary` ("Sharing an Apple Watch face").
**Common mistakes:** face only for new models without an alternative; error message instead of fallback; no preview.

---

## Widgets
**Purpose:** Offers glanceable, timely content and focused interactions of the app on the Home/Lock Screen, desktop, Smart Stack, and more. **Platforms:** ios, ipados, macos, watchos (also visionos; Apple HomeView according to the mirror). Not in tvOS.

**Families:** system small/medium/large/extra large (iPad, Mac, visionOS)/extra large portrait (visionOS only); accessory circular/rectangular/inline (Lock Screen iPhone/iPad, Watch), corner (Watch only) (hig:widgets#System-family-widgets, hig:widgets#Accessory-widgets).
**Rendering modes:** full-color, accented (accent/primary group, tinted/clear appearance with Liquid Glass), vibrant (Lock Screen, StandBy night, Mac desktop) (hig:widgets#Appearances, hig:widgets#Rendering-modes).

**Use when:** simple information matching the app's main purpose that changes over the day, plus deep links/simple actions (hig:widgets#Best-practices).
**Don't use when:** real-time updates are needed (→ Live Activity) (hig:widgets#iOS-iPadOS); just an app icon substitute; app-like complexity.

**Core rules:**
- One idea per widget; offer sizes only if they add value – don't inflate small content (hig:widgets#Best-practices).
- Balance information density; only content related to the main purpose (hig:widgets#Best-practices).
- Subtle branding; logo at most small in the top right (hig:widgets#Best-practices).
- Let the system update dates/times; show the as-of time when updates are less frequent than glances (hig:widgets#Updating-widget-content).
- Interaction: few, sufficiently large targets (buttons/toggles); a tap opens the app at the appropriate place (hig:widgets#Adding-interactivity).
- Use standard margins, match the corner radius via `ContainerRelativeShape` (hig:widgets#Choosing-margins-and-padding).
- System font, text styles, SF Symbols; never rasterize text (hig:widgets#Displaying-text-in-widgets).
- Never convey meaning by color alone; use full-color images sparingly (e.g. album art) (hig:widgets#Using-color).
- Accented: split views into accent and primary groups; vibrant: opaque grayscale instead of white opacities (hig:widgets#Rendering-modes).
- Realistic gallery preview, recognizable placeholders, one description per widget (starting with a verb), group sizes (hig:widgets#Previews-and-placeholders).

**Platform specifics:**
- iOS/iPadOS: Lock Screen widgets additionally follow the complication principles (inline above, circular/rectangular below the clock); Always On with sufficient gray contrast; StandBy/CarPlay = small without background, scaled up → mark the background as removable, little image/color, large text; StandBy night = red tint (hig:widgets#iOS-iPadOS, hig:widgets#StandBy-and-CarPlay).
- macOS: no additional guidance; the desktop uses smaller margins and the vibrant appearance (hig:widgets#Choosing-margins-and-padding, hig:widgets#Appearances).
- watchOS: Smart Stack black background by default – consider a meaningful background color; provide relevance (location, workout) via RelevanceKit (hig:widgets#watchOS).
- visionOS (peripheral topic): 3D object on surfaces, two levels of detail (simplified/default), mounting elevated/recessed, treatment paper/glass (hig:widgets#visionOS).

**Key values:**
- Default margin 16 pt, tighter 11 pt for groupings; Mac desktop/Lock Screen smaller (hig:widgets#Choosing-margins-and-padding).
- Text ≥ 11 pt; Dynamic Type Large to AX5 (iOS, iPadOS, visionOS) (hig:widgets#Displaying-text-in-widgets).
- Update animations up to 2 s (hig:widgets#Updating-widget-content).
- Inline accessory: only one tap target (hig:widgets#Adding-interactivity).
- iPhone (excerpt, pt): 430×932 → small 170×170, medium 364×170, large 364×382, circular 76×76, rectangular 172×76, inline 257×26; 393×852 → 158×158, 338×158, 338×354, 72×72, 160×72, 234×26. Full iPhone/iPad tables: (hig:widgets#Specifications).
- Watch Smart Stack (pt): 40 mm 152×69.5 · 41 mm 165×72.5 · 42 mm 176×72.5 · 44 mm 173×76.5 · 45 mm 184×80.5 · 46 mm 194×80.5 · 49 mm Ultra 3/4 198×81.5 · Ultra 1/2 191×81.5 (hig:widgets#watchOS-dimensions).
- visionOS: scaling 75–125 % by the user (hig:widgets#Thresholds-and-sizes).

**Implementation:** WidgetKit + SwiftUI: `Widget`, `StaticConfiguration`/`AppIntentConfiguration`, `TimelineProvider`, `supportedFamilies`, `containerBackground(for:)`/`containerBackgroundRemovable`, `widgetAccentable(_:)`, `widgetRenderingMode` (environment), `Button(intent:)`/`Toggle(isOn:intent:)`, `Link`/`widgetURL`, `Text(_:style:)` for times, `supportedMountingStyles(_:)` (visionOS).
**Common mistakes:** widget = copy of the app icon; too dense/app-like; static content; meaning only via color (breaks in tinted/vibrant); text below 11 pt; widget look replicated in the app (hig:widgets#Best-practices).
**Note:** "Apple HomeView" (small widgets, Modular face up to 4 widgets) is, according to the mirror, an update from 2026-10-13 – no further sources outside this page (hig:widgets#Apple-HomeView).
