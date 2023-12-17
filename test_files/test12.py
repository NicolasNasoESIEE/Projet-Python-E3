import dash
from dash import dcc
from dash import html
import plotly.graph_objects as go
import pandas as pd 
from plotly.subplots import make_subplots

FILENAME = "us_tornado_dataset_1950_2021.csv"


def create_chart(df, selected_years):
    # Filter data based on the selected range of years
    df_filtered = df[df['yr'].between(selected_years[0], selected_years[1])]

    fig = make_subplots(specs=[[{"secondary_y": True}]])

    # Group by month across all selected years
    df_graph = df_filtered.groupby('mo').agg({'st': 'count', 'mag': 'mean'}).reset_index()
    df_graph.columns = ['Month', 'Total Tornadoes', 'Average Magnitude']

    # Add traces
    fig.add_trace(
        go.Scatter(x=df_graph['Month'], y=df_graph['Total Tornadoes'], name="Total Tornadoes"),
        secondary_y=False,
    )

    fig.add_trace(
        go.Scatter(x=df_graph['Month'], y=df_graph['Average Magnitude'], name="Average Magnitude"),
        secondary_y=True,
    )

    # Add figure title
    fig.update_layout(
        title_text=f"Tornado Statistics for Years {selected_years[0]} to {selected_years[1]}"
    )

    # Set x-axis title
    fig.update_xaxes(title_text="Month")

    # Set y-axes titles
    fig.update_yaxes(title_text="<b>Total Tornadoes</b>", secondary_y=False)
    fig.update_yaxes(title_text="<b>Average Magnitude</b>", secondary_y=True)

    return fig


# Création de l'application Dash
app = dash.Dash(__name__)

# Load the DataFrame
df = pd.read_csv(FILENAME)

# Initial year range for the chart
initial_years = [1950, 1984]  # You can set your desired initial range here

# Mise en page du tableau de bord
app.layout = html.Div(
    children=[
        html.H1(children='Mon Tableau de Bord'),

        html.Div(children='''
            Analyse de données en utilisant Dash : exemple simple.
        '''),

        # Range Slider for selecting the year range
        dcc.RangeSlider(
            id='year-range-slider',
            min=df['yr'].min(),
            max=df['yr'].max(),
            step=1,
            marks={str(year): str(year) for year in range(df['yr'].min(), df['yr'].max() + 1)},
            value=initial_years,
            
        ),

        # Composant graphique interactif
        dcc.Graph(
            id='example-graph',
            # Initial figure with the selected year range
            figure=create_chart(df, initial_years)
        ),
    ]
)


# Callback to update the chart based on the selected year range
@app.callback(
    dash.dependencies.Output('example-graph', 'figure'),
    [dash.dependencies.Input('year-range-slider', 'value')]
)
def update_chart(selected_years):
    return create_chart(df, selected_years)


if __name__ == '__main__':
    app.run_server(debug=True)