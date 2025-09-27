def h():
    return "Practical 8: PySpark Inner Join – Combine employees with departments"


def h1():
    return """from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("test").getOrCreate()
sc = spark.sparkContext"""


def h2():
    return """left = [(1,"Alice"), (2,"Bob"), (3,"Charlie")]"""


def h3():
    return """right = [(1,"HR"), (2,"IT"), (4,"Finance")]"""


def h4():
    return """df_emp = spark.createDataFrame(left, ["employee_id","employee_name"])"""


def h5():
    return """df_dept = spark.createDataFrame(right, ["employee_id","department_name"])"""


def h6():
    return """joined = df_emp.join(df_dept, on="employee_id", how="inner")"""


def h7():
    return """joined.show()"""
