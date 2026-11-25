
import streamlit as st
import pandas as pd

from powering_planet.config import ENERGY_DATA_URL, CO2_DATA_URL

#streamlit takes the data previously loaded
@st.cache_data
def load_energy_data():
    return pd.read_csv(ENERGY_DATA_URL)


@st.cache_data
def load_co2_data():
    return pd.read_csv(CO2_DATA_URL)
