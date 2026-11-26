import matplotlib.pyplot as plt

from powering_planet.config import ENERGY_COLUMNS


def plot_energy_mix(df, continent):
    """
    Create a stacked area chart showing the evolution
    of the energy mix in the selected continent.
    """

    # Filter selected continent
    df_continent = df[
        df["country"] == continent
    ].sort_values("year")

    # Prepare chart data
    df_chart = df_continent.dropna(
        subset=ENERGY_COLUMNS
    ).copy()

    df_chart["total_fossil"] = (
        df_chart["coal_share_energy"] +
        df_chart["gas_share_energy"] +
        df_chart["oil_share_energy"]
    )

    # Create Energy Mix chart
    fig, ax = plt.subplots(figsize=(12, 6))

    ax.stackplot(
        df_chart["year"],
        df_chart["total_fossil"],
        df_chart["nuclear_share_energy"],
        df_chart["renewables_share_energy"],
        labels=["Fossil Fuels", "Nuclear", "Renewables"],
        alpha=0.85
    )

    ax.set_title(f"Evolution of Energy Mix - {continent}")
    ax.set_xlabel("Year")
    ax.set_ylabel("Share of Primary Energy (%)")
    ax.set_ylim(0, 100)
    ax.set_xlim(1965, 2024)
    ax.margins(x=0)

    ax.legend(loc="upper left")
    ax.grid(True, linestyle="--", alpha=0.5)

    plt.tight_layout()

    return fig


def plot_co2_emissions(df):
    """
    Create a line chart showing the evolution
    of global CO2 emissions from 1950 to 2022.
    """

    fig, ax = plt.subplots(figsize=(12, 6))

    ax.plot(
        df["year"],
        df["co2"]
    )

    ax.set_title("Global CO₂ Emissions (1950-2022)")
    ax.set_xlabel("Year")
    ax.set_ylabel("CO2 emissions (million tonnes)")
    ax.grid(True, alpha=0.3)

    plt.tight_layout()

    return fig

def plot_co2_regions(df, selected_regions):
    """Create two charts comparing selected CO2 regions."""

    # Keep the original regional groups
    target_regions_1 = [
        region for region in ["Europe", "North America", "Asia"]
        if region in selected_regions
    ]

    target_regions_2 = [
        region for region in ["South America", "Africa", "Oceania"]
        if region in selected_regions
    ]

    fig, axes = plt.subplots(1, 2, figsize=(16, 6), sharey=True)

    for ax, target_regions in zip(
        axes,
        [target_regions_1, target_regions_2]
    ):

        if not target_regions:
            ax.set_visible(False)
            continue

        # Add the World as a reference
        target_regions = target_regions + ["World"]

        for region in target_regions:
            df_temp = df[
                df["country"] == region
            ].sort_values("year")

            ax.plot(
                df_temp["year"],
                df_temp["co2"],
                label=region,
                linewidth=2.5 if region == "World" else 2,
                linestyle="--" if region == "World" else "-"
            )

        ax.set_xlabel("Year")
        ax.set_xlim(1950, 2022)
        ax.grid(True, linestyle="--", alpha=0.4)
        ax.legend()

    axes[0].set_title("Major Energy Consumers")
    axes[1].set_title("Other Regions")
    axes[0].set_ylabel("CO2 emissions (million tonnes)")

    fig.suptitle("CO₂ Emissions by Region (1950-2022)")

    plt.tight_layout()
    return fig


def plot_gdp_vs_co2(df):
    """
    Create a line chart comparing global GDP and CO2 emissions growth.
    """

    fig, ax = plt.subplots(figsize=(12, 6))

    ax.plot(
        df["year"],
        df["co2_index"],
        label="CO2 emissions"
    )

    ax.plot(
        df["year"],
        df["gdp_index"],
        label="GDP"
    )

    ax.set_title("Global GDP and CO₂ Emissions Growth (1950-2022)")
    ax.set_xlabel("Year")
    ax.set_ylabel("Index (1950 = 100)")

    ax.legend()
    ax.grid(True, alpha=0.3)

    plt.tight_layout()

    return fig
def plot_global_gdp_co2_regression(df_world_co2, regression_results):
    """Create a scatter plot with the global GDP-CO2 regression line."""

    slope, intercept, x_line, y_line, correlation, r_squared = regression_results

    x = df_world_co2["gdp"]
    y = df_world_co2["co2"]

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.scatter(
        x,
        y,
        alpha=0.6,
        label="Annual observations"
    )

    ax.plot(
        x_line,
        y_line,
        color="red",
        label="Linear regression"
    )

    ax.set_title(
        "Relationship between Global GDP and CO₂ Emissions (1950-2022)"
    )
    ax.set_xlabel("GDP")
    ax.set_ylabel("CO2 emissions (million tonnes)")
    ax.legend()
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    return fig



def plot_per_capita(df, selected_regions):
    """
    Create charts comparing CO2 emissions per capita
    across selected geographical regions.
    """

    # Define the two groups of regions
    target_regions_1 = ["Europe", "North America", "Asia", "World"]
    target_regions_2 = ["South America", "Africa", "Oceania", "World"]

    # Keep only selected regions in each group
    groups = [
        [region for region in target_regions_1 if region in selected_regions],
        [region for region in target_regions_2 if region in selected_regions]
    ]

    # Remove empty groups
    groups = [group for group in groups if group]

    # Create the charts
    fig, axes = plt.subplots(
        1,
        len(groups),
        figsize=(8 * len(groups), 6),
        sharey=True,
        squeeze=False
    )

    # Plot the selected regions
    for ax, target_regions in zip(axes[0], groups):

        for region in target_regions:

            df_temp = df[
                df["country"] == region
            ].sort_values("year")

            ax.plot(
                df_temp["year"],
                df_temp["co2_per_capita"],
                label=region,
                linewidth=2.5 if region == "World" else 2,
                linestyle="--" if region == "World" else "-"
            )

        # Configure each chart
        ax.set_xlabel("Year")
        ax.set_xlim(1950, 2022)
        ax.grid(True, linestyle="--", alpha=0.4)
        ax.legend()

    # Add titles and labels
    if len(groups) == 2:
        axes[0, 0].set_title("Major Energy Consumers")
        axes[0, 1].set_title("Other Regions")
    else:
        axes[0, 0].set_title("Selected Regions")

    axes[0, 0].set_ylabel(
        "CO2 emissions per capita (tonnes/person/year)"
    )

    fig.suptitle("CO₂ Emissions per Capita by Region (1950-2022)")

    plt.tight_layout()

    return fig



def plot_world_energy_mix(df):
    """Create a stacked area chart of the global energy mix."""

    df_chart = df.dropna(subset=ENERGY_COLUMNS).sort_values("year")

    fig, ax = plt.subplots(figsize=(12, 6))

    ax.stackplot(
        df_chart["year"],
        *[df_chart[col] for col in ENERGY_COLUMNS],
        labels=["Coal", "Oil", "Gas", "Nuclear", "Renewables"],
        alpha=0.85
    )

    ax.set_title("Historical Evolution of World's Primary Energy Mix")
    ax.set_xlabel("Year")
    ax.set_ylabel("Share of Primary Energy (%)")
    ax.set_xlim(1965, 2024)
    ax.set_ylim(0, 100)
    ax.legend(loc="upper left")
    ax.grid(True, linestyle="--", alpha=0.5)

    plt.tight_layout()
    return fig


def plot_world_energy_transition(df):
    """Create a stacked area chart of the global energy transition."""

    fig, ax = plt.subplots(figsize=(12, 6))

    ax.stackplot(
        df["year"],
        df["total_fossil"],
        df["nuclear_share_energy"],
        df["renewables_share_energy"],
        labels=["Fossil Fuels", "Nuclear", "Renewables"],
        alpha=0.85
    )

    ax.set_title("Global Energy Transition (1965-2024)")
    ax.set_xlabel("Year")
    ax.set_ylabel("Share of Primary Energy (%)")
    ax.set_xlim(1965, 2024)
    ax.set_ylim(0, 100)
    ax.legend(loc="upper left")
    ax.grid(True, linestyle="--", alpha=0.5)

    plt.tight_layout()
    return fig



def plot_regional_energy_mix(df):
    """Create six stacked area charts comparing regional energy mixes."""

    continents = [
        "Europe", "North America", "Asia",
        "South America", "Africa", "Oceania"
    ]

    fig, axes = plt.subplots(2, 3, figsize=(18, 10))

    for ax, continent in zip(axes.flatten(), continents):

        df_continent = df[
            df["country"] == continent
        ].sort_values("year")

        ax.stackplot(
            df_continent["year"],
            df_continent["total_fossil"],
            df_continent["nuclear_share_energy"],
            df_continent["renewables_share_energy"],
            labels=["Fossil Fuels", "Nuclear", "Renewables"],
            alpha=0.85
        )

        ax.set_title(continent)
        ax.set_xlabel("Year")
        ax.set_ylabel("Share of Primary Energy (%)")
        ax.set_xlim(1965, 2024)
        ax.set_ylim(0, 100)
        ax.grid(True, linestyle="--", alpha=0.5)

    axes[0, 0].legend(loc="upper left")

    plt.tight_layout()
    return fig



def plot_renewables_comparison(df):
    """Compare renewable energy shares across geographical regions."""

    target_regions_1 = [
        "Europe", "North America", "Asia", "World"
    ]

    target_regions_2 = [
        "South America", "Africa", "Oceania", "World"
    ]

    fig, axes = plt.subplots(
        1, 2,
        figsize=(16, 6),
        sharey=True
    )

    for ax, target_regions in zip(
        axes,
        [target_regions_1, target_regions_2]
    ):
        for region in target_regions:

            df_temp = df[
                df["country"] == region
            ].sort_values("year")

            ax.plot(
                df_temp["year"],
                df_temp["renewables_share_energy"],
                label=region,
                linewidth=2.5 if region == "World" else 2,
                linestyle="--" if region == "World" else "-"
            )

        ax.set_xlabel("Year")
        ax.set_xlim(1965, 2022)
        ax.grid(True, linestyle="--", alpha=0.4)
        ax.legend()

    axes[0].set_title("Major Energy Consumers")
    axes[1].set_title("Other Regions")
    axes[0].set_ylabel("Renewables Share of Primary Energy (%)")

    fig.suptitle("Renewables Share of Primary Energy by Region (1965-2022)")

    plt.tight_layout()
    return fig

def plot_continent_gdp_co2_regressions(regression_results, selected_continents, period):

    # Create one chart for each selected continent.
    fig, axes = plt.subplots(
        1,
        len(selected_continents),
        figsize=(6 * len(selected_continents), 5),
        squeeze=False
    )

    for ax, continent in zip(axes[0], selected_continents):

        results = regression_results[continent]

        # Display annual observations and regression line.
        ax.scatter(
            results["x"],
            results["y"],
            alpha=0.6,
            label="Annual observations"
        )

        ax.plot(
            results["x_line"],
            results["y_line"],
            color="red",
            label="Linear regression"
        )

        # Add chart title and labels.
        ax.set_title(
            f"{continent} (R² = {results['r_squared']:.3f})"
        )
        ax.set_xlabel("GDP (trillion dollars)")
        ax.set_ylabel("CO₂ emissions (million tonnes)")
        ax.legend()
        ax.grid(True, alpha=0.3)

    fig.suptitle(
        f"GDP vs CO₂ Emissions by Continent ({period})"
    )

    plt.tight_layout()

    return fig