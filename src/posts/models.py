from common.behaviors import Authorable, Timestampable, Rateable
from django.db import models

# Create your models here.


class Post(Timestampable, Authorable, Rateable, models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self):
        return f"{self.title}"
