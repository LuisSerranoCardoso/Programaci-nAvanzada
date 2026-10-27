"""Ejercicio 8: menú de operaciones con números enteros."""
from typing import Optional


def total_sum(numbers: list[int]) -> int:
    """Suma todos los elementos; devuelve 0 para la lista vacía."""
    total = 0
    for number in numbers:
        total += number
    return total


def signed_sums(numbers: list[int]) -> tuple[int, int]:
    """Devuelve la suma de positivos y de negativos, por separado."""
    positive = 0
    negative = 0
    for number in numbers:
        if number > 0:
            positive += number
        elif number < 0:
            negative += number
    return positive, negative


def maximum_minimum(numbers: list[int]) -> Optional[tuple[int, int]]:
    """Devuelve (máximo, mínimo), o None para una lista vacía."""
    if not numbers:
        return None
    maximum = numbers[0]
    minimum = numbers[0]
    for number in numbers:
        if number > maximum:
            maximum = number
        if number < minimum:
            minimum = number
    return maximum, minimum


def all_unique(numbers: list[int]) -> bool:
    """Indica si no hay repetidos; la lista vacía cumple esta propiedad."""
    seen = []
    for number in numbers:
        if number in seen:
            return False
        seen.append(number)
    return True


def compare_signs(numbers: list[int]) -> str:
    """Compara cantidades de positivos y negativos mediante operador condicional."""
    positive = 0
    negative = 0
    for number in numbers:
        if number > 0:
            positive += 1
        elif number < 0:
            negative += 1
    return (
        "Hay más positivos." if positive > negative else
        "Hay más negativos." if negative > positive else
        "Hay tantos positivos como negativos."
    )


def read_numbers() -> list[int]:
    """Pide enteros separados por espacios; una entrada vacía representa []."""
    while True:
        try:
            numbers = []
            for text in input("Enteros separados por espacios (vacío = []): ").split():
                numbers.append(int(text))
            return numbers
        except ValueError:
            print("Entrada inválida: use únicamente enteros separados por espacios.")


def main() -> None:
    """Comprueba casos sin imprimirlos y ejecuta el menú solicitado."""
    assert total_sum([1, -2, 0, 3]) == 2
    assert total_sum([]) == 0
    assert signed_sums([1, -2, 0, 3]) == (4, -2)
    assert signed_sums([]) == (0, 0)
    assert maximum_minimum([1, -2, 0, 3]) == (3, -2)
    assert maximum_minimum([]) is None
    assert all_unique([])
    assert not all_unique([2, 2])
    assert compare_signs([-1, 0, 1]) == "Hay tantos positivos como negativos."
    assert compare_signs([1, 2, -1]) == "Hay más positivos."
    assert compare_signs([-1, -2, 1]) == "Hay más negativos."
    numbers = read_numbers()
    while True:
        print("\n1. Suma total\n2. Sumas por signo\n3. Máximo y mínimo")
        print("4. Elementos únicos\n5. Comparar signos\n0. Salir")
        option = input("Opción: ").strip()
        if option == "0":
            break
        if option == "1":
            print(total_sum(numbers))
        elif option == "2":
            positive, negative = signed_sums(numbers)
            print(f"Suma positiva: {positive}; suma negativa: {negative}")
        elif option == "3":
            result = maximum_minimum(numbers)
            if result is None:
                print("La lista está vacía: no tiene máximo ni mínimo.")
            else:
                print(f"Máximo: {result[0]}; mínimo: {result[1]}")
        elif option == "4":
            print("Todos únicos:", all_unique(numbers))
        elif option == "5":
            print(compare_signs(numbers))
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()
