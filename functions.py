from typing import Iterable


def filter_query(value: str, data: Iterable[str]):  # Iterable[str] перечисляемое со строчками
    return filter(lambda x: value in x, data)  # проверяем что value есть в этой строке из файла


def unique_query(data, *args, **kwargs):  # **kwargs именованные аргументы (т.к. value тут не используется)
    return set(data)


def limit_query(value, data):
    limit: int = int(value)
    return list(data)[:limit]


"""
берем колонку, сплитуем по пробелам , берем нужный номер колонки
"""


def map_query(value, data):
    col_number = int(value)
    return map(lambda x: x.split(" ")[col_number], data)


def sort_query(value, data):
    reverse = value == "desc"  # bool равняется ли value = desc
    return sorted(data, reverse=reverse)
