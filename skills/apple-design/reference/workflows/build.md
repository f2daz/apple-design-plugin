# build – implement platform-true

Prerequisites: `APPLE_DESIGN.md` read, a spec from `shape` (or an unambiguous small task), platform reference loaded.

## Code rules

**Structure & navigation (SwiftUI preferred)**
- Top-level sections: `TabView` with `Tab(...)`; on iPad/Mac sidebar-adaptable (`.tabViewStyle(.sidebarAdaptable)`) where available. Hierarchy: `NavigationStack` / `NavigationSplitView`.
- Side tasks: `.sheet` with clear Cancel/Done in the `toolbar` (`.cancellationAction`, `.confirmationAction`); confirming destructive actions: `.confirmationDialog` or `.alert` with `role: .destructive`.
- Actions in `.toolbar` with semantic placements instead of custom bars; contextual actions via `.contextMenu` / `.swipeActions`.
- Mac: `commands { }` for the menu bar and keyboard shortcuts, a `Settings { }` scene, `.inspector`, `Table` for tabular data. Watch: `NavigationStack`, `TabView` with `.verticalPage`, Digital Crown.

**Visuals**
- Text via text styles (`.font(.body)`, `.headline` …), never fixed sizes for reading text; custom fonts with `Font.custom(_:size:relativeTo:)`.
- Colors: semantic (`.primary`, `.secondary`, `Color(.systemBackground)`, `.tint`), accent via `AccentColor` in the asset catalog. Custom colors as assets with light/dark/high-contrast variants.
- Liquid Glass: system components (bars, toolbars, tab bars, sheets, buttons with `.buttonStyle(.glass)`/`.glassProminent`) adopt it automatically. Use a custom `.glassEffect()` only for floating controls on the functional layer, several of them inside a `GlassEffectContainer`. Never on list cells, content cards or backgrounds. For older target OS use `if #available` with a material fallback.
- Symbols: `Image(systemName:)` / `Label(_:systemImage:)`; choose the rendering mode deliberately; check the minimum OS with `sf_symbols.py info`.
- Spacing: use standard padding and `Form`/`List` styles instead of magic numbers. Content within safe areas, backgrounds may bleed (`.ignoresSafeArea` for backgrounds only).

**Behavior**
- Every custom interaction: pressed state, VoiceOver label (`.accessibilityLabel`), `.accessibilityHint` where useful, hit target ≥ platform minimum (`.contentShape`, `.frame(minWidth:minHeight:)`).
- Animations with `withAnimation`/`.animation(_:value:)`, respect `@Environment(\.accessibilityReduceMotion)`; haptics via `.sensoryFeedback`, purposeful, not on every tap.
- Empty/loading/error states: `ContentUnavailableView`, `ProgressView`, understandable copy.

> API names that are not in the HIG mirror (e.g. `GlassEffectContainer`, `.glassProminent`) are framework knowledge – check against the current developer documentation for the project's target OS.

## Steps

1. Adopt the project's existing patterns (naming, folders, components) – don't invent a parallel system.
2. Implement screen by screen; give every view a `#Preview` in light/dark and a large Dynamic Type size:
   ```swift
   #Preview("Dark · AX3") { MyView().preferredColorScheme(.dark).dynamicTypeSize(.accessibility3) }
   ```
3. Build and look: `xcodebuild -scheme <S> -destination 'platform=iOS Simulator,name=<device>' build`, Simulator screenshot `xcrun simctl io booted screenshot <path>.png`; Dark Mode `xcrun simctl ui booted appearance dark`; text size `xcrun simctl ui booted content_size accessibility-extra-extra-large`. For macOS: launch the app and use `screencapture -l <windowid>` or `-w`. Device sizes: `device_specs.py`.
4. Fix everything one look reveals in a single pass, then look again. State what was checked in the Simulator and what only in code.
5. Short report + offer: `audit` or `polish`.
