<details>
<summary><h1>Quiz Questions</h1></summary>

Complete the Quiz shown below. It's a set of 6 multiple-choice questions to test your understanding of workflow orchestration, Kestra and ETL pipelines for data lakes and warehouses.

1) Within the execution for `Yellow` Taxi data for the year `2020` and month `12`: what is the uncompressed file size (i.e. the output file `yellow_tripdata_2020-12.csv` of the `extract` task)?
- 128.3 MB
- 134.5 MB ✅
- 364.7 MB
- 692.6 MB

2) What is the rendered value of the variable `file` when the inputs `taxi` is set to `green`, `year` is set to `2020`, and `month` is set to `04` during execution?
- `{{inputs.taxi}}_tripdata_{{inputs.year}}-{{inputs.month}}.csv` 
- `green_tripdata_2020-04.csv` ✅
- `green_tripdata_04_2020.csv`
- `green_tripdata_2020.csv`

3) How many rows are there for the `Yellow` Taxi data for all CSV files in the year 2020?
- 13,537.299
- 24,648,499 ✅
- 18,324,219
- 29,430,127

4) How many rows are there for the `Green` Taxi data for all CSV files in the year 2020?
- 5,327,301
- 936,199
- 1,734,051 ✅
- 1,342,034

5) How many rows are there for the `Yellow` Taxi data for the March 2021 CSV file?
- 1,428,092
- 706,911
- 1,925,152 ✅
- 2,561,031

6) How would you configure the timezone to New York in a Schedule trigger?
- Add a `timezone` property set to `EST` in the `Schedule` trigger configuration  
- Add a `timezone` property set to `America/New_York` in the `Schedule` trigger configuration ✅
- Add a `timezone` property set to `UTC-5` in the `Schedule` trigger configuration
- Add a `location` property set to `New_York` in the `Schedule` trigger configuration  
</details>

<details>
<summary><h1>Setup and Prerequisites</h1></summary>

## Installing Google Cloud SDK on macOS
1. Using Homebrew (recommended):
```bash
brew install --cask google-cloud-sdk
```

2. Verify installation:
```bash
gcloud --version
```

## Authentication and Configuration
1. Login to Google Cloud:
```bash
gcloud auth login
```

2. Set the project:
```bash
gcloud config set project kestra-project-450102
```

3. Authenticate application default credentials (needed for BigQuery):
```bash
gcloud auth application-default login
```

## Required Resources
- Project ID: `kestra-project-450102`
- BigQuery Dataset: `de_zoomcamp`
- BigQuery Tables: 
  - `yellow_tripdata`
  - `green_tripdata`
- Cloud Storage Bucket: `gs://zoomcamp-data-store`

The GCP configuration can be found in `Week02/kestra/flows/04_gcp_kv.yaml`. Key settings include:
```yaml
# Configuration file location: Week02/kestra/flows/04_gcp_kv.yaml
tasks:
  - id: gcp_project_id
    type: io.kestra.plugin.core.kv.Set
    key: GCP_PROJECT_ID
    kvType: STRING
    value: kestra-project-450102  # Your project ID

  - id: gcp_dataset
    type: io.kestra.plugin.core.kv.Set
    key: GCP_DATASET
    kvType: STRING
    value: de_zoomcamp  # Your BigQuery dataset name

  - id: gcp_bucket_name
    type: io.kestra.plugin.core.kv.Set
    key: GCP_BUCKET_NAME
    kvType: STRING
    value: zoomcamp-data-store  # Your Cloud Storage bucket name
```
</details>

# Answers and Commands

## Q1: Yellow Taxi December 2020 File Size
**Question:** What is the uncompressed file size of `yellow_tripdata_2020-12.csv`?
**Answer:** 134.5 MB

Command used:
```bash
gsutil ls -l gs://zoomcamp-data-store/yellow_tripdata_2020-12.csv
```
Output:
```
 134481400  2025-02-06T06:55:40Z  gs://zoomcamp-data-store/yellow_tripdata_2020-12.csv
TOTAL: 1 objects, 134481400 bytes (128.25 MiB)
```

## Q2: Green Taxi File Name Pattern
**Question:** What is the rendered filename for Green taxi data (2020-04)?
**Answer:** `green_tripdata_2020-04.csv`

Command used:
```bash
gsutil ls gs://zoomcamp-data-store/green_tripdata_2020-04.csv
```

## Q3: Yellow Taxi 2020 Total Records
**Question:** How many rows are in Yellow Taxi data for 2020?
**Answer:** 24,648,499 rows

Command used:
```bash
bq query --use_legacy_sql=false 'SELECT COUNT(*) as total_rows 
FROM `kestra-project-450102.de_zoomcamp.yellow_tripdata` 
WHERE EXTRACT(YEAR FROM tpep_pickup_datetime) = 2020'
```
Output:
```
+------------+
| total_rows |
+------------+
|   24648663 |
+------------+
```

## Q4: Green Taxi 2020 Total Records
**Question:** How many rows are in Green Taxi data for 2020?
**Answer:** 1,734,051 rows

Command used:
```bash
bq query --use_legacy_sql=false 'SELECT COUNT(*) as total_rows 
FROM `kestra-project-450102.de_zoomcamp.green_tripdata` 
WHERE EXTRACT(YEAR FROM lpep_pickup_datetime) = 2020'
```
Output:
```
+------------+
| total_rows |
+------------+
|    1734039 |
+------------+
```

## Q5: Yellow Taxi March 2021 Records
**Question:** How many rows are in Yellow Taxi data for March 2021?
**Answer:** 1,925,152 rows

Command used:
```bash
bq query --use_legacy_sql=false 'SELECT COUNT(*) as total_rows 
FROM `kestra-project-450102.de_zoomcamp.yellow_tripdata` 
WHERE EXTRACT(YEAR FROM tpep_pickup_datetime) = 2021 
AND EXTRACT(MONTH FROM tpep_pickup_datetime) = 3'
```
Output:
```
+------------+
| total_rows |
+------------+
|    1925130 |
+------------+
```

## Q6: Kestra Schedule Configuration
**Question:** How to configure New York timezone in Schedule trigger?
**Answer:** Add a `timezone` property set to `America/New_York` in the `Schedule` trigger configuration 

Example configuration:
```yaml
triggers:
  - id: schedule
    type: io.kestra.core.models.triggers.types.Schedule
    timezone: America/New_York  # IANA timezone database name
    cron: "0 0 * * *"  # Example cron expression for daily at midnight
```

References:
- [Kestra Schedule Trigger Documentation](https://kestra.io/plugins/core/triggers/io.kestra.plugin.core.trigger.schedule) - Official documentation for Kestra's Schedule trigger configuration
- [IANA Time Zone Database](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) - Official list of timezone names like `America/New_York`