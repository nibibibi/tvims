# Прочитать выборку из файла
values = []
with open("input1.txt", "r") as input_file:
    lines = input_file.readlines()
    for line in lines:
        values.extend([float(a) for a in line.split()])
n = len(values)

# Вариационный ряд
values.sort()
print("Вариационный ряд: \n", values, '\n')

# Частота каждого уникального значения в выборке 
m = {} 
for value in values:
    if value not in m:
        m[value] = 1
    else:
        m[value] = m[value] + 1
print("Частота каждого значения: \n", m, '\n')

# p для каждого значения
p = []
for key in m:
    p.append(m[key]/n)
print("p:", p, '\n')

# Fi для xi
F = []
for i, a in enumerate(p):
    if i == 0:
        F.append(a)
    else:
        F.append(round(F[i-1] + a, 4))
print("Fi:\n", F, '\n')

import matplotlib.pyplot as plt
# График Fi
plt.plot([key for key in m], F)
plt.ylabel("F")
plt.xlabel("x")
# plt.show()

import math
# Число интервалов
M = round(math.sqrt(n))
# Длина интервала
h = (values[-1] - values[0]) / M
print("h = ", h, '\n')
# Левые границы интервалов
Ai = [round(values[0] + h*i, 4) for i in range(M)]
print("Ai: ", Ai)
# Правые границы интервалов
Bi = [round(values[0] + h*(i+1), 4) for i in range(M)]
print("Bi: ", Bi)
# Количество точек  на интервалах
mi = [0 for _ in range(M)]
mi[0] = 1
mi[-1] = 1
for i, a in enumerate(mi):
	for value in values:
		if value > Ai[i] and value < Bi[i]:
			mi[i] += 1
		elif value == Bi[i] and i != M-1:
			mi[i] += 0.5
			mi[i+1] += 0.5
print("mi: ", mi)
# Статистическая плотность интервалов
fi = [round(a/(h*n), 4) for a in mi]
print(fi)

fig, ax = plt.subplots()
ax.bar(Ai, fi)
# plt.show()

intervals = [values[M*i: M*i+M] for i in range(M)]
print("intervals: ", intervals)
for i, interval in enumerate(intervals):
	if i == 0:
		Ai[0] = interval[0]
	else:
		if interval[0] == intervals[i-1][-1]:
			Ai[i] = interval[0]
			Bi[i-1] = interval[0]
		else:
			Ai[i] = round((interval[0] + intervals[i-1][-1]) / 2, 4)
			Bi[i-1] = round((interval[0] + intervals[i-1][-1]) / 2, 4)
	if i == M-1:
		Bi[-1] = interval[-1]
print("Ai: ", Ai)
print("Bi: ", Bi)
h = [round(Bi[i] - Ai[i], 4) for i in range(M)]
print("hi: ", h)
fi = [round(len(intervals[i]) / (h[i]*n), 4) for i in range(M)]
print("fi: ", fi)

# Матожидание
mx = round(sum(values) / n, 4)
print("mx: ", mx)
# Оценка дисперсии
SxS = round(sum([(value - mx)*(value - mx) for value in values])/(n-1), 4)
print("S^2: ", SxS)
S = round(math.sqrt(SxS), 4)
print("S: ", S)