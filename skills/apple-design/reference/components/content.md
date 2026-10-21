# Content – Komponenten
> Quelle: Apple HIG, lokaler Spiegel (Stand 2026-10-21). Paraphrasiert. Belege: `(hig:<slug>)`, `(hig:<slug>#Anchor)`.

Komponenten, die Inhalte darstellen statt Aktionen auszulösen: Diagramme, Bilder, mehrzeiliger Text und eingebettete Webinhalte. Alle vier sind primär passiv; Interaktion (Tap, Klick) gehört in Buttons bzw. eigene Controls (hig:content).

- [Charts](#charts) – `charts`
- [Image views](#image-views) – `image-views`
- [Text views](#text-views) – `text-views`
- [Web views](#web-views) – `web-views`

## Charts
**Zweck:** Daten so visualisieren, dass wenige Kernaussagen schnell erfassbar sind und Entscheidungen stützen (hig:charts). **Plattformen:** ios, ipados, macos, watchos (auch tvos, visionos).
**Verwenden, wenn:** Trends, Vergleiche zwischen Kategorien, Anteile oder Ausreißer gezeigt werden sollen; Detailgestaltung siehe auch `charting-data` (Patterns). **Nicht verwenden, wenn:** eine einzelne Zahl oder ein Wert in einem Bereich reicht (→ Gauge), oder die Kernaussage nur per Interaktion erreichbar wäre.

**Anatomie (Begriffe):** Mark (Darstellung eines Werts), Plot area, Scale, Axis, Ticks, Grid lines, Labels, Legend, Titel/Untertitel/Annotations (hig:charts#Anatomy).

**Kernregeln:**
- Wähle den Mark-Typ nach Aussage: Bar für Kategorienvergleich/Anteile/Summen je Zeitraum, Line für Verläufe/Trends, Point für Einzelwerte, Zusammenhänge, Cluster und Ausreißer; kombiniere Typen (z. B. Line + Point), wenn es klärt (hig:charts#Marks).
- Entscheide bewusst zwischen festem und dynamischem Achsenbereich: fest, wenn Min/Max für alle Daten bedeutsam sind (z. B. Akku 0–100 %), dynamisch, wenn Werte stark streuen und die Plot area gefüllt werden soll (hig:charts#Axes).
- Lege die Untergrenze nach Mark-Typ fest: Null bei Bar Charts, nicht zwingend Null, wenn relevante Unterschiede weit von Null liegen (z. B. Herzfrequenz) (hig:charts#Axes).
- Nutze vertraute Tick-Folgen (0, 5, 10 statt 1, 6, 11) und dosiere Grid lines/Labels nach Nutzungskontext (hig:charts#Axes).
- Beschreibe Zweck und Hauptaussage vorab in Titel/Untertitel; fasse die Kernbotschaft in Klartext zusammen (hig:charts#Descriptive-content).
- Halte die Daten visuell dominant; Achsen und Texte liefern nur Kontext (hig:charts#Best-practices).
- Mach jeden Chart barrierefrei (VoiceOver, Audio Graphs) und verstecke kritische Informationen nie hinter Interaktion (hig:charts#Best-practices).
- Vergrößere bei kleinen Marks die Trefferfläche auf die ganze Plot area (Scrubbing); biete Tastatur/Switch Control einen logischen Pfad (z. B. entlang der X-Achse oder über Teilmengen) (hig:charts#Best-practices).
- Verlasse dich nie allein auf Farbe; ergänze Formen/Muster und trenne angrenzende Farbflächen (z. B. gestapelte Bars) durch Zwischenräume (hig:charts#Color).
- Schreibe Accessibility Labels zweckbezogen: Kontext + konkreter Wert, keine subjektiven Wörter, keine mehrdeutigen Formate/Abkürzungen, Bedeutung statt Aussehen beschreiben; sichtbare Achsen-/Tick-Labels vor Assistenztechnik verbergen (hig:charts#Enhancing-the-accessibility-of-a-chart).

**Plattform-Besonderheiten:**
- watchOS: keine komplexen Chart-Interaktionen; Glanceable-Infos zeigen, Details in der App einer anderen Plattform anbieten (hig:charts#watchOS).
- iOS, iPadOS, macOS, tvOS, visionOS: keine zusätzlichen Hinweise. Im Compact-Kontext Plot-Breite maximieren, Y-Achsen-Labels kurz halten, Einheiten ggf. in den Titel (hig:charts#Best-practices).

**Kennwerte:** keine im Spiegel (0 %/100 % nur als Beispiel für festen Achsenbereich).
**Umsetzung:** Swift Charts (`Chart`, Mark-Typen wie `BarMark`, `LineMark`, `PointMark`) – liefert Audio Graphs und Accessibility-Elemente je Mark standardmäßig (hig:charts#Enhancing-the-accessibility-of-a-chart). Änderungsbenachrichtigung für Assistenztechnik: `UIAccessibility.Notification` (UIKit), `NSAccessibility.Notification` (AppKit); Navigationspfad u. a. über `accessibilityRespondsToUserInteraction(_:)` (SwiftUI).
**Typische Fehler:**
- Bar Chart ohne Null-Basis bzw. Herzfrequenz-Chart mit erzwungener Null-Basis.
- Datenreihen nur über Farbe unterschieden; Accessibility Labels beschreiben Farben statt Bedeutung.
- Kernwert nur per Scrubbing erreichbar; Datenänderungen nur animiert, nicht anderweitig signalisiert (hig:charts#Best-practices).
- Zu viele Grid lines / lange Y-Labels, die im Compact-Layout Plot-Breite fressen.

## Image views
**Zweck:** Ein einzelnes Bild (oder eine animierte Bildsequenz) auf transparentem oder deckendem Hintergrund anzeigen; typischerweise nicht interaktiv (hig:image-views). **Plattformen:** ios, ipados, macos, watchos (auch tvos, visionos).
**Verwenden, wenn:** der Hauptzweck die reine Bildanzeige ist (PNG, JPEG, PDF u. a.) (hig:image-views#Content). **Nicht verwenden, wenn:** das Bild klickbar sein soll (→ Button mit Bild / Image button), ein Icon gebraucht wird (→ SF Symbols / Interface-Icon), oder es in macOS editierbar sein soll (→ Image well) (hig:image-views#Best-practices).

**Kernregeln:**
- Setze Image views nur für reine Darstellung ein; für seltene interaktive Bilder einen System-Button mit Bild konfigurieren statt Button-Verhalten nachzubauen (hig:image-views#Best-practices).
- Nutze für Icons SF Symbols oder Template-Icons – sie übernehmen Akzentfarben (hig:image-views#Best-practices).
- Sichere Kontrast bei Text über Bildern (z. B. Textschatten oder Hintergrundebene) (hig:image-views#Content).
- Halte alle Bilder einer Animationssequenz gleich groß, idealerweise vorskaliert auf die View-Größe (hig:image-views#Content).

**Plattform-Besonderheiten:**
- iOS, iPadOS: keine zusätzlichen Hinweise.
- macOS: editierbares Bild → Image well; klickbares Bild → Image button (hig:image-views#macOS).
- watchOS: Animationen bevorzugt mit SwiftUI; alternativ WatchKit (`WKImageAnimatable`) (hig:image-views#watchOS).
- (tvOS: Layered images mit Tiefenwirkung; visionOS: 2D-, stereoskopische und Spatial Photos, RealityKit `ImagePresentationComponent`) (hig:image-views#tvOS), (hig:image-views#visionOS).

**Kennwerte:** keine im Spiegel.
**Umsetzung:** SwiftUI `Image`; UIKit `UIImageView`; AppKit `NSImageView`.
**Typische Fehler:**
- Tap-Gesture auf Image view statt Button.
- Bitmap-Icons statt SF Symbols (kein Tint, keine Skalierung).
- Unlesbarer Text auf unruhigem Foto ohne Kontrastmaßnahme.

## Text views
**Zweck:** Mehrzeiligen, formatierten Text anzeigen, optional editierbar, mit Scrollen bei Überlänge (hig:text-views). **Plattformen:** ios, ipados, macos, watchos (auch tvos, visionos).
**Verwenden, wenn:** Text lang, editierbar oder speziell formatiert ist (hig:text-views#Best-practices). **Nicht verwenden, wenn:** nur wenig Text angezeigt wird (→ Label) oder kurze Eingabe gebraucht wird (→ Text field).

**Kernregeln:**
- Wähle Text view nur für langen/formatierten/editierbaren Text; sonst Label bzw. Text field (hig:text-views#Best-practices).
- Halte Text lesbar trotz Gestaltungsfreiheit; unterstütze Dynamic Type und teste mit Bedienungshilfen wie fettem Text (hig:text-views#Best-practices).
- Mach nützlichen Text (Fehlermeldung, Seriennummer, IP-Adresse) auswählbar und kopierbar (hig:text-views#Best-practices).
- Zeige in iOS/iPadOS den zum Inhalt passenden Keyboard-Typ (hig:text-views#iOS-iPadOS).
- Standard: führende Ausrichtung und System-Label-Farbe; bei editierbarer View erscheint in iOS/iPadOS/visionOS die Tastatur bei Auswahl (hig:text-views).

**Plattform-Besonderheiten:**
- iOS, iPadOS: passenden Keyboard-Typ wählen, siehe `virtual-keyboards` (hig:text-views#iOS-iPadOS).
- macOS, watchOS: keine zusätzlichen Hinweise.
- (tvOS: Text view nur zur Anzeige; editierbarer Text über Text fields) (hig:text-views#tvOS).

**Kennwerte:** keine im Spiegel.
**Umsetzung:** SwiftUI `Text` (Anzeige; laut Spiegel als Entsprechung genannt – für editierbaren mehrzeiligen Text ist in SwiftUI `TextEditor` üblich, im Spiegel nicht erwähnt); UIKit `UITextView`; AppKit `NSTextView`.
**Typische Fehler:**
- Text view für einzeilige Eingabe statt Text field.
- Feste Schriftgrößen ohne Dynamic Type.
- Fehlercodes/IDs nicht kopierbar.

## Web views
**Zweck:** Reichhaltige Webinhalte (eingebettetes HTML, Websites) direkt in der App laden und anzeigen, z. B. HTML-Mails (hig:web-views). **Plattformen:** ios, ipados, macos (auch visionos); nicht unterstützt in tvOS, watchOS.
**Verwenden, wenn:** Nutzer kurz Webinhalte sehen sollen, ohne den App-Kontext zu verlassen. **Nicht verwenden, wenn:** ein eigener Browser nachgebaut werden soll – Safari ist der primäre Weg zum Surfen (hig:web-views#Best-practices).

**Kernregeln:**
- Biete Vor-/Zurück-Navigation samt Bedienelementen an, wenn mehrere Seiten besucht werden können – sie ist nicht standardmäßig aktiv (hig:web-views#Best-practices).
- Baue keinen Safari-Ersatz mit Web views (hig:web-views#Best-practices).
- Nutze Web views für kurze, kontextgebundene Webinhalte (hig:web-views#Best-practices).
- Plane keine Web views für watchOS/tvOS ein (hig:web-views#Platform-considerations).

**Plattform-Besonderheiten:** iOS, iPadOS, macOS, visionOS: keine zusätzlichen Hinweise; tvOS/watchOS nicht unterstützt.
**Kennwerte:** keine im Spiegel.
**Umsetzung:** WebKit `WKWebView` (laut Spiegel). Unklar/nicht im Spiegel: SwiftUI-eigene Web-View-API.
**Typische Fehler:**
- Mehrseitige Navigation ohne Zurück-Button.
- In-App-Browser mit Adressleiste/Tabs statt Übergabe an Safari.
