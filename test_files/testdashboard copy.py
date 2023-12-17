import dash
from dash import dcc
from dash import html
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd 
from plotly.subplots import make_subplots

FILENAME = "us_tornado_dataset_1950_2021.csv"
# Création de l'application Dash



# Exécution de l'application en mode serveur

def create_chart(FILENAME) :
    data = pd.read_csv(FILENAME)
    df = data.copy() # make a copy and continue over it.
    #df.info() # general information


#filtre des magnétudes negatives 
# magn_filter = df[df['mag'] > 0]
# magn_filter.plot( kind="scatter", x="date", y="mag",label = 'courbe de magn')  
# plt.title("magnétude en fonction des années")
# plt.show()


    fig5 = make_subplots(specs=[[{"secondary_y": True}]])

#nombre de tornades par année.
    df_positives = df[df['mag'] > 0]
    tornades_par_annee = df['yr'].value_counts().sort_index().reset_index()
    tornades_par_annee.columns = ['Année', 'Nombre de tornades']
    moyenne_magnitude_par_annee = df_positives.groupby('yr')['mag'].mean().reset_index()
    moyenne_magnitude_par_annee.columns = ['Année', 'Magnitude moyenne']
    y1_data = ['Magnitude moyenne']
    y2_data = ['Nombre de tornades']
    

# Tracer le graphique avec Matplotlib
# plt.bar(tornades_par_annee.index, tornades_par_annee.values, color='skyblue', edgecolor='black')
# plt.show()

#tracer avec plotly
    # fig = px.scatter(tornades_par_annee, x='Année', y='Nombre de tornades',
    #          labels={'Nombre de tornades': 'Nombre de tornades'},
    #          title='Nombre de tornades par année',
    #          )



    

# Grouper par année et calculer la magnitude moyenne des tornades positives


    df_graph2 = df.groupby('yr').agg({'st': 'count', 'mag': 'mean'}).reset_index()
    df_graph2.columns = ['Year', 'Total Tornadoes', 'Average Magnitude']


# Add traces
    fig5.add_trace(
        go.Line(x=df_graph2['Year'], y=df_graph2['Total Tornadoes'], name="Total Tornadoes"),
        secondary_y=False,
    )

    fig5.add_trace(
        go.Line(x=df_graph2['Year'], y=df_graph2['Average Magnitude'], name="Average Magnitude"),
        secondary_y=True,



    )

    # Add figure title
    fig5.update_layout(
            title_text="Double Y Axis Example"
        )

        # Set x-axis title
    fig5.update_xaxes(title_text="xaxis title")

        # Set y-axes titles
    fig5.update_yaxes(title_text="<b>primary</b> yaxis title", secondary_y=False)
    fig5.update_yaxes(title_text="<b>secondary</b> yaxis title", secondary_y=True)

# Tracer le graphique avec Plotly Express
    fig1 = px.scatter (df_graph2, x='Year', y=['Total Tornadoes','Average Magnitude'],
    labels={'Magnitude moyenne': 'Magnitude moyenne'},
    title='Magnitude moyenne des tornades par année')



    fig1.update_layout(
    yaxis=dict(title='Total Tornadoes', side='left'),
    yaxis2=dict(title='Average Magnitude', overlaying='y', side='right'),
    )

   



#ajouter les données au graphs
    

# Afficher le graphique interactif
    #fig.show()
    #fig1.show()
    #figure_combinee.show()
    return fig5

# Création de l'application Dash
app = dash.Dash(__name__)
fig = create_chart(FILENAME)
# Mise en page du tableau de bord
app.layout = html.Div(
    children=[
        html.H1(children='Mon Tableau de Bord'),
        
        html.Div(children='''
            Analyse de données en utilisant Dash : exemple simple.
        '''),
        
        # Composant graphique interactif
        dcc.Graph(
            id='example-graph',
            figure= fig
        )
    ]
)



if __name__ == '__main__':
    app.run_server(debug=True)