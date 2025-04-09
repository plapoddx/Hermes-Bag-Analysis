import requests
import time
import pandas as pd

def get_historical_rate(date, from_currency, to_currency, API_KEY):
    url = f"http://api.exchangeratesapi.io/v1/{date}?access_key={API_KEY}&base={from_currency}&symbols={to_currency}&format=1"
    
    try:
        response = requests.get(url)
        data = response.json()
        rate = data['rates'].get(to_currency)
        return rate
    except Exception as e:
        print(f"Error fetching rate for {date}, {from_currency}->{to_currency}: {e}")
        return None

def convert_historical_prices(df, date_col='Date_Purchased', currency_col='Currency', amount_col='Price', to_currency='USD'):
    converted_prices = []

    for idx, row in df.iterrows():
        date = pd.to_datetime(row[date_col]).strftime('%Y-%m-%d')
        from_currency = row[currency_col]
        amount = row[amount_col]

        rate = get_historical_rate(date, from_currency, to_currency, API_KEY='API_KEY')
        if from_currency != to_currency:
            converted_price = round(amount * rate, 2)
        else:
            converted_price = amount

        converted_prices.append(converted_price)

        time.sleep(0.1)  # to avoid rate limit (1 request/sec on free plan)

    df[f'Price_{to_currency}'] = converted_prices
    return df