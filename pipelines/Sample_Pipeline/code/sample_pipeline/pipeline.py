from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from sample_pipeline.config.ConfigStore import *
from sample_pipeline.udfs.UDFs import *
from prophecy.utils import *
from sample_pipeline.graph import *

def pipeline(spark: SparkSession) -> None:
    df_Script_0 = Script_0(spark)
    df_Deequ_1_out0, df_Deequ_1_out1 = Deequ_1(spark, df_Script_0)

    if df_Deequ_1_out1.where("constraint_status == 'Failure'").count() == 0:
        df_Reformat_1 = Reformat_1(spark, df_Deequ_1_out0)
        df_Filter_1 = Filter_1(spark, df_Reformat_1)
        dq_verified_output(spark, df_Filter_1)

    if df_Deequ_1_out1.where("constraint_status == 'Failure'").count() > 0:
        df_Reformat_2 = Reformat_2(spark, df_Deequ_1_out1)
        dq_failure_output(spark, df_Reformat_2)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/Sample_Pipeline")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/Sample_Pipeline", config = Config)(pipeline)

if __name__ == "__main__":
    main()
