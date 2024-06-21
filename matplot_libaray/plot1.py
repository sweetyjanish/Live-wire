import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x, y)


#Matplotlib Labels and Title
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.title("Sports Watch Data")

plt.show()

#fonts setting
font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}

plt.title("Sports Watch Data", fontdict = font1)
plt.xlabel("Average Pulse", fontdict = font2)
plt.ylabel("Calorie Burnage", fontdict = font2)

plt.plot(x, y)
plt.show()

#loc parameter in title() to position the title.
plt.title("Sports Watch Data", loc = 'left')
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.plot(x, y)
plt.show()

#grid()
plt.plot(x, y)
plt.grid()
plt.show()

#axis parameter in the grid() 
plt.plot(x, y)
plt.grid(axis = 'x')
plt.show()

plt.plot(x, y)
plt.grid(axis = 'y')
plt.show()

#grid(color = 'color', linestyle = 'linestyle', linewidth = number).
plt.plot(x, y)
plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
plt.show()

#subplot()
plt.subplot(1, 2, 1)
plt.plot(x,y)
plt.show()

#title()
plt.subplot(1, 2, 2)
plt.plot(x,y)
plt.title("INCOME")
#plt.show()

#suptitle()
plt.suptitle("MY SHOP")
plt.show()