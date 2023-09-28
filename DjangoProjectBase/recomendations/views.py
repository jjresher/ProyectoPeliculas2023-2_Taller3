from django.shortcuts import render
from movie.models import Movie

# Create your views here.

def recomendations(request):
    searchTerm = request.GET.get('searchMovie')
    if searchTerm: 
       movies = Movie.objects.filter(title__icontains=searchTerm) 
    else: 
        movies = Movie.objects.all()
    return render(request, 'recomendations.html', {'searchTerm':searchTerm, 'movies': movies})