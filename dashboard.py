import imports_download
import dash
import pandas as pd 
from dash import dcc
from dash import html
import os
from histogram import create_graph
from map import create_maps
from api_csv import api_csv

FILENAME = "us_tornado_dataset_1950_2021.csv"
api_csv_executed = False
imports_download_executed = False

app = dash.Dash(__name__)

def api_csv_execute():
    global api_csv_executed
    if not api_csv_executed:
        api_csv()
        api_csv_executed = True

def set_layout(app) : 
    df = pd.read_csv(FILENAME)
    initial_years = [1950, 1951]
    app.layout = html.Div(
        children=[
            html.H1(children='''
                Dashboard sur les tornades aux États-Unis entre 1950 et 2021
            '''),
            
            html.Div(children='''
            CONSIGNE DASHBOARD
            '''),

            dcc.Graph(
                id='main_graph',
                figure=create_graph(FILENAME, initial_years)
            ),

            dcc.RangeSlider(
                id='year-slider',
                min=df['yr'].min(),
                max=df['yr'].max(),
                step=1,
                value=initial_years,
                marks={str(year): str(year) for year in range(df['yr'].min(), df['yr'].max() + 1)},
            ),
            
            html.Iframe(
                srcDoc=open('map_tornado_path.html', 'r').read(),
                width='50%',
                height='400px',
            ),

            html.Div(children='''
            Carte du trajet des tornades de 2010 à 2015
            '''),

            html.Iframe(
                srcDoc=open('map_tornado_choropleth.html', 'r').read(),
                width='50%',
                height='400px',
            ),

            html.Div(children='''
            Carte de la répartition des tornades en fonction des États.
            '''),
        ]
    )

api_csv_execute()

create_maps()

set_layout(app)

@app.callback(
    dash.dependencies.Output('main_graph', 'figure'),
    [dash.dependencies.Input('year-slider', 'value')]
)

def update_graph(selected_years):
    return create_graph(FILENAME, selected_years)

if __name__ == '__main__':
    app.run_server(debug=True)