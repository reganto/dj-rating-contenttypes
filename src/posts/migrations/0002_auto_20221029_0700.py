# Generated by Django 3.2.15 on 2022-10-29 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='modified',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
