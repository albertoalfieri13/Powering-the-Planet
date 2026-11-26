import streamlit as st
import matplotlib.pyplot as plt

from powering_planet.analysis import (
    prepare_co2_data,
    prepare_gdp_vs_co2_data,
    calculate_global_regression,
    prepare_country_continent_data,
    aggregate_continent_data,
    prepare_recent_continent_data,
    calculate_continent_regressions
)

from powering_planet.plots import (
    plot_gdp_vs_co2,
    plot_global_gdp_co2_regression,
    plot_continent_gdp_co2_regressions
)

from powering_planet.interpretations import (
    GDP_CO2_INTERPRETATIONS,
    GDP_CONTINENT_INTERPRETATIONS
)


def show_gdp_vs_co2(df_co2):

    # Section title
    st.subheader("GDP vs CO₂")

    st.write(
        "Comparison between economic growth and CO₂ emissions."
    )

    # Prepare global data
    df_world_co2 = prepare_co2_data(df_co2)
    df_comparison = prepare_gdp_vs_co2_data(df_world_co2)

    # Display global data preview
    st.write("Data preview:")

    df_preview = df_comparison[
        ["year", "gdp_index", "co2_index"]
    ]

    st.write("First 3 observations:")
    st.dataframe(df_preview.head(3), hide_index=True)

    st.write("Last 3 observations:")
    st.dataframe(df_preview.tail(3), hide_index=True)

    # Display global GDP and CO2 comparison
    fig = plot_gdp_vs_co2(df_comparison)
    st.pyplot(fig)
    plt.close(fig)

    # Global trend interpretation
    st.subheader("Global trend interpretation")
    st.write(GDP_CO2_INTERPRETATIONS["trend"])

    # Calculate and display global regression
    regression_results = calculate_global_regression(df_world_co2)

    fig = plot_global_gdp_co2_regression(
        df_world_co2,
        regression_results
    )

    st.pyplot(fig)
    plt.close(fig)

    # Display global statistical indicators
    correlation = regression_results[4]
    r_squared = regression_results[5]

    st.write(f"Correlation coefficient: {correlation:.3f}")
    st.write(f"R-squared: {r_squared:.3f}")

    # Global regression interpretation
    st.subheader("Global regression analysis")
    st.write(GDP_CO2_INTERPRETATIONS["regression"])

    # Prepare GDP and CO2 data by continent
    _, df_analysis = prepare_country_continent_data(df_co2)
    df_continents = aggregate_continent_data(df_analysis)

    # Select continents for regional comparison
    st.subheader("GDP vs CO₂ by continent")

    continents = ["Europe", "North America", "Asia"]

    selected_continents = st.multiselect(
        "Select continents:",
        options=continents,
        default=continents
    )

    if selected_continents:

        # Compare continents over the full period
        regression_results = calculate_continent_regressions(
            df_continents
        )

        fig = plot_continent_gdp_co2_regressions(
            regression_results,
            selected_continents,
            "1950-2022"
        )

        st.pyplot(fig)
        plt.close(fig)

        # Explain the focus on the recent period
        # Explain why the recent period is analysed separately
        st.markdown("""
        **Why focus on 2000–2022?**

        A closer look at the recent period helps highlight a change
        in the relationship between economic growth and CO₂ emissions.
        In Europe and North America, emissions have started to decline
        despite continued GDP growth, while Asia maintains a positive
        relationship. This makes a separate analysis of the recent
        period particularly relevant.
        """)

        # Compare continents over the recent period
        recent_continent_data = prepare_recent_continent_data(
            df_continents
        )

        recent_regression_results = calculate_continent_regressions(
            recent_continent_data
        )

        fig = plot_continent_gdp_co2_regressions(
            recent_regression_results,
            selected_continents,
            "2000-2022"
        )

        st.pyplot(fig)
        plt.close(fig)

        # Display detailed interpretations when one continent is selected
        if len(selected_continents) == 1:

            selected_continent = selected_continents[0]

            st.subheader(
                f"{selected_continent}: interpretation (1950-2022)"
            )

            st.write(
                GDP_CONTINENT_INTERPRETATIONS["1950-2022"][
                    selected_continent
                ]
            )

            st.subheader(
                f"{selected_continent}: interpretation (2000-2022)"
            )

            st.write(
                GDP_CONTINENT_INTERPRETATIONS["2000-2022"][
                    selected_continent
                ]
            )