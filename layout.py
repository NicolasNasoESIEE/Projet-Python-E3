import pandas as pd 
from dash import dcc
from dash import html

# import fichiers projet
from histogram import create_graph, create_bar
from map import create_maps, create_map_tornado_path

def set_layout(app, filename):

    df = pd.read_csv(filename)
    initial_years = [df['yr'].min(), df['yr'].max()]

    # Création des cartes (HTML)
    create_maps(filename,1950)

    # Définition du layout du dashboard
    app.layout = html.Div(
        #style={'background-image': 'url("/assets/tornado.jpg")', 'background-size': 'cover'},
        style={'textAlign': 'center'},
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
                figure=create_graph(filename, initial_years)
            ),

            dcc.Graph(
                id='main_chart',
                figure=create_bar(filename, initial_years)
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
                 style={'width': '50%', 'margin': 'auto'},
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
