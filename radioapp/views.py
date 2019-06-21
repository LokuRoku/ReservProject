from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from .models import Song, ActualSong, Choices, VideoQuery, User
from .serializers import SongSerializers, VideoQuerySerializers, ChoicesSerializers, ActualSongSerializers, VideoQueryPostSerializers, UserCreateSerializer
from django.utils import timezone

# Create your views here.
class SongView(APIView):
    permission_classes = [permissions.IsAuthenticated, ]
    def get(self, request):
        letter = request.GET.get("letter")
        if (letter == "0-9"):
            songs = Song.objects.filter(name__regex=r'\d*').order_by('name')
        else:
            songs = Song.objects.filter(name__istartswith=letter).order_by('name')
        serializers = SongSerializers(songs, many=True)
        return Response({'data': serializers.data})

class VideoQueryView(APIView):
    permission_classes = [permissions.IsAuthenticated, ]
    # permission_classes = [permissions.AllowAny, ]
    def get(self, request):
        songquery = VideoQuery.objects.order_by('-user_choices', 'selection_time')[:5]
        serializer = VideoQuerySerializers(songquery, many=True)
        return Response({'data': serializer.data})

    def post(self, request):
        song = request.data.get("song")
        try:
            videoquery = VideoQuery.objects.get(id=song)
            videoquery.user_choices += 1
            videoquery.save()
            choice_user = Choices.objects.create(VideoInQuery=videoquery, voted_user=request.user)
            return Response(status=201)
            # choice = Choices.objects.filter(voted_user=request.user)
            # if choice.count() == 0:
            #     songquery = Choices.objects.get(selected_video=videoquery.selected_video)
            #     videoquery.save(user_choices=songquery.user_choices+1)
            #     choice = Choices.objects.create(VideoInQuery=songquery, voted_user=request.user)
            #     return Response(status=201)
            # else:
            #     return Response(status=400)
        except:
            return Response(status=400)


class ChoseUsers(APIView):
    def get(self, request):
        user = request.GET.get("user")
        chosing = Choices.objects.filter(user=user)
        serializer = ChoicesSerializers(chosing, many=True)
        return Response({'data': serializer.data})

class GetServerTimeData(APIView):
    permission_classes = [permissions.IsAuthenticated, ]
    def get(self, request):
        newsong = ActualSong.objects.all()[:1]
        now = timezone.now()
        then = timezone.now()
        duration = 0
        if newsong.count()>0:
            duration = newsong[0].time_duration
            then = newsong[0].selection_time
        delta = now - then
        delta = delta.seconds
        if delta >= duration:
            if newsong.count() > 0:
                newsong[0].delete()
            songquery = VideoQuery.objects.order_by('-user_choices', 'selection_time')[:1]
            if songquery.count() > 0:
                duration = songquery[0].selected_video.duration_video
                newsong = ActualSong.objects.create(video=songquery[0].selected_video, time_duration=duration)
                newsong.save()
                songquery[0].delete()
                return Response(str(duration))
            else:
                return Response(str(0))
        else:
            return Response(str(duration - delta))


class ActualSongView(APIView):
    permission_classes = [permissions.AllowAny, ]
    def get(self, request):
        newsong = ActualSong.objects.all()
        serializer = ActualSongSerializers(newsong, many=True)
        return Response({'data': serializer.data})

class postSongInQueue(APIView):
    permission_classes = [permissions.IsAuthenticated, ]
    def post(self, request):
        song = request.data.get("song")
        try:
            videoquery = Song.objects.get(id=song)
            queuesong = VideoQuery.objects.create(selected_video=videoquery, user_choices=1)
            choice_user = Choices.objects.create(VideoInQuery=queuesong, voted_user=request.user)
            return Response(status=201)
        except:
            return Response(status=201)

class UserCreateView(APIView):
    permission_classes = [permissions.AllowAny, ]
    def post(self, request):
        username=request.data.get("username")
        passwd=request.data.get("password")
        try:
            user = User.objects.create_user(username, None, passwd)
            return Response(status=201)
        except:
            return Response(status=400)

