from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.transpiler import call_spark_fcn
from prophecy.transpiler.fixed_file_schema import *
from . import *
from .config import *

def check_k_anonmity(spark: SparkSession, config: SubgraphConfig, in0: DataFrame) -> (DataFrame, DataFrame):
    Config.update(config)
    df_ref_loinc = ref_loinc(spark)
    ref_loinc_lookup(spark, df_ref_loinc)
    df_ref_diagnosis_with_is_rare = ref_diagnosis_with_is_rare(spark)
    ref_diagnosis_lookup(spark, df_ref_diagnosis_with_is_rare)
    df_patients_per_zip_state_diag = patients_per_zip_state_diag(spark)
    df_limit_for_increasing_demo_speed = limit_for_increasing_demo_speed(spark, in0)
    df_add_references = add_references(spark, df_limit_for_increasing_demo_speed)
    df_join_patients_per_zip_state_diag = join_patients_per_zip_state_diag(
        spark, 
        df_add_references, 
        df_patients_per_zip_state_diag
    )
    df_distribute_rows_out0, df_distribute_rows_orElse = distribute_rows(spark, df_join_patients_per_zip_state_diag)

    return df_distribute_rows_out0, df_distribute_rows_orElse
