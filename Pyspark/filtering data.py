from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Filtering full names with Sirname").getOrCreate()

rdd=spark.sparkContext.textFile("D:/CSV files/Full_Names.csv")

# *To get the count of each sirname
# rdd1=rdd.flatMap(lambda x:x.split(","))
# rdd2=rdd1.map(lambda x:x.split(" ")[1])
# rdd3=rdd2.map(lambda x:(x,1))
# rdd4=rdd3.reduceByKey(lambda x,y:x+y)
#
# print(rdd4.collect())
#Output : [(u'Takate', 15), (u'Jagtap', 15), (u'Name', 1), (u'Mogal', 20)]



# *To filter the data according to the sirnames e.g Takate

# rdd1=rdd.filter(lambda x:"Takate" in x and "n" in x)
# print(rdd1.collect())
# Output : [u'Kiran Takate', u'Arun Takate', u'Sachin Takate', u'Tanmay Takate', u'Nitin Takate']


# get the count of names start with specific letter

# rdd1=rdd.flatMap(lambda x:x.split(","))
# rdd2=rdd1.map(lambda x:x.split()[0][0])
# rdd3=rdd2.map(lambda x:(x,1))
# rdd4=rdd3.reduceByKey(lambda x,y:x+y)
#
# print(rdd4.collect())

#Output : [(u'A', 8), (u'G', 1), (u'I', 1), (u'K', 4), (u'M', 3), (u'O', 1), (u'S', 8), (u'D', 2), (u'F', 1), (u'H', 1), (u'J', 1), (u'N', 3), (u'P', 4), (u'R', 7), (u'T', 1), (u'V', 5)]