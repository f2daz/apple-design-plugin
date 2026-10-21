# critique – UX-Review am gerenderten Screen

Während `audit` Regelkonformität prüft, bewertet `critique` die Gestaltung: Versteht man in drei Sekunden, was der Screen ist und was man tun kann? Fühlt es sich wie eine Apple-App an?

## Eingaben

Screenshot(s) (vom Nutzer, Simulator oder Figma-Export), alternativ Code + Previews. Ohne Bild: Simulator-Screenshot erstellen (build.md) oder ehrlich sagen, dass nur der Code bewertet wird.

## Bewertungsraster (je 1–5, mit Begründung)

1. **Klarheit & Hierarchie** – eine Primäraktion, klare Titel, Inhalt vor Chrome (hig:design-principles, hig:layout).
2. **Plattformgefühl** – Systemmuster, Navigation, Gesten, Liquid-Glass-Ebenen korrekt; kein „Web-Port“.
3. **Typografie** – Textstile, Gewichte sparsam, Dynamic-Type-tauglich.
4. **Farbe & Material** – Tint gezielt, semantische Farben, Dark Mode gleichwertig.
5. **Ikonografie** – SF Symbols konsistent (Gewicht, Rendering, Größe), verständlich.
6. **Zustände & Feedback** – leer/laden/Fehler, Pressed-States, Haptik, Motion mit Sinn.
7. **Barrierefreiheit** – Kontrast, Trefferflächen, Labels, Reihenfolge.
8. **Texte** – kurz, menschlich, handlungsorientiert.

## Ausgabe

- Gesamteindruck (2–3 Sätze), Raster als Tabelle.
- Top 3 Hebel mit größter Wirkung, jeweils: Beobachtung → Warum (`hig:`) → Vorschlag (konkret, mit Code-Skizze oder ASCII-Layout).
- Bei echten Designalternativen: AskUserQuestion mit Previews (z. B. „Liste vs. Raster für die Übersicht“).
- Angebot: `polish` oder gezielte Umsetzung.
