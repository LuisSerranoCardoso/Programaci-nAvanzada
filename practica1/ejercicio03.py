"""Ejercicio 3: normalización de texto y sustitución de palabras."""
from typing import Optional


def process_text(
    text: str = "This is a default text with Python and amazing words.",
    words_to_replace: Optional[list[str]] = None,
) -> tuple[str, int]:
    """Pasa a minúsculas y sustituye palabras completas separadas por espacios.

    None selecciona la lista por defecto sin compartir una lista mutable
    entre llamadas. Una lista vacía explícita no sustituye ninguna palabra.
    split/join también normaliza los espacios interiores a uno solo.
    """
    if words_to_replace is None:
        words_to_replace = ["Python", "amazing"]
    targets = []
    for word in words_to_replace:
        targets.append(word.lower())
    result = []
    count = 0
    for word in text.lower().strip().split():
        if word in targets:
            result.append("*" * len(word))
            count += 1
        else:
            result.append(word)
    return " ".join(result), count


def main() -> None:
    """Muestra el caso por defecto y casos de mayúsculas, puntuación y vacío."""
    text, count = process_text()
    print("Reemplazar: Python amazing")
    print(f'Processed text: "{text}"')
    print("Palabras reemplazadas:", count)
    print(process_text("  PYTHON Python python.  ", ["python"]))
    print(process_text("Python", []))
    print(process_text(""))


if __name__ == "__main__":
    main()
