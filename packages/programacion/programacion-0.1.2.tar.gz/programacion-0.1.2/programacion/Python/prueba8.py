import random
import time

class Mecanografia:
    textos: list[str] = [
        "La programación es una habilidad muy útil.",
        "Python es un lenguaje versátil y potente.",
        "La práctica constante mejora la mecanografía.",
        "Escribe este texto lo más rápido que puedas.",
        "La precisión es más importante que la velocidad."
    ]

    @staticmethod
    def practicar() -> None:
        """Función practicar() -> None"""
        # Elegir un texto aleatorio
        texto_objetivo: str = random.choice(Mecanografia.textos)
        print("\n===== EJERCICIO DE MECANOGRAFÍA =====")
        print(f"Escribe exactamente este texto:\n\n{texto_objetivo}\n")

        # Esperar al usuario
        input("Presiona ENTER para comenzar...")
        
        # Iniciar cronómetro
        inicio: float = time.time()
        texto_usuario: str = input("\nTeclea aquí: ")
        fin: float = time.time()

        # Calcular resultados
        tiempo: float = fin - inicio
        tiempo_minutos: float = tiempo / 60

        # Precisión
        if texto_usuario == texto_objetivo:
            precision: float = 100.0
        else:
            coincidencias: int = sum(1 for a, b in zip(texto_usuario, texto_objetivo) if a == b)
            precision = (coincidencias / len(texto_objetivo)) * 100

        # Velocidad (palabras por minuto)
        palabras: int = len(texto_usuario.split())
        velocidad: float = palabras / tiempo_minutos if tiempo_minutos > 0 else 0

        # Mostrar resultados
        print("\n===== RESULTADOS =====")
        print(f"Tiempo total: {tiempo:.2f} segundos")
        print(f"Precisión: {precision:.2f}%")
        print(f"Velocidad: {velocidad:.2f} PPM (palabras por minuto)")

if __name__ == "__main__":
    Mecanografia.practicar()
