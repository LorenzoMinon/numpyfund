import numpy as np
import matplotlib.pyplot as plt

rg = np.random.default_rng(2)
rg.choice(26,size = 10, replace = False)


estadisticos = rg.integers(20, size = 8)
print(estadisticos)

estadisticos.min()
# print(estadisticos.min())

estadisticos.max() #Maximo
estadisticos.mean() #Promedio
estadisticos.std() #Desviacion estandar
estadisticos.var() #Varianza
estadisticos.sum() #Suma
estadisticos.prod() #Producto
estadisticos.cumsum() #
estadisticos.cumprod() #

print(estadisticos.mean())

#Array de 2 dimensiones, 5 filas y 4 columnas
estadisticos_2d = rg.integers(20, size = (5,4))

print(estadisticos_2d)


estadisticos_2d.min(axis=0) #A lo largo de los columnas.
print(estadisticos_2d.min(axis=0))

estadisticos_2d < 10
print(estadisticos_2d < 10)

estadisticos_2d[estadisticos_2d < 10]
print(estadisticos_2d[estadisticos_2d < 10])

#Generar 2 arreglos de 3x3
np1 = rg.integers(20, size = (3,3))
np2 = rg.integers(20, size = (3,3))

#np.vstack para unirlos verticalmente

np.vstack((np1,np2))
print(np.vstack((np1,np2)))
print(np.hstack((np1,np2))) #np.hstack para unirlos horizontalmente


