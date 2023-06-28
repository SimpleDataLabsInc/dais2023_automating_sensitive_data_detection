from prophecy.config import ConfigBase


class SubgraphConfig(ConfigBase):

    def __init__(
            self,
            prophecy_spark=None,
            encryptionKey: str="nadeesh:encryption_key",
            databricks_token: str="nadeesh:databricks_token",
            **kwargs
    ):

        if encryptionKey is not None:
            self.encryptionKey = self.get_dbutils(prophecy_spark).secrets.get(*encryptionKey.split(":"))

        if databricks_token is not None:
            self.databricks_token = self.get_dbutils(prophecy_spark).secrets.get(*databricks_token.split(":"))

        pass

    def update(self, updated_config):
        self.encryptionKey = updated_config.encryptionKey
        self.databricks_token = updated_config.databricks_token
        pass

Config = SubgraphConfig()
