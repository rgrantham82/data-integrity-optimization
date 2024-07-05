# Data Integrity and Optimization Using Austin Crime Reports

## Overview

Data integrity is a critical aspect of any data-related project, ensuring that the data is accurate, consistent, and reliable over its lifecycle. In this project, we focus on investigating and enhancing the data integrity and optimization techniques applied to the Austin Crime Reports dataset. This dataset, provided by the City of Austin, includes detailed records of crime incidents reported within the city.

### Objectives

1. **Assess Data Quality**: Examine the dataset for common data quality issues such as missing values, duplicates, and inconsistencies.
2. **Data Cleaning**: Apply appropriate data cleaning techniques to rectify identified issues and ensure the dataset is accurate and complete.
3. **Data Optimization**: Implement strategies to optimize the dataset for better performance in data analysis and machine learning tasks.
4. **Visualization and Reporting**: Create visualizations and reports to present the findings and improvements made during the project.

### Data Sources

- **Austin Crime Reports Dataset**: This dataset is accessed via its API endpoint [here](https://data.austintexas.gov/resource/fdj4-gpfu.csv). It includes various attributes such as the type of crime, location, date and time of occurrence, and more.

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

### Methodology

1. **Data Collection**: Retrieve the dataset using the provided API endpoint.
2. **Exploratory Data Analysis (EDA)**: Perform EDA to understand the structure, content, and quality of the dataset.
3. **Data Cleaning Steps**:
   - **Handling Missing Values**: Identify and appropriately handle missing values using techniques such as imputation or removal.
   - **Removing Duplicates**: Detect and remove duplicate records to ensure data uniqueness.
   - **Data Type Correction**: Verify and correct data types for each attribute to ensure consistency and accuracy.
4. **Data Optimization Techniques**:
   - **Indexing**: Create indexes on key attributes to speed up data retrieval.
   - **Normalization**: Normalize data to eliminate redundancy and improve data integrity.
   - **Partitioning**: Partition the dataset to enhance query performance and manageability.
5. **Visualization**: Develop visualizations to demonstrate the improvements in data quality and performance.

### Significance

Ensuring data integrity and optimization not only improves the quality of the dataset but also enhances the reliability of any analytical or machine learning models built on it. This project showcases practical techniques and best practices that can be applied to various datasets to achieve similar improvements in data quality and performance.

### Expected Outcomes

- A clean, reliable, and optimized version of the Austin Crime Reports dataset.
- Improved performance in data retrieval and analysis tasks.
- Comprehensive visualizations and reports demonstrating the data integrity and optimization processes.
- A repository of reusable scripts and methodologies for future data integrity and optimization projects.

### Project Structure

- **data_integrity_optimization.py**: Script for data cleaning and optimization.
- **SQL Scripts**: SQL queries for data cleaning and optimization.
- **Visualizations**: Graphical representations of the dataset before and after optimization.
- **Reports**: Detailed documentation of the data integrity and optimization processes.

By following the steps and methodologies outlined in this project, we aim to achieve a high level of data integrity and optimization, thereby enhancing the overall value and usability of the Austin Crime Reports dataset.