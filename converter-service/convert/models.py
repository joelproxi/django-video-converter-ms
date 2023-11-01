from django.db import models


class Mp3File(models.Model):
    audio = models.FileField()
