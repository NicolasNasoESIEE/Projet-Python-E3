import imports_download
import dash
from dash.dependencies import Input, Output
import pandas as pd
import os
import webbrowser
from threading import Timer

#fichier du projet
from histogram import create_graph, create_bar
from map import create_maps, create_map_tornado_path
from api_csv import api_csv
from layout import set_layout


# Chemin fichier CSV
FILENAME = "us_tornado_dataset_1950_2021.csv"

# Création web dash 
app = dash.Dash(__name__)

api_csv(FILENAME)

# Définition de la mise en page du dashboard 
set_layout(app, FILENAME)

# Callback pour mettre à jour les graphiques
@app.callback(
    Output('main_graph', 'figure'),
    Output('main_chart',"figure"),
    [Input('year-slider', 'value')]
)
def update_graph(selected_years):
    return create_graph(FILENAME, selected_years), create_bar(FILENAME, selected_years)


# Callback pour mettre à jour les cartes
@app.callback(
    Output('map_path', 'srcDoc'),
    [Input('year-dropdown', 'value')]
)
def update_map(selected_year):
    df = pd.read_csv(FILENAME)
    create_map_tornado_path(df[df['yr'] == selected_year], selected_year)
    with open('map_tornado_path.html', 'r') as file:
        map_html_content = file.read()
    return map_html_content

# Ouvre le navigateur et démarrer l'application web
def open_browser():
    webbrowser.open_new('http://127.0.0.1:8050/')



if __name__ == "__main__":
    Timer(1, open_browser).start()
    app.run_server(debug=True)
