from django.urls import path, include

from schedule.api.v1.views import RocketAPIList, RocketAPIUpdate, RocketAPIDestroy, LocationAPIList, AgencyAPIList


urlpatterns = [
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/rocket/', RocketAPIList.as_view(), name="rockectslist"),
    path('api/v1/rocket/<int:pk>/', RocketAPIUpdate.as_view()),
    path('api/v1/rocketdelete/<int:pk>/', RocketAPIDestroy.as_view()),
    path('api/v1/locations/', LocationAPIList.as_view(), name="locationstlist"),
    path('api/v1/agencies/', AgencyAPIList.as_view(), name="agencieslist"),
]