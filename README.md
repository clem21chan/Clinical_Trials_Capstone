# Capstone Project: Predicting Clinical Trial Terminations
Clement Chan, Data Science Diploma Program @BrainStation

Date: 2024/03/03

Dataset link: https://clinicaltrials.gov/

## Project Overview

### Problem Area

Whenever the health and medical field witnesses new advancements or innovations, it becomes imperative to conduct clinical trials to ascertain the safety and efficacy of the treatments. Often times, significant resources are dedicated towards the design, analysis, and conclusive determination of clinical trials. To optimize processes and minimize expenses, the goal is to pinpoint specific factors or parameters that contribute to clinical trial terminations. Some of these factors could include, not enough funding, shortage of personnel for the study, inadequate study design, ethical and scientific concerns, loss of staff members etc.

### Those Affected

Many large pharmaceutical companies, investors, and other research entities would benefit significantly by discerning the key parameters to prioritize in their clinical trial design. By creating a predictive model for clinical trial terminations, our aim is to guide these stakeholders towards more informed trial-design processes.

### Proposed Data Science Solution

1. Data Wrangling/Exploration: Exploring and understanding the dataset which includes data cleaning, feature selection, and preprocessing.
2. Data Analysis: Using statistics, distributions, and regression models to determine the key features that affect the termination of clinical trials.
3. Predictive Modeling: Using NLP and Word embedding to group keywords in the brief summary together for a more accurate model.

### Impact of the Solution

By creating this analysis and model, we can potentially save millions of dollars in funding by sponsors, investors, and the government. Additionally, by helping medical companies better understand the factors that cause clinical trial failures, we can improve the design of clinical trials and prevent loss of scientific advancements in medicine.

### What to expect for the next sprint:
- Start grouping unique values together in categorical columns using NLP
- Create dummy variables and perform chi-squared tests, logistic regression modelling, and understanding what p-values are significant.
- Start formulating hypothesis for further modelling.

### Rough Data Dictionary based on clinicaltrials.gov that will change as we go:

---

| Column | Description                                  |Data Type|
|-------|--------------------------------------------|-------|
| NCT Number | Unique ID                            | object |
| Study Title | Title of the Clinical Trial           | object |
| Study URL | URL link to the study on clinicaltrials.gov  | object |
| Acronym | An abbreviation used to identify the clinical study | object|
| Study Status | Categorical column displaying the current position of the study | object (could classify into dummies) |
| Brief Summary | Short description of the clinical study (Includes study hypothesis) | object |
| Study Results | Whether the results are posted (yes or no) | object (turn to binary?)|
| Conditions | Primary Disease or Condition being studied     | object |
| Interventions | The methods used in the trial to reach the outcome                 | object |
| Primary Outcome Measures | Description of specific primary outcome | object |
| Secondary Outcome Measures | Description of specific secondary outcome | object |
| Sponsor | The corporation or agency that initiates the study | object |
| Collaborators | Other organizations that provide support | object |
| Sex | All: No limit on eligibility based on sex, Male: Only male participants, Female: Only female participants | object (Could change into binary or dummies) |
| Age | Relative age of the participants? Probably need to clarify/change up the name of the values | object (could classify this into dummies)|
| Phases | Clinical trial phase of the study (drug)... need to classify this futher. | object (dummies?)|
| Enrollment | Total estimated number of participants in a study or total actual enrollment? | float -> int |
| Funder Type | Funding type in category? | object (could classify into dummies) |
| Study Type | Interventional, Observational, or Expanded Access | object (definitely dummies) |
| Study Design | Study design based on study type | object |
| Other IDs | Literally other IDs... don't know why this column is useful when we already have NCT number | object |
| Start Date | Estimated/Actual date the first participant was enrolled | object -> date |
| Primary Completion Date | Date the final participant was examined for the first outcome | object -> date |
| Completion Date | Date the final participant was examined | object -> date |
| First Posted | Date the clinical trial was first posted to the public      | object -> date  |
| Last Update Posted | Date the clinical trial was last posted to the public   | object -> date |
| Locations | Where the clinical study will be held | object |
