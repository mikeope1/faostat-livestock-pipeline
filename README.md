# FAOSTAT Africa Livestock Pipeline

A small data pipeline that turns raw FAOSTAT livestock data for Africa into a clean, queryable SQLite database.

## What it answers
- Which countries produce the most cattle meat?
- Which countries grew chicken meat production fastest from 2014 to 2024?
- How has Africa's total egg production changed since 1964?

## Data
FAOSTAT bulk download "Production: Crops and Livestock Products" for Africa (57 countries, 1961-2024). Source: https://www.fao.org/faostat

## How it works
1. `ingest.py` loads the raw CSV and checks the expected columns exist
2. `transform.py` filters to cattle meat, chicken meat, and hen eggs, reshapes the data from wide to long format, and saves `data/clean/livestock_long.csv`
3. `load.py` loads the clean data into a SQLite database (safe to re-run, no duplicates)
4. `run_queries.py` runs the SQL in `queries.sql` and prints the results

## How to run
1. Download the FAOSTAT Africa bulk CSV and save it as `data/raw/faostat_africa_raw.csv`
2. Install the requirements: `pip install pandas`
3. Run the steps in order:

```
python ingest.py
python transform.py
python load.py
python run_queries.py
```

## What I learned
- Raw data was in wide format (one column per year), so I reshaped it to long format
- The same item appears in different units (tonnes and thousands of units), so queries must filter by unit or totals become meaningless
- Windows hid a double file extension (`.csv.csv`), which broke my file path until I checked the real file name

## Next steps
- Add a feed-cost dataset to calculate feed efficiency
- Schedule the pipeline with Airflow
- Add data quality tests