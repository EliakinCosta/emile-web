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
    url(r'^destinations_by_user_type/(?P<pk>\d+)$', views.destinations_by_user_type, name='destinations_by_user_type'),
    url(r'^programs_course_sections/(?P<pk>\d+)$', views.programs_course_sections, name='programs_course_sections'),
]
