from .base_model import BaseModel, db
from app.utils.enum import SongGenre


class Song(BaseModel):
    __tablename__ = "songs"

    artist_id = db.Column(db.Integer(), db.ForeignKey('artists.id'), nullable=False)
    genre = db.Column(db.Enum(SongGenre), default="General", nullable=False)
    title = db.Column(db.String(120), nullable=False)
    album_name = db.Column(db.String(120), nullable=False)
    album_art = db.Column(db.String(1000))
    release_date = db.Column(db.Date(), nullable=False)
    artist_music = db.relationship('Artist', lazy=False)
