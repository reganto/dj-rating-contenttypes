# Generated by Django 3.2.15 on 2022-10-29 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rates', '0001_initial'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='rate',
            name='one time rating',
        ),
        migrations.AddConstraint(
            model_name='rate',
            constraint=models.UniqueConstraint(fields=('ip', 'object_id'), name='one time rating'),
        ),
    ]
