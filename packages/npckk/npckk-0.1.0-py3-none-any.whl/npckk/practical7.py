def g():
    return "Practical 7: PySpark GroupBy – Average salary per department"


def g1():
    return """from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("test").getOrCreate()
sc = spark.sparkContext"""


def g2():
    return """data = [("HR",50000), ("IT",70000), ("HR",55000), ("IT",80000), ("Sales",45000)]"""


def g3():
    return """df_dept = spark.createDataFrame(data, ["department","salary"])"""


def g4():
    return """df_dept.groupBy("department").avg("salary") \\
    .withColumnRenamed("avg(salary)","avg_salary") \\
    .show()"""
