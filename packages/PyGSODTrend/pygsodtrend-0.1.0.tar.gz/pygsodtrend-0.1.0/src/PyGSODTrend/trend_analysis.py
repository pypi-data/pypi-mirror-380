import pymannkendall as mk
import pandas as pd


def determine_trend(df, attribute, alpha):
    """
    Analyzes trends in GSOD data using the Mann-Kendall test with Hamed and Rao correction.

    Functions:
        determine_trend(df, attribute, alpha): Calculates slope and significance of trends by station.

    Args:
        df (pd.DataFrame): Cleaned GSOD data with DATE, STATION, and attribute columns.
    attribute (str): Attribute to analyze ("MAX", "MIN", or "PRCP").
    alpha (float): Significance level for trend detection.

    Returns:
    pd.DataFrame: DataFrame containing trend statistics for each station.
    """

    df['DATE'] = pd.to_datetime(df['DATE'])
    df = df.sort_values('DATE')
    grouped = df.groupby('STATION')

  # Define the schema for the new DataFrame with explicit dtypes
    new_df = pd.DataFrame({
        'STATION': pd.Series(dtype='float64'),
        'ATTRIBUTE': pd.Series(dtype='object'),
        'P': pd.Series(dtype='float64'),
        'SLOPE': pd.Series(dtype='float64'),
        'INTERCEPT': pd.Series(dtype='float64'),
        'LATITUDE': pd.Series(dtype='float64'),
        'LONGITUDE': pd.Series(dtype='float64')
    })

    for station_name, group_data in grouped:
        series = group_data[attribute]

        # filter PRCP data for when it's raining to prevent /0 errors
        if attribute == "PRCP":
            series = series[series > 0]

        if len(series) < 2 or series.var() == 0:
            continue

        # get trend
        result = mk.hamed_rao_modification_test(series, alpha=alpha)

        # get latitude and longitude for the current station
        latitude = group_data['LATITUDE'].iloc[0]
        longitude = group_data['LONGITUDE'].iloc[0]

        # append the results to the new DataFrame
        new_df = pd.concat([new_df, pd.DataFrame([{
            'STATION': station_name,
            'ATTRIBUTE': attribute,
            'P': result[2],
            'SLOPE': result[7],
            'INTERCEPT': result[8],
            'LATITUDE': latitude,
            'LONGITUDE': longitude
        }])], ignore_index=True)

    return new_df
