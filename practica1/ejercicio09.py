"""Ejercicio 9: representación, evaluación y derivación de polinomios."""
from typing import Union

Number = Union[int, float]


def format_monomial(coef: Number, exp: int) -> str:
    """Representa un monomio con signo explícito; omite coeficientes cero."""
    if coef == 0:
        return ""
    sign = "+" if coef > 0 else "-"
    magnitude = abs(coef)
    if exp == 0:
        return sign + str(magnitude)
    coefficient = "" if magnitude == 1 else str(magnitude)
    power = "x" if exp == 1 else f"x**{exp}"
    return sign + coefficient + power


def format_polynomial(coefs: list[Number]) -> str:
    """Representa términos de mayor a menor exponente, reutilizando monomios."""
    result = ""
    for exp in range(len(coefs) - 1, -1, -1):
        term = format_monomial(coefs[exp], exp)
        if not term:
            continue
        if not result:
            result = term[1:] if term[0] == "+" else term
        else:
            result += f" {term[0]} {term[1:]}"
    return result if result else "0"


def evaluate(coefs: list[Number], x: Number) -> Number:
    """Evalúa la suma de coeficiente por x elevado a su índice."""
    result = 0
    for exp, coef in enumerate(coefs):
        result += coef * x ** exp
    return result


def derivative(coefs: list[Number]) -> list[Number]:
    """Deriva los coeficientes; devuelve [] para un polinomio constante o vacío."""
    result = []
    for exp in range(1, len(coefs)):
        result.append(exp * coefs[exp])
    # Los ceros finales no cambian el polinomio. Si la derivada es toda
    # cero, el original también era constante (p. ej., [5, 0, 0]).
    if not any(result):
        return []
    return result


def main() -> None:
    """Prueba los ejemplos, coeficientes enteros y polinomios degenerados."""
    for coef, exp in ((2.0, 3), (1.0, 2), (-1.0, 1), (4.0, 0), (0.0, 5)):
        print(repr(format_monomial(coef, exp)))
    for coefs in ([4.0, 1.0, 0.0, 2.0], [0.0, -1.0, 3.0],
                  [-2.5, 0.0, -1.0], [0.0, 0.0], [], [7], [1, -1, 2]):
        print("Coeficientes:", coefs)
        print("Polinomio:", format_polynomial(coefs))
        print("Valor en 2:", evaluate(coefs, 2))
        print("Derivada:", derivative(coefs))


if __name__ == "__main__":
    main()
