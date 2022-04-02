from django.urls import path
from . import views

urlpatterns = [
    path('beds', views.beds),
]
