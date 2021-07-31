
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
     path("", views.index, name="homepage"),
     path("about", views.about, name="about"),
     path("service", views.service, name="service")
]
