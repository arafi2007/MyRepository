# Databricks notebook source
from pyspark.sql import DataFrame
#--from pyspark.sql import funtions as f

gvit = spark.table("gmdataassets.DL_EDGE_BASE_GAA_14918_BASE_OAGCCXWP_vcs.vehicle")
#gvit = gvit.filter("vin_id == '4W5FA1RX8N0105950'")


display(gvit)
