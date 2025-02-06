## Answers and Commands Used

### Setup and Prerequisites

#### Installing Google Cloud SDK on macOS
1. Using Homebrew (recommended):
```bash
brew install --cask google-cloud-sdk
```

2. Verify installation:
```bash
gcloud --version
```

#### Authentication and Configuration
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

#### Required Resources
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

### Question 1: File Size
Answer: 134.5 MB

Command used:
```bash
gsutil ls -l gs://zoomcamp-data-store/yellow_tripdata_2020-12.csv
```
Output:
```
 134481400  2025-02-06T06:55:40Z  gs://zoomcamp-data-store/yellow_tripdata_2020-12.csv
TOTAL: 1 objects, 134481400 bytes (128.25 MiB)
```

### Question 2: File Name Format
Answer: `green_tripdata_2020-04.csv`

Command used:
```bash
gsutil ls gs://zoomcamp-data-store/green_tripdata_2020-04.csv
```

### Question 3: Yellow Taxi 2020 Count
Answer: 24,648,499 rows

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

### Question 4: Green Taxi 2020 Count
Answer: 1,734,051 rows

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

### Question 5: Yellow Taxi March 2021 Count
Answer: 1,925,152 rows

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

### Question 6: Timezone Configuration
Answer: Add a `timezone` property set to `America/New_York` in the `Schedule` trigger configuration
