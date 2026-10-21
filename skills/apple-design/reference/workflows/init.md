# init – capture project context

Goal: an `APPLE_DESIGN.md` in the project root that steers every later design decision. Template: [templates/APPLE_DESIGN.md](../../templates/APPLE_DESIGN.md).

## 1. Look it up yourself first

Before asking, collect what the project already says:

```bash
find . -maxdepth 3 \( -name "*.xcodeproj" -o -name "Package.swift" -o -name "*.xcworkspace" \) -not -path "*/.build/*"
grep -hoE "(IPHONEOS|MACOSX|WATCHOS|XROS|TVOS)_DEPLOYMENT_TARGET = [0-9.]+" */project.pbxproj | sort -u
grep -hoE "TARGETED_DEVICE_FAMILY = \"?[0-9,]+\"?" */project.pbxproj | sort -u   # 1=iPhone 2=iPad 3=TV 4=Watch 6=Mac Catalyst 7=Vision
grep -rhoE "^import (SwiftUI|UIKit|AppKit|WatchKit|WidgetKit|ActivityKit)" --include=*.swift . | sort | uniq -c
find . -name "AccentColor.colorset" -o -name "*.icon" -o -name "AppIcon.appiconset" | head
```

Also read, if present: README, existing `DESIGN.md`/`PRODUCT.md` (impeccable), the asset catalog (colors, icons), Info.plist (`UIRequiredDeviceCapabilities`, purpose strings).

## 2. Interview (AskUserQuestion)

Only ask what isn't in the project. One round of up to 4 questions, a second round if needed.

**Round 1**
1. *Platforms* (multiSelect): iOS · iPadOS · macOS · watchOS. Mention the preselection from TARGETED_DEVICE_FAMILY.
2. *Stack*: SwiftUI (Recommended) · UIKit · AppKit · Mixed/legacy. For "mock-ups only": Figma with the Apple UI kit.
3. *Target OS*: current OS (Liquid Glass fully available) · current OS −1 · older (with `#available` fallbacks). Briefly explain the consequence for Liquid Glass/new APIs.
4. *App type / mode*: tool/productivity (Operate) · content/reading (Read) · media/experience (Experience) · utility/glance (Watch, widgets).

**Round 2** (only if relevant)
- *Brand*: existing accent color? (hex) · custom typeface for display moments? · system look only.
- *Accessibility goal*: baseline (HIG minimum) · extended (all Dynamic Type sizes incl. accessibility sizes, VoiceOver flows tested).
- *System integration* (multiSelect): widgets · Live Activities · complications/Smart Stack · App Intents/Siri/Shortcuts · notifications · Sign in with Apple / Apple Pay.
- *Design tool*: Figma · Sketch · straight in Xcode/Previews.

## 3. Write APPLE_DESIGN.md

Fill in the template, concisely. Spell out derived decisions, e.g.:
- Navigation skeleton per platform (iPhone: tab bar with N sections; iPad: sidebar-adaptable tab layout; Mac: NavigationSplitView + menu bar; Watch: NavigationStack + vertical pages).
- Which references to load (`reference/platforms/<p>.md`).
- Matching Apple resources (`resources.py list --platform <p>`): add the UI kit links for the chosen design tool.

## 4. Wrap-up

- Summarize briefly, list open points.
- Offer: install fonts (`resources.py install-fonts --accept-license`, only after the user agrees to Apple's license), open the UI kit, then `shape <first feature>`.
