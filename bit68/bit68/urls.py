"""bit68 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
from .views import weather,register,get_whether_in_template
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('api-auth/', include('rest_framework.urls')),
    # path('auth/', include('djoser.urls.jwt')),
    # API Auth End Points
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    #template View Auth
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register',register.as_view(), name='register'),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    #weather EndPoint
    path('weather/',weather.as_view(),name='get_weather' ),
    path('get_whether_in_template', get_whether_in_template, name='get_whether_in_template'),

]
