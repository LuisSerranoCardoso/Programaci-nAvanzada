def is_integer(text: str) -> bool:
    """Indica si el texto representa un número entero"""
    try:
        int(text)
        return True
    except ValueError:
        return False

def seconds_to_dhms(total_seconds: int) -> tuple[int, int, int, int]:
    """Convierte segundos no negativos en días, horas, minutos y segundos"""
    days = total_seconds // 86400
    remaining = total_seconds % 86400

    hours = remaining // 3600
    remaining = remaining % 3600

    minutes = remaining // 60
    seconds = remaining % 60

    return days, hours, minutes, seconds

def main() -> None:
    """Solicita segundos no negativos y muestra su desglose."""

    #Pruebas de conversión.
    assert seconds_to_dhms(0) == (0, 0, 0, 0)
    assert seconds_to_dhms(59) == (0, 0, 0, 59)
    assert seconds_to_dhms(60) == (0, 0, 1, 0)
    assert seconds_to_dhms(3600) == (0, 1, 0, 0)
    assert seconds_to_dhms(86400) == (1, 0, 0, 0)
    assert seconds_to_dhms(93784) == (1, 2, 3, 4)

    #Pruebas de validación
    assert is_integer("0")
    assert is_integer("-5")
    assert is_integer("+5")
    assert is_integer(" 42 ")
    assert not is_integer("3.14")
    assert not is_integer("Hola")
    assert not is_integer("True"

                          )
    while True:
        text = input("Introduzca los segundos: ")

        if is_integer(text):
            seconds = int(text)

            if seconds >= 0:
                break

        print("Entrada no valida. Introduzca un entero no negativo.")

    days, hours, minutes, remaining = seconds_to_dhms(seconds)

    print(f"{seconds} segundos son {days} d, {hours} h, {minutes} min y {remaining} s.")

if __name__ == "__main__":
    main()
