from main.views import delete, makePost, newPost, main, register, signin, signout
from django.urls import path

urlpatterns = [
    path("", main, name = "main"),
    path("newPost/makePost/", makePost, name = "makePost"),
    path("newPost/", newPost, name = "newPost"),
    path("delete/<int:id>", delete, name = "delete"),
    path("register", register, name = "register"),
    path("signin", signin, name = "signin"),
    path("signout", signout, name = "signout"),
]