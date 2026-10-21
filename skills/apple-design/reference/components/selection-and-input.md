# Selection and input – Components
> Source: Apple HIG, local mirror (as of 2026-10-21). Paraphrased. Sources: `(hig:<slug>)`, `(hig:<slug>#Anchor)`.

Controls that let users choose, set, or enter values: text, numbers, dates, colors, on/off, choice among options. Relevant for iOS/iPadOS/macOS/watchOS; digit entry views are tvOS-only, combo boxes and image wells macOS-only.

Contents: [Color wells](#color-wells) · [Combo boxes](#combo-boxes) · [Digit entry views](#digit-entry-views) · [Image wells](#image-wells) · [Pickers](#pickers) · [Segmented controls](#segmented-controls) · [Sliders](#sliders) · [Steppers](#steppers) · [Text fields](#text-fields) · [Toggles](#toggles) · [Virtual keyboards](#virtual-keyboards)

### Decision guide for this group
- **Choice among 2 to about 5 closely related options, state should be visible** → Segmented control (iPhone max. about 5, wide UI about 5–7) (hig:segmented-controls#Best-practices). Not available on watchOS.
- **Short list, save space** → pull-down button / pop-up button instead of picker (hig:pickers#Best-practices); macOS: with more than about 5 exclusive options, pop-up button instead of radio buttons (hig:toggles#Radio-buttons).
- **Medium to long, logically ordered list** → Picker (hig:pickers#Best-practices). **Very long list** → List/Table (possibly with index) (hig:pickers#Best-practices).
- **Switching between completely separate app areas** → tab bar, not segmented control (hig:segmented-controls#iOS-iPadOS); macOS main window area → tab view (hig:segmented-controls#macOS).
- **On/off** → iOS: switch only in a list row, otherwise a button with toggle behavior (hig:toggles#iOS-iPadOS); macOS: a single setting preferably a checkbox, emphasized/group-controlling settings a switch (hig:toggles#Switches, hig:toggles#Radio-buttons).
- **Continuous value in a range** → Slider; **small incremental change** → Stepper; **exact value** → additionally a text field (hig:sliders#Best-practices, hig:steppers#Best-practices).
- **Free text + suggestion list (macOS)** → Combo box (hig:text-fields#macOS).

---

## Color wells
**Purpose:** Field that shows a color and opens a color picker on tap/click to change the color of text, shapes, and the like. **Platforms:** ios, ipados, macos (visionos); not supported in tvOS, watchOS.
**Use when:** users adjust colors of content/elements. **Don't use when:** only a small fixed color selection is needed (then e.g. segmented control/menu – author's inference, not HIG).
**Core rules:**
- Prefer the system color picker: familiar, consistent across platforms, saved color sets are available across apps (hig:color-wells#Best-practices).
- A custom picker UI is allowed but should add value (hig:color-wells).
- Update the well immediately to the chosen color (hig:color-wells#macOS).
**Platform specifics:**
- macOS: the well is highlighted on click, opens the picker, then shows the new color; drag and drop between wells and from the picker into the well (hig:color-wells#macOS).
- iOS/iPadOS/visionOS: no additional guidance.
**Key values:** none in the mirror.
**Implementation:** SwiftUI `ColorPicker` (not listed on the page, but standard API); UIKit `UIColorWell`, `UIColorPickerViewController`; AppKit `NSColorWell`.
**Common mistakes:** Building a custom color picker without need; missing drag and drop on macOS; well shows the old color after selection.

## Combo boxes
**Purpose:** Combination of a text field and a pull-down button – free input or choice from predefined values. **Platforms:** macos only.
**Use when:** users mostly choose from likely values but may also enter their own. **Don't use when:** only predefined values are allowed (then pop-up button – author's inference).
**Core rules:**
- Populate the field with a sensible default from the list; it doesn't have to be the first entry (hig:combo-boxes#Best-practices).
- Precede it with an introductory label (title-style capitalization, ending with a colon) (hig:combo-boxes#Best-practices).
- Offer relevant, likely choices (hig:combo-boxes#Best-practices).
- Keep list entries no wider than the text field, otherwise they are truncated (hig:combo-boxes#Best-practices).
- Note: custom entries are not automatically added to the list (hig:combo-boxes).
**Platform specifics:** Not supported in iOS, iPadOS, tvOS, visionOS, watchOS (hig:combo-boxes#Platform-considerations).
**Key values:** none in the mirror.
**Implementation:** AppKit `NSComboBox`. No SwiftUI equivalent named in the mirror.
**Common mistakes:** Empty field without a default; list entries too wide; missing label.

## Digit entry views
**Purpose:** Full-screen view for entering a sequence of digits (e.g. PIN) via a digit keyboard. **Platforms:** tvos only; not supported in iOS, iPadOS, macOS, visionOS, watchOS.
**Use when:** a PIN/code is requested on Apple TV. **Don't use when:** another platform (there, a text field with a suitable keyboard type).
**Core rules:**
- Use secure digit fields (asterisks) for sensitive data (hig:digit-entry-views#Best-practices).
- Explain with a title and prompt what the digits are being entered for (hig:digit-entry-views#Best-practices).
**Platform specifics:** tvOS shows a digit keyboard on activation (hig:virtual-keyboards#tvOS).
**Key values:** none in the mirror.
**Implementation:** TVUIKit `TVDigitEntryViewController`.
**Common mistakes:** Showing the PIN in plain text; no context about what the code is for.

## Image wells
**Purpose:** Editable variant of an image view: set the image via copy/paste, delete, or drag and drop. **Platforms:** macos only.
**Use when:** users assign/replace an image (e.g. avatar, document image). **Don't use when:** the image is only displayed (then image view) (hig:image-wells).
**Core rules:**
- Show the default image again when the content of a required well is deleted (hig:image-wells#Best-practices).
- When supporting copy/paste, provide the standard menu items and shortcuts in the Edit menu (hig:image-wells#Best-practices, hig:the-menu-bar#Edit-menu).
- Allow dragging in without prior selection (hig:image-wells).
**Platform specifics:** Not supported in iOS, iPadOS, tvOS, visionOS, watchOS.
**Key values:** none in the mirror.
**Implementation:** AppKit `NSImageView` (editable).
**Common mistakes:** Empty well for a required image; copy/paste only via context menu instead of Edit menu/shortcuts.

## Pickers
**Purpose:** One or more scrollable lists of distinct values to choose from (incl. date picker). **Platforms:** ios, ipados, macos, watchos (tvos only via SwiftUI, visionos).
**Use when:** choosing from medium-length to long, predictably ordered lists of values, or a date/time. **Don't use when:** only a few options (→ pull-down button) or very many entries (→ list/table with index) (hig:pickers#Best-practices).
**Core rules:**
- Use pickers for medium to long lists; for short lists a pull-down button, for very large ones a list/table (hig:pickers#Best-practices).
- Order values logically and predictably (e.g. alphabetically), since many values are hidden (hig:pickers#Best-practices).
- Show the picker in context (below/near the field, at the bottom of the window, or in a popover), not in a separate view (hig:pickers#Best-practices).
- Reduce minute granularity where sensible; the interval must divide 60 evenly (hig:pickers#Best-practices).
- On iOS use the compact style when space is limited (hig:pickers#iOS-iPadOS).
- Expect locale-dependent values and orders (hig:pickers).
**Platform specifics:**
- iOS/iPadOS: date picker styles compact (button opens a modal view, value in accent color), inline, wheels (also keyboard input), automatic; modes date, time, date and time, countdown timer (countdown not in inline/compact) (hig:pickers#iOS-iPadOS).
- macOS: date picker textual (little space, targeted input) or graphical (browse calendar, select range, clock look) (hig:pickers#macOS).
- watchOS: navigation via Digital Crown; wheels style for lists and date/time; optional outline, caption, scroll indicator; long lists via `navigationLink` style as a button, Crown scrubbing possible without tap (hig:pickers#watchOS).
- tvOS: only available with SwiftUI (hig:pickers#tvOS).
**Key values:** minute list 60 values by default (0–59); example quarter hours 0/15/30/45; countdown max. 23 h 59 min (hig:pickers#Best-practices, hig:pickers#iOS-iPadOS).
**Implementation:** SwiftUI `Picker`, `DatePicker` (styles incl. `.wheel`, `.navigationLink`, `.segmented`, `.menu`); UIKit `UIPickerView`, `UIDatePicker`; AppKit `NSDatePicker` (for lists on macOS: `NSPopUpButton` – see Pop-up buttons).
**Common mistakes:** Wheel picker for 3 options; unsorted values; picker on a separate screen instead of in context; minute interval that doesn't divide 60.

## Segmented controls
**Purpose:** Linear group of two or more segments, each acting as a button – single selection (macOS also multiple selection) or momentary actions. **Platforms:** ios, ipados, macos (tvos, visionos); not supported in watchOS.
**Use when:** a few closely related options affect an object, state, or view and grouping/selection state should be visible (hig:segmented-controls#Best-practices). **Don't use when:** switching between completely separate app areas (→ tab bar) (hig:segmented-controls#iOS-iPadOS), on macOS switching views in the main window area (→ tab view) (hig:segmented-controls#macOS), many options (→ picker/menu).
**Core rules:**
- Limit the number of segments: max. about 5–7 in a wide UI, max. about 5 on iPhone (hig:segmented-controls#Best-practices).
- Don't mix action and selection segments in one control (hig:segmented-controls#Best-practices).
- Keep segment widths (and icon/title widths) as equal as possible (hig:segmented-controls#Best-practices).
- Use either text or images, not a mix of both (hig:segmented-controls#Content).
- Use nouns/noun phrases in title-style capitalization; with text labels no introductory text is needed (hig:segmented-controls#Content).
- Fill segments with content of similar size (hig:segmented-controls#Content).
**Platform specifics:**
- iOS/iPadOS: suitable for switching between closely related subviews (Calendar example: event vs. reminder) (hig:segmented-controls#iOS-iPadOS).
- macOS: introductory text if needed; with symbols, labels below segments and a tooltip per segment; fine for view switching in a toolbar/inspector, in the main area use a tab view; support spring loading (hig:segmented-controls#macOS).
- tvOS: a segment is selected as soon as it gets focus → no other focusable elements nearby; for filters rather a split view (hig:segmented-controls#tvOS).
- visionOS: icon segments show a tooltip with the underlying text when looked at (hig:segmented-controls#visionOS).
**Key values:** about 5–7 segments (wide), about 5 (iPhone) (hig:segmented-controls#Best-practices).
**Implementation:** SwiftUI `Picker` with `.pickerStyle(.segmented)`; UIKit `UISegmentedControl` (`isMomentary` for actions); AppKit `NSSegmentedControl` (`SwitchTracking.momentary`, multiple selection).
**Common mistakes:** Segmented control as a tab bar replacement for app navigation; 7+ segments on iPhone; icons and text mixed; action + selection in one control.

## Sliders
**Purpose:** Horizontal track with a thumb for setting a value between a minimum and a maximum. **Platforms:** ios, ipados, macos, watchos (visionos); not supported in tvOS.
**Use when:** a value is set continuously or in steps within a fixed range, ideally with live feedback. **Don't use when:** audio volume on iOS (→ volume view) (hig:sliders#iOS-iPadOS); the exact value is crucial (then additionally a text field).
**Core rules:**
- Minimum leading, maximum trailing (horizontal); minimum at the bottom, maximum at the top (vertical) (hig:sliders#Best-practices).
- Customize the appearance (track color, thumb, min/max icons) only if it conveys meaning (hig:sliders#Best-practices).
- For large ranges, add a text field and stepper for exact or integer values (hig:sliders#Best-practices).
- Provide live feedback during the change (macOS) (hig:sliders#macOS).
- Use a linear slider for fixed ranges, a circular one for repeating values (e.g. rotation) (hig:sliders#macOS).
- Use tick marks for precision; usually label only min/max, for nonlinear values periodically (hig:sliders#macOS).
**Platform specifics:**
- iOS/iPadOS: no slider for volume – use a volume view (hig:sliders#iOS-iPadOS).
- macOS: tick marks, linear (lozenge thumb) and circular; label in sentence style + colon; tooltip with the current value (hig:sliders#macOS).
- visionOS: prefer horizontal sliders (hig:sliders#visionOS).
- watchOS: discrete steps or a continuous bar, side buttons change by a fixed amount; default glyphs plus/minus, custom ones if needed (hig:sliders#watchOS).
**Key values:** none binding; example values in the mirror (0–100 %, 0–360°, 1440°) are illustrations only (hig:sliders#macOS).
**Implementation:** SwiftUI `Slider`; UIKit `UISlider`; AppKit `NSSlider`.
**Common mistakes:** Reversed direction; volume control as `UISlider`; large value range without a way to enter exact values; vertical sliders in visionOS.

## Steppers
**Purpose:** Two-segment control for increasing/decreasing an incremental value; doesn't display a value itself. **Platforms:** ios, ipados, macos (visionos); not supported in watchOS, tvOS.
**Use when:** small changes with few taps/clicks (e.g. quantity). **Don't use when:** large value jumps are common without an accompanying input field.
**Core rules:**
- Make clear which value the stepper changes (value display next to it) (hig:steppers#Best-practices).
- Combine with a text field when widely varying values are expected (hig:steppers#Best-practices).
- On macOS, for large ranges support Shift-click for larger steps (hig:steppers#macOS).
**Platform specifics:** macOS: Shift-click e.g. 10× increment (example, not a requirement) (hig:steppers#macOS).
**Key values:** none binding (factor 10 only as an example).
**Implementation:** SwiftUI `Stepper`; UIKit `UIStepper`; AppKit `NSStepper`.
**Common mistakes:** Stepper without a visible value; stepper for values with a large span without an input field.

## Text fields
**Purpose:** Rectangular area for entering/editing small, specific pieces of text (name, email). **Platforms:** ios, ipados, macos, watchos (tvos, visionos).
**Use when:** short input. **Don't use when:** longer text (→ text view) (hig:text-fields#Best-practices); on watchOS/tvOS when a list of options or buttons is sufficient (hig:text-fields#watchOS).
**Core rules:**
- Show a placeholder as a hint, add a separate label if needed (the placeholder disappears when typing) (hig:text-fields#Best-practices).
- Use secure fields for passwords/sensitive data (hig:text-fields#Best-practices).
- Size the field to match the expected amount of text; multiple fields vertically, evenly spaced, consistent widths (hig:text-fields#Best-practices).
- Ensure a logical tab order (hig:text-fields#Best-practices).
- Validate depending on context: email on field change, username/password before field change (hig:text-fields#Best-practices).
- Use a number formatter for numbers, without assuming a fixed representation (locale) (hig:text-fields#Best-practices).
- Choose wrapping/truncation behavior deliberately; expansion tooltip for truncated text (hig:text-fields#Best-practices).
- Show the appropriate keyboard type (iOS, iPadOS, tvOS, visionOS) (hig:text-fields#Best-practices).
- Minimize text input on tvOS/watchOS (hig:text-fields#Best-practices).
**Platform specifics:**
- iOS/iPadOS: clear button at the trailing end; leading image for purpose, trailing for an additional function (e.g. bookmarks) (hig:text-fields#iOS-iPadOS).
- macOS: for text + choice list, combo box (hig:text-fields#macOS).
- watchOS: text field only when necessary; prefer a list of options (hig:text-fields#watchOS).
**Key values:** none in the mirror.
**Implementation:** SwiftUI `TextField`, `SecureField`; UIKit `UITextField`; AppKit `NSTextField` (secure: `NSSecureTextField` – not listed on the page).
**Common mistakes:** Placeholder as the only label; password in a plain-text field; default keyboard for numbers/email; validation only on submit; fixed number formats instead of locale.

## Toggles
**Purpose:** Choice between two opposing states (on/off) with a distinct appearance for each state; styles switch, checkbox, (macOS) radio buttons, button with toggle behavior. **Platforms:** ios, ipados, macos, watchos (tvos, visionos).
**Use when:** the state of content/a view is turned on or off. **Don't use when:** other actions, e.g. choosing from a list (→ pop-up button) (hig:toggles#Best-practices).
**Core rules:**
- Use toggles only for two opposing values (hig:toggles#Best-practices).
- Make clear what the toggle controls (context or, especially on macOS, a label) (hig:toggles#Best-practices).
- Don't indicate states by color alone (fill, shape, checkmark/dot) (hig:toggles#Best-practices).
- iOS: switch only in list rows, without an extra label; outside lists a button with toggle behavior (hig:toggles#iOS-iPadOS).
- iOS: change the switch color (default green) only if needed, e.g. accent color with sufficient contrast (hig:toggles#iOS-iPadOS).
- macOS: switches, checkboxes, radio buttons in the window content, not in the toolbar/status bar (hig:toggles#macOS).
- macOS: switch for emphasized/group-controlling settings; in a grouped form a mini switch per row; don't replace an existing checkbox with a switch (hig:toggles#Switches).
- macOS: checkbox for hierarchies (indentation) and single on/off; show the mixed state when sub-options are inconsistent (hig:toggles#Checkboxes).
- macOS: radio buttons for mutually exclusive options (typically 2–5); with more than about 5 a pop-up button; horizontal spacing based on the longest label (hig:toggles#Radio-buttons).
**Platform specifics:**
- iOS/iPadOS: switch only in lists; toggle buttons without an explanatory label, icon + background change (hig:toggles#iOS-iPadOS).
- macOS: three variants switch/checkbox/radio; checkbox usually with a trailing title, in an editable checklist also without (hig:toggles#Checkboxes); mixed state rarely sensible for radio buttons → checkbox (hig:toggles#Radio-buttons).
- tvOS, visionOS, watchOS: no additional guidance.
**Key values:** radio groups typically 2–5; more than about 5 → pop-up button (hig:toggles#Radio-buttons).
**Implementation:** SwiftUI `Toggle` with `ToggleStyle` (`.switch`, `.checkbox` macOS, `.button`), `controlSize(.mini)`, `GroupedFormStyle`; radio on macOS via `Picker` with `.radioGroup` (not named on the page); UIKit `UISwitch`, `UIButton.changesSelectionAsPrimaryAction`; AppKit `NSSwitch`, `NSButton` (`.toggle`, `allowsMixedState`).
**Common mistakes:** Free-standing switch in an iOS layout outside a list; state shown by color only; checkbox hierarchy as switches; radio list with 8 options; toggle in a macOS toolbar.

## Virtual keyboards
**Purpose:** System on-screen keyboards with task-specific keys for devices without a physical keyboard; no keyboard shortcuts. **Platforms:** ios, ipados, watchos (tvos, visionos); not supported in macOS.
**Use when:** text input on touch/remote devices – always choose the type to match the content. **Don't use when:** custom input view without recognizable added value; custom keyboard (extension) only for systemwide functionality, for in-app input a custom input view (hig:virtual-keyboards#Custom-keyboards).
**Core rules:**
- Choose the keyboard type to match the content and set a semantic content type (improves suggestions/correction) (hig:virtual-keyboards#Best-practices).
- Customize the Return key type if it clarifies the flow (e.g. Search) (hig:virtual-keyboards#Best-practices).
- Custom input view only if the benefit is clear in the app context; play the standard keyboard click (hig:virtual-keyboards#Custom-input-views).
- Custom keyboard: clear way to switch keyboards (Globe key behavior), no duplicates of Emoji/Globe/Dictation, tutorial in the app rather than in the keyboard (hig:virtual-keyboards#Custom-keyboards).
- iOS: use the keyboard layout guide so important UI remains visible (hig:virtual-keyboards#iOS-iPadOS).
- iOS: controls above the keyboard only if task-relevant; Liquid Glass for their container, the standard toolbar adopts it automatically; standard padding (hig:virtual-keyboards#iOS-iPadOS).
**Keyboard types** (`UIKeyboardType`): ASCII capable, ASCII capable number pad, Decimal pad, Default, Email address, Name phone pad, Number pad, Numbers and punctuation, Phone pad, Twitter, URL, Web search (hig:virtual-keyboards#Best-practices).
**Platform specifics:**
- iOS/iPadOS: keyboard layout guide, input accessory view (hig:virtual-keyboards#iOS-iPadOS).
- watchOS: keyboard only on sufficiently large displays, otherwise dictation/Scribble; keyboard type can't be changed, but content type can; input also via a paired iPhone (hig:virtual-keyboards#watchOS).
- tvOS: linear keyboard with the Siri Remote, grid keyboard with other devices; digit entry view with a digit keyboard (hig:virtual-keyboards#tvOS).
- visionOS: keyboard in its own movable window; the layout doesn't need to account for it (hig:virtual-keyboards#visionOS).
- Custom keyboards (extension) in iOS, iPadOS, tvOS; not usable in secure and phone number fields (hig:virtual-keyboards#Custom-keyboards).
**Key values:** none in the mirror.
**Implementation:** SwiftUI `keyboardType(_:)`, `textContentType(_:)`, `submitLabel(_:)`, `ToolbarItemPlacement` (`.keyboard`); UIKit `UIKeyboardType`, `UITextContentType`, `UIReturnKeyType`, `inputViewController`, `inputAccessoryView`, `UIKeyboardLayoutGuide`, `UIDevice.playInputClick()`.
**Common mistakes:** Default keyboard for email/numbers/URL; missing `textContentType` (no AutoFill); keyboard covers the input field/buttons; custom keyboard without a way to switch; accessory bar with irrelevant actions.
