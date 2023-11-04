from django.urls import path
from .views import *

urlpatterns=[
    path('movies', AllMovies, name='movies_list_url'),
    path('movie/<int:movie_id>', MoviesById, name='movie_by_id_url'),
    path('movie', MoviesByGenres, name='movie_by_genre'),
    path('movie/create', MovieCreate, name='movie_create'),
    path('movie/update/<int:movie_id>', MovieUpdate, name='movie_update'),
    path('movie/delete/<int:movie_id>', MovieDelete, name='movie_delete_url')
]