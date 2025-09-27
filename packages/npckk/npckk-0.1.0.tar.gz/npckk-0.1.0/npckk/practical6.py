def f():
    return "Practical 6: PySpark Word Count – Count word frequencies from text lines"


def f1():
    return """from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("test").getOrCreate()
sc = spark.sparkContext"""


def f2():
    return """lines = ["hello world", "hello Spark", "hello PySpark world"]"""


def f3():
    return """rdd_lines = sc.parallelize(lines)"""


def f4():
    return """word_counts = (rdd_lines
    .flatMap(lambda line: line.split())
    .map(lambda w: (w.lower(), 1))
    .reduceByKey(lambda a,b: a+b))"""


def f5():
    return """print(word_counts.collect())"""
