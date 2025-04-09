import logging
from load_data import load_csv
from transformation import split_and_clean
from currency_converter import convert_historical_prices
from to_postgre import pipe_to_sql
from con_checker import test_postgres_connection

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()]
)

# Pipeline:
def main():
    source = '2024-2019_raw.csv'
    logging.info("Starting Hermes data pipeline...")
    
    # Step 0 - Testing Connection
    if not test_postgres_connection():
        logging.error('FAILED: PostgreSQL connection failed. Pipeline stopped.')
        return
    
    # Step 1 - Loading Data
    try:
        data = load_csv(source)
        logging.info(f"SUCCESS: Loaded data from '{source}' — {len(data)} rows.")
    except Exception as e:
        logging.exception(f"FAILED: Failed to Load Data from '{source}' ")

    #Step 2 - Cleaning Data
    try: 
        cleaned = split_and_clean(data)
        logging.info('SUCCESS: Data Cleaning and Transformation Completed')
    except Exception as e:
        logging.exception('FAILED: Failed to be Converted & Transformed')
        
    # Step 3 - Rates conversion to USD using ExchangerateAPI.io 
    try:
        ready = convert_historical_prices(cleaned)
        logging.info('SUCCESS: Currency Conversion Completed')
    except Exception as e:
        logging.exception('FAILED: Currency Conversion not Complete. Please Check API Settings/Subscriptions')
        
    
    # Step 4 - Send to Database
    try:
        transported = pipe_to_sql(ready, table_name='handbag', schema='hermes')
        logging.info('SUCCESS: Data loaded into PostgreSQL.')
    except Exception as e:
        logging.exception('FAILED: Data was not able to be loaded into PostgreSQL. Please Check Connection.')
        
    logging.info("SUCCESS: Pipeline complete! Check your Database now!")
    
    return ready