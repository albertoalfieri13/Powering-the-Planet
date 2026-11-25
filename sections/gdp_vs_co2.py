import streamlit as st
import matplotlib.pyplot as plt

from powering_planet.analysis import prepare_gdp_vs_co2_data
from powering_planet.plots import plot_gdp_vs_co2


def show_gdp_vs_co2(df_world_co2):

    # Prepare GDP and CO2 data
    df_comparison = prepare_gdp_vs_co2_data(df_world_co2)

    # Section title
    st.subheader("GDP vs CO₂")

    st.write(
        "Comparison between global economic growth and CO₂ emissions."
    )

    # GDP and CO2 comparison chart
    fig = plot_gdp_vs_co2(df_comparison)

    st.pyplot(fig)
    plt.close(fig)