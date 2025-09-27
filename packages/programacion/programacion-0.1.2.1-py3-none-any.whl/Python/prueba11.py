"""
Programa para evaluar expresiones matemáticas.
"""

class EvaluarExpresiones:
    """
    Clase EvaluarExpresiones
    """
    def evaluacion_de_la_expresion(self) -> None:
        """Función evaluacion_de_la_expresion(self) -> None"""
        expresion = input("Escribe la expresión numérica que quieres evaluar: ")
        try:
            resultado = eval(expresion)
            print(f"La solución de la expresión es: {resultado}")
        except Exception as e:
            print(f"Ha ocurrido un error al evaluar la expresión: {e}")


# Prueba del programa            
if __name__ == "__main__":
    evaluador = EvaluarExpresiones()
    evaluador.evaluacion_de_la_expresion()

# Mejoras hechas
# Se le ha añadido lo siguiente:
# if __name__ == "__main__":
#   evaluador = EvaluarExpresiones()
#   evaluador.evaluacion_de_la_expresion()