from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from prophecy.transpiler import call_spark_fcn
from prophecy.transpiler.fixed_file_schema import *
from packaged_pipeline.config.ConfigStore import *
from packaged_pipeline.udfs.UDFs import *

def masked_demo_data(spark: SparkSession, in0: DataFrame):
    if spark.catalog._jcatalog.tableExists(f"clean_room.demo_data.masked_demo_data_base"):
        from delta.tables import DeltaTable, DeltaMergeBuilder
        DeltaTable\
            .forName(spark, f"clean_room.demo_data.masked_demo_data_base")\
            .alias("target")\
            .merge(in0.alias("source"), (col("source.record_id") == col("target.record_id")))\
            .whenMatchedUpdateAll()\
            .whenNotMatchedInsertAll()\
            .execute()
    else:
        in0.write\
            .format("delta")\
            .option("overwriteSchema", True)\
            .mode("overwrite")\
            .saveAsTable(f"clean_room.demo_data.masked_demo_data_base")
