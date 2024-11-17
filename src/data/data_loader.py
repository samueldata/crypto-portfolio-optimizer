import yfinance as yf
import pandas as pd
import os

# Define the function before using it
def get_crypto_data(tickers, start, end):
    data = {}
    for ticker in tickers:
        df = yf.download(ticker, start=start, end=end)['Adj Close']
        data[ticker] = df.fillna(method='ffill').fillna(method='bfill')  # Fill missing data
    return pd.DataFrame(data)

# Set the path to the data directory
data_dir = os.path.join(os.getcwd(), 'data', 'processed')

# Get the list of tickers
tickers = ['BTC-USD', 'ETH-USD', 'BNB-USD', 'SOL-USD']

# Set the start and end dates
start_date = '2022-01-01'
end_date = '2023-01-01'

# Create the data directory if it doesn't exist
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

# Set the path to the output file
output_file = os.path.join(data_dir, 'crypto_data.csv')

# Get the crypto data and save it
crypto_data = get_crypto_data(tickers, start_date, end_date)
crypto_data.to_csv(output_file, index=True)

if __name__ == "__main__":
    print(f"Data saved to {output_file}")
