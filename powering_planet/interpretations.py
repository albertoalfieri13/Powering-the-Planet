ENERGY_INTERPRETATIONS = {
    "Europe": """
    Europe's energy transition shows two distinct phases.
    Nuclear energy expanded rapidly from the early 1970s until the
    mid-1980s, after which its growth slowed and eventually stabilized
    or declined around the beginning of the 21st century.
    Renewables maintained a relatively stable share until approximately
    2005, before experiencing sustained growth through 2025.
    """,

    "North America": """
    North America experienced rapid growth in nuclear energy from
    the early 1970s until the mid-1980s, followed by a slowdown and
    eventual stabilization or decline. Renewables remained relatively
    stable until approximately 2005, after which their share began
    to increase steadily through 2025.
    """,

    "Asia": """
    Asia experienced a later expansion of nuclear energy, beginning
    in the 1980s. Its growth slowed after the mid-1980s and eventually
    stabilized or declined around the beginning of the 21st century.
    Renewables maintained a relatively stable share until approximately
    2012, before starting a sustained increase through 2025.
    """,

    "South America": """
    South America presents a distinctive energy mix, with the highest
    renewables share among all continents. Renewables experienced
    particularly rapid growth between 1970 and 1990, highlighting
    the different energy development pattern of this region.
    """,

    "Africa": """
    Africa displays a relatively stable energy mix throughout the
    period considered. Unlike other continents, the shares of its
    main energy sources show comparatively limited changes over time with an overall majority of fossil fuels.
    """,

    "Oceania": """
    Oceania broadly follows the energy transition pattern observed
    in Europe and North America, with a transition from fossil fuels to renewables over time. One distinctive feature
    is the complete absence of nuclear energy in its energy mix
    throughout the period considered.
    """
}

CO2_INTERPRETATIONS = {
    "World": """
    Global CO2 emissions generally increased between 1950 and 2022,
    although the growth rate varied across decades.
    A particularly noticeable acceleration occurred from the early
    2000s. Emissions temporarily declined in 2020, corresponding
    to the COVID-19 pandemic, before recovering rapidly.
    """,

    "Europe": """
    European CO2 emissions stabilized and began to decline from
    the early 1990s, showing a different trend from rapidly
    industrializing regions such as Asia.
    """,

    "North America": """
    North American CO2 emissions stabilized and gradually declined
    from the early 1990s, following a period of substantial growth
    during the previous decades.
    """,

    "Asia": """
    Asian CO2 emissions continued to grow throughout the period,
    with a particularly sharp acceleration from the early 2000s.
    This trend contrasts with the stabilization observed in Europe
    and North America.
    """,

    "South America": """
    South American CO2 emissions increased over the period
    considered, although they remained considerably lower in
    absolute terms than those of the world's largest emitters.
    """,

    "Africa": """
    African CO2 emissions increased over time, while remaining
    relatively low in absolute terms compared with the world's
    largest emitting regions.
    """,

    "Oceania": """
    CO2 emissions in Oceania increased over the period considered,
    although their absolute levels remained relatively low
    compared with those of larger regions.
    """
}

GDP_CO2_INTERPRETATIONS = {
    "trend": """
    GDP and CO2 emissions follow a similar trend: both increase
    steadily until 2000, when their growth rates become noticeably
    steeper. Both also experience a temporary decline during the
    COVID-19 period, followed by a rapid rebound.

    Overall, GDP has a higher growth rate than CO2 emissions,
    suggesting relative decoupling: emissions continue to grow,
    but at a significantly slower rate than GDP.
    """,

    "regression": """
    Overall, there appears to be a strong positive correlation
    between GDP and CO2 emissions, confirmed by the correlation
    coefficient. Furthermore, the R-squared value indicates that
    the linear regression model explains a large proportion of
    the variation in CO2 emissions.

    However, this strong correlation does not necessarily imply
    causation, as both variables have followed an upward trend
    over time. At higher GDP levels, corresponding to more recent
    years, CO2 emissions appear to have grown at a significantly
    slower rate than GDP, suggesting possible relative decoupling.

    Nevertheless, this observation should be interpreted
    cautiously, as the high correlation may partly reflect the
    common upward trends of the two variables rather than a
    direct economic relationship.
    """
}