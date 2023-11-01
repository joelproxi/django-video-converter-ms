from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register('', views.VideoFileViewSet, basename='videos')

urlpatterns = router.urls
