import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(
        page_title= 'Mining in South Africa',
        page_icon=":world_map:",
        layout = "wide",
        initial_sidebar_state="expanded")


st.title("Cliff slumps")

st.markdown(
    """
    Welcome to this web app showing satellite imagery of mining at Tormin on the West Coast of South Africa
    """
)

center_coords = (18.099903, -31.555141)
default_zoom = 14
m = leafmap.Map(center=center_coords, zoom=default_zoom)
m.add_basemap("SATELLITE")


collapses = 'vector\cliff_collapses.csv'
regions = 'vector\collapse_areas.geojson'

m.add_geojson(regions, layer_name='Collapse areas')
m.add_points_from_xy(
    collapses,
    x="longitude",
    y="latitude",
    spin=True,
    add_legend=True,
)
        
m.to_streamlit(height=700)
