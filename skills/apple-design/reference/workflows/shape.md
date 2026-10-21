# shape – plan a feature before code exists

Result: a short spec (in chat or as `design/<feature>.md`) that `build` can implement without follow-up questions.

## Steps

1. **Understand the task.** What does the person want to get done, how often, where (on the go, at a desk, on the wrist)? If something essential is missing → one AskUserQuestion round (e.g. "How often is this used?" · "Primary platform?" · "Must it work offline?").
2. **Place it.** Does it belong in the existing navigation (which tab/sidebar section), is it a side task (sheet), a detail (push), or a system location (widget, Live Activity, control, complication, menu bar extra)? Back the decision with [components/README.md](../components/README.md) and [patterns.md](../patterns.md).
3. **Choose the idiomatic pattern per platform** (from `reference/platforms/<p>.md`). One line for each platform in `APPLE_DESIGN.md`: entry point, container, primary action, secondary actions, way back.
4. **Pick components** – system first. For real alternatives (e.g. segmented control vs. menu vs. picker), present the options with `AskUserQuestion` and an ASCII preview, recommendation first.
5. **List states:** empty, loading, partial/error, offline, no permission, a lot of content, very long text/localization, largest Dynamic Type size, Dark Mode, Reduce Motion.
6. **Content & copy:** titles, button labels (verbs), empty-state text, error messages (hig:writing).
7. **Symbols & resources:** pick SF Symbols with `sf_symbols.py search` and check their minimum OS against the target OS.

## Spec template

```markdown
## <Feature>
Goal: … · Frequency: … · Platforms: …

### Structure
| Platform | Entry point | Container | Primary action | Way back |
|---|---|---|---|---|

### Screens
#### <Screen>
- Layout (ASCII sketch)
- Components: … (hig:…)
- Symbols: `…` (iOS ≥ …)
- States: empty / loading / error / …
- Copy: …
- Accessibility: VoiceOver order, labels, Dynamic Type behavior (wrap instead of truncate)

### Open questions
```

Then offer: `build <feature>`.
