-- Check for duplicate incident numbers
SELECT incident_number,
       Count(*)
FROM   crime_reports
GROUP  BY incident_number
HAVING Count(*) > 1;

-- Check for null values in critical columns
SELECT *
FROM   crime_reports
WHERE  incident_number IS NULL
        OR highest_offense_description IS NULL
        OR occurred_date_time IS NULL;

-- Ensure latitude and longitude values are within valid ranges
SELECT *
FROM   crime_reports
WHERE  latitude < -90
        OR latitude > 90
        OR longitude < -180
        OR longitude > 180;

-- Verify data types and format consistency
SELECT *
FROM   crime_reports
WHERE  family_violence NOT IN ( 'Y', 'N' );

-- Check if there are any records with a report date before the occurred date
SELECT *
FROM   crime_reports
WHERE  report_date < occurred_date; 
