from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    #author = models.ForeignKey("Author", on_delete=models.CASCADE)
    genre = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    coverpage = models.FileField(upload_to="coverpage/")
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(default=0)
    description = models.TextField()

    def __str__(self):
        return self.title


class Genre(models.Model):
    #book = models.ForeignKey(Book, on_delete=models.CASCADE)
    type = models.CharField(max_length=100)
    icon = models.FileField(upload_to="genre/")
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.type


class Author(models.Model):
    #book = models.ForeignKey(Book, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    bio = models.TextField()
    pic = models.FileField(upload_to="author/")
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



