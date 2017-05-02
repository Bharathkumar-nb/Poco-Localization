"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import RedirectView
from django.http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^main/', include('main.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^google8a43fbed4f8a62b6\.html$', lambda r: HttpResponse("google-site-verification: google8a43fbed4f8a62b6.html", content_type="text/plain")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + [
    #url(r'^.*$', RedirectView.as_view(url='http://poco.pythonanywhere.com/main/login/', permanent=False), name='login'),
    url(r'^.*$', RedirectView.as_view(url='http://localhost:8000/main/login/', permanent=False), name='login'),
]