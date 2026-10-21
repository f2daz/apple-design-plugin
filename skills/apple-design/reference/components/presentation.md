# Presentation – Components
> Source: Apple HIG, local mirror (as of 2026-10-21). Paraphrased. Sources: `(hig:<slug>)`, `(hig:<slug>#Anchor)`.

Components that present content or tasks over, beside, or in place of the current context: modal interruptions (Alert, Action sheet, Sheet), transient overlays (Popover), floating auxiliary windows (Panel), windows, and scroll and paging containers. Cross-cutting rules on modality are in `(hig:modality)`.

Contents: [Action sheets](#action-sheets) · [Alerts](#alerts) · [Page controls](#page-controls) · [Panels](#panels) · [Popovers](#popovers) · [Scroll views](#scroll-views) · [Sheets](#sheets) · [Windows](#windows) · [Distinctions](#distinctions-confirmation-and-secondary-task)

**Cross-cutting (Modality):** Use modality only when there is a clear benefit; keep modal tasks short and linear, no "app within the app" (hig:modality#Best-practices). Always provide an obvious way to dismiss – iOS/iPadOS/watchOS: button in the top toolbar or swipe down; macOS/tvOS: button in the content area (hig:modality#Best-practices). Ask for confirmation before data loss on dismissal, in iOS e.g. via an action sheet with a save option (hig:modality#Best-practices). Never show multiple modal views at once; alerts may appear above everything, but never two alerts at the same time (hig:modality#Best-practices).

---

## Action sheets
**Purpose:** Modal choice of options related to an action the person has just deliberately initiated. **Platforms:** ios, ipados, macos, watchos (tvos as well; not supported in visionOS).

**Use when:** a user-initiated action needs clarifying choices (e.g. delete or save a draft) (hig:action-sheets#Best-practices); confirming before discarding unsaved changes on swipe-to-dismiss of a sheet (hig:sheets#iOS-iPadOS).
**Don't use when:** informing about an unexpected problem → Alert (hig:action-sheets#Best-practices); options should be shown on demand → Menu (hig:action-sheets#iOS-iPadOS).

**Core rules:**
- Use an action sheet rather than an alert for choices related to an intentional action (hig:action-sheets#Best-practices).
- Use sparingly – every instance interrupts the task (hig:action-sheets#Best-practices).
- Keep the title short, ideally a single line; add a message only if title plus context are not enough (hig:action-sheets#Best-practices).
- When data could be destroyed, provide a Cancel button, placed at the bottom (watchOS: top left) (hig:action-sheets#Best-practices).
- Mark destructive options with the destructive style and place them at the top (hig:action-sheets#Best-practices).
- Don't allow scrolling – limit the number of buttons (hig:action-sheets#iOS-iPadOS).

**Platform specifics:**
- iOS/iPadOS: action sheet rather than menu for action-related choices; don't let it scroll (hig:action-sheets#iOS-iPadOS).
- watchOS: system style with title, optional message, Cancel, and additional buttons; button styles Default, Destructive, Cancel (hig:action-sheets#watchOS).
- macOS, tvOS: no additional guidance; visionOS: not supported (hig:action-sheets#Platform-considerations).

**Key values:** watchOS: max. 4 buttons incl. Cancel, i.e. max. 3 additional options (hig:action-sheets#watchOS).

**Implementation:** SwiftUI `confirmationDialog(_:isPresented:titleVisibility:actions:)` (cross-platform, includes Cancel by default), role `ButtonRole.destructive`; UIKit `UIAlertController` with `.actionSheet`, `UIAlertAction.Style.destructive` (hig:action-sheets).

**Common mistakes:**
- Action sheet for error messages or pure information (belongs in an alert or in context).
- Long option lists that scroll.
- Destructive option at the bottom or without destructive style.
- Action sheet as a replacement for a menu the user opens.

---

## Alerts
**Purpose:** Interruptive presentation of critical information that requires immediate attention or a decision. **Platforms:** ios, ipados, macos, watchos (also tvos, visionos).

**Use when:** a problem needs to be reported, a warning is needed before rare, irreversible data destruction, or a purchase or important self-initiated action must be confirmed (hig:alerts).
**Don't use when:** merely informing (not actionable), for frequent undoable actions (even destructive ones), at app launch, for choices related to a deliberate action → Action sheet (hig:alerts#Best-practices, hig:alerts#iOS-iPadOS).

**Core rules:**
- Use sparingly; only essential information and useful actions (hig:alerts#Best-practices).
- Specific title: what happened, where, why – no "Error"/error code, max. two lines; sentence → punctuation + sentence case, fragment → title case without a period (hig:alerts#Content).
- Additional text only if it adds value; don't explain the buttons (hig:alerts#Content).
- Button titles: one or two words, a verb related to the text; "OK" only in purely informational alerts; avoid "Yes/No"; cancel is always "Cancel" (hig:alerts#Buttons).
- Order: most likely/default button trailing in a row or at the top of a stack; Cancel leading or at the bottom (hig:alerts#Buttons).
- Destructive style only for destructive actions the person did **not** deliberately choose (a deliberately chosen "Empty Trash" keeps the default style so Return confirms) (hig:alerts#Buttons).
- For a destructive action always offer Cancel, but never make Cancel the default; if the alert should be read deliberately → no default button; a single button as default → "Done", not "Cancel" (hig:alerts#Buttons).
- Support alternative ways to cancel: Home Screen (iOS/iPadOS), Esc or Cmd-. (iOS, iPadOS, macOS, visionOS), Menu button (tvOS) (hig:alerts#Buttons).
- Text field only if input is required to resolve the situation (e.g. password) (hig:alerts#Content).

**Platform specifics:**
- iOS/iPadOS: use an action sheet for action-related choices; avoid scrolling (can occur with large text sizes) (hig:alerts#iOS-iPadOS).
- macOS: app icon is shown automatically (replaceable); suppression checkbox for recurring alerts, accessory view, Help button possible; caution symbol (`exclamationmark.triangle`) only for a real risk of unexpected data loss, not for save/empty trash (hig:alerts#macOS).
- visionOS: Shared Space → in front of the window, slightly offset forward, stays anchored to the window when moved; Full Space → centered in the field of view (hig:alerts#visionOS).
- Text field possible in iOS, iPadOS, macOS, visionOS; icon + accessory view in macOS, visionOS (hig:alerts#Content).
- tvOS, watchOS: no additional guidance.

**Key values:** up to 3 buttons (all platforms) (hig:alerts#Content); visionOS accessory view max. 154 pt high, corner radius 16 pt (hig:alerts#visionOS).

**Implementation:** SwiftUI `alert(_:isPresented:actions:)` with `Button(role: .cancel/.destructive)`; UIKit `UIAlertController` (`.alert`); AppKit `NSAlert` (`accessoryView`, suppression) (hig:alerts).

**Common mistakes:**
- "OK"/"Yes"/"No" instead of verbs that describe the action.
- Alert on every deletion despite undo; alert at app launch (e.g. "No network" instead of placeholder data + a subtle notice).
- Cancel as the default button; destructive style on a deliberately chosen action.
- Title "Error" without cause/context.

---

## Page controls
**Purpose:** Row of indicators (dots) showing the pages of a flat, ordered list and the current page. **Platforms:** ios, ipados, watchos (also tvos, visionos; not supported in macOS).

**Use when:** switching between peer, sequential pages, including user-created lists (e.g. Weather locations) (hig:page-controls#Best-practices).
**Don't use when:** there is hierarchy or non-sequential relationships → sidebar/split view; with a very large number of pages → e.g. grid (hig:page-controls#Best-practices).

**Core rules:**
- Place horizontally centered near the bottom edge (hig:page-controls#Best-practices).
- Not too many pages – beyond about 10 dots they can no longer be counted at a glance (hig:page-controls#Best-practices).
- Keep custom indicator images simple (no negative space, text, inner lines); prefer SF Symbols (hig:page-controls#Customizing-indicators).
- Customize the default image only if it strengthens meaning; max. two different indicator images (hig:page-controls#Customizing-indicators).
- Don't color the indicators – the system color ensures contrast (hig:page-controls#Customizing-indicators).
- No animated page transitions while scrubbing; animate only on tap (hig:page-controls#iOS-iPadOS).
- No scrubbing with the Minimal background style (no feedback) (hig:page-controls#iOS-iPadOS).

**Platform specifics:**
- iOS/iPadOS: tapping left/right of the current dot = previous/next page, scrubbing = sequential, beyond the edge = first/last page; iPadOS: pointer on individual dots. Background styles: Automatic (only during interaction; when not primary navigation), Prominent (always; only when primary navigation), Minimal (never) (hig:page-controls#iOS-iPadOS).
- tvOS: only for collections of full-screen pages (hig:page-controls#tvOS).
- visionOS: display only, not interactive (hig:page-controls#visionOS).
- watchOS: at the bottom for horizontal pagination or next to the Digital Crown for a vertical tab view; prefer vertical pagination with the Digital Crown; limit pages to one screen height where possible, variable heights after fixed ones (hig:page-controls#watchOS).

**Key values:** "more than about 10 dots" hard to grasp (hig:page-controls#Best-practices); max. 2 different indicator images (hig:page-controls#Customizing-indicators).

**Implementation:** SwiftUI `TabView` with `PageTabViewStyle` (`.tabViewStyle(.page)`); UIKit `UIPageControl` (`preferredIndicatorImage`, `setIndicatorImage(_:forPage:)`, `backgroundStyle`, `InteractionState`) (hig:page-controls).

**Common mistakes:**
- Page control for hierarchical navigation.
- Many colorful/different indicator symbols.
- Scroll indicator on the same axis in addition to the page control (hig:scroll-views#iOS-iPadOS).

---

## Panels
**Purpose:** Floating macOS auxiliary window with controls, options, or information about the active window or selection. **Platforms:** macos (not supported in iOS, iPadOS, tvOS, visionOS, watchOS).

**Use when:** quick access to settings for the current selection is needed, especially as an inspector (content follows the selection) (hig:panels#Best-practices); repeated input with visible results (e.g. Find & Replace) instead of a sheet (hig:sheets#macOS).
**Don't use when:** an info window with fixed content is needed → regular window; the layout suggests a split view pane rather than an inspector (hig:panels#Best-practices). On other platforms consider a modal presentation instead (hig:panels).

**Core rules:**
- Prefer simple direct controls (sliders, steppers); avoid text input and select-then-act (hig:panels#Best-practices).
- Give it a short noun title in title case (e.g. "Inspector") – the title bar is needed for positioning (hig:panels#Best-practices).
- When the app becomes active, bring all open panels to the front; hide them when inactive (hig:panels#Best-practices).
- Don't include panels in the Window menu's document list (Show/Hide commands there are fine) (hig:panels#Best-practices).
- Generally don't offer a minimize button (hig:panels#Best-practices).
- Refer to it in the UI by its title, without the word "panel" ("Show Fonts") (hig:panels#Best-practices).
- HUD style only in media-oriented apps when a standard panel would obscure content and few controls are needed; prefer standard panels (hig:panels#HUD-style-panels).
- Keep HUDs small, use color sparingly, keep the style when switching modes (e.g. full screen) (hig:panels#HUD-style-panels).

**Platform specifics:** macOS only. Panels usually become the key window only after a click on the title bar or a text input element (hig:windows#macOS-window-states). In panels, small/mini scroll bars may be used, then all controls the same size (hig:scroll-views#macOS).

**Key values:** none in the mirror.

**Implementation:** AppKit `NSPanel`, HUD via `NSWindow.StyleMask.hudWindow` (hig:panels). SwiftUI: no panel type named in the mirror; for inspector functionality, `inspector(isPresented:content:)` or a split view pane could be used (framework knowledge, not in the HIG mirror – verify).

**Common mistakes:**
- Panel stays visible while the app is inactive.
- Form-heavy panels with many text fields.
- HUD without a content reason or with standard controls that don't match visually.

---

## Popovers
**Purpose:** Transient view above the content that appears after a click/tap on a control and points to it. **Platforms:** ios, ipados, macos (also visionos; not supported in tvOS, watchOS).

**Use when:** a small amount of information or a few related functions are needed briefly (e.g. changing event details) and persistent sidebars/panels would take too much space (hig:popovers#Best-practices).
**Don't use when:** a warning must be shown → Alert; in a compact size class → sheet or similar full-screen modal (hig:popovers#Best-practices, hig:popovers#iOS-iPadOS).

**Core rules:**
- Point the arrow as directly as possible at the triggering element; don't obscure it or essential content (hig:popovers#Best-practices).
- Close/Cancel/Done only if it adds clarity (e.g. with/without saving); otherwise a tap outside or a selection dismisses it; with multiple selection keep it open until explicitly closed (hig:popovers#Best-practices).
- When a nonmodal popover closes automatically, always save the work; discard only via explicit Cancel (hig:popovers#Best-practices).
- Only one popover at a time, no cascades; nothing above it except an alert (hig:popovers#Best-practices).
- Allow switching to another popover with a single click/tap (hig:popovers#Best-practices).
- Limit the size to the content; animate size changes (hig:popovers#Best-practices).
- In help text don't say "popover"; name the task/element instead (hig:popovers#Best-practices).

**Platform specifics:**
- iOS/iPadOS: no popovers in compact views; adapt the layout to the size class and use a sheet or similar there (hig:popovers#iOS-iPadOS).
- macOS: a popover can be detached by dragging and becomes a panel; consider supporting detaching, change the detached form only minimally (hig:popovers#macOS).
- visionOS: no additional guidance.

**Key values:** none in the mirror.

**Implementation:** SwiftUI `popover(isPresented:attachmentAnchor:arrowEdge:content:)`; UIKit `UIPopoverPresentationController`; AppKit `NSPopover` (hig:popovers).

**Common mistakes:**
- Forcing a popover on iPhone in compact width.
- Opening a popover from a popover.
- Discarding input on a tap outside.
- Warnings in a popover instead of an alert.

---

## Scroll views
**Purpose:** Container that makes content larger than the visible area movable vertically or horizontally. **Platforms:** ios, ipados, macos, watchos (also tvos, visionos).

**Use when:** content extends beyond the bounds of the view; paging for page-by-page content (hig:scroll-views#Best-practices).
**Don't use when:** it would nest a scroll view inside another one of the same direction (hig:scroll-views#Best-practices).

**Core rules:**
- Support standard scroll gestures and keyboard shortcuts; custom implementations with elastic behavior (hig:scroll-views#Best-practices).
- Make scrollability visible, e.g. content cut off at the edge (hig:scroll-views#Best-practices).
- No nested scroll views with the same orientation (horizontal inside vertical is fine) (hig:scroll-views#Best-practices).
- Consider page-by-page scrolling, possibly with an overlap unit (e.g. one line of text) for context (hig:scroll-views#Best-practices).
- Scroll automatically when the selection/insertion point is out of view – but only as far as necessary (hig:scroll-views#Best-practices).
- For zoom, set sensible min/max scale (hig:scroll-views#Best-practices).
- Scroll edge effect: prefer the Automatic style; only behind floating elements (e.g. toolbars), not decorative; one effect per view, in split views per pane with equal height (hig:scroll-views#Scroll-edge-effects).

**Platform specifics:**
- iOS/iPadOS: in paging mode consider a page control, then no scroll indicator on the same axis (hig:scroll-views#iOS-iPadOS). Scroll edge effects exist in iOS, iPadOS, macOS (hig:scroll-views#Scroll-edge-effects).
- macOS: the indicator is called a scroll bar; in panels possibly small/mini, then uniform control size (hig:scroll-views#macOS).
- tvOS: no indicators; the system scrolls focused elements into view (hig:scroll-views#tvOS).
- visionOS: small, fixed indicator at fixed positions, slightly thicker than iOS → enlarge margins if needed; jog bar while dragging; enable Look to Scroll per scroll view – for reading/browsing views, not for controls/dense information, consistent, clear scroll areas, remove parallax/custom scroll effects beforehand (hig:scroll-views#visionOS, hig:scroll-views#Look-to-Scroll).
- watchOS: prefer vertical (Digital Crown); paging via vertical tab views; pages ideally one screen height (hig:scroll-views#watchOS).

**Key values:** none in the mirror.

**Implementation:** SwiftUI `ScrollView`, `PagingScrollTargetBehavior`, `ScrollEdgeEffectStyle`, `ScrollInputKind.look`; UIKit `UIScrollView`, `UIScrollEdgeEffect.Style`; AppKit `NSScrollView`, `NSScrollEdgeEffectStyle`; WatchKit `WKPageOrientation` (hig:scroll-views).

**Common mistakes:**
- Vertical list inside a vertical ScrollView.
- Scroll edge effect as decoration or twice per view.
- Custom scrolling without bounce/elasticity.
- Look to Scroll in lists with many controls.

---

## Sheets
**Purpose:** View for a scoped task closely related to the current context, after which people return to the original view. **Platforms:** ios, ipados, macos, watchos (also tvos, visionos).

**Use when:** requesting specific information or completing a simple task (attach a file, choose a save location) (hig:sheets).
**Don't use when:** the flow is complex/long → iOS/iPadOS full-screen modal, macOS new window or full screen, visionOS Full Space (hig:sheets#Best-practices); repeated input while observing results in macOS → Panel (hig:sheets#macOS); watchOS for pure information/choice → Alert/Action sheet (hig:sheets#watchOS).

**Core rules:**
- Only one sheet at a time from the main interface; a follow-up sheet only after the first one is dismissed (hig:sheets#Best-practices).
- For supplementary elements that affect the main task, work nonmodally: iOS/iPadOS nonmodal sheet, macOS panel, visionOS split view (hig:sheets#Best-practices).
- Never Done alone: combine with Cancel (dismiss without saving) or Back (previous step); not all three (Cancel, Done, Back) at once (hig:sheets#Best-practices).
- Back is for navigation within the sheet, not for dismissing (hig:sheets#Anatomy).
- iOS/iPadOS single view: Cancel leading in the top toolbar, Done trailing; in multistep flows the placement varies per step (hig:sheets#iOS-iPadOS).
- Detents: large is supported automatically; add medium for progressive disclosure (e.g. share sheet); medium only prevents full height; full height for creation tasks (compose) (hig:sheets#iOS-iPadOS).
- Resizable sheets with a grabber (also operable with VoiceOver; tapping cycles detents) (hig:sheets#iOS-iPadOS).
- Support swipe-to-dismiss; with unsaved changes confirm via action sheet (hig:sheets#iOS-iPadOS).
- iPadOS: prefer page or form sheet style (hig:sheets#iOS-iPadOS).

**Platform specifics:**
- Modality: macOS, tvOS, visionOS, watchOS always modal; iOS/iPadOS modal or nonmodal (e.g. Notes formatting) (hig:sheets#Anatomy).
- macOS: card above the dimmed parent window; sensible default size, resizing if needed; other app windows remain usable; on opening, bring the parent window (and its document panels) to the front (hig:sheets#macOS).
- visionOS: doesn't slide in from the bottom edge of the window, centered in the field of view; size it so the window isn't (almost) completely covered (hig:sheets#visionOS).
- watchOS: full screen, semi-transparent with blur; only for custom titles/content, short and infrequent, not for navigation; a custom close label preferably as an SF Symbol, not styled like a page title (hig:sheets#watchOS).

**Key values:** medium detent ≈ half the height of the fully expanded sheet (mirror: "about half") (hig:sheets#iOS-iPadOS). Otherwise none.

**Implementation:** SwiftUI `sheet(item:onDismiss:content:)` / `sheet(isPresented:)`, detents via `presentationDetents([.medium, .large])`, grabber via `presentationDragIndicator(.visible)`, full screen via `fullScreenCover` (iOS/iPadOS); UIKit `UISheetPresentationController` (`detents`, `prefersGrabberVisible`), `UIModalPresentationStyle` (`.pageSheet`, `.formSheet`, `.fullScreen`); AppKit `NSViewController.presentAsSheet(_:)` (hig:sheets). SwiftUI modifier names other than `sheet` are not from the mirror.

**Common mistakes:**
- Sheet opens a sheet (stack).
- Only a Done button, no Cancel/Back.
- Complex multistep editor in a sheet instead of full screen/window.
- Swipe down discards changes without confirmation.

---

## Windows
**Purpose:** Frame for an app's UI and content, with system controls for opening, closing, moving, and resizing. **Platforms:** ipados, macos (also visionos; not supported in iOS, tvOS, watchOS).

**Use when:** multitasking or preserving context benefits (e.g. Mail compose in its own window); primary window for main navigation, auxiliary window for a self-contained task without navigation to other areas (hig:windows).
**Don't use when:** new windows would be opened by default and excessively (hig:windows#Best-practices).

**Core rules:**
- Adapt windows fluidly to all sizes (multitasking/multiwindow) (hig:windows#Best-practices).
- Open new windows deliberately; optionally offer "Open in New Window" via a context menu or the File menu (hig:windows#Best-practices).
- No custom window frames/controls, don't replicate the system look (hig:windows#Best-practices).
- In the UI say "window", not "scene" (hig:windows#Best-practices).
- macOS: use the system appearance for main/key/inactive; custom windows must represent state changes themselves (hig:windows#macOS-window-states).
- macOS: no critical information/actions in the bottom bar; only a little selection-related information, otherwise an inspector (hig:windows#macOS-window-states).
- iPadOS: inset toolbar buttons at the leading edge when window controls appear (hig:windows#iPadOS).
- visionOS: keep the glass background; initial size without empty areas, shape based on the content; set min/max size; keep 3D depth in the window low, otherwise use a volume (hig:windows#visionOS-windows).

**Platform specifics:**
- iPadOS: full-screen mode (App Switcher) or windowed (freely resizable, the system remembers size/position); consider a gesture (pinch) to open in a new window; for pure file previews `QLPreviewSceneActivationConfiguration`, but multiwindow support is mandatory (hig:windows#iPadOS).
- macOS: anatomy frame (window controls, toolbar, rarely a bottom bar) + body; states main (one per app), key (one systemwide, accepts input), inactive (without vibrancy) (hig:windows#macOS-window-anatomy, hig:windows#macOS-window-states).
- visionOS: styles window (default), volume, plain (without glass). Volumes for rich 3D content, usually dynamic scaling (fixed is the default), baseplate glow, max. one additional ornament not on the same edge as the toolbar/tab bar, orientation parallel to the floor or following the gaze (hig:windows#visionOS, hig:windows#visionOS-volumes).

**Key values:** visionOS default window 1280×720 pt; first window about 2 m in front of the person, apparent width about 3 m (hig:windows#visionOS-windows). Ornaments/baseplate glow from visionOS 2 (hig:windows#visionOS-volumes).

**Implementation:** SwiftUI `WindowGroup`, `OpenWindowAction` (`openWindow`), `DefaultWindowStyle`, `PlainWindowStyle`, `VolumetricWindowStyle`, `ornament(visibility:attachmentAnchor:contentAlignment:ornament:)`; UIKit `UIWindow`, `UIWindowScene.ActivationInteraction`; AppKit `NSWindow` (hig:windows).

**Common mistakes:**
- Every detail view opens a new window.
- Replicated title bar/traffic light buttons.
- Important actions in the macOS bottom bar.
- visionOS: opaque background instead of glass, overly large empty initial windows, no size limits.

---

## Distinctions: confirmation and secondary task

**Confirmation / decision**
| Situation | Component | Source |
|---|---|---|
| Unexpected problem, critical information, rare irreversible data destruction, purchase confirmation | Alert (`alert`) | (hig:alerts), (hig:alerts#Best-practices) |
| Choices related to an action the user deliberately initiated (delete/save/keep editing) | Action sheet (SwiftUI: `confirmationDialog`) | (hig:action-sheets#Best-practices) |
| Options the person invokes themselves | Menu, not action sheet | (hig:action-sheets#iOS-iPadOS) |
| Frequent, undoable action | no confirmation, undo | (hig:alerts#Best-practices) |
| Pure information | in-context notice instead of alert | (hig:alerts#Best-practices) |

"Confirmation dialog" is the SwiftUI name for the action sheet functionality, not a separate HIG component (hig:action-sheets).

**Secondary task**
| Situation | Component | Source |
|---|---|---|
| Little information/functionality, brief, anchored to the control, regular width / macOS | Popover | (hig:popovers#Best-practices) |
| Scoped, simple task with return to context | Sheet (iPhone: detents) | (hig:sheets) |
| Supplementary tools while the main task continues | iOS/iPadOS nonmodal sheet, macOS panel, visionOS split view | (hig:sheets#Best-practices) |
| Complex, long, media/camera, multistep editing | iOS/iPadOS full-screen modal; macOS new window/full screen; visionOS Full Space | (hig:sheets#Best-practices), (hig:modality#Best-practices) |
| Compact size class | Sheet instead of popover | (hig:popovers#iOS-iPadOS) |

**Ambiguities in the mirror:**
- Mail example: the action sheets page names two options (delete/save draft), the alerts page three (additionally "keep editing") (hig:action-sheets#Best-practices vs. hig:alerts#iOS-iPadOS).
- Destructive style: action sheets → always highlight destructive options; alerts → only for a destructive action not deliberately chosen. Not a contradiction in the strict sense (different components), but keep in mind during implementation.
- Sheet buttons in multistep flows: the page refers to illustrations (first/subsequent/last step); the text names no specific placement (hig:sheets#iOS-iPadOS).
