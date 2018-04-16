from .base import *



STATIC_ROOT = os.path.abspath(os.path.join(PROJECT_PATH, STATIC_PATH))
# MEDIA_ROOT = os.path.abspath(os.path.join(PROJECT_PATH, MEDIA_PATH))

ALLOWED_HOSTS += ['13.127.237.253', 'ec2-13-127-237-253.ap-south-1.compute.amazonaws.com',
                  'localhost']

CORS_ORIGIN_WHITELIST = (
    'localhost:4200',
    '127.0.0.1:4200'
)
