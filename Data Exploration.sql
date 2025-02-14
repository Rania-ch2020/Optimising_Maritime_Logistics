--Checking first few rows (It gives you an overview of the structure of the dataset)
SELECT * FROM shipments LIMIT 10;

--Getting basic statistics (This will give you the average weight of the shipments and the average delay (positive or negative) in days)
SELECT
    AVG(tonnage) AS avg_tonnage,
    AVG(delay_days) AS avg_delay_days
FROM shipments;

--Filter Shipments by Cargo type (If you want to analyze a specific cargo type, for example, Containers)
-->This will return the total number of container shipments and the average tonnage for those shipments.
SELECT COUNT(*) AS total_containers, AVG(tonnage) AS avg_tonnage
FROM shipments
WHERE cargo_type = 'Containers';  

--Find Shipments with Delay (This query will return the top 10 shipments with the most delayed departure dates)
SELECT shipment_id, arrival_date, departure_date, delay_days
FROM shipments
WHERE delay_days > 0
ORDER BY delay_days DESC
LIMIT 10;

--Shipments by Shipping Company (This will show you the shipping companies sorted by the total tonnage they shipped)
-->get total tonnage per shipping company
SELECT shipping_company, SUM(tonnage) AS total_tonnage 
FROM shipments
GROUP BY shipping_company
ORDER BY total_tonnage DESC;

--Get Shipments btw Specific Dates (This will return all shipments within the specified date range)
-->find all shipments that arrived within a specific date range, say from January 1, 2024 to March 31, 2024
SELECT shipment_id, arrival_date, departure_date, cargo_type
FROM shipments
WHERE arrival_date BETWEEN '2024-01-01' AND '2024-03-31';
