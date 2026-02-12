class GestorEstructuras:
    def __init__(self):
        # 1a. Declaración e inicialización de lista unidimensional (Tamaño 5)
        self.unidimensional = [10, 20, 30, 40, 50]
        
        # 1b. Declaración e inicialización de lista bidimensional (3x3)
        self.bidimensional = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]

    def mostrar_ejercicio_2(self):
        print("--- Ejercicio 2: Acceso ---")
        # 2a. Segundo elemento (índice 1)
        print(f"Segundo elemento unidimensional: {self.unidimensional[1]}")
        
        # 2b. Segunda fila, segunda columna (índice [1][1])
        valor_2b = self.bidimensional[1][1]
        print(f"Elemento en [2][2] de la matriz: {valor_2b}\n")

    def ejecutar_ejercicio_3(self):
        print("--- Ejercicio 3: Inserción y Eliminación ---")
        # 3a. Insertar en la posición 3 (índice 3)
        self.unidimensional.insert(3, "Estructura de datos")
        print(f"Lista unidimensional tras inserción: {self.unidimensional}")
        
        # 3b. Eliminar elemento 3ra fila, 3ra columna (índice [2][2])
        # Usamos 'del' para eliminar por índice
        del self.bidimensional[2][2]
        print(f"Matriz tras eliminar elemento en [3][3]: {self.bidimensional}\n")

    def ejecutar_ejercicio_4(self):
        print("--- Ejercicio 4: Búsqueda ---")
        # 4a. Buscar índice de "Estructura de datos"
        try:
            indice_4a = self.unidimensional.index("Estructura de datos")
            print(f"Índice de 'Estructura de datos': {indice_4a}")
        except ValueError:
            print("El valor no se encuentra en la lista.")

        # 4b. Buscar valor en la segunda fila (índice 1)
        # Buscaremos el valor 5, que sabemos que está allí
        valor_a_buscar = 5
        segunda_fila = self.bidimensional[1]
        try:
            indice_4b = segunda_fila.index(valor_a_buscar)
            print(f"Índice del valor {valor_a_buscar} en la segunda fila: {indice_4b}")
        except ValueError:
            print(f"El valor {valor_a_buscar} no existe en la segunda fila.")

# --- Ejecución del Programa ---
if __name__ == "__main__":
    # Instanciamos la clase
    taller = GestorEstructuras()
    
    # Ejecutamos los puntos del taller
    taller.mostrar_ejercicio_2()
    taller.ejecutar_ejercicio_3()
    taller.ejecutar_ejercicio_4()