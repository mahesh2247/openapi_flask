from flask_marshmallow import Marshmallow
ma = Marshmallow()

class PeopleSchema(ma.Schema):
    class Meta:
        fields = (
            'fname',
            'lname'
        )