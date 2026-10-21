# audit – check HIG compliance

A systematic, cited review. For large targets (whole app, several platforms) launch the `apple-design:hig-reviewer` agent once per platform in parallel and merge the results.

## Clarify scope

Determine the target (file, screen, feature, whole app). If unclear: AskUserQuestion – "What scope?" (current change (Recommended) · one screen · whole app) and "Which platforms?".

## Review steps

1. **Context:** `APPLE_DESIGN.md`, target OS, platforms. Per platform, load the checklist from `reference/platforms/<p>.md` (section "Review checklist").
2. **Static check in code** – quick finds:
   ```bash
   grep -rnE "\.font\(\.system\(size:" --include=*.swift .             # fixed font sizes
   grep -rnE "Color\((red|.*#)|UIColor\(red:|NSColor\(red:|Color\(hex" --include=*.swift .  # raw colors
   grep -rnE "\.frame\((width|height): *[1-3][0-9]\b" --include=*.swift .   # possibly too-small hit targets
   grep -rnE "onTapGesture" --include=*.swift .                          # tap without button semantics/label?
   grep -rnE "\.glassEffect|\.background\(\.ultraThinMaterial" --include=*.swift .   # check where glass/materials are used
   grep -rnE "Image\(\"" --include=*.swift .                              # custom images instead of SF Symbols?
   grep -rnE "accessibilityLabel|accessibilityHidden" --include=*.swift . | wc -l
   ```
   Judge every hit in context – no automatic verdicts.
3. **Rendered check** (if it builds): screenshots per device class, light/dark, AX text size (see build.md). Without a Simulator: say that only a static review was done.
4. **Cross-cutting:** [accessibility](../foundations/accessibility.md), [typography](../foundations/typography.md), [color-and-dark-mode](../foundations/color-and-dark-mode.md), [materials-and-liquid-glass](../foundations/materials-and-liquid-glass.md), component rules for the components in use.
5. **Doubtful cases:** check the original: `hig_search.py page <slug> --section "<…>"`.

## Severity

| Level | Meaning | Examples |
|---|---|---|
| P0 Blocker | breaks usability/accessibility or an App Review-relevant rule | no VoiceOver label on an icon button, text truncated at large sizes, blocked back swipe, restricted Apple symbol misused |
| P1 High | clearly un-platform-like | custom tab bar, hamburger menu on iOS, iPhone layout stretched on iPad, missing menu commands on the Mac |
| P2 Medium | consistency/refinement | raw colors instead of semantic ones, mixed symbol weights, wrong button hierarchy |
| P3 Low | improvement | haptics, animation, copy |

## Report

```markdown
## HIG audit: <target> (<platforms>, target OS …)
Checked: static | Simulator (<devices>) · HIG mirror as of: <date>

| # | Level | Location | Finding | Source | Fix |
|---|---|---|---|---|---|
| 1 | P0 | `Views/Foo.swift:42` | … | hig:buttons#Best-practices | … |

**Strengths:** …
**Next steps:** fix P0/P1 now? (→ AskUserQuestion: fix all P0+P1 (Recommended) · P0 only · report only)
```

After approval, fix, then re-check the affected screens.
