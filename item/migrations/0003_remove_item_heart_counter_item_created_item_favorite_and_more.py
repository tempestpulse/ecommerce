# Generated by Django 5.0.2 on 2024-04-01 15:08

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_item_description_item_photo_remove_item_category_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='heart_counter',
        ),
        migrations.AddField(
            model_name='item',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='favorite',
            field=models.ManyToManyField(related_name='favorited_items', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='item',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
