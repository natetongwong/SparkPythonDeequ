from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from sample_pipeline.config.ConfigStore import *
from sample_pipeline.udfs.UDFs import *

def Deequ_1(spark: SparkSession, in0: DataFrame) -> (DataFrame, DataFrame):
    from pydeequ.checks import Check, CheckLevel
    from pydeequ.verification import VerificationSuite, VerificationResult

    return (in0,
            VerificationResult.checkResultsAsDataFrame(
              spark,
              VerificationSuite(spark).onData(in0).addCheck(Check(spark, CheckLevel.Error, "Review Check")).run()
            ))
