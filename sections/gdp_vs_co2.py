import streamlit as st
import matplotlib.pyplot as plt

from powering_planet.analysis import (
    prepare_gdp_vs_co2_data,
    calculate_global_regression
)

from powering_planet.plots import (
    plot_gdp_vs_co2,
    plot_global_gdp_co2_regression
)

from powering_planet.interpretations import GDP_CO2_INTERPRETATIONS


def show_gdp_vs_co2(df_world_co2):

    # Section title
    st.subheader("GDP vs CO₂")

    st.write(
        "Comparison between global economic growth and CO₂ emissions."
    )

    # Prepare GDP and CO2 data
    df_comparison = prepare_gdp_vs_co2_data(df_world_co2)

    # Data preview
    st.write("Data preview:")

    df_preview = df_comparison[
        ["year", "gdp_index", "co2_index"]
    ]

    st.write("First 3 observations:")
    st.dataframe(df_preview.head(3), hide_index=True)

    st.write("Last 3 observations:")
    st.dataframe(df_preview.tail(3), hide_index=True)

    # GDP and CO2 comparison chart
    fig = plot_gdp_vs_co2(df_comparison)

    st.pyplot(fig)
    plt.close(fig)

    # GDP and CO2 trend interpretation
    st.subheader("Interpretation")

    st.write(
        GDP_CO2_INTERPRETATIONS["trend"]
    )

    # Calculate global GDP-CO2 regression
    regression_results = calculate_global_regression(df_world_co2)

    # Display GDP-CO2 regression chart
    fig = plot_global_gdp_co2_regression(
        df_world_co2,
        regression_results
    )

    st.pyplot(fig)
    plt.close(fig)

    # Display statistical indicators
    correlation = regression_results[4]
    r_squared = regression_results[5]

    st.write(
        f"Correlation coefficient: {correlation:.3f}"
    )

    st.write(
        f"R-squared: {r_squared:.3f}"
    )

    # Regression interpretation
    st.subheader("Regression analysis")

    regression_text = GDP_CO2_INTERPRETATIONS["regression"]

    st.write(regression_text)