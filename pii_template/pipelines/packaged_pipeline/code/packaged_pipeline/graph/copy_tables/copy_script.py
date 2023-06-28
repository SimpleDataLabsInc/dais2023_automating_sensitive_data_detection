from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from prophecy.transpiler import call_spark_fcn
from prophecy.transpiler.fixed_file_schema import *
from .config import *
from packaged_pipeline.udfs.UDFs import *

def copy_script(spark: SparkSession):
    
    source_catalog = Config.source_catalog
    source_schema = Config.source_schema
    target_catalog = Config.target_catalog
    target_schema = Config.target_schema

    for table in Config.tables:
        writer = spark.sql(f"""select * from {source_catalog}.{source_schema}.{table}""").write

        if spark.catalog.tableExists(f"{target_catalog}.{target_schema}.{table}"):
            writer = writer.mode('append')

        writer.saveAsTable(f"{target_catalog}.{target_schema}.{table}")

    return 
