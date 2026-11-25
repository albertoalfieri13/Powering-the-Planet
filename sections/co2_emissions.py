import streamlit as st
import matplotlib.pyplot as plt

from powering_planet.analysis import prepare_co2_data
from powering_planet.plots import plot_co2_emissions


def show_co2_emissions(df_co2):

    # Prepare CO2 data
    df_world_co2 = prepare_co2_data(df_co2)

    # Section title
    st.subheader("Global CO₂ Emissions")

    st.write(
        "Evolution of global CO₂ emissions from 1950 to 2022."
    )

    # Data preview
    st.write("Data preview:")

    st.write("First 3 observations:")
    st.dataframe(df_world_co2.head(3), hide_index=True)

    st.write("...")

    st.write("Last 3 observations:")
    st.dataframe(df_world_co2.tail(3), hide_index=True)

    # CO2 emissions chart
    fig = plot_co2_emissions(df_world_co2)

    st.pyplot(fig)
    plt.close(fig)