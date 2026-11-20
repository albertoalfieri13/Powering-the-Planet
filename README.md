# Powering the Planet

## Project Overview

**Powering the Planet** explores the global energy transition and its relationship with economic development and environmental impact.

Using historical data from [Our World in Data](https://ourworldindata.org/), this project investigates how energy production and consumption have evolved over time and examines the relationship between economic growth, population and CO₂ emissions.

The analysis aims to address three main questions:

1. How has the global energy mix changed over time, and what role have renewable energy sources played in the transition?
2. How are economic growth and CO₂ emissions related across different geographical regions?
3. How do per capita emissions differ between regions, and what do these differences reveal about their environmental impact?

## Data Sources

The project primarily relies on datasets provided by **Our World in Data**:

- [Our World in Data – Energy Dataset](https://github.com/owid/co2-data?utm_source=chatgpt.com)
- [Our World in Data – CO₂ and Greenhouse Gas Emissions](https://github.com/owid/co2-data?utm_source=chatgpt.com)

This project uses the legacy versions of the Our World in Data datasets, accessed through their public GitHub repositories.

The datasets provide historical information on energy sources, CO₂ emissions, GDP and population.

## Methodology

The analysis is conducted using Python and includes:

- Data loading, cleaning and preparation.
- Exploration of historical energy trends.
- Geographical aggregation and regional comparisons.
- Analysis of the relationship between GDP and CO₂ emissions.
- Comparison of absolute and per capita emissions.
- Data visualization and interpretation of the results.

Particular attention is given to Europe, North America and Asia, while other geographical regions are also considered where relevant.

## Technologies and Libraries

- Python
- Pandas
- NumPy
- Matplotlib
- Pycountry-convert
- Jupyter Notebook

## Project Structure

```text
Powering-the-Planet/
│
├── Powering the Planet.ipynb
├── README.md
├── requirements.txt
└── .gitignore
```

## Installation and Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/albertoalfieri13/Powering-the-Planet.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Powering-the-Planet
   ```

3. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   ```

   On Windows:

   ```powershell
   .venv\Scripts\activate
   ```

4. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Launch Jupyter Notebook or open the notebook in Visual Studio Code and execute the cells.

## Author

Alberto Alfieri