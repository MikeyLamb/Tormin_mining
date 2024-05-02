import streamlit as st
import leafmap.foliumap as leafmap



st.set_page_config(
        page_title= 'Mining in South Africa',
        page_icon=":world_map:",
        layout = "wide",
        initial_sidebar_state="expanded")


# Customize the sidebar
markdown = """
Built using Streamlit and Leafmap

By: Michael Lambrecht, One Ocean Hub & University of Cape Town
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://protectthewestcoast.org/wp-content/uploads/2023/06/PTWC_logo.svg"
st.sidebar.image(logo)

markdown_2 = """
Wu, Q. (2021). Leafmap: A Python package for interactive mapping and geospatial analysis with minimal coding in a Jupyter environment. Journal of Open Source Software, 6(63), 3414. https://doi.org/10.21105/joss.03414
"""

st.sidebar.title("Credits")
st.sidebar.info(markdown_2)


# Customize page title
st.title("Tormin Mining")

st.markdown(
    """
    Welcome to this web app showing satellite imagery of mining at Tormin on the West Coast of South Africa
    """
)

st.header("Instructions")

markdown = """
1. Explore the different apps on the left hand side panel. 
2. The left hand side panel can be collapsed and expanded as needed.
"""

st.markdown(markdown)
