import os
import json
import streamlit as st
import leafmap.foliumap as leafmap

# Set page configuration
st.set_page_config(
        page_title= 'Mining in South Africa',
        page_icon=":world_map:",
        layout = "wide",
        initial_sidebar_state="expanded")

# Display the map title
st.title("RSA Mining Map")

st.markdown(
    """
    Welcome to this web app showing satellite imagery of mining at Tormin on the West Coast of South Africa
    """
)

# Define the relative path to the vector folder
vector_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "../vector"))

# Path to the GeoJSON file
geojson_file = os.path.join(vector_folder, "rsa_mining_areas.geojson")

# Create a Leafmap map object
m = leafmap.Map()
m.add_basemap("SATELLITE", show=False)

# Define a function to map status values to colors
def style_callback(status):
    if status == "Mining Right":
        return "#940000", "", 1
    elif status == "Mining Application":
        return "#bf0000", "", 1
    elif status == "Prospecting Right":
        return "#f7525b", "", 1
    elif status ==  "Prospecting Application":
        return "#f07850", "", 1
    elif status == "Production Right":
        return "#f5bd8b", "", 1
    elif status ==  "Exploration Right":
        return "#ffe0b2", "", 1
    elif status == "Exploration Application":
        return "#f7525b", "", 1
    elif status == "Application Refused":
        return "#93c78f", "", 1
    elif status ==  "Reconnaissance Permit":
        return "#000000", "#000000", 0.8
    else:
        return "#808080", "#000000", 1  # Default color for unknown statuses


# Create a style function to dynamically assign colors based on status
def style_function(feature):
    status = feature["properties"]["Status"]
    fill_colour, border_colour, border_weight = style_callback(status)
    fill_opacity = 0.7 if status != "Reconnaissance Permit" else 0
    return {
        "fillColor": fill_colour,
        "fillOpacity": fill_opacity,
        "color": border_colour,
        "weight": border_weight
    }

# Create a highlight function to display a black border when hovering over a polygon
def highlight_function(feature):
    return {
        "color": "#000000",
        "weight": 1.5
    }

# Get unique values in the "Status" column
unique_statuses = set()
with open(geojson_file, "r") as f:
    data = json.load(f)
    for feature in data["features"]:
        unique_statuses.add(feature["properties"]["Status"])

# Create an editable legend using multiselect widget
selected_statuses = st.multiselect("Select statuses to display:", list(unique_statuses), default=list(unique_statuses))

# Filter GeoJSON features based on selected statuses
filtered_features = {
    "type": "FeatureCollection",
    "features": [feature for feature in data["features"] if feature["properties"]["Status"] in selected_statuses]
}

# Check if any features are present in the filtered GeoJSON
if len(filtered_features["features"]) > 0:
    # Add the filtered GeoJSON features to the map
    m.add_geojson(filtered_features, layer_name="Mining Areas", info_mode="on_click", style_function=style_function, highlight_function=highlight_function)
else:
    # Display only the basemap
    m.add_basemap("OpenStreetMap")

# Display the map
legend_dict = {
    "Mining Right": "#940000",
    "Mining Application": "#bf0000",
    "Prospecting Right": "#f7525b",
    "Prospecting Application": "#f07850",
    "Production Right": "#f5bd8b",
    "Exploration Right": "#facc87",
    "Exploration Application": "#ffe0b2",
    "Application Refused": "#93c78f",
    "Reconnaissance Permit": "#ffffff",
}

m.add_legend(title='Mining Status', legend_dict=legend_dict, draggable=None)

m.to_streamlit(height=550)
