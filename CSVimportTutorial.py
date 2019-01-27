from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np

style.use('ggplot')

x,y = np.loadtxt('example.csv', unpack = True, delimiter = ',')

plt.plot(x,y)

plt.title('Epic Chart')
plt.ylabel('Y label')
plt.xlabel('X label')

plt.show()