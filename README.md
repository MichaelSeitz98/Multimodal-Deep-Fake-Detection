# Mulitmodale Fake Review Detektion 

Dieses Projekt beschäftigt sich mit der Erkennung von gefälschten Bewertungen (Fake-Reviews) auf Online-Plattformen. Hierbei wird ein multi-modaler Ansatz verfolgt, der auf verschiedenen Modalitäten wie Text, Bild und Metadaten basiert.

![Artefakt Übersicht](02_Images/graphics/artefact_uebersicht_v4.jpg)




## Wichtige Notebooks:

1. `nb_generate_dataset.ipynb`: In diesem Notebook werden relevante Informationen aus den Daten extrahiert, Daten herausgefiltert und Basissätze (base_) generiert, die als Grundlage für weitere Verarbeitungsschritte dienen.

2. `nb_generate_deepfaces.ipynb`: Auf Basis der Kategorie aus Notebook 1 werden hier auf allen Modalitäten Fake-Reviews generiert. Hier werden der echte Datensatz `base_....csv` und der gefälschte Datensatz `fake_base_gpt_3_...` zusammengeführt zu `merged_fake_real.csv`. Dieser Datensatz dient als neue Ausgangsbasis für die Detektion.

3. `nb_feature_extraction.ipynb`: Hier werden die Features für alle Modalitäten extrahiert und im Datensatz `features_enrichted[..].csv` gespeichert. Dieser Datensatz wird für die Detektion herangezogen.

4. `nb_fake_detection.ipnyb`: Zuerst wird der Datensatz in Trainings-, Validierungs- und Testdatensatz aufgeteilt (`detection_train.csv`, `detection_val.csv` und `detection_test.csv`). Anschließend werden XGBoost, Random Forest und TabNet trainiert und die Hyperparameter anhand des Validierungsdatensatzes optimiert. Abschließend wird das Modell evaluiert.

## Ergänzende Notebooks:

5. `nb_generated_gpt3_finetune_datasets.ipynb`: In diesem Notebook werden verschiedene GPT3 Finetunes vorbereitet und dafür benötigte Datensätze erzeugt.

6. `nb_frontend_optional_showcase_v0.ipynb`: Eventuell wird hier für die Präsentation anhand einer prototypischen Frontend das Artefakt vorgestellt. Dieses Notebook ist noch nicht fertiggestellt.


# Datensätze 

