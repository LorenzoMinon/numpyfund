import numpy as np
import matplotlib.pyplot as plt

a = np.linspace(10,50,30)
b = np.linspace(1,5,30)

c = a+b

print(a)
print(b)
print(c)

#rg random, el generador aleatorio

rg = np.random.default_rng(2)

aleatorio = rg.random(1000)

print(aleatorio)

# plt.hist(aleatorio, bins=100)
# plt.show()

#usar rg.normal para generar 10000 valores aleaotrios que sigan una distribucion normal

normal = rg.normal(10,5,100000) #Con una media de 10, desviacion de 5 me genere 10000 valores

print(normal)

plt.hist(normal, bins=1000)
plt.show()

enteros = rg.integers(20,size = 2000)
# print(enteros)

# plt.hist(enteros)
# plt.show()

#Usar rg.choice para elegir valores aleatorios de un arreglo

rg.choice(26,size = 10, replace = False)
print(rg.choice(26,size = 10, replace = False))