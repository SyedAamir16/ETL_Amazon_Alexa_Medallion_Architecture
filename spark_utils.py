from pyspark.sql import SparkSession


def create_spark_session(app_name: str, warehouse_dir: str) -> SparkSession:
    spark = (
        SparkSession.builder.appName(app_name)
        .config("spark.sql.warehouse.dir", warehouse_dir)
        .config("spark.sql.sources.partitionOverwriteMode", "dynamic")
        .enableHiveSupport()
        .getOrCreate()
    )
    spark.sparkContext.setLogLevel("WARN")
    return spark
