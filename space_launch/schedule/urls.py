from django.urls import path
from .views import *

urlpatterns = [
    path('', ScheduleHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('addpage/', addpage, name='add_page'),
    path('rockets/', rockets, name='rockets'),
    path('locations/', locations, name='locations'),
    path('location/<slug:location_slug>/', show_location, name='location'),
    path('agencies/', agencies, name='agencies'),
    path('contact/', contacts, name='contact'),
    path('login/', login, name='login'),
    path('post/<slug:post_slug>/', show_post, name='post'),
    path('type/<slug:type_slug>', show_type, name='type'),
]
