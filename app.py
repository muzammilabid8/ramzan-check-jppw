import pandas as pd
import streamlit as st
import time

st.set_page_config(page_title="Nigehban Ramzan Check Jalalpur Pirwala")

st.title("Nigehban Ramzan Check Jalalpur Pirwala")

st.write("This app includes about 2000 benefishries of Nigehban Ramazan Program Jalalpur Pirwala")

# Load CSV
@st.cache_data
def load_data():
    return pd.read_csv("Ramzanjppw1.csv")

df = load_data()

st.write("### Please enter your phone number")

phone = st.text_input("Phone Number")

search_button = st.button("Search")

if search_button:

    if phone.strip() == "":
        st.warning("Please enter phone number")
    else:
        with st.spinner("Searching your record..."):
            time.sleep(1.5)

            results = df[df.astype(str).apply(lambda x: x.str.contains(phone, case=False)).any(axis=1)]

        if len(results) > 0:
            st.success("Record Found ✅")
            st.write(results)
        else:
            st.error("No record found ❌")
