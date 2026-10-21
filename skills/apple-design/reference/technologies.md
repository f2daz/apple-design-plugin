# Technologies (HIG section "Technologies")

Purpose: Condensed design rules for Apple technologies that an app integrates (payment, sign-in, Wallet, Siri, Health, maps, etc.). Focus on iOS, iPadOS, macOS, watchOS. For wording, brand, and button rules, always check the HIG page itself before implementing.

- Source: local HIG mirror `~/.apple-design/hig/pages/<slug>.md`, sync 2026-10-21.
- Sources cited as: `(hig:<slug>)` or `(hig:<slug>#Anchor)`; anchors correspond to the HIG page headings (spaces as `-`).
- Numbers and measurements appear only where the page states them verbatim. If a number is missing, the page gives none.
- "Platforms" = the page's header line; "not supported" = the *Platform considerations* section.
- The rules are paraphrased, not quoted. Images and assets are in the Apple Design Resources and are not embedded here.

## Overview

| Technology | Platforms per page | Slug |
|---|---|---|
| AirPlay | iOS, iPadOS, macOS, tvOS, visionOS (watchOS not supported) | `airplay` |
| Always On | iOS, watchOS | `always-on` |
| App Clips | iOS, iPadOS | `app-clips` |
| Apple In-App Purchase | iOS, iPadOS, macOS, tvOS, visionOS, watchOS | `apple-in-app-purchase` |
| Apple Pay | iOS, iPadOS, macOS, visionOS, watchOS, web (not tvOS) | `apple-pay` |
| Augmented reality | iOS, iPadOS, visionOS | `augmented-reality` |
| CareKit | iOS, iPadOS | `carekit` |
| CarPlay | iOS | `carplay` |
| Game Center | iOS, iPadOS, macOS, tvOS, visionOS, watchOS | `game-center` |
| Generative AI | all six | `generative-ai` |
| HealthKit | iOS, iPadOS, watchOS | `healthkit` |
| HomeKit | all six | `homekit` |
| iCloud | all six | `icloud` |
| ID Verifier | iOS | `id-verifier` |
| iMessage apps and stickers | iOS, iPadOS | `imessage-apps-and-stickers` |
| Live Photos | iOS, iPadOS, macOS, tvOS, visionOS (viewing only) | `live-photos` |
| Mac Catalyst | iPadOS, macOS | `mac-catalyst` |
| Machine learning | all six | `machine-learning` |
| Maps | all six (watchOS static) | `maps` |
| NFC | iOS, iPadOS | `nfc` |
| Photo editing | iOS, iPadOS, macOS | `photo-editing` |
| ResearchKit | iOS, iPadOS | `researchkit` |
| SharePlay | iOS, iPadOS, macOS, tvOS, visionOS (watchOS not supported) | `shareplay` |
| ShazamKit | all six | `shazamkit` |
| Sign in with Apple | all six, also web and non-Apple platforms | `sign-in-with-apple` |
| Siri | all six | `siri` |
| Tap to Pay on iPhone | iOS | `tap-to-pay-on-iphone` |
| VoiceOver | all six | `voiceover` |
| Wallet | iOS, iPadOS, macOS, visionOS, watchOS (not tvOS) | `wallet` |
| Cross-reference: Widgets | iOS, iPadOS, macOS, watchOS, visionOS | `widgets` |
| Cross-reference: Live Activities | iOS, iPadOS, macOS, watchOS | `live-activities` |
| Cross-reference: App Shortcuts | iOS, iPadOS, visionOS, watchOS (not tvOS; macOS App Intents only) | `app-shortcuts` |

"All six" = iOS, iPadOS, macOS, tvOS, visionOS, watchOS.

---

## AirPlay
Wireless streaming of media to Apple TV, HomePod, and AirPlay-enabled devices.
- Use the system media player (`AVPlayerViewController`). Build a custom player only if the system player isn't sufficient (hig:airplay#Best-practices).
- Offer the full range of resolutions in the HLS playlist, otherwise content looks inferior on large displays (hig:airplay).
- Stream only expected content, no background loops. Support streaming and mirroring, support remote control events (hig:airplay).
- Continue playback in the background and when the device is locked. Don't mirror automatically, and interrupt other playback only for immersive content (hig:airplay).
- With a custom player: buttons that match the system visually and behaviorally, Apple symbols only, AirPlay icon at bottom right (from iOS 16/iPadOS 16) (hig:airplay).
- **Resources/brand:** AirPlay icon (black, white, custom color matching other technology icons) from the Apple Design Resources. Don't use the icon or name interactively, and don't use the icon in running text. Your own app should appear more prominent than AirPlay (hig:airplay#Using-AirPlay-icons).
- **Spelling:** *AirPlay* one word, capital A and P, only as a noun ("Use AirPlay to …", not "AirPlay to your speaker"). Phrases like "works with", "compatible with" are allowed, as is "Apple AirPlay" (hig:airplay#Referring-to-AirPlay).

## Always On
When the device is at rest, the system shows dimmed, data-minimal content (iPhone: Lock Screen widgets and Live Activities; Watch: app in the foreground or with a background session).
- Hide sensitive data (account balances, health data), also in notifications (hig:always-on#Best-practices).
- Keep useful, non-sensitive information glanceable, e.g. pace and heart rate during a workout (hig:always-on).
- Keep important content legible and dim secondary content. Preferably remove or dim images and large areas of color (hig:always-on).
- Keep the layout stable: switch interactive elements to "unavailable" instead of removing them, update rarely and subtly (hig:always-on).
- Transition motion gently into a resting state and don't stop it abruptly (hig:always-on).
- Platforms: iOS and watchOS. On iPhone, motion is especially distracting because the device often lies face up.

## App Clips
Lightweight, instantly available partial version of an app for a task on the go or as a demo. Launched via App Clip Code, NFC, QR, Maps, Safari, Messages, or Siri Suggestions.
- Make the task or demo fully completable within the App Clip and don't force installation of the full app (hig:app-clips#Designing-your-App-Clip).
- Limit to core functionality: linear, without tab bar, complex navigation, or settings. No web views, no ads, no pure marketing (hig:app-clips).
- Immediately usable: no splash screens, all assets included, keep it small (hig:app-clips).
- Don't require an account before use. Offer Apple Pay and Sign in with Apple. Stored data may be deleted between launches (hig:app-clips#Preserving-privacy).
- Recommend the full app only at natural pauses via `SKOverlay`, not repeatedly and not via push (hig:app-clips#Showcasing-your-app).
- Notifications are possible up to 8 hours after launch. Longer periods only with explicit permission and only task-related (hig:app-clips#Limiting-notifications).
- App Clip card: image 1800x1200 px, PNG/JPEG without transparency, no text and no screenshots. Title no more than 30 characters, subtitle no more than 56. Button verb *View*, *Play*, or *Open* (hig:app-clips#Creating-content-for-an-App-Clip-card).
- **Resources – App Clip Code:** use only generated codes (App Store Connect or App Clip Code Generator), don't alter anything, don't rotate, animate, or dim. Variants: scan-only (camera glyph) and NFC-integrated (iPhone glyph). Badge with the App Clip logo if space permits. Never use the logo on its own (hig:app-clips#App-Clip-Codes).
- **App Clip Code dimensions:** print at least 3/4 inch (1.9 cm) diameter, digital at least 256×256 px (PNG/SVG). The NFC tag needs at least 35 mm, the code then at least 1.37 inch (3.48 cm). Distance to code size no more than 20:1, preferably 10:1. Clear space equals the distance between glyph and ring. On a cylinder no more than 1/6 of the circumference (hig:app-clips#Displaying-App-Clip-Codes).
- **Printing:** matte, screening at least 600 ppi, print at least 300 dpi, sRGB→CMYK relative colorimetric, Delta E 2.5, NFC tags Type 5. Check with Apple's calibration test sheets (hig:app-clips#Printing-guidelines).
- **Brand:** *App Clips*/*App Clip Code* in title case, don't translate Apple trademarks, stop showing codes of inactive clips (hig:app-clips#Legal-requirements).

## Apple In-App Purchase
Selling digital goods and subscriptions in the app (consumable, non-consumable, auto-renewable, non-renewing). Physical goods and services, by contrast, go through Apple Pay.
- Let people experience the app first, then sell. Integrate the store in the app's style and use short product names that don't wrap (hig:apple-in-app-purchase#Best-practices).
- Show the total price for every purchase. Show the store only if payments are possible (`canMakePayments`). Neither modify nor replicate the system confirmation sheet (hig:apple-in-app-purchase).
- Mention Family Sharing prominently (e.g. "Family" in the name) and write copy for purchasers and family members. Sharing covers up to five other family members (hig:apple-in-app-purchase#Supporting-Family-Sharing).
- Refunds: offer your own help page before the system refund flow, name the action plainly ("Refund"/"Request a Refund"), don't comment on Apple's refund policy, and make the refund button reachable without scrolling (hig:apple-in-app-purchase#Providing-help).
- The sign-up screen must contain: subscription name, duration, scope of benefits, localized price, and a way to sign in or restore. Clearly explain trial periods and automatic billing (hig:apple-in-app-purchase#Making-signup-effortless).
- Don't show subscription promotions to existing subscribers. Canceling must always be easy to find. Use the system UI for management (`showManageSubscriptions`) (hig:apple-in-app-purchase#Helping-people-manage-their-subscriptions).
- Offer codes (iOS/iPadOS): custom codes alphanumeric ASCII only. Explain that they can be redeemed via URL or in the app. A "Redeem Code" button is enough; the system handles the rest (hig:apple-in-app-purchase#Supporting-offer-codes).
- watchOS: the same required information as on other platforms, ideally in a modal sheet with a Close button. Make options compactly comparable, as one button per option or as a list plus button (hig:apple-in-app-purchase#watchOS). tvOS: enable sign-up via a second device.
- **Spelling:** since 2026-09-17 the technology is called "Apple In-App Purchase".

## Apple Pay
Secure payment for physical goods, services, donations, and subscriptions in apps and in any browser.
- Offer Apple Pay wherever it's supported. If the API detects an active card, show Apple Pay as the primary (not necessarily the only) option and don't move it into a separate step (hig:apple-pay#Offering-Apple-Pay).
- Use Apple Pay buttons only for paying or setting up. Never hide the button or show it disabled; explain missing information only after the tap (hig:apple-pay).
- Checkout: use express checkout and buttons on product pages. Ask for variants, optional information, multiple shipping destinations, and pickup location before the payment sheet. Don't require an account before purchase; offer registration on the confirmation page (hig:apple-pay#Streamlining-checkout).
- Payment sheet: only necessary information. Use line items for surcharges, discounts, donations, and recurring payments, not for a product list. The total line reads "Pay [merchant name]", for marketplaces "Pay [end merchant] (via [platform])". No custom spinner (hig:apple-pay#Customizing-the-payment-sheet).
- Write error messages precisely and field-specific, as a noun phrase without a final period, no more than 128 characters. Validate input tolerantly, e.g. accept ZIP+4 (hig:apple-pay#Data-validation-errors).
- Subscriptions: billing interval, trial period ($0), and start date as line items. Show the sheet again only for additional costs (hig:apple-pay#Supporting-subscriptions). Donations: line item "Donation" and predefined amounts plus "Other Amount" (hig:apple-pay#Supporting-donations).
- Website icon for Apple Pay: 60x60 pt (120x120 px @2x, 180x180 px @3x) (hig:apple-pay#Displaying-a-website-icon).
- **Resources – buttons:** create only via API (`PKPaymentButtonType`/`PKPaymentButtonStyle`, `WKInterfacePaymentButton`, web API). Types: Buy, Pay, Check Out, Continue, Book, Donate, Subscribe, Reload, Add Money, Top Up, Order, Rent, Support, Contribute, Tip, plain "Apple Pay", and "Set Up Apple Pay". Styles: automatic, Black (light backgrounds), White with outline (light backgrounds with little contrast), White (dark backgrounds). The corner radius is adjustable (hig:apple-pay#Using-Apple-Pay-buttons).
- **Size/position:** not smaller than other payment buttons and visible without scrolling. Side by side: to the right of the Add-to-Cart button; stacked: above it. Minimum: Apple Pay 100pt × 30pt, Book with Apple Pay 140pt × 30pt, margin 1/10 of the button height in each case. If the translated title doesn't fit, the system replaces it with the plain button (doesn't apply to Set Up) (hig:apple-pay#Button-size-and-position).
- **Resources – Apple Pay mark:** only indicates acceptance and is never a button. Use only Apple artwork, adjusted solely in height (at least as tall as other payment marks). Clear space 1/10 of the height, no effects, don't rotate or animate. Download via the Apple Pay Marketing Guidelines (hig:apple-pay#Apple-Pay-mark). A custom start button may carry neither "Apple Pay" nor the logo; the mark then belongs on the same page.
- **Spelling:** *Apple Pay* two words, capital A and P, never plural or possessive, never the Apple logo instead of "Apple", don't translate. In the US, ® on first mention in running text, but not in the payment method selection. Plain text in the payment method selection only if all options are textual. On the confirmation page e.g. "1234 (Apple Pay)" (hig:apple-pay#Referring-to-Apple-Pay).
- Websites with Apple Pay need a privacy policy and must comply with the acceptable use rules (hig:apple-pay).

## Augmented reality
ARKit experiences that overlay virtual objects on the camera view. The page covers iOS/iPadOS; for visionOS it refers to ARKit.
- Offer AR features only on capable devices and hide them on other devices instead of showing errors (hig:augmented-reality).
- Use the entire screen for the scene. Controls as indirect controls in screen space, ideally translucent. Scene at 60 updates per second so nothing jumps (hig:augmented-reality#Best-practices).
- Consider comfort and safety: short sessions, introduce motion gradually, don't demand abrupt large movements (hig:augmented-reality).
- Use the system coaching view (`ARCoachingOverlayView`) for initialization and relocalization, hiding other UI meanwhile (hig:augmented-reality#Providing-coaching).
- Place objects immediately and refine later. Use plane classification and don't align objects exactly with surface edges (hig:augmented-reality#Helping-people-place-objects).
- Direct manipulation with standard gestures. Scale only when it makes sense, and never as a substitute for distance (hig:augmented-reality#Designing-object-interactions).
- Use understandable wording ("surface" instead of "plane", no terms like ARKit or tracking). Allow reset and canceling relocalization. No more than 100 active reference images (hig:augmented-reality#Communicating-with-people).
- **Resources:** AR glyph and AR badges (with text or glyph only, collapsed/expanded) from the Apple Design Resources. Use only for ARKit experiences. Change the glyph only in size and color, the badges not at all. Clear space 10 % of the height in each case. Badges only if not all objects are AR-capable, and always in the same corner (hig:augmented-reality#Icons-and-badges).

## CareKit
Framework for care plan apps (chronic illness, rehabilitation, wellness), consisting of CareKit UI and CareKit Store.
- A privacy policy (URL) is mandatory. Request health data only in context, use the standard permission screen with explanatory text, and don't build custom authorization screens (hig:carekit#Data-and-privacy).
- Use view categories for their intended purpose: tasks, charts, contact views (hig:carekit#CareKit-views).
- Task styles: simple (one step), instructions, log (events with timestamp), checklist, grid (compact, allows custom UI). Required fields are title and schedule (hig:carekit#Tasks).
- Charts (bar, scatter, line): concise labels, clearly distinguishable colors with contrast, legend if needed, specify time units, condense large data sets (hig:carekit#Charts).
- Never use color as the only means of conveying information. Refer to medications by their marketing names (hig:carekit).
- Use notifications sparingly and bundle them, offer a detail view with actions (hig:carekit#Notifications).
- Custom symbols are useful (SF Symbols), no company logo as a symbol, subtle branding (hig:carekit#Symbols-and-branding).
- Platforms: iOS, iPadOS (not macOS, tvOS, visionOS, watchOS).

## CarPlay
Apps on the vehicle display, built from system-defined templates (audio, communication, navigation, etc.).
- While CarPlay is active, don't require interaction on the iPhone and never lock people out because iPhone input is needed. Must work while the iPhone is locked (hig:carplay#iPhone-interactions).
- Audio: don't start playback automatically (exceptions: single source or resuming). Open the audio session only shortly before playback. Show Now Playing immediately. Resume only after temporary interruptions. Never change the overall volume (hig:carplay#Audio).
- Layout: clear and scannable from the driver's seat. Important content large and in the upper half of the screen. Common displays: 800x480 (5:3), 960x540 and 1280x720 (16:9), 1920x720 (8:3) (hig:carplay#Layout).
- Color: limited palette. Distinguish interactive and non-interactive elements by color. Test in a real car under different lighting conditions. Support Light and Dark (hig:carplay#Color).
- Icons: reuse the iPhone app icon, don't use a black background. Sizes 120x120 (@2x) and 180x180 (@3x) px. All artwork files in @2x and @3x (hig:carplay#Icons-and-images).
- Report errors in CarPlay and never refer people to the iPhone (hig:carplay#Error-handling).
- Platforms: iOS only. Per the page, audio and video apps also run on Apple HomeView without adaptation.

## Game Center
Apple's social gaming network (GameKit): achievements, leaderboards, challenges, multiplayer.
- At game launch, check the sign-in status and initialize immediately if needed (hig:game-center#Accessing-Game-Center).
- Show the access point only in menus (not during gameplay, tutorials, or cinematics), no controls near it, account for both sizes. Pause the game while the Game Overlay or dashboard is open (hig:game-center#Integrating-the-access-point).
- Custom UI: official artwork unchanged. Correct terms: "Game Center" (not GameKit/GameCenter), "Game Center Profile", "Achievements", "Leaderboards", "Challenges", "Add Friends" (hig:game-center#Using-custom-UI).
- Achievements: four states (locked, in-progress, hidden, completed). Title and description no more than two lines each, title in title case, description in sentence case. Image 512x512 pt (1024x1024 px @2x), circular mask with 512 pt diameter, tvOS 320x320 pt with 200-pt mask (hig:game-center#Achievements).
- Leaderboards: classic or recurring, sets for grouping. Image iOS/iPadOS/macOS 512x512 pt with a 512x312 pt crop. tvOS 659x371 pt with focus layers (hig:game-center#Leaderboards).
- Challenges: 1–5 minutes, playable solo, score the last attempt instead of the best. Go directly to the level via deep link. Artwork 1920x1080 pt with a 1465x767 pt crop (hig:game-center#Challenges).
- Multiplayer: display party codes (usually eight characters) in the game and allow manual entry. Allow late joining and rejoining. Activity artwork as for challenges (hig:game-center#Multiplayer-activities).
- watchOS: no system UI for Game Center; content appears on the iPhone (hig:game-center#watchOS). tvOS: optional dashboard image 600x180 pt, no app icon.

## Generative AI
Models that generate or transform text, images, and other content.
- Design responsibly: people stay in control (discard, revert, retry). Label AI use. Where possible, offer a variant without AI (hig:generative-ai#Best-practices).
- Transparency: never present output as human-written. Explain capabilities and limitations up front, e.g. with curated example prompts (hig:generative-ai#Transparency).
- Privacy: prefer an on-device model and disclose server processing. Ask before using personal data, collect minimally, offer opt-out (hig:generative-ai#Privacy).
- Contain hallucinations: scope tasks narrowly, don't ask for uncertain facts, point out possible errors (hig:generative-ai#Inputs).
- Require confirmation before irreversible or sensitive actions (deleting, purchasing) (hig:generative-ai#Inputs).
- Outputs: offer Edit, Undo, Retry, and Adjust close to the result and visibly acknowledge corrections. For blocked requests, give hints on phrasing. Offer multiple variants (hig:generative-ai#Outputs).
- Plan for latency: specific status messages ("Summarizing key themes…") instead of "Processing…" (hig:generative-ai#Outputs).
- Voluntary, unobtrusive feedback (e.g. thumbs up/down). Keep the model separate from the UX so it's replaceable (hig:generative-ai#Continuous-improvement).
- The Foundation Models framework requires a compatible device with Apple Intelligence enabled (hig:generative-ai#Models-and-datasets).

## HealthKit
Central repository for health and fitness data.
- Without a health feature, don't request access to health data (hig:healthkit).
- A privacy policy is mandatory. Request access in context and whenever it's needed. Use the standard permission screen with a short justification and don't replicate it. Manage authorizations only via system settings (hig:healthkit#Privacy-protection).
- Activity rings only for Move, Exercise, and Stand and only for one person (clearly attributed). Not as decoration or branding, don't change colors or background. Outer margin at least the ring spacing. No rings in notifications (hig:healthkit#Activity-rings).
- **Resources – Apple Health icon:** only the Apple icon (Apple Design Resources) with the name *Apple Health* nearby. Not smaller than other icons, not a button, don't mask or alter, clear space 1/10 of the height, not in text. No screenshots of the Health app. For marketing there is the "Works with Apple Health" badge (hig:healthkit#Apple-Health-icon).
- **Spelling:** in the UI write *Apple Health* or *the Apple Health app*, never *HealthKit* (developer term). Use the system translation of "Health" (hig:healthkit#Editorial-guidelines).
- Platforms: iOS, iPadOS, watchOS (not macOS, tvOS, visionOS).

## HomeKit
Control of connected accessories via Siri and Apple Home.
- Adopt the HomeKit object model and terms: home, room, zone, accessory, service, characteristic, service group, scene, automation. Use neither "service" nor "characteristic" in the UI. "Scene" instead of "action set" (hig:homekit#Terminology-and-layout).
- Account for multiple homes, no duplicate home settings, show HomeKit details in the accessory detail view (hig:homekit).
- Setup: use the system setup flow and provide a purpose string justification. Don't require an account or personal data; custom setup steps only afterward (hig:homekit#Setup).
- Service names: only alphanumeric characters, spaces, and apostrophes, begin and end with an alphanumeric character, no emoji, no company or model names, no room information in the name (hig:homekit#Help-people-choose-useful-names).
- Siri: after setup, show example phrases with the chosen name. Shortcuts only for functions HomeKit doesn't cover (hig:homekit#Siri-interactions).
- Write to the HomeKit database only with permission and follow HomeKit in case of conflicts. Don't obscure camera images, microphone button only with bidirectional audio (hig:homekit#Custom-functionality).
- **Resources:** HomeKit icon (black, white, custom color) and Apple Home app icon only from Apple. Don't use the HomeKit icon interactively; the Home icon may link to the App Store page (hig:homekit#Using-HomeKit-icons).
- **Spelling:** *HomeKit* one word (capital H and K), *Apple Home* two words. Don't use HomeKit as an adjective ("HomeKit lightbulbs" is wrong); HomeKit doesn't act on its own. On first mention "Apple Home app", don't translate, no device categories ("iPad", not "tablet") (hig:homekit#Referring-to-HomeKit).

## iCloud
Transparent synchronization of content across all devices.
- Use iCloud automatically. If a choice is necessary, offer "all or nothing" once at first launch (hig:icloud#Best-practices).
- Don't ask per document. Keep content up to date, make downloads of large files controllable, and show progress subtly (hig:icloud).
- Respect storage: store only user-generated content, no regenerable resources. The Documents folder ends up in the backup (hig:icloud).
- Without iCloud, no alert, only a subtle notice. Store app state and cross-device settings in iCloud (hig:icloud).
- Warn before deleting, because it deletes on all devices. Resolve conflicts automatically where possible, otherwise offer the choice unobtrusively. Include iCloud content in search (hig:icloud).
- Games: sync game saves via the GameSave framework (hig:icloud).

## ID Verifier
iPhone app reads mobile IDs (ISO18013-5) in person without additional hardware, from iOS 17.
- Prefer Display Only Request (data stays in the system UI). Data Transfer Request only when legally required and with an additional entitlement (hig:id-verifier).
- Request only necessary data, e.g. an age threshold (`ageAtLeast`) instead of date of birth (hig:id-verifier#Best-practices).
- Register with Apple Business Register so the organization's name and logo appear (hig:id-verifier).
- Start button "Verify Age" or "Verify Identity". No NFC or QR symbol, never the Apple logo (hig:id-verifier).
- With Display Only, offer buttons such as "Matches Person"/"Doesn't Match Person" for the response (hig:id-verifier).
- Platforms: iOS only.

## iMessage apps and stickers
iMessage apps and sticker packs in Messages and FaceTime effects.
- One primary experience per iMessage app. Make content from the main app shareable (hig:imessage-apps-and-stickers#Best-practices).
- Core functionality in the compact view. Text input only in the expanded view (hig:imessage-apps-and-stickers).
- Stickers: expressive, inclusive, legible on all backgrounds and when rotated or scaled. One localized alternative description per sticker for VoiceOver (hig:imessage-apps-and-stickers).
- Provide the icon square; the system masks it. Sizes include Messages 148x110/143x100/120x90 (@3x 180x135)/64x48 (@3x 96x72)/54x40 (@3x 81x60), Settings 58x58/87x87, App Store 1024x1024 px (hig:imessage-apps-and-stickers#Icon-sizes).
- Stickers @3x: small 300x300, regular 408x408, large 618x618 px. No mixed sizes within a pack, no more than 500 KB per file. PNG/APNG with 8-bit transparency, GIF with single-color transparency, JPEG without (hig:imessage-apps-and-stickers#Sticker-sizes).
- Platforms: iOS, iPadOS.

## Live Photos
Photos with sound and motion before and after capture.
- Apply edits to all frames, otherwise offer conversion to a still image. Never split Live Photos into individual frames or audio (hig:live-photos#Best-practices).
- When sharing, show a preview of the full content and always also allow sharing as a regular photo (hig:live-photos).
- Show download progress and readiness for playback. Where not supported, show as a still image (hig:live-photos).
- Identify Live Photos through hinted motion. Otherwise always show the system badge (with or without text) in the same place, typically in a corner. No play button like for video (hig:live-photos).
- Platforms: iOS, iPadOS, macOS, tvOS. visionOS display only, no capture. watchOS not supported.

## Mac Catalyst
Mac version of an iPad app.
- Good candidates already support drag and drop, keyboard navigation and shortcuts, multitasking, and multiple windows. Apps with a core dependency on gyroscope, rear camera, HealthKit, or ARKit are less suitable (hig:mac-catalyst#Before-you-start).
- Idiom: the iPad idiom scales to 77 % (17pt becomes 13pt). The Mac idiom renders at 100 %. Then check the layout, adjust font sizes, use text styles instead of fixed sizes, and create a separate asset catalog if needed (hig:mac-catalyst#Choose-an-idiom).
- Replace the tab bar with a split view with sidebar (preferred) or a segmented control. Add top-level items to the View menu. Offer Next and Previous buttons in addition to swipes (hig:mac-catalyst#Navigation).
- Design a Mac-specific app icon (hig:mac-catalyst#App-icons).
- Layout: multi-column, inspector instead of popover. Move controls into the toolbar, top-down flow, move buttons away from the bottom and side edges (hig:mac-catalyst#Layout).
- Put all commands in the menu bar (`UIKeyCommand`, `UIMenuBuilder`) and offer context menus generously (hig:mac-catalyst#Menus).
- Platforms: iPadOS and macOS.

## Machine learning
Models for personalized, learning features. For generative cases see Generative AI.
- Clarify the role: critical or complementary, private or public, proactive or reactive, visible or invisible, dynamic or static (hig:machine-learning#The-role-of-machine-learning-in-your-app).
- Explicit feedback only when needed and voluntary; describe options with their consequences ("Suggest less pop music" instead of "dislike"). Apply immediately and remember permanently (hig:machine-learning#Explicit-feedback).
- Implicit feedback: protect data, give control, don't restrict discovery, prioritize recent signals, hold back sensitive recommendations (hig:machine-learning#Implicit-feedback).
- Calibration only if indispensable: once, short, with progress indicator, cancelable at any time, data changeable later (hig:machine-learning#Calibration).
- Plan for mistakes. Make corrections familiar and immediately effective, prefer guided corrections. Be especially careful with proactive features (hig:machine-learning#Mistakes).
- Multiple options: diverse, not too many, most likely first (hig:machine-learning#Multiple-options).
- Translate confidence into understandable concepts ("Because you listen to pop music" instead of "97% match"). With low confidence, show nothing (hig:machine-learning#Confidence).
- Attributions factual ("Because you've read …", not "… love …") and without statistical jargon. Communicate limitations up front (hig:machine-learning#Attribution).

## Maps
Maps (MapKit) in an app or website.
- Keep maps interactive. Choose emphasis style *default* (saturated) or *muted* (desaturated, for lots of your own content) (hig:maps#Best-practices).
- Offer search with category filters, mark selections clearly, cluster overlapping POIs (hig:maps).
- Don't permanently obscure the Apple logo and legal link: e.g. 7 pt at the sides, 10 pt at top and bottom, 10 pt above the lowest resting position of a card. Below 200x100 px they aren't shown (hig:maps).
- Annotations in the app's style. Icon strings with 2–3 characters. Overlays *above roads* (default) or *above labels*. Design custom controls with high contrast (hig:maps#Custom-information).
- Place cards: choose the style (automatic, callout full/compact, caption, sheet) to fit the map size and don't duplicate information. Keep the location visible. Outside a map, the place card must contain a map (hig:maps#Place-cards).
- Indoor maps: level of detail by zoom, floor picker with numbers, surroundings dimmed, limit scrolling, don't copy Apple Maps (hig:maps#Indoor-maps).
- watchOS: static snapshots, no more than five annotations, visible without scrolling, smallest region containing all POIs (hig:maps#watchOS).

## NFC
Reading nearby NFC tags (Core NFC).
- Don't ask people to touch: "scan" and "hold near" instead of "tap" and "touch" (hig:nfc#In-app-tag-reading).
- No technical terms (NFC, Core NFC, tag). Instead, name the object ("Scan the [object]") (hig:nfc).
- Scanning sheet text: one complete sentence in sentence case with a period, short, adapted for subsequent scans (hig:nfc).
- Offer both background tag reading and in-app scanning (hig:nfc#Background-tag-reading).
- Platforms: iOS, iPadOS.

## Photo editing
Photo editing extensions in the Photos app.
- On cancel, discard only after confirmation, but only if edits have already been made (hig:photo-editing#Best-practices).
- No custom top toolbar; the modal already has one (hig:photo-editing).
- Allow previewing before returning. Use the app icon as the extension icon (hig:photo-editing).
- Platforms: iOS, iPadOS, macOS.

## ResearchKit
Apps for medical studies.
- Onboarding always in the order introduction, eligibility, consent, data access (hig:researchkit#Creating-the-onboarding-experience).
- Check eligibility early. Divide consent into sections (with "Learn More"), optionally a comprehension quiz, then signature and contact (hig:researchkit).
- Request only study-critical data and explain the reason (hig:researchkit).
- Surveys: state number and duration, one question per screen, show progress, keep it short, report completion (hig:researchkit#Conducting-research).
- Explain active tasks clearly, state prerequisites, make the end recognizable (hig:researchkit).
- Keep the profile screen (data, withdrawal, consent) and a dashboard for motivation permanently accessible (hig:researchkit#Managing-personal-information-and-providing-encouragement).
- The page notes that it is not legal advice. Platforms: iOS, iPadOS.

## SharePlay
Shared real-time activities via FaceTime and Messages.
- Use for real time. For asynchronous collaboration, offer sharing or saving afterward (hig:shareplay#Best-practices).
- Clear entry point, e.g. a button with the SharePlay symbol. Joining without hurdles: sign-in and subscription in a self-dismissing view, provisional access, or Family Sharing (hig:shareplay).
- Describe activities concisely (title, short text, image). When others make changes, show who is doing what (hig:shareplay).
- **Spelling:** *SharePlay* as a noun or verb ("Join SharePlay", "SharePlay Movie"), without adjectives (not "spatial"/"virtual") and without inflections (SharePlayed, etc.) (hig:shareplay).
- iOS/iPadOS/macOS: support Picture in Picture for shared video (hig:shareplay#iOS-iPadOS-macOS).
- visionOS: start from a window. Spatial templates (side-by-side, surround, conversational) or custom templates. Up to five spatial Personas, seats at least one meter apart, roles independent of seats (hig:shareplay#visionOS).
- Platforms: not watchOS.

## ShazamKit
Audio recognition against the Shazam catalog or a custom catalog.
- Request microphone access with an understandable justification (hig:shazamkit, see hig:privacy).
- Stop recording as early as possible (hig:shazamkit#Best-practices).
- Saving recognized songs to the iCloud library only via opt-in (hig:shazamkit).
- Platforms: all six. The page is very short (two rules).

## Sign in with Apple
Sign-in with the Apple Account, optionally with a private relay email.
- Require sign-in only in exchange for value and as late as possible. If an account is mandatory, explain why first. Offer linking with existing accounts. In commerce, ask only after the purchase (hig:sign-in-with-apple#Offering-Sign-in-with-Apple).
- Welcome people immediately after sign-in. Show the status ("Using Sign in with Apple") (hig:sign-in-with-apple).
- Data: mark required and optional, don't require a password, with a relay address don't ask for the private email, ask for optional data later (hig:sign-in-with-apple#Collecting-data).
- Place the button prominently, not smaller than other sign-in buttons and visible without scrolling (hig:sign-in-with-apple#Displaying-buttons).
- **Resources – system buttons:** `ASAuthorizationAppleIDButton` or `WKInterfaceAuthorizationAppleIDButton`. Titles "Sign in with Apple", "Sign up with Apple", "Continue with Apple". watchOS only "Sign in". Styles White (all, for dark backgrounds), White with outline (iOS, macOS, web, for light backgrounds), Black (all, for light backgrounds). watchOS uses dark gray instead of black. Minimum 140pt × 30pt, margin 1/10 of the height, corner radius adjustable (hig:sign-in-with-apple#Using-the-system-provided-buttons).
- **Custom buttons** (iOS, macOS, web): logo only from the Apple Design Resources (PNG, SVG, PDF). Only the three titles; logo and title only black or white. Title font about 43 % of the button height. Right margin at least 8 % of the width. PNG only at 44 pt height or 44x44 pt for logo-only. Logo-only at a 1:1 ratio, shape via mask. App Review checks all custom buttons (hig:sign-in-with-apple#Creating-a-custom-Sign-in-with-Apple-button).

## Siri
System assistant, with Siri AI (Apple Intelligence) for context-aware app actions.
- Provide functionality and content via App Intents (intents, entities). In common domains, use App Schemas. Annotate onscreen content, donate entities to Spotlight and actions as intents (hig:siri#Getting-your-app-to-work-with-Siri).
- Identify the most common actions and their context. Use familiar terms, offer relevant rather than all content, no advertising (hig:siri#Best-practices).
- Custom responses only if the built-in ones aren't sufficient. Then clear, concise, self-contained both aurally and visually, device-independent, without the app name and without humor (hig:siri#Customizing-your-app's-experience-with-Siri).
- Use inclusive phrasing ("Who should I send it to?"). Replace long lists with open follow-up questions. Name errors specifically (hig:siri).
- For functionality outside the schemas, use App Shortcuts (hig:siri, hig:app-shortcuts).
- **Spelling:** refer to Siri by name, no pronouns. Don't imitate Siri, no reserved phrases ("Hey Siri", emergency calls). In translations, translate only "Hey". The page lists the permitted forms per locale, e.g. de_DE "Hey Siri", fr_FR "Dis Siri" (hig:siri#Editorial-guidelines).

## Tap to Pay on iPhone
Contactless payment on the merchant's iPhone without additional hardware (ProximityReader, via a PSP).
- Have terms and conditions accepted before customer contact, by admins only. Trigger an iOS update beforehand if needed (hig:tap-to-pay-on-iphone#Enabling-Tap-to-Pay-on-iPhone).
- Tutorial covering all payment types (custom or `ProximityReaderDiscovery`). It must show checkout, card holding, and PIN entry including accessibility mode (hig:tap-to-pay-on-iphone#Educating-merchants).
- Always offer the option at checkout, even while configuration is in progress (then with a progress indicator). Prepare at launch and every time the app returns to the foreground (`prepare`) (hig:tap-to-pay-on-iphone#Checking-out).
- **Button label:** "Tap to Pay on iPhone" or, when space is limited, "Tap to Pay". Icon `wave.3.right.circle(.fill)`, never the Apple logo. Shape and color matching the app. If it's the only payment method, the existing Charge or Checkout button may remain (hig:tap-to-pay-on-iphone).
- Set the final amount including tip before the tap. Show the result (successful or declined) clearly, offer a digital receipt, alternatives on failure (hig:tap-to-pay-on-iphone#Displaying-results).
- Without an amount (Look Up, Store Card, Verify, Refund) and for loyalty cards, use generic labels without "Tap to Pay" (hig:tap-to-pay-on-iphone#Additional-interactions).
- **Resources:** Apple-approved assets in the Tap to Pay on iPhone Marketing Guidelines. Platforms: iOS only.

## VoiceOver
Screen reader for all platforms, also in Unity apps via Apple's plug-ins.
- Give all important elements current, descriptive labels, including custom elements (hig:voiceover#Descriptions).
- Describe meaningful images, hide decorative ones (`accessibilityHidden`). Equip charts with a short description and accessible interactions (hig:voiceover).
- Use unique titles and correct headings. Make grouping, order, and relationships explicit, e.g. group an image and its caption (hig:voiceover#Navigation).
- Announce content and layout changes (`AccessibilityNotification`). Support the rotor (hig:voiceover).
- visionOS: with VoiceOver, custom gestures don't receive hand input by default (Direct Gesture mode as opt-out) (hig:voiceover#visionOS).

## Wallet
Passes, order tracking, and identity verification in Apple Wallet.
- Offer new passes directly; add recurring ones in the background after one-time permission. Group related passes. Don't repeat declined suggestions (hig:wallet#Passes).
- "Add to Apple Wallet" button (`PKAddPassButton`) for existing passes that haven't been added. Link "View in Wallet". Set expiration correctly, delete only with permission, specify relevance for Lock Screen and Live Activity (hig:wallet).
- Change messages only for time-critical changes, never for marketing (hig:wallet).
- Design: uncluttered front, important information in header fields, check contrast, device-neutral language ("Slide to view" is wrong). Don't pad images, because watchOS crops white space (hig:wallet#Designing-passes).
- Pass styles: boarding, coupon, event ticket (also poster), store card, poster generic, generic. Poster passes and semantic boarding passes need semantic tags plus pass fields for older iOS versions (hig:wallet#Pass-styles).
- Images as PNG @2x/@3x without embedded text or barcodes. logo 50 pt high (width 50–160), primaryLogo 30 pt (30–126), secondaryLogo 12 pt (12–135), icon 38x38 pt, strip 375x144 pt, thumbnail 90 pt high (60–90), background 343x503 pt, artwork (poster) 358x448 pt, footer 268x15 pt (hig:wallet#Pass-images).
- Order tracking: provide immediately after the order, keep status current. Logo and product images 300x300 px, not transparent. Provide contact options and a tracking link, no duplicate notifications. Button "Track with Apple Wallet" (`AddOrderToWalletButton`, from iOS 17) (hig:wallet#Order-tracking).
- Identity verification: only with device support and only at the moment of need. Purpose string as a complete sentence. Minimal data, state the retention period. Buttons "Verify Age/Identity with Apple Wallet", "Continue with Apple Wallet", "Verify with Apple Wallet", always white on black, optionally with outline (hig:wallet#Identity-verification).
- **Resources:** Pass Designer (Mac app with templates), Add-to-Apple-Wallet badge for email and web (Add to Apple Wallet guidelines). Platforms: not tvOS. watchOS shows passes as a carousel and crops strip images (hig:wallet#watchOS).

---

## Cross-references (located in the HIG under Components / System experiences)

### Widgets
Glanceable content and focused interactions on the Home Screen, Lock Screen, StandBy, desktop, Smart Stack, visionOS, and Apple HomeView. Located in the HIG under Components / System experiences.
- One simple idea that fits the app's purpose, with dynamic content. Multiple sizes only if they add value; balance information density (hig:widgets#Best-practices).
- Default margin 16 pt, tighter 11 pt. Text at least 11 pt, don't rasterize (hig:widgets).
- Animations for updates no more than two seconds. Let the system update date and time (hig:widgets).
- Keep interaction simple, deep link to the appropriate place (hig:widgets#Adding-interactivity).
- For real-time updates use Live Activities, because widgets don't update in real time (hig:widgets#iOS-iPadOS).

### Live Activities
Progress of a time-limited event in the Dynamic Island, Lock Screen, StandBy, CarPlay, Mac menu bar, and Smart Stack. Located in the HIG under Components / System experiences.
- Only for tasks with a beginning and end, no more than eight hours. No advertising, no sensitive data (hig:live-activities#Best-practices).
- Compact and minimal must fit into a circle with a 28 pt diameter when width is limited (hig:live-activities#Creating-Live-Activity-layouts).
- Lock Screen margin 14 pt. Check contrast in Dark Mode, Always On, and StandBy Night Mode (hig:live-activities#Lock-Screen-presentation).
- Update only for new content and alert only for essential changes. End immediately, dismissal usually after 15–30 minutes (system no more than four hours) (hig:live-activities#Starting-updating-and-ending-a-Live-Activity).
- In CarPlay, interactive elements are disabled (hig:live-activities#CarPlay).

### App Shortcuts
Key app functions for Siri, Spotlight, Shortcuts, the Action button, and Apple Pencil (squeeze). Located in the HIG under Components / System experiences.
- In common domains, check App Schemas first; App Shortcuts for everything else (hig:app-shortcuts#Best-practices).
- No more than 10 App Shortcuts per app. Most common tasks, no more than one optional parameter with predictable values (hig:app-shortcuts).
- Short, memorable phrases with the app name. All critical information also in the dialog text for audio-only devices (hig:app-shortcuts#Editorial-guidelines).
- Spelling: *App Shortcuts* and *Shortcuts* (app) in title case and plural, individual "shortcuts" lowercase (hig:app-shortcuts).
- Order by importance in the app and Spotlight. macOS doesn't support App Shortcuts, only App Intents (hig:app-shortcuts#macOS).

---

## Observations/ambiguities

**Contradictions and errors in the sources**
- **Tap to Pay on iPhone:** The header says "Update 2025-01-17", the change log "January 17, 2024" (listed above "May 7, 2024"). Probably a typo in the change log.
- **CarPlay:** The page mentions Apple HomeView, although the last change log entry is from 2023-05-02. So the content was changed without a change log entry. Per the Widgets page, HomeView was only added on 2026-10-13.
- **HomeKit:** The header line names all six platforms, the introductory text only "iOS, tvOS, or watchOS app".
- **HealthKit vs. CareKit:** For repeated access requests, one says "needs to", the other "good idea". The level of obligation differs.
- **Wallet:**
  - The "Generic passes" section links to "Creating a Poster Generic Pass".
  - The terms "Verify with Wallet" and "Verify with Apple Wallet" appear mixed side by side.
- **Apple Pay:** In the minimum size table, the rows Buy, Check Out, Donate, Set Up, and Subscribe are empty. Presumably the 140pt × 30pt from the row above applies (merged cells). Check in the original before use.

**Outdated or noticeably thin pages**
- **Always On:** mentions only iPhone 14 Pro/Pro Max. The last content status is from 2022; the 2023 update concerned only the artwork.
- **Little content:** ShazamKit (two rules), Photo editing (four rules), NFC, Live Photos. Without a change log or update note: Live Photos, NFC, Photo editing, ShazamKit, HealthKit, Augmented reality, and Sign in with Apple (the latter only with a 2022 change log entry). Siri has no "Platform considerations" section.

**Update notes 2025/2026**
- Apple In-App Purchase, 2026-09-17: renamed from "In-App Purchase" and revised.
- SharePlay, 2026-09-09: new structure, more visionOS content, custom templates.
- Apple Pay, Wallet (iOS 27, Pass Designer), Siri (Siri AI), Generative AI, and Machine learning, each 2026-06-08.
- iCloud (GameSave), App Clips (demo App Clips), and Game Center (challenges, multiplayer, Games app), each 2025-06-09.
- VoiceOver, 2025-03-07: new page.
- Cross-references: Widgets and Live Activities 2026-10-13, App Shortcuts 2026-06-08 (App Schemas).
