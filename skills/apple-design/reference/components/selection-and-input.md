# Selection and input – Komponenten
> Quelle: Apple HIG, lokaler Spiegel (Stand 2026-10-21). Paraphrasiert. Belege: `(hig:<slug>)`, `(hig:<slug>#Anchor)`.

Steuerelemente, mit denen Nutzer Werte wählen, setzen oder eingeben: Text, Zahlen, Datum, Farbe, Ein/Aus, Auswahl aus Optionen. Für iOS/iPadOS/macOS/watchOS relevant; Digit entry views sind reines tvOS, Combo boxes und Image wells reines macOS.

Inhalt: [Color wells](#color-wells) · [Combo boxes](#combo-boxes) · [Digit entry views](#digit-entry-views) · [Image wells](#image-wells) · [Pickers](#pickers) · [Segmented controls](#segmented-controls) · [Sliders](#sliders) · [Steppers](#steppers) · [Text fields](#text-fields) · [Toggles](#toggles) · [Virtual keyboards](#virtual-keyboards)

### Entscheidungshilfe in dieser Gruppe
- **Auswahl aus 2 bis ca. 5 eng verwandten Optionen, Zustand soll sichtbar sein** → Segmented control (iPhone max. ca. 5, breite UI ca. 5–7) (hig:segmented-controls#Best-practices). Auf watchOS nicht verfügbar.
- **Kurze Liste, Platz sparen** → Pull-down button / Pop-up button statt Picker (hig:pickers#Best-practices); macOS: ab mehr als ca. 5 exklusiven Optionen Pop-up button statt Radio buttons (hig:toggles#Radio-buttons).
- **Mittlere bis lange, logisch geordnete Liste** → Picker (hig:pickers#Best-practices). **Sehr lange Liste** → List/Table (ggf. mit Index) (hig:pickers#Best-practices).
- **Wechsel zwischen völlig getrennten App-Bereichen** → Tab bar, nicht Segmented control (hig:segmented-controls#iOS-iPadOS); macOS-Hauptfensterbereich → Tab view (hig:segmented-controls#macOS).
- **Ein/Aus** → iOS: Switch nur in List-Zeile, sonst Button mit Toggle-Verhalten (hig:toggles#iOS-iPadOS); macOS: Einzelsetting bevorzugt Checkbox, betonte/gruppensteuernde Settings Switch (hig:toggles#Switches, hig:toggles#Radio-buttons).
- **Kontinuierlicher Wert in Bereich** → Slider; **kleine schrittweise Änderung** → Stepper; **exakter Wert** → zusätzlich Text field (hig:sliders#Best-practices, hig:steppers#Best-practices).
- **Freitext + Vorschlagsliste (macOS)** → Combo box (hig:text-fields#macOS).

---

## Color wells
**Zweck:** Feld, das eine Farbe zeigt und per Tap/Klick einen Color picker öffnet, um Farbe von Text, Formen u. Ä. zu ändern. **Plattformen:** ios, ipados, macos (visionos); nicht unterstützt in tvOS, watchOS.
**Verwenden, wenn:** Nutzer Farben von Inhalten/Elementen einstellen. **Nicht verwenden, wenn:** nur eine feste kleine Farbauswahl nötig ist (dann z. B. Segmented control/Menu – Ableitung, nicht HIG).
**Kernregeln:**
- Bevorzuge den System-Color-Picker: vertraut, plattformübergreifend konsistent, gespeicherte Farbsets sind app-übergreifend verfügbar (hig:color-wells#Best-practices).
- Eigene Picker-UI ist erlaubt, sollte aber Mehrwert bieten (hig:color-wells).
- Aktualisiere den Well sofort auf die gewählte Farbe (hig:color-wells#macOS).
**Plattform-Besonderheiten:**
- macOS: Well wird beim Klick hervorgehoben, öffnet Picker, zeigt danach neue Farbe; Drag & Drop zwischen Wells und vom Picker in den Well (hig:color-wells#macOS).
- iOS/iPadOS/visionOS: keine Zusatzhinweise.
**Kennwerte:** keine im Spiegel.
**Umsetzung:** SwiftUI `ColorPicker` (nicht auf der Seite gelistet, aber Standard-API); UIKit `UIColorWell`, `UIColorPickerViewController`; AppKit `NSColorWell`.
**Typische Fehler:** Eigenen Farbwähler ohne Not bauen; fehlendes Drag & Drop auf macOS; Well zeigt nach Auswahl alte Farbe.

## Combo boxes
**Zweck:** Kombination aus Text field und Pull-down button – freie Eingabe oder Auswahl aus vordefinierten Werten. **Plattformen:** nur macos.
**Verwenden, wenn:** Nutzer meist aus wahrscheinlichen Werten wählen, aber auch eigene Werte eingeben dürfen. **Nicht verwenden, wenn:** nur vordefinierte Werte zulässig sind (dann Pop-up button – Ableitung).
**Kernregeln:**
- Belege das Feld mit sinnvollem Default aus der Liste; er muss nicht der erste Eintrag sein (hig:combo-boxes#Best-practices).
- Stelle ein einleitendes Label voran (Title-Style-Capitalization, endet mit Doppelpunkt) (hig:combo-boxes#Best-practices).
- Biete relevante, wahrscheinliche Auswahlwerte an (hig:combo-boxes#Best-practices).
- Halte Listeneinträge nicht breiter als das Textfeld, sonst Abschneiden (hig:combo-boxes#Best-practices).
- Beachte: Eigene Eingaben werden nicht automatisch in die Liste aufgenommen (hig:combo-boxes).
**Plattform-Besonderheiten:** Nicht unterstützt in iOS, iPadOS, tvOS, visionOS, watchOS (hig:combo-boxes#Platform-considerations).
**Kennwerte:** keine im Spiegel.
**Umsetzung:** AppKit `NSComboBox`. SwiftUI-Äquivalent im Spiegel nicht genannt.
**Typische Fehler:** Leeres Feld ohne Default; zu breite Listeneinträge; fehlendes Label.

## Digit entry views
**Zweck:** Vollbild-Ansicht zur Eingabe einer Ziffernfolge (z. B. PIN) über ein Ziffern-Keyboard. **Plattformen:** nur tvos; nicht unterstützt in iOS, iPadOS, macOS, visionOS, watchOS.
**Verwenden, wenn:** auf Apple TV PIN/Code abgefragt wird. **Nicht verwenden, wenn:** andere Plattform (dort Text field mit passendem Keyboard-Typ).
**Kernregeln:**
- Nutze sichere Ziffernfelder (Sternchen) bei sensiblen Daten (hig:digit-entry-views#Best-practices).
- Erkläre mit Titel und Prompt, wozu die Ziffern eingegeben werden (hig:digit-entry-views#Best-practices).
**Plattform-Besonderheiten:** tvOS blendet beim Aktivieren eine Ziffern-Tastatur ein (hig:virtual-keyboards#tvOS).
**Kennwerte:** keine im Spiegel.
**Umsetzung:** TVUIKit `TVDigitEntryViewController`.
**Typische Fehler:** PIN im Klartext anzeigen; kein Kontext, wofür der Code dient.

## Image wells
**Zweck:** Editierbare Variante eines Image view: Bild per Copy/Paste, Löschen oder Drag & Drop setzen. **Plattformen:** nur macos.
**Verwenden, wenn:** Nutzer ein Bild zuweisen/ersetzen (z. B. Avatar, Dokumentbild). **Nicht verwenden, wenn:** Bild nur angezeigt wird (dann Image view) (hig:image-wells).
**Kernregeln:**
- Zeige wieder das Default-Bild, wenn der Inhalt eines Pflicht-Wells gelöscht wird (hig:image-wells#Best-practices).
- Stelle bei Copy/Paste-Unterstützung die Standard-Menüpunkte und Shortcuts im Edit-Menü bereit (hig:image-wells#Best-practices, hig:the-menu-bar#Edit-menu).
- Erlaube Drag-in ohne vorherige Auswahl (hig:image-wells).
**Plattform-Besonderheiten:** Nicht unterstützt in iOS, iPadOS, tvOS, visionOS, watchOS.
**Kennwerte:** keine im Spiegel.
**Umsetzung:** AppKit `NSImageView` (editierbar).
**Typische Fehler:** Leerer Well bei Pflichtbild; Copy/Paste nur per Kontextmenü statt über Edit-Menü/Shortcuts.

## Pickers
**Zweck:** Eine oder mehrere scrollbare Listen eindeutiger Werte zur Auswahl (inkl. Date picker). **Plattformen:** ios, ipados, macos, watchos (tvos nur via SwiftUI, visionos).
**Verwenden, wenn:** mittellange bis lange, vorhersehbar geordnete Wertelisten oder Datum/Uhrzeit gewählt werden. **Nicht verwenden, wenn:** nur wenige Optionen (→ Pull-down button) oder sehr viele Einträge (→ List/Table mit Index) (hig:pickers#Best-practices).
**Kernregeln:**
- Setze Picker für mittlere bis lange Listen ein; für kurze Listen Pull-down button, für sehr große List/Table (hig:pickers#Best-practices).
- Ordne Werte logisch und vorhersehbar (z. B. alphabetisch), da viele Werte verborgen sind (hig:pickers#Best-practices).
- Zeige den Picker im Kontext (unter/nahe dem Feld, unten im Fenster oder im Popover), nicht in einer eigenen View (hig:pickers#Best-practices).
- Reduziere die Minuten-Granularität, wenn sinnvoll; Intervall muss 60 glatt teilen (hig:pickers#Best-practices).
- Nutze auf iOS den Compact-Stil bei Platzmangel (hig:pickers#iOS-iPadOS).
- Rechne mit lokalisierungsabhängigen Werten und Reihenfolgen (hig:pickers).
**Plattform-Besonderheiten:**
- iOS/iPadOS: Date-picker-Stile Compact (Button öffnet modale Ansicht, Wert in Accent color), Inline, Wheels (auch Tastatureingabe), Automatic; Modi Date, Time, Date and time, Countdown timer (Countdown nicht in Inline/Compact) (hig:pickers#iOS-iPadOS).
- macOS: Date picker textual (wenig Platz, gezielte Eingabe) oder graphical (Kalender durchblättern, Bereich wählen, Uhr-Optik) (hig:pickers#macOS).
- watchOS: Navigation per Digital Crown; Wheels-Stil für Listen und Datum/Zeit; optional Outline, Caption, Scroll-Indikator; lange Listen per `navigationLink`-Stil als Button, Crown-Scrubbing ohne Tap möglich (hig:pickers#watchOS).
- tvOS: nur mit SwiftUI verfügbar (hig:pickers#tvOS).
**Kennwerte:** Minutenliste standardmäßig 60 Werte (0–59); Beispiel Viertelstunden 0/15/30/45; Countdown max. 23 h 59 min (hig:pickers#Best-practices, hig:pickers#iOS-iPadOS).
**Umsetzung:** SwiftUI `Picker`, `DatePicker` (Stile u. a. `.wheel`, `.navigationLink`, `.segmented`, `.menu`); UIKit `UIPickerView`, `UIDatePicker`; AppKit `NSDatePicker` (für Listen auf macOS: `NSPopUpButton` – siehe Pop-up buttons).
**Typische Fehler:** Wheel-Picker für 3 Optionen; unsortierte Werte; Picker in separatem Screen statt im Kontext; Minutenintervall, das 60 nicht teilt.

## Segmented controls
**Zweck:** Lineare Gruppe aus zwei oder mehr Segmenten, die je als Button wirken – Einfachauswahl (macOS auch Mehrfachauswahl) oder momentane Aktionen. **Plattformen:** ios, ipados, macos (tvos, visionos); nicht unterstützt in watchOS.
**Verwenden, wenn:** wenige, eng verwandte Optionen ein Objekt, einen Zustand oder eine View beeinflussen und Gruppierung/Auswahlzustand sichtbar sein soll (hig:segmented-controls#Best-practices). **Nicht verwenden, wenn:** völlig getrennte App-Bereiche gewechselt werden (→ Tab bar) (hig:segmented-controls#iOS-iPadOS), auf macOS View-Wechsel im Hauptfensterbereich (→ Tab view) (hig:segmented-controls#macOS), viele Optionen (→ Picker/Menu).
**Kernregeln:**
- Begrenze die Segmentzahl: max. ca. 5–7 in breiter UI, max. ca. 5 auf iPhone (hig:segmented-controls#Best-practices).
- Mische nicht Aktions- und Auswahlsegmente in einem Control (hig:segmented-controls#Best-practices).
- Halte Segmentbreiten (und Icon-/Titelbreiten) möglichst gleich (hig:segmented-controls#Best-practices).
- Verwende entweder Text oder Bilder, nicht beides gemischt (hig:segmented-controls#Content).
- Nutze Nomen/Nominalphrasen in Title-Style-Capitalization; mit Textlabels kein einleitender Text nötig (hig:segmented-controls#Content).
- Fülle Segmente mit ähnlich großem Inhalt (hig:segmented-controls#Content).
**Plattform-Besonderheiten:**
- iOS/iPadOS: geeignet zum Umschalten zwischen eng verwandten Subviews (Beispiel Kalender: Event vs. Reminder) (hig:segmented-controls#iOS-iPadOS).
- macOS: ggf. einleitender Text; bei Symbolen Labels unter Segmenten und Tooltip je Segment; für View-Wechsel in Toolbar/Inspector okay, im Hauptbereich Tab view; Spring loading unterstützen (hig:segmented-controls#macOS).
- tvOS: Segment wird schon bei Fokus ausgewählt → keine anderen fokussierbaren Elemente nahebei; für Filter eher Split view (hig:segmented-controls#tvOS).
- visionOS: Icon-Segmente zeigen beim Anschauen Tooltip mit hinterlegtem Text (hig:segmented-controls#visionOS).
**Kennwerte:** ca. 5–7 Segmente (breit), ca. 5 (iPhone) (hig:segmented-controls#Best-practices).
**Umsetzung:** SwiftUI `Picker` mit `.pickerStyle(.segmented)`; UIKit `UISegmentedControl` (`isMomentary` für Aktionen); AppKit `NSSegmentedControl` (`SwitchTracking.momentary`, Mehrfachauswahl).
**Typische Fehler:** Segmented control als Tab-bar-Ersatz für App-Navigation; 7+ Segmente auf iPhone; Icons und Text gemischt; Aktion + Auswahl in einem Control.

## Sliders
**Zweck:** Horizontale Spur mit Thumb zum Einstellen eines Werts zwischen Minimum und Maximum. **Plattformen:** ios, ipados, macos, watchos (visionos); nicht unterstützt in tvOS.
**Verwenden, wenn:** ein Wert stufenlos oder in Schritten innerhalb eines festen Bereichs gesetzt wird, idealerweise mit Live-Feedback. **Nicht verwenden, wenn:** Audio-Lautstärke auf iOS (→ Volume view) (hig:sliders#iOS-iPadOS); exakter Wert entscheidend (dann zusätzlich Text field).
**Kernregeln:**
- Minimum leading, Maximum trailing (horizontal); Minimum unten, Maximum oben (vertikal) (hig:sliders#Best-practices).
- Passe Aussehen (Track-Farbe, Thumb, Min/Max-Icons) nur an, wenn es Bedeutung vermittelt (hig:sliders#Best-practices).
- Ergänze bei großen Bereichen Text field und Stepper für exakte bzw. ganzzahlige Werte (hig:sliders#Best-practices).
- Gib Live-Feedback während der Änderung (macOS) (hig:sliders#macOS).
- Nutze linearen Slider für feste Bereiche, zirkulären für sich wiederholende Werte (z. B. Rotation) (hig:sliders#macOS).
- Setze Tick marks für Genauigkeit; beschrifte meist nur Min/Max, bei nichtlinearen Werten periodisch (hig:sliders#macOS).
**Plattform-Besonderheiten:**
- iOS/iPadOS: kein Slider für Lautstärke – Volume view verwenden (hig:sliders#iOS-iPadOS).
- macOS: Tick marks, linear (Lozenge-Thumb) und circular; Label mit Sentence-Style + Doppelpunkt; Tooltip mit aktuellem Wert (hig:sliders#macOS).
- visionOS: horizontale Slider bevorzugen (hig:sliders#visionOS).
- watchOS: diskrete Schritte oder durchgehender Balken, Seitenbuttons ändern um festen Betrag; Default-Glyphen Plus/Minus, ggf. eigene (hig:sliders#watchOS).
**Kennwerte:** keine verbindlichen; Beispielwerte im Spiegel (0–100 %, 0–360°, 1440°) sind nur Illustrationen (hig:sliders#macOS).
**Umsetzung:** SwiftUI `Slider`; UIKit `UISlider`; AppKit `NSSlider`.
**Typische Fehler:** Umgekehrte Richtung; Lautstärkeregler als `UISlider`; großer Wertebereich ohne Möglichkeit exakter Eingabe; vertikale Slider in visionOS.

## Steppers
**Zweck:** Zweiteiliges Control zum Erhöhen/Verringern eines inkrementellen Werts; zeigt selbst keinen Wert an. **Plattformen:** ios, ipados, macos (visionos); nicht unterstützt in watchOS, tvOS.
**Verwenden, wenn:** kleine Änderungen mit wenigen Taps/Klicks (z. B. Anzahl). **Nicht verwenden, wenn:** große Wertsprünge üblich sind ohne begleitendes Eingabefeld.
**Kernregeln:**
- Mache klar, welchen Wert der Stepper ändert (Wertanzeige daneben) (hig:steppers#Best-practices).
- Kombiniere mit Text field, wenn stark variierende Werte zu erwarten sind (hig:steppers#Best-practices).
- Unterstütze auf macOS bei großen Bereichen Shift-Klick für größere Schritte (hig:steppers#macOS).
**Plattform-Besonderheiten:** macOS: Shift-Klick z. B. 10-faches Inkrement (Beispiel, keine Vorgabe) (hig:steppers#macOS).
**Kennwerte:** keine verbindlichen (Faktor 10 nur als Beispiel).
**Umsetzung:** SwiftUI `Stepper`; UIKit `UIStepper`; AppKit `NSStepper`.
**Typische Fehler:** Stepper ohne sichtbaren Wert; Stepper für Werte mit großer Spannweite ohne Eingabefeld.

## Text fields
**Zweck:** Rechteckiger Bereich zur Eingabe/Bearbeitung kleiner, konkreter Textstücke (Name, E-Mail). **Plattformen:** ios, ipados, macos, watchos (tvos, visionos).
**Verwenden, wenn:** kurze Eingaben. **Nicht verwenden, wenn:** längere Texte (→ Text view) (hig:text-fields#Best-practices); auf watchOS/tvOS, wenn eine Optionsliste oder Buttons genügen (hig:text-fields#watchOS).
**Kernregeln:**
- Zeige Placeholder als Hinweis, ergänze bei Bedarf ein separates Label (Placeholder verschwindet beim Tippen) (hig:text-fields#Best-practices).
- Verwende Secure fields für Passwörter/sensible Daten (hig:text-fields#Best-practices).
- Dimensioniere das Feld passend zur erwarteten Textmenge; mehrere Felder vertikal, gleichmäßig beabstandet, konsistente Breiten (hig:text-fields#Best-practices).
- Sorge für logische Tab-Reihenfolge (hig:text-fields#Best-practices).
- Validiere kontextabhängig: E-Mail beim Feldwechsel, Benutzername/Passwort vor dem Feldwechsel (hig:text-fields#Best-practices).
- Nutze Number formatter für Zahlen, ohne feste Darstellung anzunehmen (Locale) (hig:text-fields#Best-practices).
- Wähle Umbruch-/Kürzungsverhalten bewusst; Expansion tooltip für gekürzten Text (hig:text-fields#Best-practices).
- Zeige den passenden Keyboard-Typ (iOS, iPadOS, tvOS, visionOS) (hig:text-fields#Best-practices).
- Minimiere Texteingabe auf tvOS/watchOS (hig:text-fields#Best-practices).
**Plattform-Besonderheiten:**
- iOS/iPadOS: Clear button am trailing Ende; leading Bild für Zweck, trailing für Zusatzfunktion (z. B. Bookmarks) (hig:text-fields#iOS-iPadOS).
- macOS: Für Text + Auswahlliste Combo box (hig:text-fields#macOS).
- watchOS: Text field nur wenn nötig; Liste von Optionen bevorzugen (hig:text-fields#watchOS).
**Kennwerte:** keine im Spiegel.
**Umsetzung:** SwiftUI `TextField`, `SecureField`; UIKit `UITextField`; AppKit `NSTextField` (Secure: `NSSecureTextField` – nicht auf der Seite gelistet).
**Typische Fehler:** Nur Placeholder als Label; Passwort im Klartextfeld; Standard-Keyboard für Zahlen/E-Mail; Validierung erst beim Absenden; feste Zahlenformate statt Locale.

## Toggles
**Zweck:** Wahl zwischen zwei gegensätzlichen Zuständen (an/aus) mit unterschiedlicher Darstellung je Zustand; Stile Switch, Checkbox, (macOS) Radio buttons, Button mit Toggle-Verhalten. **Plattformen:** ios, ipados, macos, watchos (tvos, visionos).
**Verwenden, wenn:** Zustand von Inhalt/View an- oder ausgeschaltet wird. **Nicht verwenden, wenn:** andere Aktionen, z. B. Auswahl aus Liste (→ Pop-up button) (hig:toggles#Best-practices).
**Kernregeln:**
- Nutze Toggles nur für zwei gegensätzliche Werte (hig:toggles#Best-practices).
- Mache klar, was der Toggle steuert (Kontext oder, v. a. macOS, Label) (hig:toggles#Best-practices).
- Kennzeichne Zustände nicht nur über Farbe (Füllung, Form, Häkchen/Punkt) (hig:toggles#Best-practices).
- iOS: Switch nur in List-Zeilen, ohne extra Label; außerhalb von Listen Button mit Toggle-Verhalten (hig:toggles#iOS-iPadOS).
- iOS: Switch-Farbe (Default grün) nur bei Bedarf ändern, z. B. Accent color mit ausreichendem Kontrast (hig:toggles#iOS-iPadOS).
- macOS: Switches, Checkboxes, Radio buttons im Fensterinhalt, nicht in Toolbar/Statusleiste (hig:toggles#macOS).
- macOS: Switch für betonte/gruppensteuernde Settings; im Grouped Form Mini-Switch pro Zeile; bestehende Checkbox nicht durch Switch ersetzen (hig:toggles#Switches).
- macOS: Checkbox für Hierarchien (Einrückung) und Einzel-An/Aus; Mixed-State zeigen, wenn Unteroptionen uneinheitlich (hig:toggles#Checkboxes).
- macOS: Radio buttons für sich ausschließende Optionen (typ. 2–5); bei mehr als ca. 5 Pop-up button; horizontale Abstände nach längstem Label (hig:toggles#Radio-buttons).
**Plattform-Besonderheiten:**
- iOS/iPadOS: Switch nur in Listen; Toggle-Buttons ohne erklärendes Label, Icon + Hintergrundwechsel (hig:toggles#iOS-iPadOS).
- macOS: drei Varianten Switch/Checkbox/Radio; Checkbox meist mit trailing Titel, in editierbarer Checkliste auch ohne (hig:toggles#Checkboxes); Mixed-State bei Radio buttons selten sinnvoll → Checkbox (hig:toggles#Radio-buttons).
- tvOS, visionOS, watchOS: keine Zusatzhinweise.
**Kennwerte:** Radio-Gruppen typ. 2–5; mehr als ca. 5 → Pop-up button (hig:toggles#Radio-buttons).
**Umsetzung:** SwiftUI `Toggle` mit `ToggleStyle` (`.switch`, `.checkbox` macOS, `.button`), `controlSize(.mini)`, `GroupedFormStyle`; Radio auf macOS via `Picker` mit `.radioGroup` (nicht auf der Seite genannt); UIKit `UISwitch`, `UIButton.changesSelectionAsPrimaryAction`; AppKit `NSSwitch`, `NSButton` (`.toggle`, `allowsMixedState`).
**Typische Fehler:** Switch frei im iOS-Layout außerhalb einer Liste; Zustand nur per Farbe; Checkbox-Hierarchie als Switches; Radio-Liste mit 8 Optionen; Toggle in macOS-Toolbar.

## Virtual keyboards
**Zweck:** Systemseitige Bildschirmtastaturen mit aufgabenspezifischen Tasten für Geräte ohne physische Tastatur; keine Keyboard-Shortcuts. **Plattformen:** ios, ipados, watchos (tvos, visionos); nicht unterstützt in macOS.
**Verwenden, wenn:** Texteingabe auf Touch-/Remote-Geräten – Typ immer zum Inhalt passend wählen. **Nicht verwenden, wenn:** Custom input view ohne erkennbaren Mehrwert; Custom keyboard (Extension) nur für systemweite Funktionen, für App-interne Eingabe Custom input view (hig:virtual-keyboards#Custom-keyboards).
**Kernregeln:**
- Wähle den Keyboard-Typ passend zum Inhalt und setze semantischen Content type (verbessert Vorschläge/Korrektur) (hig:virtual-keyboards#Best-practices).
- Passe den Return-Key-Typ an, wenn es den Ablauf klärt (z. B. Search) (hig:virtual-keyboards#Best-practices).
- Custom input view nur, wenn der Nutzen im App-Kontext klar ist; Standard-Tastenklick abspielen (hig:virtual-keyboards#Custom-input-views).
- Custom keyboard: klarer Weg zum Tastaturwechsel (Globe-Key-Verhalten), keine Duplikate von Emoji/Globe/Dictation, Tutorial in der App statt in der Tastatur (hig:virtual-keyboards#Custom-keyboards).
- iOS: Keyboard layout guide nutzen, damit wichtige UI sichtbar bleibt (hig:virtual-keyboards#iOS-iPadOS).
- iOS: Controls über der Tastatur nur aufgabenrelevant; Liquid Glass für deren Container, Standard-Toolbar übernimmt es automatisch; Standard-Padding (hig:virtual-keyboards#iOS-iPadOS).
**Keyboard-Typen** (`UIKeyboardType`): ASCII capable, ASCII capable number pad, Decimal pad, Default, Email address, Name phone pad, Number pad, Numbers and punctuation, Phone pad, Twitter, URL, Web search (hig:virtual-keyboards#Best-practices).
**Plattform-Besonderheiten:**
- iOS/iPadOS: Keyboard layout guide, Input accessory view (hig:virtual-keyboards#iOS-iPadOS).
- watchOS: Tastatur nur bei ausreichend großem Display, sonst Diktat/Scribble; Keyboard-Typ nicht änderbar, wohl aber Content type; Eingabe auch über gekoppeltes iPhone (hig:virtual-keyboards#watchOS).
- tvOS: lineare Tastatur mit Siri Remote, Grid-Tastatur bei anderen Geräten; Digit entry view mit Ziffern-Tastatur (hig:virtual-keyboards#tvOS).
- visionOS: Tastatur in eigenem, verschiebbarem Fenster; Layout muss sie nicht berücksichtigen (hig:virtual-keyboards#visionOS).
- Custom keyboards (Extension) in iOS, iPadOS, tvOS; nicht in Secure- und Telefonnummernfeldern nutzbar (hig:virtual-keyboards#Custom-keyboards).
**Kennwerte:** keine im Spiegel.
**Umsetzung:** SwiftUI `keyboardType(_:)`, `textContentType(_:)`, `submitLabel(_:)`, `ToolbarItemPlacement` (`.keyboard`); UIKit `UIKeyboardType`, `UITextContentType`, `UIReturnKeyType`, `inputViewController`, `inputAccessoryView`, `UIKeyboardLayoutGuide`, `UIDevice.playInputClick()`.
**Typische Fehler:** Default-Keyboard für E-Mail/Zahlen/URL; fehlender `textContentType` (kein AutoFill); Tastatur verdeckt Eingabefeld/Buttons; Custom keyboard ohne Wechselmöglichkeit; Accessory-Leiste mit irrelevanten Aktionen.
