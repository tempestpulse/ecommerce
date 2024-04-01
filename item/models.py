from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Item(models.Model):
    DEFAULT_PHOTO = 'photos/default_photo.jpg'

    name = models.CharField(max_length=40)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(max_length=1000, blank=True, null=True)
    photo = models.ImageField(default=DEFAULT_PHOTO, upload_to='photos', blank=True, null=True)
    category = models.ManyToManyField(Category, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    favorite = models.ManyToManyField(User, related_name='favorited_items')
    views = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.name

    @property
    def favorite_count(self):
        return self.favorite.count()

    def save(self, *args, **kwargs):
        if not self.photo:
            self.photo = self.DEFAULT_PHOTO
        super(Item, self).save(*args, **kwargs)

    def favorite_status(self, user):
        return self.favorite.filter(pk=user.id).exists()
