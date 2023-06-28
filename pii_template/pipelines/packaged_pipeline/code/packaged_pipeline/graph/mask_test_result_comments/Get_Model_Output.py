from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from prophecy.transpiler import call_spark_fcn
from prophecy.transpiler.fixed_file_schema import *
from .config import *
from packaged_pipeline.udfs.UDFs import *

def Get_Model_Output(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        col("projected_record_id"), 
        col("input_data"), 
        get_model_response_single_with_schema(col("input_data")).alias("output_data")
    )
