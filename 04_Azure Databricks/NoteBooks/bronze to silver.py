# Databricks notebook source
# MAGIC %md
# MAGIC #bronze to silver transformation of all tables

# COMMAND ----------

dbutils.fs.ls("/mnt/bronze-layer/SalesLT/")

# COMMAND ----------

table_name = []
for i in dbutils.fs.ls("/mnt/bronze-layer/SalesLT/"):
    table_name.append(i.name.split('/')[0])

# COMMAND ----------

table_name

# COMMAND ----------

from pyspark.sql.functions import from_utc_timestamp, date_format
from pyspark.sql.types import TimestampType

for i in table_name:
    path = "/mnt/bronze-layer/SalesLT/" + i + '/' + i + ".parquet"
    df = spark.read.format('parquet').load(path)
    column = df.columns

    for col in column:
        if 'Date' in col or 'date' in col:
            df = df.withColumn(col, date_format(from_utc_timestamp(df[col].cast(TimestampType()), 'UTC'), 'yyy-mm-dd'))
    output_path = '/mnt/silver-layer/SalesLT/' + i + '/'
    df.write.format('delta').mode('overwrite').save(output_path)

# COMMAND ----------

display(df)

# COMMAND ----------


