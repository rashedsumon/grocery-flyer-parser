import streamlit as st
import pandas as pd
from excel_helpers.py import load_template, save_to_excel

st.set_page_config(page_title="Grocery Flyer QA", layout="wide")
st.title("Grocery Flyer QA & Export")

# File selector for CSV/JSON produced by Make.com (or fetch directly from Drive via API)
uploaded = st.file_uploader("Upload parse JSON or CSV file from Make.com", type=["json","csv"])
if uploaded:
    if uploaded.type.endswith("json"):
        df = pd.read_json(uploaded)
    else:
        df = pd.read_csv(uploaded)
    edited = st.experimental_data_editor(df, num_rows="dynamic")
    st.download_button("Export to Excel", data=save_to_excel(edited), file_name="final_output.xlsx")
