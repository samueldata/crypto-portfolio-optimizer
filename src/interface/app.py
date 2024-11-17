import streamlit as st
import pandas as pd
import sys
import os

# Add project root to PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

# Import necessary modules
from src.data.data_loader import get_crypto_data
from src.optimization.portfolio_optimizer import optimize_portfolio

st.title('Cryptocurrency Portfolio Optimization')

cryptos = st.multiselect('Select Cryptocurrencies', ['BTC-USD', 'ETH-USD', 'BNB-USD', 'SOL-USD'], ['BTC-USD'])
start_date = st.date_input('Start Date', value=pd.to_datetime('2022-01-01'))
end_date = st.date_input('End Date', value=pd.to_datetime('2023-01-01'))

if st.button('Optimize'):
    data = get_crypto_data(cryptos, str(start_date), str(end_date))
    if data.empty:
        st.write("No data available for the selected cryptocurrencies and dates.")
    else:
        weights, performance = optimize_portfolio(data)
        if weights is None:
            st.write("Optimization failed. Ensure the selected cryptocurrencies have valid data and expected returns.")
        else:
            st.write("Optimized Weights:", weights)
            st.write("Portfolio Performance:", performance)

