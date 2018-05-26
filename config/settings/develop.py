# config/settings/develop.py
import os

from .common import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/


# SECURITY WARNING: don"t run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

THIRD_PARTY_APPS_LOCAL = (
    "django_extensions",
)

INSTALLED_APPS += THIRD_PARTY_APPS_LOCAL

# Django Rest Framework CORS configuration
CORS_ORIGIN_ALLOW_ALL = True

# Graph models conf
GRAPH_MODELS = {
    "all_applications": True,
    "group_models": True,
}
