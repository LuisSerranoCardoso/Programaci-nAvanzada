"""Práctica 2: clase Time, validación de horas y menú de terminal.

Decisiones donde el guion no fija un contrato:
- Estado inicial: 00:00:00 en formato 24 HOURS.
- Las properties son de solo lectura: set_time cambia la hora completa.
- get_time devuelve (horas, minutos, segundos, formato).
- from_string muestra un mensaje y devuelve None si la entrada es inválida.
- time_count cuenta construcciones, no objetos vivos. Una cadena inválida
  se rechaza antes de construir un objeto, por lo que no aumenta el contador.
"""
from __future__ import annotations

import re
from typing import ClassVar, Optional


class Time:
    """Representa una hora válida en formato AM, PM o 24 HOURS."""

    TIME_FORMATS: ClassVar[tuple[str, ...]] = ("AM", "PM", "24 HOURS")
    time_count: ClassVar[int] = 0

    # Instancia: inicializa el estado privado de cada objeto nuevo.
    def __init__(self) -> None:
        """Crea una hora válida a medianoche e incrementa el contador global."""
        self.__hours = 0
        self.__minutes = 0
        self.__seconds = 0
        self.__time_format = "24 HOURS"
        Time.time_count += 1

    # Instancia: expone únicamente las horas del objeto receptor.
    @property
    def hours(self) -> int:
        """Devuelve las horas sin permitir asignación directa."""
        return self.__hours

    # Instancia: consulta los minutos del objeto receptor.
    @property
    def minutes(self) -> int:
        """Devuelve los minutos sin permitir asignación directa."""
        return self.__minutes

    # Instancia: consulta los segundos del objeto receptor.
    @property
    def seconds(self) -> int:
        """Devuelve los segundos sin permitir asignación directa."""
        return self.__seconds

    # Instancia: consulta el formato almacenado en el objeto receptor.
    @property
    def time_format(self) -> str:
        """Devuelve el formato almacenado en mayúsculas."""
        return self.__time_format

    # Instancia: modifica el formato privado de este objeto.
    def __assign_format(self, time_format: str) -> bool:
        """Valida el formato y lo asigna en mayúsculas si es correcto."""
        if not self.is_valid_format(time_format):
            return False
        self.__time_format = time_format.upper()
        return True

    # Estático: la respuesta depende solo del formato recibido, no de un objeto.
    @staticmethod
    def __is_24hour_format(time_format: str) -> bool:
        """Indica si el formato recibido representa 24 horas."""
        return isinstance(time_format, str) and time_format.upper() == "24 HOURS"

    # Estático: valida valores candidatos sin consultar ni modificar un objeto.
    @staticmethod
    def _is_valid_time(hours: int, minutes: int, seconds: int,
                       time_format: str) -> bool:
        """Valida enteros y rangos; rechaza booleanos, floats y formatos inválidos."""
        if not Time.is_valid_format(time_format):
            return False
        # bool hereda de int: type(...) is int excluye True y False.
        if not all(type(value) is int for value in (hours, minutes, seconds)):
            return False
        if not (0 <= minutes <= 59 and 0 <= seconds <= 59):
            return False
        if Time.__is_24hour_format(time_format):
            return 0 <= hours <= 23
        return 1 <= hours <= 12

    # Instancia: cambia el estado de una hora concreta.
    def set_time(self, hours: int, minutes: int, seconds: int,
                 time_format: str) -> bool:
        """Asigna todos los valores si son válidos; al fallar conserva el estado."""
        if not self._is_valid_time(hours, minutes, seconds, time_format):
            return False
        self.__assign_format(time_format)
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds
        return True

    # Instancia: devuelve datos pertenecientes al objeto receptor.
    def get_time(self) -> tuple[int, int, int, str]:
        """Devuelve (horas, minutos, segundos, formato) del objeto."""
        return self.hours, self.minutes, self.seconds, self.time_format

    # Clase: es un constructor alternativo; usa cls para crear la instancia.
    @classmethod
    def from_string(cls, time_string: str) -> Optional[Time]:
        """Construye una hora desde HH:MM:SS FORMATO o informa y devuelve None.

        Exige dos cifras por campo. Acepta AM/PM/24 HOURS sin distinguir
        mayúsculas y quita espacios exteriores. Valida toda la cadena.
        """
        if not isinstance(time_string, str):
            print("Entrada no válida: se requiere una cadena.")
            return None
        pattern = r"([0-9]{2}):([0-9]{2}):([0-9]{2}) (AM|PM|24 HOURS)\Z"
        match = re.match(pattern, time_string.strip(), flags=re.IGNORECASE)
        if match is None:
            print("Cadena no válida. Use HH:MM:SS AM, PM o 24 HOURS.")
            return None
        hours, minutes, seconds = (int(match.group(i)) for i in (1, 2, 3))
        time_format = match.group(4)
        if not cls._is_valid_time(hours, minutes, seconds, time_format):
            print("Hora no válida: alguno de sus valores está fuera de rango.")
            return None
        result = cls()
        result.set_time(hours, minutes, seconds, time_format)
        return result

    # Estático: valida un argumento con el catálogo fijo de formatos de Time.
    @staticmethod
    def is_valid_format(time_format: str) -> bool:
        """Comprueba AM, PM o 24 HOURS sin distinguir mayúsculas/minúsculas."""
        return isinstance(time_format, str) and time_format.upper() in Time.TIME_FORMATS

    # Clase: consulta el contador compartido, sin necesitar una instancia.
    @classmethod
    def get_time_count(cls) -> int:
        """Devuelve el total acumulado de objetos creados de la clase Time."""
        return cls.time_count


def format_time(time: Time) -> str:
    """Devuelve la hora formateada desde una función externa a la clase."""
    hours, minutes, seconds, time_format = time.get_time()
    return f"{hours:02d}:{minutes:02d}:{seconds:02d} {time_format}"


def main() -> None:
    """Gestiona una hora mediante un menú repetido hasta la opción 4."""
    current_time = Time()
    while True:
        print("\n1. Introducir una nueva hora")
        print("2. Visualizar hora")
        print("3. Crear una hora a partir de una cadena")
        print("4. Terminar")
        option = input("Opción: ").strip()
        if option == "1":
            try:
                hours = int(input("Horas: "))
                minutes = int(input("Minutos: "))
                seconds = int(input("Segundos: "))
            except ValueError:
                print("Horas, minutos y segundos deben ser enteros.")
                continue
            time_format = input("Formato (AM, PM o 24 HOURS): ").strip()
            if current_time.set_time(hours, minutes, seconds, time_format):
                print("Hora asignada:", format_time(current_time))
            else:
                print("Hora o formato inválidos. Se conserva la hora anterior.")
        elif option == "2":
            print("Hora:", format_time(current_time))
        elif option == "3":
            candidate = Time.from_string(input("Hora (HH:MM:SS FORMATO): "))
            if candidate is not None:
                current_time = candidate
                print("Hora creada:", format_time(current_time))
        elif option == "4":
            print("Fin del programa.")
            break
        else:
            print("Opción no válida. Elija de 1 a 4.")


if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print("\nPrograma terminado.")
