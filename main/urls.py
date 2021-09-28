from main.views import main, makePost
from django.urls import path

urlpatterns = [
    path("", main, name="main"),
    path("makePost/", makePost, name="makePost")
]