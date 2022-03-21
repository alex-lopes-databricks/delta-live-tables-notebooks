# Databricks notebook source
json_path = "/databricks-datasets/wikipedia-datasets/data-001/clickstream/raw-uncompressed-json/2015_2_clickstream.json"
def external_func():     
    return (
    spark.read.option("inferSchema", "true").json(json_path))
