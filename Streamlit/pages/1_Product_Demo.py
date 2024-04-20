### DATA VISUALIZATIONS ###

## Import Libraries
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
# huggingface/transformers
from transformers import AutoTokenizer, AutoModelForSequenceClassification, TextClassificationPipeline

st.set_page_config(
    page_title='Product Demo',
    page_icon='💻'
)

# Sidebar
st.sidebar.header('Product Demo')

#################### Data Visualization ##################
st.title('Product Demo')

@st.cache_data # Used to cache the results of the functions to optimize performance

# Create a data loading function
def load_data(path):
    df = pd.read_csv(path, nrows=100, index_col=0)

    return df

# Load clean dataframe
clean_df = load_data('./Streamlit/sample_dataset.csv')

# Display dataframe
st.header('Peek at the dataset:')
st.markdown('[ClinicalTrials](https://clinicaltrials.gov/) Dataset')
st.dataframe(clean_df.head(5))


######## Graph 1: Clinical Trial Termination Based on Enrollment Number #######
# manually sort the categories
st.markdown("## Data Insights")
st.markdown("### Clinical Trial Termination Based on Enrollment Number")
graph1 = load_data('./Streamlit/enrollment_trial_status.csv')

# creating the bar graph
fig1 = px.bar(graph1, orientation='h', color_discrete_sequence=['#f35c6e', '#686ee2'])

fig1.update_layout(
    xaxis_title="Percentage",
    yaxis_title="Enrollment Number"
)

st.plotly_chart(fig1)

st.markdown('**Insights:**\
            \n - As the number of participants in a study **decreases**, trial termination **increases.**\
            \n - Potential Reasons: High requirements, no interest, lack of funding, etc.')

####### Graph 2: Study Title Coefficients that lead to a terminated trial #######
st.markdown("### Top 10 Study Condition Coefficients That Lead to a Trial Termination")
# Load the data
cond_coef = load_data('./Streamlit/top_cond_coef.csv')
# Clean up the labels
labels = {
    'Condition_end stage':'end stage',
    'Condition_crohn disease':'crohn disease',
    'Condition_parkinson':'parkinson',
    'Condition_19':'covid 19',
    'Condition_prostate':'prostate',
    'Condition_fibrillation':'fibrillation',
    'Condition_macular degeneration':'macular degeneration',
    'Condition_cancer':'cancer',
    'Condition_sleep apnea':'sleep apnea',
    'Condition_cystic fibrosis':'cystic fibrosis'
}
cond_coef = cond_coef.rename(labels)

# Creating the plotly figure
fig2 = px.bar(cond_coef.head(10),color_discrete_sequence=['#f35c6e'])

fig2.update_layout(
    yaxis_title="Logistic Regression Coefficient",
    xaxis_title="Study Condition Words",
    showlegend=False
)

st.plotly_chart(fig2)

st.markdown('**Insights:**\
            \n - Greater the coefficient the more likely the word is associated with trial termination.\
            \n - **Chronic Conditions** such as Crohn disease, Parkinson, cancer etc. seem to have the greatest impact on trial termination.\
            \n - [Studies](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8164884/) in 2021 found that **19%** of Covid related trials\
             were terminated due to enrollment difficulties and less people with covid cases.')


###################### MODELLING #################
st.title('ML Modelling - Neural Networks')

## Word Embedded Transfer Learning Model ##
st.markdown('### Transfer Learning using Bio_ClinicalBERT')
# Create expected IDs and their labels
id2label = {0: "COMPLETED", 1: "TERMINATED"}
label2id = {"COMPLETED": 0, "TERMINATED": 1}

# Load model
model = AutoModelForSequenceClassification.from_pretrained(
    "clem21chan/clinical_trial_termination",
    num_labels=2,
    id2label=id2label,
    label2id=label2id)

# Load tokenizer
tokenizer = AutoTokenizer.from_pretrained("emilyalsentzer/Bio_ClinicalBERT")

# textbox
text = st.text_input('Fine-Tuned Bio_ClinicalBERT Model', 'Phase 2 Study of JK07 in Chronic Heart Failure (RENEU-HF)')

# text predictions using a pipe
pipe = TextClassificationPipeline(model=model, tokenizer=tokenizer, device='cpu')
output = pipe(text)

# Extract label and score
label = output[0]["label"]
score = output[0]["score"]

# prediction return
st.write('Classification:', label, ', Confidence_Score:', round(score*100, 1))

# st.image('.Streamlit/clinicalbert.png')
st.markdown('**What is [BioClinicalBERT](https://huggingface.co/emilyalsentzer/Bio_ClinicalBERT)?**\
            \n - Trained by Emily Alsentzer with over millions of downloads.\
            \n - **HuggingFace Transformer** that was trained on PubMed and MIMIC III dataset.')
