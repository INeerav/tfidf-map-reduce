import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node Amazon S3
AmazonS3_node1699470580477 = glueContext.create_dynamic_frame.from_options(
    format_options={"quoteChar": '"', "withHeader": True, "separator": ","},
    connection_type="s3",
    format="csv",
    connection_options={
        "paths": ["s3://emails-6a3d13b0/csv/clintonmails.csv"],
        "recurse": True,
    },
    transformation_ctx="AmazonS3_node1699470580477",
)

# Script generated for node Change Schema
ChangeSchema_node1699470599276 = ApplyMapping.apply(
    frame=AmazonS3_node1699470580477,
    mappings=[],
    transformation_ctx="ChangeSchema_node1699470599276",
)

# Script generated for node Amazon S3
AmazonS3_node1699470612338 = glueContext.write_dynamic_frame.from_options(
    frame=ChangeSchema_node1699470599276,
    connection_type="s3",
    format="glueparquet",
    connection_options={"path": "s3://emails-6a3d13b0/output/", "partitionKeys": []},
    format_options={"compression": "snappy"},
    transformation_ctx="AmazonS3_node1699470612338",
)

job.commit()
