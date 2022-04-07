from django.urls import path

from . import views

urlpatterns = [
    path('beds', views.beds),
    path('beds/<int:bed_id>', views.bed_detail),
    path('grpc/beds', views.beds_grpc),
    path('grpc/beds/<str:bed_id>', views.bed_detail_grpc),
]
