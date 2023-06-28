from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from prophecy.transpiler import call_spark_fcn
from prophecy.transpiler.fixed_file_schema import *
from .config import *
from packaged_pipeline.udfs.UDFs import *

def Group_By_Record(spark: SparkSession, in0: DataFrame) -> DataFrame:
    df1 = in0.groupBy(col("input_data"), col("projected_record_id"))

    return df1.agg(collect_list(col("`output-index-tuple`")).alias("output_index_list"))
