from django.urls import path
from .views import *


urlpatterns = [
    path('convert_text/', convertor, name='convertor'),
]