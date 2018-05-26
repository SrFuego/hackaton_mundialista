# config/settings/staging.py
from .common import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# TODO: production
# complete allowed hosts
ALLOWED_HOSTS = ["*"]

# Django Rest Framework CORS configuration
# TODO: production
# complete cors origin whitelist
# delete CORS_ORIGIN_ALLOW_ALL (default=False)
CORS_ORIGIN_ALLOW_ALL = True

# CORS_ORIGIN_WHITELIST = (
#     "google.com",
#     "hostname.example.com",
#     "localhost:8000",
#     "127.0.0.1:9000",)
