#Takes the request and sends back an HTTP response from Django HTTP

from django.http import HttpResponse
from .models import Movie, themeSong
from django.shortcuts import render, get_object_or_404
#from django.http import Http404
#from django.template import loader

# def index(request): #Connect to database and have all movie and make a link and display in http response
#     all_movies = Movie.objects.all()
#     html = ''
#     for movie in all_movies:
#         url = '/movie/' + str(movie.id) + '/'
#         html += '<a href="' + url + '">' + movie.movie_title + '</a><br>'
#     return HttpResponse(html)

def index(request):
    all_movies = Movie.objects.all()
    #template = loader.get_template('movie/index.html') #template file is referenced to index.html file

    context = {
        "all_movies":all_movies,
    }
    return render(request,'movie/index.html',context) #http response already included by render

# def detail(request, movie_id):
#     return HttpResponse("<h2>Details for Movie id: " + str(movie_id) + "</h2>")

def detail(request, movie_id):
    # try:
    #     movie = Movie.objects.get(id = movie_id)
    # except Movie.DoesNotExist:
    #     raise Http404("Movie does not exist")
    movie = get_object_or_404(Movie, pk = movie_id)
    return render(request, 'movie/detail.html', {"movie":movie})

def favorite(request, movie_id):
    movie = get_object_or_404(Movie, pk = movie_id)
    try:
        selected_song = movie.themesong_set.get(pk=request.POST['song'])
    except(KeyError, themeSong.DoesNptExist):
        return render(request, 'movie/detail.html', {'movie': movie, 'error_message': "You did not select a valid song",})
    else:
        selected_song.is_favorite = True
        selected_song.save()
        return render(request, 'movie/detail.html', {"movie":movie})