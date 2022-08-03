import requests
import pandas as pd
import time

ny = [40.78, -73.97]
chicago = [41.79, -87.74]

ny_api = f'https://api.weather.gov/points/{ny[0]},{ny[1]}'
chicago_api = f'https://api.weather.gov/points/{chicago[0]},{chicago[1]}'

ny_initial_call = requests.get(ny_api).json()
ny_hourly_api = requests.get(ny_initial_call['properties']['forecastHourly']).json()

time.sleep(2)

chicago_initial_call = requests.get(chicago_api).json()
chicago_hourly_api = requests.get(chicago_initial_call['properties']['forecastHourly']).json()

ny_hourly_items = ny_hourly_api['properties']['periods']
chicago_hourly_items = chicago_hourly_api['properties']['periods']

ny_df = pd.DataFrame(ny_hourly_items)
ny_df["location"] = "NY"

chicago_df = pd.DataFrame(chicago_hourly_items)
chicago_df["location"] = "Chicago"

combined_df = pd.concat([ny_df, chicago_df])

combined_df.to_csv("C:/Users/johnp/Downloads/weather.csv", index=False, header=True)
