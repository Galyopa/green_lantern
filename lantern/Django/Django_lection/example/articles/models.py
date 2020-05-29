from django.contrib.auth.models import User
from django.db import models


class Article(models.Model):
    id = models.UUIDField(primary_key=True)
    title = models.CharField(max_length=255, verbose_name='Article')
    body = models.TextField(max_length=5000)
    views = models.IntegerField(default=0)
    author = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='articles')
    tags = models.ManyToManyField(to="Tag", blank=True)
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)


class Tag(models.Model):
    name = models.CharField(max_length=30, unique=True)
