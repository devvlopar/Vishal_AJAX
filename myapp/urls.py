from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('create_data/', create_data, name='create_data')
]