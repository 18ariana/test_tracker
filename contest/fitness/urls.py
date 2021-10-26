"""fitness URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.contrib import admin
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView)

urlpatterns = [
    path('admin/',  admin.site.urls),
    # Логин
    path('jwt/create/', TokenObtainPairView.as_view(), name="jwt-create"),
    # Обновление
    path('jwt/refresh/', TokenRefreshView.as_view(), name="jwt-create"),
    # Проверка
    path('jwt/verify/', TokenVerifyView.as_view(), name="jwt-create"),
    # Регистрация по /auth/users/
    path('auth/', include('djoser.urls')),
    path('', include('fitness_tracker.urls') )
]

