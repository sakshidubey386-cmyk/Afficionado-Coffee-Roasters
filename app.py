import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Afficionado Coffee Roasters", layout="wide")
st.title("☕ Afficionado Coffee Roasters - Sales Dashboard")
st.markdown("Peak hours, Monthly sales & Store performance")

# Try to load data - will look for common csv names
@st.cache_data
def load_data():
    for name in ["Coffee.csv", "coffee.csv", "Afficionado Coffee Roasters.xlsx", "data.csv"]:
        try:
            if name.endswith(".xlsx"):
                return pd.read_excel(name)
            else:
                return pd.read_csv(name)
        except:
            continue
    return None

df = load_data()

if df is None:
    st.warning("Data file nahi mila. Please 'Coffee.csv' upload karo repo me.")
    st.info("Dashboard ka structure ready hai, data upload karte hi graphs aa jayenge.")
else:
    st.success(f"Data loaded: {df.shape[0]} rows")
    st.dataframe(df.head())

    # Basic charts if columns exist
    if 'transaction_time' in df.columns or 'Date' in df.columns:
        st.subheader("Sales Trend")
        st.line_chart(df.select_dtypes(include='number').iloc[:,0])

st.sidebar.header("About")
st.sidebar.write("Power BI dashboard for sales analysis - Peak hours, trend, Monthly sales 2025")
