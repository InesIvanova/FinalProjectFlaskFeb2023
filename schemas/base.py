from marshmallow import Schema, fields


class UserRequestBase(Schema):
    email = fields.Email(required=True)
    password = fields.String(required=True)


class ComplaintBaseSchema(Schema):
    title = fields.Str(required=True)
    description = fields.Str(required=True)
    photo_url = fields.Str(required=True)
    amount = fields.Float(required=True)
