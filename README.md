
# TODO  cat otherfile | grep 'something'
# Данная запись выводит все содержимое файла otherfile (cat otherfile),
# а затем ищет в нем строки, которые содержат something (grep 'something').

### Задание

# Сделать веб-сервер на flask, который
# 1) “повторяет” функционал командной строки линукса для обработки файлов.
# 2) состоит из одного POST метода. Метод должен удовлетворять следующим требованиям:
#
# + 1. Доступен по пути /perform_query
# 2. Принимает 5 параметров: где 1, 2, 3, 4 - запрос, 5-ый - имя файла.
# Ссылка на [примеры запросов](https://gist.github.com/alexopryshko/4f5264eac09a46a368ac16add1a9e0dc)
# 3. Метод должен искать файлы внутри директории data. Папка data должна находиться в одной папке с веб-сервером.
# 4. Обрабатывать файл, следуя написанному запросу, и возвращать ответ клиенту




import requests

url = "http://127.0.0.1:5000/perform_query"
payload={
  'file_name': 'apache_logs.txt',
  'cmd1': 'filter',
  'value1': 'GET',
  'cmd2': 'map',
  'value2': '0'
}
payload={
  "file_name": "apache_logs.txt",
  "cmd1": "map",
  "value1": "0",
  "cmd2": "unique",
  "value2": ""
}

response = requests.request("POST", url, data=payload)
print(response.text)