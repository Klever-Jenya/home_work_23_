from typing import Iterable, Iterator, Any, Set, List
import re


def filter_query(value: str, data: Iterable[str]) -> Iterator[str]:
    # Iterable[str] перечисляемое со строчками; Iterator[str] итератор строчек
    return filter(lambda x: value in x, data)  # проверяем что value есть в этой строке из файла


def unique_query(data: Iterable[str], *args: Any, **kwargs: Any) -> Set[str]:
    # **kwargs именованные аргументы (т.к. value тут не используется); Set[str] сет строчек
    return set(data)


def limit_query(value: str, data: Iterable[str]) -> List[str]:
    limit: int = int(value)
    return list(data)[:limit]


def map_query(value: str, data: Iterable[str]) -> Iterator[
    str]:  # берем колонку, сплитуем по пробелам, берем нужный номер колонки
    col_number = int(value)
    return map(lambda x: x.split(" ")[col_number], data)


def sort_query(value: str, data: Iterable[str]) -> List[str]:
    reverse = value == "desc"  # bool равняется ли value = desc
    return sorted(data, reverse=reverse)


# TODO: Усовершенствовать язык программирования и добавить команду — regex.
def regex_query(value: str, data: Iterable[str]) -> Iterator[str]:  # : Iterable[str]
    pattern = re.compile(value)
    return filter(lambda x: re.search(pattern, x), data)

