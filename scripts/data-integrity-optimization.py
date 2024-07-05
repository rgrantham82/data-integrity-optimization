import pandas as pd
import requests
from sqlalchemy import create_engine

# Define the API endpoint
api_url = 'https://data.austintexas.gov/resource/fdj4-gpfu.csv'

# Fetch the data
response = requests.get(api_url)
response.raise_for_status()  # Ensure we notice bad responses

# Load the data into a pandas DataFrame
data = pd.read_csv(api_url)

# Display basic information about the data
print("Data fetched from API:")
print(data.info())

# Data Cleaning
print("Starting data cleaning...")

# Remove any duplicate records based on the incident number
data.drop_duplicates(subset='incident_number', inplace=True)

# Check for null values in critical columns and fill or drop them accordingly
critical_columns = ['incident_number', 'highest_offense_description', 'occurred_date_time']
for column in critical_columns:
    if data[column].isnull().sum() > 0:
        print(f"Found missing values in {column}. Dropping rows with missing values.")
        data.dropna(subset=[column], inplace=True)

# Convert date and time columns to appropriate formats
data['occurred_date_time'] = pd.to_datetime(data['occurred_date_time'])
data['report_date_time'] = pd.to_datetime(data['report_date_time'])

# Ensure family_violence column only contains 'Y' or 'N'
data = data[data['family_violence'].isin(['Y', 'N'])]

# Filter out invalid latitude and longitude values
data = data[(data['latitude'] >= -90) & (data['latitude'] <= 90)]
data = data[(data['longitude'] >= -180) & (data['longitude'] <= 180)]

# Remove records where the report date is before the occurred date
data = data[data['report_date_time'] >= data['occurred_date_time']]

print("Data cleaning completed.")

# Data Optimization
print("Starting data optimization...")

# Create an index on the incident number for faster lookups
data.set_index('incident_number', inplace=True)

print("Data optimization completed.")

# Save the cleaned and optimized data to a new CSV file
cleaned_data_path = 'cleaned_crime_reports.csv'
data.to_csv(cleaned_data_path)

print(f"Cleaned data saved to {cleaned_data_path}.")

# Define database connection parameters
db_engine = create_engine('postgresql://your_user:your_password@your_host:your_port/your_db')

# Load data into the PostgreSQL database
print("Loading data into the PostgreSQL database...")
data.to_sql('crime_reports', db_engine, if_exists='replace', index=True)

print("Data loaded into the PostgreSQL database successfully.")
