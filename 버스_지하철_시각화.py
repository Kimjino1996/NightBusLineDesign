#!/usr/bin/env python
# coding: utf-8

# In[63]:


import folium
import pandas as pd


# In[69]:


df_s = pd.read_csv('C:/Users/leegi/OneDrive/바탕 화면/빅데이터_oracle/버스_승차.csv',encoding='cp949')
df_x = pd.read_csv('C:/Users/leegi/OneDrive/바탕 화면/빅데이터_oracle/버스_하차.csv',encoding='cp949')


# In[70]:


map_osm = folium.Map(location=[35.8796687,128.4266147], zoom_start=13)


# In[72]:


df_s = df_s.dropna()
df_x = df_x.dropna()

df_s2 = df_s.loc[:100]
df_x2 = df_x.loc[:100]


# In[74]:


for item in df_s2.index:
    lat = df_s2.loc[item,'lat']
    lng = df_s2.loc[item,'lng']
    
    folium.CircleMarker([lat,lng], 
                    radius=df_s2.loc[item,'승차']/700,
                    popup = df_s2.loc[item, '정류장명'],
                    color = 'blue',
                    fill = True).add_to(map_osm)
        
for item in df_x2.index:
    lat = df_x2.loc[item,'lat']
    lng = df_x2.loc[item,'lng']
    
    folium.CircleMarker([lat,lng], 
                    radius=df_x2.loc[item,'하차']/700,
                    popup = df_x2.loc[item, '정류장명'],
                    color = 'red',
                    fill = True).add_to(map_osm)
#     folium.Marker([lat,lng], popup=df2.loc[item,'정류장명']).add_to(map_osm)

map_osm

