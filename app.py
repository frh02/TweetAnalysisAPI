import streamlit as st
import requests

API_URL = "http://localhost:8000"  # Replace with your FastAPI API URL

st.title("Sentiment Analysis App")

# Input text box
text_input = st.text_area("Enter a tweet:", "")

if st.button("Predict"):
    if text_input:
        payload = {"text": text_input}
        response = requests.post(f"{API_URL}/predict", json=payload)
        
        if response.status_code == 200:
            result = response.json()
            st.subheader("Prediction:")
            st.write(f"Sentiment: {result['label']}")
            st.write(f"Confidence: {result['confidence']:.2f}")
            
            st.subheader("Probabilities:")
            for sentiment, probability in result['probabilities'].items():
                st.write(f"{sentiment}: {probability:.2f}")
        else:
            st.write("Error occurred while making a prediction.")
