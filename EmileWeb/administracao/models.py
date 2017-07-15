from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.IntegerField(blank=False, null=False)


class MessageFile(models.Model):
    message_file = models.FileField(upload_to='wall_messages_files/')
    message_id = models.IntegerField(unique=True, blank=True, null=True)
