import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

FILENAME = "us_tornado_dataset_1950_2021.csv"

def create_graph(FILENAME,selected_years) :
    df = pd.read_csv(FILENAME)

    df['mo'] = pd.to_datetime(df['date']).dt.month

    df_filtered = df[df['yr'].between(selected_years[0], selected_years[1])]
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    df_graph = df_filtered.groupby(['yr', 'mo']).agg({'st': 'count', 'mag': 'mean'}).reset_index()
    df_graph.columns = ['Year', 'Month', 'Total Tornadoes', 'Average Magnitude']

    fig.add_trace(
        go.Scatter(x=df_graph['Month'] + (df_graph['Year'] - selected_years[0]) * 12, y=df_graph['Total Tornadoes'], name="Nombre total de tornades"),
        secondary_y=False,
    )

    fig.add_trace(
        go.Scatter(x=df_graph['Month'] + (df_graph['Year'] - selected_years[0]) * 12, y=df_graph['Average Magnitude'], name="Magnitude moyenne des tornades"),
        secondary_y=True,
    )

    fig.update_layout(
            title_text=f"Nombre total et magnitude moyenne des tornades pour les années {selected_years}"
    )

    fig.update_xaxes(title_text="mois total")

    fig.update_yaxes(title_text="<b>Nombre total de tornades</b>", secondary_y=False)
    fig.update_yaxes(title_text="<b>Magnitude moyenne des tornades</b>", secondary_y=True)
    
    return fig