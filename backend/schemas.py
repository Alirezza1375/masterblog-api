from marshmallow import Schema, fields, ValidationError, validates, INCLUDE, validate


class PostSchema(Schema):
    title = fields.String(required=True, validate=validate.Length(min=1))
    content = fields.String(required=True, validate=validate.Length(min=1))
    author = fields.String(required=True, validate=validate.Length(min=1))


class PostUpdateSchema(Schema):
    title = fields.String(required=False, validate=validate.Length(min=1))
    content = fields.String(required=False, validate=validate.Length(min=1))
    author = fields.String(required=False, validate=validate.Length(min=1))

    class Meta:
        unknown = INCLUDE

    def validate(self, data, **kwargs):
        """Custom validation to ensure at least one field is provided and non-empty."""
        if not (data.get('title') or data.get('content') or data.get('author')):
            raise ValidationError("At least one field must be provided and non-empty.",
                                  field_names=['title', 'content', 'author'])
        return data


class QueryParamSchema(Schema):
    sort = fields.String(required=False)
    direction = fields.String(required=False)

    @validates('sort')
    def validate_sort(self, value):
        sort_permissible_values = ['title', 'content', 'id', 'author', 'date']
        if value not in sort_permissible_values:
            raise ValidationError("Invalid direction value: {value}. Expected values: {direction_permissible_values}")
