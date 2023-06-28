from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from prophecy.transpiler import call_spark_fcn
from prophecy.transpiler.fixed_file_schema import *
from .config import *
from packaged_pipeline.udfs.UDFs import *

def distribute_rows(spark: SparkSession, in0: DataFrame) -> (DataFrame, DataFrame):
    df1 = in0.filter(
        (
          (col("num_patients_in_state_with_same_diag_code").isNull() | (col("num_patients_in_state_with_same_diag_code") > lit(Config.min_num_patients)))
          & (~ col("is_rare_diagnosis") | col("is_rare_diagnosis").isNull())
        )
    )
    df2 = in0.filter(
        ~ (
          (col("num_patients_in_state_with_same_diag_code").isNull() | (col("num_patients_in_state_with_same_diag_code") > lit(Config.min_num_patients)))
          & (~ col("is_rare_diagnosis") | col("is_rare_diagnosis").isNull())
        )
    )

    return df1, df2
