from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from prophecy.transpiler import call_spark_fcn
from prophecy.transpiler.fixed_file_schema import *
from .config import *
from packaged_pipeline.udfs.UDFs import *

def join_patients_per_zip_state_diag(spark: SparkSession, in0: DataFrame, in1: DataFrame, ) -> DataFrame:
    return in0\
        .alias("in0")\
        .join(
          in1.alias("in1"),
          (
            (col("in0.patient_state") == col("in1.patient_state"))
            & (col("in0.diagnosis_code") == col("in1.diagnosis_code"))
          ),
          "left_outer"
        )\
        .select(col("in0.record_id").alias("record_id"), col("in0.record_created_dt").alias("record_created_dt"), col("in0.claim_id").alias("claim_id"), col("in0.patient_id").alias("patient_id"), col("in0.patient_gender").alias("patient_gender"), col("in0.patient_age").alias("patient_age"), col("in0.patient_year_of_birth").alias("patient_year_of_birth"), col("in0.patient_zip3").alias("patient_zip3"), col("in0.patient_state").alias("patient_state"), col("in0.date_service").alias("date_service"), col("in0.date_specimen").alias("date_specimen"), col("in0.diagnosis_code").alias("diagnosis_code"), col("in0.diagnosis_description").alias("diagnosis_description"), col("in0.procedure_code").alias("procedure_code"), col("in0.loinc_code").alias("loinc_code"), col("in0.loinc_component").alias("loinc_component"), col("in0.test_ordered_name").alias("test_ordered_name"), col("in0.test_result_value").alias("test_result_value"), col("in0.test_result_name").alias("test_result_name"), col("in0.test_result_comments").alias("test_result_comments"), col("in0.date_report").alias("date_report"), col("in0.time_report").alias("time_report"), col("in0.lab_id").alias("lab_id"), col("in0.lab_test_id").alias("lab_test_id"), col("in0.lab_test_number").alias("lab_test_number"), col("in0.test_battery_local_id").alias("test_battery_local_id"), col("in0.test_battery_std_id").alias("test_battery_std_id"), col("in0.test_battery_name").alias("test_battery_name"), col("in0.test_ordered_local_id").alias("test_ordered_local_id"), col("in0.test_ordered_std_id").alias("test_ordered_std_id"), col("in0.result_id").alias("result_id"), col("in0.result_unit_of_measure").alias("result_unit_of_measure"), col("in0.ref_range").alias("ref_range"), col("in0.abnormal_flag").alias("abnormal_flag"), col("in0.fasting_status").alias("fasting_status"), col("in0.lab_npi").alias("lab_npi"), col("in0.payer_id").alias("payer_id"), col("in0.payer_id_qual").alias("payer_id_qual"), col("in0.payer_name").alias("payer_name"), col("in0.ordering_provider_npi").alias("ordering_provider_npi"), col("in0.ordering_name").alias("ordering_name"), col("in0.ordering_market_type").alias("ordering_market_type"), col("in0.ordering_specialty").alias("ordering_specialty"), col("in0.ordering_state").alias("ordering_state"), col("in0.ordering_zip").alias("ordering_zip"), col("in0.is_rare_diagnosis").alias("is_rare_diagnosis"), col("in1.num_patients").alias("num_patients_in_state_with_same_diag_code"), col("in0.testing_comments").alias("testing_comments"))
