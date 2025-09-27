def e():
    return "Practical 5: PySpark DataFrame Filter – People older than 30"


def e1():
    return """from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.appName("test").getOrCreate()
sc = spark.sparkContext"""


def e2():
    return """data = [("Alice",25), ("Bob",35), ("Charlie",40), ("David",28), ("Eva",32)]"""


def e3():
    return """df_people = spark.createDataFrame(data, ["name","age"])"""


def e4():
    return """df_people.filter(col("age") > 30).show()"""
