import pandas as pd
data=pd.read_csv("C:/Users/jino/Desktop/card_use_1.csv",sep='|')
print(data)

data.columns

data=data.drop(['INDEX', 'STD_YM', 'BLOCK_CD', 'SALE_AMT_00TMST', 'SALE_AMT_01TMST',
       'SALE_AMT_02TMST', 'SALE_cAMT_03TMST', 'SALE_AMT_04TMST',
       'SALE_AMT_05TMST', 'SALE_AMT_20TMST', 'SALE_AMT_21TMST',
       'SALE_AMT_22TMST', 'SALE_AMT_23TMST'],axis=1)

data

card_data_place=data.groupby(['LAT','LON']).sum()

card_data_place



# https://github.com/python-visualization/folium/issues/803
# https://nbviewer.jupyter.org/github/python-visualization/folium/blob/master/examples/MarkerCluster.ipynb
import folium
from folium.plugins import MarkerCluster



map_osm = folium.Map(location=[35.8796687,128.4266147], zoom_start=13)
marker_cluster = MarkerCluster().add_to(map_osm)

#card_data_place.dropna()
drop_index=card_data_place[card_data_place['SUM']==0].index

card_data_place=card_data_place.drop(drop_index)

card_data_place=card_data_place.reset_index(level='LAT')
card_data_place=card_data_place.reset_index(level='LON')

card_data_place.columns
card_data_place



for i in range(0, len(card_data_place.index)):
    lat = card_data_place.loc[i, 'LAT']
    lon = card_data_place.loc[i, 'LON']

    folium.CircleMarker([lat, lon], radius=card_data_place.loc[i, 'SUM'] / 70000, color='blue', fill=True).add_to(
        marker_cluster)

map_osm.save('map.html')