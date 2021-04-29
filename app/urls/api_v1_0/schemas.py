from marshmallow import fields, validate, ValidationError
from app.ext import ma

class UrlSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    created = fields.DateTime(format='%Y-%m-%dT%H:%M:%S%z', dump_only=True)
    original_url = fields.String(validate=validate.URL(), required=True)
    clicks = fields.Integer(dump_only=True)