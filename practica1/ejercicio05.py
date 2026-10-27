"""Ejercicio 5: palíndromos en frases y palabras."""


def normalize(text: str) -> str:
    """Quita tildes vocálicas, diéresis y caracteres no alfanuméricos."""
    text = text.lower()
    for original, replacement in zip("áéíóúü", "aeiouu"):
        text = text.replace(original, replacement)
    result = ""
    for char in text:
        if char.isalnum():
            result += char
    return result


def is_palindrome(text: str) -> bool:
    """Compara el texto normalizado con su reverso; el vacío es palíndromo."""
    normalized = normalize(text)
    return normalized == normalized[::-1]


def find_palindromes(sentences: list[str]) -> list[str]:
    """Devuelve las frases palíndromas conservando su escritura y orden."""
    result = []
    for sentence in sentences:
        if is_palindrome(sentence):
            result.append(sentence)
    return result


def palindrome_words(text: str) -> list[str]:
    """Extrae palabras palíndromas de al menos tres letras de una frase sin signos."""
    result = []
    for word in text.split():
        if len(word) >= 3 and is_palindrome(word):
            result.append(word)
    return result


def main() -> None:
    """Prueba las frases indicadas y ejemplos adicionales."""
    sentences = [
        "Anita lava la tina",
        "Dábale arroz a la zorra el abad",
        "Esto no es un palíndromo",
        "¿Acaso hubo búhos acá?",
        "Reconocer",
        "Python",
    ]
    for phrase in find_palindromes(sentences):
        print(phrase)
    print(palindrome_words("Ana vio un oso en el ojo de Anita"))
    print("Normalización:", normalize("¡ÁÉÍÓÚÜ Ñ 123!"))
    print("Vacío:", is_palindrome(""))


if __name__ == "__main__":
    main()
