import streamlit as st
import matplotlib.pyplot as plt

from powering_planet.analysis import prepare_per_capita_data
from powering_planet.plots import plot_per_capita


def show_per_capita(df_co2):

    # Prepare per capita data
    df_co2_regions = prepare_per_capita_data(df_co2)

    # Section title
    st.subheader("CO₂ Emissions per Capita")

    st.write(
        "Comparison of CO₂ emissions per capita across geographical regions from 1950 to 2022."
    )

    # CO2 emissions per capita chart
    fig = plot_per_capita(df_co2_regions)

    st.pyplot(fig)
    plt.close(fig)