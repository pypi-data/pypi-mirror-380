# streamtick/model_identification.py

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from statsmodels.tsa.stattools import acf, pacf

# Import core library functions using relative pathing
from .data_acquisition import get_stock_data_by_years
from .data_preprocessing import preprocess_data

def check_autocorrelation(ticker: str, years: int):
    """
    analyzes and plots the autocorrelation function (ACF) and partial autocorrelation
    function (PACF) of the differenced time series.

    the plots are essential for visually identifying the optimal p (AR) and q (MA)
    parameters for an ARIMA model based on the Box-Jenkins methodology.
    """
    st.subheader(f"ACF and PACF for Differenced {ticker}")
    
    # 1. data acquisition and differencing (Ensuring Stationarity)
    try:
        # fetch the raw data
        raw_df = get_stock_data_by_years(ticker, years)
        if raw_df.empty:
            st.error(f"Error: Could not fetch data for ticker {ticker}.")
            return
        
        # pass the DataFrame to preprocess_data
        processed_data = preprocess_data(raw_df) 
        
        column_name = f"Close_{ticker}" 
        close_series = processed_data[column_name] 
        
        # differencing the series (d=1, same as in make_stationary)
        diff_series = close_series.diff().dropna()
        
    except KeyError:
        st.error(f"Error: Could not find the '{column_name}' column in the processed data. Ticker name may be incorrect or data is missing.")
        return
    except Exception as e:
        st.error(f"An unexpected error occurred during analysis: {e}")
        return

    # 2. aalculate ACF and PACF values
    # the confidence interval is set to 95% (alpha=0.05)
    lag_count = min(30, len(diff_series) // 2 - 1)
    
    # calculate ACF values and confidence bounds
    acf_values, acf_conf_int = acf(diff_series.values, nlags=lag_count, alpha=0.05, fft=True)
    
    # calculate PACF values and confidence bounds
    # method 'ywm' is used by default for PACF in statsmodels, so we explicitly use 'ywm'
    pacf_values, pacf_conf_int = pacf(diff_series.values, nlags=lag_count, alpha=0.05, method='ywm')

    # convert confidence intervals to upper/lower bounds
    acf_conf_lower = acf_conf_int[:, 0] - acf_values
    acf_conf_upper = acf_conf_int[:, 1] - acf_values
    
    pacf_conf_lower = pacf_conf_int[:, 0] - pacf_values
    pacf_conf_upper = pacf_conf_int[:, 1] - pacf_values
    
    lags = np.arange(len(acf_values))

    # Plotting Function
    def plot_correlation(corr_values, conf_lower, conf_upper, title, y_label):
        fig = go.Figure()

        # 1. add confidence band (shaded area)
        fig.add_trace(go.Scatter(
            x=lags, 
            y=conf_upper, 
            line=dict(width=0),
            mode='lines', 
            fill=None,
            showlegend=False
        ))
        
        fig.add_trace(go.Scatter(
            x=lags, 
            y=conf_lower,
            line=dict(width=0),
            mode='lines',
            fill='tonexty', # Fill the area between this trace and the previous trace (conf_upper)
            fillcolor='rgba(0, 204, 204, 0.2)', # Semi-transparent teal/cyan shading
            name='95% Confidence Band',
            showlegend=False
        ))
        
        # 2. Add Correlation Bars (The main values)
        for i, val in enumerate(corr_values):
            fig.add_trace(go.Bar(
                x=[lags[i]],
                y=[val],
                marker_color="#2427D9", 
                name=f'Lag {lags[i]}',
                showlegend=False
            ))

        fig.update_layout(
            title=title,
            xaxis_title='Lag',
            yaxis_title=y_label,
            template="plotly_dark", 
            xaxis=dict(tickmode='linear', tick0=0, dtick=1), # ensuring integer lags are shown
            yaxis=dict(range=[-1, 1]),
            height=400,
            margin=dict(l=20, r=20, t=40, b=20)
        )
        # add a line at y=0
        fig.add_hline(y=0, line_width=1, line_dash="solid", line_color="#444444")
        return fig

    # 3. displaying plots in streamlit
    col_acf, col_pacf = st.columns(2)
    
    with col_acf:
        acf_fig = plot_correlation(
            acf_values, 
            acf_conf_lower, 
            acf_conf_upper, 
            "Autocorrelation Function (ACF)", 
            "Correlation"
        )
        st.plotly_chart(acf_fig, use_container_width=True)
        st.markdown(
            "**ACF Interpretation (q):** The **Moving Average (q)** order is typically identified by the point where the correlation bars **drop significantly into the shaded confidence band**."
        )

    with col_pacf:
        pacf_fig = plot_correlation(
            pacf_values, 
            pacf_conf_lower, 
            pacf_conf_upper, 
            "Partial Autocorrelation Function (PACF)", 
            "Partial Correlation"
        )
        st.plotly_chart(pacf_fig, use_container_width=True)
        st.markdown(
            "**PACF Interpretation (p):** The **Autoregressive (p)** order is typically identified by the point where the partial correlation bars **drop significantly into the shaded confidence band**."
        )
