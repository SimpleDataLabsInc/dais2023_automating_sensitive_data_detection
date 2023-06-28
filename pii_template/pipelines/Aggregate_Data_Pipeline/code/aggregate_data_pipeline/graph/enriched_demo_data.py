from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from prophecy.transpiler import call_spark_fcn
from prophecy.transpiler.fixed_file_schema import *
from aggregate_data_pipeline.config.ConfigStore import *
from aggregate_data_pipeline.udfs.UDFs import *

def enriched_demo_data(spark: SparkSession) -> DataFrame:
    return spark.read.format("parquet").load("dbfs:/tmp/enriched_dataset/pii_enriched_data.parquet/")
