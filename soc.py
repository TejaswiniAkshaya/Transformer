import streamlit as st
from transformers import pipeline

pipe = pipeline('sentiment-analysis')

# Set the title and add introductory text
st.title("Sentiment Analysis App")
st.write("This simple app analyzes the sentiment of your text.")

# Use 'form' to group input elements together
with st.form("sentiment_form"):
    # Input for text to analyze sentiment
    text = st.text_area("Enter text for sentiment analysis:")

    # Add a button with a label
    submit_button = st.form_submit_button("Analyze Sentiment")

# Check if the form was submitted
if text and submit_button:
    # Analyze sentiment
    out = pipe(text)
    result = out[0]  # Assuming you want the first result if multiple are returned
    sentiment = result["label"]
    score = round(result["score"], 2)  # Round the score to two decimal places

    # Display sentiment analysis results
    st.header("Sentiment Analysis Result")
    st.write(f"Sentiment: {sentiment}")
    st.write(f"Sentiment Score: {score}")

# Add a section for instructions on how to use the app
st.header("How to Use")
st.write("1. Enter text in the text area above.")
st.write("2. Click the 'Analyze Sentiment' button to analyze the sentiment.")
st.write("3. The sentiment label and score will be displayed below.")
