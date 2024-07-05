# Data Integrity and Optimization Project

## Project Overview

This project aims to ensure the integrity and optimization of the Austin Police Department crime reports dataset. The dataset includes records of incidents that the Austin Police Department responded to and wrote reports for, capturing various aspects of each incident.

## Data Source

The dataset can be accessed via the Austin Police Department's API endpoint:
- [Austin Police Department Crime Reports](https://data.austintexas.gov/resource/fdj4-gpfu.csv)

## Data Description

The dataset includes the following fields:

- **Incident Number**: Incident report number
- **Highest Offense Description**: Description of the highest-level offense
- **Highest Offense Code**: Code for the highest-level offense
- **Family Violence**: Indicates whether the incident involves family violence (Y = yes, N = no)
- **Occurred Date Time**: Date and time the incident occurred
- **Occurred Date**: Date the incident occurred
- **Occurred Time**: Time the incident occurred
- **Report Date Time**: Date and time the incident was reported
- **Report Date**: Date the incident was reported
- **Report Time**: Time the incident was reported
- **Location Type**: General description of the premise where the incident occurred
- **Address**: Incident location
- **Zip Code**: Zip code where the incident occurred
- **Council District**: Austin city council district where the incident occurred
- **APD Sector**: APD sector where the incident occurred
- **APD District**: APD district where the incident occurred
- **PRA**: APD police reporting area where the incident occurred
- **Census Tract**: Census tract where the incident occurred
- **Clearance Status**: How/whether the crime was solved (C = Cleared by Arrest, O = Cleared by Exception, N = Not cleared)
- **Clearance Date**: Date the crime was solved
- **UCR Category**: Code for the most serious crimes identified by the FBI as part of its Uniform Crime Reporting program
- **Category Description**: Description of the most serious crimes identified by the FBI as part of its Uniform Crime Reporting program
- **X-coordinate**: X-coordinate where the incident occurred
- **Y-coordinate**: Y-coordinate where the incident occurred
- **Latitude**: Latitude where the incident occurred
- **Longitude**: Longitude where the incident occurred
- **Location**: 3rd party generated spatial column

## Project Goals

1. **Data Cleaning**: Remove duplicates, handle null values, and ensure data consistency.
2. **Data Integrity**: Verify and validate the data to ensure accuracy and reliability.
3. **Data Optimization**: Optimize the database for efficient querying and storage.

## Python Script for Data Cleaning and Optimization

```python
import requests
import pandas as pd
import sqlite3

# Step 1: Download data from the API
url = "https://data.austintexas.gov/resource/fdj4-gpfu.csv"
response = requests.get(url)
with open("austin_crime_reports.csv", "wb") as file:
    file.write(response.content)

# Step 2: Load data into a DataFrame
df = pd.read_csv("austin_crime_reports.csv")

# Step 3: Data Cleaning
# Remove duplicates
df.drop_duplicates(subset="incident_number", inplace=True)

# Handle null values
df.fillna({
    'x_coordinate': 0,
    'y_coordinate': 0,
    'latitude': 0,
    'longitude': 0,
    'highest_offense_description': None,
    'location_type': None,
}, inplace=True)

# Ensure family_violence is either 'Y' or 'N'
df['family_violence'] = df['family_violence'].apply(lambda x: 'N' if pd.isna(x) or x not in ['Y', 'N'] else x)

# Step 4: Insert data into SQLite database
conn = sqlite3.connect('austin_crime_reports.db')
df.to_sql('crime_reports', conn, if_exists='replace', index=False)

# Step 5: Create Indexes and Optimize the Database
cursor = conn.cursor()

# Indexing commonly queried columns
cursor.execute('CREATE INDEX idx_occurred_date_time ON crime_reports(occurred_date_time);')
cursor.execute('CREATE INDEX idx_report_date_time ON crime_reports(report_date_time);')
cursor.execute('CREATE INDEX idx_zip_code ON crime_reports(zip_code);')
cursor.execute('CREATE INDEX idx_council_district ON crime_reports(council_district);')
cursor.execute('CREATE INDEX idx_apd_sector ON crime_reports(apd_sector);')

# Compressing large text columns to save space
cursor.execute('ALTER TABLE crime_reports ADD COLUMN temp_description TEXT;')
cursor.execute('UPDATE crime_reports SET temp_description = highest_offense_description;')
cursor.execute('ALTER TABLE crime_reports DROP COLUMN highest_offense_description;')
cursor.execute('ALTER TABLE crime_reports RENAME COLUMN temp_description TO highest_offense_description;')

cursor.execute('ALTER TABLE crime_reports ADD COLUMN temp_location_type TEXT;')
cursor.execute('UPDATE crime_reports SET temp_location_type = location_type;')
cursor.execute('ALTER TABLE crime_reports DROP COLUMN location_type;')
cursor.execute('ALTER TABLE crime_reports RENAME COLUMN temp_location_type TO location_type;')

cursor.execute('ALTER TABLE crime_reports ADD COLUMN temp_address TEXT;')
cursor.execute('UPDATE crime_reports SET temp_address = address;')
cursor.execute('ALTER TABLE crime_reports DROP COLUMN address;')
cursor.execute('ALTER TABLE crime_reports RENAME COLUMN temp_address TO address;')

cursor.execute('ALTER TABLE crime_reports ADD COLUMN temp_category_description TEXT;')
cursor.execute('UPDATE crime_reports SET temp_category_description = category_description;')
cursor.execute('ALTER TABLE crime_reports DROP COLUMN category_description;')
cursor.execute('ALTER TABLE crime_reports RENAME COLUMN temp_category_description TO category_description;')

cursor.execute('ALTER TABLE crime_reports ADD COLUMN temp_location TEXT;')
cursor.execute('UPDATE crime_reports SET temp_location = location;')
cursor.execute('ALTER TABLE crime_reports DROP COLUMN location;')
cursor.execute('ALTER TABLE crime_reports RENAME COLUMN temp_location TO location;')

conn.commit()
conn.close()# Data Integrity and Optimization Project

## Project Overview

This project aims to ensure the integrity and optimization of the Austin Police Department crime reports dataset. The dataset includes records of incidents that the Austin Police Department responded to and wrote reports for, capturing various aspects of each incident.

## Data Source

The dataset can be accessed via the Austin Police Department's API endpoint:
- [Austin Police Department Crime Reports](https://data.austintexas.gov/resource/fdj4-gpfu.csv)

## Data Description

The dataset includes the following fields:

- **Incident Number**: Incident report number
- **Highest Offense Description**: Description of the highest-level offense
- **Highest Offense Code**: Code for the highest-level offense
- **Family Violence**: Indicates whether the incident involves family violence (Y = yes, N = no)
- **Occurred Date Time**: Date and time the incident occurred
- **Occurred Date**: Date the incident occurred
- **Occurred Time**: Time the incident occurred
- **Report Date Time**: Date and time the incident was reported
- **Report Date**: Date the incident was reported
- **Report Time**: Time the incident was reported
- **Location Type**: General description of the premise where the incident occurred
- **Address**: Incident location
- **Zip Code**: Zip code where the incident occurred
- **Council District**: Austin city council district where the incident occurred
- **APD Sector**: APD sector where the incident occurred
- **APD District**: APD district where the incident occurred
- **PRA**: APD police reporting area where the incident occurred
- **Census Tract**: Census tract where the incident occurred
- **Clearance Status**: How/whether the crime was solved (C = Cleared by Arrest, O = Cleared by Exception, N = Not cleared)
- **Clearance Date**: Date the crime was solved
- **UCR Category**: Code for the most serious crimes identified by the FBI as part of its Uniform Crime Reporting program
- **Category Description**: Description of the most serious crimes identified by the FBI as part of its Uniform Crime Reporting program
- **X-coordinate**: X-coordinate where the incident occurred
- **Y-coordinate**: Y-coordinate where the incident occurred
- **Latitude**: Latitude where the incident occurred
- **Longitude**: Longitude where the incident occurred
- **Location**: 3rd party generated spatial column

## Project Goals

1. **Data Cleaning**: Remove duplicates, handle null values, and ensure data consistency.
2. **Data Integrity**: Verify and validate the data to ensure accuracy and reliability.
3. **Data Optimization**: Optimize the database for efficient querying and storage.

## Python Script for Data Cleaning and Optimization

```python
import requests
import pandas as pd
import sqlite3

# Step 1: Download data from the API
url = "https://data.austintexas.gov/resource/fdj4-gpfu.csv"
response = requests.get(url)
with open("austin_crime_reports.csv", "wb") as file:
    file.write(response.content)

# Step 2: Load data into a DataFrame
df = pd.read_csv("austin_crime_reports.csv")

# Step 3: Data Cleaning
# Remove duplicates
df.drop_duplicates(subset="incident_number", inplace=True)

# Handle null values
df.fillna({
    'x_coordinate': 0,
    'y_coordinate': 0,
    'latitude': 0,
    'longitude': 0,
    'highest_offense_description': None,
    'location_type': None,
}, inplace=True)

# Ensure family_violence is either 'Y' or 'N'
df['family_violence'] = df['family_violence'].apply(lambda x: 'N' if pd.isna(x) or x not in ['Y', 'N'] else x)

# Step 4: Insert data into SQLite database
conn = sqlite3.connect('austin_crime_reports.db')
df.to_sql('crime_reports', conn, if_exists='replace', index=False)

# Step 5: Create Indexes and Optimize the Database
cursor = conn.cursor()

# Indexing commonly queried columns
cursor.execute('CREATE INDEX idx_occurred_date_time ON crime_reports(occurred_date_time);')
cursor.execute('CREATE INDEX idx_report_date_time ON crime_reports(report_date_time);')
cursor.execute('CREATE INDEX idx_zip_code ON crime_reports(zip_code);')
cursor.execute('CREATE INDEX idx_council_district ON crime_reports(council_district);')
cursor.execute('CREATE INDEX idx_apd_sector ON crime_reports(apd_sector);')

# Compressing large text columns to save space
cursor.execute('ALTER TABLE crime_reports ADD COLUMN temp_description TEXT;')
cursor.execute('UPDATE crime_reports SET temp_description = highest_offense_description;')
cursor.execute('ALTER TABLE crime_reports DROP COLUMN highest_offense_description;')
cursor.execute('ALTER TABLE crime_reports RENAME COLUMN temp_description TO highest_offense_description;')

cursor.execute('ALTER TABLE crime_reports ADD COLUMN temp_location_type TEXT;')
cursor.execute('UPDATE crime_reports SET temp_location_type = location_type;')
cursor.execute('ALTER TABLE crime_reports DROP COLUMN location_type;')
cursor.execute('ALTER TABLE crime_reports RENAME COLUMN temp_location_type TO location_type;')

cursor.execute('ALTER TABLE crime_reports ADD COLUMN temp_address TEXT;')
cursor.execute('UPDATE crime_reports SET temp_address = address;')
cursor.execute('ALTER TABLE crime_reports DROP COLUMN address;')
cursor.execute('ALTER TABLE crime_reports RENAME COLUMN temp_address TO address;')

cursor.execute('ALTER TABLE crime_reports ADD COLUMN temp_category_description TEXT;')
cursor.execute('UPDATE crime_reports SET temp_category_description = category_description;')
cursor.execute('ALTER TABLE crime_reports DROP COLUMN category_description;')
cursor.execute('ALTER TABLE crime_reports RENAME COLUMN temp_category_description TO category_description;')

cursor.execute('ALTER TABLE crime_reports ADD COLUMN temp_location TEXT;')
cursor.execute('UPDATE crime_reports SET temp_location = location;')
cursor.execute('ALTER TABLE crime_reports DROP COLUMN location;')
cursor.execute('ALTER TABLE crime_reports RENAME COLUMN temp_location TO location;')

conn.commit()
conn.close()
