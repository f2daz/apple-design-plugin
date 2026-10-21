# critique – UX review of the rendered screen

While `audit` checks rule compliance, `critique` evaluates the design: do you understand within three seconds what the screen is and what you can do? Does it feel like an Apple app?

## Inputs

Screenshot(s) (from the user, the Simulator or a Figma export), alternatively code + previews. Without an image: take a Simulator screenshot (build.md) or say honestly that only the code is being evaluated.

## Rubric (1–5 each, with reasoning)

1. **Clarity & hierarchy** – one primary action, clear titles, content over chrome (hig:design-principles, hig:layout).
2. **Platform feel** – system patterns, navigation, gestures, Liquid Glass layers correct; no "web port".
3. **Typography** – text styles, sparing weights, Dynamic Type-ready.
4. **Color & material** – tint used deliberately, semantic colors, Dark Mode on par.
5. **Iconography** – SF Symbols consistent (weight, rendering, size), understandable.
6. **States & feedback** – empty/loading/error, pressed states, haptics, motion with purpose.
7. **Accessibility** – contrast, hit targets, labels, order.
8. **Copy** – short, human, action-oriented.

## Output

- Overall impression (2–3 sentences), rubric as a table.
- Top 3 levers with the biggest impact, each: observation → why (`hig:`) → suggestion (concrete, with a code sketch or ASCII layout).
- For real design alternatives: AskUserQuestion with previews (e.g. "list vs. grid for the overview").
- Offer: `polish` or targeted implementation.
