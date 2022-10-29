from common.behaviors import ContentTypeable
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.


class Rate(ContentTypeable, models.Model):
    ip = models.GenericIPAddressField()
    score = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1),
        ]
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
    )

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
