# Capstone Project: Predicting Clinical Trial Terminations
**Author:** Clement Chan

Date: 2024/04/15

Dataset link: https://clinicaltrials.gov/

## 1. Project Overview

### Problem Area

Whenever the health and medical field reaches new advancements or innovations, it becomes imperative to conduct clinical trials to ascertain the safety and efficacy of the treatments. Often times, significant resources are dedicated towards the design, analysis, and conclusive determination of clinical trials. [Previous studies](https://pubmed.ncbi.nlm.nih.gov/26011295/) have shown that out of 8000 trials, 960 or (12%) will be terminated. Additionally, average costs of clinical trials ranges from [1.4 million - 52.9 million USD](https://journals.sagepub.com/doi/10.1177/1740774515625964) in 2015, and is increasing at a rapid rate. To optimize processes and minimize expenses, the goal is to pinpoint specific factors or parameters that contribute to clinical trial terminations. Some of these factors could include, not enough funding, shortage of personnel for the study, inadequate study design, ethical and scientific concerns, loss of staff members etc.

### Those Affected

Many large pharmaceutical companies, investors, and other research entities would benefit significantly by discerning the key parameters to prioritize in their clinical trial design. By creating a predictive model for clinical trial terminations, our aim is to guide these stakeholders towards more informed trial-design processes.

### Proposed Data Science Solution

The main goal of this project is to first discover the primary factors associated with Trial Terminations and then create a predictive machine learning model that classifies terminated trials based on feature engineering, ensemble, and word embedded transfer learning.

**General Breakdown:**
1. Data Wrangling: Exploring and understanding the dataset which includes data cleaning, feature selection, and preliminary EDA.
2. Data Preprocessing/EDA: Using statistics, distributions, and regression models to determine the key features that affect the termination of clinical trials.
3. Predictive Modeling: Using Logistic Regression, Random Forest Classification, and Word Embedded Transfer Learning ([Bio_ClinicalBERT](https://huggingface.co/emilyalsentzer/Bio_ClinicalBERT)).

### Impact of the Solution

By creating this analysis and model, we can save up to 50 million USD per trial in funding by sponsors, investors, and the government. Additionally, by helping medical companies better understand the factors that cause clinical trial failures, we can improve the design of clinical trials and prevent loss of scientific advancements in medicine.

## 2. Data Information

### Brief Description

The dataset was retrieved from [ClinicalTrials.gov](https://clinicaltrials.gov/) on Feb. 16th 2024. It consists of 483,238 different clinical studies and 30 different columns of information. ClinicalTrials.gov is a online database that is primarily used by Canada and the United States. It includes studies that take place in over 200 countries and relies on sponsors and collaborators to submit up to date information of their studies.

### Data Dictionary For This Project:

| Column | Description                                  |Data Type|
|-------|--------------------------------------------|-------|
| Study Status (**Dependant Variable**)| Binary column, 0 for Completed Trials and 1 for Terminated Trials | int |
| Study Title | Title of the Clinical Trial           | object |
| Brief Summary | Short description of the clinical study (Includes study hypothesis) | object |
| Study Results | Whether the results are posted (yes = 1 or no = 0) | int|
| Conditions | Primary Disease or Condition being studied     | object |
| Primary Outcome Measures | Description of specific primary outcome | object |
| Sponsor | The corporation or agency that initiates the study | object |
| Collaborators | Other organizations that provide support | object |
| Sex | All: No limit on eligibility based on sex, Male: Only male participants, Female: Only female participants | int |
| Age | Age group of participants: ADULT, OLDER_ADULT, CHILD  | int |
| Phases | Clinical trial phase of the study | int |
| Enrollment | Total number of participants in a study | int |
| Funder Type | Government, Industry, or Other | int |
| Study Type | Interventional = 1, Observational = 0 | int |
| Study Design | Study design based on study type | object |
| Study Duration | Length of the entire study in categories | object |
| Locations | Country of where the clinical study was held | object |

## 3. Project Workflow
1. **Data Collection:**
    - Retrieve dataset from clinicaltrials.gov
2. **Data Preprocessing:**
    - Handle missing values
    - Analyze data quality, data type, issues, etc.
    - Selecting important features/feature engineering
3. **Exploratory Data Analysis:**
    - Evaluate distributions of important variables
    - Visualize patterns and important issues to address
    - Perform Hypothesis Testing to determine statistical significance
    - Formulate questions and discover hidden information within the dataset
4. **Baseline Modelling:**
    - Logistic regression, decision tree
    - Evaluate model using confusion matrix and classification reports
    - Preprocessing Text data
5. **Advanced Modelling:**
    - Ensemble learning (Random Forest)
    - Hyperparameter fine tuning
    - Word Embedded Transfer Learning

## 4. Repository Navigation

### Notebooks
**1_DataWrangling:**
- Initial look into dataset
- Cleaning missing values and analyzing distributions
- Preliminary EDA and creating workflow

**2_Preprocessing&EDA:**
- Indepth cleaning of tabular columns
- Created dummy variables and prepared data for baseline model
- More comprehensive EDA of the targeted variable `Study Status`
- Chi-Squared Hypothesis Testing

**3.0_BaselineModelling:**
- Logistic Regression of tabular variables
- Confusion Matrix: Precision, Recall, and F1 score analysis
- Text Data preprocessing + Baseline Model

**3.1_AdditionalTextPreprocessing:**
- Preprocessed the `Sponsor`, `Collaborators`, `Conditions`, and `Primary Outcome Measures` text columns.
- Fitted each to the LogisticRegression baseline model
- Evaluated Coefficients, insights, and model scores

**4.0_AdvancedModelling_Ensemble:**
- Fit a decision tree baseline
- Optimized Random Forest Classification
- HyperParameter Fine-tuned Random Forest Classfier
- Evaluated accuracy, f1_score, roc_auc_score

**4.1_AdvModel_WordEmbedding:**
- Utilised BioClinicalBERT tokenizer and model
- Preprocessed `Study Title` text column
- Fine-tuned to pretrain model for Transfer Learning
- Sample testing

## 5. Setup
I've included all the appropriate packages needed to be installed in the environment file `Clinical_Trial_env.yml`
