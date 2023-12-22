import pandas as pd
from dash.dependencies import Input, Output

# fichier projet
from histogram import create_graph, create_bar
from map import create_maps, create_map_tornado_path

# Callback pour mettre à jour le graph et l'histogramme
def set_callback(app, filename):
    @app.callback(
        Output('main_graph', 'figure'),
        Output('main_chart',"figure"),
        [Input('year-slider', 'value')]
    )
    def update_graph(selected_years):
        return create_graph(filename, selected_years), create_bar(filename, selected_years)


    # Callback pour mettre à jour les cartes
    @app.callback(
        Output('map_path', 'srcDoc'),
        [Input('year-dropdown', 'value')]
    )
    def update_map(selected_year):
        df = pd.read_csv(filename)
        create_map_tornado_path(df[df['yr'] == selected_year], selected_year)
        with open('map_tornado_path.html', 'r') as file:
            map_html_content = file.read()
        return map_html_content

