# polish – final pass before release

Preserves identity and behavior; improves details. No redesign through the back door.

## Checklist

**Typography**
- [ ] Hierarchy via text styles/weights, max. 2–3 levels per screen
- [ ] Largest Dynamic Type size: wrap instead of truncate; layouts may switch from horizontal to vertical (`ViewThatFits`, `dynamicTypeSize.isAccessibilitySize`)
- [ ] Numbers in tables/timers with `.monospacedDigit()`

**Color & material**
- [ ] Tint only for interactive elements; status shown with symbol + color, never color alone
- [ ] Dark Mode and Increase Contrast reviewed; Reduce Transparency yields legible surfaces
- [ ] Liquid Glass only on the functional layer; scroll edge effects under bars are clean

**Symbols & images**
- [ ] SF Symbols consistent in weight/scale with the text; fill variants for selected states (the tab bar picks them automatically)
- [ ] Images at @2x/@3x or vector; app icon in all variants (default/dark/clear/tinted)

**Interaction**
- [ ] Pressed/disabled/selected states everywhere
- [ ] Haptics at meaningful moments (success, error, selection), not on every tap
- [ ] Animations short, interruptible, with a Reduce Motion alternative
- [ ] Keyboard: return key type, autofill `textContentType`, focus order; Mac/iPad: keyboard shortcuts for main actions

**Content & states**
- [ ] Empty, loading, error, offline states written and designed
- [ ] Copy: verbs on buttons, no blame in errors, localization (+30–40 % length, RTL) considered
- [ ] Permission prompts with an honest purpose string, requested in context

**Platform details**
- [ ] iPad: pointer hover effects, multiple windows, resizing; Mac: complete menus, minimum window size, undo/redo; Watch: glance in 2 s, Digital Crown, Always On

## Steps

Work through the checklist for the target, implement fixes in one batch, check rendered (light/dark/AX), output a change list with sources.
