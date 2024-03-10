# def imprimir_pares(numero):
#     if numero <= 100:
#         if numero % 2 == 0:
#             print(numero)
#         imprimir_pares(numero + 2)

# imprimir_pares(2)

#########################################

# def suma_recursiva(n):
#     if n == 1:
#         return 1
#     else:
#         suma = n + suma_recursiva(n - 1)
#         print(f"Suma hasta {n}: {suma}")
#         return suma


# n = int(input("ingrese el numero limite: "))
# resultado = suma_recursiva(n)
# print(f"La suma total de los números del 1 al {n} es: {resultado}")

######################################

# def piramide_recursiva(n,i=1):
#     if i<=n:
#         separar=" " *(n-i)
#         fila =" ".join(str(j) for j in range(1,i+1))
#         print(separar+fila+separar)
#         piramide_recursiva(n,i+1)
# def main():
#     altura=int(input("ingrese la altura de la piramide: "))
#     piramide_recursiva(altura)
# if __name__=="__main__":
#     main()

######################################################
# def piramide_invertida(n, espacios=0):
#     if n > 0:
#         print(" " * espacios, end="")
#         for i in range(n, 0, -1):
#             print(i, end=" ")
#         print()
#         piramide_invertida(n - 1, espacios + 1)
# numero_filas = 5
# piramide_invertida(numero_filas)

################################################################
    
# def tabla_de_multiplicar(n,i=1):
#     if i <= 12:
#         multiplicacion=(i*n)
#         print(f"{n} x {i} = {multiplicacion}")
#         tabla_de_multiplicar(n,i+1)

# tabla_de_multiplicar(5)

##############################################################
import numpy as np
# matriz_real=np.array([
#                        [1.0, 2.9, 3.4],
#                       [5.4, 8.8, 19.4],
#                       [3.3, 4.6, 13.7]
# ])
# print(matriz_real)

##################################################################

# matriz_compleja = ([
#     [2 + 3j, -1 - 2j, 4 + 1j],
#     [0, 5j, -3 - 4j],
#     [1 - 2j, 7, -6j]
# ])
# for fila in matriz_compleja:
#     for elemento in fila:
#         print(elemento, end="\t")
#     print()

################################################################

matriz_de_matrices = np.array([
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
    [[19, 20, 21], [22, 23, 24], [25, 26, 27]]
])
# for matriz in matriz_de_matrices:
#     for fila in matriz:
#         for elemento in fila:
#             print(elemento, end="\t")
#         print()
print(matriz_de_matrices)
################################################################3
    
def obtener_elemento_central(matriz):
    filas = len(matriz)
    columnas = len(matriz[0]) if filas > 0 else 0

    if filas > 0 and columnas > 0:
        fila_central = filas // 2
        columna_central = columnas // 2
        elemento_central = matriz[fila_central][columna_central]
        return elemento_central
    else:
        return None 
matriz = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])


elemento_central = obtener_elemento_central(matriz)
print(matriz)
print("Elemento central de la matriz:", elemento_central)
###########################################################################

