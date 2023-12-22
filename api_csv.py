import os
import json

# Définition des informations d'authentification Kaggle
DATA = {"username": "nicolasnaso", "key": "dfd72dc597bb350a527001eec6b7c699"}

# Fonction pour télécharger le CSV sur Kaggle
def api_csv(filename):

    if os.path.exists(filename):
        os.remove(filename)

    # Récupérer le nom d'utilisateur de l'environnement
    username = os.environ['USERNAME']
    
    # Définir le chemin du fichier JSON Kaggle
    json_path = 'C:\\Users\\' + username + '\\.kaggle'
    
    # Vérifier si le dossier .kaggle existe, sinon le créer
    if not os.path.exists(json_path):
        os.mkdir(json_path)
    
    # Écrire les informations d'authentification dans le fichier JSON
    with open(json_path + "\\kaggle.json", 'w') as f:
        json.dump(DATA, f)
    
    # Télécharger le jeu de données Kaggle
    os.system('kaggle datasets download -d danbraswell/us-tornado-dataset-1950-2021')
    
    # Extraire le contenu du fichier zip téléchargé et supprimer de ce dernier après décompression
    os.system('tar -xf us-tornado-dataset-1950-2021.zip')
    os.remove("us-tornado-dataset-1950-2021.zip")

