# Multimodal Review Generation and Detection


Online-Rezensionen tragen maßgeblich zur Kaufentscheidung von Konsument:innen bei.
Allerdings sind die Echtheit und Authentizität dieser Rezensionen nicht immer gegeben.
Teils lassen sich sog. Fake Reviews einfach identifizieren, aber teils ist dies auch nicht
möglich. Im Angesicht neuartiger Methoden der generativen künstlichen Intelligenz stellt
sich nun vielmehr die Frage nach der Echtheit der Rezensionen. Während populäre
generative Modelle wie ChatGPT in der Lage sind plausible Text nach Gusto in
Sekundenschnelle zu formulieren und dabei reaktiv auf Nutzereingaben zu reagieren,
können solche Applikationen derzeit noch keine multimodalen Inhalte generieren—sprich
schlüssige Samples bestehend aus mehreren zusammengehörenden Datenmodalitäten.
Gerade bei Rezensionen sind multimodale Inhalte bei Konsument:innen eine wichtige
Referenzquelle. Im Anbetracht der derzeitigen Entwicklung im Bereich der generativen
künstlichen Intelligenz ist abzusehen, dass zeitnahe solche Applikationen den Markt
erreichen und dabei auch für die massenweise Manipulation von Online-Rezensionen
eingesetzt werden.
Zentrales Ziel der Seminararbeit ist es somit ein IT-System für die Identifikation solcher
multimodaler Deepfakes zu entwickeln und evaluieren. Hierfür soll als Erstes ein geeigneter
Review-Datensatz als Datenbasis (Text, Bild und Tabellarisch) gewählt werden. Im
nächsten Schritt soll dieser dann mittels verschiedener state-of-the-art (SOTA)
Applikationen zur Generierung künstlicher Daten ebendieser Modalitäten augmentiert
werden. Im Anschluss soll mittels überwachter maschineller Lernverfahren die Genauigkeit
bei der Identifikation der Fake Reviews ermittelt werden und anschließend Implikationen für
die Zukunft abgeleitet werden.