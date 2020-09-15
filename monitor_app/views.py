#from django.shortcuts import render
from .models import Image, Container
from .serializers import ImageSerializer, ContainerSerializer
from rest_framework import generics

class ImageListCreate(generics.ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

class ContainerListCreate(generics.ListCreateAPIView):
    queryset = Container.objects.all()
    serializer_class = ContainerSerializer

