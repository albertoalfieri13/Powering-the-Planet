import streamlit as st

from powering_planet.analysis import prepare_energy_mix_data
from powering_planet.plots import plot_energy_mix
from powering_planet.interpretations import ENERGY_INTERPRETATIONS
from powering_planet.config import CONTINENTS


def show_energy_mix(df_energy):

    # Prepare Energy Mix data
    df_mix = prepare_energy_mix_data(df_energy)

    # Continent selection
    selected_continent = st.selectbox(
        "Select a continent:",
        CONTINENTS
    )

    # Filter selected continent
    df_continent = df_mix[
        df_mix["country"] == selected_continent
    ].sort_values("year")

    st.write(f"Selected continent: {selected_continent}")

    # Data preview
    st.write("Data preview:")

    st.write("First 3 observations:")
    st.dataframe(df_continent.head(3), hide_index=True)

    st.write("...")

    st.write("Last 3 observations:")
    st.dataframe(df_continent.tail(3), hide_index=True)

    # Energy Mix chart
    fig = plot_energy_mix(df_mix, selected_continent)

    st.pyplot(fig)

    import matplotlib.pyplot as plt
    plt.close(fig)

    # Continent-specific interpretation
    st.markdown("### Interpretation")
    st.markdown(ENERGY_INTERPRETATIONS[selected_continent])

    # Comparative insights
    st.markdown("### Comparative Insights")

    st.markdown("""
    The comparison across continents highlights three main differences:

    - **Nuclear energy:** Europe and North America experienced an earlier expansion of nuclear energy, starting in the 1970s, while Asia followed a similar trend from the 1980s.

    - **Renewables:** South America stands out for having the highest renewables share, while Europe, North America and Asia experienced a more recent acceleration in renewable energy adoption.

    - **Regional patterns:** Africa shows relatively stable energy shares over time, whereas Oceania broadly follows the trends observed in Europe, Asia and North America, with the notable absence of nuclear energy.
    """)