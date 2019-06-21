from django.db import models
from django.contrib.auth.models import User
from embed_video.fields import EmbedVideoField
# from djoser.urls.base import User
# Create your models here.

class Song(models.Model):
    video = EmbedVideoField()
    name = models.CharField(verbose_name="Название", max_length=300)
    author = models.CharField(verbose_name="Автор", null=True, max_length=300)
    duration_video = models.IntegerField(verbose_name="Длительность", null=True, default=0)

    def __str__(self):
        return "{} - {}".format(self.name, self.author)

    class Meta:
        verbose_name = "Песня"
        verbose_name_plural = "Песни"


class VideoQuery(models.Model):
    selection_time = models.DateTimeField(verbose_name="Время выбора", auto_now_add=True)
    selected_video = models.ForeignKey(Song, verbose_name="Выбранная песня", on_delete=models.CASCADE)
    user_choices = models.IntegerField(verbose_name="Голоса", default=1)

    def __str__(self):
        return self.selected_video.name

    class Meta:
        verbose_name = "Песня в очереди"
        verbose_name_plural = "Очередь песен"


class Choices(models.Model):
    VideoInQuery = models.ForeignKey(VideoQuery, verbose_name="Песня в очереди", on_delete=models.CASCADE)
    voted_user = models.ForeignKey(User, verbose_name="Проголосовавший пользователь", on_delete=models.CASCADE)
    voted_time = models.DateTimeField(verbose_name="Время выбора", auto_now_add=True)

    class Meta:
        verbose_name = "Голос"
        verbose_name_plural = "Голоса"


class ActualSong(models.Model):
    video = models.ForeignKey(Song, verbose_name="Текущее видео", on_delete=models.CASCADE)
    time_duration = models.IntegerField(verbose_name="Оставшееся время", default=0)
    selection_time = models.DateTimeField(verbose_name="Время выбора", auto_now_add=True, null=True)

    class Meta:
        verbose_name = "Проигрываемое видео"
        verbose_name_plural = "Проигрываемые видео"