from django.urls import path

from . import views

urlpatterns = [
    path('demo/beds', views.beds),
    path('demo/beds/<int:bed_id>', views.bed_detail),
    path('beds', views.beds_grpc),
    path('beds/<str:bed_id>', views.bed_detail_grpc),
]
