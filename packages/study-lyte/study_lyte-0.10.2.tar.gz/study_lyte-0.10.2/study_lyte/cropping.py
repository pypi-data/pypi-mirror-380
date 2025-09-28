from study_lyte.adjustments import remove_ambient
from .detect import get_acceleration_start, get_acceleration_stop, get_nir_surface
from .adjustments import  get_neutral_bias_at_border
from .decorators import time_series
import pandas as pd


@time_series
def crop_to_motion(df: pd.DataFrame, detect_col='Y-Axis', start_kwargs=None, stop_kwargs=None) -> pd.DataFrame:
    """
    Crop the dataset to only the motion as seen by the accelerometer

    Args:
        df: pd.DataFrame containing the column specified for acceleration
        detect_col: Column name to use to determine the start/stop of motion
        start_kwargs: Dict of keyword arguments to pass on to detect.get_acceleration_start
        stop_kwargs: Dict of  keyword arguments to pass on to detect.get_acceleration_stop

    Returns:
        cropped: pd.Dataframe cropped to the time period where motion start/stopped
    """
    start_kwargs = start_kwargs or {}
    stop_kwargs = stop_kwargs or {}

    neutral = get_neutral_bias_at_border(df[detect_col])
    start = get_acceleration_start(neutral, **start_kwargs)
    neutral = get_neutral_bias_at_border(df[detect_col], direction='backward')
    stop = get_acceleration_stop(neutral, **stop_kwargs)
    cropped = df.iloc[start:stop]
    return cropped


@time_series
def crop_to_snow(df: pd.DataFrame, active_col='Sensor3', ambient_col='Sensor2', **kwargs) -> pd.DataFrame:
    """
    Crop the dataset to only the data in the snow as seen by the
    NIR sensors

    Args:
        df: pd.DataFrame containing the column specified for acceleration
        active_col: Column name containing active nir data
        ambient_col: Column name containing ambient nir data
        kwargs: Other keyword arguments to pass on to detect.get_nir_surface

    Returns:
        cropped: pd.Dataframe cropped to the time period where a surface was detected to the end
    """
    df['nir'] = remove_ambient(df[active_col],  df[ambient_col])
    surface = get_nir_surface(df['nir'], **kwargs)
    cropped = df.iloc[surface:]
    return cropped

