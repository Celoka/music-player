import logging

from werkzeug.exceptions import HTTPException
from flask_script import Manager
from flask import jsonify, make_response
from flask_migrate import Migrate, MigrateCommand

from app import app, create_app
from app.utils import db
from app.utils.auth import Auth
from config import get_env

manager = Manager(app)
migrate = Migrate(app, db)

# Run migrations
manager.add_command('db', MigrateCommand)

@app.before_request
def check_token():
    return Auth.check_token()

@manager.command
def create_db():
    db.create_all()


@manager.command
def drop_db():
    db.drop_all()


if __name__ == "__main__":
    manager.run()
