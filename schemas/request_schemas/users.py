from marshmallow import fields

from schemas.base import UserRequestBase


class UserRegisterRequestSchema(UserRequestBase):
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
    phone = fields.String(required=True)
    iban = fields.String(required=True, min_length=22, max_length=22)


class UserLoginRequestSchema(UserRequestBase):
    pass
