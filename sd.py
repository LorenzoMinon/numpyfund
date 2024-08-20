import numpy as np
import matplotlib.pyplot as plt

rg = np.random.default_rng(2)

enteros = rg.integers(20,size =(10))

enteros[0:6]
# print(enteros[0:6:2])

enteros[::2]
# print(enteros[::2])

#Ejercicio 22

enteros_2d = rg.integers(20,size=(8,5))
print(enteros_2d)
#Cuarto valor del segundo array
print(enteros_2d[1,3])

#Segundo valor de los arrays con indice 3,4,5
print(enteros_2d[3:6,1]) #Del 3 al 5, el segundo valor 0, 1!

#Seleccionar los 2 primeros valores de los arrays con indice 4,5,6
print(enteros_2d[4:7,:2])