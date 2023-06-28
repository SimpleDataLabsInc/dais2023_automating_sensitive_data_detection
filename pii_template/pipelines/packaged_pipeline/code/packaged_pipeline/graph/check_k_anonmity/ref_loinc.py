from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from prophecy.transpiler import call_spark_fcn
from prophecy.transpiler.fixed_file_schema import *
from .config import *
from packaged_pipeline.udfs.UDFs import *

def ref_loinc(spark: SparkSession) -> DataFrame:
    return spark.read\
        .schema(
          StructType([
            StructField("loinc_num", StringType(), True), StructField("component", StringType(), True), StructField("property", StringType(), True), StructField("time_aspct", StringType(), True), StructField("loinc_system", StringType(), True), StructField("scale_type", StringType(), True), StructField("method_type", StringType(), True), StructField("loinc_class", StringType(), True), StructField("versionlastchanged", StringType(), True), StructField("chng_type", StringType(), True), StructField("definitiondescription", StringType(), True), StructField("status", StringType(), True), StructField("consumer_name", StringType(), True), StructField("classtype", StringType(), True), StructField("formula", StringType(), True), StructField("exmpl_answers", StringType(), True), StructField("survey_quest_text", StringType(), True), StructField("survey_quest_src", StringType(), True), StructField("unitsrequired", StringType(), True), StructField("submitted_units", StringType(), True), StructField("relatednames2", StringType(), True), StructField("shortname", StringType(), True), StructField("order_obs", StringType(), True), StructField("cdisc_common_tests", StringType(), True), StructField("hl7_field_subfield_id", StringType(), True), StructField("external_copyright_notice", StringType(), True), StructField("example_units", StringType(), True), StructField("long_common_name", StringType(), True), StructField("unitsandrange", StringType(), True), StructField("document_section", StringType(), True), StructField("example_ucum_units", StringType(), True), StructField("example_si_ucum_units", StringType(), True), StructField("status_reason", StringType(), True), StructField("status_text", StringType(), True), StructField("change_reason_public", StringType(), True), StructField("common_test_rank", StringType(), True), StructField("common_order_rank", StringType(), True), StructField("common_si_test_rank", StringType(), True), StructField("hl7_attachment_structure", StringType(), True), StructField("external_copyright_link", StringType(), True), StructField("paneltype", StringType(), True), StructField("askatorderentry", StringType(), True), StructField("associatedobservations", StringType(), True), StructField("versionfirstreleased", StringType(), True), StructField("validhl7attachmentrequest", StringType(), True)
        ])
        )\
        .option("header", True)\
        .option("sep", ",")\
        .csv("dbfs:/FileStore/tables/v_ref_loinc.csv")
