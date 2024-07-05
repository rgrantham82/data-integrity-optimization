# Data Integrity and Optimization Project

## Project Overview

This project aims to ensure the integrity and optimization of the Austin Police Department's crime reports data. By utilizing data cleaning and optimization techniques, the project addresses inconsistencies and prepares the data for effective analysis. The data is accessed via the API endpoint: https://data.austintexas.gov/resource/fdj4-gpfu.csv.

## Data Description

### AUSTIN POLICE DEPARTMENT DATA DISCLAIMER

Please read and understand the following information.

This dataset contains a record of incidents that the Austin Police Department responded to and wrote a report. Please note one incident may have several offenses associated with it, but this dataset only depicts the highest level offense of that incident. Data is from 2003 to present. This dataset is updated weekly. Understanding the following conditions will allow you to get the most out of the data provided. Due to the methodological differences in data collection, different data sources may produce different results. This database is updated weekly, and a similar or same search done on different dates can produce different results. Comparisons should not be made between numbers generated with this database to any other official police reports. Data provided represents only calls for police service where a report was written. Totals in the database may vary considerably from official totals following investigation and final categorization. Therefore, the data should not be used for comparisons with Uniform Crime Report statistics. The Austin Police Department does not assume any liability for any decision made or action taken or not taken by the recipient in reliance upon any information or data provided.

### Fields Description

- **Incident Number**: Incident report number
- **Highest Offense Description**: Description of the highest level offense
- **Highest Offense Code**: Code of the highest level offense
- **Family Violence**: Indicates if the incident involves family violence (Y = yes, N = no)
- **Occurred Date Time**: Combined date and time when the incident occurred
- **Occurred Date**: Date when the incident occurred
- **Occurred Time**: Time when the incident occurred
- **Report Date Time**: Combined date and time when the incident was reported
- **Report Date**: Date when the incident was reported
- **Report Time**: Time when the incident was reported
- **Location Type**: General description of the premise where the incident occurred
- **Address**: Incident location
- **Zip Code**: Zip code where incident occurred
- **Council District**: Austin city council district where the incident occurred
- **APD Sector**: APD sector where incident occurred
- **APD District**: APD district where incident occurred
- **PRA**: APD police reporting area where incident occurred
- **Census Tract**: Census tract where incident occurred
- **Clearance Status**: How/whether crime was solved (Cleared by Arrest, Cleared by Exception, Not cleared)
- **Clearance Date**: Date crime was solved
- **UCR Category**: Code for the most serious crimes identified by the FBI as part of its Uniform Crime Reporting program
- **Category Description**: Description for the most serious crimes identified by the FBI as part of its Uniform Crime Reporting program
- **X-coordinate**: X-coordinate where the incident occurred
- **Y-coordinate**: Y-coordinate where the incident occurred
- **Latitude**: Latitude where the incident occurred
- **Longitude**: Longitude where the incident occurred
- **Location**: 3rd party generated spatial column

## Python Scripts

### Data Cleaning

The `data_cleaning.py` script handles the data cleaning process by:
- Removing duplicates
- Handling missing values
- Correcting data types
- Normalizing text data

### Data Optimization

The `data_optimization.py` script focuses on optimizing the data by:
- Creating indexes
- Normalizing the database schema
- Aggregating data for efficient queries

## SQL Scripts

### create_tables.sql

This script creates the necessary tables to store the cleaned and optimized data.

### insert_data.sql

This script inserts the cleaned data into the database tables.

### data_quality_checks.sql

This script performs various data quality checks to ensure the integrity of the data.
