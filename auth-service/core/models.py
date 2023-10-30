from django.db import models
from django.contrib.auth.models import AbstractUser


class UserModel(AbstractUser):
    username = None
    email = models.EmailField(unique=True, max_length=255)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def get_email(self):
        return self.email


class TokenModel(models.Model):
    user_id = models.PositiveIntegerField()
    token = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    expired_at = models.DateTimeField()

    def __str__(self) -> str:
        return str(self.user_id)
