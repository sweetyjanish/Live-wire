import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x,y)
plt.show()

# barh()
plt.barh(x, y)
plt.show()

#argument color change with name 
plt.bar(x, y, color = "red")
plt.show()

#colour name with name 
plt.bar(x, y, color = "hotpink")
plt.show()

#hexa code colour(color code change )
plt.bar(x, y, color = "#4CAF50")
plt.show()

#bar width size change
plt.bar(x, y, width = 0.1)
plt.show()

#Bar Height size change 
plt.barh(x, y, height = 0.1)
plt.show()