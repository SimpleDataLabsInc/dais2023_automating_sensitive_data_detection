from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from prophecy.transpiler import call_spark_fcn
from prophecy.transpiler.fixed_file_schema import *
from aggregate_data_pipeline.config.ConfigStore import *
from aggregate_data_pipeline.udfs.UDFs import *

def Aggregate_patients_by_zip(spark: SparkSession, in0: DataFrame) -> DataFrame:
    df1 = in0.groupBy(col("patient_state"), col("diagnosis_code"))

    return df1.agg(countDistinct(col("patient_id")).alias("num_patients"))
