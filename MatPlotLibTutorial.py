from matplotlib import pyplot as plt 
from matplotlib import style 



x = [5,6,7,8]
y = [7,3,8,3]

x2 = [4,3,2,9]
y2 = [6,7,2,6]

#plt.plot(x,y,'g',linewidth=5, label = 'Line One')
#plt.plot(x2,y2,'c',linewidth=10, label = 'Line Two')

#plt.scatter(x,y,color='g')
#plt.scatter(x2,y2,color='c')

plt.bar(x,y,color='g', align = 'center')
plt.bar(x2,y2,color='c',align = 'center')

plt.title('Epic Chart')
plt.ylabel('Y axis')
plt.xlabel('X axis')
plt.legend()

plt.grid(True, color='k')
plt.show()