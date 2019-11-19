import os
from werkzeug.utils import secure_filename
from app.controllers.base_controller import BaseController
from app.services.song import SongService
from app.services.artist import ArtistService
from app.utils.helper import conflict_handler


UPLOAD_PATH = './app/uploads'
FILE_TYPE = set(['png', 'jpg', 'jpeg'])
enum_values = ['Afro beats', 'Jazz', 'Rock', 'Folk music', 'Blues', 'Rythm and blues', 'Pop music', 'Country music', 'Hip hop music',
               'Musical theatre', 'Classical music', 'Popular music', 'Funk', 'Raggae', 'Punk rock', 'Heavy metal', 'Dance music', 'Techno']


class SongController(BaseController):
    def __init__(self, request):
        BaseController.__init__(self, request)
        self.song_service = SongService()
        self.artist_service = ArtistService()

    def create_song(self):
        artist_name, title, genre, album_name, album_art, release_date = self.request_params(
            'artistName', 'title', 'genre', 'album_name', 'album_art', 'release_date'
        )
        if genre not in enum_values:
            return self.handle_response('Invalid Genre.', status_code=404)
        artist = self.artist_service.filter_first(**{'artist_name': artist_name})
        song = self.song_service.filter_first(**{'title': title})

        if not artist:
            return self.handle_response('Artist does not exist', status_code=404)
        if song:
            msg = "The song with the title Already exists. You cannot create another song with the same title"
            return self.handle_response("Incomplete Request",conflict_handler(msg,'Song Title: '+title), status_code=409)
        song = self.song_service.create_song(artist.id, title, genre, album_name, album_art, release_date)
        return self.handle_response('Ok', payload={'song': song.serialize()})

    def list_song(self):
        songs = self.song_service.filter_by(**{'is_deleted': 'false'})
        song_list = [song.serialize() for song in songs.items]
        return self.handle_response('Ok', payload={'song': song_list})
    
    def _allowed_file(self, filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in FILE_TYPE

    def upload_image(self, song_id):
        data = {}
        song = self.song_service.get(song_id)
        if song:
            if 'file' not in self.request.files:
                return self.handle_response('File not included', status_code=400)
            file = self.request.files['file']
            if file.filename == '':
                return self.handle_response('File not selected', status_code=400)
            if file and self._allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(UPLOAD_PATH, filename))
                data['album_art'] = os.path.join(UPLOAD_PATH, filename)
                self.song_service.update(song, **data)
                return self.handle_response('OK')
            return self.handle_response('Invalid file type', status_code=400)
        return self.handle_response('Song Id is not valid', status_code=400)
           
    def get_song(self, song_id):
        song = self.song_service.get(song_id)
        if song:
            song = song.serialize()
            return self.handle_response('Ok', payload={'song': song})
        else:
            return self.handle_response('Song does not exist or missing song_id', status_code=400)

    def update_song(self, song_id):
        artist_name, title, genre, album_name, album_art, release_date = self.request_params(
            'artistName', 'title', 'genre', 'album_name', 'album_art', 'release_date'
        )
        artist = self.artist_service.filter_first(**{'artist_name': artist_name})
        if not artist:
            return self.handle_response('This field cannot be edited.', status_code=400)
        artist_id = artist.id
        song = self.song_service.get(song_id)
        if song:
            data = {}
            if title:
                data['title'] = title
            if genre:
                data['genre'] = genre
            if album_name:
                data['album_name'] = album_name
            if album_art:
                data['album_art'] = album_art
            if release_date:
                data['release_date'] = release_date
            self.song_service.update(song, **data)
            return self.handle_response('Ok', payload={'status': 'Updated!', 'song': song.serialize()})
        return self.handle_response('Invalid or Incorrect song_id given', status_code=400)
    
    def delete_song(self, song_id):
        song = self.song_service.get(song_id)
        data = {}
        if song:
            data['is_deleted'] = True
            self.song_service.update(song, **data)
            return self.handle_response('Ok', payload={'status': 'Deleted!'})
        return self.handle_response('Invalid or incorrect song', status_code=400)
