from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Chat


def chat(request):
    context = {}
    chats = Chat.objects.values('room').distinct()
    context['rooms'] = chats
    return render(request, 'chatting/chat.html', context)


@login_required
def room(request, room_name):
    chats = Chat.objects.values('room').distinct()
    return render(request, 'chatting/room.html', {
        'room_name': room_name,
        'username': request.user.username,
        'rooms': chats
    })
