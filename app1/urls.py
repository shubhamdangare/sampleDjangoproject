"""app1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from app1 import views
from app1.views import redirect_login

urlpatterns = [
    url(r'^$', views.redirect_login),
    url(r'^admin/', admin.site.urls),
    url(r'^account/', include('account.urls', namespace='account')),
    url(r'^home/', include('home.urls', namespace='home')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
