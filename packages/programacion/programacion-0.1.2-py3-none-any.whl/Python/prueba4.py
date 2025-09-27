class MaximoComunDivisor:
    """
    Clase MaximoComunDivisor
    """
    @staticmethod
    def max_com_div() -> None:
        """Función max_com_div() -> None"""
        a = 76
        b = 44
        c = a // b
        r = a % b
        MaximoComunDivisor.max_com_div_operacion(a, b, c, r)

    @staticmethod
    def max_com_div_operacion(a, b, c, r) -> None:
        """Función max_com_div_operacion(a, b, c, r) -> None"""
        while r != 0:
            a = b
            b = r
            c = a // b
            r = a % b
        mcd = b
        print(mcd)

# Se activa el programa
MaximoComunDivisor.max_com_div()