from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Song, VideoQuery, Choices, ActualSong

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("id", "username")

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "password")

class SongSerializers(serializers.ModelSerializer):

    class Meta:
        model = Song
        fields = ("video", "name", "author", "duration_video", "id", )

class VideoQuerySerializers(serializers.ModelSerializer):
    selected_video = SongSerializers()
    class Meta:
        model = VideoQuery
        fields = ("selection_time", "selected_video", "user_choices", "id",)

class VideoQueryPostSerializers(serializers.ModelSerializer):
    selected_video = SongSerializers()
    class Meta:
        model = VideoQuery
        fields = ("selected_video", )

class ChoicesSerializers(serializers.ModelSerializer):
    VideoInQuery = VideoQuerySerializers()
    voted_user = UserSerializer()
    class Meta:
        model = Choices
        fields = ("VideoInQuery", "voted_user", "voted_time", )

class ActualSongSerializers(serializers.ModelSerializer):
    video = SongSerializers()
    class Meta:
        model = ActualSong
        fields = ("video", "time_duration",)