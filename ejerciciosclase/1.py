def crear_multiplicador(factor):
    """Crea una función que multiplica por el factor indicado."""
    def multiplicar(numero):
        """Multiplica el número por el factor recordado."""
        return numero * factor

    return multiplicar


duplicar = crear_multiplicador(2)
triplicar = crear_multiplicador(3)

print(duplicar(5))   # 10
print(triplicar(5))  # 15
