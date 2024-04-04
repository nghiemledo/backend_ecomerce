from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('products.urls')),
    path('api/v1/', include('upload.urls')),
    path('api/v1/', include('users.urls')),
    path('api/v1/', include('djoser.urls')),
	path('api/v1/', include('djoser.urls.jwt')),
]
