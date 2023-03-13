from marshmallow import Schema, fields


class UserAuthResponseSchema(Schema):
    token = fields.Str(required=True)
