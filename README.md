# Détecteur d'anomalies SMTP

Ce projet utilise un script Python pour détecter les anomalies dans les activités de messagerie SMTP, en se basant sur des données historiques. L'objectif est d'identifier les comportements suspects qui pourraient indiquer des cyber-attaques.

## Fonctionnement du script `predict_smtp.py`

1. **Chargement des données** : Le script lit les données à partir du fichier `smtp.csv`, qui doit contenir des enregistrements d'activités SMTP.

2. **Nettoyage des données** : Suppression de plusieurs colonnes jugées non pertinentes pour l'analyse.

3. **Encodage** : Les colonnes catégorielles (`helo`, `mailfrom`, etc.) sont encodées numériquement pour permettre leur traitement par le modèle.

4. **Imputation** : Les valeurs manquantes dans les colonnes numériques sont remplacées par la médiane de la colonne concernée.

5. **Préparation des données** : Construction d'une matrice de caractéristiques `X` à partir des données nettoyées et préparées.

6. **Modélisation** : Entraînement d'un modèle `IsolationForest` pour identifier les anomalies.

7. **Prédiction** : Le script prédit les anomalies dans le jeu de données et les ajoute au DataFrame sous la colonne `Prediction`.

8. **Résultats** : Les données sont divisées en anomalies (potentielles cyber-attaques) et normales, puis affichées.

## Fichier `smtp.csv`

Le fichier CSV doit suivre une structure spécifique, avec des colonnes pour les timestamps, adresses IP, ports, protocole utilisé, et divers attributs SMTP tels que `helo`, `mailfrom`, `path`, `user_agent`, `fuids`, et `is_webmail`.

## Installation des dépendances

Avant d'exécuter le script, assurez-vous d'avoir installé les dépendances nécessaires :

```bash
pip install pandas scikit-learn
```

## Exécution du script

Lancez le script en utilisant Python 3 :

```bash
python predict_smtp.py
```

Assurez-vous que le fichier `smtp.csv` se trouve dans le même répertoire que le script ou modifiez le chemin d'accès dans le code source.
