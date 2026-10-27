"""Ejercicio 11: anonimización del informe simulado del enunciado.

Es un ejercicio sobre un formato concreto, no un anonimizador general.
"""
import re
from datetime import date

DATE_PATTERN = re.compile(r"\b([0-9]{1,2})/([0-9]{1,2})/([0-9]{4})\b")
BIRTH_PATTERN = re.compile(r"^Fecha de nacimiento:[^\r\n]*", re.MULTILINE)
NAME_PATTERN = re.compile(r"^Nombre:[^\r\n]*", re.MULTILINE)
DOCTOR_PATTERN = re.compile(r"\bDra?\.[^\r\n]*")


def parse_date(text: str) -> date:
    """Convierte una fecha día/mes/año y verifica que exista en el calendario."""
    match = DATE_PATTERN.fullmatch(text)
    if match is None:
        raise ValueError("Formato de fecha incorrecto.")
    day, month, year = match.groups()
    return date(int(year), int(month), int(day))


def calculate_age(birth: date, consultation: date) -> int:
    """Calcula años cumplidos a fecha de consulta, descontando cumpleaños pendiente."""
    if consultation < birth:
        raise ValueError("La consulta no puede preceder al nacimiento.")
    age = consultation.year - birth.year
    if (consultation.month, consultation.day) < (birth.month, birth.day):
        age -= 1
    return age


def anonymize_report(report: str) -> str:
    """Anonimiza un informe con una línea de nacimiento y una de consulta/médico.

    Lanza ValueError si faltan datos para calcular la edad o las fechas
    son inválidas. Calcula la edad antes de ocultar las demás fechas.
    """
    birth_line = BIRTH_PATTERN.search(report)
    if birth_line is None:
        raise ValueError("Falta la línea de fecha de nacimiento.")
    birth_match = DATE_PATTERN.search(birth_line.group())
    if birth_match is None:
        raise ValueError("Falta una fecha de nacimiento con formato válido.")
    consultation_match = None
    for line in report.splitlines():
        doctor = DOCTOR_PATTERN.search(line)
        if doctor is not None:
            consultation_match = DATE_PATTERN.search(line[:doctor.start()])
            if consultation_match is not None:
                break
    if consultation_match is None:
        raise ValueError("Falta la fecha de consulta en la línea del médico.")
    birth = parse_date(birth_match.group())
    consultation = parse_date(consultation_match.group())
    age = calculate_age(birth, consultation)
    result = BIRTH_PATTERN.sub(f"Edad: {age}", report)
    result = DATE_PATTERN.sub("FECHA", result)
    result = NAME_PATTERN.sub("Nombre: PACIENTE", result)
    result = DOCTOR_PATTERN.sub("MEDICO", result)
    return result


def main() -> None:
    """Prueba el informe original y un cumpleaños pendiente con día/mes de una cifra."""
    report = """Informe clínico de Urgencias
Nombre: Juan Pérez López
Género: Hombre
Fecha de nacimiento: 12/05/1980
Motivo de consulta: dolor abdominal
12/05/2023 Dr. Ramírez
Tratamiento: reposo y analgésicos"""
    print(anonymize_report(report))
    additional = """Informe de prueba
Nombre: Ana Ejemplo
Fecha de nacimiento: 9/5/2000
8/5/2023 Dra. Ejemplo
Revisión prevista: 10/6/2023"""
    print("\nCaso adicional:")
    print(anonymize_report(additional))


if __name__ == "__main__":
    main()
