from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from aggregate_data_pipeline.config.ConfigStore import *
from aggregate_data_pipeline.udfs.UDFs import *
from prophecy.utils import *
from prophecy.transpiler import call_spark_fcn
from prophecy.transpiler.fixed_file_schema import *
from aggregate_data_pipeline.graph import *

def pipeline(spark: SparkSession) -> None:
    df_enriched_demo_data = enriched_demo_data(spark)
    df_Aggregate_patients_by_zip = Aggregate_patients_by_zip(spark, df_enriched_demo_data)
    patients_per_zip_state_diag(spark, df_Aggregate_patients_by_zip)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()\
                .newSession()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/Aggregate_Data_Pipeline")
    registerUDFs(spark)
    
    MetricsCollector.start(spark = spark, pipelineId = "pipelines/Aggregate_Data_Pipeline")
    pipeline(spark)
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
