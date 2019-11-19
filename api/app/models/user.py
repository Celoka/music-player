from .base_model import BaseModel, db


class UserModel(BaseModel):
    __tablename__ = "users"

    first_name = db.Column(db.String(120), nullable=False)
    last_name = db.Column(db.String(120), nullable=False)
    email_address = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(750), nullable=False)
