import streamlit as st
import plotly.express as px
import pandas as pd
from statsmodels.tsa.stattools import adfuller 
from .data_acquisition import get_stock_data_by_years 

def make_stationary(ticker: str, years: int):
    """
    fetches raw stock data, plots its raw time series, and then plots the 
    first-order differenced series to demonstrate stationarity.
    
    the 'I' (Integrated) component of ARIMA relies on this differencing step.

    args:
        ticker (str): The stock ticker symbol (e.g., 'AAPL').
        years (int): The number of years of historical data to fetch.
    """
    st.subheader(f"Stationarity Analysis for {ticker}")
    
    # 1. fetch Data
    try:
        data = get_stock_data_by_years(ticker, years)
        if data.empty:
            st.error(f"No data fetched for {ticker}. Check the ticker symbol.")
            return

        # 2. column Selection Logic (handles yfinance's single-ticker naming)
        if 'Close' in data.columns:
            close_price = data['Close']
        else:
            # fallback for old structure if fetching multiple tickers
            close_price = data[f'Close_{ticker}']

        
    except KeyError as e:
        st.error(f"Column not found. Data columns are: {list(data.columns)}. Ensure the data fetch was successful.")
        return
    except Exception as e:
        st.error(f"An unexpected error occurred during data processing: {e}")
        return

    # 3. perform Differencing (I component of ARIMA)
    diff_series = close_price.diff().dropna()

    # 4. create plots
    col1, col2 = st.columns(2)
    
    # plot 1: raw data (Non-Stationary)
    with col1:
        st.markdown("#### Raw Time Series (Non-Stationary)")
        fig_raw = px.line(close_price, title=f"Raw Close Price for {ticker}")
        fig_raw.update_layout(xaxis_title="Date", yaxis_title="Price ($)")
        st.plotly_chart(fig_raw, use_container_width=True)

    # plot 2: differenced data (stationary candidate)
    with col2:
        st.markdown("#### Differenced Time Series (Stationary Candidate)")
        fig_diff = px.line(diff_series, title=f"First Difference of Close Price")
        fig_diff.update_layout(xaxis_title="Date", yaxis_title="Daily Change ($)")
        st.plotly_chart(fig_diff, use_container_width=True)

    # 5. statistical check (Augmented Dickey-Fuller Test)
    st.markdown("---")
    st.markdown("##### Augmented Dickey-Fuller (ADF) Test Result (Statistical Confirmation)")
    
    # run ADF test on the differenced data
    adf_result = adfuller(diff_series)
    adf_p_value = adf_result[1]
    
    st.code(f"ADF p-value on DIFFERENCED data: {adf_p_value:.4f}")

    if adf_p_value < 0.05:
        st.success(f"The p-value ({adf_p_value:.4f}) is below 0.05. We reject the null hypothesis, meaning the differenced series is **STATISTICALLY STATIONARY**.")
    else:
        st.warning("The p-value is high. The differenced series may still contain trend or seasonality, and further differencing might be required.")
