from datetime import datetime

class CalcularFechaNacimiento:
    """
    Clase CalcularFechaNacimiento
    """
    @staticmethod
    def calcularFechaNac() -> None:
        """Función calcularFechaNac() -> None"""
        fecha_str = input("Escribe tu fecha de nacimiento para sacar tu edad (dd/mm/yyyy): ")
        try:
            fecha_nac = datetime.strptime(fecha_str, "%d/%m/%Y")
            hoy = datetime.now()
            
            edad = hoy.year - fecha_nac.year
            if (hoy.month, hoy.day) < (fecha_nac.month, fecha_nac.day):
                edad -= 1
                
            print(f"Tienes {edad} años de vida.")
        except ValueError:
            print("Formato de fecha incorrecto, utiliza (dd/mm/yyyy).")

# Ejecución del Programa
CalcularFechaNacimiento.calcularFechaNac()
