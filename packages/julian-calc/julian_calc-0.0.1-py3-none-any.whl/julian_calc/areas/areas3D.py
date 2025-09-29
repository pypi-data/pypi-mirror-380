import math
"""Importa la librería math para usar PI en los cálculos 3D."""

class Areas3D:
    """Esta clase maneja el menú y los cálculos de áreas 3D."""

    def menu(self):
        """Muestra un menú generado dinámicamente y maneja la selección."""

        while True:
            print("\n--- Menú Áreas 3D ---")

            # 1. Obtenemos los nombres de los métodos (excluyendo a menu).
            metodos_figuras = [
                metodo for metodo in dir(self) 
                if not metodo.startswith('__') and metodo != 'menu'
            ]

            # 2. Mostramos los métodos como opciones.
            for i, nombre_figura in enumerate(metodos_figuras, 1):
                print(f"{i}. {nombre_figura.replace('_', ' ').capitalize()}")

            print("0. Volver al menú principal")

            opcion = input("Seleccione una opción: ")

            try:
                opcion_num = int(opcion)

                if opcion_num == 0:
                    print("Volviendo al menú principal...")
                    break

                # 3. Verificamos que la opción esté en el rango de figuras disponibles.
                if 0 < opcion_num <= len(metodos_figuras):
                    # 4. Llamamos dinámicamente al método con getattr().
                    nombre_metodo = metodos_figuras[opcion_num - 1]
                    metodo_a_llamar = getattr(self, nombre_metodo)
                    resultado = metodo_a_llamar()

                    if resultado is not None:
                        print(f"Resultado: El área superficial del {nombre_metodo.replace('_', ' ')} es {resultado:.2f}")
                else:
                    print("Opción no válida. Por favor, intente de nuevo.")

            except ValueError:
                print("Error: Debe ingresar un número.")

    def area_cubo(self):
        """Pide datos y calcula el área superficial de un cubo."""
        try:
            lado = float(input("Ingrese el lado del cubo: "))
            if lado < 0:
                print("Error: El lado no puede ser negativo.")
                return None
            return 6 * (lado ** 2)
        except ValueError:
            print("Error: Entrada inválida. Debe ingresar un valor numérico.")
            return None

    def area_esfera(self):
        """Pide datos y calcula el área superficial de una esfera."""
        try:
            radio = float(input("Ingrese el radio de la esfera: "))
            if radio < 0:
                print("Error: El radio no puede ser negativo.")
                return None
            return 4 * math.pi * (radio ** 2)
        except ValueError:
            print("Error: Entrada inválida. Debe ingresar un valor numérico.")
            return None

    def area_cilindro(self):
        """Pide datos y calcula el área superficial de un cilindro."""
        try:
            radio = float(input("Ingrese el radio de la base del cilindro: "))
            altura = float(input("Ingrese la altura del cilindro: "))
            if radio < 0 or altura < 0:
                print("Error: Las dimensiones no pueden ser negativas.")
                return None
            return 2 * math.pi * radio * (radio + altura)
        except ValueError:
            print("Error: Entrada inválida. Debe ingresar valores numéricos.")
            return None
    def area_prisma_rectangular(self):
        try:
            l = float(input("Largo: "))
            w = float(input("Ancho: "))
            h = float(input("Altura: "))
            if l < 0 or w < 0 or h < 0:
                print("Error: Dimensiones negativas no válidas.")
                return None
            return 2 * (l*w + l*h + w*h)
        except ValueError:
            print("Error: Entrada inválida.")
            return None

    def area_cono(self):
        try:
            r = float(input("Radio: "))
            h = float(input("Altura: "))
            if r < 0 or h < 0:
                print("Error: Dimensiones negativas no válidas.")
                return None
            g = math.sqrt(r**2 + h**2)
            return math.pi * r * (r + g)
        except ValueError:
            print("Error: Entrada inválida.")
            return None

    def area_tetraedro(self):
        try:
            a = float(input("Arista: "))
            if a < 0:
                print("Error: La arista no puede ser negativa.")
                return None
            return math.sqrt(3) * a**2
        except ValueError:
            print("Error: Entrada inválida.")
            return None

    def area_octaedro(self):
        try:
            a = float(input("Arista: "))
            if a < 0:
                print("Error: La arista no puede ser negativa.")
                return None
            return 2 * math.sqrt(3) * a**2
        except ValueError:
            print("Error: Entrada inválida.")
            return None

    def area_dodecaedro(self):
        try:
            a = float(input("Arista: "))
            if a < 0:
                print("Error: La arista no puede ser negativa.")
                return None
            return 3 * math.sqrt(25 + 10*math.sqrt(5)) * a**2
        except ValueError:
            print("Error: Entrada inválida.")
            return None

    def area_icosaedro(self):
        try:
            a = float(input("Arista: "))
            if a < 0:
                print("Error: La arista no puede ser negativa.")
                return None
            return 5 * math.sqrt(3) * a**2
        except ValueError:
            print("Error: Entrada inválida.")
            return None

    def area_prisma_triangular(self):
        try:
            a = float(input("Arista del triángulo: "))
            h = float(input("Altura del prisma: "))
            if a < 0 or h < 0:
                print("Error: Dimensiones negativas no válidas.")
                return None
            area_base = (math.sqrt(3)/4) * a**2
            perimetro = 3*a
            return 2*area_base + perimetro*h
        except ValueError:
            print("Error: Entrada inválida.")
            return None

    def area_prisma_hexagonal(self):
        try:
            a = float(input("Arista del hexágono: "))
            h = float(input("Altura del prisma: "))
            if a < 0 or h < 0:
                print("Error: Dimensiones negativas no válidas.")
                return None
            area_base = (3*math.sqrt(3)/2) * a**2
            perimetro = 6*a
            return 2*area_base + perimetro*h
        except ValueError:
            print("Error: Entrada inválida.")
            return None

    def area_piramide_cuadrada(self):
        try:
            l = float(input("Lado de la base: "))
            g = float(input("Apotema: "))
            if l < 0 or g < 0:
                print("Error: Dimensiones negativas no válidas.")
                return None
            return l**2 + 2*l*g
        except ValueError:
            print("Error: Entrada inválida.")
            return None

    def area_tronco_cono(self):
        try:
            r1 = float(input("Radio mayor: "))
            r2 = float(input("Radio menor: "))
            h = float(input("Altura: "))
            if r1 < 0 or r2 < 0 or h < 0:
                print("Error: Dimensiones negativas no válidas.")
                return None
            g = math.sqrt((r1-r2)**2 + h**2)
            return math.pi*(r1+r2)*g + math.pi*(r1**2 + r2**2)
        except ValueError:
            print("Error: Entrada inválida.")
            return None

    def area_toro(self):
        try:
            R = float(input("Radio mayor (centro al círculo): "))
            r = float(input("Radio menor (círculo): "))
            if R < 0 or r < 0:
                print("Error: Dimensiones negativas no válidas.")
                return None
            return 4*math.pi**2 * R * r
        except ValueError:
            print("Error: Entrada inválida.")
            return None


if __name__ == "__main__":
    """Bloque para test: solo se ejecuta si corres el archivo directamente."""
    calculador_areas3D = Areas3D()
    calculador_areas3D.menu()
