from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("pokemon/<str:nombre>/", views.pokemons_details, name="pokemon_details"),
]