from marshmallow import Schema, fields, validates_schema, ValidationError, validate

VALID_CMD_COMMANDS = ("filter", "unique", "map", "limit", "sort")

"""
валидируем строчками
типизация страдает (подсвечивается)
"""


class RequestSchema(Schema):
    cmd = fields.Str(required=True, validate=validate.OneOf(VALID_CMD_COMMANDS))
    value = fields.Str(required=True)

    # @validates_schema
    # def check_all_cmd_valid(self, value: dict[str, str], *args, **kwargs):
    #     if value["cmd"] not in VALID_CMD_COMMANDS:
    #         raise ValidationError('"cmd" contains invalid value')


"""
вложенная схема
Batch - Пачка
"""


class BatchRequestSchema(Schema):
    queries = fields.Nested(RequestSchema, many=True)
    file_name = fields.Str(required=True)
