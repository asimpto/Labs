import matplotlib.pyplot as plt
import numpy as np


# Задаем функцию
def f(x1, x2):
    return x1 * x2 - x1 ** 2 * x2 - 3


# Создаем массив значений x
x1, x2 = np.meshgrid(np.arange(0, 2, 0.01), np.arange(0, 1, 0.01))

z = f(x1, x2)

# fig = plt.figure()
# ax = fig.add_subplot(projection='3d')
# ax.plot_surface(x1, x2, z, cmap='inferno')
# plt.xlabel("x1")
# plt.ylabel("x2")
# ax.set_zlabel("z")


# Находим экстремумы (корни производной)
derivative = np.gradient(z)
extrema_indices = np.where(np.diff(np.sign(derivative)))[0]
extrema_x1 = x1[extrema_indices]
extrema_z = z[extrema_indices]
plt.plot(x1, z)


#Выводим экстремумы
for i, (ex, ey) in enumerate(zip(extrema_x1, extrema_z)):
    plt.plot([ex], [ey])
plt.show()

