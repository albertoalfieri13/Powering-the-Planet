
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


# PAGE CONFIGURATION
st.set_page_config(
    page_title="Powering the Planet",
    page_icon="🌍",
    layout="wide"
)


# MAIN TITLE
st.title("🌍 Powering the Planet")

st.write(
    "Exploring the global energy transition "
    "and its environmental impact."
)


# SIDEBAR NAVIGATION
st.sidebar.title("Navigation")

section = st.sidebar.radio(
    "Choose an analysis:",
    [
        "Introduction",
        "Energy Mix",
        "CO₂ Emissions",
        "GDP vs CO₂",
        "Per Capita Analysis"
    ]
)


# INTRODUCTION
if section == "Introduction":

    st.markdown("""
    🌍 Welcome to Powering the Planet

    Understanding the global energy transition

    Energy is at the heart of modern economic development. However, the way countries produce and consume energy has significant consequences for the environment, particularly in terms of CO₂ emissions.

    **Powering the Planet** explores the relationship between energy consumption, economic growth and environmental sustainability through historical global data.

    ### What will you explore?

    - **Energy Mix:** How has the global energy mix evolved over time? What role do fossil fuels and renewable sources play across continents?
    - **CO₂ Emissions:** How have carbon emissions changed across different regions?
    - **GDP vs CO₂:** Is economic growth necessarily associated with higher carbon emissions?
    - **Per Capita Analysis:** How do environmental footprints differ when population size is taken into account?

    ### Explore the data

    Use the navigation menu to move between analyses and the continent selector to compare different geographical regions.

    The objective is to understand not only how energy systems have changed, but also whether economic development can become increasingly sustainable.
    """)


# LOAD ENERGY DATA
@st.cache_data
def load_energy_data():

    url = "https://raw.githubusercontent.com/owid/energy-data/master/owid-energy-data.csv"

    return pd.read_csv(url)


df_energy = load_energy_data()


# ENERGY MIX DATA
mix_columns = [
    'coal_share_energy',
    'oil_share_energy',
    'gas_share_energy',
    'nuclear_share_energy',
    'renewables_share_energy'
]

df_mix = df_energy[
    (df_energy['country'] != 'World') &
    (df_energy['year'] >= 1965)
][['country', 'year'] + mix_columns].dropna(
    subset=mix_columns,
    how='all'
)


# CONTINENT SELECTION
continents = [
    'Africa',
    'Asia',
    'Europe',
    'North America',
    'Oceania',
    'South America'
]

if section != "Introduction":

    selected_continent = st.selectbox(
        "Select a continent:",
        continents
    )

    # Filter selected continent
    df_continent = df_mix[
        df_mix['country'] == selected_continent
    ].sort_values('year')


# ENERGY MIX SECTION
if section == "Energy Mix":

    st.write(f"Selected continent: {selected_continent}")

    # Data preview
    st.write("Data preview:")

    st.write("First 3 observations:")
    st.dataframe(df_continent.head(3), hide_index=True)

    st.write("...")

    st.write("Last 3 observations:")
    st.dataframe(df_continent.tail(3), hide_index=True)

    # Prepare chart data
    df_chart = df_continent.dropna(
        subset=mix_columns
    ).copy()

    df_chart['total_fossil'] = (
        df_chart['coal_share_energy'] +
        df_chart['gas_share_energy'] +
        df_chart['oil_share_energy']
    )

    # Create Energy Mix chart
    fig, ax = plt.subplots(figsize=(12, 6))

    ax.stackplot(
        df_chart['year'],
        df_chart['total_fossil'],
        df_chart['nuclear_share_energy'],
        df_chart['renewables_share_energy'],
        labels=['Fossil Fuels', 'Nuclear', 'Renewables'],
        alpha=0.85
    )

    ax.set_title(f'Evolution of Energy Mix - {selected_continent}')
    ax.set_xlabel('Year')
    ax.set_ylabel('Share of Primary Energy (%)')
    ax.set_ylim(0, 100)
    ax.set_xlim(1965, 2024)
    ax.margins(x=0)

    ax.legend(loc='upper left')
    ax.grid(True, linestyle='--', alpha=0.5)

    plt.tight_layout()
    st.pyplot(fig)
    plt.close(fig)


    # CONTINENT-SPECIFIC INTERPRETATION

    interpretations = {
        'Europe': """
        Europe's energy transition shows two distinct phases.
        Nuclear energy expanded rapidly from the early 1970s until the
        mid-1980s, after which its growth slowed and eventually stabilized
        or declined around the beginning of the 21st century.
        Renewables maintained a relatively stable share until approximately
        2005, before experiencing sustained growth through 2025.
        """,

        'North America': """
        North America experienced rapid growth in nuclear energy from
        the early 1970s until the mid-1980s, followed by a slowdown and
        eventual stabilization or decline. Renewables remained relatively
        stable until approximately 2005, after which their share began
        to increase steadily through 2025.
        """,

        'Asia': """
        Asia experienced a later expansion of nuclear energy, beginning
        in the 1980s. Its growth slowed after the mid-1980s and eventually
        stabilized or declined around the beginning of the 21st century.
        Renewables maintained a relatively stable share until approximately
        2012, before starting a sustained increase through 2025.
        """,

        'South America': """
        South America presents a distinctive energy mix, with the highest
        renewables share among all continents. Renewables experienced
        particularly rapid growth between 1970 and 1990, highlighting
        the different energy development pattern of this region.
        """,

        'Africa': """
        Africa displays a relatively stable energy mix throughout the
        period considered. Unlike other continents, the shares of its
        main energy sources show comparatively limited changes over time.
        """,

        'Oceania': """
        Oceania broadly follows the energy transition pattern observed
        in Europe and North America, with changes in the relative shares
        of fossil fuels and renewables over time. One distinctive feature
        is the complete absence of nuclear energy in its energy mix
        throughout the period considered.
        """
    }

  
    # CONTINENT-SPECIFIC INTERPRETATION

    interpretations = {
        'Europe': """
        Europe's energy transition shows two distinct phases.
        Nuclear energy expanded rapidly from the early 1970s until the
        mid-1980s, after which its growth slowed and eventually stabilized
        or declined around the beginning of the 21st century.
        Renewables maintained a relatively stable share until approximately
        2005, before experiencing sustained growth through 2025.
        """,

        'North America': """
        North America experienced rapid growth in nuclear energy from
        the early 1970s until the mid-1980s, followed by a slowdown and
        eventual stabilization or decline. Renewables remained relatively
        stable until approximately 2005, after which their share began
        to increase steadily through 2025.
        """,

        'Asia': """
        Asia experienced a later expansion of nuclear energy, beginning
        in the 1980s. Its growth slowed after the mid-1980s and eventually
        stabilized or declined around the beginning of the 21st century.
        Renewables maintained a relatively stable share until approximately
        2012, before starting a sustained increase through 2025.
        """,

        'South America': """
        South America presents a distinctive energy mix, with the highest
        renewables share among all continents. Renewables experienced
        particularly rapid growth between 1970 and 1990, highlighting
        the different energy development pattern of this region.
        """,

        'Africa': """
        Africa displays a relatively stable energy mix throughout the
        period considered. Unlike other continents, the shares of its
        main energy sources show comparatively limited changes over time.
        """,

        'Oceania': """
        Oceania broadly follows the energy transition pattern observed
        in Europe and North America, with changes in the relative shares
        of fossil fuels and renewables over time. One distinctive feature
        is the complete absence of nuclear energy in its energy mix
        throughout the period considered.
        """
    }

  
    # CONTINENT-SPECIFIC INTERPRETATION

    interpretations = {
        'Europe': """
        Europe's energy transition shows two distinct phases.
        Nuclear energy expanded rapidly from the early 1970s until the
        mid-1980s, after which its growth slowed and eventually stabilized
        or declined around the beginning of the 21st century.
        Renewables maintained a relatively stable share until approximately
        2005, before experiencing sustained growth through 2025.
        """,

        'North America': """
        North America experienced rapid growth in nuclear energy from
        the early 1970s until the mid-1980s, followed by a slowdown and
        eventual stabilization or decline. Renewables remained relatively
        stable until approximately 2005, after which their share began
        to increase steadily through 2025.
        """,

        'Asia': """
        Asia experienced a later expansion of nuclear energy, beginning
        in the 1980s. Its growth slowed after the mid-1980s and eventually
        stabilized or declined around the beginning of the 21st century.
        Renewables maintained a relatively stable share until approximately
        2012, before starting a sustained increase through 2025.
        """,

        'South America': """
        South America presents a distinctive energy mix, with the highest
        renewables share among all continents. Renewables experienced
        particularly rapid growth between 1970 and 1990, highlighting
        the different energy development pattern of this region.
        """,

        'Africa': """
        Africa displays a relatively stable energy mix throughout the
        period considered. Unlike other continents, the shares of its
        main energy sources show comparatively limited changes over time with an overall majority of fossil fuels.
        """,

        'Oceania': """
        Oceania broadly follows the energy transition pattern observed
        in Europe and North America, with a transition from fossil fuels to renewables over time. One distinctive feature
        is the complete absence of nuclear energy in its energy mix
        throughout the period considered.
        """
    }

    st.markdown("### Interpretation")
    st.markdown(interpretations[selected_continent])


    # COMPARATIVE INSIGHTS

    st.markdown("### Comparative Insights")

    st.markdown("""
    The comparison across continents highlights three main differences:

    - **Nuclear energy:** Europe and North America experienced an earlier expansion of nuclear energy, starting in the 1970s, while Asia followed a similar trend from the 1980s.

    - **Renewables:** South America stands out for having the highest renewables share, while Europe, North America and Asia experienced a more recent acceleration in renewable energy adoption.

    - **Regional patterns:** Africa shows relatively stable energy shares over time, whereas Oceania broadly follows the trends observed in Europe, Asia and North America, with the notable absence of nuclear energy.
    """)






