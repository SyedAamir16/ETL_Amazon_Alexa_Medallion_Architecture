# Amazon Alexa Medallion ETL

This project builds a simple medallion ETL pipeline on top of the `amazon_alexa.tsv` dataset using PySpark and Hive.

## Architecture

- `bronze`: raw TSV ingested with minimal transformation plus ingestion metadata
- `silver`: cleaned and standardized review records
- `gold`: business aggregates for reporting and downstream analytics

## Project layout

- `src/amazon_alexa_medallion/config.py`: shared table names and defaults
- `src/amazon_alexa_medallion/spark_utils.py`: Spark session creation with Hive support
- `src/amazon_alexa_medallion/jobs/bronze.py`: raw ingestion job
- `src/amazon_alexa_medallion/jobs/silver.py`: cleaning and conformance job
- `src/amazon_alexa_medallion/jobs/gold.py`: aggregate job
- `run_pipeline.py`: orchestration entry point
- `requirements.txt`: Python dependencies

## Dataset

Expected columns in the source TSV:

- `rating`
- `date`
- `variation`
- `verified_reviews`
- `feedback`

## Example run

```powershell
cd C:\Users\Mustafa\Documents\Playground\amazon_alexa_medallion
spark-submit run_pipeline.py --input "C:\Users\Mustafa\Downloads\amazon_alexa.tsv"
```

To override the Hive database or warehouse path:

```powershell
spark-submit run_pipeline.py `
  --input "C:\Users\Mustafa\Downloads\amazon_alexa.tsv" `
  --database amazon_alexa `
  --warehouse-dir "C:\Users\Mustafa\Documents\Playground\amazon_alexa_medallion\warehouse"
```

## Hive tables created

- `amazon_alexa.bronze_reviews`
- `amazon_alexa.silver_reviews`
- `amazon_alexa.gold_variation_summary`
- `amazon_alexa.gold_daily_review_summary`
- `amazon_alexa.gold_feedback_summary`

## Notes

- The pipeline uses `saveAsTable`, so Hive support must be available in the Spark environment.
- Bronze and silver are stored as Parquet-backed Hive tables.
- Gold tables are regenerated on each run using `overwrite` mode.
