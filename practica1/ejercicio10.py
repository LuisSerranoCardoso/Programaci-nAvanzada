"""Ejercicio 10: menú de cadenas, identidad de objetos y for...else."""
from typing import Optional


def starting_with(strings: list[str], letter: str) -> list[str]:
    """Devuelve cadenas que empiezan por letter, distinguiendo mayúsculas."""
    result = []
    for text in strings:
        if text.startswith(letter):
            result.append(text)
    return result


def count_containing(strings: list[str], substring: str) -> int:
    """Cuenta cadenas con la subcadena, no el total de apariciones."""
    count = 0
    for text in strings:
        if substring in text:
            count += 1
    return count


def longest_shortest(strings: list[str]) -> Optional[tuple[str, str]]:
    """Devuelve (más larga, más corta); gana la primera en empate; None si vacío."""
    if not strings:
        return None
    longest = strings[0]
    shortest = strings[0]
    for text in strings:
        if len(text) > len(longest):
            longest = text
        if len(text) < len(shortest):
            shortest = text
    return longest, shortest


def same_object(strings: list[str], first: int, second: int) -> bool:
    """Compara identidad con is, no igualdad de contenido; índices desde cero."""
    if not (0 <= first < len(strings) and 0 <= second < len(strings)):
        raise IndexError("Índice fuera de rango.")
    return strings[first] is strings[second]


def has_long_string(strings: list[str]) -> bool:
    """Comprueba con for...else si existe una cadena con más de diez caracteres."""
    for text in strings:
        if len(text) > 10:
            break
    else:
        return False
    return True


def check_long_strings(strings: list[str]) -> bool:
    """Muestra el resultado de buscar cadenas con más de diez caracteres."""
    found = has_long_string(strings)
    if found:
        print("Hay alguna cadena con más de 10 caracteres.")
    else:
        print("Ninguna cadena tiene más de 10 caracteres.")
    return found


def read_strings() -> list[str]:
    """Pide una cantidad no negativa y después cada cadena, permitiendo vacías."""
    while True:
        try:
            count = int(input("Número de cadenas: "))
            if count >= 0:
                break
        except ValueError:
            pass
        print("Introduzca un entero no negativo.")
    strings = []
    for index in range(count):
        strings.append(input(f"Cadena {index}: "))
    return strings


def main() -> None:
    """Comprueba funciones sin salida previa y ejecuta el menú de cadenas."""
    example = ["Ana", "oso", "Programación", "Anabel"]
    assert starting_with(example, "A") == ["Ana", "Anabel"]
    assert count_containing(example, "a") == 3
    assert longest_shortest(example) == ("Programación", "Ana")
    assert longest_shortest([]) is None
    assert same_object(example, 0, 0)
    assert not same_object(example, 0, 1)
    assert not has_long_string([])
    assert not has_long_string(["1234567890"])
    assert has_long_string(example)
    strings = read_strings()
    while True:
        print("\n1. Empiezan por letra\n2. Contienen subcadena")
        print("3. Más larga y más corta\n4. Mismo objeto\n5. Longitud > 10\n0. Salir")
        option = input("Opción: ").strip()
        if option == "0":
            break
        if option == "1":
            letter = input("Letra inicial (se distinguen mayúsculas): ")
            if len(letter) != 1 or not letter.isalpha():
                print("Debe introducir una sola letra.")
            else:
                for text in starting_with(strings, letter):
                    print(text)
        elif option == "2":
            print(count_containing(strings, input("Subcadena: ")))
        elif option == "3":
            result = longest_shortest(strings)
            if result is None:
                print("La lista está vacía.")
            else:
                print(f"Más larga: {result[0]!r}; más corta: {result[1]!r}")
        elif option == "4":
            if not strings:
                print("La lista está vacía.")
                continue
            for index, text in enumerate(strings):
                print(index, repr(text))
            try:
                first = int(input("Primer índice: "))
                second = int(input("Segundo índice: "))
                print("Mismo objeto:", same_object(strings, first, second))
            except (ValueError, IndexError) as error:
                print("Índices no válidos:", error)
        elif option == "5":
            check_long_strings(strings)
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()
