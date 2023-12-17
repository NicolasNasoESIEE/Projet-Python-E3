import folium
import branca
import csv
import pandas as pd
import os
import requests

FILENAME = "us_tornado_dataset_1950_2021.csv"

def create_map_tornado_path(data):

    if os.path.exists("map_tornado_path.html") : 
        os.remove("map_tornado_path.html")

    data_filtered = data[(data['yr'] >= 2010) & (data['yr'] <= 2015)]

    map = folium.Map(location=[38, -97], tiles='OpenStreetMap', zoom_start=4)

    cm = branca.colormap.LinearColormap(['blue', 'red'], vmin=data['len'].min(), vmax=data['len'].max())

    cm.caption = "distance tornade (miles)"

    for index, row in data_filtered.iterrows():
        if(row['elat'] != 0 or row['elon'] != 0):
            color = cm(row['len'])
            folium.PolyLine(
            [(row['slat'], row['slon']), (row['elat'], row['elon'])],
            color=color,
            weight=1,
            opacity=1,
            popup=f"Mag: {row['mag']}, Wid: {row['wid']}, Len: {row['len']}"
            ).add_to(map)

    folium.TileLayer('https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png', name='OpenTopoMap', attr='OpenTopoMap').add_to(map)

    map.add_child(cm)

    folium.LayerControl().add_to(map)

    map.save('map_tornado_path.html')

def create_map_tornado_choropleth(data):

    if os.path.exists("map_tornado_choropleth.html"):
        os.remove("map_tornado_choropleth.html")

    data_filtered = data[(data['yr'] >= 1950) & (data['yr'] <= 2021)]

    geo_json_data = requests.get(
        "https://raw.githubusercontent.com/python-visualization/folium-example-data/main/us_states.json"
    ).json()

    tornado_count_by_state = data_filtered.groupby('st').size().reset_index(name='count')

    #merged_data = pd.merge(geo_json_data['features'], tornado_count_by_state, left_on='id', right_on='st')

    map = folium.Map(location=[38, -97], tiles='OpenStreetMap', zoom_start=4)

    folium.Choropleth(
        geo_data=geo_json_data,
        data=tornado_count_by_state,
        columns=['st', 'count'],
        key_on='feature.id',
        fill_color='YlOrRd',
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name='Nb tornades par État',
        popup=f"nb tornades : {tornado_count_by_state['st']}",
        name='Filtre Couleurs'
    ).add_to(map)

    folium.GeoJson(
        geo_json_data,
        style_function=lambda feature: {
            'fillColor': 'transparent',
            'color': 'black',
            'weight': 1
        },
        highlight_function=lambda x: {'weight': 3, 'color': '#666'},
        smooth_factor=2.0,
        name='States'
    ).add_to(map)

    #folium.GeoJson(geo_json_data).add_to(map)

    folium.TileLayer('https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png', name='OpenTopoMap', attr='OpenTopoMap').add_to(map)

    folium.LayerControl().add_to(map)

    #map.add_child(folium.ClickForMarker(popup="Tornado count: {count}".format(count=tornado_count_by_state['count'].max())))

    map.save('map_tornado_choropleth.html')


def create_maps():
    df = pd.read_csv(FILENAME)
    create_map_tornado_choropleth(df)
    create_map_tornado_path(df)