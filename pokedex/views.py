from django.shortcuts import render

def index(request):
    pokemons = ["Pikachu", "Charmander", "Bulbasaur", "Squirtle", "Eevee"]
    return render(request, "index.html", {"pokemons": pokemons})

def pokemons_details(request, nombre):
    return render(request, "details.html", {"nombre": nombre})