from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Userpune(models.Manager):
    def get_queryset(self):
        return super(Userpune, self).get_queryset().filter(city='Apune')


class Userprofile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    phone = models.IntegerField()
    image = models.ImageField(upload_to="profile_image", blank=True)


    def __str__(self):
        return self.user.username

