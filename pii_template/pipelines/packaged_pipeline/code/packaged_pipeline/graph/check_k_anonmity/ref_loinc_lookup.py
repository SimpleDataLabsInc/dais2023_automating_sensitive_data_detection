from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from prophecy.transpiler import call_spark_fcn
from prophecy.transpiler.fixed_file_schema import *
from .config import *
from packaged_pipeline.udfs.UDFs import *

def ref_loinc_lookup(spark: SparkSession, in0: DataFrame):
    keyColumns = ['''loinc_num''']
    valueColumns = ['''loinc_num''', '''component''', '''property''', '''time_aspct''', '''loinc_system''',
                    '''scale_type''', '''method_type''', '''loinc_class''',
                    '''versionlastchanged''', '''chng_type''', '''definitiondescription''',
                    '''status''', '''consumer_name''', '''classtype''', '''formula''',
                    '''exmpl_answers''', '''survey_quest_text''', '''survey_quest_src''',
                    '''unitsrequired''', '''submitted_units''', '''relatednames2''',
                    '''shortname''', '''order_obs''', '''cdisc_common_tests''',
                    '''hl7_field_subfield_id''', '''external_copyright_notice''',
                    '''example_units''', '''long_common_name''', '''unitsandrange''',
                    '''document_section''', '''example_ucum_units''', '''example_si_ucum_units''',
                    '''status_reason''', '''status_text''', '''change_reason_public''',
                    '''common_test_rank''', '''common_order_rank''', '''common_si_test_rank''',
                    '''hl7_attachment_structure''', '''external_copyright_link''', '''paneltype''',
                    '''askatorderentry''', '''associatedobservations''', '''versionfirstreleased''',
                    '''validhl7attachmentrequest''']
    createLookup("ref_loinc", in0, spark, keyColumns, valueColumns)
