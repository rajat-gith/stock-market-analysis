import requests
import random
import time

# def fetch_current_stock_data(symbol):
#     api_key = 'your_alpha_vantage_api_key'
#     url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey=L31Y6SHETHU2ZVAO'
#     response = requests.get(url)
#     data = response.json()
#     return data

def fetch_current_stock_data(symbol):
    return {
        'Global Quote': {
            '01. symbol': symbol,
            '02. open': f"{random.uniform(100, 500):.2f}",
            '03. high': f"{random.uniform(100, 500):.2f}",
            '04. low': f"{random.uniform(100, 500):.2f}",
            '05. price': f"{random.uniform(100, 500):.2f}",
            '06. volume': f"{random.randint(1000, 1000000)}",
            '07. latest trading day': time.strftime('%Y-%m-%d'),
            '08. previous close': f"{random.uniform(100, 500):.2f}",
            '09. change': f"{random.uniform(-10, 10):.2f}",
            '10. change percent': f"{random.uniform(-5, 5):.2f}%"
        }
    }