import numpy as np
import streamlit as st
import pandas as pd
import altair as alt




# LOADING DATA
DATE_TIME = "date/time"
DATA_URL = (
    "http://s3-us-west-2.amazonaws.com/streamlit-demo-data/uber-raw-data-sep14.csv.gz"
)

st.title("UBER pickups in NEW YORK city")
st.markdown(
"""
## This is a demo of a STREAMLIT app that shows the Uber pickups gepgraphical dostribution in NY city. Use the slider to pick a specific hour
## and look at how the charts change.
""" )

@st.cache(persist=True)
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis="columns", inplace=True)
    data[DATE_TIME] = pd.to_datetime(data[DATE_TIME])
    return data

data = load_data(100000)
print(data.head)
#'data', data
hour = st.sidebar.slider('hour',0,23,11)
data = data[data[DATE_TIME].dt.hour== hour]

'## Geo Data at %sh' %hour
st.map(data)
#hour = st.slider("")
