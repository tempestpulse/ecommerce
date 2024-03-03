from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    DEFAULT_AVATAR = 'avatars/default-av.png'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default=DEFAULT_AVATAR, upload_to='avatars')
    bio = models.CharField(max_length=50, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.avatar:
            self.avatar = self.DEFAULT_AVATAR
        super(Profile, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.user.username} Profile'


class Follower(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    followed_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followed_by')
    date_followed = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def follower_count(user):
        return Follower.objects.filter(user=user).all().count()

    @staticmethod
    def following_count(followed_by):
        return Follower.objects.filter(followed_by=followed_by).all().count()

    def __str__(self):
        return f'{str(self.user.username)} followed by {str(self.followed_by)}'
