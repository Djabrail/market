from django.urls import path, include

from .views import *

urlpatterns = [
    path('auth/', include('djoser.urls')),
]