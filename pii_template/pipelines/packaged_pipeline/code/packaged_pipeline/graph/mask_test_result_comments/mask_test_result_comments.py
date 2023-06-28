from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.transpiler import call_spark_fcn
from prophecy.transpiler.fixed_file_schema import *
from . import *
from .config import *

def mask_test_result_comments(spark: SparkSession, config: SubgraphConfig, in0: DataFrame) -> DataFrame:
    Config.update(config)
    df_Projection_For_Masking = Projection_For_Masking(spark, in0)
    df_Get_Model_Output = Get_Model_Output(spark, df_Projection_For_Masking)
    df_FlattenSchema_1 = FlattenSchema_1(spark, df_Get_Model_Output)
    df_Filter_By_Entity_Type = Filter_By_Entity_Type(spark, df_FlattenSchema_1)
    df_Collecting_Start_End_Indices = Collecting_Start_End_Indices(spark, df_Filter_By_Entity_Type)
    df_SchemaTransform_1 = SchemaTransform_1(spark, in0)
    df_Group_By_Record = Group_By_Record(spark, df_Collecting_Start_End_Indices)
    df_Masking_With_Star = Masking_With_Star(spark, df_Group_By_Record)
    df_Join_1 = Join_1(spark, df_Masking_With_Star, df_SchemaTransform_1)

    return df_Join_1
