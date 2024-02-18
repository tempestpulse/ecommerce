# Generated by Django 5.0.2 on 2024-02-17 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='photo',
            field=models.ImageField(blank=True, default='photos/default_photo.jpg', null=True, upload_to='photos'),
        ),
        migrations.RemoveField(
            model_name='item',
            name='category',
        ),
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.ManyToManyField(blank=True, to='item.category'),
        ),
    ]
