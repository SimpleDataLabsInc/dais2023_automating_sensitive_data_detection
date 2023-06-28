from prophecy.config import ConfigBase


class Config(ConfigBase):

    def __init__(self, encryptionKey: str=None, databricks_token: str=None, **kwargs):
        self.spark = None
        self.update(encryptionKey, databricks_token)

    def update(
            self,
            encryptionKey: str="nadeesh:encryption_key",
            databricks_token: str="nadeesh:databricks_token",
            **kwargs
    ):
        prophecy_spark = self.spark

        if encryptionKey is not None:
            self.encryptionKey = self.get_dbutils(prophecy_spark).secrets.get(*encryptionKey.split(":"))

        if databricks_token is not None:
            self.databricks_token = self.get_dbutils(prophecy_spark).secrets.get(*databricks_token.split(":"))

        pass
