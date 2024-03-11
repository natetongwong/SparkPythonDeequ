from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from sample_pipeline.config.ConfigStore import *
from sample_pipeline.udfs.UDFs import *

def Script_0(spark: SparkSession) -> DataFrame:
    out0 = spark.sparkContext\
               .parallelize([
Row(a = "foo", b = 1, c = 5), Row(a = "bar", b = 2, c = 6), Row(a = "baz", b = - 1, c = None)])\
               .toDF()

    return out0
