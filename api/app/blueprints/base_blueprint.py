
class BaseBlueprint:
    base_url_prefix = '/api/v1'

    def __init__(self, app):
        self.app = app

    def register(self):
        """All Blueprints are registered here"""
        from app.blueprints.user_blueprint import user_blueprint
        from app.blueprints.artist_blueprint import artist_blueprint
        from app.blueprints.song_blueprint import song_blueprint
        from app.blueprints.home_blueprint import home_blueprint


        self.app.register_blueprint(user_blueprint)
        self.app.register_blueprint(artist_blueprint)
        self.app.register_blueprint(song_blueprint)
        self.app.register_blueprint(home_blueprint)
