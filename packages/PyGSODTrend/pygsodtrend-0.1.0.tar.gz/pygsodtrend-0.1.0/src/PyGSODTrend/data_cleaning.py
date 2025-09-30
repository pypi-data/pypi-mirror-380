import pandas as pd
import numpy as np


def clean_data(df, temp_min, temp_max, prcp_max):
    """
    Cleans and preprocesses GSOD weather data by identifying and removing unreliable records.

    Functions:
    clean_data(df, temp_min, temp_max, prcp_max): Cleans the data and imputes invalid values.

    Args:
    df (pd.DataFrame): Raw GSOD data with columns like DATE, STATION, MAX, MIN, PRCP.
    temp_min (float): Minimum acceptable temperature (°F).
    temp_max (float): Maximum acceptable temperature (°F).
    prcp_max (float): Maximum acceptable precipitation (mm).

    Returns:
    valid (pd.DataFrame): DataFrame with cleaned and valid data records.
    invalid (pd.DataFrame): DataFrame containing remaining invalid records.
    """

    df["DATE"] = pd.to_datetime(df["DATE"], errors="coerce")
    df["status"] = "valid"

    # Filter for data points with invalid data
    df.loc[(df[["MAX", "MIN"]].eq(9999.9).any(axis=1)) |
           (df["PRCP"].eq(99.99)), "status"] = "invalid"

    # Remove Stations where >= 10% of data is invalid
    missing_pct = df[["MAX", "MIN"]].eq(9999.9).groupby(df['STATION']).mean()
    invalid_stations = missing_pct[missing_pct.ge(0.1).all(axis=1)].index
    df.loc[df["STATION"].isin(invalid_stations), "status"] = "invalid"

    # Remove Stations w/ < 70% Coverage
    summary_data = (
        df.groupby('STATION').agg(
            station_name=("NAME", "first"),
            n_records=("DATE", "count"),
            first_date=("DATE", "min"),
            last_date=("DATE", "max"),
        )
    )
    summary_data["total_days"] = (
        summary_data["last_date"] - summary_data["first_date"]).dt.days + 1
    summary_data["missing_days"] = summary_data["total_days"] - \
        summary_data["n_records"]
    summary_data["coverage_pct"] = (
        summary_data["n_records"] / summary_data["total_days"])
    unreliable_stations = summary_data[summary_data["coverage_pct"] < 0.7].index
    df.loc[df["STATION"].isin(unreliable_stations), "status"] = "invalid"

  # remove Stations w/ unrealistic records
    df.loc[(df["MAX"] > temp_max) | (df["MIN"] < temp_min)
           | (df["PRCP"] > prcp_max), "status"] = "invalid"

  # filter by valid and invalid data
    valid = df[df["status"] == "valid"].copy()
    invalid = df[df["status"] == "invalid"].copy()

  # for invalid data, replace with monthly mean temp., filter back to valid
    valid['MONTH'] = valid['DATE'].dt.month
    invalid['MONTH'] = invalid['DATE'].dt.month
    station_month_averages = valid.groupby(['STATION', 'MONTH'])[
        ['PRCP', 'MIN', 'MAX']].mean()
    count = 0

    for index, row in invalid.iterrows():
        station = row['STATION']
        month = row['MONTH']

        if (station, month) in station_month_averages.index:
            avg_values = station_month_averages.loc[(station, month)]

            df.loc[index, 'PRCP'] = avg_values['PRCP']
            df.loc[index, 'MIN'] = avg_values['MIN']
            df.loc[index, 'MAX'] = avg_values['MAX']
            df.loc[index, 'status'] = 'valid'
            count += 1

  # filter by valid and invalid data
    valid = df[df["status"] == "valid"].copy()
    invalid = df[df["status"] == "invalid"].copy()

    return valid, invalid
