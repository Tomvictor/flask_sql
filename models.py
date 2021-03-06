from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import JSON, VARCHAR

db = SQLAlchemy()


class ModelSupportMixin:

    def as_dict(self):
        return {}

class Organization(db.Model,ModelSupportMixin):
    __tablename__ = 'organization'
    identifier = db.Column(VARCHAR(length=36), primary_key=True, index=True, nullable=False)

    doc = db.Column(JSON(), nullable=False)
    created = db.Column(db.DateTime, server_default=db.func.now())
    name = db.Column(VARCHAR(length=128), nullable=False)
    address_line = db.Column(VARCHAR(length=128), nullable=False)
    city = db.Column(VARCHAR(length=64), nullable=False)
    state = db.Column(VARCHAR(length=64), nullable=False)
    country = db.Column(VARCHAR(length=64), nullable=False)
    zip = db.Column(VARCHAR(length=64), nullable=False)
    phone = db.Column(VARCHAR(length=64), nullable=False)
    last_updated = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def as_dict(self):
        serialized_data = self.doc
        serialized_data["created"] = self.created
        serialized_data["last_updated"] = self.last_updated
        return serialized_data
