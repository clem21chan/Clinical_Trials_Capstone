### DATA Modelling ###

## Import Libraries
import streamlit as st
import pandas as pd
import numpy as np
import joblib
# huggingface/transformers
from transformers import AutoTokenizer, AutoModelForSequenceClassification, TextClassificationPipeline

st.set_page_config(
    page_title='ML Modelling',
    page_icon='💻'
)

'''
'''

# Main Page
st.title('ML Modelling')

@st.cache_data # Used to cache the results of the functions to optimize performance
# Create a data loading function
def load_data(path):
    # load clean dataset
    df = pd.read_csv(path, index_col=0)

    return df

## Ensemble Learning: RandomForest Model ##
st.header('Ensemble Learning: Random Forest Classification')
# Load model
rmf_model = joblib.load('../Notebooks/models/RandomForest.pkl')

# Load testing set
test_df = load_data('../Notebooks/updated_test_set.csv')

# Slice out X and y test
X_test = test_df.iloc[:,:2277]
y_test = test_df.iloc[:, -1]

st.write(rmf_model.predict(X_test.iloc[0:1,:]))


'''
'''

## Word Embedded Transfer Learning Model ##
st.header('Transfer Learning using Bio_ClinicalBERT')
# Create expected IDs and their labels
id2label = {0: "COMPLETED", 1: "TERMINATED"}
label2id = {"COMPLETED": 0, "TERMINATED": 1}

# Load model
model = AutoModelForSequenceClassification.from_pretrained(
    "../Notebooks/models/TransferModel_v2",
    num_labels=2,
    id2label=id2label,
    label2id=label2id)

# Load tokenizer
tokenizer = AutoTokenizer.from_pretrained("emilyalsentzer/Bio_ClinicalBERT")

# textbox
text = st.text_input('Fine-Tuned Bio_ClinicalBERT Model', 'Phase 2 Study of JK07 in Chronic Heart Failure (RENEU-HF)')

# text predictions using a pipe
pipe = TextClassificationPipeline(model=model, tokenizer=tokenizer, device='cuda')
output = pipe(text)

# Extract label and score
label = output[0]["label"]
score = output[0]["score"]

# prediction return
st.write('Classification:', label, ', Confidence_Score:', round(score*100, 1))