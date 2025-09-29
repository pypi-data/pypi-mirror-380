import math

class CalculadoraTrigonometrica:
    """
    Una clase para una calculadora científica que puede operar en modo de
    grados ('grados') o radianes ('radianes'), incluyendo funciones recíprocas.
    """

    def __init__(self, mode='grados'):
        self.mode = mode

    def _grados_a_radianes(self, grados):
        return math.radians(grados)

    def _radianes_a_grados(self, radianes):
        return math.degrees(radianes)
    
    # --- Métodos de cálculo (sin cambios) ---
    def seno(self, angulo):
        angulo_en_radianes = angulo if self.mode == 'radianes' else self._grados_a_radianes(angulo)
        return math.sin(angulo_en_radianes)

    def coseno(self, angulo):
        angulo_en_radianes = angulo if self.mode == 'radianes' else self._grados_a_radianes(angulo)
        return math.cos(angulo_en_radianes)

    def tangente(self, angulo):
        if self.mode == 'grados' and angulo % 180 == 90:
            return float('inf')
        angulo_en_radianes = angulo if self.mode == 'radianes' else self._grados_a_radianes(angulo)
        return math.tan(angulo_en_radianes)

    def cosecante(self, angulo):
        seno_val = self.seno(angulo)
        if seno_val == 0:
            return float('inf')
        return 1 / seno_val

    def secante(self, angulo):
        coseno_val = self.coseno(angulo)
        if round(coseno_val, 10) == 0:
            return float('inf')
        return 1 / coseno_val

    def cotangente(self, angulo):
        seno_val = self.seno(angulo)
        if round(seno_val, 10) == 0:
           return float('inf')
        return self.coseno(angulo) / seno_val
    
    def arcoseno(self, valor):
        if not -1 <= valor <= 1:
            raise ValueError("El valor para arcoseno debe estar entre -1 y 1.")
        resultado_rad = math.asin(valor)
        return self._radianes_a_grados(resultado_rad) if self.mode == 'grados' else resultado_rad

    def arcocoseno(self, valor):
        if not -1 <= valor <= 1:
            raise ValueError("El valor para arcocoseno debe estar entre -1 y 1.")
        resultado_rad = math.acos(valor)
        return self._radianes_a_grados(resultado_rad) if self.mode == 'grados' else resultado_rad

    def arcotangente(self, valor):
        resultado_rad = math.atan(valor)
        return self._radianes_a_grados(resultado_rad) if self.mode == 'grados' else resultado_rad

    def arcocosecante(self, valor):
        if -1 < valor < 1:
            raise ValueError("El valor para arcocosecante debe ser >= 1 o <= -1.")
        return self.arcoseno(1 / valor)

    def arcosecante(self, valor):
        if -1 < valor < 1:
            raise ValueError("El valor para arcosecante debe ser >= 1 o <= -1.")
        return self.arcocoseno(1 / valor)

    def arcocotangente(self, valor):
        if valor == 0:
            return 90.0 if self.mode == 'grados' else math.pi / 2
        return self.arcotangente(1 / valor)

    # --- Menú interactivo ---
    def mostrar_menu(self):
        while True:
            print(f"\n--- Menú de Trigonometría (Modo: {self.mode}) ---")
            print("1. Seno (sin)")
            print("2. Coseno (cos)")
            print("3. Tangente (tan)")
            print("4. Cosecante (csc)")
            print("5. Secante (sec)")
            print("6. Cotangente (cot)")
            print("7. Arcoseno (asin)")
            print("8. Arcocoseno (acos)")
            print("9. Arcotangente (atan)")
            print("10. Arcocosecante (acsc)")
            print("11. Arcosecante (asec)")
            print("12. Arcotangente (acot)")
            print("99. Cambiar Modo (grados/radianes)")
            print("0. Volver al menú principal")
            opcion = input("Seleccione una opción: ")

            if opcion == '0':
                break
            
            if opcion == '99':
                self.mode = 'radianes' if self.mode == 'grados' else 'grados'
                print(f"Modo cambiado a: {self.mode}")
                continue

            # Diccionarios para mapear opciones a funciones
            funciones_angulares = {
                '1': ('Seno', self.seno), '2': ('Coseno', self.coseno),
                '3': ('Tangente', self.tangente), '4': ('Cosecante', self.cosecante),
                '5': ('Secante', self.secante), '6': ('Cotangente', self.cotangente),
            }
            funciones_inversas = {
                '7': ('Arcoseno', self.arcoseno), '8': ('Arcocoseno', self.arcocoseno),
                '9': ('Arcotangente', self.arcotangente), '10': ('Arcocosecante', self.arcocosecante),
                '11': ('Arcosecante', self.arcosecante), '12': ('Arcocotangente', self.arcocotangente)
            }

            try:
                if opcion in funciones_angulares:
                    unidad = "grados" if self.mode == 'grados' else "radianes"
                    valor = float(input(f"Ingrese el ángulo en {unidad}: "))
                    nombre_func, func = funciones_angulares[opcion]
                    resultado = func(valor)
                    print(f"El {nombre_func} de {valor} {unidad} es: {resultado}")

                elif opcion in funciones_inversas:
                    valor = float(input("Ingrese el valor para calcular el ángulo: "))
                    nombre_func, func = funciones_inversas[opcion]
                    resultado = func(valor)
                    unidad = "°" if self.mode == 'grados' else " rad"
                    print(f"El {nombre_func} de {valor} es: {resultado}{unidad}")

                else:
                    print("Opción no válida.")
            except ValueError as e:
                print(f"Error: {e}. Ingrese un número válido.")
            except Exception as e:
                print(f"Ocurrió un error inesperado: {e}")