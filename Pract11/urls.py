"""
URL configuration for Pract11 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
import protoWiki11.views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', protoWiki11.views.index),
    path('index.html', protoWiki11.views.index),
    path('MelinasPage.html', protoWiki11.views.MelinasPage),
    path('AstelPage.html', protoWiki11.views.AstelPage),
    path('FirePotPage.html', protoWiki11.views.FirePotPage),
    path('WeaponPage.html', protoWiki11.views.WeaponPage),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)