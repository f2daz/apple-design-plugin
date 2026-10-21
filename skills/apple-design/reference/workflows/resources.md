# resources – use Apple Design Resources

Source: https://developer.apple.com/design/resources/ (catalog shipped in `data/resources.json`, refresh with `resources.py sync`).

## What's available

| Kind | Content | Form |
|---|---|---|
| UI kits | iOS & iPadOS, macOS, watchOS (also tvOS, visionOS) – all system components | Figma Community file, Sketch library |
| App icon templates | iOS/iPadOS/watchOS (Figma/Sketch), Photoshop/Illustrator DMG | Link / DMG |
| Technology templates | App Clips, Apple Pay, Live Activities, Messages, Sign in with Apple, Siri & App Shortcuts, Tap to Pay, TipKit, Wallet … | Figma/Sketch |
| Fonts | SF Pro, SF Compact, SF Mono, New York, SF Arabic/Armenian/Georgian/Hebrew | DMG (pkg) |
| SF Symbols app | Symbol library, export, custom symbols | DMG |
| Icon Composer | Liquid Glass app icons | Download page |
| Bezels | iPhone, iPad, Mac, Watch, Studio Display for marketing | DMG (some several 100 MB) |
| Glyphs/logos | AirPlay, ARKit, HomeKit, Apple Health, Siri, Sign in with Apple, Game Center … | DMG |

## Steps

1. Clarify the need (AskUserQuestion if unclear): mock-ups in Figma/Sketch · fonts locally · icon · marketing bezels · technology badge.
2. `resources.py list [--platform ios|macos|watchos]` or `show "<query>"` – output the links directly (Figma links open in the Figma Community → "Open in Figma"/duplicate).
3. Downloads only after the user agrees to Apple's license (`--accept-license`). State the size first for bezels/SF Symbols (several 100 MB). `status` shows what's already there.
4. Fonts: `install-fonts --accept-license` unpacks the pkgs without the installer or sudo into `~/Library/Fonts`. Note: never embed SF font files in app code – the system provides SF automatically (`.font(.body)`, `.fontDesign(.serif)` for New York, `.monospaced` for SF Mono).
5. Badges/logos (App Store, Apple Pay, Wallet …): only use the originals from https://developer.apple.com/licensing-trademarks/, never recreate them; rules in [technologies.md](../technologies.md).

## License in one sentence

Fonts and resources may be used to design and develop software for Apple platforms, but not redistributed or embedded in other products – the license inside each DMG is authoritative.
