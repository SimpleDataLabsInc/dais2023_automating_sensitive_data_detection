from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from prophecy.transpiler import call_spark_fcn
from prophecy.transpiler.fixed_file_schema import *
from aggregate_data_pipeline.config.ConfigStore import *
from aggregate_data_pipeline.udfs.UDFs import *

def patients_per_zip_state_diag(spark: SparkSession, in0: DataFrame):
    in0.write.format("delta").mode("overwrite").saveAsTable(f"clean_room.demo_data.patients_per_zip_state_diagnosis")
