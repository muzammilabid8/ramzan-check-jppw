import pandas as pd
import streamlit as st
import time

st.set_page_config(page_title="Nigehban Ramzan Check Jalalpur Pirwala")

st.title("Nigehban Ramzan Check Jalalpur Pirwala")


# Load CSV
@st.cache_data
def load_data():
    return pd.read_csv("cleaned_ramzan.csv
")

df = load_data()

st.write("### Please Enter Phone Number without 0 as (3001234567)")

phone = st.text_input("Phone Number")

search_button = st.button("Search")

if search_button:

    if phone.strip() == "":
        st.warning("Please Enter Phone Number without 0 as (3001234567)")
    else:
        with st.spinner("Searching your record..."):
            time.sleep(1.5)

            results = df[df.astype(str).apply(lambda x: x.str.contains(phone, case=False)).any(axis=1)]

        if len(results) > 0:
            st.success("Mubarak Ho! Apka Name Nigehban Ramzan ki list me agya he. Apne Post Office se call ka wait karen or Apna Card Hasil Karen  ✅")
            st.write(results)
        else:
            st.error(" Apka Fund Manzoor Nahi Hua, Nayi List Ka Intizar Karen❌")
st.write("Is app men Nigehban Ramazan Program 2026 ke Jalalpur Pirwala ki list he")

st.write("##### Created by: Muzammil Abid")
