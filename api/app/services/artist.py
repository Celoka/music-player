from app.services.base_service import BaseService
from app.models.artist import Artist


class ArtistService(BaseService):

    def __init__(self):
        BaseService.__init__(self, Artist)
    
    def create_artist(self, artist_name, date_of_birth):
        artist = Artist(artist_name=artist_name, date_of_birth=date_of_birth)
        artist.save()
        return artist
