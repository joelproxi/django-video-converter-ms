
from django.urls import path

from convert import views


urlpatterns = [
    path('', views.convert_video, ),
]
