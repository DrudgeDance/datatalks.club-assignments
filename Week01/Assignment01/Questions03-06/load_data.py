import pandas as pd
from sqlalchemy import create_engine
import time
import os

def wait_for_postgres():
    """Wait for PostgreSQL to be ready"""
    print("Checking data files...")
    if not os.path.exists('taxi_zone_lookup.csv'):
        raise Exception("taxi_zone_lookup.csv not found!")
    if not os.path.exists('green_tripdata_2019-10.csv.gz'):
        raise Exception("green_tripdata_2019-10.csv.gz not found!")

    print("Connecting to PostgreSQL...")
    engine = create_engine('postgresql://user:pass@pgdatabase:5432/ny_taxi')
    retries = 5
    while retries > 0:
        try:
            conn = engine.connect()
            conn.close()
            print("Successfully connected to PostgreSQL")
            return engine
        except Exception as e:
            print(f"Failed to connect: {e}")
            retries -= 1
            time.sleep(5)
    raise Exception("Could not connect to PostgreSQL")

def load_data():
    print("Starting data load...")
    engine = wait_for_postgres()
    
    # Load taxi zones
    print("Loading taxi zones...")
    try:
        print("Reading taxi_zone_lookup.csv...")
        zones_df = pd.read_csv('taxi_zone_lookup.csv')
        print(f"Loaded zones file with {len(zones_df)} rows and columns: {zones_df.columns.tolist()}")
        zones_df.to_sql('taxi_zones', engine, if_exists='replace', index=False)
        print("Taxi zones loaded successfully")
    except Exception as e:
        print(f"Error loading zones: {e}")
        raise

    # Load trip data
    print("Loading trip data...")
    try:
        print("Reading green_tripdata_2019-10.csv.gz...")
        chunks = pd.read_csv('green_tripdata_2019-10.csv.gz', 
                        compression='gzip', 
                        iterator=True, 
                        chunksize=100000)

        for i, chunk in enumerate(chunks):
            chunk.to_sql('green_taxi_trips', engine, 
                        if_exists='append' if i > 0 else 'replace', 
                        index=False)
            print(f"Loaded chunk {i+1} with {len(chunk)} rows")
    except Exception as e:
        print(f"Error loading trip data: {e}")
        raise

    print("All data loaded successfully!")

if __name__ == '__main__':
    load_data() 