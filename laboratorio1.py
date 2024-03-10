
# def suma(a, b):
#     return a + b


# def resta(a, b):
#     return a - b


# def multiplicacion(a, b):
#     return a * b


# def division(a, b):
    
#     if b != 0:
#         return a / b
#     else:
#         return "No es posible dividir entre cero."

# a = int(input("Ingrese el primer número: "))
# b = int(input("Ingrese el segundo número: "))


# print(f"la Suma es: {suma(a, b)}")
# print(f"la Resta es: {resta(a, b)}")
# print(f"la Multiplicación es: {multiplicacion(a, b)}")
# print(f"la División es: {division(a, b)}")

###############################################
# def determinar_par_impar(numero):
#     if numero % 2 == 0:
#         return "El número es par"
#     else:
#         return "El número es impar"

# numero = int(input("Ingresa un número: "))
# resultado = determinar_par_impar(numero)
# print(resultado)

############################################
# def area(base, altura):
#     area = 0.5 * base * altura
#     return area

# base = int(input("Ingrese la base del triángulo: "))
# altura = int(input("Ingrese la altura del triángulo: "))

# area1= area(base, altura)

# print(f"El área del triángulo con base {base} y altura {altura} es: {area1}")
#############################################################################################

# def factorial(n):
#     if n==0:
#         resultado =  1
#     else :
#         resultado = n*factorial(n-1)
#     return resultado 
##################################################

# def es_primo(numero):
#     if numero < 2:
#         return False
#     if numero == 2:
#         return True
#     if numero % 2 == 0:
#         return False
#     i = 3
#     while i * i <= numero:
#         if numero % i == 0:
#             return False
#         i += 2 
#     return True


# numero = int(input("Ingrese un número para verificar si es primo: "))

# if es_primo(numero):
#     print(f"{numero} es un número primo.")
# else:
#     print(f"{numero} no es un número primo.")
####################################################################
# def invertir_cadena(cadena):
#     inversa = cadena[::-1]
#     return inversa

# cadena = input("Ingresa una cadena de texto: ")
# resultado = invertir_cadena(cadena)
# print(resultado)
####################################################
    

# inicio = int(input("Ingrese el número inicial del rango: "))
# fin = int(input("Ingrese el número final del rango: "))


# suma_pares = 0


# for numero in range(inicio, fin + 1):
#     if numero % 2 == 0:
#         suma_pares += numero

# print(f"La suma de los números pares en el rango [{inicio}, {fin}] es: {suma_pares}")

#################ejericicio 7#################################

# cadena = input("Ingrese una cadena de texto: ")


# num_vocales = 0


# vocales = "laboratorioestructura"


# for caracter in cadena:
#     if caracter in vocales:
#         num_vocales += 1

# print(f"El número de vocales en la cadena es: {num_vocales}")

##########################ejercicio 8 #######################3

# cuadrados = [numero ** 2 for numero in range(1, 11)]

# print(cuadrados)
########################ejericio 9#####################################
# lista = input("Ingrese una lista de números separados por espacios: ")

# numeros = [int(x) for x in lista.split()]

# numeros_ordenados = sorted(numeros)

# print("Lista ordenada de menor a mayor:", numeros_ordenados)

##########################ejercicios 10#####################
# def fibonacci(n):
#     if n <= 0:
#         return []
#     elif n == 1:
#         return [0]
#     elif n == 2:
#         return [0, 1]
#     else:
#         fib = [0, 1]
#         while len(fib) < n:
#             fib.append(fib[-1] + fib[-2])
#         return fib

# numeros_fibonacci = fibonacci(10)
# print(numeros_fibonacci)
############################ejercicio 13####################################
# numero = int(input("Ingresa un número para generar su tabla de multiplicar: "))

# print(f"Tabla de multiplicar del {numero}:")

# for i in range(1, 12):
#     resultado = numero * i
#     print(f"{numero} x {i} = {resultado}")


########################ejercicio 12###############################
# def es_palindromo(palabra):
#     palabra = palabra.lower()  
#     palabra = palabra.replace(" ", "")  

#     if palabra == palabra[::-1]:
#         return True
#     else:
#         return False

# palabra = input("Ingresa una palabra: ")
# if es_palindromo(palabra):
#     print("La palabra es un palíndromo")
# else:
    # print("La palabra no es un palíndromo")
##################################ejericio 14#############################333
import math

def calcular_area_circulo(radio):
    area = math.pi * radio**2
    return area

radio = float(input("Ingresa el radio del círculo: "))
area = calcular_area_circulo(radio)
print("El área del círculo es:", area)
#############################ejercicio 15###################################
# numero = input("Ingresa un número mayor de dos dígitos: ")

# if len(numero) < 2 or not numero.isdigit():
#     print("Por favor, ingresa un número válido mayor de dos dígitos.")
# else:
#     suma_digitos = sum(int(digito) for digito in numero)
#     print(f"La suma de los dígitos de {numero} es: {suma_digitos}")