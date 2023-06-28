from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from prophecy.transpiler import call_spark_fcn
from prophecy.transpiler.fixed_file_schema import *
from .config import *
from packaged_pipeline.udfs.UDFs import *

def decryption(spark: SparkSession, in0: DataFrame) -> DataFrame:
    from cryptography.fernet import Fernet
    import numpy as np
    import pandas as pd
    import base64

    def base64_encode(value: str) -> str:
        encoded = base64.urlsafe_b64encode(str.encode(value))
        result = encoded.rstrip(b"=")

        return result.decode()

    def base64_decode(value: str) -> str:
        padding = 4 - (len(value) % 4)
        value = value + ("=" * padding)
        result = base64.urlsafe_b64decode(value)

        return result.decode()

    encryptionKeyFinal = base64_decode(base64_encode(Config.encryptionKey))

    for column in in0.columns:
        in0 = in0.withColumn(column, decrypt(col(column).cast("string"), lit(encryptionKeyFinal)))

    out0 = in0

    return out0
