# build – plattformtreu umsetzen

Voraussetzung: `APPLE_DESIGN.md` gelesen, Spezifikation aus `shape` (oder eindeutiger Kleinauftrag), Plattform-Referenz geladen.

## Regeln für den Code

**Struktur & Navigation (SwiftUI bevorzugt)**
- Top-Level-Bereiche: `TabView` mit `Tab(...)`; auf iPad/Mac sidebar-adaptiv (`.tabViewStyle(.sidebarAdaptable)`), wenn verfügbar. Hierarchie: `NavigationStack` / `NavigationSplitView`.
- Nebenaufgaben: `.sheet` mit klarem Abbrechen/Fertig in der `toolbar` (`.cancellationAction`, `.confirmationAction`); Bestätigung destruktiver Aktionen: `.confirmationDialog` bzw. `.alert` mit `role: .destructive`.
- Aktionen in `.toolbar` mit semantischen Placements statt eigener Leisten; Kontextaktionen über `.contextMenu` / `.swipeActions`.
- Mac: `commands { }` für Menüleiste und Tastenkürzel, `Settings { }`-Scene, `.inspector`, `Table` für tabellarische Daten. Watch: `NavigationStack`, `TabView` mit `.verticalPage`, Digital Crown.

**Optik**
- Text über Textstile (`.font(.body)`, `.headline` …), nie feste Größen für Lesetext; eigene Schrift mit `Font.custom(_:size:relativeTo:)`.
- Farben: semantisch (`.primary`, `.secondary`, `Color(.systemBackground)`, `.tint`), Akzent über `AccentColor` im Asset-Katalog. Eigene Farben als Asset mit Light/Dark/High-Contrast-Varianten.
- Liquid Glass: Systemkomponenten (Bars, Toolbars, Tab bars, Sheets, Buttons mit `.buttonStyle(.glass)`/`.glassProminent`) übernehmen es automatisch. Eigenes `.glassEffect()` nur für schwebende Steuerelemente der Funktionsebene, mehrere davon in `GlassEffectContainer`. Nie auf Listenzellen, Karten mit Inhalt oder Hintergründen. Bei älterem Ziel-OS `if #available` mit Material-Fallback.
- Symbole: `Image(systemName:)` / `Label(_:systemImage:)`; Rendering-Modus bewusst wählen; Mindest-OS mit `sf_symbols.py info` prüfen.
- Abstände: Standard-Padding/`Form`/`List`-Stile nutzen, statt magischer Zahlen. Inhalte in Safe Areas, Hintergründe dürfen randlos sein (`.ignoresSafeArea` nur für Hintergrund).

**Verhalten**
- Jede eigene Interaktion: Pressed-State, VoiceOver-Label (`.accessibilityLabel`), ggf. `.accessibilityHint`, Trefferfläche ≥ Plattformminimum (`.contentShape`, `.frame(minWidth:minHeight:)`).
- Animationen mit `withAnimation`/`.animation(_:value:)`, `@Environment(\.accessibilityReduceMotion)` respektieren; Haptik über `.sensoryFeedback` gezielt, nicht inflationär.
- Leere/Lade-/Fehlerzustände: `ContentUnavailableView`, `ProgressView`, verständliche Texte.

## Ablauf

1. Bestehende Muster im Projekt übernehmen (Naming, Ordner, Komponenten) – nichts Paralleles erfinden.
2. Screen für Screen umsetzen; zu jeder View eine `#Preview` mit hell/dunkel und großer Dynamic-Type-Stufe:
   ```swift
   #Preview("Dark · AX3") { MyView().preferredColorScheme(.dark).dynamicTypeSize(.accessibility3) }
   ```
3. Bauen und ansehen: `xcodebuild -scheme <S> -destination 'platform=iOS Simulator,name=<Gerät>' build`, Simulator-Screenshot `xcrun simctl io booted screenshot <pfad>.png`; Dark Mode `xcrun simctl ui booted appearance dark`; Textgröße `xcrun simctl ui booted content_size accessibility-extra-extra-large`. Für macOS: App starten und `screencapture -l <windowid>` bzw. `-w`.
4. Auffälligkeiten in einem Durchgang beheben, dann erneut ansehen. Sagen, was im Simulator und was nur im Code geprüft wurde.
5. Kurzbericht + Angebot: `audit` oder `polish`.
