from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    DEFAULT_AVATAR = 'avatars/default-av.png'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default=DEFAULT_AVATAR, upload_to='avatars')

    def save(self, *args, **kwargs):
        if not self.avatar:
            self.avatar = self.DEFAULT_AVATAR
        super(Profile, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.user.username} Profile'
