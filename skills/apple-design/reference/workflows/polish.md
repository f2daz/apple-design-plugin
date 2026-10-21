# polish – letzter Durchgang vor dem Release

Bewahrt Identität und Verhalten; verbessert Details. Keine Neugestaltung durch die Hintertür.

## Checkliste

**Typografie**
- [ ] Hierarchie über Textstile/Gewichte, max. 2–3 Ebenen pro Screen
- [ ] Größte Dynamic-Type-Stufe: umbrechen statt abschneiden; Layout wechselt ggf. von horizontal zu vertikal (`ViewThatFits`, `dynamicTypeSize.isAccessibilitySize`)
- [ ] Zahlen in Tabellen/Timern mit `.monospacedDigit()`

**Farbe & Material**
- [ ] Tint nur für Interaktives; Status mit Symbol + Farbe, nie nur Farbe
- [ ] Dark Mode und „Kontrast erhöhen“ gesichtet; Reduce Transparency liefert lesbare Flächen
- [ ] Liquid Glass nur auf Funktionsebene; Scroll-Edge-Effekte unter Bars sauber

**Symbole & Bilder**
- [ ] SF Symbols einheitlich in Gewicht/Skala zum Text; Fill-Varianten für ausgewählte Zustände (Tab bar wählt automatisch)
- [ ] Bilder in @2x/@3x bzw. Vektor; App-Icon in allen Varianten (default/dark/clear/tinted)

**Interaktion**
- [ ] Pressed/Disabled/Selected-States überall
- [ ] Haptik an bedeutsamen Momenten (Erfolg, Fehler, Auswahl), nicht bei jedem Tap
- [ ] Animationen kurz, unterbrechbar, mit Reduce-Motion-Alternative
- [ ] Tastatur: Return-Taste-Typ, Autofill-`textContentType`, Fokusreihenfolge; Mac/iPad: Tastenkürzel für Hauptaktionen

**Inhalt & Zustände**
- [ ] Leer-, Lade-, Fehler-, Offline-Zustände formuliert und gestaltet
- [ ] Texte: Verben auf Buttons, keine Schuldzuweisung in Fehlern, Lokalisierung (+30–40 % Länge, RTL) bedacht
- [ ] Berechtigungsdialoge mit ehrlichem Purpose string, im Kontext angefragt

**Plattformdetails**
- [ ] iPad: Pointer-Hover-Effekte, Mehrfenster, Größenänderung; Mac: Menüs vollständig, Fenster-Mindestgröße, Undo/Redo; Watch: Glance in 2 s, Digital Crown, Always-On

## Ablauf

Checkliste gegen Ziel abarbeiten, Fixes gesammelt umsetzen, gerendert prüfen (hell/dunkel/AX), Änderungsliste mit Belegen ausgeben.
