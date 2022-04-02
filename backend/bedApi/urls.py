from django.urls import path

from . import views

urlpatterns = [
    path('beds', views.beds),
    path('beds/<int:bed_id>', views.bed_detail),
]
