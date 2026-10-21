# resources – Apple Design Resources nutzen

Quelle: https://developer.apple.com/design/resources/ (Katalog im Plugin unter `data/resources.json`, aktualisierbar mit `resources.py sync`).

## Was es gibt

| Art | Inhalt | Form |
|---|---|---|
| UI-Kits | iOS & iPadOS, macOS, watchOS (auch tvOS, visionOS) – alle Systemkomponenten | Figma-Community-Datei, Sketch-Library |
| App-Icon-Templates | iOS/iPadOS/watchOS (Figma/Sketch), Photoshop/Illustrator-DMG | Link / DMG |
| Technologie-Templates | App Clips, Apple Pay, Live Activities, Messages, Sign in with Apple, Siri & App Shortcuts, Tap to Pay, TipKit, Wallet … | Figma/Sketch |
| Fonts | SF Pro, SF Compact, SF Mono, New York, SF Arabic/Armenian/Georgian/Hebrew | DMG (pkg) |
| SF Symbols App | Symbolbibliothek, Export, Custom Symbols | DMG |
| Icon Composer | Liquid-Glass-App-Icons | Download-Seite |
| Bezels | iPhone, iPad, Mac, Watch, Studio Display für Marketing | DMG (teils mehrere 100 MB) |
| Glyphen/Logos | AirPlay, ARKit, HomeKit, Apple Health, Siri, Sign in with Apple, Game Center … | DMG |

## Ablauf

1. Bedarf klären (AskUserQuestion, falls nicht klar): Mock-ups in Figma/Sketch · Fonts lokal · Icon · Marketing-Bezels · Technologie-Badge.
2. `resources.py list [--platform ios|macos|watchos]` bzw. `show "<suche>"` – Links direkt ausgeben (Figma-Links öffnen sich in der Figma-Community → „Open in Figma“/Duplizieren).
3. Downloads nur nach Zustimmung zur Apple-Lizenz (`--accept-license`). Vorher Größe nennen bei Bezels/SF Symbols (mehrere 100 MB). `status` zeigt Vorhandenes.
4. Fonts: `install-fonts --accept-license` entpackt die pkgs ohne Installer/sudo nach `~/Library/Fonts`. Hinweis: Im App-Code nie SF-Dateien einbetten – das System liefert SF automatisch (`.font(.body)`, `.fontDesign(.serif)` für New York, `.monospaced` für SF Mono).
5. Badges/Logos (App Store, Apple Pay, Wallet …): nur Originale aus https://developer.apple.com/licensing-trademarks/ nutzen, nicht nachbauen; Regeln in [technologies.md](../technologies.md).

## Lizenz in einem Satz

Fonts und Ressourcen dürfen zum Gestalten und Entwickeln von Software für Apple-Plattformen genutzt, aber nicht weitergegeben oder in andere Produkte eingebettet werden – maßgeblich ist die Lizenz im jeweiligen DMG.
