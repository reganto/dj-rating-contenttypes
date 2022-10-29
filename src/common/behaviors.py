from typing import Optional

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.conf import settings
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.db.models import Avg
from django.core.exceptions import ObjectDoesNotExist


class Timestampable(models.Model):
    created = models.DateTimeField(auto_now_add=True, null=True)
    modified = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True


class Authorable(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        null=True,
    )

    class Meta:
        abstract = True


class Rateable(models.Model):
    rates = GenericRelation("rates.Rate")

    class Meta:
        abstract = True

    @property
    def rates_count(self) -> int:
        """Calculate number of rates for a particular post.

        :return: Number of rates
        :rtype: int
        """
        return self.rates.count()

    @property
    def rates_average(self) -> float:
        """Calculate average of rates for a particular post.

        :return: Average of rates
        :rtype: float
        """
        return self.rates.aggregate(avg=Avg("score")).get("avg")

    def current_user_rate(self, user_id: int) -> Optional[int]:
        """Current user rate for a particular post.

        :param user_id: Current user id
        :type user_id: int
        :return: Current user rate or None
        :rtype: Optional[int]
        """
        try:
            obj = self.rates.get(user=user_id)
        except ObjectDoesNotExist:
            return None
        else:
            return obj.score


class ContentTypeable(models.Model):
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
    )
    object_id = models.PositiveIntegerField()
    contect_object = GenericForeignKey()

    class Meta:
        abstract = True
