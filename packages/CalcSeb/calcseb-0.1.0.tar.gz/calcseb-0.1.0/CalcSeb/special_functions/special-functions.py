import math

class SpecialFunctions:
    """
    Clase: SpecialFunctions
    Contiene métodos para cálculos logarítmicos,
    exponenciales y de potencias.
    """

    # ========================
    # Métodos Logarítmicos
    # ========================

    def log_base_e(self, x: float) -> float:
        """
        Calcula el logaritmo natural (base e).  
        """
        if x <= 0:
            raise ValueError("El logaritmo natural no está definido para valores <= 0.")
        return math.log(x)

    def log_base_10(self, x: float) -> float:
        """
        Calcula el logaritmo en base 10.
        """
        if x <= 0:
            raise ValueError("El logaritmo base 10 no está definido para valores <= 0.")
        return math.log10(x)

    def log_base(self, x: float, base: float) -> float:
        """
        Calcula el logaritmo en una base arbitraria.
        """
        if x <= 0:
            raise ValueError("El logaritmo no está definido para valores <= 0.")
        if base <= 0 or base == 1:
            raise ValueError("La base del logaritmo debe ser positiva y distinta de 1.")
        return math.log(x, base)

    # ========================
    # Métodos Exponenciales
    # ========================

    def exp_e(self, x: float) -> float:
        """
        Calcula e^x.
        """
        return math.exp(x)

    def exp_base(self, base: float, x: float) -> float:
        """
        Calcula base^x.
        """
        return math.pow(base, x)

    # ========================
    # Métodos Potenciales
    # ========================

    def power(self, base: float, exponent: float) -> float:
        """
        Calcula base elevado a la potencia exponent.
        """
        return math.pow(base, exponent)

    def sqrt(self, x: float) -> float:
        """
        Calcula la raíz cuadrada.
        """
        if x < 0:
            raise ValueError("La raíz cuadrada no está definida para números negativos en R.")
        return math.sqrt(x)

def run_menu():
    """
    Función principal para ejecutar el menú interactivo.
    """
    calculator = SpecialFunctions()

    while True:
        print("\n--- Menú de Funciones Especiales ---")
        print("1. Logaritmo natural (base e)")
        print("2. Logaritmo base 10")
        print("3. Logaritmo en base arbitraria")
        print("4. Exponencial e^x")
        print("5. Exponencial base^x")
        print("6. Potencia base^exponente")
        print("7. Raíz cuadrada")
        print("8. Salir")
        
        choice = input("Selecciona una opción (1-8): ")
        
        if choice == '1':
            try:
                x = float(input("Ingresa el valor de x: "))
                result = calculator.log_base_e(x)
                print(f"Resultado: ln({x}) = {result}")
            except ValueError as e:
                print(f"Error: {e}")
        
        elif choice == '2':
            try:
                x = float(input("Ingresa el valor de x: "))
                result = calculator.log_base_10(x)
                print(f"Resultado: log10({x}) = {result}")
            except ValueError as e:
                print(f"Error: {e}")
        
        elif choice == '3':
            try:
                x = float(input("Ingresa el valor de x: "))
                base = float(input("Ingresa la base: "))
                result = calculator.log_base(x, base)
                print(f"Resultado: log_{base}({x}) = {result}")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == '4':
            x = float(input("Ingresa el valor de x: "))
            result = calculator.exp_e(x)
            print(f"Resultado: e^({x}) = {result}")
        
        elif choice == '5':
            base = float(input("Ingresa la base: "))
            x = float(input("Ingresa el exponente x: "))
            result = calculator.exp_base(base, x)
            print(f"Resultado: {base}^({x}) = {result}")

        elif choice == '6':
            base = float(input("Ingresa la base: "))
            exponent = float(input("Ingresa el exponente: "))
            result = calculator.power(base, exponent)
            print(f"Resultado: {base}^({exponent}) = {result}")

        elif choice == '7':
            try:
                x = float(input("Ingresa el valor de x: "))
                result = calculator.sqrt(x)
                print(f"Resultado: √({x}) = {result}")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == '8':
            print("Saliendo del programa.")
            break
        
        else:
            print("Opción inválida. Por favor, selecciona un número entre 1 y 8.")

if __name__ == "__main__":
    run_menu()