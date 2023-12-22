**Contexte :** 
L’objectif du mini projet est d’éclairer un sujet d’intérêt public (météo, environnement, politique, vie publique, finance, transports, culture, santé, sport, économie, agriculture, écologie, etc…) que vous choisissez librement. 
Vous utiliserez des données publiques Open Data, accessibles et non modifiées.

**liste des modules requis (requirements.txt) :** 
kaggle
dash
folium
branca
plotly
pandas
Timer

**User Guide :** 
*Installation :*
- récupérer le lien ssh du projet sur github
- cloner le dépot sur vscode
- se placer dans le répertoire du projet (bien vérifier le nom du dossier : Projet-Python-E3)
Le téléchargement des modules python est automatique au lancement du programme. 
Il faut parfois vérifier que la bonne version de python est utilisée (Barre de recherche VSCODE => >Python: Select Interpreter).
Le dashboard comprend : texte, graphique, histogramme, cartes, slider et menu déroulant.
Le slider permet de choisir l'intervalle des années pour afficher les données du graphique et de l'histogramme.
Le menu déroulant permet d'afficher la trajectoire des tornades de l'année choisi.

**Developper Guide:**
expliquer les fichiers et résumé ce qu'il font

**Présentation du dataset :**
le dataset répertorie de nombreuses données sur les tornades aux USA entre 1950 et 2021.
Données :
*yr*   - Année à 4 chiffres
*mn*   - Mois (1-12)
*dy*   - Jour du mois
*date* - Objet datetime (par exemple, 1950-01-01)
*st*   - État où la tornade a commencé ; abréviation à 2 chiffres
*mag*  - Echelle de Fujita (-9 si la magnitude est inconnue)
*inj*  - Nombre de blessés
*fat*  - Nombre de décès
*slat* - Latitude de départ en degrés décimaux
*slon* - Longitude de départ en degrés décimaux
*elat* - Latitude de fin en degrés décimaux (valeur de 0 si elle est manquante)
*elon* - Longitude de fin en degrés décimaux (valeur de 0 si elle est manquante)
*len*  - Longueur de la trajectoire en miles
*wid*  - Largeur en yards

**Rapport d'analyse :**

À l'aide des différents outils du dashboard (graphique, histogramme, cartes), on peut tirer plusieurs conclusions sur les données des tornades aux USA.
*Définition (Wikipédia) :* 
Une tornade est un tourbillon de vents extrêmement violents, prenant naissance à la base d'un nuage d'orage lorsque les conditions de cisaillement des vents sont favorables dans la basse atmosphère. 
De très faibles tornades peuvent également se développer sous des nuages d'averses.

*Analyse du graphique :*
Ce graphique montre le nombre de tornades par an ainsi que leur magnitude moyenne en fonction des années (de 1950 à 2021). 
On remarque que la magnitude des tornades décroît sur 71 ans passant de 1,2 en moyenne (entre 1955 et 1975) à 0,6 (entre 1990 et 2021) sur l'échelle de Fujita (certaines tornades n'ont pas de relevés de magnitude et n'apparaissent donc pas dans les données du graphique).
La magnitude moyenne décroît au plus bas jusqu'en 2000 où une légère hausse est présente jusqu'en 2021.
Les tornades sont donc moins violentes qu'il y a 70 ans (de dégâts importants à dégâts modérés).
Cependant, on remarque également que le nombre de tornades augmente chaque année allant de quelques centaines en 1950 à plus de 1000 au 21ème siècle.
Cet accroissement peut être expliqué par la montée progressive des températures et la modification des courants de l'air dans l'atmosphère. De plus on répertorie beaucoup de tornades aux USA car le pays possède une situation géographique qui favorise les mouvements d'airs chauds et froids.
En conclusion, la magnitude moyenne des tornades diminue mais leur nombre augmente, ce qui peut impliquer davantage de destruction et de pertes humaines. 

*Analyse de l'histogramme :*
Cet histogramme montre le nombre de décès suite aux tornades en fonction de l'année. 
On remarque que la moyenne du nombre de décès est d'une centaine de personnes par an. Cependant, certaines années montrent des catastrophes violentes comme en 1952, 1953, 1957, 1965, 1974 et 2011.
L'année 2011 a recensé près de 2000 tornades, ce qui pourrait expliquer les 553 morts.

*Analyse des cartes :*
On observe que les plaines connaissent davantage de tornades en raison de leur topographie plate, favorisant la formation de ces phénomènes météorologiques alors que les régions montagneuses ou accidentées en enregistrent généralement moins. 
Les tornades ont tendance à se déplacer d'ouest en est ou du sud au nord, suivant la direction des vents dominants. On remarque également que la trajectoire des tornades est relativement courtes, ne parcourant que quelques miles en moyenne.
Enfin, la fréquence élevée des tornades au Texas s'explique par la vaste étendue de l'État. 

