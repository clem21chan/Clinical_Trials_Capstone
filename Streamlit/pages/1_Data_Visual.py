### DATA VISUALIZATIONS ###

## Import Libraries
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(
    page_title='Data Visualization',
    page_icon='📈'
)

# Main Page
st.title('Data Visualization')

@st.cache_data # Used to cache the results of the functions to optimize performance

# Create a data loading function
def load_data(path):
    # load clean dataset
    df = pd.read_csv(path, index_col=0)

    return df

# Load clean dataset
clean_df = load_data('../Notebooks/clean_ctg.csv')

# Display dataframe
st.dataframe(clean_df.head())

## Graph 1: Clinical Trial Termination Based on Enrollment Number ##
# manually sort the categories
enrollment_categories = ['0-8','9-19','20-29','30-41','42-59','60-79','80-119','120-209','210-490','491-188814085']
clean_df['Enrollment'] = pd.Categorical(clean_df['Enrollment'], enrollment_categories)

# slice out completed and terminated rows
completed = clean_df['Study Status'] == 0
terminated = clean_df['Study Status'] == 1

# Count the rows of completed and terminated
completed_counts = clean_df[completed].groupby('Enrollment')['Study Status'].count().rename({'491-188814085' : '491-200000000'}) # rename to cleanup the label
terminated_counts = clean_df[terminated].groupby('Enrollment')['Study Status'].count().rename({'491-188814085' : '491-200000000'})

# total counts
total_counts = clean_df.groupby('Enrollment')['Enrollment'].count().rename({'491-188814085' : '491-200000000'})

# completed ratio df
comp_ratio = pd.DataFrame((completed_counts / total_counts)*100).rename(columns={0:'Completed'})

# terminated ratio df
term_ratio = pd.DataFrame((terminated_counts / total_counts)*100).rename(columns={0:'Terminated'})

# Concat df
graph1 = pd.concat([term_ratio, comp_ratio], axis=1)

# creating the bar graph
fig1 = px.bar(graph1, orientation='h', color_discrete_sequence=['#f35c6e', '#686ee2'])

fig1.update_layout(
    title="Clinical Trial Termination Based on Enrollment Number",
    xaxis_title="Percentage",
    yaxis_title="Enrollment Number"
)

st.plotly_chart(fig1)

# Sidebar
st.sidebar.header('Data Visualization')

