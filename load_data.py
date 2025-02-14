import pandas as pd
import psycopg2

# Load CSV into DataFrame
df = pd.read_csv("simulated_port_data.csv")

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="port_data",
    user="postgres",
    password="20022020",  # place your PostgreSQL password
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# Insert data into PostgreSQL
for _, row in df.iterrows():
    cur.execute("""
        INSERT INTO shipments (shipment_id, arrival_date, departure_date, cargo_type, shipping_company,
                               port_of_origin, port_of_destination, tonnage, delay_days)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
    """, tuple(row))

# Commit & Close Connection
conn.commit()
cur.close()
conn.close()

print("Data successfully loaded into PostgreSQL!")
