import os

BASE_DIR = os.path.dirname(__file__)
print("BASE_DIR = "+str(BASE_DIR))
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
print("SQLALCHEMY_DATABASE_URI = "+str(SQLALCHEMY_DATABASE_URI))

SECRET_KEY = "dev"