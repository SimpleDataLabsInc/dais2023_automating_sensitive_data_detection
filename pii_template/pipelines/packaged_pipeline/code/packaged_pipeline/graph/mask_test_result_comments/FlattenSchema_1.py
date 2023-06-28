from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from prophecy.transpiler import call_spark_fcn
from prophecy.transpiler.fixed_file_schema import *
from .config import *
from packaged_pipeline.udfs.UDFs import *

def FlattenSchema_1(spark: SparkSession, in0: DataFrame) -> DataFrame:
    flt_col = in0.withColumn("output_data", explode_outer("output_data")).columns
    selectCols = [col("input_data") if "input_data" in flt_col else col("input_data"),                   col("output_data-entity") if "output_data-entity" in flt_col else col("output_data.entity")\
                    .alias("output_data-entity"),                   col("output_data-score") if "output_data-score" in flt_col else col("output_data.score")\
                    .alias("output_data-score"),                   col("output_data-word") if "output_data-word" in flt_col else col("output_data.word")\
                    .alias("output_data-word"),                   col("output_data-start") if "output_data-start" in flt_col else col("output_data.start")\
                    .alias("output_data-start"),                   col("output_data-end") if "output_data-end" in flt_col else col("output_data.end").alias("output_data-end"),                   col("projected_record_id") if "projected_record_id" in flt_col else col("projected_record_id")]

    return in0.withColumn("output_data", explode_outer("output_data")).select(*selectCols)
