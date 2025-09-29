from .arithmetic.arithmetic import Aritmetica
from .areas.areas import Areas
from .trigonometry.trig import CalculadoraTrigonometrica
from .coolstuff import FrasesDesarrollador

def main():
    while True:
        print("\n=== Calculadora ===")
        print("1. Aritmética")
        print("2. Áreas")
        print("3. Trigonometría")
        print("0. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            Aritmetica().mostrar_menu()
        elif opcion == "2":
            Areas().mostrar_menu()
        elif opcion == "3":
            CalculadoraTrigonometrica().mostrar_menu()
        elif opcion == "0":
            print(FrasesDesarrollador().mostrar_frase())
            break
            
        else:
            print("Opción no válida.")  

if __name__ == "__main__":
    main()