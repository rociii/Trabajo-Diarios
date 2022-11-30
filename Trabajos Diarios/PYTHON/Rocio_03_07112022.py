# Cálculo con Matrices
import numpy as m
A= m.array([[2,3,1],[4,0,5]])
B= m.array([[0,4,3],[1,6,2]])
C= m.array([[1,2,3],[3,4,5],[6,7,8]])
print ("La Matriz A es:\n",A)
print ("La Matriz B es:\n",B)
suma = A+B
print("La suma de A+B es:\n", suma)
resta= A-B
print("La resta de A-B es:\n",resta)
productoEscalar= 3*A
print("El producto de 3*A es:\n",productoEscalar)
#Vamos a calcular el determinante
det= m.linalg.det(C)
print("El determinante de C es:\n",det)