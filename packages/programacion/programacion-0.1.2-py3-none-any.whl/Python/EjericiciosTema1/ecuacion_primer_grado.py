class Ecuacion:

    def resolucion_ecuacion():
        a = float(input("Escribe el primer número: "))
        b = float(input("Escribe el segundo número: "))
        Ecuacion.resolucion_ecuacion_formula(a, b)

    def resolucion_ecuacion_formula(a, b):
        if b == 0:
            if a == 0:
                print("Soluciones varias")
            else:
                print("Sin solución")

        else:
            x = -a / b
            print("La solución de la ecuación es:", x)
        
Ecuacion.resolucion_ecuacion()