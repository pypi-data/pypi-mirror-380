class Silaba:

    @staticmethod
    def separar_en_silabas(palabra: str) -> list:
        """Función separar_en_silabas(palabra: str) -> list"""
        palabra = palabra.lower()
        vocales = "aeiouáéíóúü"
        fuertes = "aáeéoó"
        silabas = []
        silaba = ""

        i = 0
        while i < len(palabra):
            silaba += palabra[i]

            if palabra[i] in vocales:
                if i+1 < len(palabra) and palabra[i+1] in vocales:
                    if palabra[i] in fuertes and palabra[i+1] in fuertes:
                        silabas.append(silaba)
                        silaba = ""
                else:
                    if i+1 < len(palabra):
                        if palabra[i+1] not in vocales:
                            silabas.append(silaba)
                            silaba = ""
                        else:
                            
                            pass
                    else:
                        silabas.append(silaba)
                        silaba = ""

            i += 1

        if silaba:
            silabas.append(silaba)

        return silabas


if __name__ == "__main__":
    palabra = input("Escribe la palabra para su posterior separación en sílabas: ")
    resultado = Silaba.separar_en_silabas(palabra)
    print("Sílabas:", "-".join(resultado))
