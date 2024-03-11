from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from sample_pipeline.config.ConfigStore import *
from sample_pipeline.udfs.UDFs import *

def dq_verified_output(spark: SparkSession, in0: DataFrame):
    in0.write.format("delta").mode("overwrite").saveAsTable("`ntong`.`default`.`deequ_verified_output`")
