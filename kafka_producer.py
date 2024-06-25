import requests
import json
import time
import threading
from kafka import KafkaProducer

from fetch_data import fetch_current_stock_data

def produce_stock_data(symbol, producer):
    while True:
        data = fetch_current_stock_data(symbol)
        if 'Global Quote' in data:
            stock_data = data['Global Quote']
            record_value = json.dumps(stock_data)
            producer.send('topic-1', key=symbol.encode('utf-8'), value=record_value.encode('utf-8'))
            print(f"Stock data for {symbol}: {record_value}")
        else:
            print(f"Stock data not found for symbol: {symbol}")

        time.sleep(5)

def continuous_produce(producer):
    while True:
        producer.flush()
        time.sleep(0.2)

def main():
    producer = KafkaProducer(bootstrap_servers='13.53.41.31:9092')
    producer_thread = threading.Thread(target=continuous_produce, args=(producer,))
    producer_thread.daemon = True
    producer_thread.start()
    symbol = input("Enter a stock symbol (e.g., AAPL): ").strip().upper()
    produce_stock_data(symbol, producer)

if __name__ == "__main__":
    main()
