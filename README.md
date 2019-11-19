# Music Player
This repository contains the source code of Music Player, an app built using Flask and React where users can create music artists profile. This enables users to visit the application and perform basic CRUD. The users will have a level of authorization before they can perform some of the operations. 

### Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites
For Backend:
- Clone this repository https://github.com/Celoka/music-player.git and cd into `music-player` directory

- Install pip if it is not installed yet in your system

- To install virtual environment, run in your terminal:

  `pip install virtualenv`

- To create a virtual environment, in the root folder of the cloned app, run: `virtualenv -p python3 venv`
- To activate the virtualenv: source venv/bin/activate
- Run the command below to install all the project dependencies: `pip install -r requirements.txt`
- Create a .env file, copy the variables in the .env_sample in the root directory of the project and set up the configurations according to your system.
- To initialise flask and create migrations change into `api` directory and run: `flask db init` `flask db upgrade` `flask db migrate`
- To start the server: `python run.py runserver`
- To deactivate the virtualenv, run the command below: deactivate

For Frontend:
- Change into `frontend` directory and run the command: `npm install`
- To start the app, run: `npm start`

### Features of the Project
- User Registration
- User Login
- User Upload Passport Photo
- User create artist
- User get one/all artist(s)
- User edit artist
- User delete artist
- User create song
- User get one/all song(s)
- User edit song
- User delete song

### Built With
- Python 3
- Flask
- React
- Docker

Authors
Eloka Chima
