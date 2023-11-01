
from auth_svc import views
from django.urls import path


urlpatterns = [
    path('login/', views.LoginAPIView.as_view()),
    path('register/', views.RegisterAPIView.as_view()),
]
