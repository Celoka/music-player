from .base_model import BaseModel, db


class Artist(BaseModel):
    __tablename__="artists"

    artist_name = db.Column(db.String(120), nullable=False)
    date_of_birth = db.Column(db.Date(), nullable=False)
    artist_music = db.relationship('Song', lazy=False)
