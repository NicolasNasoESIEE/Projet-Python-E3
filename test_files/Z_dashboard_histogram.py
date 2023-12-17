import dash
from dash import dcc
from dash import html
import plotly.express as go
import pandas as pd 
from plotly.subplots import make_subplots

FILENAME = "us_tornado_dataset_1950_2021.csv"
# Création de l'application Dash


# Exécution de l'application en mode serveur

def create_chart(FILENAME) :
    data = pd.read_csv(FILENAME)
    df = data.copy() # make a copy and continue over it.
    df.info() # general information


#filtre des magnétudes negatives 
# magn_filter = df[df['mag'] > 0]
# magn_filter.plot( kind="scatter", x="date", y="mag",label = 'courbe de magn')  
# plt.title("magnétude en fonction des années")
# plt.show()

#nombre de tornades par année.
    df_positives = df[df['mag'] > 0]
    tornades_par_annee = df['yr'].value_counts().sort_index().reset_index()
    tornades_par_annee.columns = ['Année', 'Nombre de tornades']
    moyenne_magnitude_par_annee = df_positives.groupby('yr')['mag'].mean().reset_index()
    moyenne_magnitude_par_annee.columns = ['Année', 'Magnitude moyenne']
# Tracer le graphique avec Matplotlib
# plt.bar(tornades_par_annee.index, tornades_par_annee.values, color='skyblue', edgecolor='black')
# plt.show()

#tracer avec plotly
    fig = go.scatter(tornades_par_annee, x='Année', y='Nombre de tornades',
             labels={'Nombre de tornades': 'Nombre de tornades'},
             title='Nombre de tornades par année',
             )

# Grouper par année et calculer la magnitude moyenne des tornades positives
   

# Tracer le graphique avec Plotly Express
    fig1 = go.scatter(moyenne_magnitude_par_annee, x='Année', y='Magnitude moyenne',
    labels={'Magnitude moyenne': 'Magnitude moyenne'},
    title='Magnitude moyenne des tornades par année')

    figure_combinee = make_subplots(rows=1, cols=2, subplot_titles=('Nombre de tornades par année','Magnitude moyenne des tornades par année '))

#ajouter les données au graphs
    for trace in fig.data:
        figure_combinee.add_trace(trace, row=1, col=1)

    for trace in fig1.data:
        figure_combinee.add_trace(trace, row=1, col=2)

# Afficher le graphique interactif
    #fig.show()
    #fig1.show()
    #figure_combinee.show()
    return figure_combinee

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