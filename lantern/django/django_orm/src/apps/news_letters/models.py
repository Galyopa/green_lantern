from django.db import models


class NewsLetter(models.Model):
    email = models.EmailField(max_length=64, unique=True)

    def __str__(self):
        return self.email
