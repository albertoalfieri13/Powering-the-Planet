import streamlit as st
import matplotlib.pyplot as plt

from powering_planet.analysis import (
    prepare_co2_data,
    prepare_co2_region_data
)
from powering_planet.plots import (
    plot_co2_emissions,
    plot_co2_regions
)

from powering_planet.interpretations import CO2_INTERPRETATIONS

def show_co2_emissions(df_co2):

    # Prepare CO2 data
    df_world_co2 = prepare_co2_data(df_co2)

    # Prepare regional CO2 data
    df_co2_regions = prepare_co2_region_data(df_co2)

    # Section title
    st.subheader("Global CO₂ Emissions")

    st.write(
        "Evolution of global CO₂ emissions from 1950 to 2022."
    )

    # Data preview
    st.write("Data preview:")

    df_preview = df_world_co2[["year", "co2"]]

    st.write("First 3 observations:")
    st.dataframe(df_preview.head(3), hide_index=True)

    st.write("...")

    st.write("Last 3 observations:")
    st.dataframe(df_preview.tail(3), hide_index=True)

    # CO2 emissions chart
    fig = plot_co2_emissions(df_world_co2)

    st.pyplot(fig)
    plt.close(fig)  

           # Global CO2 interpretation
    st.subheader("Interpretation")

    st.write(
        CO2_INTERPRETATIONS["World"]
    )           

    # Regional CO2 emissions
    st.subheader("CO₂ Emissions by Region")

    regions = [
        "Europe", "North America", "South America",
        "Asia", "Africa", "Oceania"
    ]

    selected_regions = st.multiselect(
        "Select regions to compare:",
        options=regions,
        default=regions
    )

    # Regional CO2 emissions chart
    if selected_regions:

        fig = plot_co2_regions(
            df_co2_regions,
            selected_regions
        )

        st.pyplot(fig)
        plt.close(fig)

        # Regional interpretation
        if len(selected_regions) == 1:

            selected_region = selected_regions[0]

            st.subheader("Interpretation")

            st.write(
                CO2_INTERPRETATIONS[selected_region]
            )

    else:
        st.info("Select at least one region to display the chart.")

    