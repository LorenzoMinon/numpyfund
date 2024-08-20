import numpy as np
from numpy import pi
import matplotlib.pyplot as plt

lista = [31,28,29,19]

arr = np.array(lista)

lista_2d= [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]

arr = np.array(lista_2d)

print(arr)

print(arr.shape)
print(arr.ndim)
print(arr.dtype)
print(arr.size)

#Cambiar tipos de datos:

arr = np.array(lista, dtype= np.int16)

print(arr.dtype)

#Crear matrices vacias 3x2

np.zeros((3,2))
print(np.zeros((3,2)))

print (np.ones((3,2)))

hola = np.empty((2,4)) #crea una matriz de 2x4 con valores aleatorios
print(np.empty((2,4)))
print(hola.dtype)

#Crear matrices con valores consecutivos
np.arange(10)
print(np.arange(10))

np.arange(10).reshape(2,5)
print(np.arange(10).reshape(2,5))

#Crear matrices con valores consecutivos
np.arange(10,21,2)
print(np.arange(10,21,2))

#Creare matrices con linspace
#Muy importante para graficar funciones

np.linspace(10,20,11)
print(np.linspace(10,20,50))

#Creemos un arreglo con 100 nros entre 0 y 2pi

rad = np.linspace(0,2*np.pi,100)
print(rad)

seno = np.sin(rad)
coseno = np.cos(rad)

plt.plot(seno,coseno)
plt.show()