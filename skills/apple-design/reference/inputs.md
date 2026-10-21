# Inputs – input methods (HIG section "Inputs")

Condensed reference for all input pages of the Apple HIG. Source: local HIG mirror (`~/.apple-design/hig/pages/`, sync 2026-10-21). Citations as `(hig:<slug>)` or `(hig:<slug>#Anchor)`. Rules paraphrased; tables of gestures and shortcuts are factual overviews.

Shortcut notation: symbols in HIG order ⌃ Control, ⌥ Option, ⇧ Shift, ⌘ Command (hig:keyboards#Custom-keyboard-shortcuts).

## Contents

1. [Platform matrix](#platform-matrix)
2. [Touch and gestures](#touch-and-gestures)
3. [Keyboards](#keyboards)
4. [Pointing devices](#pointing-devices)
5. [Digital Crown](#digital-crown)
6. [Apple Pencil and Scribble](#apple-pencil-and-scribble)
7. [Game controls](#game-controls)
8. [Focus and selection](#focus-and-selection)
9. [Action button](#action-button)
10. [Camera Control](#camera-control)
11. [Gyroscope/Accelerometer, Nearby interactions](#gyroscopeaccelerometer-nearby-interactions)
12. [Remotes (tvOS)](#remotes-tvos)
13. [Eyes (visionOS)](#eyes-visionos)
14. [Observations and ambiguities](#observations-and-ambiguities)

---

## Platform matrix

According to each page's platform statement ("Not supported in …"):

| Input | iOS | iPadOS | macOS | watchOS | tvOS | visionOS | Slug |
|---|---|---|---|---|---|---|---|
| Gestures | yes | yes | yes (trackpad/Magic Mouse) | yes | yes | yes | gestures |
| Keyboards (physical) | yes | yes | yes | no | yes | yes | keyboards |
| Pointing devices | yes | yes | yes | no | no | yes | pointing-devices |
| Digital Crown | no | no | no | yes | no | yes (system only) | digital-crown |
| Apple Pencil & Scribble | no | yes | no | no | no | no | apple-pencil-and-scribble |
| Game controls | yes | yes | yes | no | yes | yes | game-controls |
| Focus and selection | no | yes | yes | no | yes | yes | focus-and-selection |
| Action button | yes | no | no | yes | no | no | action-button |
| Camera Control | yes | no | no | no | no | no | camera-control |
| Gyro/Accelerometer | yes | yes | (listed) | yes | Siri Remote | (listed) | gyro-and-accelerometer |
| Nearby interactions | yes | yes | no | yes | no | no | nearby-interactions |
| Remotes | – | – | – | – | yes | – | remotes |
| Eyes | – | – | – | – | – | yes | eyes |

Default input per platform (from a games perspective, hig:designing-for-games#Enable-intuitive-interactions):

| Platform | Default | Additional |
|---|---|---|
| iOS | Touch | Game controller |
| iPadOS | Touch | Game controller, keyboard, mouse, trackpad, Apple Pencil |
| macOS | Keyboard, mouse, trackpad | Game controller |
| tvOS | Remote | Game controller, keyboard, mouse, trackpad |
| visionOS | Touch (per table; in practice eyes + hands) | Game controller, keyboard, mouse, trackpad, spatial game controller |
| watchOS | Touch | – |

---

## Touch and gestures

Purpose: physical motion that directly affects an object – on a touchscreen, in the air (visionOS), or via trackpad, mouse, remote, or a controller with a touch surface (hig:gestures).

### Core rules

- Always offer more than one way to interact (voice, keyboard, Switch Control); never assume that someone can perform a particular gesture (hig:gestures#Best-practices).
- Use familiar gestures only for their expected meaning; don't assign app-specific special actions to tap/swipe and don't invent a custom gesture for standard actions like activating a button or scrolling (hig:gestures#Best-practices).
- Respond immediately and give feedback during the gesture that makes the result and the required range of motion recognizable (hig:gestures#Best-practices).
- Indicate when a gesture isn't available (e.g. locked object, disabled button clearly distinguishable) – otherwise the app appears frozen (hig:gestures#Best-practices).
- Custom gestures only when necessary (frequent specialized tasks, games, drawing apps); they must be discoverable, easy to perform, distinguishable, and never the only way to perform an important action (hig:gestures#Custom-gestures).
- Shortcut gestures supplement standard controls, they don't replace them – e.g. edge swipe to go back **plus** Back button in the toolbar (hig:gestures#Custom-gestures).
- Don't conflict with system gestures (edge swipe in watchOS, hand roll for system overlays in visionOS); defer the system gesture only in games/immersive experiences (hig:gestures#Custom-gestures).

### Standard gestures (all platforms)

| Gesture | Supported in | Common action |
|---|---|---|
| Tap | iOS, iPadOS, macOS, tvOS, visionOS, watchOS | Activate a control, select an item |
| Swipe | iOS, iPadOS, macOS, tvOS, visionOS, watchOS | Reveal actions/controls, dismiss views, scroll |
| Drag | iOS, iPadOS, macOS, tvOS, visionOS, watchOS | Move a UI element |
| Touch (or pinch) and hold | iOS, iPadOS, tvOS, visionOS, watchOS | Show additional controls/functionality |
| Double tap | iOS, iPadOS, macOS, tvOS, visionOS, watchOS | Zoom in/out; primary action on Apple Watch Series 9 / Ultra 2 |
| Zoom | iOS, iPadOS, macOS, tvOS, visionOS | Zoom a view, magnify content |
| Rotate | iOS, iPadOS, macOS, tvOS, visionOS | Rotate the selected item |

(hig:gestures#Standard-gestures)

### Additional gestures iOS/iPadOS

| Gesture | Action |
|---|---|
| Three-finger swipe | left: undo, right: redo |
| Three-finger pinch | in: copy text, out: paste |
| Four-finger swipe (iPadOS only) | Switch between apps |
| Shake | Undo / redo |

(hig:gestures#iOS-iPadOS)

- Allow simultaneous recognition of multiple gestures only when it helps – typically in games (joystick + fire buttons) (hig:gestures#iOS-iPadOS).

### Platform differences

- **macOS:** primarily keyboard + mouse; standard gestures via Magic Trackpad, Magic Mouse, or a controller with a touch surface (hig:gestures#macOS). For details see [Pointing devices](#pointing-devices).
- **watchOS – double tap (watchOS 11 and later):** scrolls lists/scroll views, switches vertical tabs; an app, widget, or Live Activity (in the Smart Stack) can designate a toggle/button as the primary action; in notifications it acts on the first nondestructive action (hig:gestures#watchOS).
  - Don't set a primary action in views with lists, scroll views, or vertical tabs (conflicts with navigation) (hig:gestures#watchOS).
  - Choose the most frequently used button of a nonscrolling view as the primary action (e.g. play/pause); API `handGestureShortcut(_:isEnabled:)`, `.primaryAction` (hig:gestures#watchOS).
- **tvOS:** standard gestures via Siri Remote/controller (hig:gestures#tvOS).
- **visionOS (brief):** indirect gestures (look + finger tap) preferred for UI; direct gestures (touching) for objects within reach and infrequent use; custom gestures only in a Full Space with hand-tracking permission; keep the area around the hand clear for system overlays (hig:gestures#visionOS).

---

## Keyboards

Purpose: physical keyboard for text, games, and app control; can be connected to any device except Apple Watch. Mac users almost always, iPad users often (hig:keyboards).

### Core rules

- Support Full Keyboard Access (iOS, iPadOS, macOS, visionOS); test via Accessibility in Settings (hig:keyboards#Best-practices).
- iPadOS: keyboard navigation for text fields, text views, sidebars, and collections – **not** for buttons, segmented controls, switches; those are reached via Full Keyboard Access (hig:keyboards#Best-practices).
- Respect standard shortcuts; create custom shortcuts for frequent app actions instead of repurposing standard shortcuts (hig:keyboards#Standard-keyboard-shortcuts).
- Repurpose only if the standard action makes no sense in the app (example: ⌘I as "Get Info" in an app without text editing) (hig:keyboards#Standard-keyboard-shortcuts).
- Custom shortcuts only for the most frequently used app-specific commands – too many make the app hard to learn (hig:keyboards#Custom-keyboard-shortcuts).
- Modifiers as expected: ⌘ while dragging = move group; ⇧ while resizing = maintain aspect ratio; held arrow key = move by the smallest app unit (hig:keyboards#Custom-keyboard-shortcuts).
- Modifier order in the display is always: Control, Option, Shift, Command (hig:keyboards#Custom-keyboard-shortcuts).
- No ⇧ for the upper character of a two-character key – show the upper character directly (Help = ⌘?, not ⇧⌘/) (hig:keyboards#Custom-keyboard-shortcuts).
- Let the system localize shortcuts and mirror them for RTL (hig:keyboards#Custom-keyboard-shortcuts).
- Don't create a new shortcut by adding a modifier to an existing one for an unrelated command (e.g. ⇧⌘Z only for redo) (hig:keyboards#Custom-keyboard-shortcuts).
- Combine additional modifiers only with letters; some layouts need modifiers for special characters (French keyboard: ⌥5 = "{") (hig:keyboards#Custom-keyboard-shortcuts).

### Modifier recommendation

| Modifier | Symbol | Recommendation |
|---|---|---|
| Command | ⌘ | Main modifier for custom shortcuts |
| Shift | ⇧ | Secondary, complements a related shortcut |
| Option | ⌥ | Sparingly, for infrequent commands/power features |
| Control | ⌃ | Avoid – used systemwide (focus, screenshots) |

(hig:keyboards#Custom-keyboard-shortcuts)

### Standard keyboard shortcuts (complete per HIG table)

The HIG provides **one** table without platform separation; many entries are macOS system functions (Dock, Force Quit, Eject). A separate iPadOS list does not exist in the mirror (hig:keyboards#Standard-keyboard-shortcuts).

| Key | Shortcut | Action |
|---|---|---|
| Space | ⌘Space | Show/hide the Spotlight search field |
| | ⇧⌘Space | Varies |
| | ⌥⌘Space | Show the Spotlight results window |
| | ⌃⌘Space | Show the Special Characters window |
| Tab | ⇧Tab | Navigate backward through controls |
| | ⌘Tab | Move to the next most recently used open app |
| | ⇧⌘Tab | Move backward through open apps (sorted by recent use) |
| | ⌃Tab | Move focus to the next group of controls in a dialog or the next table (when Tab moves to the next cell) |
| | ⌃⇧Tab | Move focus to the previous group of controls |
| Esc | Esc | Cancel the current action/process |
| | ⌥⌘Esc | Open the Force Quit dialog |
| Eject | ⌃⌘Eject | Quit all apps (after saving) and restart |
| | ⌃⌥⌘Eject | Quit all apps (after saving) and shut down |
| F1 | ⌃F1 | Turn Full Keyboard Access on/off |
| F2 | ⌃F2 | Move focus to the menu bar |
| F3 | ⌃F3 | Move focus to the Dock |
| F4 | ⌃F4 | Move focus to the active (or next) window |
| | ⌃⇧F4 | Move focus to the previously active window |
| F5 | ⌃F5 | Move focus to the toolbar |
| | ⌘F5 | Turn VoiceOver on/off |
| F6 | ⌃F6 | Move focus to the first (or next) panel |
| | ⌃⇧F6 | Move focus to the previous panel |
| F7 | ⌃F7 | Temporarily override the current keyboard access mode in windows/dialogs |
| F8 | – | Varies |
| F9 | – | Varies |
| F10 | – | Varies |
| F11 | – | Show desktop |
| F12 | – | Show/hide Dashboard |
| ` (grave accent) | ⌘` | Activate the next open window of the frontmost app |
| | ⇧⌘` | Activate the previous open window of the frontmost app |
| | ⌥⌘` | Move focus to the window drawer |
| - (hyphen) | ⌘- | Decrease the size of the selection |
| | ⌥⌘- | Zoom out (when screen zoom is enabled) |
| { (left bracket) | ⌘{ | Left-align the selection |
| } (right bracket) | ⌘} | Right-align the selection |
| \| (pipe) | ⌘\| | Center the selection |
| : (colon) | ⌘: | Show the Spelling window |
| ; (semicolon) | ⌘; | Find misspelled words in the document |
| , (comma) | ⌘, | Open the app's settings window |
| | ⌃⌥⌘, | Decrease screen contrast |
| . (period) | ⌘. | Cancel an operation |
| | ⌃⌥⌘. | Increase screen contrast |
| ? (question mark) | ⌘? | Open the app's Help menu |
| / (slash) | ⌥⌘/ | Turn font smoothing on/off |
| = (equal sign) | ⇧⌘= | Increase the size of the selection |
| | ⌥⌘= | Zoom in (when screen zoom is enabled) |
| 3 | ⇧⌘3 | Capture the screen to a file |
| | ⌃⇧⌘3 | Capture the screen to the clipboard |
| 4 | ⇧⌘4 | Capture a selection to a file |
| | ⌃⇧⌘4 | Capture a selection to the clipboard |
| 8 | ⌥⌘8 | Turn screen zoom on/off |
| | ⌃⌥⌘8 | Invert screen colors |
| A | ⌘A | Select all (document/window, or all characters in a text field) |
| | ⇧⌘A | Deselect all |
| B | ⌘B | Bold (toggle) |
| C | ⌘C | Copy the selection |
| | ⇧⌘C | Show the Colors window |
| | ⌥⌘C | Copy the style of the selected text |
| | ⌃⌘C | Copy the formatting of the selection (clipboard) |
| D | ⌥⌘D | Show/hide the Dock |
| | ⌃⌘D | Show the definition of the selected word in the Dictionary |
| E | ⌘E | Use the selection for a find |
| F | ⌘F | Open a Find window |
| | ⌥⌘F | Jump to the search field |
| | ⌃⌘F | Enter full screen |
| G | ⌘G | Find the next occurrence |
| | ⇧⌘G | Find the previous occurrence |
| H | ⌘H | Hide the windows of the current app |
| | ⌥⌘H | Hide the windows of all other apps |
| I | ⌘I | Italic (toggle) |
| | ⌘I | Show an Info window (assigned twice, see Observations) |
| | ⌥⌘I | Show an Inspector window |
| J | ⌘J | Scroll to the selection |
| M | ⌘M | Minimize the active window to the Dock |
| | ⌥⌘M | Minimize all windows of the active app |
| N | ⌘N | New document |
| O | ⌘O | Open dialog |
| P | ⌘P | Print dialog |
| | ⇧⌘P | Page Setup dialog |
| Q | ⌘Q | Quit the app |
| | ⇧⌘Q | Log out the user |
| | ⌥⇧⌘Q | Log out the user without confirmation |
| S | ⌘S | Save (new document or version) |
| | ⇧⌘S | Duplicate or "Save As" |
| T | ⌘T | Show the Fonts window |
| | ⌥⌘T | Show/hide the toolbar |
| U | ⌘U | Underline (toggle) |
| V | ⌘V | Paste at the insertion point |
| | ⇧⌘V | Paste as … (e.g. as quotation) |
| | ⌥⌘V | Apply the style of an object to the selection |
| | ⌥⇧⌘V | Paste and match the style of the surrounding text |
| | ⌃⌘V | Apply formatting to the selection |
| W | ⌘W | Close the active window |
| | ⇧⌘W | Close a file and its associated windows |
| | ⌥⌘W | Close all windows of the app |
| X | ⌘X | Cut |
| Z | ⌘Z | Undo |
| | ⇧⌘Z | Redo (when undo/redo are separate commands) |
| → | ⌘→ | Change the keyboard layout to the current layout of the Roman script |
| | ⇧⌘→ | Extend the selection to the next semantic unit (usually end of line) |
| | ⇧→ | Extend the selection one character to the right |
| | ⌥⇧→ | Extend the selection to the end of the word, then the end of the next word |
| | ⌃→ | Move focus to another value/cell in a view (e.g. table) |
| ← | ⌘← | Change the keyboard layout to the current layout of the system script |
| | ⇧⌘← | Extend the selection to the previous semantic unit (usually beginning of line) |
| | ⇧← | Extend the selection one character to the left |
| | ⌥⇧← | Extend the selection to the beginning of the word, then the beginning of the previous word |
| | ⌃← | Move focus to another value/cell in a view |
| ↑ | ⇧⌘↑ | Extend the selection upward to the next semantic unit (usually beginning of document) |
| | ⇧↑ | Extend the selection to the line above (same horizontal position) |
| | ⌥⇧↑ | Extend the selection to the beginning of the paragraph, then the beginning of the next paragraph |
| | ⌃↑ | Move focus to another value/cell in a view |
| ↓ | ⇧⌘↓ | Extend the selection downward to the next semantic unit (usually end of document) |
| | ⇧↓ | Extend the selection to the line below (same horizontal position) |
| | ⌥⇧↓ | Extend the selection to the end of the paragraph, then the end of the next paragraph (including the paragraph-end character for cut/copy/paste) |
| | ⌃↓ | Move focus to another value/cell in a view |

Shortcuts for input sources (not tied to menu commands):

| Shortcut | Action |
|---|---|
| ⌃Space | Switch between the current and the previous input source |
| ⌃⌥Space | Next input source in the list |
| [Modifier]⌘Space | Varies |
| ⌘→ | Layout of the Roman script |
| ⌘← | Layout of the system script |

(hig:keyboards#Standard-keyboard-shortcuts)

### Platform differences

- **iOS, iPadOS, macOS, tvOS:** no additional considerations; watchOS not supported (hig:keyboards#Platform-considerations).
- **iPadOS/macOS menus:** shortcuts appear in menu bar menus (see hig:the-menu-bar).
- **visionOS (brief):** holding ⌘ shows a shortcut overview by menu category (File, Edit, View …) as a flat list – shortcut titles must be understandable without submenu context (`discoverabilityTitle`); with a physical keyboard the system shows a virtual overlay with completions (hig:keyboards#visionOS).
- **Games:** key bindings, single-key commands, freely remappable – see [Game controls](#game-controls) (hig:game-controls#Keyboards).

---

## Pointing devices

Purpose: trackpad/mouse for precise navigation. Standard on the Mac together with the keyboard; on iPad and Vision Pro an additional way that doesn't replace touch/eyes/gestures (hig:pointing-devices).

### Core rules

- Respond consistently to mouse/trackpad gestures (e.g. "Swipe between pages" the same everywhere) (hig:pointing-devices#Best-practices).
- Don't redefine systemwide trackpad gestures (Dock, Mission Control); users can customize them (hig:pointing-devices#Best-practices).
- Same behavior across gestures, eyes, pointer, keyboard (hig:pointing-devices#Best-practices).
- Let the pointer automatically reveal minimized controls (Safari toolbar on iPad, video controls in full screen) (hig:pointing-devices#Best-practices).
- Modifier behavior (e.g. ⌥ while dragging = duplicate) must work the same with touch and pointer (hig:pointing-devices#Best-practices).

### iPadOS

- Implement band selection (iPadOS 15 and later) yourself in custom views (`UIBandSelectionInteraction`); standard collection views (not lists) support it (hig:pointing-devices#iPadOS).
- Distinguish pointer and finger only when it adds real value (e.g. precise click on a scrubber position) (hig:pointing-devices#iPadOS).
- Pointer is a circle by default; I-beam over text input (hig:pointing-devices#Pointer-shape-and-content-effects).
- Content effects:

| Effect | Behavior | Use | System default for |
|---|---|---|---|
| Highlight | Pointer becomes a translucent rounded rect behind the control, slight parallax | Small element, transparent background | Bar buttons, tab bars, segmented controls, edit menus |
| Lift | Element scales up, shadow + specular highlight, appears to float | Small element, opaque background | App icons, Control Center buttons |
| Hover | Custom values for scale, tint, shadow; pointer shape stays | Large elements | – |

(hig:pointing-devices#Standard-pointers-and-effects)

- Pointer magnetism: automatic with lift/highlight and text input, not with hover (hig:pointing-devices#Pointer-magnetism).
- Hit regions: about **12 pt** padding around elements with a bezel, about **24 pt** around elements without a bezel (hig:pointing-devices#Standard-pointers-and-effects).
- Contiguous hit regions for custom bar buttons (otherwise the pointer snaps back to its default shape) (hig:pointing-devices#Standard-pointers-and-effects).
- For lift on nonstandard shapes, specify a corner radius (`UIPointerShape.roundedRect(_:radius:)`) (hig:pointing-devices#Standard-pointers-and-effects).
- Custom pointer: system effects for standard-like elements, consistent, no decorative effects, simple shapes, useful annotations (e.g. X/Y values) yes, instructional text on the pointer no (hig:pointing-devices#Customizing-pointers).
- Scale only where there's room (not for table rows); never shadow without scale (hig:pointing-devices#Customizing-pointers).
- Pointer accessories (`UIPointerAccessory`): simple images; state changes via accessory transition (e.g. `plus` → `circle.slash`) (hig:pointing-devices#Pointer-accessories).

### macOS – clicks and gestures

| Click/gesture | Expected behavior | Mouse | Trackpad |
|---|---|---|---|
| Primary click | Select/activate | yes | yes |
| Secondary click | Context menu | yes | yes |
| Scrolling | Move content | yes | yes |
| Smart zoom | Zoom in on content (web, PDF) | yes | yes |
| Swipe between pages | Page forward/back | yes | yes |
| Swipe between full-screen apps | Between full-screen apps/Spaces | yes | yes |
| Mission Control (mouse: two-finger double tap; trackpad: 3/4 fingers up) | Mission Control | yes | yes |
| Lookup/Data detectors (force click 1 finger or tap 3 fingers) | Lookup window | – | yes |
| Tap to click | Tap instead of click | – | yes |
| Force click | Quick Look/Lookup; pressure-sensitive controls | – | yes |
| Pinch (2 fingers) | Zoom | – | yes |
| Rotate (2 fingers circling) | Rotate | – | yes |
| Notification Center (swipe from trackpad edge) | Notification Center | – | yes |
| App Exposé (3/4 fingers down) | App's windows in Exposé | – | yes |
| Launchpad (pinch thumb + 3 fingers) | Launchpad | – | yes |
| Show Desktop (spread thumb + 3 fingers) | Reveal the desktop | – | yes |

(hig:pointing-devices#macOS)

### macOS – standard pointers (`NSCursor`)

| Pointer | Meaning | API |
|---|---|---|
| Arrow | Default | `arrow` |
| Closed hand | Content in the view is being moved (e.g. map) | `closedHand` |
| Open hand | Moving is possible | `openHand` |
| Contextual menu | Context menu available (usually only while ⌃ is pressed) | `contextualMenu` |
| Crosshair | Precise rectangular selection | `crosshair` |
| Disappearing item | Dragged item disappears on drop (original remains) | `disappearingItem` |
| Drag copy | Copy instead of move (⌥ while dragging) | `dragCopy` |
| Drag link | Create alias (⌥⌘ while dragging) | `dragLink` |
| Horizontal I-beam | Horizontal text selection | `iBeam` |
| Vertical I-beam | Vertical text selection | `iBeamCursorForVerticalLayout` |
| Operation not allowed | Dropping here isn't possible | `operationNotAllowed` |
| Pointing hand | Link | `pointingHand` |
| Resize up/down/left/right, left/right, up/down | Change size/position in direction | `resizeUp`, `resizeDown`, `resizeLeft`, `resizeRight`, `resizeLeftRight`, `resizeUpDown` |

(hig:pointing-devices#Pointers)

- **visionOS (brief):** gaze target determines pointer context; pointer disappears during trackpad gestures (hig:pointing-devices#visionOS). iOS: no additional considerations; tvOS/watchOS not supported.

---

## Digital Crown

Purpose: hardware input on Apple Watch (system + apps) and Vision Pro (system only) (hig:digital-crown).

### Apple Watch

- From watchOS 10 the primary navigation input: Smart Stack on the watch face, Home Screen, vertically paginated tabs, lists, pages of variable height (hig:digital-crown#Apple-Watch).
- Apps receive **no** Crown presses – reserved for the system (Home Screen) (hig:digital-crown#Apple-Watch).
- Anchor app navigation to the Crown (vertical list/tab/scroll views) and offer touch equivalents in parallel (hig:digital-crown#Apple-Watch).
- Use the Crown to inspect data where no navigation is needed (example World Clock: advance the time of day) (hig:digital-crown#Apple-Watch).
- Give visible feedback for every rotation; otherwise the Crown seems nonfunctional (hig:digital-crown#Apple-Watch).
- Tie the rate of change to the rotation speed; values must remain precisely selectable (hig:digital-crown#Apple-Watch).
- Use standard haptics (linear detents); turn them off if they don't match the animation; for tables with very different row heights consider linear instead of row-based detents (hig:digital-crown#Apple-Watch).

### Vision Pro (brief)

Volume, level of immersion (portal, environment, Full Space), recenter, accessibility, exit app. Apps receive no direct Crown information (hig:digital-crown#Apple-Vision-Pro).

---

## Apple Pencil and Scribble

Purpose: precise drawing, writing, marking on iPad; Scribble = handwriting in any text field, recognized on-device. iPadOS only (hig:apple-pencil-and-scribble).

### Core rules

- Support what people expect from real pens (e.g. writing in margins) (hig:apple-pencil-and-scribble#Best-practices).
- All controls must also respond to Pencil – don't force a switch to the finger (hig:apple-pencil-and-scribble#Best-practices).
- Mark immediately on touchdown, without selecting a mode/button first (hig:apple-pencil-and-scribble#Best-practices).
- Use tilt (altitude), force, azimuth, barrel roll for stroke character; pressure for continuous properties (opacity, brush size) (hig:apple-pencil-and-scribble#Best-practices).
- Direct connection to content; don't trigger distant effects (hig:apple-pencil-and-scribble#Best-practices).
- Left- and right-handed users: no controls that can be obscured, or make them movable (hig:apple-pencil-and-scribble#Best-practices).

### Interactions

| Interaction | Rules |
|---|---|
| Hover | Preview of the upcoming mark; don't vary with height; don't trigger actions; preview with the midpoint value of dynamic ranges; hover preview only for Pencil, not for pointer (hig:apple-pencil-and-scribble#Hover) |
| Double tap | Respect the user setting (default: tool ↔ eraser; alternatives: previous tool, color picker, nothing); custom behavior only optional and not the default; no content-changing/destructive actions (hig:apple-pencil-and-scribble#Double-tap) |
| Squeeze (Pencil Pro) | Single, discrete action; result near the pencil tip; nondestructive, undoable; users can assign squeeze to an App Shortcut; only with display on and without contact (hig:apple-pencil-and-scribble#Squeeze) |
| Barrel roll (Pencil Pro) | Change only marking behavior (e.g. stroke angle), never navigation/controls (hig:apple-pencil-and-scribble#Barrel-roll) |

### Scribble

- Works by default in all standard text components except password fields; don't require tapping custom fields first (hig:apple-pencil-and-scribble#Scribble).
- Offer Scribble wherever text is natural, even without a visible field (`UIIndirectScribbleInteraction`, example Reminders) (hig:apple-pencil-and-scribble#Scribble).
- While writing: don't show autocompletion, hide the placeholder immediately, don't move/scale the field, no autoscroll (hig:apple-pencil-and-scribble#Scribble).
- Enough writing space: enlarge the field before writing starts or during pauses (`UIScribbleInteraction`) (hig:apple-pencil-and-scribble#Scribble).

### Custom drawing (PencilKit)

- When drawing on a PDF/photo, turn off dynamic Dark Mode color adaptation (hig:apple-pencil-and-scribble#Custom-drawing).
- In compact environments, custom undo/redo buttons (the tool picker has none there); support three-finger undo (hig:apple-pencil-and-scribble#Custom-drawing).

---

## Game controls

Purpose: precise game control via touch, physical controllers, keyboard (hig:game-controls).

### Touch controls (iOS/iPadOS, framework `TouchController`)

- Virtual controls only when it makes sense; where possible, direct interaction with game objects (hig:game-controls#Touch-controls).
- Placement: respect safe areas, not over the Home indicator/Dynamic Island; frequent buttons near the thumb, secondary ones (menus) at the top (hig:game-controls#Touch-controls).
- Minimum sizes: frequent controls **44x44 pt**, less important ones (menus) **28x28 pt** (hig:game-controls#Touch-controls).
- Visible (even under the finger, e.g. glow) and tactile pressed state plus sound/haptics (hig:game-controls#Touch-controls).
- Symbols that show the action – no controller names like A, X, R1 (hig:game-controls#Touch-controls).
- Show/hide controls depending on context; combine actions (double tap, touch and hold for variants) (hig:game-controls#Touch-controls).
- Movement on the left, camera on the right; make the thumbstick appear where the thumb lands; camera via direct pan instead of a thumbstick (hig:game-controls#Touch-controls).

### Physical controllers

- Always fall back to the platform's default input (hig:game-controls#Physical-controllers).
- tvOS/visionOS may require a controller (App Store badge "Game Controller Required", `GCRequiresControllerUserInteraction`); detect a missing controller and prompt kindly to connect one (hig:game-controls#Physical-controllers).
- Detect controllers automatically; show labels/glyphs of the actually connected controller (`GCControllerElement`); with multiple controllers, use the active one (hig:game-controls#Physical-controllers).
- SF Symbols instead of text for controller elements (hig:game-controls#Physical-controllers).

UI mapping outside of gameplay (all Apple platforms):

| Button | Behavior in UI |
|---|---|
| A | Activate a control |
| B | Cancel / back |
| X, Y | – |
| Left/Right shoulder | To another screen/section left/right |
| Left/Right trigger | – |
| Thumbsticks, D-pad | Move selection |
| Home/Logo | Reserved by the system |
| Menu | Game settings / pause |

(hig:game-controls#Physical-controllers)

### Keyboard (games)

- Prefer single-key commands (I = Inventory, M = Map, Space = main action) (hig:game-controls#Keyboards).
- Test on an Apple keyboard (consider mapping ⌃ to ⌘, which sits next to Space) (hig:game-controls#Keyboards).
- Consider proximity to WASD and grouping of related actions (number keys); make key bindings freely remappable (hig:game-controls#Keyboards).

- **visionOS (brief):** treat spatial game controllers (e.g. PlayStation VR2 Sense) like hands: look + trigger = indirect, reach + trigger = direct (hig:game-controls#visionOS). watchOS: no controllers.

---

## Focus and selection

Purpose: focus shows what an interaction targets; navigation via keyboard, remote, controller. Focus often also selects, except when that would cause a disruptive context change (hig:focus-and-selection).

### Core rules

- Use system focus effects; custom only when absolutely necessary (hig:focus-and-selection#Best-practices).
- Don't change focus without user action. Exception: discrete directional input and the focused element disappears → move to an adjacent element; otherwise hide the focus indicator (hig:focus-and-selection#Best-practices).
- iPadOS/macOS: focus only for content elements (list items, text/search fields), not for buttons, sliders, toggles (Full Keyboard Access covers those). tvOS: every element focusable (hig:focus-and-selection#Best-practices).
- Focus ring for text/search fields, highlight for lists/collections; focused list items: white text + accent color background, unfocused gray (hig:focus-and-selection#Best-practices).

### Platform differences

- **iPadOS (15 and later):** focus groups. Tab jumps between groups (sidebar, grid, list), arrow keys within a group; order leading→trailing, top→bottom. Halo (focus ring) customizable (`UIFocusHaloEffect`); groups via `focusGroupIdentifier`, primary element via `UIFocusGroupPriority`. Highlight (accent-color text) is not a focus effect (hig:focus-and-selection#iPadOS).
- **macOS:** focus ring / highlight as above; Full Keyboard Access covers controls (hig:focus-and-selection#Best-practices).
- **tvOS (brief):** directional focus, parallax; up to five states (unfocused, focused, highlighted, selected, unavailable); provide assets at the enlarged focus size; no pointer; in full screen, gestures act on content, not focus (hig:focus-and-selection#tvOS).
- **visionOS (brief):** same focus system for external input devices; gaze highlighting is the hover effect, not focus (hig:focus-and-selection#visionOS).
- iOS, watchOS: not supported.

---

## Action button

Purpose: hardware button on supported iPhone and Apple Watch models for App Shortcuts or system functions; on Apple Watch Ultra additionally Workout/Dive (hig:action-button).

### Core rules

- Offer a selection of essential functions as App Shortcuts; no shortcut just to open the app (the system does that) (hig:action-button#Best-practices).
- Labels (visible in Settings): title case, verb first, present tense, without articles/prepositions, **maximum three words** ("Start Race") (hig:action-button#Best-practices).
- No custom instructions that repeat the system help in Settings (hig:action-button#Best-practices).

### Platform differences

- **iOS:** perform the action without losing context – Live Activities and snippets instead of launching the app (example "Set Timer") (hig:action-button#iOS).
- **watchOS:** first press e.g. waypoint, dive, workout; subsequent presses as a logical secondary function (mark segment, next discipline) – usually only one; subsequent presses extend rather than end (stopping in the UI); Action + side button together = pause (exception: diving) (hig:action-button#watchOS).
- iPadOS, macOS, tvOS, visionOS: not supported.

---

## Camera Control

Purpose: hardware control on iPhone 16 / iPhone 16 Pro (as of the page's state), opens the app's camera experience; light press shows the overlay, light double press shows available controls, swiping adjusts values (hig:camera-control).

- Control types: **slider** (range of values) and **picker** (discrete options); system controls for zoom and exposure can optionally be included (hig:camera-control#Anatomy).
- SF Symbols only (no custom symbols); symbols show function, not state (hig:camera-control#Best-practices).
- Short control names (Dynamic Type, otherwise they cover the viewfinder) (hig:camera-control#Best-practices).
- Units on slider values (EV, %, custom string; `localizedValueFormat`) and define prominent values (`prominentValues`) (hig:camera-control#Best-practices).
- UI outside the overlay zone (portrait and landscape); no duplicate controls in UI and overlay (hig:camera-control#Best-practices).
- Enable/disable controls per camera mode – don't add/remove them at runtime (hig:camera-control#Best-practices).
- Frequent controls in the middle, infrequent ones at the edges; the system remembers the most recently used control (hig:camera-control#Best-practices).
- Offer a locked camera capture extension (launch from the Lock Screen, Home Screen, other apps) (hig:camera-control#Best-practices, hig:controls#Camera-experiences-on-a-locked-device).
- iOS only.

---

## Gyroscope/Accelerometer, Nearby interactions

**Gyroscope and accelerometer** (Core Motion; iOS, iPadOS, watchOS; tvOS via Siri Remote) (hig:gyro-and-accelerometer):
- Collect motion data only when there is a concrete benefit (hig:gyro-and-accelerometer#Best-practices).
- Access requires a purpose string in the permission dialog (hig:gyro-and-accelerometer#Best-practices).
- Outside active gameplay, no direct UI manipulation via motion (hard to reproduce, physically demanding, battery) (hig:gyro-and-accelerometer#Best-practices).

**Nearby interactions** (Ultra Wideband, framework `NearbyInteraction`; iOS, iPadOS, watchOS) (hig:nearby-interactions):
- Think about the task from the perspective of the physical world (e.g. handing off audio to HomePod mini by moving closer) (hig:nearby-interactions#Best-practices).
- Use distance, direction, context; vary feedback with proximity; continuous feedback; combine visual, audible, haptic (hig:nearby-interactions#Best-practices).
- Never the only way to perform a task (hig:nearby-interactions#Best-practices).
- Encourage portrait orientation (implicitly, not via instruction); sensor field of view like the Ultra Wide camera (iPhone 11 and later) – outside it only distance, no direction; explain obstructions in onboarding (hig:nearby-interactions#Device-usage).
- iOS: distance and direction; watchOS: distance only, app must be in the foreground (hig:nearby-interactions#Platform-considerations).

---

## Remotes (tvOS)

Only for completeness (outside the focus): standard gestures for standard actions; couple gestures with focus direction; distinguish press (deliberate) vs. tap (navigate), don't evaluate taps during live video; Back opens the parent (in a game: pause menu); Play/Pause controls playback; EPG buttons as expected (hig:remotes).

| Button/area | App | Game |
|---|---|---|
| Touch surface (swipe) | Navigate, change focus | D-pad |
| Touch surface (press) | Activate, navigate deeper | Primary button |
| Back | Back / Apple TV Home | Pause/resume, back, main menu, Home |
| Play/Pause | Start/pause playback | Secondary button, skip intro |

(hig:remotes#Buttons)

---

## Eyes (visionOS)

Summary: gaze selects the target, the system shows the hover effect; for privacy reasons the app isn't told where the person is looking – only the tap (hig:eyes).

- Offer multiple ways to interact (accessibility) (hig:eyes#Best-practices).
- Content within the field of view; place reading material at least **1 m** away (hig:eyes#Best-practices).
- Spacing between interactive elements: at least **16 pt** padding around each element or centers at least **60 pt** apart (hig:eyes#Making-items-easy-to-see).
- Prefer rounded shapes; compound components with a shared hover region; no area-filling repeating patterns; avoid motion near the gaze target (hig:eyes#Making-items-easy-to-see, hig:eyes#Encouraging-interaction).
- Custom hover effects run outside the app process (no code on gaze); use sparingly; delay: none (subtle), short (tab bar expansion), long (tooltip); keep one primary view stable (hig:eyes#Custom-hover-effects).

---

## Observations and ambiguities

- **Shortcut table without platform assignment:** hig:keyboards contains only one shared table that mostly describes macOS system functions; a separate iPadOS shortcut list doesn't exist in the mirror. For iPadOS, therefore, only the app-related entries (⌘C/V/X/Z, ⌘N, ⌘F, ⌘W, ⌘, …) transfer meaningfully – this is an inference, not an HIG statement.
- **⌘I assigned twice** (italic and Info window) – as in the HIG table; the page cites ⌘I as an example of permissible repurposing when no text editing exists.
- **F12 "Dashboard"**: the table still lists Dashboard, which no longer exists in current macOS versions – the table appears partly outdated; likewise "window drawer" (⌥⌘`).
- **⌘←/⌘→** are listed in the table only as keyboard layout switches; the cursor jump to beginning/end of line is missing. Navigation shortcuts without ⇧ (⌥←, ⌘↑, etc.) are generally not listed.
- Typo in the source: "Control- F3" (space) – normalized here to ⌃F3.
- **Camera Control** mentions only iPhone 16 / 16 Pro; whether later models are meant, the page doesn't say (update state 2024-09-09).
- **watchOS double tap**: hig:gestures mentions Apple Watch Series 9 and Ultra 2 in the gestures table, in the body text "watchOS 11 and later" without a model list.
- **Default input visionOS = "Touch"** in hig:designing-for-games contradicts the rest of the documentation (eyes + indirect gestures, hig:designing-for-visionos); watchOS = "Touch" ignores the Digital Crown as the primary navigation input (hig:digital-crown).
- **Gyroscope page** lists macOS and visionOS as platforms, but the text mentions only iOS, iPadOS, watchOS, and tvOS (Siri Remote).
- hig:designing-for-ios still links to the old slug `spatial-interactions` (now `nearby-interactions`, renamed 2023-06-21).
