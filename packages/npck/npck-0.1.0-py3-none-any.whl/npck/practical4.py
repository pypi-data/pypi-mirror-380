def d():
    return "Practical 4: PySpark RDD to DataFrame – Numbers list example"


def d1():
    return """from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("test").getOrCreate()
sc = spark.sparkContext"""


def d2():
    return """numbers_list = [1,2,3,4,5,6,7,8,9,10]"""


def d3():
    return """rdd = sc.parallelize(numbers_list)"""


def d4():
    return """df_numbers = rdd.map(lambda x: (x,)).toDF(["numbers"])"""


def d5():
    return """df_numbers.show()"""
