from django.urls import path, include

from .views import *

urlpatterns = [
    path('', ScheduleHome.as_view(), name='home'),
    # path('', index, name='home'),
    path('rockets', rockets),
    path('about/', about, name='about'),
    path('addpage/', addpage, name='add_page'),
    path('contact/', contacts, name='contact'),
    path('login/', login, name='login'),
    path('post/<slug:post_slug>/', show_post, name='post'),
    path('type/<slug:type_slug>', show_type, name='type'),
]
