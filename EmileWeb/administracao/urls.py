from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from administracao import views
from django.contrib.auth import views as auth_views

app_name = 'administracao'

urlpatterns = [
    url(r'^home/$', views.home, name='home'),
    url(r'^wall_messages_list/$', views.wall_messages_list, name='wall_messages_list'),
    url(r'^login/$', auth_views.login, {'template_name': 'administracao/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^wall_message_create/$', views.WallMessageCreateView.as_view(), name='wall_message_create'),
    url(r'^institutions_programs/(?P<pk>\d+)$', views.institutions_programs, name='institutions_programs'),
]
