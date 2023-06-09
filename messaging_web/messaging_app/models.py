from django.db import models

class User(models.Model): name = models.CharField(max_length=100)

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages') 
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages') 
    text = models.TextField() 
    timestamp = models.DateTimeField(auto_now_add=True)