from app.controllers.base_controller import BaseController
from app.services.artist import ArtistService
from app.utils.helper import conflict_handler

class ArtistController(BaseController):
    def __init__(self, request):
        BaseController.__init__(self, request)
        self.artist_service = ArtistService()

    def create_artist(self):
        artist_name, date_of_birth = self.request_params(
            'artistName', 'dateOfBirth')
        artist = self.artist_service.filter_first(
            **{'artist_name': artist_name})
        if artist:
            msg = "Artist with name already exists."
            return self.handle_response("Incomplete Request", conflict_handler(msg,'ArtistName: '+artist_name), status_code=409)
        artist = self.artist_service.create_artist(artist_name, date_of_birth)
        return self.handle_response('Ok', payload={'artist': artist.serialize()}, status_code=201)

    def get_artists(self):
        artists = self.artist_service.filter_by(**{'is_deleted': 'false'})
        artist_list = [artist.serialize() for artist in artists.items]
        return self.handle_response('Ok', payload={'artist': artist_list})

    def get_artist(self, artist_id):
        artist = self.artist_service.get(artist_id)
        if artist:
            artist = artist.serialize()
            return self.handle_response('Ok', payload={'artist': artist})
        else:
            return self.handle_response('Artist does not exist or missing artist_id', status_code=400)

    def update_artist(self, artist_id):
        artist_name, date_of_birth = self.request_params(
            'artistName', 'dateOfBirth')
        artist = self.artist_service.get(artist_id)
        if artist:
            data = {}
            if artist_name:
                data['artist_name'] = artist_name
            if date_of_birth:
                data['date_of_birth'] = date_of_birth
            self.artist_service.update(artist, **data)
            return self.handle_response('Ok', payload={'status': 'Updated!', 'artist': artist.serialize()})
        return self.handle_response('Invalid or Incorrect artist_id given', status_code=400)

    def delete_artist(self, artist_id):
        artist = self.artist_service.get(artist_id)
        data = {}
        if artist:
            data['is_deleted'] = True
            self.artist_service.update(artist, **data)
            return self.handle_response('Ok', payload={'status': 'Deleted!'})
        return self.handle_response('Invalid or incorrect artist_id', status_code=400)
