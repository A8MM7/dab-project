import os
import sys
import pytest

sys.path.append(os.getcwd())  # Ensure the project root is in the path for imports  

@pytest.fixture()
def spark():
    try:
        from databricks.connect import DatabricksSession
        spark = DatabricksSession.builder.getOrCreate()
    except ImportError:
        try:
            from pyspark.sql import SparkSession
            spark = SparkSession.builder.getOrCreate()
        except:
            raise ImportError("Neither DatabricksSession nor SparkSession could be imported.")
    return spark