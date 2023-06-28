from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from prophecy.transpiler import call_spark_fcn
from prophecy.transpiler.fixed_file_schema import *
from .config import *
from packaged_pipeline.udfs.UDFs import *

def Filter_By_Entity_Type(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.filter(col("`output_data-entity`").isin(lit("HCW"), lit("PATIENT")))
