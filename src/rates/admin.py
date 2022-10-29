from django.contrib import admin

from rates.models import Rate
# Register your models here.

@admin.register(Rate)
class RateAdmin(admin.ModelAdmin):
    pass