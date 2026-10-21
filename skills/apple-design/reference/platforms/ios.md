# iOS (iPhone) – Plattformreferenz

> Quelle: lokaler HIG-Spiegel `~/.apple-design/hig/pages/<slug>.md` (Stand 2026-10-21). Belege als `(hig:<slug>)` bzw. `(hig:<slug>#Anchor)`.
> Paraphrasiert und verdichtet, keine Originaltexte. Zahlen nur, wenn sie im Spiegel stehen.

---

## 1. Kurzprofil

- **Display:** mittelgroß, hochauflösend; Hardware-Features wie Dynamic Island und Statusleiste begrenzen den nutzbaren Bereich (hig:designing-for-ios, hig:layout#Guides-and-safe-areas).
- **Ergonomie:** ein- oder beidhändig gehalten, Hoch- und Querformat, Sehabstand etwa ein bis zwei Fuß. Mitte und unterer Bildschirmbereich sind am besten erreichbar (hig:designing-for-ios).
- **Eingabe:** Multi-Touch, virtuelle Tastatur, Sprache (Siri); dazu Sensoren (Gyro/Accelerometer), persönliche Daten mit Erlaubnis (hig:designing-for-ios).
- **Nutzungsmuster:** sehr kurze Sessions (Minuten) ebenso wie lange (Stunden); häufiges App-Switching, mehrere Apps offen (hig:designing-for-ios).
- **Multitasking auf iPhone:** Picture in Picture (Video, FaceTime) über anderen Apps (hig:multitasking#iOS). Sonderfall **iPhone Duo** (zwei Displays, Scharnier, Split-View-Multitasking auf dem Innendisplay) – siehe Abschnitt 4.4 (hig:designing-for-iphone-duo).
- **Systemflächen:** Widgets, Home Screen Quick Actions, Spotlight, Shortcuts, Activity Views, Live Activities, Control Center (hig:designing-for-ios, hig:controls).

---

## 2. Nicht verhandelbar

1. **Layout über Size Classes entscheiden, nie über Gerätetyp oder Orientierung**; alle Kombinationen compact/regular einplanen (hig:layout#Size-classes).
2. **Safe Areas und System-Margins respektieren** – Dynamic Island, Statusleiste, Toolbars und Tab Bar dürfen Inhalt/Controls nicht verdecken (hig:layout#Guides-and-safe-areas).
3. **Dynamic Type vollständig unterstützen**, inkl. Accessibility-Größen (AX1–AX5); Layout muss umbrechen/stapeln statt abschneiden (hig:typography#Supporting-Dynamic-Type, hig:layout#Adaptability).
4. **Hit-Targets: Standard 44×44 pt, Minimum 28×28 pt** (hig:accessibility#Mobility, hig:buttons#Best-practices).
5. **Tab Bar nur für Navigation, nie für Aktionen**; Aktionen gehören in eine Toolbar (hig:tab-bars#Best-practices).
6. **Tab Bar in allen Bereichen sichtbar lassen** (Ausnahme: Modal verdeckt sie); Tabs nie deaktivieren oder ausblenden (hig:tab-bars#Best-practices).
7. **Liquid Glass nur in der Funktionsebene** (Bars, Controls), nicht im Content Layer; sparsam bei Custom Controls (hig:materials#Liquid-Glass).
8. **Keine eigenen Bar-Hintergründe/Tönungen**; Trennung über Scroll Edge Effect statt opaker Fläche (hig:toolbars#Best-practices, hig:layout#Visual-hierarchy).
9. **Standard-Back- und Close-Buttons verwenden**, keine Textlabels „Zurück“/„Schließen“ (hig:toolbars#Navigation).
10. **Jedes Modal muss offensichtlich schließbar sein** – Button in der oberen Toolbar oder Wischen nach unten; bei drohendem Datenverlust Bestätigung per Action Sheet (hig:modality#Best-practices, hig:sheets#iOS-iPadOS).
11. **Nur ein Sheet gleichzeitig**, nie mehr als ein Alert gleichzeitig (hig:sheets#Best-practices, hig:modality#Best-practices).
12. **Light, Dark und Increased Contrast unterstützen** – auch bei Single-Appearance-Apps beide Farbvarianten liefern (Liquid-Glass-Adaptivität) (hig:color).
13. **Systemgesten nicht überschreiben** (Edge-Swipes, Home-Indikator, Drei-Finger-Undo, Shake) (hig:gestures#Custom-gestures, hig:undo-and-redo#iOS-iPadOS).
14. **Launch Screen = fast identisch zum ersten Screen**, kein Text, kein Branding/Werbung (hig:launching#Launch-screens).
15. **Kontext sichern und wiederherstellen** – App kann jederzeit unterbrochen werden (hig:multitasking#Best-practices, hig:launching#Best-practices).

---

## 3. Layout & Maße

### 3.1 Belegte Kennwerte

| Kennwert | Wert | Quelle |
|---|---|---|
| Control-Größe Standard / Minimum | 44×44 pt / 28×28 pt | (hig:accessibility#Mobility) |
| Button-Hit-Region mindestens | 44×44 pt | (hig:buttons#Best-practices) |
| Padding um Elemente mit Bezel | ca. 12 pt | (hig:accessibility#Mobility) |
| Padding um Elemente ohne Bezel | ca. 24 pt (um sichtbare Kanten) | (hig:accessibility#Mobility) |
| Textgröße Standard / Minimum | 17 pt / 11 pt | (hig:typography#Ensuring-legibility) |
| Textvergrößerung anbieten | mind. 200 % | (hig:accessibility) |
| Toolbar-/Fenstertitel | unter 15 Zeichen | (hig:toolbars#Titles) |
| Toolbar-Gruppen | max. ca. 3 | (hig:toolbars#Item-groupings) |
| Sign-in-with-Apple-Button-Höhe (Default iOS) | 44 pt | (hig:sign-in-with-apple) |
| Drag-Image erscheinen lassen nach | ca. 3 pt Bewegung | (hig:drag-and-drop#Providing-feedback) |
| Dimming hinter Clear Liquid Glass über hellem Inhalt | 35 % Deckkraft, dunkel | (hig:materials#Liquid-Glass) |
| Home Screen Quick Actions | max. 4 | (hig:home-screen-quick-actions) |
| App-Icon-Layoutgröße | 1024×1024 px, quadratisch, Systemmaske | (hig:app-icons#Specifications) |

### 3.2 Gerätegrößen / Safe-Area-Insets

**Im Spiegel nicht enthalten.** Die Seite `layout.md` (Update 2026-09-09) enthält keine Gerätetabelle und keine Safe-Area-Insets mehr, obwohl das Change Log frühere Spezifikationen (iPhone 14–17, iPhone Air, 16e) erwähnt. Safe-Area-Werte deshalb **nie hart kodieren**, sondern zur Laufzeit über `safeAreaInsets`/Layout Guides beziehen; Werte für Mockups aus Apple Design Resources (hig:layout, hig:designing-for-iphone-duo#Dynamic-layouts).

Indirekt belegte iPhone-Bildschirmgrößen (Portrait, pt) aus den Widget- und Live-Activity-Tabellen, **ohne Gerätezuordnung im Spiegel**: 430×932, 428×926, 414×896, 414×736, 393×852, 390×844, 375×812, 375×667, 360×780, 320×568 (hig:widgets#Specifications, hig:live-activities#Specifications).

### 3.3 Adaptivität – was die App aushalten muss
(hig:layout#Adaptability)
- compact/regular in beiden Achsen, Hoch-/Querformat, verschiedene Seitenverhältnisse
- Dynamic Island, Display Zoom, iPhone Mirroring auf dem Mac (frei skalierbare Fenstergröße)
- Textgrößenänderung, RTL-Layout, lokalisierte Datums-/Zahlenformate, Textlängen
- Auch orientierungsfixierte Apps (z. B. Landscape-Spiele) müssen sauber skalieren; Hintergrundartwork skalieren statt verzerren/letterboxen.
- Landscape-only: beide Querlagen (links/rechts gedreht) korrekt behandeln; in aktueller Geräteorientierung starten (hig:launching#iOS-iPadOS).

### 3.4 Visuelle Hierarchie
- Wichtigstes oben und leading; Ausrichtung zum Scannen, Einrückung für Unterordnung (hig:layout#Visual-hierarchy).
- Verwandtes gruppieren (Weißraum, Container, Trennlinien); Progressive Disclosure (hig:layout#Visual-hierarchy).
- Vollflächige Hintergründe unter Toolbar und Tab Bar durchlaufen lassen (hig:layout#Visual-hierarchy).

---

## 4. Navigation & Struktur

### 4.1 Entscheidungsmatrix

| Situation | Muster | Quelle |
|---|---|---|
| 2+ gleichrangige Top-Level-Bereiche | **Tab Bar** (unten, schwebend, Liquid Glass) | (hig:tab-bars#iOS) |
| Hierarchisches Drill-down | **Navigation Stack** mit Toolbar (Navigation Bar), Large Title, Back-Button | (hig:toolbars#Navigation, hig:toolbars#iOS) |
| Mehrere Ebenen nebeneinander | **Split View nur in regular width** (z. B. iPhone quer großes Modell, iPhone Duo innen); compact → einspaltig | (hig:split-views#iOS) |
| Eng umrissene Teilaufgabe | **Sheet** (Detents medium/large) | (hig:sheets) |
| Komplexe/lange Aufgabe, Medien, Kamera | **Full-Screen-Modal** | (hig:sheets#Best-practices, hig:modality) |
| Auswahl zu einer gerade ausgelösten Aktion | **Action Sheet** (nicht Menü, nicht Alert) | (hig:action-sheets#iOS-iPadOS, hig:alerts#iOS-iPadOS) |
| Kritische Info/Bestätigung | **Alert** | (hig:alerts) |
| Wechsel eng verwandter Unteransichten | **Segmented Control** (nicht Tab Bar) | (hig:segmented-controls#iOS-iPadOS) |
| Zusatzinformationen in compact width | **kein Popover**, stattdessen Sheet | (hig:popovers#iOS-iPadOS) |
| Paging (Weather-artig) | Scroll View paged + Page Control; dann keinen Scroll-Indikator auf derselben Achse | (hig:scroll-views#iOS-iPadOS) |

### 4.2 Tab Bar (iOS)
- Schwebt unten über dem Inhalt auf Liquid Glass (hig:tab-bars#iOS).
- Optional **Bottom Accessory** (z. B. MiniPlayer); Tab Bar kann sich beim Herunterscrollen minimieren, Accessory rückt inline. Rückkehr durch Tab-Tap oder Scroll nach oben (hig:tab-bars#iOS).
- Optional **Search-Tab** am trailing Ende (hig:tab-bars#iOS, hig:search-fields#iOS).
- Labels immer (möglichst ein Wort), SF Symbols, bevorzugt gefüllt; in compact Icon über Label (hig:tab-bars#Best-practices).
- More-Tab (Overflow) vermeiden; leere Bereiche erklären statt Tab deaktivieren (hig:tab-bars#Best-practices).
- Badge nur für kritische Info (rotes Oval) (hig:tab-bars#Best-practices).
- Tab-Label-Farbe nicht ähnlich zum Content-Hintergrund; bei buntem Inhalt monochrom (hig:tab-bars#Best-practices, hig:color#Liquid-Glass-color).

### 4.3 Toolbars / Navigation Bar (iOS)
- Nur das Wichtigste in den Hauptbereich; Rest in ein **More-Menü** (hig:toolbars#iOS).
- **Large Title** zur Orientierung; kollabiert beim Scrollen zum Standardtitel (hig:toolbars#iOS).
- Drei Zonen: leading (Back, Titel, Dokumentmenü), center, trailing (wichtige Aktionen, Suche, More, primäre Aktion) (hig:toolbars#Item-groupings).
- **Eine** primäre Aktion (Done/Submit) im `.prominent`-Stil, trailing (hig:toolbars#Actions).
- Symbole ohne Rahmen (keine Kreis-Outlines); Text nur, wo kein Symbol trägt (z. B. „Bearbeiten“); Text- und Symbol-Buttons durch festen Abstand trennen (hig:toolbars#Actions, hig:toolbars#Item-groupings).
- Titel nicht mit App-Namen belegen (hig:toolbars#Titles).
- Custom-Komponenten in Bars: Eckradien konzentrisch zur Bar (hig:toolbars#Best-practices).

### 4.4 iPhone Duo (seit 2026-09-09 im Spiegel)
(hig:designing-for-iphone-duo)
- Außendisplay = compact width, Innendisplay = regular width; Posen über Size Classes abdecken, **kein** Custom-Layout je Pose.
- Toolbars, Tab Bar, Statusleiste, Dynamic Island wandern bei geschlossenem Gerät (und innen quer) **vertikal an die Seite**; Ausnahme: Innendisplay hochkant. Standardplatzierung nicht überschreiben.
- Vertikale Reihenfolge: oben Navigation (Back/Close), dann prominente Aktion (Done), restliche Gruppen beibehalten; Overflow läuft von unten nach oben, über Visibility Priority steuerbar.
- **Reserved Regions**: äußere Kamera (immer, wird für Live Activities zur Dynamic Island), innere Kamera (nur aktiv), Faltbereich (nur teilgefaltet). Custom Views über `ReservedRegion` freihalten; Grids mit gerader Spaltenzahl.
- Split View: innen ausgeklappt, außen eine Spalte. **Arrangement Views** (split/overlay) für zweiteilige Layouts; Navigation-Container gehören außerhalb.
- Jede Toolbar-Aktion mit Titel **und** Symbol (Titel wird im Overflow genutzt); Text-Buttons minimieren; eigenes Overflow-Menü in das System-Overflow-Menü überführen.
- Platzmangel: navigationslastig → Toolbar-Items ins Overflow; aufgabenlastig → Tab Bar minimieren.

### 4.5 Sheets (iOS)
(hig:sheets#iOS-iPadOS, hig:sheets#Best-practices)
- Einzelansicht: **Cancel leading, Done trailing** in der oberen Toolbar. Mehrschritt: Schritt 1 Cancel + (inaktiv) Done; Folgeschritte Back + Done. Nie Cancel, Done und Back gleichzeitig.
- Done immer mit Alternative (Cancel oder Back) kombinieren.
- Detents: *large* (voll), *medium* (ca. halbe Höhe), eigene möglich. Medium für Progressive Disclosure (Share Sheet); Compose-artige Aufgaben nur large.
- Bei resizable Sheets **Grabber** zeigen (auch VoiceOver-relevant).
- Swipe-to-dismiss unterstützen; bei ungesicherten Änderungen Action Sheet zur Bestätigung.
- Sheets können **nichtmodal** sein (z. B. Format-Sheet in Notes), wenn sie den Parent-View beeinflussen.
- Aus einem Sheet heraus kein zweites Sheet stapeln; erst schließen.

### 4.6 Suche (iOS)
(hig:search-fields#iOS)
- Drei Orte: **Tab** (Standard-Tab mit Landing Page für Entdecken; oder Button-Erscheinung für sofortiges Tippen), **Toolbar** (unten bevorzugt, wenn Platz; oben, wenn unten Inhalt Vorrang hat), **inline** (Filter einer Liste; oben über der Liste, ggf. an Toolbar pinnen).

### 4.7 Modality allgemein
(hig:modality)
- Nur bei klarem Nutzen; kurz und einfach; keine „App in der App“ mit eigener Hierarchie.
- Titel benennt die Aufgabe.

---

## 5. Komponenten-Besonderheiten (Platform considerations iOS)

| Komponente | Regel | Quelle |
|---|---|---|
| Action Sheet | Für Wahl zu einer Aktion; nicht scrollen lassen | (hig:action-sheets#iOS-iPadOS) |
| Alert | Möglichst nicht scrollend (kurze Titel, Nachricht nur wenn nötig); für Fehler Alert statt Notification | (hig:alerts#iOS-iPadOS, hig:notifications) |
| Buttons | Activity Indicator im Button bei verzögerten Aktionen, ggf. Label „Checking out…“; 1–2 prominente Buttons pro View; Press-State Pflicht | (hig:buttons#iOS-iPadOS, hig:buttons#Style) |
| Button-Rollen | Primary nie für destruktive Aktion; destruktiv = Systemrot | (hig:buttons#Role) |
| Context Menu | Entweder Context Menu oder Edit Menu pro Objekt, nicht beides; grafische Vorschau; destruktive Items ans Ende, rot | (hig:context-menus#iOS-iPadOS, hig:context-menus) |
| Menüs | Layouts small (4 Symbole oben), medium (3 Symbole+Label), large (Liste, Default) | (hig:menus#iOS-iPadOS) |
| Edit Menu | kompakt horizontal bei Touch, vertikal bei Tastatur/Pointer; Position ggf. verschieben | (hig:edit-menus#iOS-iPadOS) |
| Pull-down | More-Button (Ellipse) für Nebensächliches, Abwägung Auffindbarkeit | (hig:pull-down-buttons#iOS-iPadOS) |
| Listen | Info-Button nur für Zusatzinfo, Drill-down per Disclosure Indicator; kein Index bei trailing Accessories | (hig:lists-and-tables#iOS-iPadOS-visionOS) |
| Toggles | Switch nur in Listenzeilen (ohne extra Label); außerhalb Toggle-Button; Grün nur bei Bedarf ändern | (hig:toggles#iOS-iPadOS) |
| Slider | Nie für Lautstärke – Volume View verwenden | (hig:sliders#iOS-iPadOS) |
| Date Picker | Stile compact/inline/wheels/automatic; Countdown max. 23 h 59 min; compact bei Platzmangel | (hig:pickers#iOS-iPadOS) |
| Text Fields | Clear-Button trailing; leading = Zweck, trailing = Zusatzfunktion | (hig:text-fields#iOS-iPadOS) |
| Text Views | passenden Keyboard-Typ zeigen | (hig:text-views#iOS-iPadOS) |
| Virtuelle Tastatur | Keyboard Layout Guide; Input-Accessory-Controls nur aufgabenrelevant, bei Bedarf Liquid Glass bzw. Standard-Toolbar | (hig:virtual-keyboards#iOS-iPadOS) |
| Page Control | Hintergrund automatic/prominent/minimal; bei minimal kein Scrubbing; keine Animation beim Scrubben | (hig:page-controls#iOS-iPadOS) |
| Refresh Control | automatisch aktualisieren; Titel nur mit Mehrwert (z. B. letzte Aktualisierung) | (hig:progress-indicators#iOS-iPadOS) |
| Collections | Layoutwechsel nicht während Interaktion | (hig:collections#iOS-iPadOS) |
| Status Bar | Inhalt darunter abdunkeln/verdecken; nur für Vollbildmedien temporär ausblenden, nie dauerhaft | (hig:status-bars) |
| Vollbild | Home-Indikator-Verhalten beibehalten; nur bei Fehl-Exits auf Zwei-Wisch-Exit umstellen | (hig:going-full-screen#iOS-iPadOS) |
| Gesten | Drei-Finger-Swipe Undo/Redo, Drei-Finger-Pinch Copy/Paste, Shake Undo; Simultangesten v. a. für Spiele | (hig:gestures#iOS-iPadOS) |
| Undo/Redo | Alert-Titel „Undo <Objekt>“ präzise; Standardgesten nicht umdefinieren | (hig:undo-and-redo#iOS-iPadOS) |
| Haptik | Standard-Controls nutzen System-Haptik; Feedback Generator: notification (success/warning/error), impact (light/medium/heavy/rigid/soft), selection | (hig:playing-haptics#iOS) |
| Audio | System Sound Services für kurze Töne/Vibrationen | (hig:playing-audio#iOS-iPadOS) |
| Farben | Background-Sets *system* und *grouped* (primary/secondary/tertiary); Label-Hierarchie label…quaternaryLabel, separator, link | (hig:color#iOS-iPadOS) |
| Dark Mode | base vs. elevated Hintergründe; System-Hintergrundfarben bevorzugen | (hig:dark-mode#iOS-iPadOS) |
| Dateien | Document Launcher (ab iOS 18) mit Title Card (2 Buttons), Hintergrund, Accessories; File-Provider-Extension ohne eigene Top-Toolbar | (hig:file-management#iOS-iPadOS) |
| Action Button | Aktionen ohne App-Start (Live Activity, Snippets) | (hig:action-button#iOS) |

---

## 6. Liquid Glass & Materialien

- **Zwei Ebenen:** Liquid Glass = Funktionsebene (Tab Bar, Toolbars, Sidebars, Controls), schwebt über dem Content Layer; Standardmaterialien = Differenzierung *im* Content Layer (hig:materials).
- **Kein Liquid Glass im Content Layer.** Ausnahme: transiente Controls (Slider, Toggle) nehmen beim Bedienen Glass-Optik an (hig:materials#Liquid-Glass).
- **Varianten:** *regular* (blurrt/regelt Luminanz, Default für die meisten Systemkomponenten, für textlastige Elemente wie Alerts, Sidebars, Popovers) und *clear* (stark transparent, nur über visuell reichen Medien). Bei clear über hellem Inhalt dunkle Dimming-Ebene 35 %; bei dunklem Inhalt oder AVKit-Controls nicht nötig (hig:materials#Liquid-Glass).
- **Sparsam bei Custom Controls**; Standardkomponenten übernehmen Glass automatisch (hig:materials#Liquid-Glass).
- **Farbe:** Glass ist farblos und übernimmt Farbe vom Hintergrund. Tönung nur für Emphase (primäre Aktion, Status), dann auf den **Hintergrund** des Controls, nicht auf Symbol/Text; nicht mehrere getönte Controls. Kleine Elemente (Tab Bar, Toolbar) schalten automatisch hell/dunkel mit monochromen Symbolen (hig:color#Liquid-Glass-color).
- **Scroll Edge Effect** statt opaker Bar-Hintergründe: *automatic* bevorzugen; *hard* = opaker mit Kante, *soft* = weicher Verlauf (testen); nur wenn Scroll-Inhalt unter schwebenden Elementen liegt; einer pro View (hig:scroll-views#Scroll-edge-effects).
- **Background Extension Effect**, wenn Hintergrundbild unter Sidebar/Inspector gespiegelt-geblurrt weiterlaufen soll (hig:layout#Visual-hierarchy).
- **Standardmaterialien iOS:** ultraThin, thin, regular (Default), thick; dazu Vibrancy für Labels (label…quaternaryLabel; quaternary nicht auf thin/ultraThin), Fills (fill…tertiaryFill), Separator (eine Stufe) (hig:materials#iOS-iPadOS).
- **Material nach Semantik wählen, nicht nach Farbwirkung**; dickere Materialien für feine Texte, dünnere für Kontext (hig:materials#Standard-materials).
- **App-Icons** sind geschichtet, erhalten Liquid-Glass-Effekte (Spiegelungen, Refraktion); Erscheinungen default, dark, clear light/dark, tinted light/dark; ungemaskte quadratische Layer, Vektor bevorzugt, Gestaltung in Icon Composer (hig:app-icons).

---

## 7. Typografie & Dynamic Type

- Systemschrift **SF Pro**, zusätzlich **New York** (Serif) (hig:typography#iOS-iPadOS). Systemfonts nicht einbetten, über `Font.Design` ansprechen (hig:typography#Using-system-fonts).
- Default 17 pt, Minimum 11 pt; leichte Schnitte (Ultralight/Thin/Light) meiden (hig:typography#Ensuring-legibility).
- Built-in Text Styles nutzen → Dynamic Type inkl. AX-Größen gratis; Custom Fonts müssen Dynamic Type und Bold Text selbst unterstützen (hig:typography#Using-custom-fonts).
- Bei großen Größen: stapeln statt nebeneinander, Spalten reduzieren, Trunkierung minimieren, Icons mitskalieren, Hierarchie halten (hig:typography#Supporting-Dynamic-Type).
- Tracking im laufenden System automatisch; für Mockups Tracking-Tabellen (hig:typography#Tracking-values).

### 7.1 Default-Größe „Large“ (pt; Gewicht / Leading / Emphasized)
(hig:typography#Specifications)

| Style | Gewicht | Größe | Leading | Emphasized |
|---|---|---|---|---|
| Large Title | Regular | 34 | 41 | Bold |
| Title 1 | Regular | 28 | 34 | Bold |
| Title 2 | Regular | 22 | 28 | Bold |
| Title 3 | Regular | 20 | 25 | Semibold |
| Headline | Semibold | 17 | 22 | Semibold |
| Body | Regular | 17 | 22 | Semibold |
| Callout | Regular | 16 | 21 | Semibold |
| Subhead | Regular | 15 | 20 | Semibold |
| Footnote | Regular | 13 | 18 | Semibold |
| Caption 1 | Regular | 12 | 16 | Semibold |
| Caption 2 | Regular | 11 | 13 | Semibold |

### 7.2 Größenverlauf ausgewählter Styles (pt)
(hig:typography#Specifications)

| Style | xS | S | M | **L** | xL | xxL | xxxL | AX1 | AX2 | AX3 | AX4 | AX5 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Large Title | 31 | 32 | 33 | **34** | 36 | 38 | 40 | 44 | 48 | 52 | 56 | 60 |
| Title 1 | 25 | 26 | 27 | **28** | 30 | 32 | 34 | 38 | 43 | 48 | 53 | 58 |
| Body/Headline | 14 | 15 | 16 | **17** | 19 | 21 | 23 | 28 | 33 | 40 | 47 | 53 |
| Subhead | 12 | 13 | 14 | **15** | 17 | 19 | 21 | 25 | 30 | 36 | 42 | 49 |
| Footnote | 12 | 12 | 12 | **13** | 15 | 17 | 19 | 23 | 27 | 33 | 38 | 44 |
| Caption 2 | 11 | 11 | 11 | **11** | 13 | 15 | 17 | 20 | 24 | 29 | 34 | 40 |

Vollständige Tabellen (alle Styles, Leading) im Spiegel unter `typography.md#Specifications`. Punktgrößen basieren auf 144 ppi (@2x) bzw. 216 ppi (@3x).

---

## 8. Systemintegration

### 8.1 Widgets
(hig:widgets)
- Home Screen / Today View: system small, medium, large; StandBy, CarPlay, Apple HomeView: nur small. Lock Screen: accessory circular, rectangular, inline (über der Uhr). Kein extra large auf iPhone.
- Lock-Screen-Widgets wie Complications denken: Information, kein App-Launcher; Always-On mit reduzierter Leuchtdichte → genug Graustufenkontrast.
- Erscheinungen auf dem Home Screen: light, dark, clear, tinted (System entsättigt; Full-Color-Bilder gezielt freigeben). Rendering Modes full-color / accented / vibrant beachten.
- StandBy: zwei small-Widgets nebeneinander, hochskaliert, Hintergrund entfernt → Hintergrund als entfernbar markieren, Text vergrößern statt Bildfarben; Nachtmodus rot monochrom.
- Ränder **16 pt** Standard, **11 pt** für enge Gruppierungen; Text ≥ **11 pt**; Text nicht rastern; Eckradien über `ContainerRelativeShape` (hig:widgets#Choosing-margins-and-padding, hig:widgets#Displaying-text-in-widgets).
- Animationen bei Updates bis **2 s** (hig:widgets#Updating-widget-content).
- Tap öffnet die passende Stelle in der App; Interaktion einfach halten, kein App-artiges Layout.
- Echtzeit → Live Activity statt Widget.

**Widget-Größen iPhone (pt)** (hig:widgets#Specifications)

| Screen (Portrait) | Small | Medium | Large | Circular | Rectangular | Inline |
|---|---|---|---|---|---|---|
| 430×932 | 170×170 | 364×170 | 364×382 | 76×76 | 172×76 | 257×26 |
| 428×926 | 170×170 | 364×170 | 364×382 | 76×76 | 172×76 | 257×26 |
| 414×896 | 169×169 | 360×169 | 360×379 | 76×76 | 160×72 | 248×26 |
| 414×736 | 159×159 | 348×157 | 348×357 | 76×76 | 170×76 | 248×26 |
| 393×852 | 158×158 | 338×158 | 338×354 | 72×72 | 160×72 | 234×26 |
| 390×844 | 158×158 | 338×158 | 338×354 | 72×72 | 160×72 | 234×26 |
| 375×812 | 155×155 | 329×155 | 329×345 | 72×72 | 157×72 | 225×26 |
| 375×667 | 148×148 | 321×148 | 321×324 | 68×68 | 153×68 | 225×26 |
| 360×780 | 155×155 | 329×155 | 329×345 | 72×72 | 157×72 | 225×26 |
| 320×568 | 141×141 | 292×141 | 292×311 | – | – | – |

### 8.2 Live Activities
(hig:live-activities)
- Für Aufgaben mit Anfang und Ende, max. ca. **8 Stunden**; keine Werbung; sensible Daten nur als harmlose Zusammenfassung.
- Präsentationen: compact (leading+trailing um die TrueDepth-Kamera, als *eine* Info lesbar, eng an die Kamera), minimal, expanded, Lock Screen, StandBy. Erst iPhone-Design, dann verfeinern.
- **Limited width** (z. B. Dynamic Island quer): compact/minimal in einen Kreis von **28 pt** Durchmesser einpassen.
- Lock-Screen-Rand **14 pt**; Höhe dynamisch anpassen; keine Notification-Optik kopieren; Dismiss-Button-Farbe prüfen.
- Dynamic Island: schwarzer, opaker Hintergrund, nicht änderbar → kräftige Farben, Key Line tönen. Logo ohne Container, nie ganzes App-Icon. Nichts in der App, das auf die Dynamic Island zeigt.
- Text: groß, mindestens Medium-Gewicht.
- Ende sofort beenden; auf dem Lock Screen bleibt sie bis zu **4 Stunden**. Alerts nur für essenzielle Updates. Mehrere Events in *einer* Activity rotieren.
- App Shortcut zum Starten anbieten (z. B. über Action Button).

**Live-Activity-Maße iPhone (pt)** (hig:live-activities#Specifications)

| Screen (Portrait) | Compact (je Seite) | Minimal (Breite) | Expanded (Höhe) | Lock Screen (Höhe) | Limited width |
|---|---|---|---|---|---|
| 430×932 | 62.33×36.67 | 36.67–45 × 36.67 | 408 × 84–160 | 408 × 84–160 | 28×28 |
| 393×852 | 52.33×36.67 | 36.67–45 × 36.67 | 371 × 84–160 | 371 × 84–160 | 28×28 |

### 8.3 Controls (Control Center, Lock Screen, Action Button)
(hig:controls)
- Button oder Toggle mit Symbol, Titel, optional Wert; Symbol muss allein verständlich sein (Lock Screen zeigt nur Symbol).
- Symbolanimation für Zustandswechsel; Tint-Farbe passend zur Marke; Hint-Text für den Action Button; Platzhalter, wenn Titel/Wert situativ.
- Sensible Werte im gesperrten Zustand redigieren; sicherheitsrelevante Aktionen nur nach Entsperren.

### 8.4 App Shortcuts / App Intents / Siri
(hig:app-shortcuts)
- Häufigste, wichtigste Aufgaben; höchstens ein optionaler Parameter; kurze Phrasen; in Spotlight (Top Hit) und Shortcuts-App nach Wichtigkeit ordnen.
- Für Standard-Domänen App Schemas erwägen. Antworten auch audio-only verständlich.

### 8.5 Notifications & Badges
(hig:notifications)
- Kurz, keine Dubletten, keine sensiblen Daten, kein App-Name/Icon im Text; generischer Text für ausgeblendete Vorschauen.
- Aktionen: zeitsparend, nicht „App öffnen“, bevorzugt nicht-destruktiv, mit Symbol.
- Badge nur für Anzahl ungelesener Notifications; nie nachbauen.

### 8.6 Weitere
- Home Screen Quick Actions: max. 4, SF Symbols statt Emoji, stabile Titel (hig:home-screen-quick-actions).
- Bewertungsprompt des Systems; System begrenzt auf 3× pro 365 Tage (hig:ratings-and-reviews).
- Passkeys bevorzugen, wenn kein Sign in with Apple (hig:managing-accounts).

---

## 9. Umsetzung: SwiftUI / UIKit

Legende: **[S]** = API im Spiegel referenziert; **[K]** = gängige API, nicht im Spiegel belegt – vor Verwendung in der Entwicklerdoku prüfen.

| Muster | SwiftUI | UIKit |
|---|---|---|
| Tab-Navigation | `TabView` [S], `Tab` [K], `Tab(role: .search)` [K] | `UITabBarController` [K], `UITabBar` [S] |
| Tab Bar minimieren / Accessory | `TabBarMinimizeBehavior` [S], `tabViewBottomAccessory` [K] / `TabViewBottomAccessoryPlacement` [S] | `UITabBarController.MinimizeBehavior` [S] |
| Navigation Stack | `NavigationStack` [K], `.navigationTitle` [K] | `UINavigationController` [K], `prefersLargeTitles` [S] |
| Split View | `NavigationSplitView` [S] | `UISplitViewController` [S] |
| Toolbar | `.toolbar` / `ToolbarItem(placement:)` [K], `ToolbarItemGroup` [S], `ToolbarItemPlacement` [S], `ToolbarItemVisibilityPriority` [S], `ToolbarOverflowMenu` [S] | `UIToolbar` [S], `UIBarButtonItemGroup` [S], `fixedSpace` [S], `additionalOverflowItems` [S] |
| Sheet / Detents | `.sheet(item:)` [S], `.presentationDetents` [K], `.presentationDragIndicator` [K] | `UISheetPresentationController` [S], `detents` [S], `prefersGrabberVisible` [S] |
| Full-Screen-Modal | `.fullScreenCover` [K] | `UIModalPresentationStyle.fullScreen` [S] |
| Action Sheet | `.confirmationDialog` [K] (Spiegel: „presentation modifier for a confirmation dialog“) | `UIAlertController.Style.actionSheet` [S] |
| Suche | `.searchable` [K] | `UISearchController` [K] |
| Liquid Glass custom | `.glassEffect(_:in:)` [S], `Glass.regular` / `Glass.clear` [S], `GlassEffectContainer` [K], `.buttonStyle(.glass/.glassProminent)` [K] | `UIGlassEffect` [K] |
| Scroll Edge Effect | `ScrollEdgeEffectStyle` [S] | `UIScrollEdgeEffect.Style` [S] |
| Background Extension | `backgroundExtensionEffect()` [S] | `UIBackgroundExtensionView` [S] |
| Materialien | `Material` (`.ultraThin` … `.thick`) [S] | `UIVisualEffectView`, `UIBlurEffect`, `UIVibrancyEffect` [S] |
| Size Classes | `UserInterfaceSizeClass` [S] | `UITraitChangeObservable` [S] |
| Safe Area | `SafeAreaRegions` [S], `safeAreaInsets` [S] | `safeAreaInsets` [S], `UILayoutGuide` [S] |
| Tastatur | `ToolbarItemPlacement` (keyboard) [S] | `UIKeyboardLayoutGuide` [S], `inputAccessoryView` [S] |
| iPhone Duo | `ReservedRegion` [S], `ArrangementView` [S], `ToolbarVerticalCompressionBehavior` [S] | `UIView.ReservedRegion` [S], `UIArrangementViewController` [S], `UIVerticalBarCompressionBehavior` [S] |
| Menü-Layout | – | `UIMenu.preferredElementSize` [S] |
| Refresh | `.refreshable` [K] | `UIRefreshControl` [S] |
| Haptik | `.sensoryFeedback` [K] | `UIFeedbackGenerator` [S] |
| Widgets | WidgetKit, `ContainerRelativeShape` [S], `padding(_:_:)` [S] | – |
| Live Activities | ActivityKit [S], `ActivityFamily.small` (CarPlay) [S], `activitySystemActionForegroundColor(_:)` [S] | – |
| Controls | `ControlWidget` [K], `IntentAuthenticationPolicy` [S] | – |
| Vollbild/Systemgesten | `preferredScreenEdgesDeferringSystemGestures` [S] | dito |
| Dokument-Launcher | `DocumentGroupLaunchScene` [S] | – |
| Review-Prompt | `RequestReviewAction` [S] | – |

---

## 10. Review-Checkliste (iOS)

- [ ] Layout-Entscheidungen hängen an Size Classes, nicht an `idiom`/Orientierung/Bildschirmbreite (hig:layout#Size-classes)
- [ ] Getestet: kleinste und größte iPhone-Größe, quer und hoch, Display Zoom, iPhone Mirroring (hig:layout#Adaptability)
- [ ] Keine hart kodierten Safe-Area-Werte; nichts unter Dynamic Island/Statusleiste/Home-Indikator verdeckt (hig:layout#Guides-and-safe-areas)
- [ ] Alle Tap-Ziele ≥ 44×44 pt (Minimum 28×28 pt nur ausnahmsweise), ausreichender Abstand (hig:accessibility#Mobility)
- [ ] Dynamic Type bis AX5 ohne Abschneiden/Überlappen; horizontale Gruppen stapeln (hig:typography#Supporting-Dynamic-Type)
- [ ] Kein Text unter 11 pt; keine Light/Thin-Schnitte für Fließtext (hig:typography#Ensuring-legibility)
- [ ] Text Styles statt fixer Punktgrößen; Custom Fonts unterstützen Dynamic Type + Bold Text (hig:typography)
- [ ] Tab Bar nur Navigation, mit Labels, SF Symbols, kein More-Overflow, keine deaktivierten Tabs (hig:tab-bars)
- [ ] Tab Bar bleibt in allen Bereichen sichtbar (außer unter Modals) (hig:tab-bars#Best-practices)
- [ ] Navigation Stack mit Standard-Back-Button und Swipe-back; Large Title auf Top-Level-Screens (hig:toolbars, hig:designing-for-ios)
- [ ] Genau eine prominente Toolbar-Aktion, trailing; Symbole ohne Rahmen (hig:toolbars#Actions)
- [ ] Keine eigenen Bar-Hintergrundfarben/Blur-Fakes; Scroll Edge Effect automatic (hig:toolbars, hig:scroll-views#Scroll-edge-effects)
- [ ] Liquid Glass nicht im Content Layer; Custom-Glass sparsam; clear nur über Medien, ggf. 35-%-Dimming (hig:materials#Liquid-Glass)
- [ ] Farbe auf Glass nur für primäre Aktion/Status, auf dem Hintergrund statt auf Symbol (hig:color#Liquid-Glass-color)
- [ ] Sheets: Cancel leading, Done trailing; Grabber bei Resize; Swipe-to-dismiss mit Verlustschutz (hig:sheets#iOS-iPadOS)
- [ ] Kein gestapeltes Sheet, nie zwei Alerts gleichzeitig (hig:sheets, hig:modality)
- [ ] Popovers nur in regular width; in compact Sheet (hig:popovers#iOS-iPadOS)
- [ ] Wahl zu einer Aktion = Action Sheet, nicht Alert; Action Sheets scrollen nicht (hig:action-sheets#iOS-iPadOS)
- [ ] Switches nur in Listenzeilen; Lautstärke über Volume View (hig:toggles#iOS-iPadOS, hig:sliders#iOS-iPadOS)
- [ ] Destruktive Menüeinträge am Ende und als destruktiv markiert; primäre Rolle nie destruktiv (hig:context-menus, hig:buttons#Role)
- [ ] Light/Dark/Increased Contrast geprüft; System- bzw. semantische Farben (hig:color, hig:dark-mode#iOS-iPadOS)
- [ ] Systemgesten (Edge-Swipe, Home-Indikator, Drei-Finger-Undo) nicht überschrieben (hig:gestures, hig:undo-and-redo#iOS-iPadOS)
- [ ] Status Bar nicht dauerhaft versteckt; Inhalt darunter lesbar abgedeckt (hig:status-bars)
- [ ] Launch Screen ≈ erster Screen, ohne Text/Logo; Zustand wird wiederhergestellt (hig:launching)
- [ ] App-Icon: 1024×1024 px, ungemaskte Layer, dark/clear/tinted geprüft (hig:app-icons)
- [ ] Widgets: 16-pt-Ränder, Text ≥ 11 pt, Deep Link, Always-On/StandBy/tinted geprüft (hig:widgets)
- [ ] Live Activity: compact als eine Einheit, Limited Width 28 pt, Lock-Screen-Rand 14 pt, endet sofort (hig:live-activities)
- [ ] Notifications ohne sensible Daten, Badge nur für Ungelesenes (hig:notifications)
- [ ] iPhone Duo (falls unterstützt): vertikale Bars nicht überschrieben, Reserved Regions frei, alle Toolbar-Items mit Titel+Symbol (hig:designing-for-iphone-duo)

---

## 11. Häufige Fehler („Web-Port-Geruch“)

- **Hamburger-Menü/Drawer** statt Tab Bar für Top-Level-Navigation (hig:tab-bars).
- **Aktionen in der Tab Bar** (z. B. „+“-Tab, der ein Formular öffnet) (hig:tab-bars#Best-practices).
- **Eigene Top-Bar** als `div`-artiger, opaker Farbbalken mit Logo statt Navigation Bar mit Titel; App-Name als Titel (hig:toolbars#Titles, hig:toolbars#Best-practices).
- **Text-Button „Zurück“** oder Back-Pfeil-Eigenbau ohne Swipe-back (hig:toolbars#Navigation).
- **Fixe px-Layouts** / Breakpoints nach Gerätebreite statt Size Classes und Safe Areas (hig:layout).
- **Fixe Schriftgrößen** (z. B. 14 px Fließtext), kein Dynamic Type, Text abgeschnitten mit „…“ (hig:typography).
- **Mini-Tap-Ziele** (Icons 20–24 pt ohne Hit-Area-Padding) (hig:accessibility#Mobility).
- **Modale Dialoge als zentrierte Overlay-Box** mit „X“ oben rechts statt Sheet mit Cancel/Done; Popover-Kacheln auf dem iPhone (hig:sheets, hig:popovers#iOS-iPadOS).
- **Toasts/Snackbars** für Fehler statt Alert; In-App-Badges als Fake-Notifications (hig:notifications).
- **Glass-Overload**: Liquid Glass auf Karten, Listenzellen, Hintergründen; mehrere farbig getönte Glass-Buttons (hig:materials#Liquid-Glass, hig:color#Liquid-Glass-color).
- **Opake Bar-Hintergründe** in Markenfarbe statt Inhalt darunter durchscheinen zu lassen (hig:toolbars#Best-practices).
- **Checkbox statt Switch** in Einstellungslisten bzw. Switch frei im Layout (hig:toggles#iOS-iPadOS).
- **Dropdown-`<select>`-Optik** statt Menü/Picker (hig:menus, hig:pickers).
- **Pull-to-refresh als einzige Aktualisierung** (hig:progress-indicators#iOS-iPadOS).
- **Splash Screen mit Logo** als Launch Screen (hig:launching#Launch-screens).
- **Emoji als Icons** (Quick Actions, Toolbar) statt SF Symbols (hig:home-screen-quick-actions).
- **Hover-abhängige Funktionen** (Tooltips, Hover-Menüs) ohne Touch-Äquivalent (hig:gestures#Best-practices).

---

## Widersprüche & Lücken im Spiegel

- **Keine Gerätetabelle/Safe-Area-Werte** in `layout.md`, obwohl das Change Log solche Spezifikationen nennt. Gerätespezifische Maße nur indirekt aus Widget-/Live-Activity-Tabellen.
- **Overflow:** `toolbars.md` verlangt auf iOS ein selbst angelegtes More-Menü und sagt, das System füge Overflow-Menüs nur in macOS/iPadOS automatisch hinzu; `designing-for-iphone-duo.md` verlangt dagegen, eigene Overflow-Menüs ins System-Overflow (`ToolbarOverflowMenu`) zu überführen. Für iPhone Duo gilt Letzteres; für klassische iPhones ist das Verhältnis offen.
- **Split View auf iPhone:** `multitasking.md#iOS` nennt nur Picture in Picture, `designing-for-iphone-duo.md` erwähnt dagegen Split-View-Multitasking auf dem Innendisplay.
- **Sheet-Schließen:** Text nennt Cancel leading; die Detent-Illustrationen zeigen einen runden Close-Button oben links. Beides ist leading, die Form (Text vs. Symbol) ist nicht eindeutig geregelt. `toolbars.md` bevorzugt Symbole (kein Text „Close“).
- **Detent medium** ist nur als „ungefähr halbe Höhe“ beschrieben, ohne Zahl.
