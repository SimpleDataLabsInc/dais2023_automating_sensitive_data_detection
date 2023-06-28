from pyspark.sql import SparkSession
from prophecy.config.utils import *
from .Config import Config as ConfigClass
Config: ConfigClass = ConfigClass()


class Utils:
    @staticmethod
    def initializeFromArgs(spark: SparkSession, args, default_conf="packaged_pipeline.conf"):
        global Config
        Config.updateSpark(spark)
        conf = parse_config(args, default_conf)
        Config.update(**conf)
