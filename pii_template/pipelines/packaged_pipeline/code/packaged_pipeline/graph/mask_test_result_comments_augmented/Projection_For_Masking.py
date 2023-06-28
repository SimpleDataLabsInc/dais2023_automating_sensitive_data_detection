from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from prophecy.transpiler import call_spark_fcn
from prophecy.transpiler.fixed_file_schema import *
from .config import *
from packaged_pipeline.udfs.UDFs import *

def Projection_For_Masking(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(expr(Config.id_field).alias("projected_record_id"), expr(Config.input_column).alias("input_data"))
