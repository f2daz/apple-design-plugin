# shape – Feature planen, bevor Code entsteht

Ergebnis: eine kurze Spezifikation (im Chat oder als `design/<feature>.md`), die `build` ohne Rückfragen umsetzen kann.

## Ablauf

1. **Aufgabe verstehen.** Was will die Person erledigen, wie oft, wo (unterwegs, Schreibtisch, Handgelenk)? Fehlt Wesentliches → eine AskUserQuestion-Runde (z. B. „Wie oft wird das genutzt?“ · „Primäre Plattform?“ · „Muss es offline gehen?“).
2. **Einordnen.** Gehört es in die bestehende Navigation (welcher Tab/Sidebar-Bereich), ist es eine Nebenaufgabe (Sheet), ein Detail (Push) oder ein Systemort (Widget, Live Activity, Control, Complication, Menüleisten-Extra)? Entscheidung mit [components/README.md](../components/README.md) und [patterns.md](../patterns.md) belegen.
3. **Je Plattform das idiomatische Muster wählen** (aus `reference/platforms/<p>.md`). Für jede Plattform in `APPLE_DESIGN.md` eine Zeile: Einstieg, Container, Primäraktion, Sekundäraktionen, Rückweg.
4. **Komponenten festlegen** – System zuerst. Bei echten Alternativen (z. B. Segmented control vs. Menu vs. Picker) die Optionen mit `AskUserQuestion` und ASCII-Preview vorlegen, Empfehlung zuerst.
5. **Zustände** aufzählen: leer, lädt, Teil-/Fehlerzustand, offline, keine Berechtigung, sehr viel Inhalt, sehr lange Texte/Lokalisierung, größte Dynamic-Type-Stufe, Dark Mode, Reduce Motion.
6. **Inhalte & Texte**: Titel, Buttonbeschriftungen (Verben), Leerzustandstext, Fehlermeldungen (hig:writing).
7. **Symbole & Ressourcen**: SF Symbols mit `sf_symbols.py search` auswählen und Mindest-OS gegen Ziel-OS prüfen.

## Spezifikations-Vorlage

```markdown
## <Feature>
Ziel: … · Häufigkeit: … · Plattformen: …

### Struktur
| Plattform | Einstieg | Container | Primäraktion | Rückweg |
|---|---|---|---|---|

### Screens
#### <Screen>
- Layout (ASCII-Skizze)
- Komponenten: … (hig:…)
- Symbole: `…` (iOS ≥ …)
- Zustände: leer / lädt / Fehler / …
- Texte: …
- Barrierefreiheit: VoiceOver-Reihenfolge, Labels, Dynamic-Type-Verhalten (Umbruch statt Abschneiden)

### Offene Fragen
```

Danach anbieten: `build <feature>`.
