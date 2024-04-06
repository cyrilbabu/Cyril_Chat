from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Message(models.Model):
    message_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    message = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now=True)
    message_by =  models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.message