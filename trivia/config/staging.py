from .base import *


ALLOWED_HOSTS += ['13.127.237.253', 'ec2-13-127-237-253.ap-south-1.compute.amazonaws.com']

STATIC_ROOT = os.path.abspath(os.path.join(PROJECT_PATH, STATIC_PATH))
# MEDIA_ROOT = os.path.abspath(os.path.join(PROJECT_PATH, MEDIA_PATH))

CORS_ORIGIN_WHITELIST = (
    'localhost:4200',
    '127.0.0.1:4200'
)
CORS_ORIGIN_ALLOW_ALL = True
