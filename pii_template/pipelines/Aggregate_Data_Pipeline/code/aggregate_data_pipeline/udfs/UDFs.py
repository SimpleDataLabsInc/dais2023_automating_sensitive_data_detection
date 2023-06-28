from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.transpiler import ABIUtil, BigDecimal, ScalaUtil, getContentAsStream, call_spark_fcn, substring_scala
from prophecy.lookups import (
    createLookup,
    createRangeLookup,
    lookup,
    lookup_last,
    lookup_match,
    lookup_count,
    lookup_row,
    lookup_row_reverse,
    lookup_nth
)

def registerUDFs(spark: SparkSession):
    spark.udf.register("decrypt", decrypt)
    spark.udf.register("encrypt", encrypt)
    spark.udf.register("get_model_response_single_with_schema", get_model_response_single_with_schema)
    spark.udf.register("mask_output_data", mask_output_data)
    ScalaUtil.initializeUDFs(spark)

def decryptGenerator():
    import pyspark.sql.functions as F
    import pyspark.sql.types as T
    from cryptography.fernet import Fernet
    import numpy as np
    import pandas as pd

    @udf(returnType = StringType())
    def func(cipher_text, MASTER_KEY):

        if (
            not cipher_text
            or cipher_text == np.nan
            or pd.isna(cipher_text)
            or cipher_text != cipher_text
            or not str(cipher_text)
            or cipher_text is None
        ):
            cipher_text = ''

        from cryptography.fernet import Fernet
        f = Fernet(MASTER_KEY)
        clear_val = f.decrypt(cipher_text.encode()).decode()

        return clear_val

    return func

decrypt = decryptGenerator()

def encryptGenerator():
    import pyspark.sql.functions as F
    import pyspark.sql.types as T
    from cryptography.fernet import Fernet
    import numpy as np
    import pandas as pd

    @udf(returnType = StringType())
    def func(clear_text, MASTER_KEY):

        if (
            not clear_text
            or clear_text == np.nan
            or pd.isna(clear_text)
            or clear_text != clear_text
            or not str(clear_text)
            or clear_text is None
        ):
            clear_text = ''

        from cryptography.fernet import Fernet
        f = Fernet(MASTER_KEY)
        clear_text_b = bytes(clear_text, 'utf-8')
        cipher_text = f.encrypt(clear_text_b)
        cipher_text = str(cipher_text.decode('ascii'))

        return cipher_text

    return func

encrypt = encryptGenerator()

def get_model_response_single_with_schemaGenerator():
    import requests
    import os
    import json
    from pyspark.sql.types import StringType, ArrayType, StructField, StructType, IntegerType, DoubleType

    @udf(
         returnType = ArrayType(
           StructType([
                             StructField("entity", StringType(), True),
                             StructField("score", DoubleType(), True),
                             StructField("index", DoubleType(), True),
                             StructField("word", StringType(), True),
                             StructField("start", IntegerType(), True),
                             StructField("end", IntegerType(), True),
             
         ]),
           True
         )
    )
    def func(message: str) -> dict:
        url = 'https://dbc-19bbe7b0-ce18.cloud.databricks.com/serving-endpoints/test-pii-model/invocations'
        headers = {'Authorization' : f'Bearer {Config.databricks_token}', 'Content-Type' : 'application/json'}
        data_json = json.dumps({'inputs' : [message]})
        response = requests.request(method = 'POST', headers = headers, url = url, data = data_json)

        if response.status_code != 200:
            raise Exception(f'Request failed with status {response.status_code}, {response.text}')

        return response.json().get('predictions')[0]

    return func

get_model_response_single_with_schema = get_model_response_single_with_schemaGenerator()

@udf(returnType = StringType())
def mask_output_data(input_string, output_indexes_to_mask):
    output_string = input_string

    for index_tuple in output_indexes_to_mask:
        output_string = (
            output_string[:index_tuple[0]]
            + (Config.mask_character * (index_tuple[1] - index_tuple[0]))
            + output_string[index_tuple[1]:]
        )

    return output_string
