import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))
# Enable debug mode.
DEBUG = True
# Connect to the database
MONGODB_DB = 'netflixMedia'
MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017
#MONGODB_USERNAME = 'webapp'
#MONGODB_PASSWORD = '27017'