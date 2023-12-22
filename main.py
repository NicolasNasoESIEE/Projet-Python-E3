import imports_download
import dash
import pandas as pd
import os
import webbrowser
from threading import Timer

#fichier du projet
from api_csv import api_csv
from layout import set_layout
from callback import set_callback


# Chemin fichier CSV
FILENAME = "us_tornado_dataset_1950_2021.csv"

# Création web dash 
app = dash.Dash(__name__)

# API pour récupérer le dataset sur kaggle 
api_csv(FILENAME)

# Définition de la mise en page du dashboard 
set_layout(app, FILENAME)

# Définition du callback pour update le dashboard
set_callback(app, FILENAME)

# Ouvre le navigateur et démarrer l'application web
def open_browser():
    webbrowser.open_new('http://127.0.0.1:8050/')

if __name__ == "__main__":
    Timer(1, open_browser).start()
    app.run_server(debug=True)
