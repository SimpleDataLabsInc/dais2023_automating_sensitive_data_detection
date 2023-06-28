from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from prophecy.transpiler import call_spark_fcn
from prophecy.transpiler.fixed_file_schema import *
from packaged_pipeline.config.ConfigStore import *
from packaged_pipeline.udfs.UDFs import *

def quarantined_demo_data(spark: SparkSession, in0: DataFrame):
    in0.write.format("delta").mode("overwrite").saveAsTable(f"clean_room.demo_data.quartantined_demo_data_base")
