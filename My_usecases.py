# Databricks notebook source
# MAGIC %md
# MAGIC # Task1:Document the Notebook Using mark down %md

# COMMAND ----------

# MAGIC %md
# MAGIC ![Inceptez group picture](https://fpimages.withfloats.com/actual/6929d1ac956d0a744b5c9822.jpeg)
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ##Basic markdown tasks

# COMMAND ----------

name = "Meena Velusamy"
displayHTML(f'<h2 style="color: #008080; font-family: sans-serif;">{name}</h2>')

# COMMAND ----------

# MAGIC %md 
# MAGIC # Task 2 Create a volume namely usage_metrics using sql magic command %sql
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC CREATE VOLUME IF NOT EXISTS usage_metrics;

# COMMAND ----------

# MAGIC %md 
# MAGIC # Task 3: Create a child notebook "4_child_nb_dataload" and write code to load data, Using the requests library, perform api call to pull data from "https://public.tableau.com/app/sample-data/mobile_os_usage.csv" into a python variable using the magic command %py and write the data into the created volume "/Volumes/workspace/default/usage_metrics/mobile_os_usage.csv" using the above variable.text using the magic command dbutils.fs.put("volume",variable.text,overwrite=True)

# COMMAND ----------

# MAGIC %run ./4_child_nb_dataload

# COMMAND ----------

# MAGIC %md
# MAGIC Task 4: Call the notebook 4_child_nb_dataload using the magic command %run

# COMMAND ----------

# MAGIC %run ./4_child_nb_dataload
# MAGIC

# COMMAND ----------

# MAGIC %md 
# MAGIC Task 5: list the file is created in the given volume or not and do the head of this file using fs magic command %fs

# COMMAND ----------

# MAGIC %fs ls /Volumes/workspace/default/usage_metrics/
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC Task6: Create a pyspark dataframe df1 reading the data from the above file using pyspark magic command %python

# COMMAND ----------

file_path = "/Volumes/workspace/default/usage_metrics/mobile_os_usage.csv"

df1 = (
    spark.read
    .option("header", "true")
    .option("inferSchema", "true")
    .csv(file_path)
)

display(df1)

# COMMAND ----------

# MAGIC %md
# MAGIC # Task7: Write the above dataframe df1 data into a databricks table called 'default.mobile_os_usage' using pyspark magic command %python

# COMMAND ----------

# Replace spaces in column names with underscores for Delta table compatibility
df1_clean = (
    df1
    .withColumnRenamed("Mobile Operating System", "Mobile_Operating_System")
    .withColumnRenamed("Percent of Usage", "Percent_of_Usage")
)

# Write the DataFrame to the Databricks Delta table
df1_clean.write.mode("overwrite").saveAsTable("default.mobile_os_usage")

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM default.mobile_os_usage LIMIT 10;
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC # Task8: Write sql query to display the data loaded into the table 'default.mobile_os_usage' using the pyspark magic command %python

# COMMAND ----------

df_result = spark.sql("SELECT * FROM default.mobile_os_usage")
display(df_result)

# COMMAND ----------

# MAGIC %md
# MAGIC # Task9: Create a python function to convert the given input to upper case

# COMMAND ----------

def to_upper_case(text):
    if text is None:
        return None
    return str(text).upper()

# Example usage
print(to_upper_case("mobile_os_usage"))

# COMMAND ----------

from pyspark.sql.functions import upper, col

df_upper = df1_clean.withColumn("Mobile_Operating_System", upper(col("Mobile_Operating_System")))
display(df_upper)

# COMMAND ----------

from pyspark.sql.functions import udf, col
from pyspark.sql.types import StringType

# Load the saved table directly
df_table = spark.table("default.mobile_os_usage")

# Apply your custom uppercase UDF
to_upper_udf = udf(to_upper_case, StringType())
df_upper = df_table.withColumn("Mobile_Operating_System", to_upper_udf(col("Mobile_Operating_System")))

display(df_upper)

# COMMAND ----------

from pyspark.sql.functions import udf, col
from pyspark.sql.types import StringType

to_upper_udf = udf(to_upper_case, StringType())
df_upper = df1.withColumn("Mobile Operating System", to_upper_udf(col("Mobile Operating System")))

display(df_upper)

# COMMAND ----------

# MAGIC %md
# MAGIC # Task10: Install pandas library using the pip python magic command %pip

# COMMAND ----------

# MAGIC %pip install pandas
# MAGIC

# COMMAND ----------

# MAGIC %restart_python

# COMMAND ----------

# MAGIC %md
# MAGIC # Task11: Import pandas, using pandas read_csv and display the output using the magic command %python
# MAGIC
# MAGIC

# COMMAND ----------

import pandas as pd

file_path = "/Volumes/workspace/default/usage_metrics/mobile_os_usage.csv"
pdf = pd.read_csv(file_path)

display(pdf)

# COMMAND ----------

# MAGIC %md
# MAGIC # Task12: echo "Magic commands tasks completed" using the linux shell magic command %sh

# COMMAND ----------

# MAGIC %sh
# MAGIC echo "Magic commands tasks completed"
# MAGIC