from flask import request, Blueprint
from app.blueprints.base_blueprint import BaseBlueprint
from app.controllers.song_controller import SongController

url_prefix = '{}/song'.format(BaseBlueprint.base_url_prefix)
song_blueprint = Blueprint('song', __name__, url_prefix=url_prefix)
song_controller = SongController(request)


@song_blueprint.route('/', strict_slashes=False, methods=['POST'])
def create_song():
    return song_controller.create_song()


@song_blueprint.route('/', strict_slashes=False, methods=['GET'])
def list_song():
    return song_controller.list_song()


@song_blueprint.route('/<int:song_id>/upload', strict_slashes=False, methods=['POST'])
def upload_album_art(song_id):
    return song_controller.upload_image(song_id)


@song_blueprint.route('/<int:song_id>/', strict_slashes=False, methods=['GET'])
def get_song(song_id):
    return song_controller.get_song(song_id)


@song_blueprint.route('/<int:song_id>/', strict_slashes=False, methods=['PUT'])
def update_song(song_id):
    return song_controller.update_song(song_id)


@song_blueprint.route('/<int:song_id>/', strict_slashes=False, methods=['DELETE'])
def delete_song(song_id):
    return song_controller.delete_song(song_id)
