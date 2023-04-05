from django.urls import path
from .views import *


urlpatterns = [
    path('', ScheduleHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('addpage/', addpage, name='add_page'),
    path('rockets/', rockets, name='rockets'),
    path('launcher/', launcher_list, name='launcher_list'),
    path('locations/', locations, name='locations'),
    path('locations/<slug:slug>/', show_location, name='location'),
    path('agencies/', agencies, name='agencies'),
    path('agencies/<slug:slug>/', show_agency, name='agency'),
    path('contacts/', contacts, name='contacts'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('post/<slug:post_slug>/', show_post, name='post'),
    path('type/<slug:type_slug>', RocketType.as_view(), name='type'),
    path('next_launch/', next_launch, name='next_launch'),
]
