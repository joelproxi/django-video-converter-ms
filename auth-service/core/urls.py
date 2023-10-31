from django.urls import path

from core import views


urlpatterns = [
    path('register/', views.RegisterAPIView.as_view()),
    path('login/', views.LoginAPIView.as_view()),
    path('user/', views.UserProfilAPIView.as_view()),
]
