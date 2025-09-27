def i():
    return "Practical 9: PySpark DataFrame + RDD Operations (Load, Transform, Join, MapReduce)"


def i1():
    return """!pip install pyspark"""


def i2():
    return """from pyspark.sql import SparkSession
from pyspark.sql.functions import sum

spark = SparkSession.builder.appName("LoadAndDisplayData").getOrCreate()"""


def i3():
    return """df = spark.read.csv("Orders.csv", header=True, inferSchema=True)
customer_df = spark.read.csv("Customer.csv", header=True, inferSchema=True)"""


def i4():
    return """print("DataFrame Content")
df.show()

print("DataFrame Structure:")
df.printSchema()"""


def i5():
    return """filtered_Orders = df.filter(df.Quantity > 1)
print("Order Quantity Greater than 1:")
filtered_Orders.show()"""


def i6():
    return """product_revenue = df.groupBy("Product").agg(sum("Price").alias("totalRevenue"))
print("Total Revenue by Product:")
product_revenue.show()"""


def i7():
    return """joined_df = df.join(customer_df, on="CustomerID", how="inner")
print("Joined DataFrame:")
joined_df.show()

sc.stop()"""


def i8():
    return """from pyspark import SparkContext

sc = SparkContext("local", "Resilient Distributed Databases (RDD)")
rdd = sc.parallelize([1, 2, 3, 4, 5])
print(rdd.collect())

sc.stop()"""


def i9():
    return """from pyspark import SparkContext

sc = SparkContext("local", "Resilient Distributed Databases (RDD)")
rdd = sc.textFile("Customer_data.txt")
print(rdd.count())

sc.stop()"""


def i10():
    return """from pyspark import SparkContext

sc = SparkContext("local", "Resilient Distributed Databases (RDD)")
rdd = sc.parallelize([1, 2, 3, 4, 5])
squared_rdd = rdd.map(lambda x: x**x)
even_rdd = rdd.filter(lambda x: x % 2 == 0)

print("Even_RDD: ", even_rdd.collect())
print("Square_RDD: ", squared_rdd.collect())

sc.stop()"""


def i11():
    return """from pyspark import SparkContext

sc = SparkContext("local","RDD Creation Example")
rdd = sc.parallelize([("a",1),("b",2),("a",3),("b",4)])
result = rdd.reduceByKey(lambda x,y: x+y)
print(result.collect())

result.saveAsTextFile("output.txt")

output = sc.textFile("output.txt")
print(output.count())

sc.stop()"""
