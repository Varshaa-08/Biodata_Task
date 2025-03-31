import streamlit as st
import requests

# FastAPI backend URL
API_URL = "https://biodata-task.onrender.com"

st.title("Biodata")

# Input form
with st.form("user_form"):
    name = st.text_input("Enter your name:")
    age = st.number_input("Enter your age:", min_value=1, step=1)
    submit = st.form_submit_button("Submit")

# When form is submitted, send data to FastAPI
if submit and name and age:
    response = requests.post(f"{API_URL}/add_user/", json={"name": name, "age": age})
    if response.status_code == 200:
        st.success("User added successfully!")
    else:
        st.error("Error adding user.")

# Show a link to view logged users in Render (as an HTML table)
st.subheader("View Logged Users:")
st.markdown(f"[Click here to see users](https://biodata-task.onrender.com/get_users/)", unsafe_allow_html=True)
