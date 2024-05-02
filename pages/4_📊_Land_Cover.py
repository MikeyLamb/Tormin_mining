import os
import streamlit as st
import altair as alt
import leafmap.foliumap as leafmap
import pandas as pd



st.set_page_config(
        page_title= 'Mining in South Africa',
        page_icon=":world_map:",
        layout = "wide",
        initial_sidebar_state="expanded")

st.title("Area of Land Cover Map")

st.markdown(
    """
    Welcome to this web app showing satellite imagery of mining at Tormin on the West Coast of South Africa
    """
)

text_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "../text"))
csv_file = os.path.join(text_folder, "class_areas.csv")

#Get the raster folder
raster_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "../raster"))
raster_files = [f for f in os.listdir(raster_folder) if f.endswith('.tif')]

active_layer = st.sidebar.selectbox("Select Layer:", [None] + raster_files)


# Define a function to zoom to Tormin Mine
def zoom_to_tormin_mine():
    # Replace these values with your custom bounding box coordinates [minx, miny, maxx, maxy]
    center_coords = (-31.555141, 18.099903)
    default_zoom = 14
    # Update the map's center and zoom level
    m.set_center(center_coords[1], center_coords[0],zoom=default_zoom)


center_coords = (-31.555141, 18.099903)
default_zoom = 14
m = leafmap.Map(center=center_coords, zoom=default_zoom)
m.add_basemap("SATELLITE", show=False)


# Add raster layers if selected
if active_layer and active_layer.endswith('.tif'):
    raster_path = os.path.join(raster_folder, active_layer)
    m.add_raster(raster_path)

    # Read CSV file containing class areas
    try:
        if os.path.exists(csv_file):
            class_areas_df = pd.read_csv(csv_file)
            if active_layer in class_areas_df["Image"].values:
                selected_image_class_areas = class_areas_df[class_areas_df["Image"] == active_layer]

                # Check if the DataFrame has the expected columns
                if "Class" in selected_image_class_areas.columns and "Area" in selected_image_class_areas.columns:
                    # Plot dynamic bar chart based on class areas for selected image using Altair
                    chart = alt.Chart(selected_image_class_areas).mark_bar().encode(
                        x=alt.X('Class', title='Class'),
                        y=alt.Y('Area', title='Area'),
                        color=alt.Color('Class', scale=alt.Scale(range=["#f5e833", "#5c703c", "#d30105", "#136ede"]), legend=None),
                        tooltip=['Class', 'Area']
                    ).properties(
                        width=600,
                        height=400
                    )
                    st.altair_chart(chart, use_container_width=True)
                else:
                    st.error("Class or Area column not found in the CSV file.")
        else:
            st.error("CSV file not found.")
    except Exception as e:
        st.error(f"An error occurred: {e}")



# Add a button to zoom to Tormin Mine
if st.sidebar.button("Zoom to Tormin Mine"):
    zoom_to_tormin_mine()


# Display the map
legend_dict = {
    "Beach": "#f5e833",
    "Shrub": "#5c703c",
    "Disturbed/Barren": "#d30105",
    "Water": "#136ede",

}

m.add_legend(title='Mining Status', legend_dict=legend_dict, draggable=None)


m.to_streamlit(height=550)