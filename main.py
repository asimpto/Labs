import numpy as np
import time
from scipy.optimize import minimize


# Целевая функция
def task_func(x):
    return x[0] ** 2 + x[1] ** 2


# Градиент целевой функции
def gradient(x):
    return np.array([2 * x[0], 2 * x[1]])


# Ограничения
def cons1(x):
    return -(2 * x[0] + x[1] - 2)


def cons2(x):
    return -(-x[1] + 1)


# Проекция на область допустимых значений
def proj(x):
    if cons1(x) < 0:
        # Проекция на -2 * x[0] - x[1] + 2 >= 0
        a, b, c = -2, -1, 2
        x = x - ((a * x[0] + b * x[1] - c) / (a ** 2 + b ** 2)) * np.array([a, b])
    if cons2(x) < 0:
        # Проекция на x[1] >= 1
        x[1] = max(x[1], 1)
    return x


# Параметры градиентного спуска
a = 0.01  # шаг градиентного спуска
eps = 1e-6  # допустимая погрешность
max_iter = 1000  # максимальное количество итераций

# Начальная точка
x = np.array([2.0, 6.0])
x0 = x

# Таймер работы градиентного спуска
start_timer_grad = time.perf_counter()

# Градиентный спуск
for i in range(max_iter):
    new_x = proj(x - a * gradient(x))

    if np.linalg.norm(new_x - x) < eps:
        break

    x = new_x

end_timer_grad = time.perf_counter()

# Scipy.minimize

cons = [{'type': 'ineq', 'fun': cons1},
        {'type': 'ineq', 'fun': cons2}]

start_timer_scipy = time.perf_counter()

result_scipy = minimize(task_func, x0, constraints=cons)

end_timer_scipy = time.perf_counter()

# Вывод результатов
print("Градиент\n", "Корень:", x)
print(" Значение целевой функции:", task_func(x), "\n")

print("Scipy\n", "Корень:", result_scipy.x)
print(" Значение целевой функции:", result_scipy.fun, "\n")

print("Погрешность:", abs(result_scipy.fun - task_func(x)))
print("Время работы градиентного спуска:", round(end_timer_grad - start_timer_grad, 5), "секунд")
print("Время работы библиотеки scipy:", round(end_timer_scipy - start_timer_scipy, 5), "секунд")