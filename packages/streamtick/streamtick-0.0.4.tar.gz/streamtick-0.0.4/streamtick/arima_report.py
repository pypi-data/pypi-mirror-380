import streamlit as st
import pandas as pd
import numpy as np
from statsmodels.tsa.statespace.sarimax import SARIMAXResultsWrapper

def ArimaReport():
    
    # Generates a Streamlit UI component for an ARIMA model evaluation report.
    
    st.subheader("ARIMA Model Evaluation Report Generator")
    st.markdown("Enter your model's performance metrics below to get a detailed report.")

    # Create input fields for key metrics
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        r_squared = st.number_input(
            "R-squared (R²)", 
            min_value=0.0, 
            max_value=1.0, 
            step=0.01, 
            format="%.2f", 
            key="report_r2",
            help="A score from 0 to 1 indicating how much variance the model explains. Higher is better."
        )
    with col2:
        mae = st.number_input(
            "Mean Absolute Error (MAE)", 
            min_value=0.0, 
            step=0.01,
            key="report_mae",
            help="The average absolute difference between the forecast and the actual values. Lower is better."
        )
    with col3:
        rmse = st.number_input(
            "Root Mean Squared Error (RMSE)",
            min_value=0.0,
            step=0.01,
            key="report_rmse",
            help="The square root of MSE. In the same units as the original data. Lower is better."
        )
    with col4:
        mape = st.number_input(
            "Mean Absolute Percentage Error (MAPE)",
            min_value=0.0,
            step=0.01,
            key="report_mape",
            help="The average absolute percentage error. Scale-independent, so values are comparable across datasets."
        )
    
    col5, col6 = st.columns(2)
    with col5:
        aic = st.number_input(
            "Akaike Information Criterion (AIC)",
            step=0.01,
            format="%.2f",
            key="report_aic",
            help="Measures model fit and complexity. Lower is better."
        )
    with col6:
        bic = st.number_input(
            "Bayesian Information Criterion (BIC)",
            step=0.01,
            format="%.2f",
            key="report_bic",
            help="Similar to AIC but with a stronger penalty for complexity. Lower is better."
        )


    # generate report button
    if st.button("Generate Report", key="generate_report_btn"):
        # create the report dictionary
        report = {
            "title": "ARIMA Model Evaluation Report",
            "metrics": {
                "R-squared (R²)": r_squared,
                "Mean Absolute Error (MAE)": mae,
                "Root Mean Squared Error (RMSE)": rmse,
                "Mean Absolute Percentage Error (MAPE)": mape,
                "Akaike Information Criterion (AIC)": aic,
                "Bayesian Information Criterion (BIC)": bic
            },
            "assessment": {
                "conclusion": "",
                "reasons": []
            }
        }

        # qualitative assessment logic
        reasons = []

        # Heuristic 1: R-squared
        if r_squared > 0.8:
            reasons.append("R-squared is strong (> 0.8), indicating the model explains a large portion of the variance.")
        elif r_squared > 0.6:
            reasons.append("R-squared is moderate (> 0.6), a decent but improvable result.")
        else:
            reasons.append("R-squared is low, suggesting the model does not capture the data's trends well.")
        
        # Heuristic 2: MAE and RMSE
        if rmse < 10 and mae < 10:
            reasons.append("RMSE and MAE values are low, indicating accurate predictions on average. Good signs for model performance.")
        else:
            reasons.append("RMSE and MAE values are high, suggesting significant prediction errors.")

        # Heuristic 3: AIC and BIC
        if aic > 0 and bic > 0 and aic < 200 and bic < 200: # These are general heuristics and can be contextual
            reasons.append("AIC and BIC are low, which suggests a good balance between model fit and complexity.")
        else:
            reasons.append("AIC and/or BIC are high, which could indicate overfitting or that a different model is needed.")


        # final conclusion
        if r_squared > 0.6 and rmse < 20 and aic < 200:
            report["assessment"]["conclusion"] = "This model shows great promise. The metrics suggest it is a reliable forecasting tool."
        else:
            report["assessment"]["conclusion"] = "The model's performance is currently below expectations. Consider re-evaluating the data or using a different model."
        
        report["assessment"]["reasons"] = reasons
        
        st.session_state['arima_report'] = report
        st.success("Report generated successfully!")

        st.write("---")
        st.subheader("Generated Report Dictionary")
        st.json(st.session_state['arima_report'])
