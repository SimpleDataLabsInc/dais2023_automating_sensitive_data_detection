from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.transpiler import call_spark_fcn
from prophecy.transpiler.fixed_file_schema import *
from . import *
from .config import *

def copy_tables(spark: SparkSession, config: SubgraphConfig) -> None:
    Config.update(config)
    copy_script(spark)
