# Databricks notebook source
import sys
sys.path.append("/Workspace/Repos/dlt/delta-live-tables-notebooks/python/")

# COMMAND ----------

print(sys.path)

# COMMAND ----------

help('modules')

# COMMAND ----------

import another_file

# COMMAND ----------

another_file.external_func(spark)

# COMMAND ----------

import another_notebook
