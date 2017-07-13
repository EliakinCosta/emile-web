from django.db import models

# Create your models here.

class MessageFile(models.Model):
    message_file = models.FileField(upload_to='wall_messages_files/')
    message_id = models.IntegerField(unique=True)
