import argparse
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent
SRC_DIR = PROJECT_ROOT / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from amazon_alexa_medallion.config import PipelineConfig
from amazon_alexa_medallion.jobs.bronze import run_bronze
from amazon_alexa_medallion.jobs.gold import run_gold
from amazon_alexa_medallion.jobs.silver import run_silver
from amazon_alexa_medallion.spark_utils import create_spark_session


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run the Amazon Alexa medallion ETL pipeline.")
    parser.add_argument("--input", required=True, help="Path to the source TSV file.")
    parser.add_argument("--database", default="amazon_alexa", help="Hive database name.")
    parser.add_argument(
        "--warehouse-dir",
        default="warehouse",
        help="Spark SQL warehouse directory.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    config = PipelineConfig(
        input_path=args.input,
        database=args.database,
        warehouse_dir=args.warehouse_dir,
    )

    spark = create_spark_session(
        app_name="amazon-alexa-medallion-etl",
        warehouse_dir=config.warehouse_dir,
    )

    try:
        run_bronze(spark, config)
        run_silver(spark, config)
        run_gold(spark, config)
    finally:
        spark.stop()


if __name__ == "__main__":
    main()
