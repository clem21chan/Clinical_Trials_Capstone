# Capstone Project: Predicting Clinical Trial Terminations
Clement Chan, Data Science Diploma Program @BrainStation

Date: 2024/03/30

Dataset link: https://clinicaltrials.gov/

## Project Overview

### Problem Area

Whenever the health and medical field witnesses new advancements or innovations, it becomes imperative to conduct clinical trials to ascertain the safety and efficacy of the treatments. Often times, significant resources are dedicated towards the design, analysis, and conclusive determination of clinical trials. To optimize processes and minimize expenses, the goal is to pinpoint specific factors or parameters that contribute to clinical trial terminations. Some of these factors could include, not enough funding, shortage of personnel for the study, inadequate study design, ethical and scientific concerns, loss of staff members etc.

### Those Affected

Many large pharmaceutical companies, investors, and other research entities would benefit significantly by discerning the key parameters to prioritize in their clinical trial design. By creating a predictive model for clinical trial terminations, our aim is to guide these stakeholders towards more informed trial-design processes.

### Proposed Data Science Solution

1. Data Wrangling/Exploration: Exploring and understanding the dataset which includes data cleaning, feature selection, and preprocessing.
2. Data Preprocessing: Using statistics, distributions, and regression models to determine the key features that affect the termination of clinical trials.
3. Predictive Modeling: Using NLP and Word embedding to identify keywords in the brief summary together for a more accurate model.

### Impact of the Solution

By creating this analysis and model, we can potentially save millions of dollars in funding by sponsors, investors, and the government. Additionally, by helping medical companies better understand the factors that cause clinical trial failures, we can improve the design of clinical trials and prevent loss of scientific advancements in medicine.


### Data Dictionary based on clinicaltrials.gov:

---

| Column | Description                                  |Data Type|
|-------|--------------------------------------------|-------|
| Study Title | Title of the Clinical Trial           | object |
| Study Status | Binary column, 0 for Completed Trials and 1 for Terminated Trials | int |
| Brief Summary | Short description of the clinical study (Includes study hypothesis) | object |
| Study Results | Whether the results are posted (yes = 1 or no = 0) | int|
| Conditions | Primary Disease or Condition being studied     | object |
| Interventions | The methods used in the trial to reach the outcome                 | object |
| Primary Outcome Measures | Description of specific primary outcome | object |
| Secondary Outcome Measures | Description of specific secondary outcome | object |
| Sponsor | The corporation or agency that initiates the study | object |
| Collaborators | Other organizations that provide support | object |
| Sex | All: No limit on eligibility based on sex, Male: Only male participants, Female: Only female participants | int |
| Age | Age group of participants: ADULT, OLDER_ADULT, CHILD  | int |
| Phases | Clinical trial phase of the study | int |
| Enrollment | Total number of participants in a study | int |
| Funder Type | Government, Industry, or Other | int |
| Study Type | Interventional = 1, Observational = 0 | int |
| Study Design | Study design based on study type | object |
| Start Date | Estimated/Actual date the first participant was enrolled | datetime |
| Primary Completion Date | Date the final participant was examined for the first outcome | datetime |
| Completion Date | Date the final participant was examined | datetime |
| Locations | Where the clinical study will be held | object |

## Flowchart
1. **Data Collection:**
    - Retrieve dataset from clinicaltrials.gov
2. **Data Preprocessing:**
    - Handle missing values
    - Analyze data quality, data type, issues, etc.
    - Selecting important features/feature engineering
3. **Exploratory Data Analysis:**
    - Evaluate distributions of important variables
    - Visualize patterns and important issues to address
    - Formulate questions and find hidden information within the dataset
4. **Baseline Modelling:**
    - Linear regression, decision tree
    - Evaluate model using confusion matrix and classification reports
5. **Advanced Modelling:**
    - Ensemble learning (Random Forest)
    - Gradient Boosting
    - Word Embedding + neural networks
    - Hyperparameter fine tuning

## Repository Navigation

### Notebooks
**1_DataWrangling:**
- Initial look into dataset
- Cleaning missing values and analyzing distributions
- Preliminary EDA and creating workflow

**2_Preprocessing&EDA:**
- Indepth cleaning of tabular columns
- Created dummy variables and prepared data for baseline model
- More comprehensive EDA of the targeted variable `Study Status`

**3_BaselineModelling:**
- Logistic Regression of tabular variables
- Confusion Matrix: Precision, Recall, and F1 score analysis
- Text Data preprocessing + Baseline Model

## What to expect for the next sprint:
- Deal with massive data imbalance by random desampling the completed trials.
- Perform ensemble learning and word embedding for better predictions.
