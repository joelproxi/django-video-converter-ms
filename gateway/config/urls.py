
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include('auth_svc.urls')),
    path('api/v1/videos/', include('core.urls')),
]
