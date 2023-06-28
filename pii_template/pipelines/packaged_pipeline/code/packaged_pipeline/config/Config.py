from packaged_pipeline.graph.decompress_decrypt.config.Config import SubgraphConfig as decompress_decrypt_Config
from packaged_pipeline.graph.check_k_anonmity.config.Config import SubgraphConfig as check_k_anonmity_Config
from packaged_pipeline.graph.mask_test_result_comments.config.Config import (
    SubgraphConfig as mask_test_result_comments_Config
)
from packaged_pipeline.graph.copy_tables.config.Config import SubgraphConfig as copy_tables_Config
from prophecy.config import ConfigBase


class Config(ConfigBase):

    def __init__(
            self,
            mask_test_result_comments: dict=None,
            check_k_anonmity: dict=None,
            encryptionKey: str=None,
            databricks_token: str=None,
            min_num_patients: int=None,
            mask_character: str=None,
            decompress_decrypt: dict=None,
            copy_tables: dict=None,
            **kwargs
    ):
        self.spark = None
        self.update(
            mask_test_result_comments, 
            check_k_anonmity, 
            encryptionKey, 
            databricks_token, 
            min_num_patients, 
            mask_character, 
            decompress_decrypt, 
            copy_tables
        )

    def update(
            self,
            mask_test_result_comments: dict={},
            check_k_anonmity: dict={},
            encryptionKey: str="nadeesh:encryption_key",
            databricks_token: str="nadeesh:databricks_token",
            min_num_patients: int=3,
            mask_character: str="*",
            decompress_decrypt: dict={},
            copy_tables: dict={},
            **kwargs
    ):
        prophecy_spark = self.spark
        self.mask_test_result_comments = self.get_config_object(
            prophecy_spark, 
            mask_test_result_comments_Config(prophecy_spark = prophecy_spark), 
            mask_test_result_comments, 
            mask_test_result_comments_Config
        )
        self.check_k_anonmity = self.get_config_object(
            prophecy_spark, 
            check_k_anonmity_Config(prophecy_spark = prophecy_spark), 
            check_k_anonmity, 
            check_k_anonmity_Config
        )

        if encryptionKey is not None:
            self.encryptionKey = self.get_dbutils(prophecy_spark).secrets.get(*encryptionKey.split(":"))

        if databricks_token is not None:
            self.databricks_token = self.get_dbutils(prophecy_spark).secrets.get(*databricks_token.split(":"))

        self.min_num_patients = self.get_int_value(min_num_patients)
        self.mask_character = mask_character
        self.decompress_decrypt = self.get_config_object(
            prophecy_spark, 
            decompress_decrypt_Config(prophecy_spark = prophecy_spark), 
            decompress_decrypt, 
            decompress_decrypt_Config
        )
        self.copy_tables = self.get_config_object(
            prophecy_spark, 
            copy_tables_Config(prophecy_spark = prophecy_spark), 
            copy_tables, 
            copy_tables_Config
        )
        pass
