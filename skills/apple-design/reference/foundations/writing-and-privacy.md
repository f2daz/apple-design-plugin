# Writing, Privacy, and Branding

Sources (HIG mirror, as of 2026-10-21): `writing` (updated 2025-12-16: language patterns, possessive pronouns), `privacy` (2023-06-21), `branding` (2026-09-09: brand color), `inclusion` (welcoming language, gender identity), `onboarding` (2024-06-10), `alerts` (2024-02-02), plus `buttons#Content`, `notifications`, `launching`, `progress-indicators`.

## Overview

Text is part of the UX: onboarding, alerts, error messages, accessibility descriptions (hig:writing). At Apple, privacy is a design topic, not just a legal one: transparency about the data needed, minimal requests, protection of shared data; the App Store product page shows the privacy details from App Store Connect (hig:privacy). Branding should make the app recognizable, but **defer to the content** and keep familiar platform patterns (hig:branding).

## Core rules

### Voice and tone
- Define the app's voice (audience, vocabulary, desired feeling) and keep a word list for consistency (hig:writing#Getting-started).
- Adapt the tone to the situation: matter-of-fact and direct for serious matters (payment error), light for successes (goal reached) (hig:writing#Getting-started).
- Write clearly and concisely; examine every word, read it aloud when in doubt (hig:writing#Getting-started).
- Write for everyone: plain language, no jargon, no gendered terms; keep localization and VoiceOver in mind (hig:writing#Getting-started).
- Check the tone from different perspectives; an academic tone feels exclusionary (hig:inclusion#Welcoming-language).
- Address people directly ("you", "your") instead of "the user"/"the player" (hig:inclusion#Welcoming-language).
- Technical terms only with a definition; replace idioms with plain language; use humor only with care (translatability, fatigue, misunderstanding) (hig:inclusion#Welcoming-language).
- Avoid unnecessary gender references ("Subscribers can post recipes" instead of "…his or her recipes"); ask for gender only when necessary, and then with options such as nonbinary, self-identify, decline to state (hig:inclusion#Gender-identity).
- Avoid context-specific assumptions (e.g. security questions about college or a first car) – choose universal experiences (hig:inclusion#Avoiding-stereotypes).
- Check colors for cultural meaning per locale (hig:inclusion#Languages).

### Structure and language patterns
- Most important information first; spread multiple ideas across multiple screens if needed (hig:writing#Best-practices).
- Action-oriented: active voice, buttons and links with a verb ("Send" instead of "Let's go!"); no "Click here" links, but descriptive link text (important for screen readers) (hig:writing#Best-practices).
- Build recurring language patterns (hig:writing#Best-practices).
- Choose one capitalization style per UI element type and stick to it (hig:writing#Best-practices).
- Multistep flows: start with "Get Started", progress consistently with "Continue" or "Next" or a preview of the next step, finish with "Done" (hig:writing#Best-practices).
- Use possessive pronouns sparingly ("Favorites" instead of "Your Favorites"), don't switch perspective; **avoid "we"** ("Unable to load content" instead of "We're having trouble …") (hig:writing#Best-practices).
- Name gestures appropriately for the device (touch: "tap", not "click") (hig:writing#Best-practices).
- Small displays (iPhone, Watch) and large ones (TV, multiple viewers) demand brevity (hig:writing#Best-practices).
- Empty states: name next steps, offer a button/link, no critical information that disappears later (hig:writing#Best-practices).
- Settings: name them practically; the description explains the on state; link to Settings via a direct link/button instead of describing the path (hig:writing#Best-practices).
- Text fields: clear labels, hint/placeholder with a format example ("name@example.com") (hig:writing#Best-practices).
- Choose the delivery channel by urgency: inline, notification, alert, action sheet (hig:writing#Best-practices).

### Error messages
- Avoid errors where possible; when necessary, show them **close to the problem** (hig:writing#Best-practices).
- No blame; say what to do ("Choose a password with at least 8 characters" instead of "Password too short") (hig:writing#Best-practices).
- No interjections like "Oops!"/"Uh-oh" (hig:writing#Best-practices).
- Phrase positively ("Use only letters" instead of "No numbers or symbols"); no robotic messages like "Invalid name" (hig:writing#Best-practices).
- Errors that affect many people and that wording can't solve → rethink the interaction (hig:writing#Best-practices).
- Errors via alert, not via notification (hig:notifications).

### Alerts – text and buttons
- Tone direct, neutral, approachable; don't obscure anything, don't accuse (hig:alerts#Content).
- The title describes the situation concretely (what, context, why); no "Error" or "Error 329347"; at most two lines (hig:alerts#Content).
- Title as a complete sentence → sentence case + punctuation; as a fragment → title case without ending punctuation (hig:alerts#Content).
- Informative text only when it adds value, short, complete sentences (hig:alerts#Content).
- Don't explain the buttons; if you must, use "choose" and the exact button title without quotation marks (hig:alerts#Content).
- Button titles: one or two words, a verb, describing the result ("View All", "Reply", "Ignore"); title case, no ending punctuation (hig:alerts#Buttons).
- "OK" only in purely informational alerts; avoid "Yes/No"; a specific verb instead of OK (Apple examples: Erase, Convert, Clear, Delete) (hig:alerts#Buttons).
- The cancel button is always titled **"Cancel"**; never the default button; a single button that is the default → "Done", not Cancel (hig:alerts#Buttons).
- Destructive style only for destructive actions that people didn't deliberately choose (emptying the Trash after a deliberate choice → no destructive style) (hig:alerts#Buttons).
- Never assign the primary role to a destructive action (hig:buttons#Content).
- No alert for pure information, for common undoable actions, or at app launch (hig:alerts#Best-practices).

### Permission requests and purpose strings
- Request only data that a feature really needs, as specifically as possible (hig:privacy#Best-practices).
- Ask only when the feature is used; at launch only if the app can't function without the permission (navigation + location) (hig:privacy#Requesting-permission).
- Purpose string: short, complete, active sentence, specific, sentence case, period at the end (hig:privacy#Requesting-permission).
- Pre-alert screen only if context isn't enough: **exactly one button** that opens the system alert, titled "Continue" or "Next" – **not** "Allow"; no close/cancel option, no additional actions except for legally required consent (hig:privacy#Requesting-permission, section "Pre-alert screens, windows, or views").
- Tracking (ATT): system alert **before** any collection of tracking data; no misleading screens in front of it. Prohibited (leads to rejection): incentives, screens that look like a request, an image of the alert, annotations behind the alert. Allowed: a consent screen before/after the ATT alert to comply with local privacy laws (App Review Guideline 5.1.1 (iv)) (hig:privacy#Tracking-requests).
- Respect Hide My Email, Mail Privacy Protection; know your tracking obligations (hig:privacy#Best-practices).
- Where appropriate, integrate necessary permissions into onboarding to explain the benefit; otherwise at the first access to the feature (hig:onboarding#Additional-requests).
- Use the **location button** (iOS, iPadOS, watchOS) for one-time, situational location sharing (hig:privacy#Location-button).

### Implementing data protection
- Process data on the device where possible (hig:privacy#Best-practices).
- Use system protections (e.g. CloudKit encryption from iOS 15) (hig:privacy#Best-practices).
- Passkeys instead of passwords; otherwise 2FA; Face ID / Touch ID / Optic ID for signed-in apps (hig:privacy#Protecting-data).
- Sensitive data in the keychain, never in plain-text files (hig:privacy#Protecting-data).
- No custom authentication schemes; passkeys, Sign in with Apple, Password AutoFill (hig:privacy#Protecting-data).
- No sensitive/personal data in notifications; provide generic text for hidden previews (hig:notifications).

### Branding
- Brand voice in all text (e.g. simple words, occasional exclamation points and emoji if it fits the brand) (hig:branding#Best-practices).
- Accent color sparingly: primary actions, status indicators (badges, selected tab); rather move the brand color into the content layer beneath Liquid Glass controls (hig:branding#Best-practices).
- Custom font only if legible at all sizes and with Bold Text and Dynamic Type; pattern: custom font for headlines, system font for body/captions (hig:branding#Best-practices).
- Express the brand through familiar components; keep size, placement, behavior typical for the platform (hig:branding#Best-practices).
- Branding defers to content; no areas just for brand assets (hig:branding#Best-practices).
- Don't display the logo throughout (hig:branding#Best-practices).
- The launch screen is not a place for branding; brand, if anything, in the welcome/onboarding screen (hig:branding#Best-practices, hig:launching#Launch-screens).
- Apple trademarks must not appear in the app name or in images; follow the Apple Trademark Guidelines (hig:branding#Best-practices).
- No SF Symbols in logos/app icons, no replicas of Apple hardware (hig:sf-symbols, hig:app-icons#Design).

### Onboarding (brief)
- Only after launch, not part of it; fast, fun, optional (hig:onboarding).
- Teach through interactivity; contextual tips (TipKit) instead of a long flow (hig:onboarding#Best-practices).
- Tutorial skippable, not shown again afterwards, but findable (Help/Settings) (hig:onboarding#Best-practices).
- Explain only the app, not the system (hig:onboarding#Best-practices).
- Splash screen only briefly; no large downloads before launch; no license text in onboarding (the App Store shows it) (hig:onboarding#Additional-content).
- Defer setup, sensible defaults; rating and purchase prompts only after real use (hig:onboarding#Additional-requests).

## Key values and examples

### Purpose strings (hig:privacy#Requesting-permission, paraphrased)

| Rating | Example | Why |
|---|---|---|
| good | "The app records during the night to detect snoring sounds." | Active, specific: how and why |
| bad | "Microphone access is needed for a better experience." | Passive, vague reason |
| bad | "Turn on microphone access." | Imperative, no reason |

The system alert shows the purpose string after the app name and before the buttons; people see and change it later under Settings > Privacy.

### What requires permission (hig:privacy#Requesting-permission)

| Category | Examples |
|---|---|
| Personal data | Location, health, financial, contacts, other identifying data |
| User content | Emails, messages, calendar, contacts, game saves, Apple Music activity, HomeKit data, audio, video, photos |
| Protected resources | Bluetooth peripherals, home automation, Wi-Fi, local network |
| Device capabilities | Camera, microphone |
| visionOS Full Space | ARKit data (hand tracking, plane estimation, image anchoring, world tracking) |
| Tracking | Advertising identifier |

### Alert buttons (hig:alerts#Buttons)

| Situation | Title | Position |
|---|---|---|
| Pure information | OK | – |
| Confirming an action | Specific verb (Delete, Convert, Clear) | Default = trailing (row) or top (stack) |
| Cancel | Cancel (always exactly this) | leading (row) or bottom (stack); never default |
| Only one button, which is the default | Done | – |
| People should read rather than press Return | no button as default | – |

Alternative ways to cancel: Home Screen (iOS/iPadOS), Esc or Cmd-. (iOS, iPadOS, macOS, visionOS with keyboard), Menu button (tvOS). Alerts everywhere have a title, optional text, and up to three buttons; a text field is possible in iOS, iPadOS, macOS, visionOS.

### Location button – customizable vs. fixed (hig:privacy#Location-button)

| Customizable | Not customizable |
|---|---|
| System title (e.g. "Current Location", "Share My Current Location") | all other styling |
| Glyph filled or outline | – |
| Background, title, and glyph color | – |
| Corner radius | – |

Text must fit without truncation at all accessibility sizes and in all translations; after repeated problems (contrast, transparency) the system no longer provides the location.

## Platform differences

| Topic | iOS / iPadOS | macOS | watchOS |
|---|---|---|---|
| Gesture verbs | tap, swipe | click | tap, turn the Digital Crown |
| Alerts | Action sheet instead of alert for options related to a deliberate action; avoid scrolling alerts (large text) | App icon automatically in the alert; suppression checkbox, accessory view, Help button; caution symbol `exclamationmark.triangle` sparingly (not for saving/Trash) | concise, little space |
| Privacy | Location button | Sign with Developer ID (outside the Store); sandbox (required in the Mac App Store); Fast User Switching – no assumptions about the signed-in person | Location button available |
| Text | Short (small display) | more space, but the same clarity | very short, notification titles especially concise |

visionOS: ARKit data only in a Full Space after permission; gaze direction stays private (hover effects handled by the system); the rear camera delivers a blank image – replace camera features (e.g. import) (hig:privacy#visionOS).

## Implementation

### Purpose strings (Info.plist, localized via `InfoPlist.strings`/String Catalog)
```text
NSCameraUsageDescription           – Camera
NSMicrophoneUsageDescription       – Microphone
NSLocationWhenInUseUsageDescription – Location when in use
NSPhotoLibraryUsageDescription     – Photos
NSContactsUsageDescription         – Contacts
NSCalendarsFullAccessUsageDescription – Calendar (newer systems; older: NSCalendarsUsageDescription)
NSUserTrackingUsageDescription     – App Tracking Transparency
NSBluetoothAlwaysUsageDescription  – Bluetooth
NSLocalNetworkUsageDescription     – Local network
NSFaceIDUsageDescription           – Face ID
```
Key names come from the Apple SDK, not from the HIG mirror; check the documentation for each target OS.

### SwiftUI
```swift
.alert("Delete Draft?", isPresented: $showAlert) {
    Button("Delete", role: .destructive) { delete() }
    Button("Cancel", role: .cancel) { }
} message: {
    Text("The draft can't be recovered.")
}

LocationButton(.shareCurrentLocation) { manager.requestLocation() }   // CoreLocationUI
    .symbolVariant(.fill)
    .foregroundStyle(.white)
    .tint(.blue)

TipView(FavoriteTip())   // TipKit for contextual onboarding
```

### UIKit / AppKit
```swift
let alert = UIAlertController(title: "Delete Draft?",
                              message: "The draft can't be recovered.",
                              preferredStyle: .alert)
alert.addAction(UIAlertAction(title: "Cancel", style: .cancel))
alert.addAction(UIAlertAction(title: "Delete", style: .destructive) { _ in delete() })

let ns = NSAlert()
ns.messageText = "Delete Draft?"
ns.informativeText = "The draft can't be recovered."
ns.addButton(withTitle: "Delete")
ns.addButton(withTitle: "Cancel")
ns.showsSuppressionButton = true   // only for recurring alerts
```

## Review checklist

**Text**
- [ ] Word list exists; the same things have the same name everywhere.
- [ ] Tone fits the situation; no humor in error/payment contexts.
- [ ] Buttons/links with a verb; no "Click here" links; no cute labels.
- [ ] Consistent capitalization per element type (for German localization: apply German spelling rules instead of English title case).
- [ ] Form of address consistent (in German: du or Sie) – no mixing; no "we" in error messages.
- [ ] Possessive pronouns only where necessary.
- [ ] Gesture verbs correct for each device.
- [ ] Empty states with next step + action.
- [ ] Error messages close to the field, solution-oriented, blame-free, no "Oops".
- [ ] Placeholders with a format example; settings with a description of the on state.
- [ ] Inclusive: no gender assumptions, no unexplained jargon, no idioms.

**Alerts**
- [ ] Only for critical, actionable cases; none at launch.
- [ ] Title specific, ≤ 2 lines; no "Error" without content.
- [ ] Buttons: 1–2 words, verb; "OK" only for informational alerts; "Cancel" exactly like this and not default.
- [ ] Destructive style correct (only for destruction not deliberately chosen); primary role never destructive.

**Privacy**
- [ ] Every permission justified and deferred to the moment the feature is used (exception: the app doesn't work otherwise).
- [ ] Purpose strings: active, specific sentence with a period; localized.
- [ ] Pre-alert screen: exactly one "Continue" button, no "Allow", no close.
- [ ] ATT alert before any tracking data collection; no incentives or alert imitations.
- [ ] Location button instead of a permanent request where situational.
- [ ] Keychain for secrets; passkeys/Sign in with Apple; no homegrown auth.
- [ ] No sensitive content in notifications.
- [ ] Privacy details in App Store Connect up to date.
- [ ] macOS: sandbox, Developer ID (outside the Store).

**Branding / onboarding**
- [ ] Accent color only for primary actions and status.
- [ ] Custom font supports Dynamic Type and Bold Text; body in the system font.
- [ ] No logo on every screen, no brand-only areas.
- [ ] Launch screen without logo/text.
- [ ] No Apple trademarks in the app name or images.
- [ ] Onboarding short, skippable, interactive; tutorial findable later; no license text.
- [ ] Rating/purchase prompts only after use.

## Anti-patterns

- "Oops! Something went wrong. We're looking into it." – interjection, "we", no option to act.
- Alert title "Error" with an "OK" button for a delete confirmation.
- Yes/No buttons.
- Purpose string "Needed for a better experience."
- Pre-permission screen with "Allow" and "Later".
- Requesting all permissions at once at first launch.
- Voucher/reward for consenting to tracking.
- Logo splash as the launch screen; brand color on all controls.
- Custom login with the password in a plain-text cache.
- Notification with an account balance or diagnosis in the preview text.
- "Click on …" in an iPhone app.
- Settings hint "Go to Settings > Privacy > …" instead of a direct link.

## Ambiguities / contradictions in the mirror

- **"We":** `writing#Best-practices` advises avoiding "we" **entirely**; `inclusion#Welcoming-language` recommends **reserving** "we/our" for your own software or company. The stricter rule (writing, newer: 2025-12-16) applies to UI text, especially error messages.
- **Capitalization:** `writing` leaves the choice (title vs. sentence case) to the app's style; `alerts` and `buttons` prescribe title case for buttons and fragment titles. For German localization, both are English conventions – in German the normal spelling rules apply (author's own assessment, not in the mirror).
- **Exclamation points/emoji:** `branding` names them as a possible stylistic device of the brand voice; `writing` and `alerts` require a neutral, direct tone. Resolution: brand voice in success/empty states, never in errors and alerts.
- **Pre-alert screen without close:** `privacy` prohibits close/cancel in the pre-alert screen, but allows additional actions if legally required for consent (e.g. GDPR). Legal review is outside the scope of the HIG.
- **Location button title** "Share My Current Location" uses a possessive pronoun – a system default, not a violation of `writing`.
