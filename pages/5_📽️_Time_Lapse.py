# import os
# import streamlit as st
# import leafmap.foliumap as leafmap


# st.set_page_config(layout="wide")

# st.title("Split-panel Map")

# st.markdown(
#     """
#     Welcome to this web app showing satellite imagery of mining at Tormin on the West Coast of South Africa
#     """
# )


# images = "peru/*.tif"

# leafmap.create_timelapse(
#     images,
#     out_gif="landsat.gif",
#     bands=[0, 1, 2],
#     fps=10,
#     progress_bar_color="blue",
#     add_text=True,
#     text_xy=("3%", "3%"),
#     text_sequence=1984,
#     font_size=20,
#     font_color="black",
#     mp4=False,
#     reduce_size=False,
# )

# leafmap.show_image("landsat.gif")