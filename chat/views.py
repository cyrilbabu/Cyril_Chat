from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import MessageForm
from django.shortcuts import get_object_or_404
from .models import Message
from django.db.models import Q
from django.db.models.functions import Random

# Create your views here.
def index(request):
    users = User.objects.all().order_by(Random())
    user_name = request.GET.get('user_name')
    if user_name != '' and user_name is not None:
        users = users.filter(username__icontains=user_name)   
    return render(request, 'chat/index.html',{'users':users})

def profile(request, id):
    user = get_object_or_404(User, id=id)
    return render(request, 'chat/profile.html',{'users':user})

def chat(request, id):
    current_user = request.user
    current_user_id = current_user.id
    user_name = get_object_or_404(User, id=id).username
    user = User.objects.get(username=user_name)
    if request.method == 'POST':
        message = request.POST.get('message')
        message_by = current_user
        message_to = user
        msg = Message(message=message,message_by=message_by,message_to=message_to,)
        msg.save()   
    
    user = get_object_or_404(User, id=id)  
    all_messages = Message.objects.filter(
    Q(message_to=user.id, message_by=current_user_id) | Q(message_to=current_user_id, message_by=user.id)
).order_by('-created')
    return render(request, 'chat/chat.html',{'user':user,'all_messages':all_messages,'current_user':current_user})
        