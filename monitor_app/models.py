from django.db import models

# Create your models here.
class Image(models.Model):
    imageId = models.CharField(max_length=100)
    size = models.CharField(max_length=20)
    tags = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.imageId

class Container(models.Model):
    name = models.CharField(max_length=50)
    state = models.CharField(max_length=20)
    image = models.CharField(max_length=50)
    ports = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name