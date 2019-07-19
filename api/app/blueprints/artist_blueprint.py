from flask import request, Blueprint
from app.blueprints.base_blueprint import BaseBlueprint
from app.controllers.artist_controller import ArtistController

url_prefix = '{}/artist'.format(BaseBlueprint.base_url_prefix)
artist_blueprint = Blueprint('artist', __name__, url_prefix=url_prefix)
artist_controller = ArtistController(request)


@artist_blueprint.route('/', strict_slashes=False, methods=['POST'])
def create_artist():
    return artist_controller.create_artist()


@artist_blueprint.route('/', strict_slashes=False, methods=['GET'])
def list_artist():
    return artist_controller.get_artists()


@artist_blueprint.route('/<int:artist_id>/', strict_slashes=False, methods=['GET'])
def get_artist(artist_id):
    return artist_controller.get_artist(artist_id)


@artist_blueprint.route('/<int:artist_id>/', strict_slashes=False, methods=['PUT'])
def update_artist(artist_id):
    return artist_controller.update_artist(artist_id)


@artist_blueprint.route('<int:artist_id>/', strict_slashes=False, methods=['DELETE'])
def delete_artist(artist_id):
    return artist_controller.delete_artist(artist_id)
