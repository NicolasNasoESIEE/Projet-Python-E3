import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from matplotlib.widgets import Slider

# Charger les données depuis le fichier CSV
df = pd.read_csv("us_tornado_dataset_1950_2021.csv")

# Convertir la colonne 'date' en format datetime
df['date'] = pd.to_datetime(df['date'])

# Créer une figure avec des axes partagés
fig, ax1 = plt.subplots()

# Ajouter un axe y à droite
ax2 = ax1.twinx()

# Fonction pour mettre à jour le graphique en fonction de l'année sélectionnée
def update(val):
    year = int(slider.val)
    selected_data = df[df['date'].dt.year == year]
    grouped_data = selected_data.groupby('date').agg({'mag': 'mean', 'yr': 'count'})

    # Mettre à jour les données des axes
    ax1.clear()
    ax1.plot(grouped_data.index, grouped_data['mag'], 'b-', label='Magnitude moyenne')
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Magnitude moyenne', color='b')
    ax1.tick_params('y', colors='b')
    ax1.xaxis.set_major_locator(MaxNLocator(nbins=6))
    
    ax2.clear()
    ax2.bar(grouped_data.index, grouped_data['yr'], color='r', alpha=0.5, label='Nombre de tornades')
    ax2.set_ylabel('Nombre de tornades', color='r')
    ax2.tick_params('y', colors='r')

    # Mettre à jour le titre du graphique
    plt.title(f'Données pour l\'année {year}')

# Ajouter un slider pour sélectionner l'année
ax_slider = plt.axes([0.1, 0.01, 0.8, 0.03])
slider = Slider(ax_slider, 'Année', df['yr'].min(), df['yr'].max(), valinit=df['yr'].min(), valstep=1)
slider.on_changed(update)

# Afficher le graphique initial
update(None)

# Afficher le graphique interactif
plt.show()
