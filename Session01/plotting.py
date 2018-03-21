import matplotlib
matplotlib.use("TkAgg")

from matplotlib import pyplot

# 1. Prepare database
labels = ["Web", "iOS", "Android", "React Native"]
values = [40, 20, 35, 15]
colors = ["red", "orange", "yellow", "beige"]
explode = [0, 0.2, 0, 0]

# 2. Plot
pyplot.pie(values,
           labels=labels,
           colors=colors,
           explode = explode,
           shadow = True)
           
pyplot.axis("equal")



# 3. Show
pyplot.show()
