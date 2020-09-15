from django.urls import path
from . import views

urlpatterns = [
    path('api/image/', views.ImageListCreate.as_view() ),
    path('api/container/', views.ContainerListCreate.as_view() ),
]