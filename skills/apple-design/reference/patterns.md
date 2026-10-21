# Patterns – condensed rules from the Apple HIG

Purpose: reference for recurring interaction patterns (loading, modality, undo, settings, media playback, etc.) when designing and reviewing apps for iOS, iPadOS, macOS, and watchOS. tvOS/visionOS only in passing.

- Source: local HIG mirror `~/.apple-design/hig/pages/<slug>.md`, sync state 2026-10-21 (section "Patterns", 25 pages plus overview `hig:patterns`).
- Citation convention: `(hig:<slug>)` or `(hig:<slug>#Anchor)`. Anchors correspond to the page headings.
- Numbers and thresholds appear only if they occur verbatim on the page. Paraphrase, not original text.

## Contents

1. [Charting data](#charting-data)
2. [Collaboration and sharing](#collaboration-and-sharing)
3. [Drag and drop](#drag-and-drop)
4. [Entering data](#entering-data)
5. [Feedback](#feedback)
6. [File management](#file-management)
7. [Going full screen](#going-full-screen)
8. [Launching](#launching)
9. [Live-viewing apps](#live-viewing-apps)
10. [Loading](#loading)
11. [Managing accounts](#managing-accounts)
12. [Managing notifications](#managing-notifications)
13. [Modality](#modality)
14. [Multitasking](#multitasking)
15. [Offering help](#offering-help)
16. [Onboarding](#onboarding)
17. [Playing audio](#playing-audio)
18. [Playing haptics](#playing-haptics)
19. [Playing video](#playing-video)
20. [Printing](#printing)
21. [Ratings and reviews](#ratings-and-reviews)
22. [Searching](#searching)
23. [Settings](#settings)
24. [Undo and redo](#undo-and-redo)
25. [Workouts](#workouts)
26. [Observations/Ambiguities](#observationsambiguities)

---

## Charting data

**Purpose:** Charts should communicate insights about data (trends, state, comparison), not merely store data. Pure data output belongs in a searchable and sortable list or table instead (hig:charting-data).

**Core rules**
- Use a chart only when you want to highlight an important insight about the dataset; charts draw attention (hig:charting-data#Best-practices).
- Keep charts simple; offer details progressively (levels of detail, subsets, possibly multiple chart versions with increasing functionality) (hig:charting-data#Best-practices).
- Make every chart accessible: accessibility labels for values and components plus accessibility elements for interaction; a descriptive headline does not replace the labels (hig:charting-data#Best-practices).
- Prefer common types (bar, line); actively explain novel representations, e.g. with an introductory animation (hig:charting-data#Designing-effective-charts).
- Look at the data at the macro, intermediate, and individual-point level to show totals, averages, subsets, or outliers (hig:charting-data#Designing-effective-charts).
- Add a title, subtitle, annotations, or a summary line with the actionable key insight (hig:charting-data#Designing-effective-charts).
- Choose the size by function and level of detail: large for interaction, small for glanceables or a preview of a larger view (hig:charting-data#Designing-effective-charts).
- Keep charts with a similar purpose consistent; deviate only to emphasize differences (hig:charting-data#Designing-effective-charts).
- Maintain continuity across multiple charts of the same dataset: same type, same colors, annotations, layout (hig:charting-data#Designing-effective-charts).

**Platform differences:** no additional considerations for iOS, iPadOS, macOS, watchOS (hig:charting-data#Platform-considerations).

## Collaboration and sharing

**Purpose:** Sharing and collaboration via the system share sheet, sharing popover, Collaboration button, and Messages integration; works with CloudKit, iCloud Drive, or your own infrastructure (then universal links are required) (hig:collaboration-and-sharing).

**Core rules**
- Place the Share button where it is easy to reach, e.g. in the toolbar; in SwiftUI `ShareLink` (hig:collaboration-and-sharing#Best-practices).
- Adapt the share sheet or sharing popover to the supported sharing types ("send copy" depending on CloudKit/iCloud Drive/custom) (hig:collaboration-and-sharing#Best-practices).
- Phrase the permission summary as a short phrase; the system uses it as a button for the sharing options (hig:collaboration-and-sharing#Best-practices).
- Keep custom sharing options minimal and clearly grouped (access, read/edit, add participants) (hig:collaboration-and-sharing#Best-practices).
- Show the Collaboration button prominently as soon as collaboration starts, ideally next to the Share button (hig:collaboration-and-sharing#Best-practices).
- In the collaboration popover (three areas: participants/communication, custom items, management button), add only truly necessary custom actions (hig:collaboration-and-sharing#Best-practices).
- Rename the management button (default "Manage Shared File") if needed; without CloudKit sharing you must build the management view yourself (hig:collaboration-and-sharing#Best-practices).
- Consider surfacing collaboration events (change, members, mention) as a Messages notification with a universal link (`SWHighlightEvent`) (hig:collaboration-and-sharing#Best-practices).

**Platform differences**
- iOS: share sheet with sharing method and permissions from iOS 16. iPadOS 16 and macOS 13: comparable sharing popover. Otherwise no additional considerations (hig:collaboration-and-sharing#Best-practices).
- watchOS: `ShareLink` in SwiftUI presents the system share sheet (hig:collaboration-and-sharing#watchOS).
- visionOS: screen sharing in the Shared Space; switching to a Full Space pauses the stream. tvOS: not available.

## Drag and drop

**Purpose:** Move or copy content from a source to a destination. Rule of thumb: same container = move, different container = copy, between apps always copy (hig:drag-and-drop).

**Core rules**
- Support drag and drop wherever possible; system components (text field, text view) include it (hig:drag-and-drop#Best-practices).
- Offer alternatives (menu commands, accessibility APIs `accessibilityDragSourceDescriptors`/`accessibilityDropPointDescriptors`) (hig:drag-and-drop#Best-practices).
- Decide move/copy according to user expectations; when in doubt, choose the behavior with the lowest risk of data loss (hig:drag-and-drop#Best-practices).
- Support multi-item drag where it makes sense (hig:drag-and-drop#Best-practices).
- Enable undo; for drops that can't be undone, ask for confirmation beforehand or offer a way to revert (hig:drag-and-drop#Best-practices).
- Offer multiple representations from highest to lowest fidelity (e.g. PDF, PNG, JPEG); on drop, take the richest supported one (hig:drag-and-drop#Accepting-drops).
- Consider spring loading (controls activate when dragged over) (hig:drag-and-drop#Best-practices).
- Show a translucent drag image as soon as roughly three points have been dragged; change it only for clarification, not constantly (hig:drag-and-drop#Providing-feedback).
- Indicate whether a destination accepts the drop (insertion point, highlight; otherwise nothing or `circle.slash`); show hints only while over the destination (hig:drag-and-drop#Providing-feedback).
- Give visible feedback for an invalid or failed drop (fly back or vanish) (hig:drag-and-drop#Providing-feedback).
- Auto-scroll destinations, extract only relevant parts, check the Option key on drop (forces copy), show progress/placeholders for long transfers (hig:drag-and-drop#Accepting-drops).
- Preserve text styles if both sides support them, otherwise use the destination style; keep the selection in the destination, clear it appropriately in the source (hig:drag-and-drop#Accepting-drops).

**Platform differences**
- iOS/iPadOS: touch, pointing device, and Full Keyboard Access. iPadOS: add items during an ongoing drag (flocking) and accept multiple simultaneous drops (hig:drag-and-drop#iOS-iPadOS).
- macOS: drag to the Finder (in a reopenable format, possibly as a clipping); drag from inactive windows without activation (background selection); badge with count for multi-item drags; pointer variants (copy, drag link, disappearing item, operation not allowed); select and drag in one motion (hig:drag-and-drop#macOS). Universal Control between Mac and iPad.
- watchOS: not supported (nor tvOS). visionOS: dropping into empty space can launch an app/scene.

## Entering data

**Purpose:** Minimize input and make it error-resistant; support all input methods (hig:entering-data).

**Core rules**
- Get information from the system (Settings, permissions for location/calendar) instead of asking for it (hig:entering-data#Best-practices).
- Make the requirement clear: placeholder, label, sensible default value (hig:entering-data#Best-practices).
- Use a secure field (`SecureField`) for sensitive data (hig:entering-data#Best-practices).
- Never prefill password fields; use input, biometrics, or Keychain (hig:entering-data#Best-practices).
- Offer choices (picker, menu) instead of free text where possible (hig:entering-data#Best-practices).
- Allow input via drag and drop and paste (hig:entering-data#Best-practices).
- Validate dynamically as the user types; use number formatters for numeric fields (hig:entering-data#Best-practices).
- Enable Next/Continue only once the required data is present (hig:entering-data#Best-practices).

**Platform differences**
- macOS: expansion tooltip for truncated field content (also applies to iOS/iPadOS apps on the Mac) (hig:entering-data#macOS).
- iOS, iPadOS, watchOS: no additional considerations. tvOS: digit entry view can hide digits; visionOS: secure field is blurred during AirPlay streaming.

## Feedback

**Purpose:** Communicate status, success/failure, warnings, and ways to correct; match the delivery to the significance (passive for status, interrupting for data loss) (hig:feedback).

**Core rules**
- Make feedback accessible and multichannel (color, text, sound, haptics) (hig:feedback#Best-practices).
- Integrate status information near the affected elements (e.g. toolbar status in Mail) (hig:feedback#Best-practices).
- Use alerts only for critical, ideally actionable information; overuse devalues them (hig:feedback#Best-practices).
- Warn only about unexpected, irreversible data loss, not when deletion is the expected outcome (hig:feedback#Best-practices).
- Confirm completion only for truly significant actions (e.g. payment) (hig:feedback#Best-practices).
- Explain why a command can't be carried out (hig:feedback#Best-practices).

**Platform differences**
- watchOS: avoid indeterminate progress indicators (loading indicator); instead, announce a notification upon completion (hig:feedback#watchOS).
- iOS, iPadOS, macOS: no additional considerations.

## File management

**Purpose:** Make document-based apps behave consistently with the system when creating, opening, saving, and previewing files (Finder, Files) (hig:file-management).

**Core rules**
- Offer New/Open via app menus and keyboard shortcuts, and always also an Add button (+); on macOS put the add action in the File menu (hig:file-management#Creating-and-opening-files).
- Let a custom file browser give access to the entire file system, even if it starts at a relevant location (hig:file-management#Creating-and-opening-files).
- Save automatically and periodically, as well as on close and app switch; avoid forcing explicit saves (hig:file-management#Saving-work).
- Hide file extensions by default, but make them showable and consistent across all Open/Save dialogs (hig:file-management#Saving-work).
- Use a Quick Look viewer for unsupported files and a Quick Look generator for your own file types (hig:file-management#Quick-Look-previews).

**Platform differences**
- iOS/iPadOS (18 and later): document launcher (`DocumentGroupLaunchScene`) with title card (app name + primary/secondary button), background + accessories, sheet with file browser. Primary button = new document; background clearly set apart and calm; don't overload accessories and test them at all sizes/orientations; use animation sparingly (hig:file-management#Document-launcher).
- iOS/iPadOS: File Provider extension – show only contextually relevant documents, destination choice when exporting/moving, no custom top toolbar (the modal already has one) (hig:file-management#File-provider-app-extension).
- macOS: prefer the standard file browser; custom Open with "open recent", filters, multiple selection, renameable Open button; Save dialog for name/format/location (default "Untitled"), possibly an accessory view (hig:file-management#Custom-file-management).
- macOS: Finder Sync extension for sync status badges, context menus, toolbar buttons. With autosave disabled ("Ask to keep changes when closing documents"): indicate unsaved changes with a dot in the close button and in the Window menu and show a Save dialog on close/quit; with autosave enabled, no dot. Remove the "Edited" suffix in the title after saving (hig:file-management#Finder-Sync-extensions).
- watchOS: no document browsing in the system; no additional considerations.

## Going full screen

**Purpose:** Distraction-free full-screen presentation on iPhone, iPad, and Mac (games, media, immersive tasks) (hig:going-full-screen).

**Core rules**
- Offer full screen when it serves the experience (hig:going-full-screen#Best-practices).
- Adjust the layout subtly in full screen, but don't change the window size programmatically (hig:going-full-screen#Best-practices).
- Keep essential controls accessible (e.g. playback controls permanently visible or easy to reveal) (hig:going-full-screen#Best-practices).
- Except in games, keep the Dock accessible in iPadOS/macOS (hig:going-full-screen#Best-practices).
- Pause when switching away and resume when returning (hig:going-full-screen#Best-practices).
- Let users decide when to exit full screen; no automatic exit (hig:going-full-screen#Best-practices).
- Temporarily hide toolbars/navigation when content is in focus; restore via tap, swipe down, or cursor at the top; keep essential controls visible (hig:going-full-screen#Best-practices).

**Platform differences**
- iOS/iPadOS: keep Home indicator behavior where possible; require two swipes only to prevent unintended exits (`preferredScreenEdgesDeferringSystemGestures`). iPadOS games can have the first swipe from the bottom edge ignored (hig:going-full-screen#iOS-iPadOS).
- macOS: use system full screen (`toggleFullScreen(_:)`, accounts for the camera housing); don't change the display mode in games; entry only by the user (window button, View menu, Control-Command-F), no custom window-mode menu; optional toggle in games; Dock can be hidden in games via `hideDock` (hig:going-full-screen#macOS).
- watchOS: not supported (apps fill the screen anyway). tvOS/visionOS: not supported.

## Launching

**Purpose:** From opening (including initial download) to the first ready screen; onboarding follows afterward (hig:launching).

**Core rules**
- Launch instantly; some users don't want to wait longer than a few seconds (hig:launching#Best-practices).
- Provide a launch screen where the platform requires it (iOS, iPadOS, tvOS) (hig:launching#Best-practices).
- If needed, show a splash screen at the start of onboarding or right after launch (hig:launching#Best-practices).
- Restore the previous state granularly (scroll position, window state and position) (hig:launching#Best-practices).
- Design the launch screen nearly identical to the first screen (same base color, orientation, appearance mode) – no onboarding, no splash, no artwork (hig:launching#Launch-screens).
- Avoid text in the launch screen (it isn't localized) (hig:launching#Launch-screens).
- Don't advertise; logos only if they are a fixed part of the first screen (hig:launching#Launch-screens).

**Platform differences**
- iOS/iPadOS: launch in the current device orientation; if only one orientation is supported, launch in that one; landscape-only must respond correctly when rotated left or right (hig:launching#iOS-iPadOS).
- macOS, watchOS: no launch screen needed, no additional considerations.
- tvOS: launch screen is static; live-viewing apps can autoplay after a few seconds of inactivity. visionOS: launch even fully immersive apps in the Shared Space.

## Live-viewing apps

**Purpose:** Prioritize live content and clearly distinguish it from VOD; content strongly oriented toward TV experiences (hig:live-viewing-apps).

**Core rules**
- Place live content prominently, e.g. in the first tab (hig:live-viewing-apps#Best-practices).
- Start playback with at most one tap (e.g. a Watch Now button that disappears when tapped) (hig:live-viewing-apps#Best-practices).
- Mark live content (badge, symbol, sash, "Live" row) and show the progress of ongoing broadcasts if applicable (hig:live-viewing-apps#Best-practices).
- Keep playback as the primary action; further actions always in the same order (e.g. Watch, Start Over, Record, Favorite); show further airtimes (hig:live-viewing-apps#Best-practices).
- Use a content footer if appropriate (dimmed, current channel highlighted, categories as in the EPG, symmetric show/hide) (hig:live-viewing-apps#Best-practices).
- Give immediate visual feedback when changing channels; adapt audio to context (stop when leaving the live tab) (hig:live-viewing-apps#Best-practices).
- EPG: current programming immediately visible, easy to browse, familiar categories, favorites, browsing without interrupting playback (PiP/background) (hig:live-viewing-apps#EPG-experience).
- Cloud DVR: recording from the info panel, single/series recording, fine-grained control, playback/deletion in the DVR area, automatic storage management (hig:live-viewing-apps#Cloud-DVR).

**Platform differences:** no additional considerations for iOS, iPadOS, macOS, watchOS (hig:live-viewing-apps#Platform-considerations).

## Loading

**Purpose:** Design loading so it goes as unnoticed as possible (hig:loading).

**Core rules**
- Show something as early as possible (placeholders for text, graphics, animation) (hig:loading#Best-practices).
- Let users do other things while loading; load in the background (hig:loading#Best-practices).
- For unavoidably long loads, offer something interesting (tips, new features) and estimate the remaining time realistically (hig:loading#Best-practices).
- Download large assets in the background via Background Assets (after installation, during updates, at noncritical times) (hig:loading#Best-practices).
- Communicate loading with progress indicators: determinate for known duration, indeterminate for unknown duration (hig:loading#Showing-progress).
- In games, consider a custom loading view that matches the style (hig:loading#Showing-progress).

**Platform differences**
- watchOS: avoid loading indicators where possible; if content takes "a second or two", an indicator is better than a blank screen (hig:loading#watchOS).
- iOS, iPadOS, macOS: no additional considerations.

## Managing accounts

**Purpose:** Require accounts only when the core functionality needs it; then prefer Sign in with Apple (hig:managing-accounts).

**Core rules**
- Briefly explain the benefit and the sign-in method in the sign-in view (hig:managing-accounts#Best-practices).
- Delay sign-in as long as possible (e.g. until purchase) (hig:managing-accounts#Best-practices).
- Without Sign in with Apple, prefer passkeys (iOS, iPadOS, macOS, visionOS); with passwords, two-factor authentication (hig:managing-accounts#Best-practices).
- Name the method specifically ("Sign In with Face ID") and only if it's available on the device (`LABiometryType`) (hig:managing-accounts#Best-practices).
- Avoid an in-app option for biometrics opt-in and the term "passcode" (hig:managing-accounts#Best-practices).
- Enable genuine account deletion (not just deactivation) in the app or via a direct, easy-to-find web link; same effort in app and web (hig:managing-accounts#Deleting-accounts).
- Consider scheduled deletion, but always also offer immediate deletion; inform about duration and completion (hig:managing-accounts#Deleting-accounts).
- For in-app purchases, explain that subscription billing through Apple continues until cancellation; support deletion even if the subscription wasn't purchased in the app (hig:managing-accounts#Deleting-accounts).
- With Sign in with Apple: revoke tokens on deletion (hig:managing-accounts#Deleting-accounts).

**Platform differences**
- watchOS: use iCloud sync for Keychain access (AutoFill, settings) (hig:managing-accounts#watchOS).
- iOS, iPadOS, macOS: no additional considerations.
- tvOS: sign-in via another device, shared accounts with profiles, minimal input; TV provider: no sign-out with system sign-in, never let users sign out via privacy controls.

## Managing notifications

**Purpose:** Notifications only with permission; represent urgency honestly via interruption levels and respect Focus (hig:managing-notifications).

**Core rules**
- Distinguish communication notifications (direct communication, SiriKit intents) and noncommunication notifications (with interruption level) (hig:managing-notifications#Integrating-with-Focus).
- Choose the interruption level realistically: Passive, Active (default), Time Sensitive, Critical (hig:managing-notifications#Integrating-with-Focus).
- Note: Time Sensitive and Critical bypass scheduled delivery and Focus; only Critical bypasses the Ring/Silent switch and requires an entitlement (hig:managing-notifications#Integrating-with-Focus).
- Use Time Sensitive only for events happening now or within an hour; the system periodically asks users whether they want to keep it (hig:managing-notifications#Best-practices).
- Send marketing only after explicit opt-in (custom prompt with a clear yes/no option) and never as Time Sensitive (hig:managing-notifications#Sending-marketing-notifications).
- Provide an in-app settings screen for changing notification choices (hig:managing-notifications#Sending-marketing-notifications).

**Platform differences**
- watchOS: iPhone settings apply to the Watch by default; management in the Watch app, swipe left for options like "Mute 1 Hour" or "Turn off Time Sensitive" (hig:managing-notifications#watchOS).
- iOS, iPadOS, macOS: no additional considerations.

## Modality

**Purpose:** Content in a separate mode that blocks the parent view and requires an explicit action to dismiss (alert, sheet, popover, action sheet/confirmation dialog, activity view, full-screen modal) (hig:modality).

**Core rules**
- Present modally only when there is a clear benefit (focus, or decisions about content/device) (hig:modality#Best-practices).
- Keep modal tasks simple, short, and streamlined (hig:modality#Best-practices).
- Avoid an "app within an app": for subviews only one path, no buttons that look like the dismiss button (hig:modality#Best-practices).
- Consider a full-screen modal for media, camera, or multistep editing (hig:modality#Best-practices).
- Always provide an obvious way to dismiss according to platform convention (hig:modality#Best-practices).
- Get confirmation when user-generated content could be lost (in iOS e.g. an action sheet with a Save option) – whether by gesture or button (hig:modality#Best-practices).
- Identify the task with a title or help text (hig:modality#Best-practices).
- Let one modal close before another appears; never more than one alert at a time (alerts may appear over other modals) (hig:modality#Best-practices).

**Platform differences**
- iOS, iPadOS, watchOS: dismiss button in the top toolbar or swipe down expected (hig:modality#Best-practices).
- macOS: dismiss button in the main content expected; iPadOS/macOS can also use a separate window instead of a modal (hig:modality).
- Platform considerations: no additional considerations (hig:modality#Platform-considerations).

## Multitasking

**Purpose:** Apps must handle app switching, windows, PiP, and interruptions and be able to save/restore context at any time (hig:multitasking).

**Core rules**
- Pause activities that require attention (game, video) when switching away and resume seamlessly (hig:multitasking#Best-practices).
- Respond to audio interruptions: for primary audio (music, podcast) pause indefinitely; for short interruptions (navigation prompt) lower volume or pause, then resume (hig:multitasking#Best-practices).
- Finish user-initiated tasks in the background without further input (hig:multitasking#Best-practices).
- Notify only for important/time-sensitive tasks, not routine ones (hig:multitasking#Best-practices).

**Platform differences**
- iOS: FaceTime or video in PiP alongside another app (hig:multitasking#iOS).
- iPadOS: full-screen or windowed apps; windows freely resizable and arrangeable (similar to macOS), system window controls for tiling, full screen, minimize, close; frontmost window marked by colored controls and shadow; PiP in both modes. Apps aren't told the chosen configuration – layout must adapt to all sizes (hig:multitasking#iPadOS).
- macOS: multitasking is the default; window shadows and window states (hig:multitasking#macOS).
- watchOS: not supported (hig:multitasking#Platform-considerations).
- visionOS: don't change window edges, don't pause video when the user looks away, expect audio ducking. tvOS: PiP.

## Offering help

**Purpose:** Contextual help, tips (TipKit), and tooltips when the interface alone isn't enough (hig:offering-help).

**Core rules**
- Align help with the task: inline explanation for one or two steps, tutorial for complex goals; easy to ignore and dismiss (hig:offering-help#Best-practices).
- Use context- and platform-appropriate language/images (no "click" on iPhone, no "tap" on Mac) (hig:offering-help#Best-practices).
- Keep help inclusive; don't explain standard components, but their function in your app (hig:offering-help#Best-practices).
- Choose the tip type: popover tip (preserves content flow) or inline tip (surroundings visible); annotation style for a specific UI element, hint style without a reference (hig:offering-help#Creating-tips).
- Use tips only for simple features; more than three actions is too complex for a tip (hig:offering-help#Creating-tips).
- Write tips in one or two sentences, action-oriented, without promotion (hig:offering-help#Creating-tips).
- Control the audience via parameter/event rules and frequency (example: once every 24 hours) (hig:offering-help#Creating-tips).
- Use familiar symbols in the filled variant, but don't duplicate the UI element; buttons lead to settings or further information (hig:offering-help#Creating-tips).

**Platform differences**
- macOS (also iPhone/iPad apps on the Mac): tooltips (`help(_:)`) when the pointer hovers. Describe only the displayed control, start with a verb, don't repeat the control name, maximum 60–75 characters, sentence case, state-dependent text if needed (hig:offering-help#macOS-visionOS).
- iOS, iPadOS, watchOS: no additional considerations. visionOS: tooltips also via gaze.

## Onboarding

**Purpose:** Fast, enjoyable, optional introduction after launch – not part of it (hig:onboarding).

**Core rules**
- Teach interactively rather than through passive viewing (hig:onboarding#Best-practices).
- Consider contextual tips instead of a single onboarding flow; hints close to the relevant UI area (hig:onboarding#Best-practices).
- Keep a mandatory flow short and don't require memorization (hig:onboarding#Best-practices).
- Make tutorials optional; after skipping, don't show them again, but keep them findable in Help/Account/Settings (hig:onboarding#Best-practices).
- Focus on your app, not on system or device operation (hig:onboarding#Best-practices).
- Show a splash screen only briefly, just long enough for a glance (hig:onboarding#Additional-content).
- Don't let large downloads block onboarding; leave license texts to the App Store (hig:onboarding#Additional-content).
- Defer nonessential setup; choose sensible defaults (hig:onboarding#Additional-requests).
- Integrate permission requests into onboarding only if the app won't work otherwise; otherwise at first use of the feature (hig:onboarding#Additional-requests).
- Ask for ratings or purchases only after genuine use (hig:onboarding#Additional-requests).

**Platform differences:** no additional considerations (hig:onboarding#Platform-considerations).

## Playing audio

**Purpose:** Audio must behave as expected with respect to volume, muting, headphones, and output device (hig:playing-audio).

**Core rules**
- Respect silent mode: then only explicitly started audio (media, alarms, calls) (hig:playing-audio).
- Pause immediately when headphones are disconnected; reroute without interruption when connecting (hig:playing-audio).
- Adjust only relative levels, never the system volume (hig:playing-audio#Best-practices).
- Allow audio rerouting (AirPlay, Bluetooth) and use the system volume view `MPVolumeView` (hig:playing-audio#Best-practices).
- Choose the appropriate `AVAudioSession.Category`: Solo ambient, Ambient (both respond to Silent, no background), Playback, Record, Play and record (ignore Silent, background possible) (hig:playing-audio#Best-practices).
- Respond to external audio controls only in a clear audio context; don't redefine controls; custom player only for commands the system doesn't support (hig:playing-audio#Best-practices).
- Signal the end of temporary audio (`notifyOthersOnDeactivation`) (hig:playing-audio#Best-practices).
- Decide deliberately on interruption behavior; e.g. a VoIP app must not silently reactivate the microphone when the Smart Folio is closed (hig:playing-audio#Handling-interruptions).
- After an interruption, check `shouldResume` (media apps); games may resume automatically (hig:playing-audio#Handling-interruptions).

**Platform differences**
- iOS/iPadOS: short sounds and vibrations via System Sound Services (Audio Services) (hig:playing-audio#iOS-iPadOS).
- macOS: notification sounds mix with other audio by default (hig:playing-audio#macOS).
- watchOS: system manages playback; short clips in the foreground or longer background audio; encoding 64 kbps HE-AAC; consider a Now Playing view (hig:playing-audio#watchOS).
- visionOS: prefer sound, spatial audio, fixed vs. tracked sound; never convey important information only through sound. tvOS: audio only when user-initiated.

## Playing haptics

**Purpose:** Haptics complement visual and auditory feedback and create clear cause-and-effect relationships (hig:playing-haptics).

**Core rules**
- Use system haptic patterns only according to their documented meaning; otherwise a generic or custom pattern (hig:playing-haptics#Best-practices).
- Use haptics consistently (don't use the same pattern for success and failure) (hig:playing-haptics#Best-practices).
- Coordinate haptics with animation and sound (intensity, sharpness) (hig:playing-haptics#Best-practices).
- Avoid overuse; in apps, short haptics for discrete events rather than continuous vibration (e.g. with Apple Pencil Pro) (hig:playing-haptics#Best-practices).
- Make haptics optional; the app must work without them (hig:playing-haptics#Best-practices).
- Watch for interference with camera, gyroscope, microphone (hig:playing-haptics#Best-practices).
- Build custom haptics (Core Haptics) from transient and continuous events with sharpness and intensity, optionally with audio (hig:playing-haptics#Custom-haptics).

**Platform differences**
- iOS: standard controls (toggle, slider, picker) play system haptics; `UIFeedbackGenerator` with categories Notification (success, warning, error), Impact (light, medium, heavy, rigid, soft), Selection (hig:playing-haptics#iOS).
- iPadOS: haptics via game controllers, Apple Pencil Pro, and some trackpads on certain iPads (hig:playing-haptics).
- macOS: with Force Touch/Magic Trackpad, the patterns Alignment, Level change, Generic during drag or force click (`NSHapticFeedbackPerformer`) (hig:playing-haptics#macOS).
- watchOS: Digital Crown detents from Apple Watch Series 4; `WKHapticType` patterns Notification, Up, Down, Success, Failure, Retry, Start, Stop, Click – use Click sparingly (hig:playing-haptics#watchOS).

## Playing video

**Purpose:** System player for familiar playback; integration with the TV app (hig:playing-video).

**Core rules**
- Use the system video player; model custom players on system behavior (hig:playing-video#Best-practices).
- Show video in its original aspect ratio, without embedded letterbox/pillarbox padding. Defaults: aspect-fill for 2:1 to 2.40:1, aspect (fit) for standard (4:3, 16:9, up to 2:1) and ultrawide above 2.40:1 (hig:playing-video).
- Add metadata (image, title, description) without obscuring playback (`externalMetadata`) (hig:playing-video#Best-practices).
- Support expected input, e.g. Space bar for play/pause (hig:playing-video#Best-practices).
- Prevent audio mixing on mode change (PiP) through correct secondary audio handling (`silenceSecondaryAudioHintNotification`) (hig:playing-video#Best-practices).
- TV app: custom black screen as transition, show content immediately, resume without asking at the previous end time, correct profile, Space bar supported (hig:playing-video#Integrating-with-the-TV-app).
- Loading: avoid a loading screen; if loading takes more than two seconds, black screen with centered spinner; only until playback starts (hig:playing-video#Loading-content).
- After playback ends: contextually relevant detail view with resume option; prepare the exit view early (hig:playing-video#Exiting-playback).

**Platform differences**
- iOS, iPadOS, macOS: no additional considerations (hig:playing-video#Platform-considerations).
- watchOS: clips only in the foreground, at most 30 seconds; don't scale; encoding H.264 High Profile, 160 kbps at up to 30 fps, 208x260 px (portrait, full screen) or 320x180 px (16:9, landscape), audio 64 kbps HE-AAC; poster image content-related and not resembling a control (hig:playing-video#watchOS).
- tvOS: subtle overlays; interactive overlays with at least 0.5 s delay. visionOS: comfort, no automatically starting full immersion, thumbnail track 160 px wide.

## Printing

**Purpose:** Integrate system printing and show only relevant options (hig:printing).

**Core rules**
- Make printing discoverable: macOS in the File menu, iOS/iPadOS via a toolbar button with an action sheet (hig:printing#Best-practices).
- Offer printing only when possible; otherwise dim the menu item or remove the action, dim or hide a custom button (hig:printing#Best-practices).
- Show options (page range, copies, duplex) via the system view, if the printer supports them (hig:printing#Best-practices).

**Platform differences**
- macOS: print button in the toolbar optional (customizable); custom print panel category for app-specific options; Page Setup dialog only for document-specific settings without duplicating system features; make dependencies clear; advanced options via disclosure as "Advanced Options"; preview of settings; save settings at least until the document is closed (hig:printing#macOS).
- iOS, iPadOS: no additional considerations. watchOS: not supported (nor tvOS).

## Ratings and reviews

**Purpose:** Rating requests at the right time; the App Store allows rating at any time (hig:ratings-and-reviews).

**Core rules**
- Ask only after demonstrated engagement (completed level/task), never at first launch or during onboarding (hig:ratings-and-reviews#Best-practices).
- Don't interrupt an ongoing task; use natural pauses (hig:ratings-and-reviews#Best-practices).
- Don't pester; consider at least one or two weeks between requests (hig:ratings-and-reviews#Best-practices).
- Prefer the system prompt (`RequestReviewAction`); it appears at most three times per app in 365 days (hig:ratings-and-reviews#Best-practices).
- Weigh resetting the summary rating for a new version against fewer visible ratings (hig:ratings-and-reviews#Best-practices).

**Platform differences:** system prompt in iOS, iPadOS, macOS; otherwise no additional considerations (hig:ratings-and-reviews#Platform-considerations).

## Searching

**Purpose:** Search in the app, in documents, and systemwide (Spotlight); personalization via history, suggestions, corrections; scopes and tokens for narrowing (hig:searching).

**Core rules**
- Give important search a primary position (e.g. bottom toolbar as in Notes or its own tab) (hig:searching#Best-practices).
- Make content searchable from one central place; local search as a filter only for clearly separate areas (hig:searching#Best-practices).
- Show the current search scope (placeholder, scope bar, title) (hig:searching#Best-practices).
- Offer suggestions (recent searches, predictive) via `searchSuggestions(_:)` (hig:searching#Best-practices).
- Consider privacy for search history and offer deletion (hig:searching#Best-practices).
- Make content indexable in Spotlight via metadata; for custom file types a Spotlight file importer (`CSImportExtension`) (hig:searching#Systemwide-search).
- Use Spotlight for advanced file search in the app; prefer system Open/Save views (with built-in search); Quick Look generator for custom types (hig:searching#Systemwide-search).

**Platform differences:** Spotlight and search within documents/windows apply to iOS, iPadOS, macOS; otherwise no additional considerations (hig:searching#Platform-considerations).

## Settings

**Purpose:** Few, well-chosen settings; global options stay in the system Settings app (hig:settings).

**Core rules**
- Choose defaults that are optimal for most people (e.g. automatically adapt performance to the device) (hig:settings#Best-practices).
- Minimize the number of settings (hig:settings#Best-practices).
- Open settings the expected way: Command-Comma with a keyboard, Esc in games (hig:settings#Best-practices).
- Don't ask for anything that can be detected (controller, Dark Mode) (hig:settings#Best-practices).
- Don't duplicate systemwide settings (accessibility, scrolling behavior, authentication) (hig:settings#Best-practices).
- Put rarely changed, general options in your own settings area (hig:settings#General-settings).
- Offer task-specific options (show/hide, sort, filter) directly in the affected screen (hig:settings#Task-specific-options).
- Put only the rarest options in the system Settings app; possibly a button that opens them directly (hig:settings#System-settings).

**Platform differences**
- macOS: Settings item in the app menu (not in the toolbar); document-related options in the File menu; dim Minimize/Maximize; noncustomizable, always-visible toolbar with the active pane; window title = current pane or "App Name Settings"; restore the most recently used pane (hig:settings#macOS).
- watchOS: no custom settings in the system Settings app; a few essential options at the bottom of the main view or via a More menu (hig:settings#watchOS).
- iOS, iPadOS: no additional considerations.

## Undo and redo

**Purpose:** Make actions reversible and encourage experimentation; make the result predictable and visible (hig:undo-and-redo).

**Core rules**
- Make results predictable (descriptive alert or menu texts like "Undo Typing", "Redo Bold") (hig:undo-and-redo#Best-practices).
- Show the result, even outside the visible area (e.g. scroll to it) (hig:undo-and-redo#Best-practices).
- Allow multiple undo without artificial limits, at least back to the last logical step (open, save) (hig:undo-and-redo#Best-practices).
- Consider batch undo of related changes or "everything since open/save" (hig:undo-and-redo#Best-practices).
- Offer custom undo/redo buttons only if needed, then with system symbols in the toolbar (hig:undo-and-redo#Best-practices).

**Platform differences**
- iOS/iPadOS: don't redefine standard gestures (three-finger swipe, shake); the alert title automatically gets the prefix "Undo "/"Redo ", add one or two descriptive words (hig:undo-and-redo#iOS-iPadOS).
- macOS: Undo/Redo at the top of the Edit menu; Command-Z and Shift-Command-Z (hig:undo-and-redo#macOS).
- watchOS: not supported (nor tvOS).

## Workouts

**Purpose:** Fitness experiences on Apple Watch, iPhone, and iPad focused on the current activity and progress (hig:workouts).

**Core rules**
- In watchOS, use workout sessions; show relevant data (time, calories, distance) and controls (lap, interval) (hig:workouts#Best-practices).
- Avoid distraction by irrelevant information during the workout (hig:workouts#Best-practices).
- Mark active workouts visually unambiguously (live-updating metrics, distinct layout) (hig:workouts#Best-practices).
- Make pause/resume/stop easy to find and clearly confirm start/stop (hig:workouts#Best-practices).
- Explain missing sensor data (e.g. heart rate while swimming) in language similar to the Workout app (types Swimming, Other) (hig:workouts#Best-practices).
- Show a summary at the end, optionally with Activity rings (hig:workouts#Best-practices).
- Automatically discard extremely short sessions (a few seconds) or ask (hig:workouts#Best-practices).
- Ensure legibility in motion: large text, high contrast (hig:workouts#Best-practices).
- Use Activity rings only for their documented purpose (hig:workouts#Best-practices).

**Platform differences:** no additional considerations for iOS, iPadOS, watchOS; macOS (as well as tvOS, visionOS) not supported (hig:workouts#Platform-considerations).

---

## Observations/Ambiguities

**Contradictions and tensions between pages**
- watchOS loading indicators: `hig:feedback#watchOS` advises against indeterminate indicators (explicitly including loading indicator) and recommends referring to a notification; `hig:loading#watchOS` considers a loading indicator better than a blank screen for one to two seconds of load time. Presumably resolved by duration (short vs. long process), but the pages don't say so explicitly.
- Splash screen: `hig:launching` and `hig:onboarding` allow a brief splash screen at the start of onboarding; `hig:playing-video#Integrating-with-the-TV-app` prohibits splash screens on the transition from the TV app. Context-dependent, not a genuine contradiction.
- Workouts: the introduction mentions Mac and Apple TV for live/recorded workouts, Platform considerations exclude macOS and tvOS (hig:workouts).
- Live-viewing apps: the platform header lists all six platforms including watchOS, but the content is consistently TV-oriented (EPG, Cloud DVR, info panel); unclear how far the rules apply to iOS/macOS/watchOS (hig:live-viewing-apps).
- File management: the platform header lists tvOS and watchOS, the text says these systems don't offer document browsing (hig:file-management).
- Going full screen: the platform header lists only iOS, iPadOS, macOS, yet a best practice mentions visionOS windows with hideable toolbars (hig:going-full-screen).

**Duplications**
- Quick Look generator for custom file types appears both in `hig:file-management#Quick-Look-previews` and in `hig:searching#Systemwide-search`.
- Audio interruptions: `hig:multitasking#Best-practices` and `hig:playing-audio#Handling-interruptions` cover the same topic at different depths.

**Update notes (page headers)**
- 2026-06-08 searching: terminology updated, best practices refined (most recent note; previous version 2025-06-09 incorporated content from Search fields).
- 2025-06-09 going-full-screen: hiding toolbars/navigation, deferring Home indicator gestures.
- 2025-06-09 loading: background download of large assets (Background Assets).
- 2025-06-09 multitasking: platform section restructured, iPadOS multiwindow multitasking added.
- 2024-06-10 file-management (document launcher), launching (splash screen), onboarding (approaches, splash screen), settings (restructuring, game examples).
- 2024-05-07 playing-haptics: Apple Pencil Pro.
- 2023-12-05 collaboration-and-sharing (artwork), modality (full-screen modals, multiple modals), offering-help (visionOS tooltips).
- 2023-10-24 drag-and-drop, 2023-09-12 ratings-and-reviews (artwork only in each case); 2023-09-12 playing-video (visionOS thumbnail width corrected); 2023-06-21 entering-data, playing-audio (visionOS).
- No update note: patterns, charting-data, feedback, live-viewing-apps, managing-accounts, managing-notifications, printing, undo-and-redo, workouts. live-viewing-apps, managing-accounts, managing-notifications, printing, undo-and-redo, workouts, and feedback also have no change log.

**Missing information**
- `hig:playing-video#Best-practices` refers to "Keyboards and Remotes" without a link.
- `hig:entering-data#macOS` links Offering help via a web URL instead of a `hig:` slug.
- No concrete time or quantity figures for autosave intervals, undo depth, or splash screen duration; only qualitative guidance.
- Modality states dismissal conventions (toolbar button/swipe vs. button in content), but Platform considerations report "no additional considerations"; the platform rules thus appear only in the best-practices section.
