from django.conf.urls import url
from . import views

app_name = 'movie'

urlpatterns = [
    # /music/
    url(r'^$',views.index,name='index'),

    #/music/712/
    url(r'^(?P<movie_id>[0-9]+)/$',views.detail,name = 'detail'),

    #/music/<movie_id>/favorite/
    url(r'^(?P<movie_id>[0-9]+)/favorite/$',views.favorite,name = 'favorite'),
]
