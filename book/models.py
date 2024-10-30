from datetime import datetime

from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=20)
    pub_time = models.DateTimeField(auto_now_add=True)
    price = models.FloatField(default=0)

    class Meta:
        db_table = 'book_table'
        ordering = ['-pub_time','name']

class Author(models.Model):
    is_active = models.BooleanField(default=True)
    username = models.CharField(max_length=20)
    date_joined = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()
    visit_count = models.IntegerField(default=0)
    profile = models.TextField()
    website = models.URLField()

class Tag(models.Model):
    name = models.CharField(max_length=200, unique=True)
    create_time = models.DateTimeField(default=datetime.now)
