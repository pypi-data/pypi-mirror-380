import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from .data_acquisition import get_stock_data_by_years
from .data_preprocessing import preprocess_data
from .arima import build_arima_models

def analyze_stock_ui():
    """
    this function contains the complete Streamlit UI logic for the stock analysis
    and ARIMA forecasting dashboard.
    """
    # --- Main Page UI ---
    st.header("Dynamic Stock ARIMA Forecast Dashboard")

    # Use st.session_state to manage the list of tickers and analysis results
    if 'analysis_tickers' not in st.session_state:
        st.session_state.analysis_tickers = [''] # Start with one empty cell
    if 'analysis_results' not in st.session_state:
        st.session_state.analysis_results = {} # Dictionary to store results

    # Dynamically create a section for each added stock
    for ticker_id in range(len(st.session_state.analysis_tickers)):
        st.write("---")
        
        col1, col2, col3 = st.columns([0.4, 0.4, 0.2])
        with col1:
            current_ticker = st.text_input("Ticker Symbol", value=st.session_state.analysis_tickers[ticker_id], key=f"ticker_input_{ticker_id}")
        with col2:
            years_to_fetch = st.number_input("Years of Data", min_value=1, max_value=10, value=3, key=f"years_input_{ticker_id}")
        with col3:
            run_btn = st.button("Run Analysis", key=f"run_btn_{ticker_id}")

        if run_btn:
            if current_ticker.strip() == '':
                st.error("Please enter a valid stock ticker.")
            else:
                with st.spinner(f"Running analysis for {current_ticker}..."):
                    st.session_state.analysis_tickers[ticker_id] = current_ticker
                    
                    raw_data = get_stock_data_by_years(current_ticker, years_to_fetch)
                    
                    if raw_data is not None:
                        processed_data = preprocess_data(raw_data)
                        
                        if processed_data is not None:
                            arima_results = build_arima_models(processed_data, forecast_horizon=90)
                            
                            if arima_results and current_ticker in arima_results:
                                st.session_state.analysis_results[current_ticker] = {
                                    'results': arima_results[current_ticker],
                                    'processed_data': processed_data
                                }
                            else:
                                st.error(f"ARIMA modeling failed for {current_ticker}.")
                        else:
                            st.error(f"Preprocessing failed for {current_ticker}.")
                    else:
                        st.error(f"Failed to fetch raw data for {current_ticker}.")
        
        # Display the results if they exist in the session state
        if current_ticker in st.session_state.analysis_results:
            results_data = st.session_state.analysis_results[current_ticker]
            results = results_data['results']
            processed_data = results_data['processed_data']
            
            st.write("### Analysis Results")
            forecast = results['forecast']
            conf_int = results['conf_int']
            simulations = results.get('simulations', None)
            order = results['optimal_order']
            
            hist_series = processed_data[f"Close_{current_ticker}"].dropna().copy()
            if isinstance(hist_series.index, pd.MultiIndex) and 'Date' in hist_series.index.names:
                hist_series.index = hist_series.index.get_level_values('Date')
            
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=hist_series.index, y=hist_series, mode='lines', name=f"{current_ticker} Historical", line=dict(color='blue')))
            if simulations is not None:
                for col in simulations.columns[:30]:
                    fig.add_trace(go.Scatter(x=simulations.index, y=simulations[col], mode='lines', line=dict(color='rgba(128,128,128,0.2)', width=1), name="Simulated Path", showlegend=False))
            fig.add_trace(go.Scatter(x=forecast.index, y=forecast, mode='lines', name=f"{current_ticker} Forecast", line=dict(color='orange', dash='dash')))
            fig.add_trace(go.Scatter(x=conf_int.index.tolist() + conf_int.index[::-1].tolist(), y=conf_int.iloc[:, 0].tolist() + conf_int.iloc[:, 1][::-1].tolist(), fill='toself', fillcolor='rgba(255,165,0,0.2)', line=dict(color='rgba(255,255,255,0)'), hoverinfo="skip", showlegend=True, name="Confidence Interval"))
            fig.update_layout(title=f"{current_ticker} ARIMA Forecast + Monte Carlo (Next 90 Business Days)", xaxis_title="Date", yaxis_title="Price", template="plotly_white", hovermode="x unified")
            st.plotly_chart(fig, use_container_width=True)
            st.write(f"**ARIMA Order:** {order}")
        
    # the button to add a new analysis block is placed outside the loop, at the very end
    if st.button("Add New Stock for Analysis"):
        st.session_state.analysis_tickers.append('')
        st.rerun()
