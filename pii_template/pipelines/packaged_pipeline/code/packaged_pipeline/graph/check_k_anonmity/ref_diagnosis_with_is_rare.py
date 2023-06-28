from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from prophecy.transpiler import call_spark_fcn
from prophecy.transpiler.fixed_file_schema import *
from .config import *
from packaged_pipeline.udfs.UDFs import *

def ref_diagnosis_with_is_rare(spark: SparkSession) -> DataFrame:
    return spark.read.table(f"clean_room.demo_data.final_ref_diagnosis_table")
