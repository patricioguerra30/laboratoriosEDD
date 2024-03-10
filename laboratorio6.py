def es_palindromo(palabra):
    cola = list(palabra)
    while len(cola) > 1:
        if cola.pop(0) != cola.pop():
            return False
    return True

print(es_palindromo('radar'))  
print(es_palindromo('laboratorio')) 

print(es_palindromo('radar'))  
print(es_palindromo('laboratorio')) 
#######################################################################
class SistemaPedidos:
    def __init__(self):
        self.cola_pedidos = []

    def agregar_pedido(self, pedido):
        self.cola_pedidos.append(pedido)

    def procesar_pedido(self):
        if len(self.cola_pedidos) == 0:
            print("No hay pedidos para procesar.")
        else:
            pedido_procesado = self.cola_pedidos.pop(0)
            print(f"El pedido {pedido_procesado} ha sido procesado.")

    def mostrar_estado(self):
        if len(self.cola_pedidos) == 0:
            print("No hay pedidos en la cola.")
        else:
            print(f"Pedidos en la cola: {self.cola_pedidos}")

sistema = SistemaPedidos()
sistema.agregar_pedido("Pedido 1")
sistema.agregar_pedido("Pedido 2")
sistema.mostrar_estado()
sistema.procesar_pedido()
sistema.mostrar_estado()
###########################################################################
def camino_minimo(laberinto, inicio, destino):
    filas, columnas = len(laberinto), len(laberinto[0])
    movimientos = [[-1 for _ in range(columnas)] for _ in range(filas)]
    movimientos[inicio[0]][inicio[1]] = 0

    cola = [inicio]

    while cola:
        x, y = cola.pop(0)

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy

            if nx >= 0 and ny >= 0 and nx < filas and ny < columnas:
                if laberinto[nx][ny] == 0 and movimientos[nx][ny] == -1:
                    movimientos[nx][ny] = movimientos[x][y] + 1
                    cola.append((nx, ny))

    return movimientos[destino[0]][destino[1]]

laberinto = [
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0],
    [1, 1, 1, 1, 0]
]
inicio = (0, 0)
destino = (4, 4)
print(camino_minimo(laberinto, inicio, destino))  
