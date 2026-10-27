"""Ejercicio 7: listas sin ordenación incorporada ni conjuntos."""
from typing import Optional


def remove_duplicates(numbers: list[int]) -> list[int]:
    """Devuelve valores únicos en orden de primera aparición sin modificar numbers."""
    result = []
    for number in numbers:
        if number not in result:
            result.append(number)
    return result


def rotate_left(numbers: list[int], k: int) -> list[int]:
    """Rota a la izquierda; k negativo rota a la derecha. Siempre crea otra lista."""
    if not numbers:
        return []
    k %= len(numbers)
    result = []
    for index in range(len(numbers)):
        result.append(numbers[(index + k) % len(numbers)])
    return result


def split_even_odd(numbers: list[int]) -> tuple[list[int], list[int]]:
    """Separa pares e impares preservando su orden."""
    even = []
    odd = []
    for number in numbers:
        if number % 2 == 0:
            even.append(number)
        else:
            odd.append(number)
    return even, odd


def merge_sorted(a: list[int], b: list[int]) -> list[int]:
    """Fusiona dos listas ya ordenadas mediante dos índices, sin alterarlas."""
    result = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    while i < len(a):
        result.append(a[i])
        i += 1
    while j < len(b):
        result.append(b[j])
        j += 1
    return result


def second_largest(numbers: list[int]) -> Optional[int]:
    """Obtiene el segundo máximo distinto en una pasada, o None si no existe."""
    largest = None
    second = None
    for number in numbers:
        if largest is None or number > largest:
            second = largest
            largest = number
        elif number != largest and (second is None or number > second):
            second = number
    return second


def main() -> None:
    """Prueba todos los ejemplos y casos vacíos y negativos."""
    print(remove_duplicates([3, 1, 3, 2, 1]))
    numbers = [1, 2, 3, 4, 5]
    for k in (2, 7, -1, 0):
        print(k, rotate_left(numbers, k))
    print("Original:", numbers)
    print(split_even_odd([1, 2, 3, 4, 5, 6]))
    print(merge_sorted([1, 4, 9], [2, 3, 10, 11]))
    for values in ([4, 9, 2, 9, 7], [5, 5], [], [8], [-4, -2, -3]):
        print(values, "Segundo máximo:", second_largest(values))
    print(remove_duplicates([]), rotate_left([], 3), split_even_odd([]))
    print(merge_sorted([], [1, 2]))


if __name__ == "__main__":
    main()
