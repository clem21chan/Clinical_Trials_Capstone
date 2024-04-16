### Predicting Clinical Trial Terminations ###

## Instructions
# conda install -c conda-forge streamlit
# open terminal and run: streamlit run <name_of_file.py>


## Importing Libraries
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Clinical Trial Terminations",
    page_icon="🥼"
)

st.title('Predicting Clinical Trial Terminations')
st.markdown('Insert Brief description here')

# page_bg_img = f"""
# <style>
# [data-testid="stAppViewContainer"] > .main {{
# background-image: url("https://i.pinimg.com/564x/4a/a8/7f/4aa87fb76e0355db7654985cde9677e8.jpg");
# background-size: cover;
# background-position: center center;
# background-repeat: no-repeat;
# background-attachment: local;
# }}
# [data-testid="stHeader"] {{
# background: rgba(0,0,0,0);
# }}
# </style>
# """
# st.markdown(page_bg_img, unsafe_allow_html=True)


st.sidebar.success("Select a page above.")