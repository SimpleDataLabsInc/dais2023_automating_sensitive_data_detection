from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from prophecy.transpiler import call_spark_fcn
from prophecy.transpiler.fixed_file_schema import *
from .config import *
from packaged_pipeline.udfs.UDFs import *

def Masking_With_Star(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        col("input_data"), 
        mask_output_data(col("input_data"), col("output_index_list")).alias("output_data"), 
        col("projected_record_id")
    )
