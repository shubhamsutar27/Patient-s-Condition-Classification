# Patient's-Condition-Classification

## Business Objective:
The business objective of this project is to classify patient reviews related to specific conditions, namely Depression, High Blood Pressure, and Type 2 Diabetes. The goal is to understand the effectiveness of drugs for specific conditions and their potential side effects by analyzing patient reviews, ratings, and useful counts. The insights gained from this analysis can be used to recommend suitable drugs for patients based on their condition and the experiences of other patients with similar conditions.

## Features:
* DrugName (categorical): The name of the drug that the patient is reviewing. This feature will be used to group reviews by drug and analyze the effectiveness of each drug for specific conditions.
* Condition (categorical): The name of the condition that the patient is reviewing the drug for. This feature will be used to identify reviews related to Depression, High Blood Pressure, and Type 2 Diabetes.
* Review (text): The patient's review of the drug. This feature will be used to extract insights on the effectiveness and potential side effects of drugs for specific conditions.
* Rating (numerical): A 10-star patient rating reflecting overall patient satisfaction with the drug. This feature will be used to understand the level of patient satisfaction with different drugs for specific conditions.
* Date (date): The date on which the review was entered. This feature will be used to analyze trends over time in patient reviews and ratings.
* UsefulCount (numerical): The number of users who found the review useful. This feature will be used to identify reviews that are likely to be helpful in understanding the effectiveness and potential side effects of drugs for specific conditions.

## Project Summary:
* Project aims to classify patient reviews related to specific conditions, including Depression, High Blood Pressure, and Type 2 Diabetes. The data was cleaned by removing stop words and normalization, and the date feature was removed as it was not deemed useful for model building. The TF-IDF vectorizer was used to convert the review text into numerical data, and multiple models, including Logistic Regression, Random Forest, SVM, Gradient Boosting, and Decision Tree, were built using the condition as the dependent variable and the review as the independent variable. Based on the model evaluation metrics, the SVM model was selected as the best model due to its highest accuracy.
* Additionally, the project also recommended 10 popular drugs based on their ratings, but it was noted that the effects of drugs may vary from person to person, and the recommendations are general.

## Conclusion: 
* The project successfully predicted patient conditions based on drug reviews, and the insights gained can be used to recommend suitable drugs for patients based on their condition and the experiences of other patients with similar conditions. The project's findings provide valuable information to healthcare providers and patients alike in making informed decisions regarding drug usage.
