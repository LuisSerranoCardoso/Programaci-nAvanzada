"""Ejercicio 6: números primos y primos palíndromos."""


def is_prime(n: int) -> bool:
    """Comprueba primalidad probando divisores hasta la raíz cuadrada."""
    if n < 2:
        return False
    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 1
    return True


def prime_list(limit: int) -> list[int]:
    """Devuelve los primos hasta limit incluido; [] si limit < 2."""
    result = []
    for number in range(2, limit + 1):
        if is_prime(number):
            result.append(number)
    return result


def check_palindrome(primes: list[int]) -> list[int]:
    """Filtra los números palíndromos de una lista que se supone de primos."""
    result = []
    for prime in primes:
        text = str(prime)
        if text == text[::-1]:
            result.append(prime)
    return result


def categorize_prime(prime: int) -> str:
    """Clasifica un primo dado como pequeño, mediano o grande."""
    if prime < 10:
        return "pequeño"
    if prime < 100:
        return "mediano"
    return "grande"


def main() -> None:
    """Comprueba primalidad, generación, palíndromos y categorías."""
    for number in (-3, 0, 1, 2, 9, 11, 97, 101):
        print(f"{number}: primo = {is_prime(number)}")
    for limit in (1, 2, 30, 150):
        primes = prime_list(limit)
        print(f"Primos hasta {limit}: {primes}")
        print("Palíndromos:", check_palindrome(primes))
    for prime in (2, 11, 101):
        print(prime, categorize_prime(prime))


if __name__ == "__main__":
    main()
