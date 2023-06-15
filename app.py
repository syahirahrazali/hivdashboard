import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

st.set_page_config(page_title="HIV Dashboard",
                   page_icon="hiv.png",
                   layout="wide"
)

def get_data_from_excel():
    df = pd.read_excel(
            io = 'datahiv.xlsx',
            engine= 'openpyxl',
            usecols='B:R',
            nrows=1000,
    )
    return df
df=get_data_from_excel()

st.title("HIV CASES IN MALAYSIA (2018-2021)")

st.sidebar.header("Please Filter Here:")
country = st.sidebar.multiselect(
    "Select the Country:",
    options=df["Country"].unique(),
    default=df["Country"].unique(),
)

year = st.sidebar.multiselect(
    "Select the Year:",
    options=df["Year"].unique(),
    default=df["Year"].unique(),
)

df_selection = df.query(
    "Country == @country & Year == @year"
)

st.markdown("##")

total_case = int(df_selection["Total"].sum())
average_case = round(df_selection["Average"].mean(),1)


left_column, middle_column, right_column = st.columns(3)

with middle_column:
    st.subheader("Total Cases:")
    st.subheader(f"{total_case}")

with right_column:
    st.subheader("Average Case:")
    st.subheader(f"{average_case}")

st.markdown("---")
left_column, right_column = st.columns(2)
with left_column:
    st.subheader("HIV Table of Dataset")
    st.dataframe(df_selection)
with right_column:
    st.subheader(" Total Cases by Year")
    c_data = pd.DataFrame(
    np.random.randn(100, 4),
    columns=['2018', '2019', '2020', '2021'])
    st.line_chart(c_data)

@st.cache_data
def load_data(nrows):
    data = pd.read_csv('hivdataset.csv', nrows=nrows)
    return data

weekly_data = load_data(1000)
left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.subheader("Cases in Kuala Lumpur")
    st.bar_chart(weekly_data["Kuala Lumpur"])
    df = pd.DataFrame(weekly_data[:200], columns=['Johor', 'Kedah', 'Kelantan'])
    df.hist()
with middle_column:
    st.subheader("Cases in 14 States")
    chart_data = pd.DataFrame(weekly_data[:40],
                              columns=['Johor', 'Kedah', 'Kelantan', 'Melaka', 'Negeri Sembilan', 'Pahang', 'Perak',
                                       'Perlis'
                                       'Pulau Pinang', 'Sabah', 'Sarawak', 'Terengganu', 'Kuala Lumpur', 'Labuan'])
    st.area_chart(chart_data)
with right_column:
    st.subheader("Total Cases in 3 States by year")
    st.line_chart(df)
# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)