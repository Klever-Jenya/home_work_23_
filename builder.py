import os
from typing import Optional, Iterator, Dict, Callable, List, Iterable

from flask import jsonify

from functions import filter_query, unique_query, limit_query, map_query, sort_query, regex_query

"""
преобразовывает запрос от пользователя в файл
прослойка между пользовательским JSON и файлом с данными и результатами
"""
# Callable - вызываемый объект, после которого можно поставить скобки и передать какие-то параметры
CMD_TO_FUNCTIONS: Dict[str, Callable] = {  # объекты функций без () (~ссылка на функцию)
    "filter": filter_query,
    "unique": unique_query,
    "limit": limit_query,
    "map": map_query,
    "sort": sort_query,
    "regex": regex_query
}


def read_file(file_name: str) -> Iterable[str]:
    if not os.path.exists(file_name):
        return jsonify({'error': 'Файл не найден'}), 400

    with open(file_name) as file:
        """
        читаем файл и делаем yield на каждую строчку
        читаем по строчно, не выгружая полностью
        большой файл в оперативную память может не войти
        """
        for line in file:
            yield line


def build_query(cmd: str, value: str, file_name: str, data: Optional[Iterable[str]]) -> List[str]:  # опционально итерируемые строки
    if data is None:
        prepared_data: Iterable[str] = read_file(file_name)  # если запрос первый в цепочке запросов, то читаем из файла
    else:
        prepared_data = data  # второй раз определять тип переменной не надо, MYPY будет ругаться
    return list(CMD_TO_FUNCTIONS[cmd](value=value, data=prepared_data))  # подставляя () мы уже вызываем эту функцию

 ## error: Cannot call function of unknown type  [operator]
