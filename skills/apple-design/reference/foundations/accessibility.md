# Accessibility

Quellen (HIG-Spiegel, Stand 2026-10-21): `accessibility` (Update 2025-06-09: Assistive Access, Switch Control, Accessibility Nutrition Labels), `voiceover` (2025-03-07), `inclusion`, `typography` (Dynamic Type), `color`, `dark-mode`, `materials`, `motion`, `buttons`, `right-to-left`.

## Einordnung

Apple beschreibt eine zugängliche Oberfläche als **intuitiv** (vertraute, konsistente Interaktionen), **wahrnehmbar** (Information nie nur über einen Kanal) und **anpassbar** (System-Accessibility-Features und persönliche Einstellungen werden respektiert) (hig:accessibility). Die HIG gliedert nach Vision, Hearing, Mobility, Speech, Cognitive. Behinderung ist ein Spektrum und kann permanent, temporär oder situativ sein (hig:inclusion#Accessibility).

Prüfwerkzeug: **Accessibility Inspector** (Xcode). Ergebnis lässt sich im App Store über **Accessibility Nutrition Labels** (App Store Connect) ausweisen (hig:accessibility).

## Kernregeln

### Sehen
- Unterstütze größere Textgrößen: Ziel mindestens **200 %** Vergrößerung (watchOS **140 %**), über Dynamic Type oder eigene UI (hig:accessibility#Vision).
- Halte die plattformspezifischen Default- und Mindestschriftgrößen ein, auch bei Custom Fonts; bei dünnen Schnitten größer wählen (hig:accessibility#Vision, hig:typography#Ensuring-legibility).
- Vermeide Ultralight, Thin, Light – besonders bei kleinem Text (hig:typography#Ensuring-legibility).
- Erfülle Mindestkontraste (Tabelle unten) in Light **und** Dark; falls der Default nicht reicht, liefere zumindest bei **Increase Contrast** ein kontrastreicheres Schema (hig:accessibility#Vision).
- Bevorzuge Systemfarben – sie bringen Varianten für Dark Mode und Increase Contrast mit; eigene Farben brauchen Light, Dark und je eine Increased-Contrast-Variante (hig:color#Best-practices).
- Vermittle Information nie nur über Farbe; ergänze Form, Symbol, Text (problematisch: Rot-Grün, Blau-Orange). Biete ggf. anpassbare Farbschemata (Charts, Spielfiguren) (hig:accessibility#Vision, hig:color#Inclusive-color).
- Beschreibe UI und Inhalte für VoiceOver (hig:voiceover).
- Teste Dark Mode mit Increase Contrast und Reduce Transparency – einzeln und kombiniert (hig:dark-mode#Best-practices).
- Prüfe Liquid Glass (regular/clear) mit Reduce Transparency und Increase Contrast; das Erscheinungsbild ändert sich mit diesen Einstellungen (hig:materials).
- Lass interface-relevante Icons mit der Schriftgröße mitwachsen (SF Symbols skalieren automatisch) (hig:typography#Supporting-Dynamic-Type).
- Custom Fonts müssen Dynamic Type und **Bold Text** selbst unterstützen; Systemschriften tun das automatisch (hig:typography#Using-custom-fonts).

### VoiceOver
- Vergib Labels für alle wesentlichen Elemente; Standard-Labels von System-Controls durch funktionsbeschreibende ersetzen, Custom Elements immer beschriften, Labels aktuell halten (hig:voiceover#Descriptions).
- Beschreibe bedeutungstragende Bilder – nur das, was das Bild selbst vermittelt, nicht die benachbarte Bildunterschrift (hig:voiceover#Descriptions).
- Mache Charts/Infografiken vollständig zugänglich: knappe Gesamtbeschreibung, interaktive Details auch per VoiceOver erreichbar (hig:voiceover#Descriptions).
- Blende rein dekorative Bilder aus (hig:voiceover#Descriptions).
- Vergib eindeutige Bildschirmtitel und korrekte Überschriften (hig:voiceover#Navigation).
- Gruppiere zusammengehörige Elemente (Bild + Bildunterschrift) und lege Reihenfolge/Beziehungen fest, wo sie nur visuell erkennbar sind (hig:voiceover#Navigation).
- Melde sichtbare Inhalts- und Layoutänderungen an VoiceOver (hig:voiceover#Navigation).
- Unterstütze den Rotor (Überschriften, Links, eigene Inhaltstypen) (hig:voiceover#Navigation).

### Hören
- Transportiere Dialog und wichtige Information nie nur per Audio; biete Captions, Subtitles, Audio Descriptions, Transcripts je nach Medium (hig:accessibility#Hearing).
- Kombiniere Audio-Cues mit Haptics; in iOS/iPadOS zusätzlich Music Haptics und Audio Graphs möglich (hig:accessibility#Hearing).
- Ergänze Audio-Hinweise durch visuelle Hinweise, besonders bei Inhalten außerhalb des Bildschirms (Spiele, Spatial) (hig:accessibility#Hearing).

### Motorik
- Halte Control-Mindestgrößen ein (Tabelle unten); Buttons brauchen ein Hit-Target von mindestens 44x44 pt, in visionOS 60x60 pt (hig:accessibility#Mobility, hig:buttons#Best-practices).
- Abstand ist so wichtig wie Größe: ca. **12 pt** Padding um Elemente mit Bezel, ca. **24 pt** um Elemente ohne Bezel (hig:accessibility#Mobility).
- Nutze für häufige Interaktionen die einfachste Geste; keine eigenen Mehrfinger-/Mehrhand-Gesten (hig:accessibility#Mobility).
- Biete für jede Geste eine Alternative auf dem Bildschirm (z. B. Button zusätzlich zu Swipe-to-dismiss) (hig:accessibility#Mobility).
- Beschrifte Elemente so, dass **Voice Control** sie per Sprache ansprechen kann (hig:accessibility#Mobility).
- Integriere Siri und Shortcuts für wiederkehrende Aufgaben (auch Action Button) (hig:accessibility#Mobility).
- Teste mit VoiceOver, AssistiveTouch, Full Keyboard Access, Pointer Control, Switch Control (hig:accessibility#Mobility).

### Sprache / Eingabe
- Ermögliche vollständige Bedienung per Tastatur (**Full Keyboard Access**); systemweite Tastaturkurzbefehle nicht überschreiben (hig:accessibility#Speech).
- Unterstütze **Switch Control** (externe Schalter, Controller, Geräusche) für Auswählen, Tippen, Tippen von Text, Zeichnen (hig:accessibility#Speech).

### Kognition
- Halte Aktionen einfach und konsistent; Systemgesten vor eigenen (hig:accessibility#Cognitive).
- Vermeide zeitgesteuert verschwindende UI; schließen per expliziter Aktion (hig:accessibility#Cognitive).
- Kein Autoplay von Audio/Video ohne Start-/Stopp-Steuerung; globale Opt-out-Einstellung erwägen (hig:accessibility#Cognitive).
- Reagiere auf **Dim Flashing Lights** bei Videowiedergabe (hig:accessibility#Cognitive).
- Reagiere auf **Reduce Motion**: automatische und wiederholte Animationen (Zoom, Skalierung, periphere Bewegung) reduzieren (hig:accessibility#Cognitive) – Details in `motion-and-feedback.md`.
- Optimiere für **Assistive Access** (iOS/iPadOS): Kernfunktionen identifizieren, Nebenpfade entfernen, Mehrschritt-Flows auf einen Schritt pro Screen aufteilen, schwer umkehrbare Aktionen doppelt bestätigen lassen (hig:accessibility#Cognitive).
- Biete in Spielen Schwierigkeits-Anpassungen (Kriterien, Reaktionszeit, Steuerhilfen) (hig:accessibility#Cognitive).

### Inklusion
- Keine Bilder/Sprache, die Menschen mit Behinderung ausschließen oder Behinderung als negative Metapher nutzen; People-first schreiben (hig:inclusion#Accessibility).
- Gehe nicht davon aus, dass eine Behinderung jemanden von der Nutzung abhält (hig:inclusion#Accessibility).

## Kennwerte

### Schriftgrößen Default / Minimum (hig:accessibility#Vision, hig:typography#Ensuring-legibility)

| Plattform | Default | Minimum |
|---|---|---|
| iOS, iPadOS | 17 pt | 11 pt |
| macOS | 13 pt | 10 pt |
| tvOS | 29 pt | 23 pt |
| visionOS | 17 pt | 12 pt |
| watchOS | 16 pt | 12 pt |

### Kontrast (Accessibility Inspector, WCAG Level AA) (hig:accessibility#Vision)

| Textgröße | Gewicht | Mindestkontrast |
|---|---|---|
| bis 17 pt | alle | 4.5:1 |
| ab 18 pt | alle | 3:1 |
| alle | Bold | 3:1 |

Zusatz aus `dark-mode#Dark-Mode-colors`: mindestens 4.5:1; bei eigenen Vorder-/Hintergrundfarben **7:1 anstreben**, besonders bei kleinem Text. Als Messmethoden nennt Apple WCAG und APCA.

### Control-Größen (hig:accessibility#Mobility)

| Plattform | Default | Minimum |
|---|---|---|
| iOS, iPadOS | 44x44 pt | 28x28 pt |
| macOS | 28x28 pt | 20x20 pt |
| tvOS | 66x66 pt | 56x56 pt |
| visionOS | 60x60 pt | 28x28 pt |
| watchOS | 44x44 pt | 28x28 pt |

Abstand: ~12 pt um Elemente mit Bezel, ~24 pt um bezellose Elemente (gemessen ab sichtbarer Kante).

### Dynamic Type – Body-Stil als Referenz (hig:typography#Specifications)

| Größe | iOS/iPadOS Body (pt / Leading) | watchOS Body (pt / Leading) |
|---|---|---|
| xSmall | 14 / 19 | 14 / 16.5 |
| Small | 15 / 20 | 15 / 17.5 (Default 38 mm) |
| Medium | 16 / 21 | – |
| Large | **17 / 22 (Default)** | 16 / 18.5 (Default 40/41/42 mm) |
| xLarge | 19 / 24 | 17 / 19.5 (Default 44/45/49 mm) |
| xxLarge | 21 / 26 | 18 / 20.5 |
| xxxLarge | 23 / 29 | 19 / 21.5 |
| AX1 | 28 / 34 | 21 / 23.5 |
| AX2 | 33 / 40 | 22 / 24.5 |
| AX3 | 40 / 48 | 23 / 25.5 |
| AX4 | 47 / 56 | – |
| AX5 | 53 / 62 | – |

Vollständige Stil-Tabellen: `typography`-Referenz. Dynamic Type gibt es in iOS, iPadOS, tvOS, visionOS, watchOS – **nicht in macOS** (hig:typography#macOS).

### System-Einstellungen, auf die eine App reagieren muss

| Einstellung | Erwartete Reaktion | Beleg |
|---|---|---|
| Larger Text / Dynamic Type inkl. AX-Größen | Layout skaliert, minimal kürzen, ggf. gestapeltes Layout, weniger Spalten | hig:typography#Supporting-Dynamic-Type |
| Bold Text | Custom Fonts liefern fetteren Schnitt | hig:typography#Using-custom-fonts |
| Increase Contrast | Eigene Farben mit Increased-Contrast-Varianten; Systemfarben passen sich an | hig:color#Best-practices |
| Reduce Transparency | Materialien/Liquid Glass werden opaker; Lesbarkeit prüfen | hig:materials, hig:dark-mode#Best-practices |
| Reduce Motion | Bewegung reduzieren, Fades statt Bewegung | hig:accessibility#Cognitive |
| Dim Flashing Lights | Video-Wiedergabe reagiert | hig:accessibility#Cognitive |
| Dark Mode | Beide Appearances lesbar, Kontrast in beiden prüfen | hig:dark-mode |
| VoiceOver | Labels, Reihenfolge, Gruppen, Notifications, Rotor | hig:voiceover |
| Voice Control | Sichtbare, eindeutige Beschriftungen | hig:accessibility#Mobility |
| Switch Control, Full Keyboard Access, AssistiveTouch, Pointer Control | Alle Funktionen ohne Touch-Gesten erreichbar | hig:accessibility#Mobility, #Speech |
| Assistive Access | Reduzierte, einschrittige Oberfläche | hig:accessibility#Cognitive |

Nicht im Spiegel ausgeführt, aber im System vorhanden: Button Shapes, Smart Invert, Differentiate Without Color, On/Off Labels – die HIG-Seiten geben dazu keine eigenen Regeln; in der Praxis über die unten genannten APIs abfragen und Farbe-allein vermeiden.

## Plattform-Unterschiede

| Thema | iOS / iPadOS | macOS | watchOS |
|---|---|---|---|
| Dynamic Type | ja, 7 Standard- + 5 AX-Größen | **nein** – eigene Skalierung oder Systemschriftgrößen/-Varianten (`NSFont`-Dynamic-Variants) | ja, 6 Standard- + 3 AX-Größen; Default abhängig von Gehäusegröße |
| Vergrößerungsziel | 200 % | 200 % (über eigene UI) | 140 % |
| Default/Min Text | 17 / 11 pt | 13 / 10 pt | 16 / 12 pt |
| Control Default/Min | 44 / 28 pt | 28 / 20 pt | 44 / 28 pt |
| Dark Mode | ja (Base/Elevated-Hintergründe) | ja (Desktop Tinting) | kein Dark Mode (immer dunkel) |
| Eingabe-Alternativen | Voice Control, Switch Control, AssistiveTouch, Full Keyboard Access | Full Keyboard Access, Voice Control, Switch Control, Pointer Control | VoiceOver, Siri/Shortcuts, Action Button, Digital Crown |
| Assistive Access | ja | – | – |
| Besonderheit | Music Haptics, Audio Graphs | Tastatur-Navigation zentral, Systemkürzel nicht überschreiben | Kurze Interaktionen, keine zeitkritischen UIs |

visionOS (zur Vollständigkeit): Pointer Control (Kopf/Hand), Zoom; Komfort priorisieren (Inhalte im Blickfeld, horizontale statt vertikale Layouts, keine kopfverankerten Inhalte, keine großen repetitiven Gesten); mit VoiceOver erhalten Custom Gestures standardmäßig keine Handeingabe (Direct Gesture Mode) (hig:accessibility#visionOS, hig:voiceover#visionOS).

## Umsetzung

### SwiftUI
```swift
// Labels, Werte, Hinweise
Button(action: share) { Image(systemName: "square.and.arrow.up") }
    .accessibilityLabel("Teilen")
    .accessibilityHint("Öffnet Optionen zum Teilen")   // sparsam
Slider(value: $volume).accessibilityValue("\(Int(volume * 100)) Prozent")
Image(decorative: "Hintergrund")                       // aus VoiceOver ausblenden
Text("Einstellungen").accessibilityAddTraits(.isHeader)

// Gruppieren / Reihenfolge
VStack { Image(photo); Text(caption) }
    .accessibilityElement(children: .combine)
.accessibilitySortPriority(1)

// Voice Control: alternative Sprachbefehle
.accessibilityInputLabels(["Senden", "Abschicken"])

// Custom Actions statt Swipe-only
.accessibilityAction(named: "Löschen") { delete() }

// Rotor
.accessibilityRotor("Überschriften") { ... }

// Änderungen melden
AccessibilityNotification.Announcement("Download abgeschlossen").post()

// Einstellungen abfragen
@Environment(\.dynamicTypeSize) var typeSize          // typeSize.isAccessibilitySize
@Environment(\.accessibilityReduceMotion) var reduceMotion
@Environment(\.accessibilityReduceTransparency) var reduceTransparency
@Environment(\.colorSchemeContrast) var contrast       // .increased
@Environment(\.legibilityWeight) var weight            // .bold bei Bold Text
@Environment(\.accessibilityDifferentiateWithoutColor) var noColorOnly

// Custom Font mit Dynamic Type
.font(.custom("BrandSans", size: 17, relativeTo: .body))
@ScaledMetric(relativeTo: .body) var iconSize = 24
```

### UIKit
```swift
button.accessibilityLabel = "Teilen"
imageView.isAccessibilityElement = false                 // dekorativ
label.font = UIFontMetrics(forTextStyle: .body).scaledFont(for: brandFont)
label.adjustsFontForContentSizeCategory = true
label.numberOfLines = 0                                  // Truncation vermeiden
if traitCollection.preferredContentSizeCategory.isAccessibilityCategory { /* gestapeltes Layout */ }
UIAccessibility.post(notification: .layoutChanged, argument: firstElement)
UIAccessibility.isReduceMotionEnabled / .isReduceTransparencyEnabled
UIAccessibility.isBoldTextEnabled / .isDarkerSystemColorsEnabled
view.shouldGroupAccessibilityChildren = true
let rotor = UIAccessibilityCustomRotor(name: "Überschriften") { ... }
```

### AppKit
```swift
button.setAccessibilityLabel("Teilen")
NSWorkspace.shared.accessibilityDisplayShouldReduceMotion
NSWorkspace.shared.accessibilityDisplayShouldReduceTransparency
NSWorkspace.shared.accessibilityDisplayShouldIncreaseContrast
NSAccessibility.post(element: view, notification: .layoutChanged)
NSAccessibilityCustomRotor(label: "Überschriften", itemSearchDelegate: self)
```

Hinweis: API-Namen oben stammen aus dem Apple-SDK, nicht aus dem HIG-Spiegel; der Spiegel verweist auf `accessibilityHidden(_:)`, `accessibilityElement`, `isAccessibilityElement`, `shouldGroupAccessibilityChildren`, `AccessibilityNotification`, `AccessibilityRotorEntry`, `UIAccessibilityCustomRotor`, `NSAccessibilityCustomRotor`, `isAccessibilityCategory`, `numberOfLines`.

## Audit-Checkliste

**Sehen**
- [ ] Alle Texte über Text Styles / skalierte Fonts; AX5 (iOS) bzw. AX3 (watchOS) ohne abgeschnittene Kerninhalte.
- [ ] Layout wechselt bei AX-Größen auf gestapelt; Spaltenzahl reduziert; Hierarchie bleibt oben.
- [ ] Keine Texte unter Plattform-Minimum; keine Light/Thin-Schnitte bei kleinem Text.
- [ ] Kontraste ≥ 4.5:1 (≤ 17 pt) bzw. ≥ 3:1 (≥ 18 pt oder Bold) in Light **und** Dark; eigene Farben Ziel 7:1.
- [ ] Increase Contrast liefert sichtbar stärkere Differenzierung (eigene Farben mit HC-Variante).
- [ ] Reduce Transparency: Text auf Materialien/Liquid Glass weiterhin lesbar.
- [ ] Bold Text greift auch bei Custom Fonts.
- [ ] Zustände/Fehler nicht nur über Farbe (zusätzlich Symbol, Text, Form).
- [ ] Bedeutungstragende Icons wachsen mit der Schriftgröße.

**VoiceOver**
- [ ] Jedes interaktive Element hat ein funktionales Label (kein „Button“, kein Dateiname).
- [ ] Dekorative Bilder ausgeblendet; Inhaltsbilder beschrieben.
- [ ] Titel je Screen eindeutig, Überschriften als Header markiert.
- [ ] Lesereihenfolge logisch; Bild + Caption gruppiert.
- [ ] Dynamische Änderungen (Laden fertig, Fehler, Layoutwechsel) werden angesagt.
- [ ] Charts mit Zusammenfassung und navigierbaren Datenpunkten.
- [ ] Custom Controls mit Wert, Traits und Adjustable-/Custom Actions.

**Motorik / Eingabe**
- [ ] Hit-Targets ≥ 44x44 pt (iOS/iPadOS/watchOS), ≥ 28x28 pt (macOS-Default), ≥ 60x60 pt (visionOS); Minima nicht unterschritten.
- [ ] Abstände ~12 pt (mit Bezel) / ~24 pt (ohne Bezel).
- [ ] Jede Geste hat eine sichtbare Alternative (Button, Menü, Custom Action).
- [ ] Keine Mehrfinger-Pflichtgesten für Kernfunktionen.
- [ ] Voice Control: alle Elemente per „Tippe <Name>“ erreichbar.
- [ ] Full Keyboard Access / Tab-Reihenfolge vollständig; Systemkürzel nicht überschrieben.
- [ ] Switch Control erreicht alle Funktionen.

**Hören**
- [ ] Untertitel/Captions/Transkripte für Audio- und Videoinhalte.
- [ ] Audio-Signale zusätzlich visuell und haptisch.

**Kognition / Bewegung**
- [ ] Keine automatisch verschwindenden Hinweise mit Handlungsbedarf.
- [ ] Kein Autoplay ohne Steuerung.
- [ ] Reduce Motion: keine Zoom-/Parallax-/Bounce-Effekte, Fades statt Slides.
- [ ] Dim Flashing Lights bei Videowiedergabe berücksichtigt.
- [ ] Assistive Access (falls relevant): Kernflows einschrittig, destruktive Aktionen doppelt bestätigt.

**Prozess**
- [ ] Accessibility Inspector Audit ohne offene Befunde.
- [ ] Test mit echten Einstellungen (Larger Text, Bold Text, Increase Contrast, Reduce Transparency, Reduce Motion, VoiceOver) – einzeln und kombiniert.
- [ ] Accessibility Nutrition Labels in App Store Connect gepflegt.

## Anti-Patterns

- Feste Schriftgrößen (`.system(size: 15)`) ohne `relativeTo`/`UIFontMetrics`.
- `lineLimit(1)` auf Inhaltstexten → Truncation bei großen Größen.
- Icon-Buttons ohne Label („Button, Bild“ in VoiceOver).
- Status nur als roter/grüner Punkt.
- Grauer Text auf Liquid Glass ohne Prüfung mit Reduce Transparency.
- Swipe-to-delete als einziger Weg zum Löschen.
- Toasts/Banner, die nach wenigen Sekunden verschwinden und eine Aktion enthalten.
- App-eigener Light/Dark-Schalter statt Systemeinstellung (hig:dark-mode#Best-practices).
- Kleine Tap-Ziele dicht nebeneinander (z. B. 24-pt-Icons ohne Padding).
- Dekorative Bilder mit Alt-Text, die VoiceOver-Nutzer ausbremsen.
- Überschreiben von Systemkürzeln (z. B. Cmd-Tab-ähnliche Bindings) in macOS.

## Unklarheiten / Widersprüche im Spiegel

- **Hit-Target macOS:** `buttons#Best-practices` nennt allgemein mindestens 44x44 pt (visionOS 60x60), `accessibility#Mobility` nennt für macOS 28x28 pt Default und 20x20 pt Minimum. Für macOS gilt die plattformspezifische Tabelle; die 44-pt-Regel ist auf Touch ausgerichtet.
- **Kontrast:** `accessibility` nennt 4.5:1 bzw. 3:1 (WCAG AA), `dark-mode` zusätzlich 7:1 als Zielwert für eigene Farben. Kein Widerspruch, aber zwei Niveaus: 4.5:1 = Pflichtminimum, 7:1 = Empfehlung.
- **Schwelle 17/18 pt:** Die Tabelle springt von „bis 17 pt“ auf „18 pt“; Zwischenwerte (z. B. 17.5 pt) sind nicht geregelt.
- **200 %-Ziel vs. tatsächliche Skala:** iOS-Body wächst von 17 auf 53 pt (AX5), watchOS-Body von 16 auf 23 pt (AX3) – die Ziele 200 % / 140 % sind Mindestanforderungen an eigene Lösungen, keine Systemgrenzen.
