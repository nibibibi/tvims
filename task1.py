values = []
with open("input1.txt", "r") as input_file:
    lines = input_file.readlines()
    for line in lines:
        values.extend([float(a) for a in line.split()])
print(values, '\n')
values.sort()
print(values, '\n')
m = {} 
for value in values:
    if value not in m:
        m[value] = 1
    else:
        m[value] = m[value] + 1
print(m, '\n')
p = []
for key in m:
    p.append(m[key]/100)
print(p, '\n')
F = []
for i, a in enumerate(p):
    if i == 0:
        F.append(a)
    else:
        F.append(round(F[i-1] + a, 2))
print(F, '\n')

import matplotlib.pyplot as plt

plt.plot([key for key in m], F)
plt.ylabel("F")
plt.xlabel("x")
plt.show()

