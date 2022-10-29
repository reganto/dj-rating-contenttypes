from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.db import models

# Create your models here.


class Rate(models.Model):
    ip = models.GenericIPAddressField()
    score = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1),
        ]
    )
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
    )
    object_id = models.PositiveIntegerField()
    contect_object = GenericForeignKey()

    class Meta:
        indexes = [
            models.Index(
                fields=[
                    "content_type",
                    "object_id",
                ],
            )
        ]
        constraints = [
            models.UniqueConstraint(
                fields=[
                    "ip",
                    "object_id",
                ],
                name="one time rating",
            )
        ]

    def __str__(self):
        return f"{self.score}"
