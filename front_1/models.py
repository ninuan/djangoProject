from django.db import models
from django.core import validators

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200, validators=[validators.MinLengthValidator(2)])
    content = models.TextField(validators=[validators.MinLengthValidator(3)])
    create_time = models.DateTimeField(auto_now_add=True)
    #blank=True表示表单验证时可以为空，但是数据库不可以为空
    category = models.CharField(max_length=50, blank=True)