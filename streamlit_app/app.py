import streamlit as st
import pandas as pd
from excel_helpers import save_to_excel   # only import what exists

st.set_page_config(page_title="Grocery Flyer QA", layout="wide")
st.title("Grocery Flyer QA & Export")

# File uploader for JSON or CSV produced by Make.com
uploaded = st.file_uploader(
    "Upload parsed JSON or CSV file from Make.com",
    type=["json", "csv"]
)

if uploaded:
    # Load data into a DataFrame
    if uploaded.name.endswith(".json"):
        df = pd.read_json(uploaded)
    else:
        df = pd.read_csv(uploaded)

    st.subheader("Parsed Data (editable)")
    edited = st.experimental_data_editor(df, num_rows="dynamic")

    # Export button
    st.download_button(
        "Export to Excel",
        data=save_to_excel(edited),
        file_name="flyer_output.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
