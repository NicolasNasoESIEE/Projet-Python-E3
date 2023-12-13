##################################################
################### IMPORTS ######################
##################################################

#import imports_download
import folium
import branca
import webbrowser
import csv
import pandas as pd
import numpy as np
import os
import shutil
import requests
import zipfile
import io

##################################################
#########VARIABLES & IMPORTS (LOCAL) #############
##################################################

FILENAME = "us_tornado_dataset_1950_2021.csv"

##################################################
############### MANIPULATION CSV #################
##################################################

def api_csv():
    os.remove(FILENAME)
    username = os.environ['USERNAME']
    json_path = 'C:\\Users\\'+username+'\\.kaggle'
    if not os.path.exists(json_path): 
        os.mkdir(json_path)
    shutil.copy('kaggle.json', json_path)
    os.system('kaggle datasets download -d danbraswell/us-tornado-dataset-1950-2021')
    os.system('tar -xf us-tornado-dataset-1950-2021.zip')
    os.remove("us-tornado-dataset-1950-2021.zip")

def api_csv_old():
    url = "https://storage.googleapis.com/kaggle-data-sets/3103925/5569891/compressed/us_tornado_dataset_1950_2021.csv.zip?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20231206%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20231206T121728Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=037a2ef1a8521a2727f23e5e3808cc06aac45d8e544a388481b186811c0410c830a20f050bb1b76eb6737275f9f64f5dcdd569e2d4b093de63ffd5bafe7ebb3e7b531b9b3f35ce6c7118b1ffb09d75d914a4ab8c0d0a0d036ac6a6ddbf00ab1e215eb836b067939f7d53ddc28560fb15406c2301ca24a888394f656d5dbe35e4736efb944a23e9465fc023213ee5094bb87508955ed195f31264d6ced50ec18d058896d7eac7e6c5c5c758066dd2d7060effa4ace8bd54e84dfeee91956e98320e35e627474bcfa7784990751f17ea2514bb7c53b2c1c9a9982eb15fa55ac4b02dfdd1618e37c59517f92dbde8a6fb5653ed7775b5a2e521dee41144412795f2"

    try:
        reponse = requests.get(url)
        with zipfile.ZipFile(io.BytesIO(reponse.content), 'r') as archive:
            archive.extractall('')
    except Exception as e:
        print(f"Erreur : {e}")

def read_file(filename):
    df = pd.read_csv(filename)
    return df

##################################################
############ AFFICHAGE/CREATION CARTE ############
##################################################


def create_map_old(data,filter) :

    lat = data['slat'].unique().tolist()
    lon = data['slon'].unique().tolist()
    flt = data[filter].unique().tolist()

    list_filter_tornados = []
    for i in range (len(data)) : 
        list_filter_tornados.append(flt[i])

    coords_USA = (38,-97)
    map = folium.Map(location=coords_USA, tiles='OpenStreetMap', zoom_start=4)

    folium.TileLayer('https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png',name='OpenTopoMap',attr='OpenTopoMap').add_to(map)

    folium.LayerControl().add_to(map)
    
    cm = branca.colormap.LinearColormap(['blue', 'red'], vmin=0, vmax=10)
    cm.caption = filter
    map.add_child(cm)
    
    #Affichage couleurs/nb tornades par état => Cartes choroplèthes

    #Marqueurs de tornades 
    for i in range(len(data)+1):
        #radius = data[i][2]
        #color = 100
        folium.CircleMarker(
            location = (lat, lon),
            radius = 1,
            color = cm(float(flt[i])),
            fill = False,
            fill_color = cm(float(flt[i])),
            fill_opacity = 0.4
        ).add_to(map)

    map.save(outfile='map.html')


def create_map(data):

    os.remove("map.html")

    data_filtered = data[(data['yr'] >= 2010) & (data['yr'] <= 2015)]

    geo_json_data = requests.get(
        "https://raw.githubusercontent.com/python-visualization/folium-example-data/main/us_states.json"
    ).json()

    map = folium.Map(location=[38, -97], tiles='OpenStreetMap', zoom_start=4)

    cm = branca.colormap.LinearColormap(['blue', 'red'], vmin=data['len'].min(), vmax=data['len'].max())

    cm.caption = "distance tornade (miles)"

    for index, row in data_filtered.iterrows():
        if(row['elat'] != 0 or row['elon'] != 0):
            color = cm(row['len'])
            folium.PolyLine(
            [(row['slat'], row['slon']), (row['elat'], row['elon'])],
            color=color,
            weight=2.5,
            opacity=1,
            popup=f"Mag: {row['mag']}, Wid: {row['wid']}, Len: {row['len']}"
            ).add_to(map)

    folium.GeoJson(geo_json_data).add_to(map)

    folium.TileLayer('https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png', name='OpenTopoMap', attr='OpenTopoMap').add_to(map)

    folium.LayerControl().add_to(map)

    map.add_child(cm)

    map.save('map.html')


def display_map():
    webbrowser.open('map.html') 


##################################################
################### MAIN #########################
##################################################

def main():
    api_csv()
    data = read_file(FILENAME)
    #filter = 'mag'
    create_map(data)
    display_map()
    #print(data['mag'])

if __name__ == "__main__":
    main()