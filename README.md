# F1 Race Performance & Strategy Analytics

A data analytics project analyzing Formula 1 race performance, driver pace, tyre strategy, stint performance, and lap-time consistency across three 2026 Grand Prix.

The project combines Python/Pandas, SQL, and Power BI to transform raw F1 session data into performance metrics and an interactive analytical dashboard.

---

## Project Overview

Formula 1 performance is influenced by much more than finishing position. Lap pace, tyre compound, tyre life, stint length, race conditions, and consistency all provide additional insight into how drivers and teams perform.

This project analyzes these factors across:

- 🇦🇺 Australian Grand Prix
- 🇨🇳 Chinese Grand Prix
- 🇯🇵 Japanese Grand Prix

The analysis focuses on identifying differences in driver performance, race pace, tyre usage, stint strategy, and consistency across races.

---

## Tech Stack

- **Python** — Data processing and analysis
- **Pandas / NumPy** — Data cleaning and transformation
- **SQL** — Race and driver-level analytical queries
- **Power BI** — Interactive dashboard and visualization
- **DAX** — Calculated performance metrics
- **FastF1 / F1 session data** — Formula 1 race data

---

## Project Workflow

```text
F1 Session Data
       ↓
Data Cleaning & Transformation
       ↓
Feature Engineering
       ↓
Python / Pandas Analysis
       ↓
Performance & Strategy Metrics
       ↓
Power BI Dashboard
```

---

## Analysis Performed

### Driver Performance

- Average representative lap time
- Best lap time
- Driver pace comparison
- Race-level performance comparison
- Finishing position

### Race Performance

- Lap-time consistency
- Lap-time standard deviation
- Driver performance across different circuits
- Race-level pace comparison

### Tyre & Strategy Analysis

- Tyre compound performance
- Average tyre pace
- Tyre life analysis
- Maximum stint length
- Driver stint strategies
- Comparison of tyre usage across races


## Power BI Dashboard

The project includes an interactive Power BI dashboard with three analytical pages.

### 1. Overview

Provides a high-level view of:

- Representative average lap time
- Best lap time
- Total laps
- Number of drivers
- Driver pace
- Race and driver comparisons

### 2. Tyre & Strategy Analysis

Explores:

- Maximum stint length by driver
- Maximum stint length by tyre compound
- Average tyre pace
- Tyre-life performance
- Race-level strategy differences

### 3. Race Performance

Focuses on:

- Driver finishing positions
- Representative average lap time
- Lap-time consistency
- Detailed race and driver comparisons

The dashboard includes interactive race filtering and conditional formatting to make performance differences easier to identify.

---

## Project Structure

```text
F1-Race-Performance-Analytics/
│
├── dashboard/
│   └── README.md
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── 01_data_exploration_all_races.ipynb
│   └── 02_performance_analysis.ipynb
│
├── src/
│   ├── data_loader.py
│   ├── download_f1_data.py
│   └── feature_engineering.py
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Key Takeaways

The analysis demonstrates that race performance cannot be evaluated using finishing position alone.

Driver pace, tyre usage, stint length, and lap-time consistency provide additional perspectives on race performance. Comparisons also need to account for differences between circuits, since lap times are not directly comparable across tracks.

The Power BI dashboard allows these metrics to be explored interactively across the three races.

---

## Data

The project uses Formula 1 session data containing lap timing, driver, team, tyre, stint, and race information.

Raw race data is excluded from the repository where appropriate. Processed analytical outputs are included to support reproducibility of the analysis.

---

## Reproducibility

### 1. Clone the repository

```bash
git clone https://github.com/spandhana-2128/F1-Race-Performance-Analytics.git
cd F1-Race-Performance-Analytics
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the notebooks

Open the notebooks in Jupyter or VS Code and run them in order:

```text
01_data_exploration_all_races.ipynb
02_performance_analysis.ipynb
```

---

## Limitations

- The analysis covers three 2026 Grand Prix rather than the complete season.
- Lap times vary naturally between circuits, so direct cross-circuit lap-time comparisons should be interpreted with race context.
- Race conditions, safety cars, traffic, pit stops, and other race events can affect lap times.
- The project focuses on descriptive and analytical insights rather than attempting to predict race outcomes.

---

