from marshmallow import fields

from schemas.base import ComplaintBaseSchema


class ComplaintRequestSchema(ComplaintBaseSchema):
    photo = fields.Str(required=True)
    extension = fields.Str(required=True)

