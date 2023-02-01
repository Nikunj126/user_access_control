from .db import db


class role_db(db.Document):
    user = db.StringField(required=True, unique=True)
    role_type = db.StringField(required=True, choices=["USER", "ADMIN", "MASTERADMIN"])


class employee_db(db.Document):
    name = db.StringField(required=True)
    skills = db.ListField(db.StringField(), required=True)
    team = db.StringField(required=True)

