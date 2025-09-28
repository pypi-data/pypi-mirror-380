import pandas as pd
import numpy as np
from statsmodels.tsa.arima.model import ARIMA
import pmdarima as pm
from .data_acquisition import get_multiple_stock_data
from .data_preprocessing import preprocess_data
import warnings

# Suppress ARIMA warnings for cleaner output
warnings.filterwarnings("ignore")

def build_arima_models(processed_data, forecast_horizon=90, n_simulations=100):
    """
    Builds optimized ARIMA models for all tickers, performs forecasts, and includes
    Monte Carlo simulations and key evaluation metrics.
    """
    results = {}

    # extract all tickers from column names
    ticker_cols = [col for col in processed_data.columns if col.startswith("Close_") and not col.startswith("Close_Diff")]
    tickers = [col.split("_")[1] for col in ticker_cols]

    for ticker in tickers:
        try:
            col_name = f"Close_{ticker}"
            series = processed_data[col_name].copy()

            # ensure datetime index if MultiIndex is used
            if 'Date' in processed_data.index.names:
                series.index = processed_data.index.get_level_values('Date')

            # using auto_arima to find optimal (p,d,q) with robust error handling
            auto_model = pm.auto_arima(
                series,
                seasonal=False,
                stepwise=True,
                suppress_warnings=True,
                error_action='ignore',
                trace=False, 
                d=None 
            )
            p, d, q = auto_model.order

            # fit final ARIMA model with suggested order
            model = ARIMA(series, order=(p, d, q))
            model_fit = model.fit()

            # deterministic forecast
            forecast_obj = model_fit.get_forecast(steps=forecast_horizon)
            forecast = forecast_obj.predicted_mean
            conf_int = forecast_obj.conf_int()

            # assign datetime index to forecast
            last_date = series.index[-1]
            forecast_index = pd.date_range(start=last_date + pd.Timedelta(days=1), periods=forecast_horizon, freq='B')
            forecast.index = forecast_index
            conf_int.index = forecast_index

            # monte Carlo Simulations
            sim_paths = []
            residuals = model_fit.resid
            sigma = np.std(residuals)

            for _ in range(n_simulations):
                # we will simulate the differences and then cumsum to get prices
                sim_diffs = np.random.normal(0, sigma, forecast_horizon)
                # take the last known price and add cumulative differences
                sim_path = series.iloc[-1] + np.cumsum(sim_diffs)
                sim_paths.append(sim_path)

            sim_df = pd.DataFrame(sim_paths).T
            sim_df.index = forecast_index

            # save results with advanced metrics
            results[ticker] = {
                'model': model_fit,
                'forecast': forecast,
                'conf_int': conf_int,
                'simulations': sim_df,
                'optimal_order': (p, d, q),
                'aic': model_fit.aic,
                'bic': model_fit.bic,
                'log_likelihood': model_fit.llf,
            }

            print(f"[{ticker}] Optimal ARIMA order: {auto_model.order}")
            print(f"[{ticker}] AIC: {model_fit.aic:.2f}, BIC: {model_fit.bic:.2f}")

        except Exception as e:
            print(f"[{ticker}] Error during ARIMA modeling: {e}")
            continue

    return results

#Example Usage
if __name__ == "__main__":
    tickers = [
        'AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA',
        'MC.PA', 'AZN.L', 'SIE.DE', 'SHEL.L', 'SAP.DE',
        'ASML', 'NESN.SW'
    ]
    years_to_fetch = 3

    print("Step 1: Fetching raw stock data...")
    raw_data = get_multiple_stock_data(tickers, years_to_fetch)

    if raw_data is not None:
        print("Raw data obtained successfully.")
        print("Step 2: Preprocessing data...")
        processed_data = preprocess_data(raw_data)

        if processed_data is not None:
            print("Step 3: Building ARIMA models and forecasting...")
            arima_results = build_arima_models(processed_data)

            for ticker in arima_results.keys():
                forecast = arima_results[ticker]['forecast']
                conf_int = arima_results[ticker]['conf_int']

                print(f"\n--- {ticker} Forecast (next 90 business days) ---")
                print(forecast.to_string())
                print(f"\n--- {ticker} Forecast Confidence Intervals ---")
                print(conf_int.to_string())
                print(f"\n--- {ticker} Model Metrics ---")
                print(f"Optimal Order: {arima_results[ticker]['optimal_order']}")
                print(f"AIC: {arima_results[ticker]['aic']:.2f}")
                print(f"BIC: {arima_results[ticker]['bic']:.2f}")

                print(f"\n--- {ticker} Monte Carlo Simulated Paths (first 5 shown) ---")
                print(arima_results[ticker]['simulations'].iloc[:, :5].head())
        else:
            print("Preprocessing failed.")    
    else:
        print("Raw data could not be obtained.")


