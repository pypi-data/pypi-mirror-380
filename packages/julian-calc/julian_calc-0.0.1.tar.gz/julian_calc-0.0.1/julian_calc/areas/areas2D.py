import math
"""Importa la librería math para usar PI en el cálculo del círculo."""

class Areas2D:
    """Esta clase maneja el menú y los cálculos de áreas 2D."""
    
    def menu(self):
        """Muestra un menú generado dinámicamente y maneja la selección."""
        
        while True:
            print("\n--- Menú Áreas 2D ---")
            
            """
            1. Se obtiene los nombres de los metodos (excluyendo a menu).
            """
            metodos_figuras = [
                metodo for metodo in dir(self) 
                if not metodo.startswith('__') and metodo != 'menu'
            ]
            
            """2. Se muestran los metodos como opciones."""
            for i, nombre_figura in enumerate(metodos_figuras, 1):
                print(f"{i}. {nombre_figura.capitalize()}")
            
            print("0. Volver al menú principal")

            opcion = input("Seleccione una opción: ")

            try:
                opcion_num = int(opcion)

                if opcion_num == 0:
                    print("Volviendo al menú principal...")
                    break
                
                """3. Verificamos que la opción esté en el rango de figuras disponibles."""
                if 0 < opcion_num <= len(metodos_figuras):
                    """
                    Parte Dinámica: Llamar al Método
                    4. Obtenemos el nombre del método, lo traemos con getattr() y lo llamamos.
                    """
                    nombre_metodo = metodos_figuras[opcion_num - 1]
                    metodo_a_llamar = getattr(self, nombre_metodo)
                    resultado = metodo_a_llamar()
                    
                    if resultado is not None:
                        print(f"Resultado: El área del {nombre_metodo} es {resultado:.2f}")
                else:
                    print("Opción no válida. Por favor, intente de nuevo.")

            except ValueError:
                """Maneja el error si el usuario no ingresa un número."""
                print("Error: Debe ingresar un número.")

    def rectangulo(self):
        """Pide datos y calcula el área de un rectángulo."""
        try:
            base = float(input("Ingrese la base: "))
            altura = float(input("Ingrese la altura: "))
            if base < 0 or altura < 0:
                print("Error: Las dimensiones no pueden ser negativas.")
                return None
            return base * altura
        except ValueError:
            print("Error: Entrada inválida. Debe ingresar valores numéricos.")
            return None
    
    def triangulo(self):
        """Pide datos y calcula el área de un triángulo."""
        try:
            base = float(input("Ingrese la base: "))
            altura = float(input("Ingrese la altura: "))
            if base < 0 or altura < 0:
                print("Error: Las dimensiones no pueden ser negativas.")
                return None
            return (base * altura) / 2
        except ValueError:
            print("Error: Entrada inválida. Debe ingresar valores numéricos.")
            return None

    def circulo(self):
        """Pide datos y calcula el área de un círculo."""
        try:
            radio = float(input("Ingrese el radio: "))
            if radio < 0:
                print("Error: El radio no puede ser negativo.")
                return None
            return math.pi * (radio ** 2)
        except ValueError:
            print("Error: Entrada inválida. Debe ingresar un valor numérico.")
            return None

    def rombo(self):
        """Pide datos y calcula el área de un rombo."""
        try:
            d_mayor = float(input("Ingrese la diagonal mayor: "))
            d_menor = float(input("Ingrese la diagonal menor: "))
            if d_mayor < 0 or d_menor < 0:
                print("Error: Las diagonales no pueden ser negativas.")
                return None
            return (d_mayor * d_menor) / 2
        except ValueError:
            print("Error: Entrada inválida. Debe ingresar valores numéricos.")
            return None

    def trapecio(self):
        """Pide datos y calcula el área de un trapecio."""
        try:
            b_mayor = float(input("Ingrese la base mayor: "))
            b_menor = float(input("Ingrese la base menor: "))
            altura = float(input("Ingrese la altura: "))
            if b_mayor < 0 or b_menor < 0 or altura < 0:
                print("Error: Las dimensiones no pueden ser negativas.")
                return None
            return ((b_mayor + b_menor) / 2) * altura
        except ValueError:
            print("Error: Entrada inválida. Debe ingresar valores numéricos.")
            return None

    def cuadrado(self):
        """Pide datos y calcula el área de un cuadrado."""
        try:
            lado = float(input("Ingrese la longitud del lado: "))
            if lado < 0:
                print("Error: El lado no puede ser negativo.")
                return None
            return lado ** 2
        except ValueError:
            print("Error: Entrada inválida. Debe ingresar un valor numérico.")
            return None

if __name__ == "__main__":
    """
    Bloque para test. 
    Solo se ejecuta si se corre el archivo independientemente.
    """
    calculador_areas = Areas2D()
    calculador_areas.menu()
