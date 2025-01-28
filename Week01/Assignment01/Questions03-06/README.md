# NYC Green Taxi Data Analysis

## Architecture

This project uses Docker Compose to orchestrate two services:
1. `pgdatabase`: PostgreSQL database storing taxi trip data
2. `data_loader`: Python service that loads data into PostgreSQL

The services communicate through a Docker network named `pg-network`, which is automatically created by Docker Compose. The data loader waits for PostgreSQL to be healthy before starting.

## Setup Instructions

1. Download the data:
```bash
# Download taxi zone lookup data
curl -L "https://d37ci6vzurychx.cloudfront.net/misc/taxi+_zone_lookup.csv" -o taxi_zone_lookup.csv 

# Download trip data
curl -L "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-10.csv.gz" -o green_tripdata_2019-10.csv.gz
```

2. Start everything with docker-compose:
```bash
docker compose up
```

This will:
- Create a Docker network for service communication
- Start PostgreSQL and wait for it to be healthy
- Build and run the data loader automatically
- Load all data into the database

To shut everything down and clean up:
```bash
docker compose down
```

## Running Queries

Connect to PostgreSQL in a new terminal:
```bash
docker exec -it questions03-06-pgdatabase-1 psql -U user -d ny_taxi
```

You will see a PostgreSQL prompt, where you can run the analysis queries below.

## Analysis Queries

### Question 3: Trip Segmentation by Time of Day
Hourly distribution:
```sql
-- Get trips per hour
SELECT 
  CAST(SUBSTRING(lpep_pickup_datetime, 12, 2) AS INTEGER) as hour,
  COUNT(*) as count 
FROM green_taxi_trips 
GROUP BY hour 
ORDER BY hour;
```

Results:
```
Hour | Count   | Time Period
-----|---------|------------
0    | 10,594  | Night
1    |  7,109  | Night
2    |  5,121  | Night
3    |  4,238  | Night
4    |  4,304  | Night
5    |  4,474  | Night
6    |  8,250  | Morning
7    | 16,082  | Morning
8    | 23,568  | Morning
9    | 26,692  | Morning
10   | 26,615  | Morning
11   | 26,159  | Afternoon
12   | 26,873  | Afternoon
13   | 25,149  | Afternoon
14   | 27,680  | Afternoon
15   | 29,898  | Afternoon
16   | 30,863  | Afternoon
17   | 33,400  | Afternoon
18   | 31,910  | Evening
19   | 28,815  | Evening
20   | 24,292  | Evening
21   | 21,271  | Evening
22   | 17,801  | Late Night
23   | 15,228  | Late Night
```

Time periods:
```sql
WITH hourly AS (
  SELECT 
    CAST(SUBSTRING(lpep_pickup_datetime, 12, 2) AS INTEGER) as hour,
    COUNT(*) as cnt 
  FROM green_taxi_trips 
  GROUP BY hour
)
SELECT 
  CASE 
    WHEN hour BETWEEN 0 AND 5 THEN 'Night'
    WHEN hour BETWEEN 6 AND 10 THEN 'Morning'
    WHEN hour BETWEEN 11 AND 17 THEN 'Afternoon'
    WHEN hour BETWEEN 18 AND 21 THEN 'Evening'
    ELSE 'Late Night'
  END as time_period,
  SUM(cnt) as count
FROM hourly 
GROUP BY 
  CASE 
    WHEN hour BETWEEN 0 AND 5 THEN 'Night'
    WHEN hour BETWEEN 6 AND 10 THEN 'Morning'
    WHEN hour BETWEEN 11 AND 17 THEN 'Afternoon'
    WHEN hour BETWEEN 18 AND 21 THEN 'Evening'
    ELSE 'Late Night'
  END
ORDER BY count DESC;
```

Results:
```
Time Period | Count   | Hours Covered
------------|---------|---------------
Afternoon   | 200,022 | 11:00-17:59 (7 hours)
Evening     | 106,288 | 18:00-21:59 (4 hours)
Morning     | 101,207 | 06:00-10:59 (5 hours)
Night       |  35,840 | 00:00-05:59 (6 hours)
Late Night  |  33,029 | 22:00-23:59 (2 hours)
```


### Question 4: Longest Trip
```sql
SELECT SUBSTRING(lpep_pickup_datetime, 1, 10) as date, 
       trip_distance
FROM green_taxi_trips 
ORDER BY trip_distance DESC 
LIMIT 5;
```

### Question 5: Biggest Pickup Zones
```sql
SELECT tz."Zone", 
       COUNT(*) as pickup_count 
FROM green_taxi_trips t 
JOIN taxi_zones tz 
  ON t."PULocationID" = tz."LocationID" 
GROUP BY tz."Zone" 
ORDER BY pickup_count DESC 
LIMIT 10;
```

### Question 6: Largest Tip
```sql
SELECT tz."Zone", 
       t.tip_amount 
FROM green_taxi_trips t 
JOIN taxi_zones tz 
  ON t."DOLocationID" = tz."LocationID" 
ORDER BY t.tip_amount DESC 
LIMIT 5;
```

## Answers for Questions 3-6

1. Trip Segmentation by Time of Day:
   - Afternoon (11:00-17:59): 200,022 trips
   - Evening (18:00-21:59): 106,288 trips
   | Morning (06:00-10:59): 101,207 trips
   - Night (00:00-05:59): 35,840 trips
   - Late Night (22:00-23:59): 33,029 trips
2. Longest Trip Date: 2019-10-31 (515.89 miles)
3. Biggest Pickup Zones: East Harlem North, East Harlem South, Morningside Heights
4. Largest Tip Zone: JFK Airport
