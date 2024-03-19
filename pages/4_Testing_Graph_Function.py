import os
import streamlit as st
import leafmap.foliumap as leafmap
st.set_page_config(layout="wide")

st.title("Area of Land Cover Map")

#Get the raster folder
raster_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "../raster"))
# Get all raster files from the "raster" folder
raster_files = [f for f in os.listdir(raster_folder) if f.endswith('.tif')]

active_layer = st.sidebar.selectbox("Select Layer:", raster_files)

if st.sidebar.button("Zoom to Tormin Mine"):
    # Replace these values with your custom bounding box coordinates [minx, miny, maxx, maxy]
    center_coords = (-31.555141,18.099903)
    default_zoom = 14
    m = leafmap.Map(center=center_coords, zoom=default_zoom)


center_coords = (-31.555141, 18.099903)
default_zoom = 14
m = leafmap.Map(center=center_coords, zoom=default_zoom)
m.add_basemap("SATELLITE")

m.to_streamlit(height=550)