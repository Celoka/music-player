from app.services.base_service import BaseService
from app.models.song import Song


class SongService(BaseService):

    def __init__(self):
        BaseService.__init__(self, Song)
    
    def create_song(self, artist_id, title, genre, album_name, album_art, release_date):
        song = Song(artist_id=artist_id, title=title,genre=genre, 
                    album_name=album_name, album_art=album_art,
                    release_date=release_date)
        song.save()
        return song
