from django.urls import path
from django.contrib.auth.models import User
from base import views


urlpatterns = [
    path('list/', views.listUsers, name='list-users'),
]