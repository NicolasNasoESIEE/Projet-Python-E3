import imports_download
import dash
import pandas as pd 
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import os
import webbrowser
from threading import Timer
from histogram import create_graph, create_bar
from map import create_maps, create_map_tornado_path
from api_csv import api_csv


# Chemin fichier CSV
FILENAME = "us_tornado_dataset_1950_2021.csv"

# Création web dash 
app = dash.Dash(__name__)


# Mise en page du dashboard 
def set_layout(app):
    df = pd.read_csv(FILENAME)
    initial_years = [df['yr'].min(), df['yr'].max()]
    app.layout = html.Div(
        #style={'background-image': 'url("/assets/tornado.jpg")', 'background-size': 'cover'},
        children=[
            html.H1(children='''
                Dashboard sur les tornades aux États-Unis entre 1950 et 2021
            '''),

            html.H2(children='''
            Introduction au projet : 
            '''),

            html.H2(children='''
            L'objectif du mini projet est d'éclairer un sujet d'intérêt public (météo, environnement, politique, vie publique, finance, transports, culture, santé, sport, économie, agriculture, écologie, etc…) que vous choisissez librement.
            '''),

            html.H2(children='''
            Vous utiliserez des données publiques Open Data, accessibles et non modifiées.
            '''),

            dcc.Graph(
                id='main_graph',
                figure=create_graph(FILENAME, initial_years)
            ),

            dcc.Graph(
                id='main_chart',
                figure=create_bar(FILENAME, initial_years)
            ),

            dcc.RangeSlider(
                id='year-slider',
                min=df['yr'].min(),
                max=df['yr'].max(),
                step=1,
                value=initial_years,
                marks={str(year): str(year) for year in range(df['yr'].min(), df['yr'].max() + 1)},
            ),

            html.H3(children='''
            Intervalle entre les deux années selectionnées
            '''),

            html.H3(children='''
            On remarque que la magnitude moyenne des tornades diminue entre 1950 et 2021. 
            Cependant, le nombre total de tornades par année est de plus en plus elevé.
            '''),

            html.Iframe(
                id='map_path',
                srcDoc=open('map_tornado_path.html', 'r').read(),
                width='50%',
                height='400px',
            ),

            dcc.Dropdown(
                id='year-dropdown',
                options=[{'label': str(year), 'value': year} for year in range(df['yr'].min(), df['yr'].max() + 1)],
                value=df['yr'].min(),
                style={'width': '50%'},
            ),

            html.H3(children='''
            Carte du trajet des tornades de 2010 à 2015
            '''),

            html.Iframe(
                id='map_choropleth',
                srcDoc=open('map_tornado_choropleth.html', 'r').read(),
                width='50%',
                height='400px',
            ),

            html.H3(children='''
            Carte de la répartition des tornades en fonction des États.
            '''),
        ]
    )



api_csv(FILENAME)

create_maps(FILENAME,1950)

# Définition de la mise en page du dashboard 
set_layout(app)


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
