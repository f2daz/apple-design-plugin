# init – Projektkontext erfassen

Ziel: `APPLE_DESIGN.md` im Projekt-Root, die jede spätere Designentscheidung steuert. Vorlage: [templates/APPLE_DESIGN.md](../../templates/APPLE_DESIGN.md).

## 1. Erst selbst nachsehen

Bevor du fragst, sammle, was im Projekt steht:

```bash
find . -maxdepth 3 \( -name "*.xcodeproj" -o -name "Package.swift" -o -name "*.xcworkspace" \) -not -path "*/.build/*"
grep -hoE "(IPHONEOS|MACOSX|WATCHOS|XROS|TVOS)_DEPLOYMENT_TARGET = [0-9.]+" */project.pbxproj | sort -u
grep -hoE "TARGETED_DEVICE_FAMILY = \"?[0-9,]+\"?" */project.pbxproj | sort -u   # 1=iPhone 2=iPad 3=TV 4=Watch 6=Mac Catalyst 7=Vision
grep -rhoE "^import (SwiftUI|UIKit|AppKit|WatchKit|WidgetKit|ActivityKit)" --include=*.swift . | sort | uniq -c
find . -name "AccentColor.colorset" -o -name "*.icon" -o -name "AppIcon.appiconset" | head
```

Auch lesen, falls vorhanden: README, bestehende `DESIGN.md`/`PRODUCT.md` (impeccable), Asset-Katalog (Farben, Icons), Info.plist (`UIRequiredDeviceCapabilities`, Purpose strings).

## 2. Interview (AskUserQuestion)

Frage nur, was nicht im Projekt steht. Eine Runde mit bis zu 4 Fragen, ggf. zweite Runde.

**Runde 1**
1. *Plattformen* (multiSelect): iOS · iPadOS · macOS · watchOS. Vorauswahl aus TARGETED_DEVICE_FAMILY nennen.
2. *Stack*: SwiftUI (Empfohlen) · UIKit · AppKit · Gemischt/Bestand. Bei „nur Mock-ups“: Figma mit Apple UI Kit.
3. *Ziel-OS*: aktuelles OS (Liquid Glass voll nutzbar) · aktuelles OS −1 · älter (mit `#available`-Fallbacks). Erkläre kurz die Konsequenz für Liquid Glass/neue APIs.
4. *App-Art / Modus*: Werkzeug/Produktivität (Operate) · Inhalt/Lesen (Read) · Medien/Erlebnis (Experience) · Utility/Glance (Watch, Widgets).

**Runde 2** (nur wenn relevant)
- *Marke*: Akzentfarbe vorhanden? (Hex) · eigene Schrift für Display-Momente? · nur System-Look.
- *Barrierefreiheit-Ziel*: Basis (HIG-Minimum) · erweitert (alle Dynamic-Type-Stufen inkl. Accessibility sizes, VoiceOver-Flows getestet).
- *Systemintegration* (multiSelect): Widgets · Live Activities · Complications/Smart Stack · App Intents/Siri/Shortcuts · Notifications · Sign in with Apple / Apple Pay.
- *Design-Werkzeug*: Figma · Sketch · direkt in Xcode/Previews.

## 3. APPLE_DESIGN.md schreiben

Vorlage füllen, knapp. Ableitungen ausformulieren, z. B.:
- Navigationsgerüst je Plattform (iPhone: Tab bar mit N Bereichen; iPad: Sidebar-adaptives Tab-Layout; Mac: NavigationSplitView + Menüleiste; Watch: NavigationStack + vertikale Seiten).
- Welche Referenzen geladen werden (`reference/platforms/<p>.md`).
- Passende Apple-Ressourcen (`resources.py list --platform <p>`): UI-Kit-Links für das gewählte Design-Werkzeug eintragen.

## 4. Abschluss

- Kurz zusammenfassen, offene Punkte nennen.
- Angebot: Fonts installieren (`resources.py install-fonts --accept-license`, nur nach Zustimmung zur Apple-Lizenz), UI-Kit öffnen, dann `shape <erstes Feature>`.
