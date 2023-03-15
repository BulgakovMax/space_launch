from django.urls import path, include

from space_launch.schedule.api.v1.views import RocketAPIList, RocketAPIUpdate, RocketAPIDestroy


urlpatterns = [
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/rocket/', RocketAPIList.as_view(), name="rockectlist"),
    # path('api/v1/rocket/<int:pk>/', RocketAPIUpdate.as_view()),
    # path('api/v1/rocketdelete/<int:pk>/', RocketAPIDestroy.as_view()),
]