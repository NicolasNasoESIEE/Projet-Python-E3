#fichiers du projet
import imports_download
from api_csv import api_csv
from layout import set_layout
from callback import set_callback

import dash
import os
import webbrowser
from threading import Timer


# Chemin fichier CSV
FILENAME = "us_tornado_dataset_1950_2021.csv"

# Création du dashboard
app = dash.Dash(__name__)

# Fonction pour télécharger le CSV sur Kaggle
api_csv(FILENAME)

# Mise en page du dashboard 
set_layout(app, FILENAME)

# Callback pour update le dashboard
set_callback(app, FILENAME)

# Ouvre le navigateur et affiche le dashboard
def open_browser():
    webbrowser.open_new('http://127.0.0.1:8050/')

if __name__ == "__main__":
    Timer(1, open_browser).start()
    app.run_server(debug=True)
