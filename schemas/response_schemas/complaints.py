from marshmallow import fields, Schema

from models import State
from schemas.base import ComplaintBaseSchema


class ComplaintResponseSchema(ComplaintBaseSchema):
    id = fields.Integer(required=True)
    created_at = fields.DateTime(required=True)
    status = fields.Enum(State, by_value=True)
    user_id = fields.Integer(required=True)
    # Todo: nest user inside this schema


class ComplaintsResponseSchema(Schema):
    # TODO: make schema working without list ofComplaints schema
    complains = fields.Nested(ComplaintResponseSchema, many=True)
