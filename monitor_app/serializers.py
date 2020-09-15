from rest_framework import serializers
from .models import Image, Container

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'
        #fields = ('id', 'name', 'email', 'message')

class ContainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Container
        fields = '__all__'