from django.shortcuts import render 
from .models import User, Message 
 
def home(request): 
    users = User.objects.all() 
    return render(request, 'home.html', {'users': users}) 
 
def conversation(request, user_id): 
    user = User.objects.get(id=user_id) 
    conversations = Message.objects.filter(sender=user) | Message.objects.filter(receiver=user) 
    return render(request, 'conversation.html', {'user': user, 'conversations': conversations}) 