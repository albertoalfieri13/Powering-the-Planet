import streamlit as st

from powering_planet.data import load_energy_data, load_co2_data

from sections.introduction import show_introduction
from sections.energy_mix import show_energy_mix
from sections.co2_emissions import show_co2_emissions
from sections.gdp_vs_co2 import show_gdp_vs_co2
from sections.per_capita import show_per_capita



# PAGE CONFIGURATION
st.set_page_config(
    page_title="Powering the Planet",
    page_icon="🌍",
    layout="wide"
)


# MAIN TITLE
st.title("🌍 Powering the Planet")

st.write(
    "Exploring the global energy transition "
    "and its environmental impact."
)


# SIDEBAR NAVIGATION
st.sidebar.title("Navigation")

section = st.sidebar.radio(
    "Choose an analysis:",
    [
        "Introduction",
        "Energy Mix",
        "CO₂ Emissions",
        "GDP vs CO₂",
        "Per Capita Analysis"
    ]
)


# INTRODUCTION
if section == "Introduction":

    show_introduction()


# ENERGY MIX
elif section == "Energy Mix":

    df_energy = load_energy_data()
    show_energy_mix(df_energy)


# CO2 EMISSIONS
elif section == "CO₂ Emissions":

    df_co2 = load_co2_data()
    show_co2_emissions(df_co2)


# GDP VS CO2
elif section == "GDP vs CO₂":
    df_co2 = load_co2_data()
    show_gdp_vs_co2(df_co2)

# PER CAPITA ANALYSIS
elif section == "Per Capita Analysis":

    df_co2 = load_co2_data()
    show_per_capita(df_co2)