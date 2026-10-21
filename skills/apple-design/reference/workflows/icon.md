# icon – design the app icon

Rules and sizes are in [icons-and-symbols.md](../foundations/icons-and-symbols.md) (source: hig:app-icons). This playbook drives the process.

## Steps

1. **Briefing** (AskUserQuestion): platforms (iOS/iPadOS, macOS, watchOS – one `.icon` can serve all) · motif idea (one idea, no text, no screenshot) · style (flat graphic, glyph on a color field, illustrative) · tool (Icon Composer (Recommended) · Figma/Illustrator template).
2. **Get the templates:**
   - Icon Composer: `resources.py show "icon composer"` (download via developer.apple.com, macOS Sequoia or later).
   - Templates: `resources.py show "app icon template"` (Figma/Sketch link) or `resources.py download "icon templates" --accept-license` (Photoshop/Illustrator).
3. **Plan layers:** background + 1–3 foreground layers, exported as vectors (SVG); Liquid Glass properties (specular, blur, translucency, shadow) are applied in Icon Composer, not baked into the artwork.
4. **Variants:** default, dark, clear (light/dark), tinted – review each one; the Mac icon may look more distinct, the Watch icon is circular (see reference).
5. **Create/validate the `.icon` package:** if the `compose-app-icon` skill is available, use it to build/validate `icon.json`. Otherwise use Icon Composer manually.
6. **Integrate:** drag the `.icon` file into the Xcode project and set it as the target's app icon; older OS versions automatically get generated bitmaps (check the details: `hig_search.py page app-icons --section "Platform considerations"`).
7. **Check:** Home Screen light/dark/tinted, small sizes (Settings, Spotlight), Mac Dock/Finder, Watch grid.
