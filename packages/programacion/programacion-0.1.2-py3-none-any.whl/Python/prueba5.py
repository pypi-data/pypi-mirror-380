class ContarLetras:
    
    @staticmethod    
    def numero_de_letras() -> None:
        """Función numero_de_letras() -> None"""
        palabra = input("Escrbe la palabra para que le cuenta el numero de letras: ")
        ContarLetras.numero_de_letras_proceso(palabra)
    
    @staticmethod
    def numero_de_letras_proceso(palabra: str) -> None:
        """Función numero_de_letras_proceso(palabra: str) -> None"""
        cantidad = len(palabra)
        print(f"La palabra {palabra} tiene {cantidad} letras.")
        
ContarLetras.numero_de_letras()