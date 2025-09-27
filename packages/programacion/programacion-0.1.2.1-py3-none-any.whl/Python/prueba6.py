import csv
class LectorCSV:

    def leer_csv() -> None:
        """Función leer_csv() -> None"""
        with open('/home/nrodgue0605/curso2025_26/Programación/Python/data.csv', newline="", encoding="utf-8") as archivo: #se le ha puesto el enlace del archivo
            lector = csv.reader(archivo)
            encabezados = next(lector)
            print("Encabezados:", encabezados)

            for i, fila in enumerate(lector):
                print(fila)
                if i == 21:
                    break
LectorCSV.leer_csv()