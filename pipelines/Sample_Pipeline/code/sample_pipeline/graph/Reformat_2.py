from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from sample_pipeline.config.ConfigStore import *
from sample_pipeline.udfs.UDFs import *

def Reformat_2(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        col("check"), 
        col("check_level"), 
        col("check_status"), 
        col("constraint"), 
        col("constraint_status"), 
        col("constraint_message"), 
        current_timestamp().alias("insert_ts")
    )
