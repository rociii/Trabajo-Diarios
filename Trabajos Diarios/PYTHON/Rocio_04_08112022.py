# Cálculo con Matrices
import numpy as m
A= m.array([[2,5],[4,-3]])
B= m.array([[1,0],[-3,2]])
C= m.array([[2,-5],[1,0]])
D=m.array([[1,2],[-3,-1]])
print ("La Matriz A es:\n",A)
print ("La Matriz B es:\n",B)
print ("La Matriz C es:\n",C)
print("La Matriz D es:\n",D)
suma = A+B
suma1=C+D
print("La suma de A+B es:\n", suma)
print("La suma de C+D es:\n", suma1)
resta= A-B
resta1=C-D
print("La resta de A-B es:\n",resta)
print("La resta de C-D es:\n",resta1)
multi=m.dot(C,D)
multi1=m.dot(A,B)
print("\n El producto de C*D es:\n",multi)
print("\n El producto de A*B es:\n",multi1)
productoEscalar = 3*A
print("\nEl producto 3*A es: \n",productoEscalar)
#Vamos a calcular el determinante
det= m.linalg.det(A)
det= m.linalg.det(D)
print("El determinante de A es:\n",int(det))
print("El determinante de D es:\n",int(det))
#Vamos a calcular la matriz inversa.
import numpy as m
 
Matriz = m.array([[-1,0,1],[1,-1,0],[1,1,0]])
MatrizInversa = m.linalg.inv(Matriz)
MatrizTraspuesta = m.transpose(Matriz)
 
print("La Matriz Inversa es: \n",MatrizInversa)
print("La Matriz Traspuesta es: \n",MatrizTraspuesta)

