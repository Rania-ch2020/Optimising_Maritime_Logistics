import pandas as pd
import random
from datetime import datetime, timedelta

# Define cargo types and shipping companies
cargo_types = ["Liquid Bulk", "Solid Bulk", "General Cargo", "Containers", "Vehicles"]
shipping_companies = ["Maersk", "MSC", "CMA CGM", "Hapag-Lloyd", "Evergreen", "ONE", "COSCO"]
ports = ["Rotterdam", "Shanghai", "Los Angeles", "Singapore", "Dubai", "New York", "Tokyo", "Antwerp"]

# Generate 100 rows of data
data = []
for i in range(1, 101):
    arrival_date = datetime(2024, random.randint(1, 12), random.randint(1, 28))
    departure_date = arrival_date + timedelta(days=random.randint(1, 15))
    delay_days = random.randint(-2, 10)  # Some shipments arrive early (-), some are delayed (+)
    
    data.append([
        f"SHIP_{i:04d}",  # Unique Shipment ID
        arrival_date.strftime("%Y-%m-%d"),  # Format date
        departure_date.strftime("%Y-%m-%d"),
        random.choice(cargo_types),
        random.choice(shipping_companies),
        random.choice(ports),
        random.choice(ports),
        round(random.uniform(100, 5000), 2),  # Tonnage (random weight)
        delay_days
    ])

# Create DataFrame
columns = ["Shipment_ID", "Arrival_Date", "Departure_Date", "Cargo_Type", "Shipping_Company",
           "Port_of_Origin", "Port_of_Destination", "Tonnage", "Delay_Days"]
df = pd.DataFrame(data, columns=columns)

# Save to CSV
df.to_csv("simulated_port_data.csv", index=False)

print("CSV file 'simulated_port_data.csv' generated successfully!")
