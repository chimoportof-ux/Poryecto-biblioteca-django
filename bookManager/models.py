from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    resume = models.TextField(max_length=500)
    author = models.CharField(max_length=120)
    image = models.ImageField(upload_to="images", null=True, blank=True)
    category = models.ManyToManyField(Category, related_name="category")
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}, ({self.author})" 
