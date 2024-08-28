#Построй диаграмму рассеяния для двух наборов случайных данных,
#сгенерированных с помощью функции `numpy.random.rand`.


import matplotlib.pyplot as plt
import numpy as np

x = np.random.rand(5)  # массив из 5 случайных чисел
y = np.random.rand(5)





plt.title('Диаграмма рассеяния')
plt.xlabel('ось x')
plt.ylabel('ось y')

plt.scatter(x, y)
plt.show()