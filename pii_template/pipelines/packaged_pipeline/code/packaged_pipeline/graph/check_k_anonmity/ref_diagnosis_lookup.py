from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from prophecy.transpiler import call_spark_fcn
from prophecy.transpiler.fixed_file_schema import *
from .config import *
from packaged_pipeline.udfs.UDFs import *

def ref_diagnosis_lookup(spark: SparkSession, in0: DataFrame):
    keyColumns = ['''diag_cd''']
    valueColumns = ['''diag_cd''', '''diag_cd_type''', '''diag_desc_short''', '''diag_desc_long''', '''diag_group''',
                    '''diag_cd_level''', '''diag_is_rare''']
    createLookup("ref_diagnosis", in0, spark, keyColumns, valueColumns)
