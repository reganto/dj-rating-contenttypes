from django.contrib.contenttypes.admin import GenericStackedInline
from django.contrib import admin

from posts.models import Post
from rates.models import Rate

# Register your models here.


class RateInline(GenericStackedInline):
    model = Rate


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [
        RateInline,
    ]
