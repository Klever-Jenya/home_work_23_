from flask import request, Blueprint, jsonify
from marshmallow import ValidationError

from builder import build_query
from models import BatchRequestSchema

main_bp = Blueprint('main', __name__)



FILE_NAME = "data/apache_logs.txt"


@main_bp.route("/perform_query/", methods=["POST"])
def perform_query():
    # =TODO: Принять запрос от пользователя
    data = request.json

    # TODO: + Получить параметры query и file_name из request.args, - при ошибке вернуть ошибку 400
    # =TODO: обработать запрос, валидировать значения
    try:
        validated_data = BatchRequestSchema().load(data)  # сериализация через load загружаем данные в нашу схему
    except ValidationError as e:  # маршмелоу выкинет свою ошибку если не хватает какого-то параметра
        return jsonify(e.messages), 400

    # TODO: выполнить запрос
    """
    цикл по списку запроса: Схема Schema
    """

    result = None  # if data is None: prepared_data = read_file(file_name)
    for query in validated_data["queries"]:  #
        result = build_query(
            cmd=query["cmd"],
            value=query["value"],
            file_name=validated_data["file_name"],
            data=result  # перезаписываем результат. по цепочке
        )
    return jsonify(result)
