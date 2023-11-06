from snowflake.snowpark.session import Session
from snowflake.snowpark.types import IntegerType, FloatType
from snowflake.snowpark.functions import avg, sum, col, udf, call_udf, call_builtin, year
import streamlit as st
import pandas as pd
from datetime import date

# scikit-learn (install: pip install -U scikit-learn)
from sklearn.linear_model import LinearRegression


connection_parameters = {
  "ACCOUNT":"eighty451.east-us-2.azure",
  "USER":"SVC_STRATUM_STAGING_SOURCE_MEASUREMENTS_RO",
  "PASSWORD":"???",
  "ROLE":"STRATUM_STAGING_DEV_SOURCE_MEASUREMENTS_RO_AR",
  "DATABASE":"STRATUM_STAGING_DEV",
  "SCHEMA":"SOURCE_MEASUREMENTS",
  "WAREHOUSE":"STRATUM_STAGING_ADHOC_WH"
}

sess = Session.builder.configs(connection_parameters).create()

df = sess.sql("select current_role(), current_database(), current_schema(), current_warehouse()")

df.show()