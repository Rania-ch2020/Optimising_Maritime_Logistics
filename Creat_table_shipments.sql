CREATE TABLE shipments (
    shipment_id VARCHAR(10) PRIMARY KEY,   -- Unique shipment identifier
    arrival_date DATE,                     -- Date when shipment arrives
    departure_date DATE,                   -- Date when shipment departs
    cargo_type VARCHAR(50),                -- Type of cargo (e.g., Containers, Vehicles)
    shipping_company VARCHAR(50),          -- Name of the shipping company
    port_of_origin VARCHAR(50),            -- Origin port
    port_of_destination VARCHAR(50),       -- Destination port
    tonnage FLOAT,                         -- Weight of cargo in tons
    delay_days INT                         -- Shipment delay in days
);



