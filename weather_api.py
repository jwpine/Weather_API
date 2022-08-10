import requests
import time
import openpyxl

# Get Current Time and Date
date = time.strftime("%m/%d/%Y")
clock = time.strftime("%H:%M:%S")

# Storage for Staion List
chicago_station = 'KMDW'
ny_station = 'KNYC'

# Create the Two URLs for the API Call
chicago_url = f'https://api.weather.gov/stations/{chicago_station}/observations'
ny_url = f'https://api.weather.gov/stations/{ny_station}/observations'

# Execute the API Call
chicago_results = requests.get(chicago_url).json()
ny_results = requests.get(ny_url).json()

# Get the Current Temperature
chicago_temp_c = chicago_results['features'][0]['properties']['temperature']['value']
ny_temp_c = ny_results['features'][0]['properties']['temperature']['value']

# Convert C to F
chicago_temp_f = (chicago_temp_c * (9/5)) + 32
ny_temp_f = (ny_temp_c * (9/5)) + 32

# Open an Excel Workbook to add the Data
book = openpyxl.load_workbook('Weather_Data.xlsx')
sheet = book.active

# Insert a Row at the top so it is sorted properly
sheet.insert_rows(2)

# Insert the data from the Call
date_excel = sheet.cell(row=2, column=1)
date_excel.value = date
time_excel = sheet.cell(row=2, column=2)
time_excel.value = clock
chicago_f_excel = sheet.cell(row=2, column=3)
chicago_f_excel.value = chicago_temp_f
chicago_c_excel = sheet.cell(row=2, column=4)
chicago_c_excel.value = chicago_temp_c
ny_f_excel = sheet.cell(row=2, column=5)
ny_f_excel.value = ny_temp_f
ny_c_excel = sheet.cell(row=2, column=6)
ny_c_excel.value = ny_temp_c

# Save the Workbook
book.save('Weather_Data.xlsx')