# Import libraries
import streamlit as st
import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv("C:\\Users\\SHUBHAM\\Desktop\\PROJECT 2\\filtered_df.csv")

# Clean the data
df = df.dropna()
df = df.drop_duplicates()
df["rating"] = df["rating"].astype(int)

# Write a function that returns the predicted condition
def predict_condition(review):
    # Import libraries
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.decomposition import TruncatedSVD
    from sklearn.svm import SVC
    
    # Create the feature matrix
    vectorizer = TfidfVectorizer(lowercase=True, stop_words="english")
    reviews = vectorizer.fit_transform(df["review"])

    # Reduce the dimensionality of the feature matrix
    svd = TruncatedSVD(n_components=500)
    reviews_reduced = svd.fit_transform(reviews)

    # Train the model
    model = SVC()
    model.fit(reviews_reduced, df["condition"])

    # Make prediction
    review = vectorizer.transform([review])
    review_reduced = svd.transform(review)
    condition = model.predict(review_reduced)[0]
    return condition

# Write a function that returns recommended drugs based on ratings
def recommend_drugs(review):
    condition = predict_condition(review)
    drug_ratings = df[df["condition"] == condition].groupby("drugName")["rating"].mean()
    recommended_drugs = drug_ratings.nlargest(5).index.tolist()
    return recommended_drugs

# Write a Streamlit app that allows the user to enter a review and receive recommendations
st.title("Patient's Condition Classification Using Drug Reviews")
review = st.text_input("Enter a patient review:")

if st.button("Predict Condition"):
    condition = predict_condition(review)
    st.write("Predicted Condition:", condition)

if st.button("Recommend Drugs"):
    recommended_drugs = recommend_drugs(review)
    st.write("Recommended Drugs:")
    for drug in recommended_drugs:
        st.write("-", drug)


st.markdown(
    f"""
    <style>
         .stApp {{
             background-image: url("https://www.missouripartnership.com/wp-content/uploads/2018/01/iStock-695349930.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
