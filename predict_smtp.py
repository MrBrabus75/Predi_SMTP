import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import SimpleImputer

# Charger les données
data = pd.read_csv('smtp.csv')  # Assurez-vous d'utiliser le bon chemin vers le fichier

# Supprimer les colonnes inutiles
data = data.drop(['rcptto', 'date', 'from', 'to', 'in_reply_to', 'subject', 'x_originating_ip', 'first_received', 'second_received', 'last_reply', 'tls', 'trans_depth'], axis=1)

# Encoder les colonnes catégorielles
categorical_cols = ['helo', 'mailfrom', 'path', 'user_agent', 'fuids', 'is_webmail']
numerical_cols = ['ts', 'id.orig_p', 'id.resp_p', 'proto']

for col in categorical_cols:
    le = LabelEncoder()
    data[col] = le.fit_transform(data[col].astype(str))  # Convertir en string pour le LabelEncoder
    data[col] = data[col].replace(-1, len(le.classes_), inplace=False)  # Remplacer -1 par une nouvelle catégorie

# Imputer les valeurs manquantes dans les colonnes numériques avec la médiane
imputer = SimpleImputer(strategy='median')
data[numerical_cols] = imputer.fit_transform(data[numerical_cols])

# Créer une matrice X avec les données préparées
X = data[categorical_cols + numerical_cols]

# Entraîner le modèle IsolationForest
model = IsolationForest(contamination=0.1)
model.fit(X)

# Prédire les anomalies
y_pred = model.predict(X)

# Ajouter les prédictions au DataFrame
data['Prediction'] = y_pred

# Filtrer les anomalies (cyber-attaques potentielles) et les normales
anomalies = data[data['Prediction'] == -1]
normales = data[data['Prediction'] == 1]

print("Anomalies:")
print(anomalies)
print("\nNormales:")
print(normales)
