"""
Conversor de monedas encualquier formato
"""
import requests
class Conversor:
    """
    Clase Conversor
    """    
    @staticmethod
    def conversor_de_monedas_en_cualquier_formato() -> None:
        """Función conversor_de_monedas_en_cualquier_formato() -> None"""
        print("==== Conversor de Monedas (tasa en tiempo real) ====")
        
        moneda_origen = input("Moneda de origen (ej: EUR, USD, GBP, JPY): ").upper()
        moneda_destino = input("Moneda de destino (ej: EUR, USD, GBP, JPY): ").upper()
        cantidad = float(input(f"Cantidad en {moneda_origen}: "))
        
        url = f"https://open.er-api.com/v6/latest/{moneda_origen}"
        response = requests.get(url)
        data = response.json()
        
        if "rates" not in data:
            print("Error: la API no devolvió tasas de cambio.")
            print("DEBUG:", data)
            return
        
        if moneda_destino not in data["rates"]:
            print(f"Error: la moneda {moneda_destino} no está disponible.")
            return
        
        tasa = data["rates"][moneda_destino]
        convertido = cantidad * tasa
        
        print(f"\n💱 {cantidad} {moneda_origen} = {convertido:.2f} {moneda_destino}")
        print(f"(tasa actual: 1 {moneda_origen} = {tasa:.4f} {moneda_destino})")

Conversor.conversor_de_monedas_en_cualquier_formato()
