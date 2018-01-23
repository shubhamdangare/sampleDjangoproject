from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Datastrore(models.Model):
    post = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)


class Friendlist(models.Model):
    user = models.ManyToManyField(User)
    current_user = models.ForeignKey(User, related_name='owner', null=True, on_delete=models.CASCADE)

    @classmethod
    def Create_list(cls, current_user, new_user):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.user.add(new_user)

    @classmethod
    def Remove_list(cls, current_user, new_user):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.user.remove(new_user)
