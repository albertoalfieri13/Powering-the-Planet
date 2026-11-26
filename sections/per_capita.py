import streamlit as st
import matplotlib.pyplot as plt

from powering_planet.analysis import prepare_per_capita_data
from powering_planet.plots import plot_per_capita
from powering_planet.interpretations import PER_CAPITA_INTERPRETATION


def show_per_capita(df_co2):

    # Section title
    st.subheader("CO₂ Emissions per Capita")

    st.write(
        "Comparison of CO₂ emissions per capita across geographical regions from 1950 to 2022."
    )

    # Prepare per capita data
    df_co2_regions = prepare_per_capita_data(df_co2)

    # Select geographical regions
    regions = [
        "Europe",
        "North America",
        "Asia",
        "South America",
        "Africa",
        "Oceania",
        "World"
    ]

    selected_regions = st.multiselect(
        "Select regions:",
        options=regions,
        default=regions
    )

    # Display chart only when at least one region is selected
    if selected_regions:

                # Display relevant data preview
        st.write("Data preview:")

        df_preview = df_co2_regions[
            df_co2_regions["country"].isin(selected_regions)
        ][["country", "year", "co2_per_capita"]]

        st.write("First 3 observations:")
        st.dataframe(df_preview.head(3), hide_index=True)

        st.write("Last 3 observations:")
        st.dataframe(df_preview.tail(3), hide_index=True)

        # Display per capita emissions chart
        fig = plot_per_capita(
            df_co2_regions,
            selected_regions
        )

        st.pyplot(fig)
        plt.close(fig)

        # Display interpretation
        st.subheader("Interpretation")

        st.write(PER_CAPITA_INTERPRETATION)

    else:
        st.info("Select at least one region to display the analysis.")