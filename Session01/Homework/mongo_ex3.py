from pymongo import MongoClient
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot

mongo_URI = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(mongo_URI)

db = client.get_default_database()

customers = db["customers"]

ref_counting = customers.find()
ref_only = []
for i in ref_counting:
    j = i["ref"]
    ref_only.append(j)
# print(ref_only)
count = {}
for ref_option in ref_only:
    count[ref_option] = count.get(ref_option, 0) + 1
print("ads", ":", count["ads"])
print("wom", ":", count["wom"])
print("events", ":", count["events"])


labels = ["ads", "wom", "events"]
values = [count["ads"], count["wom"], count["events"]]
colors = ["red", "orange", "beige"]

pyplot.pie(values,
           labels=labels,
           colors=colors,
           )

pyplot.axis("equal")
pyplot.show()
