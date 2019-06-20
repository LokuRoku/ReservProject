from .views import SongView, VideoQueryView, GetServerTimeData, ActualSongView, ChoseUsers, postSongInQueue, UserCreateView
from django.urls import path, include

urlpatterns = [
    path("songs/", SongView.as_view()),
    path("songquery/", VideoQueryView.as_view()),
    path("servertime/", GetServerTimeData.as_view()),
    path("actualvideo/", ActualSongView.as_view()),
    path("chosinguser/", ChoseUsers.as_view()),
    path("addsong/", postSongInQueue.as_view()),
    path("createuser/", UserCreateView.as_view()),
]