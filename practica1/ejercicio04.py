"""Ejercicio 4: cifrado César sobre el alfabeto inglés."""


def shift_char(char: str, shift: int) -> str:
    """Desplaza un carácter inglés; conserva los demás caracteres."""
    if len(char) != 1:
        raise ValueError("Se requiere exactamente un carácter.")
    if "a" <= char <= "z":
        base = ord("a")
    elif "A" <= char <= "Z":
        base = ord("A")
    else:
        return char
    return chr(base + (ord(char) - base + shift) % 26)


def encrypt(text: str, shift: int) -> str:
    """Cifra recorriendo el texto carácter a carácter."""
    result = ""
    for char in text:
        result += shift_char(char, shift)
    return result


def decrypt(text: str, shift: int) -> str:
    """Descifra reutilizando encrypt con el desplazamiento opuesto."""
    return encrypt(text, -shift)


def brute_force(cipher_text: str) -> list[str]:
    """Devuelve los descifrados para desplazamientos de 0 a 25 en ese orden."""
    results = []
    for shift in range(26):
        results.append(decrypt(cipher_text, shift))
    return results


def main() -> None:
    """Prueba los ejemplos, desplazamientos grandes y caracteres no ingleses."""
    print("Carácter:", shift_char("z", 3))
    print(encrypt("Hola, Mundo!", 3))
    print(decrypt("Krod, Pxqgr!", 3))
    print(encrypt("xyz", 3))
    print(encrypt("abc", -3))
    print(encrypt("abc Ñá 123!", 29))
    print("Texto vacío:", repr(encrypt("", 3)))
    for shift, text in enumerate(brute_force("Krod, Pxqgr!")):
        print(f"{shift:2}: {text}")


if __name__ == "__main__":
    main()
