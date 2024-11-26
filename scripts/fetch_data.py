import requests
import pandas as pd
from datetime import datetime

def fetch_crypto_data():
    # Fetch cryptocurrency data from CoinGecko API
    url = 'https://api.coingecko.com/api/v3/coins/markets'
    params = {
        'vs_currency': 'usd',
        'order': 'market_cap_desc',
        'per_page': 10,
        'page': 1,
        'sparkline': 'false'
    }
    response = requests.get(url, params=params)
    data = response.json()

    # Select required fields
    crypto_data = []
    for coin in data:
        crypto_data.append({
            'name': coin['name'],
            'symbol': coin['symbol'],
            'current_price': coin['current_price'],
            'market_cap': coin['market_cap'],
            'total_volume': coin['total_volume'],
            'date': datetime.now().strftime('%Y-%m-%d'),
            'time': datetime.now().strftime('%H:%M:%S')
        })

    # Save data to a CSV
    df = pd.DataFrame(crypto_data)
    df.to_csv('data/raw/raw_data.csv', index=False)
    print("Raw data saved as raw_data.csv")

if __name__ == "__main__":
    fetch_crypto_data()
