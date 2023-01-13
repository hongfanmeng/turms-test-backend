from .common import Common


class Dev(Common):
    DEBUG = True
    ALLOWED_HOSTS = ["*"]
    CORS_ALLOW_ALL_ORIGINS = True
