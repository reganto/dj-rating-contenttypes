from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from common.behaviors import Authorable, Timestampable

from rates.models import Rate

# Create your models here.


class Post(Timestampable, Authorable, models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    rates = GenericRelation(Rate)

    def __str__(self):
        return f"{self.title}"
