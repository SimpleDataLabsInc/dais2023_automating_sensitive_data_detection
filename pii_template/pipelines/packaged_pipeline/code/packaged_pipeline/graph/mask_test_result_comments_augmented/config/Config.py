from prophecy.config import ConfigBase


class SubgraphConfig(ConfigBase):

    def __init__(
            self,
            prophecy_spark=None,
            input_column: str="input",
            filter_entity: str="True",
            id_field: str="record_id",
            **kwargs
    ):
        self.input_column = input_column
        self.filter_entity = filter_entity
        self.id_field = id_field
        pass

    def update(self, updated_config):
        self.input_column = updated_config.input_column
        self.filter_entity = updated_config.filter_entity
        self.id_field = updated_config.id_field
        pass

Config = SubgraphConfig()
