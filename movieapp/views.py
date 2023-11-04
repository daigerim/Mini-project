from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.shortcuts import render
from .models import *

# Create your views here.
def AllMovies(request):
    movies = Movie.objects.all()
    context = {
        'message': 'You can see all the movies below:',
        'movies': movies
    }
    return render(request, 'movies_list.html', context)

def MoviesById(request, movie_id):
    try:
        movie = Movie.objects.get(id=movie_id)
        genres = movie.genre.all()  # Retrieve all genres associated with the movie
        context = {
            'movie': movie,
            'genres': genres
        }
        return render(request, 'movie_by_id.html', context)
    except Movie.DoesNotExist:
        return HttpResponse("Movie not found", status=404)

def MoviesByGenres(request):
    genre = request.GET.get('genre')
    print(genre)
    if genre is not None:
        movies = Movie.objects.filter(genre__name=genre)
    else:
        movies = Movie.objects.all()
    context = {
        'movies': movies
    }
    return render(request=request, template_name='movies_genre.html', context=context)

def MovieCreate(request):
    if request.method=='GET':
        movies = Movie.objects.all()
        context = {
            'movies': movies
        }
        return render(request=request, template_name='movie_create.html', context=context)
    elif request.method == 'POST':
        title = request.POST.get('title').capitalize()
        director = request.POST.get('director').capitalize()
        release_year = request.POST.get('release_year')
        genre = request.POST.get('genre')
        poster = request.FILES.get('poster')
        description = request.POST.get('description')
        uploaded_by = request.user

        genre, created = Genre.objects.get_or_create(name=genre)

        movie = Movie(
            title=title,
            director=director,
            release_year=release_year,
            poster=poster,
            description=description,
            uploaded_by=uploaded_by
        )
        movie.save()
        movie.genre.add(genre)
        return redirect('movies_list_url')

def MovieUpdate(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    if request.method == 'GET':
        context = {
            'movie': movie
        }
        return render(request=request, template_name='movie_update.html', context=context)
    elif request.method == 'POST':
        movie.title = request.POST.get('title').capitalize()
        movie.director = request.POST.get('director').capitalize()
        movie.release_year = request.POST.get('release_year')
        genre = request.POST.get('genre')
        movie.poster = request.FILES.get('poster')
        movie.description = request.POST.get('description')
        movie.uploaded_by = request.user

        genre, created = Genre.objects.get_or_create(name=genre)

        movie.save()
        movie.genre.clear()
        movie.genre.add(genre)
        return redirect('movies_list_url')

def MovieDelete(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    if request.method == 'GET':
        context = {
            'movie': movie
        }
        return render(request=request, template_name='movie_delete.html', context=context)
    elif request.method == 'POST':
        movie.delete()
        return redirect('movies_list_url')
