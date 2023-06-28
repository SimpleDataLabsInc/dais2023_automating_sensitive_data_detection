from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from packaged_pipeline.config.ConfigStore import *
from packaged_pipeline.udfs.UDFs import *
from prophecy.utils import *
from prophecy.transpiler import call_spark_fcn
from prophecy.transpiler.fixed_file_schema import *
from packaged_pipeline.graph import *

def pipeline(spark: SparkSession) -> None:
    df_new_clean_encrypted_ds = new_clean_encrypted_ds(spark)
    df_decompress_decrypt = decompress_decrypt(spark, Config.decompress_decrypt, df_new_clean_encrypted_ds)
    df_check_k_anonmity_out0, df_check_k_anonmity_orElse0 = check_k_anonmity(
        spark, 
        Config.check_k_anonmity, 
        df_decompress_decrypt
    )
    df_mask_test_result_comments = mask_test_result_comments(
        spark, 
        Config.mask_test_result_comments, 
        df_check_k_anonmity_out0
    )
    masked_demo_data(spark, df_mask_test_result_comments)
    quarantined_demo_data(spark, df_check_k_anonmity_orElse0)
    copy_tables(spark, Config.copy_tables)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()\
                .newSession()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/packaged_pipeline")
    registerUDFs(spark)
    
    MetricsCollector.start(spark = spark, pipelineId = "pipelines/packaged_pipeline")
    pipeline(spark)
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
