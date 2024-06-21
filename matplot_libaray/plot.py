import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

#pyplot
plt.plot(xpoints, ypoints)
plt.show()

#Plotting Without Line
plt.plot(xpoints, ypoints, 'o')
plt.show()

#multiple points
xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])

plt.plot(xpoints, ypoints)
plt.show()

#Default X-Points
ypoints = np.array([3, 8, 1, 10, 5, 7])

plt.plot(ypoints)
plt.show()

#markers as o
plt.plot(ypoints, marker = 'o')
plt.show()

#markers as *
plt.plot(ypoints, marker = '*')
plt.show()

#formate string
plt.plot(ypoints, 'o:r')
plt.show()

#markersize or the shorter version, ms
plt.plot(ypoints, marker = 'o', ms = 20)
plt.show()

#markeredgecolor or the shorter mec
plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r')
plt.show()

#markerfacecolor or the shorter mfc
plt.plot(ypoints, marker = 'o', ms = 20, mfc = 'r')
plt.show()

# both the mec and mfc
plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r', mfc = 'r')
plt.show()

# Hexadecimal color values:
plt.plot(ypoints, marker = 'o', ms = 20, mec = '#4CAF50', mfc = '#4CAF50')
plt.show()

#colour markers
plt.plot(ypoints, marker = 'o', ms = 20, mec = 'hotpink', mfc = 'hotpink')
plt.show()

#Linestyle
plt.plot(ypoints, linestyle = 'dotted')
plt.show()

plt.plot(ypoints, linestyle = 'dashed')
plt.show()

#line colour
plt.plot(ypoints, color = 'r')
plt.show()

plt.plot(ypoints, c = '#4CAF50')
plt.show()

plt.plot(ypoints, c = 'hotpink')
plt.show()

#Line Width or the shorter lw
plt.plot(ypoints, linewidth = '20.5')
plt.show()

#Multiple Lines plt.plot()
y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])

plt.plot(y1)
plt.plot(y2)

plt.show()

#using multiple x,y
x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])

plt.plot(x1, y1, x2, y2)
plt.show()