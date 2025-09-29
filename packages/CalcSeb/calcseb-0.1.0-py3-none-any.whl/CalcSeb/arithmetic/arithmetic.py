class Aritmetica:
    def __init__(self):
        self.ultimo_resultado = 0  # guarda el último valor calculado

    def sumar(self, a, b):
        self.ultimo_resultado = a + b
        return self.ultimo_resultado

    def restar(self, a, b):
        self.ultimo_resultado = a - b
        return self.ultimo_resultado

    def multiplicar(self, a, b):
        self.ultimo_resultado = a * b
        return self.ultimo_resultado

    def dividir(self, a, b):
        if b != 0:
            self.ultimo_resultado = a / b
            return self.ultimo_resultado
        else:
            return "Error: división entre cero"

    def mostrar_menu(self):
        while True:
            print("\n--- Módulo Aritmética ---")
            print("1. Sumar")
            print("2. Restar")
            print("3. Multiplicar")
            print("4. Dividir")
            print("5. Mostrar último resultado")
            print("0. Volver al menú principal")

            opcion = input("Elige una opción: ")

            if opcion == "0":
                break
            elif opcion == "5":
                print(f"Último resultado: {self.ultimo_resultado}")
            elif opcion in ["1", "2", "3", "4"]:
                try:
                    num1 = float(input("Ingresa el primer número: "))
                    num2 = float(input("Ingresa el segundo número: "))

                    if opcion == "1":
                        print(f"Resultado: {self.sumar(num1, num2)}")
                    elif opcion == "2":
                        print(f"Resultado: {self.restar(num1, num2)}")
                    elif opcion == "3":
                        print(f"Resultado: {self.multiplicar(num1, num2)}")
                    elif opcion == "4":
                        print(f"Resultado: {self.dividir(num1, num2)}")

                except ValueError:
                    print("Error: Debes ingresar números válidos.")
            else:
                print("Opción no válida. Intenta de nuevo.")
