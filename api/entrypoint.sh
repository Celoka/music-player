#!/usr/bin/env bash

export FLASK_CONFIG=development
export SECRET_KEY=key
export APP_ENV=development
export FLASK_ENV=development
export FLASK_APP=run.py
python run.py db migrate
python run.py db upgrade
python run.py runserver -h 0.0.0.0
