# icon – App-Icon gestalten

Regeln und Maße stehen in [icons-and-symbols.md](../foundations/icons-and-symbols.md) (Quelle: hig:app-icons). Dieses Playbook steuert den Ablauf.

## Ablauf

1. **Briefing** (AskUserQuestion): Plattformen (iOS/iPadOS, macOS, watchOS – ein `.icon` kann alle bedienen) · Motiv-Idee (eine Idee, kein Text, kein Screenshot) · Stil (flach-grafisch, Glyph mit Farbfläche, illustrativ) · Werkzeug (Icon Composer (Empfohlen) · Figma/Illustrator-Template).
2. **Vorlagen holen**:
   - Icon Composer: `resources.py show "icon composer"` (Download über developer.apple.com, ab macOS Sequoia).
   - Templates: `resources.py show "app icon template"` (Figma/Sketch-Link) bzw. `resources.py download "icon templates" --accept-license` (Photoshop/Illustrator).
3. **Ebenen planen**: Hintergrund + 1–3 Vordergrundebenen, als Vektoren (SVG) exportiert; Liquid-Glass-Eigenschaften (Specular, Blur, Translucency, Shadow) entstehen in Icon Composer, nicht im Artwork.
4. **Varianten**: Default, Dark, Clear (light/dark), Tinted – jede kontrollieren; Mac-Icon darf eigenständiger wirken, Watch-Icon ist rund (siehe Referenz).
5. **`.icon`-Paket erzeugen/prüfen**: Wenn der Skill `compose-app-icon` verfügbar ist, ihn für Aufbau/Validierung von `icon.json` nutzen. Sonst Icon Composer manuell.
6. **Einbinden**: `.icon`-Datei ins Xcode-Projekt ziehen, als App-Icon im Target setzen; ältere OS-Versionen bekommen automatisch generierte Bitmaps (Details prüfen: `hig_search.py page app-icons --section "Platform considerations"`).
7. **Prüfen**: Home Screen hell/dunkel/getönt, kleine Größen (Einstellungen, Spotlight), Mac Dock/Finder, Watch-Raster.
