import os

class Config:
  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL').replace('postgres://', 'postgresql://') if os.environ.get('DATABASE_URL') else 'sqlite:///:memory:'
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  MAP_CENTER = [50, 15]
  MAP_ZOOM = 7
