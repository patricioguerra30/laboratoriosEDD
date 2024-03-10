class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def buscar_nodo(self, valor):
        actual = self.cabeza
        while actual is not None:
            if actual.dato == valor:
                return actual
            actual = actual.siguiente
        return None

lista = ListaEnlazada()
nodo1 = Nodo(12)
nodo2 = Nodo(23)
nodo3 = Nodo(34)

lista.cabeza = nodo1
nodo1.siguiente = nodo2
nodo2.siguiente = nodo3
 
nodo_buscado = lista.buscar_nodo(14)
if nodo_buscado:
    print("Se encontró el nodo con valor", nodo_buscado.dato)
else:
    print("No se encontró el nodo con el valor especificado")
    
###################################################################3#####33

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def sumar_nodos(self):
        suma = 0
        actual = self.cabeza
        while actual is not None:
            suma += actual.dato
            actual = actual.siguiente
        return suma

lista = ListaEnlazada()
nodo1 = Nodo(12)
nodo2 = Nodo(23)
nodo3 = Nodo(34)

lista.cabeza = nodo1
nodo1.siguiente = nodo2
nodo2.siguiente = nodo3

resultado = lista.sumar_nodos()
print("La suma de los nodos en la lista es:", resultado)

#############################################################################

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def longitud(self):
        contador = 0
        actual = self.cabeza
        while actual is not None:
            contador += 1
            actual = actual.siguiente
        return contador

lista = ListaEnlazada()
nodo1 = Nodo(12)
nodo2 = Nodo(23)
nodo3 = Nodo(34)

lista.cabeza = nodo1
nodo1.siguiente = nodo2
nodo2.siguiente = nodo3

longitud = lista.longitud()
print("La longitud de la lista es:", longitud)

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

#######################################################################
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar_al_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            return
        actual = self.cabeza
        while actual.siguiente is not None:
            actual = actual.siguiente
        actual.siguiente = nuevo_nodo

    def concatenar(self, otra_lista):
        if self.cabeza is None:
            self.cabeza = otra_lista.cabeza
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = otra_lista.cabeza

lista1 = ListaEnlazada()
lista1.agregar_al_final(12)
lista1.agregar_al_final(23)

lista2 = ListaEnlazada()
lista2.agregar_al_final(34)
lista2.agregar_al_final(45)

lista1.concatenar(lista2)

actual = lista1.cabeza
while actual is not None:
    print(actual.dato, end=" ; ")
    actual = actual.siguiente
print("None")

##################################################################

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar_al_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            return
        actual = self.cabeza
        while actual.siguiente is not None:
            actual = actual.siguiente
        actual.siguiente = nuevo_nodo

    def eliminar_duplicados(self):
        if self.cabeza is None:
            return

        valores = set()
        anterior = None
        actual = self.cabeza

        while actual is not None:
            if actual.dato in valores:
                anterior.siguiente = actual.siguiente
            else:
                valores.add(actual.dato)
                anterior = actual
            actual = actual.siguiente

lista = ListaEnlazada()
lista.agregar_al_final(12)
lista.agregar_al_final(23)
lista.agregar_al_final(12)
lista.agregar_al_final(23)
lista.agregar_al_final(34)

print("Lista original:")
actual = lista.cabeza
while actual is not None:
    print(actual.dato, end=" ; ")
    actual = actual.siguiente
print("None")

lista.eliminar_duplicados()

print("Lista sin duplicados:")
actual = lista.cabeza
while actual is not None:
    print(actual.dato, end=" ; ")
    actual = actual.siguiente
print("None")