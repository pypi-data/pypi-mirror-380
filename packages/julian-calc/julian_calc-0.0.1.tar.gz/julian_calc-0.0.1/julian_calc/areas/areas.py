from .areas2D import Areas2D
from .areas3D import Areas3D
from .IrrAreas import InterfazPoligonoIrregular

" Clase principal de los cálculos de Áreas"

class Areas:
    def mostrar_menu(self):
        while True:
            print("\n--- Menú de Áreas ---")
            print("1. Áreas 2D")
            print("2. Áreas 3D")
            print("3. Crea tu figura")
            print("0. Volver al menú principal")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                Areas2D().menu()
            elif opcion == "2":
                Areas3D().menu()
            elif opcion == "3":
                InterfazPoligonoIrregular.ejecutar()
            elif opcion == "0":
                break
            else:
                print("Opción no válida.")

if __name__ == "__main__":
    Area  = Areas()
    Area.mostrar_menu()