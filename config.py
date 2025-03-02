import os
# test
class Config:
  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL').replace('postgres://', 'postgresql://') if os.environ.get('DATABASE_URL') else 'sqlite:///:memory:'
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  
  # Map center coordinates
  MAP_CENTER = [0, 0]

  # Default map zoom, range 0-18
  MAP_ZOOM = 2
