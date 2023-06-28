from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from prophecy.transpiler import call_spark_fcn
from prophecy.transpiler.fixed_file_schema import *
from .config import *
from packaged_pipeline.udfs.UDFs import *

def preprocess(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        col("record_id"), 
        col("record_created_dt"), 
        col("claim_id"), 
        col("patient_id"), 
        col("patient_gender"), 
        col("patient_age"), 
        col("patient_year_of_birth"), 
        col("patient_zip3"), 
        col("patient_state"), 
        col("date_service"), 
        col("date_specimen"), 
        col("diagnosis_code"), 
        col("procedure_code"), 
        col("loinc_code"), 
        col("test_ordered_name"), 
        col("test_result_value"), 
        col("test_result_name"), 
        col("date_report"), 
        col("time_report"), 
        col("lab_id"), 
        col("lab_test_id"), 
        col("lab_test_number"), 
        col("test_battery_local_id"), 
        col("test_battery_std_id"), 
        col("test_battery_name"), 
        col("test_ordered_local_id"), 
        col("test_ordered_std_id"), 
        col("result_id"), 
        col("result_unit_of_measure"), 
        col("ref_range"), 
        col("abnormal_flag"), 
        col("fasting_status"), 
        col("lab_npi"), 
        col("payer_id"), 
        col("payer_id_qual"), 
        col("payer_name"), 
        col("ordering_provider_npi"), 
        col("ordering_name"), 
        col("ordering_market_type"), 
        col("ordering_specialty"), 
        col("ordering_state"), 
        col("ordering_zip"), 
        expr("replace(test_result_comments, '~^~', ' ')").alias("test_result_comments"), 
        col("testing_comments")
    )
