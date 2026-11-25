
import numpy as np
import pycountry_convert as pc

from powering_planet.config import START_YEAR, ENERGY_COLUMNS


# ENERGY MIX ANALYSIS

# Select energy data, excluding World and years before START_YEAR as incomplete rows.
def prepare_energy_mix_data(df):
    """Prepare the dataset for the Energy Mix analysis."""

    df_mix = df[
        (df["country"] != "World") &
        (df["year"] >= START_YEAR)
    ][["country", "year"] + ENERGY_COLUMNS].dropna(
        subset=ENERGY_COLUMNS,
        how="all"
    )

    return df_mix


# Calculate the total share of the five main energy sources for each year.
def prepare_world_energy_mix_data(df_world):
    """Calculate the total share of the five main energy sources by year."""

    df_world_with_total = df_world.copy()

    df_world_with_total["total_share"] = df_world_with_total[ENERGY_COLUMNS].sum(
        axis=1,
        min_count=len(ENERGY_COLUMNS)
    )

    return df_world_with_total


# Keep regional observations and calculates the total fossil fuel share.
def prepare_regional_energy_mix_data(df_regions):
    """Prepare complete regional observations and aggregate fossil fuels."""

    df_regional_mix = df_regions.dropna(subset=ENERGY_COLUMNS).copy()

    df_regional_mix["total_fossil"] = (
        df_regional_mix["coal_share_energy"] +
        df_regional_mix["gas_share_energy"] +
        df_regional_mix["oil_share_energy"]
    )

    return df_regional_mix.sort_values("year")


# Prepare global data for the energy transition chart.
def prepare_world_energy_transition_data(df_regions):
    """Prepare global energy shares for the 1965-2024 transition chart."""

    df_world = df_regions[df_regions["country"] == "World"].copy()

    df_world["total_fossil"] = (
        df_world["coal_share_energy"] +
        df_world["gas_share_energy"] +
        df_world["oil_share_energy"]
    )

    # Keep observations from 1965 to 2024.
    df_world = df_world[df_world["year"].between(1965, 2024)]

    # Groups data by year and calculates the average share of each category.
    df_plot = (
        df_world.groupby("year")[
            ["total_fossil", "nuclear_share_energy", "renewables_share_energy"]
        ].mean().reset_index()
    )

    return df_plot.sort_values("year")


def prepare_renewables_comparison_data(df_regions):
    """Select the regions used for the renewable energy comparison."""

    target_regions = [
        "Europe", "North America", "Asia",
        "South America", "Africa", "Oceania", "World"
    ]

    return df_regions[
        df_regions["country"].isin(target_regions)
    ].copy()


# CO2 ANALYSIS

# Select the most relevant CO2 variables from 1950 onwards and removes observations with missing values.
def prepare_co2_analysis_data(df):
    """Select the core CO2 variables from 1950 onwards and remove incomplete rows."""

    columns_of_interest = [
        "country",
        "year",
        "co2",
        "gdp",
        "population"
    ]

    df_co2_analysis = df[columns_of_interest]
    df_co2_analysis = df_co2_analysis[df_co2_analysis["year"] >= 1950]
    df_co2_analysis = df_co2_analysis.dropna(
        subset=["co2", "gdp", "population"]
    )

    return df_co2_analysis


# Select global observations and sorts them by year.
def prepare_co2_data(df):
    """Prepare global CO2 data for the emissions analysis."""

    df_co2_analysis = prepare_co2_analysis_data(df)

    df_world_co2 = df_co2_analysis[
        df_co2_analysis["country"] == "World"
    ]

    return df_world_co2.sort_values("year")


# Select the seven regions considered for the CO2 analysis, keeping only the period from 1950 to 2022.
def prepare_co2_region_data(df):
    """Select regional CO2 and population data for 1950-2022."""

    regions = [
        "Europe", "North America", "South America",
        "Asia", "Africa", "Oceania", "World"
    ]

    df_co2_regions = df[
        df["country"].isin(regions)
    ][["country", "year", "co2", "population"]]

    return df_co2_regions[
        df_co2_regions["year"].between(1950, 2022)
    ].copy()


# Calculate GDP and CO2 indexes using 1950 as the base year (100).
def prepare_gdp_vs_co2_data(df_world_co2):
    """Calculate GDP and CO2 indexes using 1950 as the base year (100)."""

    df_world_co2 = df_world_co2.sort_values("year").copy()

    df_world_co2["co2_index"] = (
        df_world_co2["co2"] /
        df_world_co2["co2"].iloc[0] * 100
    )

    df_world_co2["gdp_index"] = (
        df_world_co2["gdp"] /
        df_world_co2["gdp"].iloc[0] * 100
    )

    return df_world_co2


# COUNTRY-TO-CONTINENT AND CONTINENTAL GDP/CO2 ANALYSIS

# Convert ISO country code into the corresponding continent
def get_continent(iso):
    """Convert a three-letter ISO country code into a continent name."""

    try:
        country_alpha2 = pc.country_alpha3_to_country_alpha2(iso)
        continent_code = pc.country_alpha2_to_continent_code(country_alpha2)
        return pc.convert_continent_code_to_continent_name(continent_code)
    except:
        return None


# Add continent names to country data and excludes Antarctica and observations without an assigned continent.
def prepare_country_continent_data(df_co2):
    """Add continent names to country data and exclude Antarctica/unassigned rows."""

    df_gdp_co2_countries = df_co2[
        (df_co2["year"].between(1950, 2022)) &
        (df_co2["iso_code"].notna())
    ][["country", "iso_code", "year", "gdp", "co2", "population"]].copy()

    # Apply get_continent to each ISO country code.
    df_gdp_co2_countries["continent"] = (
        df_gdp_co2_countries["iso_code"].apply(get_continent)
    )

    df_analysis = df_gdp_co2_countries[
        (df_gdp_co2_countries["continent"] != "Antarctica") &
        (df_gdp_co2_countries["continent"].notna())
    ].copy()

    return df_gdp_co2_countries, df_analysis


# Aggregate GDP, CO2 emissions and population by continent and year.
def aggregate_continent_data(df_analysis):
    """Aggregate GDP, CO2 and population by continent and year."""

    df_continents = (
        df_analysis
        .groupby(["continent", "year"], as_index=False).agg(
            gdp=("gdp", lambda x: x.sum(min_count=1)),
            co2=("co2", lambda x: x.sum(min_count=1)),
            population=("population", lambda x: x.sum(min_count=1))
        )
    )

    # Calculate CO2 emissions per capita.
    df_continents["co2_per_capita"] = (
        df_continents["co2"] * 1_000_000 /
        df_continents["population"]
    )

    return df_continents


# Calculate the global linear regression, correlation and R-squared.
def calculate_global_regression(df_world_co2):
    """Calculate the linear regression, correlation and R-squared for global GDP/CO2."""

    x = df_world_co2["gdp"]
    y = df_world_co2["co2"]

    # Calculate the slope and intercept of the regression line.
    slope, intercept = np.polyfit(x, y, 1)

    # Generate points used to draw the regression line.
    x_line = np.linspace(x.min(), x.max(), 100)
    y_line = slope * x_line + intercept

    correlation = np.corrcoef(x, y)[0, 1]
    r_squared = correlation ** 2

    return slope, intercept, x_line, y_line, correlation, r_squared


def prepare_recent_continent_data(df_continents):
    """Select Europe, North America and Asia for the 2000-2022 comparison."""

    return df_continents[
        (df_continents["continent"].isin(
            ["Europe", "North America", "Asia"]
        )) &
        (df_continents["year"].between(2000, 2022))
    ].copy()



# Calculate a separate GDP-CO2 regression for each of the three continents.
def calculate_continent_regressions(df_continents):
    """Calculate GDP-CO2 linear regressions and R-squared for each continent."""

    continents = ["Europe", "North America", "Asia"]
    regression_results = {}

    for continent in continents:

        # Select and sort the observations for the current continent.
        df_temp = df_continents[
            df_continents["continent"] == continent
        ].sort_values("year")

        x = df_temp["gdp"] / 1_000_000_000_000
        y = df_temp["co2"]

        # Calculate the regression line.
        slope, intercept = np.polyfit(x, y, 1)

        # Generate points for plotting the regression line.
        x_line = np.linspace(x.min(), x.max(), 100)
        y_line = slope * x_line + intercept

        # Calculate R-squared for further analysis
        ss_res = np.sum((y - (slope * x + intercept)) ** 2)
        ss_tot = np.sum((y - y.mean()) ** 2)

        r_squared = 1 - (ss_res / ss_tot)

        # Store the results for the current continent.
        regression_results[continent] = {
            "x": x,
            "y": y,
            "x_line": x_line,
            "y_line": y_line,
            "r_squared": r_squared
        }

    return regression_results


# Prepare regional data to compare CO2 emissions per capita.
def prepare_per_capita_data(df_co2):
    """Prepare regional CO2 emissions per capita for 1950-2022."""

    df_co2_regions = prepare_co2_region_data(df_co2)

    df_co2_regions["co2_per_capita"] = (
        df_co2_regions["co2"] * 1_000_000 /
        df_co2_regions["population"]
    )

    return df_co2_regions
