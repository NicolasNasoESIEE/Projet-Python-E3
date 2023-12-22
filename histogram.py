import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Fonction pour créer un graphique avec deux axes y (nombre total de tornades et magnitude moyenne) pour les années sélectionnées
def create_graph(filename, selected_years):

    df = pd.read_csv(filename)
    df = df[df['mag'] >= 0]
    df_filtered = df[df['yr'].between(selected_years[0], selected_years[1])]
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    df_graph = df_filtered.groupby('yr').agg({'st': 'count', 'mag': 'mean'}).reset_index()
    df_graph.columns = ['Year', 'Total Tornadoes', 'Average Magnitude']

    fig.add_trace(
        go.Scatter(x=df_graph['Year'], y=df_graph['Total Tornadoes'], name="Nombre total de tornades"),
        secondary_y=False,
    )

    fig.add_trace(
        go.Scatter(x=df_graph['Year'], y=df_graph['Average Magnitude'], name="Magnitude moyenne des tornades"),
        secondary_y=True,
    )

    fig.update_layout(
        title_text=f"Nombre total et magnitude moyenne des tornades pour les années {selected_years}"
    )

    fig.update_xaxes(title_text="Année")
    fig.update_yaxes(title_text="<b>Nombre total de tornades</b>", secondary_y=False)
    fig.update_yaxes(title_text="<b>Magnitude moyenne des tornades</b>", secondary_y=True)
    
    return fig


# Fonction pour créer un histogramme du nombre de décès pour les années sélectionnées
def create_bar(filename, selected_years):

    df = pd.read_csv(filename)
    df_filtered = df[df['yr'].between(selected_years[0], selected_years[1])]
    deces_par_annees = df_filtered.groupby('yr')['fat'].sum().reset_index()
    deces_par_annees.columns = ['Année', 'décès']
    
    fig = go.Figure(go.Bar(x=deces_par_annees['Année'], y=deces_par_annees['décès']))

    fig.update_layout(
        xaxis_title='Année',
        yaxis_title='Nombre de décès',
        title_text=f'Nombre de décès pour les années {selected_years}'
    )

    return fig