from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from prophecy.transpiler import call_spark_fcn
from prophecy.transpiler.fixed_file_schema import *
from packaged_pipeline.config.ConfigStore import *
from packaged_pipeline.udfs.UDFs import *

def new_clean_encrypted_ds(spark: SparkSession) -> DataFrame:
    return spark.read.table(f"clean_room.demo_data.encrypted_vendor_1_data")
