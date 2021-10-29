from config.default import *

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'\x0f\xbdn\x01\xac\x90\xb8\x04\xd4\x9f\xf9\xcc\x0b\xd5\xf4\xb4'
