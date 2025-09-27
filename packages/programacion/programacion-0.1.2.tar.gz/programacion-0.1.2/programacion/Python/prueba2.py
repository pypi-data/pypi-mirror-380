class Conversor:

    @staticmethod
    def conversor_tasa_fija() -> None:
        """Función conversor_tasa_fija() -> None"""
        euro_dolar = 1.07
        dolar_euro = 1

        print("==== Conversor de Monedas tasa fija ====")
        print("1. Euros -> Dólares")
        print("2. Dólares -> Euros")
        opcion = input("Elige una opcion (1/2): ")

        if opcion == "1":
            euros = float(input("Escribe la cantidad en euros: "))
            dolares = euros * euro_dolar
            print(f"{euros} € = {dolares:.2f} $")
        elif opcion == "2":
            dolares = float(input("Escribe la cantidad en dólares: "))
            euros = dolares * dolar_euro
            print(f"{dolares} $ = {euros:.2f} €")
        else:
            print("Opción incorrecta")
        
Conversor.conversor_tasa_fija()