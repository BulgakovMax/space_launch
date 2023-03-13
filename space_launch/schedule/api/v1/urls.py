from django.urls import path, include

from .views import *


urlpatterns = [
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/rocket/', RocketAPIList.as_view()),
    path('api/v1/rocket/<int:pk>/', RocketAPIUpdate.as_view()),
    path('api/v1/rocketdelete/<int:pk>/', RocketAPIDestroy.as_view()),
]