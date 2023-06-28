from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from prophecy.transpiler import call_spark_fcn
from prophecy.transpiler.fixed_file_schema import *
from .config import *
from packaged_pipeline.udfs.UDFs import *

def Collecting_Start_End_Indices(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        col("input_data"), 
        col("`output_data-entity`"), 
        col("`output_data-score`"), 
        col("`output_data-word`"), 
        array(col("`output_data-start`"), col("`output_data-end`")).alias("output-index-tuple"), 
        col("projected_record_id")
    )
