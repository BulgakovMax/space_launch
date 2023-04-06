from django.urls import path
from .views import convertor


urlpatterns = [
    path('convert_text/', convertor, name='convertor'),
]