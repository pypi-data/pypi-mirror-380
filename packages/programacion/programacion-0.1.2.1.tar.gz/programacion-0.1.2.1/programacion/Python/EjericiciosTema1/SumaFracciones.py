class Fraccion:

    def fraccion():
        a = 9
        b = 10
        c = 8
        d = 20
        Fraccion.operar_fraccion(a, b, c, d)

    def operar_fraccion(a, b, c, d):
        numerador = a*d + b*c
        denominador = b*d
        print("La suma es:", numerador, "/", denominador)

Fraccion.fraccion()