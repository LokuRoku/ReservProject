from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from .models import Song, VideoQuery, Choices, ActualSong

class SongAdmin(AdminVideoMixin, admin.ModelAdmin):
    """Админка песен"""
    list_display = ("video", "name", "author", "duration_video")

admin.site.register(Song, SongAdmin)

class VideoQueryAdmin(admin.ModelAdmin):
    """Админка очереди"""
    list_display = ("selection_time", "selected_video", "user_choices")

admin.site.register(VideoQuery, VideoQueryAdmin)

class ChoicesAdmin(admin.ModelAdmin):
    """Админка голосов"""
    list_display = ("VideoInQuery", "voted_user", "voted_time")

admin.site.register(Choices, ChoicesAdmin)

class ActualSongAdmin(admin.ModelAdmin):
    """Админка текущей песни"""
    list_display = ("video", "time_duration")

admin.site.register(ActualSong, ActualSongAdmin)
# Register your models here.
