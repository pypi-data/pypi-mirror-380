from .ui import analyze_stock_ui as tick_arima

from .data_acquisition import get_stock_data_by_years
from .data_preprocessing import preprocess_data
from .arima import build_arima_models


from .arima_report import ArimaReport


#################################


from .ui import analyze_stock_ui as tick_arima

from .data_acquisition import get_stock_data_by_years
from .data_preprocessing import preprocess_data
from .arima import build_arima_models

from .arima_report import ArimaReport

from .make_stationary import make_stationary


#################################


from .ui import analyze_stock_ui as tick_arima

from .data_acquisition import get_stock_data_by_years
from .data_preprocessing import preprocess_data
from .arima import build_arima_models

from .make_stationary import make_stationary
from .decompose_series import decompose_series # <-- NEW IMPORT ADDED

from .arima_report import ArimaReport

__all__ = [
    'tick_arima',
    'get_stock_data_by_years',
    'preprocess_data',
    'build_arima_models',
    'ArimaReport',
    'make_stationary',
    'decompose_series' 
]


##################################

from .ui import analyze_stock_ui as tick_arima

from .data_acquisition import get_stock_data_by_years
from .data_preprocessing import preprocess_data
from .arima import build_arima_models

from .make_stationary import make_stationary
from .decompose_series import decompose_series
from .model_identification import check_autocorrelation



from .arima_report import ArimaReport

__all__ = [
    'tick_arima',
    'get_stock_data_by_years',
    'preprocess_data',
    'build_arima_models',
    'ArimaReport',
    'make_stationary',
    'decompose_series',
    'check_autocorrelation',
    'custom_arima_forecast',
    'check_residuals',
]
