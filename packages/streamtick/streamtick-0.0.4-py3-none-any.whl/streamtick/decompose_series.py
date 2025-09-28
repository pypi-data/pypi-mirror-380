import streamlit as st
import plotly.graph_objects as go
import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose

from .data_acquisition import get_stock_data_by_years

def decompose_series(ticker: str, years: int):
    """
    decomposes the raw time series into its core components (Trend, Seasonality, Residuals).

    args:
        ticker (str): The stock ticker symbol (e.g., 'AAPL').
        years (int): The number of years of historical data to fetch.
    """
    st.subheader(f"Decomposition Analysis for {ticker}")

    # 1. fetch Data
    try:
        data = get_stock_data_by_years(ticker, years)
        if data.empty:
            st.error(f"No data fetched for {ticker}. Check the ticker symbol.")
            return

        # 2. column Selection (assume 'Close' price is present)
        close_price = data['Close']
    except Exception as e:
        st.error(f"Error during data acquisition: {e}")
        return

    # ensure the index is a DatetimeIndex for decomposition
    if not isinstance(close_price.index, pd.DatetimeIndex):
        close_price.index = pd.to_datetime(close_price.index)

    # 3. perform Multiplicative Decomposition
    # multiplicative model is often preferred for financial data where fluctuations scale with the price level.
    # period=252 is used for daily data in a trading year (252 trading days)
    try:
        # we need enough data to cover one period (252 days)
        if len(close_price) < 252 * 2: # check for at least 2 full periods for better results
             st.warning("Insufficient data. Decomposition works best with at least 2 years of data (approx 500 points).")

        decomposition = seasonal_decompose(close_price, model='multiplicative', period=252)
    except Exception as e:
        st.error(f"Error during decomposition. Ensure data is sampled daily and the period (252) is appropriate. Error: {e}")
        return

    # 4. create Plots for each component
    components = {
        "Original Series": decomposition.observed,
        "Trend Component": decomposition.trend,
        "Seasonality Component": decomposition.seasonal,
        "Residuals (Noise)": decomposition.resid
    }

    st.markdown("##### Multiplicative Decomposition Results")

    # use 2 columns for a clean, traditional dashboard look
    cols = st.columns(2)
    
    for i, (title, series) in enumerate(components.items()):
        # alternate columns for cleaner display
        with cols[i % 2]:
            st.markdown(f"**{title}**")
            
            fig = go.Figure()
            
            # use 'plotly_dark' template and a professional color
            fig.add_trace(go.Scatter(
                x=series.index, 
                y=series.values, 
                mode='lines', 
                name=title,
                line=dict(color="#143392", width=2) 
            ))
            
            # Update Y-axis title based on component
            y_title = "Value"
            if "Residuals" in title:
                y_title = "Multiplicative Factor"
            elif "Seasonality" in title:
                y_title = "Seasonal Factor"

            fig.update_layout(
                template="plotly_dark",
                margin=dict(l=20, r=20, t=30, b=20),
                xaxis_title="Date",
                yaxis_title=y_title
            )
            st.plotly_chart(fig, use_container_width=True)
