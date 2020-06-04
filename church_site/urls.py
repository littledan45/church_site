"""church_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from accounts.views import UserViewSet
from churches.views import ChurchViewSet

router = routers.DefaultRouter()
router.register(r'api/v1/users', UserViewSet)
router.register(r'api/v1/churches', ChurchViewSet)

urlpatterns = [
    path('', include('home.urls')),
    url(r'^', include(router.urls)),
    path('admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls')),
    path('accounts/', include('accounts.urls')),
    path('churches/', include('churches.urls')),
    path('speakers/', include('speakers.urls')),
    path('schedules/', include('schedules.urls')),
    path('sermons/', include('sermons.urls')),
    path('streams/', include('streams.urls')),
]
