from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from administracao import views

app_name = 'administracao'

urlpatterns = [
    url(r'^home/$', views.home, name='home'),
]
