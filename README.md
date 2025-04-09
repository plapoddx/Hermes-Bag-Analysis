# 👜 Hermès Handbag Price Analysis

This project analyzes the global pricing of Hermès’ most iconic handbags using user-submitted data from the **PurseForum**. The data consists of handbag prices collected at the end of each year, shared by users across various countries.

## Project Overview

The goal of this analysis is to explore international price differences and trends in Hermès handbag pricing over time. The project involves:

- Extracting forum data from PurseForum posts
- Formatting and cleaning the raw text data
- Currency normalization using historical exchange rates
- Loading processed data into a PostgreSQL database
- Exploratory Data Analysis (EDA)

## Data Source

- **Forum**: [PurseForum](https://forum.purseblog.com/)
- **Data Type**: User-reported Hermès handbag prices
- **Timeframe**: Year-end posts (2019-2024)

## 📁 Project Structure
```bash
HERMES-BAG-ANALYSIS/
├── README.md                    # Project overview and documentation
├── main.ipynb                   # Notebook for development & testing
├── pipeline.ipynb               # Optional notebook version of pipeline
├── 2024-2019_raw.csv            # Raw handbag price data
├── con_checker.py               # PostgreSQL connection tester
├── currency_converter.py        # Historical currency conversion using ExchangeRatesAPI
├── load_data.py                 # Loads CSV data into DataFrame
├── pipeline.py                  # Finalized pipeline script (run-ready)
├── to_postgre.py                # Sends data to PostgreSQL (schema-aware)
└── transformation.py            # Extracts features from raw handbag descriptions
```

## Technologies Used
- Python
- Pandas (data manipulation)
- SQLAlchemy + psycopg2 (PostgreSQL ingestion)
- ExchangeRatesAPI (for historical currency conversion)
- PostgreSQL (data storage)
- Matplotlib / Seaborn (for visualizations)

## 🧱 Modularized Project Structure

This project was refactored from a monolithic Jupyter notebook into modular Python scripts using a separation of concerns approach. Each core function (e.g., data loading, transformation, currency conversion, and database ingestion) is now handled by its own file, improving reusability, readability, and maintainability.

## 🖥️ Database Setup with DBeaver

This project uses **PostgreSQL** for data storage, managed through [DBeaver](https://dbeaver.io/) — a free and user-friendly database management tool.

## Features Implemented

- ✅ Data extraction from forum text
- ✅ Cleaning and feature engineering (`Bag_Type`, `Material_Style`, `Leather`, etc.)
- ✅ Historical currency conversion with caching to reduce API calls
- ✅ PostgreSQL ingestion into specific schema/table
- ✅ Auto-creation of schema if missing
- ✅ Precision handling (2-decimal price rounding)
- 🔄 EDA and visualizations (in progress)

## How It Works

1. **Raw CSV Data** is loaded and cleaned using Pandas.
2. **Material and stitching information** are extracted using regex.
3. **Prices are normalized** using the ExchangeRatesAPI, with caching for performance.
4. **Data is stored in PostgreSQL** with a schema-aware, append-only strategy to prevent schema loss.
5. Visualizations and analysis steps follow.

## Future Plans

- Complete EDA: price distributions, stitching types, bag popularity
- Regional trend comparisons using normalized prices
- Build a dashboard (e.g., Streamlit or Tableau)
- Apply clustering or predictive modeling

## License
This project is for educational purposes only.

## Author
Hao Le  
[LinkedIn](https://linkedin.com/in/haonle) | haole7124@gmail.com