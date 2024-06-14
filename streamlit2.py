import streamlit as st
import Fine_Tunned_model

st.set_page_config(page_title="GenAI Proposals")  # HTML title
st.title("Proposals")  # Page title

col1, col2 = st.columns(2)

with col1:
    prompt_text = st.text_area("Enter Job Description", height=350)
    user_name = st.text_input("Enter your name", placeholder="Your name here")
    client_name = st.text_input("Enter Client's name", placeholder="Your client's name here")
    experience_year = st.text_input("Enter the years of experience", placeholder="Years of experience here")
    process_button = st.button("Run", type="primary")

with col2:
    if process_button:
        with st.spinner("Creating Proposal"):
            response = Fine_Tunned_model.llm_and_prompt(prompt_text, user_name, client_name, experience_year)
            st.write(response)
