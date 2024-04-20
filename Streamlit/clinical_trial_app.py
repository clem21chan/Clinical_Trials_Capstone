### Predicting Clinical Trial Terminations ###

## Instructions
# conda install -c conda-forge streamlit
# open terminal and run: streamlit run <name_of_file.py>


## Importing Libraries
import streamlit as st

st.set_page_config(
    page_title="Clinical Trial Terminations",
    page_icon="🥼",
    layout='centered'
)

#### Sidebar ####
st.sidebar.success("Select a page above.")

# Page title
st.title('Predicting Clinical Trial Terminations')
st.markdown('**Author: Clement Chan**')
st.markdown('---')
# Header image
# st.image('.Streamlit/clinical_trial_header.jpg')
# st.markdown('[Source](https://reverserett.org/site/assets/files/7643/hero-what-it-takes-clinical-trial.1500x700.jpg?2n32co)')

# What are Clinical Trials?
st.markdown('## What are Clinical Trials?')
st.markdown('- Clinical Trials are research studies conducted on human participants to assess the **safety** and **effectiveness** of drugs. \
            \n - Newly developed drugs must be tested before they are released into public. \
            \n - Examples: Covid-19 Vaccines, Diabetic Medication, Hypertension, etc.')

# The Problem
st.markdown('## The Problem')
st.markdown('- Significant resources are dedicated towards the design, analysis, and conclusive determination of clinical trials. \
            \n - The average cost of clinical trials ranges from [1.4 million - 52.9 million USD](https://journals.sagepub.com/doi/10.1177/1740774515625964) in 2015 \
            and is increasing at a rapid rate. \
            \n - [Previous studies](https://pubmed.ncbi.nlm.nih.gov/26011295/) indicated that out of 8000 trials, 960 or **(12%)** will be terminated. \
            \n - Some factors include not enough funding, shortage of participants for the study, inadequate study design, ethical and scientific concerns, etc.')

# My Goal
st.markdown('## My Goal')
st.markdown('The goal is to help government and pharmaceutical companies discern the primary factors leading to trial terminations and\
             to create a predictive ML model that classifies terminated trials.')

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
