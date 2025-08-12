import numpy as np

vector = np.array([1,2,3,4,5])
print(vector)

print(vector[2])
"""los vectores no son como las listas, no tiene un metodo end() para agregar elementos ,pero un metodo pop()
para rliminar elemento, perp si tienes metodo rehhape() para cambiar su forma, adicionalmente despues 
crear no se puede cambiar el tamaño del vector"""

vector1 = np.zeros(5)
print(vector1)
vector2 = np.ones(5)
print(vector2)
vector3 = np.arange(1,10)
print("rango",vector3)
vector4 = np.linspace(1,5,100)
print(vector4)
vector5 = np.random.rand(10)
print("ramdom" , vector5)
vector6 = np.random.randint(1,10,10)
print("randint", vector6)