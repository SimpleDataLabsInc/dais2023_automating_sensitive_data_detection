from prophecy.config import ConfigBase


class SubgraphConfig(ConfigBase):

    def __init__(
            self,
            prophecy_spark=None,
            min_num_patients: str="3",
            limit_records_for_model_inference: int=500,
            **kwargs
    ):
        self.min_num_patients = min_num_patients
        self.limit_records_for_model_inference = limit_records_for_model_inference
        pass

    def update(self, updated_config):
        self.min_num_patients = updated_config.min_num_patients
        self.limit_records_for_model_inference = updated_config.limit_records_for_model_inference
        pass

Config = SubgraphConfig()
