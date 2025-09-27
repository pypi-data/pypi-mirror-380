class Contador:
    def cuenta_atras():
        i = 10
        Contador.contador_cuenta_atras(i)

    def contador_cuenta_atras(i):
        while i >= 0:
            print(i)
            i -= 1

Contador.cuenta_atras()