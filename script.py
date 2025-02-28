import streamlit as st
import pandas as pd
import folium 
from streamlit_folium import st_folium

url = ""
df = pd.read_csv(url)

st.title('Matka')

st.write("Keskinopeus on :", df['Speed (m/s)'].mean(),'m/s' )
st.write("Kokonaismatka on :", df['Distance (km)'].max(),'km' )

st.line_chart(df, x = 'Time (s)', y = 'Distance (km)', y_label = 'Distance',x_label = 'Time')

start_lat = df['Latitude (°)'].mean()
start_long = df['Longitude (°)'].mean()
map = folium.Map(location = [start_lat,start_long], zoom_start = 14)

folium.PolyLine(df[['Latitude (°)','Longitude (°)']], color = 'blue', weight = 3.5, opacity = 1).add_to(map)



st_map = st_folium(map, width=900, height=650)