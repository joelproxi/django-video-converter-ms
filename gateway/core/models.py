from django.db import models


class VideoFile(models.Model):
    video = models.FileField()
