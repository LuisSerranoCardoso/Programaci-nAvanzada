"""Ejercicio 1: convertir segundos a días, horas, minutos y segundos."""


def is_integer(text: str) -> bool:
    """Indica si text admite la conversión int()."""
    try:
        int(text)
        return True
    except ValueError:
        return False


def seconds_to_dhms(total_seconds: int) -> tuple[int, int, int, int]:
    """Descompone un entero no negativo en días, horas, minutos y segundos."""
    if total_seconds < 0:
        raise ValueError("Los segundos no pueden ser negativos.")
    days = total_seconds // 86400
    remaining = total_seconds % 86400
    hours = remaining // 3600
    remaining = remaining % 3600
    minutes = remaining // 60
    seconds = remaining % 60
    return days, hours, minutes, seconds


def main() -> None:
    """Comprueba los ejemplos sin imprimirlos y solicita segundos válidos."""
    # El guion exige pruebas desde main. Los assert no imprimen si se cumplen.
    for text in ("0", "-5", "+5", " 42 "):
        assert is_integer(text)
    for text in ("3.14", "Hola", "True"):
        assert not is_integer(text)
    for value, expected in (
        (0, (0, 0, 0, 0)), (59, (0, 0, 0, 59)), (60, (0, 0, 1, 0)),
        (3600, (0, 1, 0, 0)), (86400, (1, 0, 0, 0)), (93784, (1, 2, 3, 4)),
    ):
        assert seconds_to_dhms(value) == expected
    while True:
        text = input("Introduzca los segundos: ")
        if is_integer(text) and int(text) >= 0:
            break
        print("Entrada no válida. Introduzca un entero no negativo.")
    total = int(text)
    days, hours, minutes, seconds = seconds_to_dhms(total)
    print(f"{total} segundos son {days} d, {hours} h, {minutes} min y {seconds} s.")


if __name__ == "__main__":
    main()
