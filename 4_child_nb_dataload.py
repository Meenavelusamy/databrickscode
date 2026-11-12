# Databricks notebook source
# MAGIC %py
# MAGIC import requests
# MAGIC
# MAGIC # 1. Perform API call to pull the CSV data into a Python variable
# MAGIC url = "https://public.tableau.com/app/sample-data/mobile_os_usage.csv"
# MAGIC response = requests.get(url)
# MAGIC response.raise_for_status()  # Ensures the request succeeded before writing
# MAGIC
# MAGIC # 2. Write the text content into the Unity Catalog volume
# MAGIC volume_path = "/Volumes/workspace/default/usage_metrics/mobile_os_usage.csv"
# MAGIC dbutils.fs.put(volume_path, response.text, overwrite=True)
# MAGIC

# COMMAND ----------

spark.read.csv("/Volumes/workspace/default/usage_metrics/mobile_os_usage.csv", header=True).display()