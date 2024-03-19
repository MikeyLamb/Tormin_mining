import os
import streamlit as st
import leafmap.foliumap as leafmap
st.set_page_config(layout="wide")

# Define the relative path to the raster folder
raster_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "../raster"))

# Print the resolved path to raster folder for debugging
print("Resolved path to raster folder:", raster_folder)

# Check if the raster folder exists
if not os.path.exists(raster_folder):
    st.error("The 'raster' folder does not exist. Please make sure it is located at the correct location.")
    st.stop()

# Get all raster files from the "raster" folder
raster_files = [f for f in os.listdir(raster_folder) if f.endswith('.tif')]

if not raster_files:
    st.error("No raster files found in the 'raster' folder.")
    st.stop()

# Define ESA layers
esa_layers = ['ESA WorldCover 2020']

# Create sidebar widget for the dropdown menu to select the right layer
left_layer = st.sidebar.selectbox("Select Left Layer", ["OpenStreetMap", "SATELLITE"] + raster_files)
right_layer = st.sidebar.selectbox("Select Right Layer", ["OpenStreetMap", "SATELLITE"] + raster_files + esa_layers)

# Add a button to zoom to a custom bounding box in the sidebar
if st.sidebar.button("Zoom to Tormin Mine"):
    # Replace these values with your custom bounding box coordinates [minx, miny, maxx, maxy]
    center_coords = (18.099903, -31.555141)
    default_zoom = 14
    m = leafmap.Map(center=center_coords, zoom=default_zoom)
    
    # Add raster layers if selected
    if left_layer.endswith('.tif'):
        raster_path = os.path.join(raster_folder, left_layer)
        m.add_raster(raster_path)
    if right_layer.endswith('.tif'):
        raster_path = os.path.join(raster_folder, right_layer)
        m.add_raster(raster_path)
    
    m.split_map(left_layer=left_layer, right_layer=right_layer)



st.title("Split-panel Map")

# Dynamic header to display the selected right layer
left_header, right_header = st.columns(2)
left_header.header(f"{left_layer}")
right_header.header(f"{right_layer}")

default_center = (-31.555141, 18.099903)
default_zoom = 14

m = leafmap.Map(center=default_center, zoom=default_zoom)

# Add raster layers if selected
if left_layer.endswith('.tif'):
    raster_path = os.path.join(raster_folder, left_layer)
    m.add_raster(raster_path)
if right_layer.endswith('.tif'):
    raster_path = os.path.join(raster_folder, right_layer)
    m.add_raster(raster_path)


m.split_map(left_layer=left_layer, right_layer=right_layer)

# Check if the selected layer is ESA WorldCover, then display the legend
if right_layer in esa_layers:
    m.add_legend(title="ESA World Cover", builtin_legend="ESA_WorldCover", )

m.to_streamlit(height=700)
