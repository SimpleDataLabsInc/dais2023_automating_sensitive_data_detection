from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from prophecy.transpiler import call_spark_fcn
from prophecy.transpiler.fixed_file_schema import *
from .config import *
from packaged_pipeline.udfs.UDFs import *

def patients_per_zip_state_diag(spark: SparkSession) -> DataFrame:
    return spark.read.table(f"clean_room.demo_data.patients_per_state_diagnosis")
