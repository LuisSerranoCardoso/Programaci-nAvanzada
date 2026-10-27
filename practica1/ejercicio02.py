"""Ejercicio 2: años bisiestos y calendario gregoriano."""


def is_leap_year(year: int) -> bool:
    """Aplica la regla de los años bisiestos a cualquier año entero."""
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)


def leap_years_between(start: int, end: int) -> list[int]:
    """Devuelve bisiestos entre ambos extremos; si start > end, devuelve []."""
    years = []
    for year in range(start, end + 1):
        if is_leap_year(year):
            years.append(year)
    return years


def explain_leap_year(year: int) -> str:
    """Explica el resultado de aplicar la regla de divisibilidad al año."""
    if year % 400 == 0:
        return f"{year} es bisiesto: es divisible entre 400."
    if year % 100 == 0:
        return f"{year} no es bisiesto: es divisible entre 100 pero no entre 400."
    if year % 4 == 0:
        return f"{year} es bisiesto: es divisible entre 4 y no entre 100."
    return f"{year} no es bisiesto: no es divisible entre 4."


def main() -> None:
    """Comprueba ejemplos sin mostrarlos y solicita un año al usuario."""
    for year, expected in ((1900, False), (2000, True), (2023, False),
                           (2024, True), (2100, False)):
        assert is_leap_year(year) == expected
    assert leap_years_between(1896, 1912) == [1896, 1904, 1908, 1912]
    assert leap_years_between(2024, 2020) == []
    assert explain_leap_year(1900) == (
        "1900 no es bisiesto: es divisible entre 100 pero no entre 400."
    )
    assert explain_leap_year(2000) == "2000 es bisiesto: es divisible entre 400."
    assert explain_leap_year(2023) == "2023 no es bisiesto: no es divisible entre 4."
    assert explain_leap_year(2024) == (
        "2024 es bisiesto: es divisible entre 4 y no entre 100."
    )
    while True:
        try:
            year = int(input("Año: "))
            break
        except ValueError:
            print("Introduzca un año entero.")
    if year < 1582:
        print("El calendario gregoriano se estableció en 1582.")
    else:
        print(explain_leap_year(year))


if __name__ == "__main__":
    main()
