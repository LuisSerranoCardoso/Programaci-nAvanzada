"""Ejercicio 12: anagramas y agrupación estable."""


def is_anagram(word1: str, word2: str) -> bool:
    """Compara letras ignorando mayúsculas y espacios, sin quitar tildes."""
    return sorted(word1.lower().replace(" ", "")) == sorted(word2.lower().replace(" ", ""))


def group_anagrams(words: list[str]) -> list[list[str]]:
    """Agrupa anagramas en orden de primera aparición, conservando duplicados."""
    groups = []
    for word in words:
        for group in groups:
            if is_anagram(word, group[0]):
                group.append(word)
                break
        else:
            groups.append([word])
    return groups


def largest_group(groups: list[list[str]]) -> list[str]:
    """Devuelve una copia del grupo mayor; el primero si empatan; [] si vacío."""
    largest = []
    for group in groups:
        if len(group) > len(largest):
            largest = group
    return largest.copy()


def find_anagrams(word: str, words: list[str]) -> list[str]:
    """Busca anagramas excluyendo coincidencias literales sin distinguir caja."""
    result = []
    for candidate in words:
        if candidate.lower() != word.lower() and is_anagram(word, candidate):
            result.append(candidate)
    return result


def main() -> None:
    """Prueba todos los ejemplos y listas vacías y grupos empatados."""
    words = ["roma", "amor", "pelo", "mora", "casa", "lope", "ramo"]
    print(is_anagram("Roma", "amor"))
    print(is_anagram("casa", "caso"))
    print(is_anagram("dormitory", "dirty room"))
    print(group_anagrams(words))
    print(largest_group(group_anagrams(words)))
    print(find_anagrams("amor", words))
    print(find_anagrams("amor", ["amor", "roma", "AMOR", "roma"]))
    print(find_anagrams("sol", words))
    print(group_anagrams(["sol", "los", "sal", "las", "otra"]))
    print(largest_group([["sol", "los"], ["sal", "las"]]))
    print(group_anagrams([]), largest_group([]))


if __name__ == "__main__":
    main()
