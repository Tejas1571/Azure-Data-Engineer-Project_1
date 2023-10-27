# Databricks notebook source
# MAGIC %md
# MAGIC #Connection to ADLS

# COMMAND ----------

configs = {
  "fs.azure.account.auth.type": "CustomAccessToken",
  "fs.azure.account.custom.token.provider.class": spark.conf.get("spark.databricks.passthrough.adls.gen2.tokenProviderClassName")
}

# Optionally, you can add <directory-name> to the source URI of your mount point.
dbutils.fs.mount(
  source = "abfss://bronze-layer@001azstorageaccount.dfs.core.windows.net/",
  mount_point = "/mnt/bronze-layer",
  extra_configs = configs)

# COMMAND ----------

dbutils.fs.ls("/mnt/bronze-layer")

# COMMAND ----------

configs = {
  "fs.azure.account.auth.type": "CustomAccessToken",
  "fs.azure.account.custom.token.provider.class": spark.conf.get("spark.databricks.passthrough.adls.gen2.tokenProviderClassName")
}

# Optionally, you can add <directory-name> to the source URI of your mount point.
dbutils.fs.mount(
  source = "abfss://silver-layer@001azstorageaccount.dfs.core.windows.net/",
  mount_point = "/mnt/silver-layer",
  extra_configs = configs)

# COMMAND ----------

dbutils.fs.ls("/mnt/silver-layer")

# COMMAND ----------

configs = {
  "fs.azure.account.auth.type": "CustomAccessToken",
  "fs.azure.account.custom.token.provider.class": spark.conf.get("spark.databricks.passthrough.adls.gen2.tokenProviderClassName")
}

# Optionally, you can add <directory-name> to the source URI of your mount point.
dbutils.fs.mount(
  source = "abfss://gold-layer@001azstorageaccount.dfs.core.windows.net/",
  mount_point = "/mnt/gold-layer",
  extra_configs = configs)

# COMMAND ----------

dbutils.fs.ls("/mnt/gold-layer")
