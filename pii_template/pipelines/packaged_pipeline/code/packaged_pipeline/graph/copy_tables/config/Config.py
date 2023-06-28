from prophecy.config import ConfigBase


class SubgraphConfig(ConfigBase):

    def __init__(
            self,
            prophecy_spark=None,
            source_catalog: str="clean_room",
            source_schema: str="demo_data",
            tables: list=["masked_demo_data"],
            target_catalog: str="clean_room",
            target_schema: str="hv",
            **kwargs
    ):
        self.source_catalog = source_catalog
        self.source_schema = source_schema
        self.tables = tables
        self.target_catalog = target_catalog
        self.target_schema = target_schema
        pass

    def update(self, updated_config):
        self.source_catalog = updated_config.source_catalog
        self.source_schema = updated_config.source_schema
        self.tables = updated_config.tables
        self.target_catalog = updated_config.target_catalog
        self.target_schema = updated_config.target_schema
        pass

Config = SubgraphConfig()
