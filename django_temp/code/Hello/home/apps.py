from django.apps import AppConfig
from django.http import response


class HomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'

def homepage():
    return response("we are in home page")


