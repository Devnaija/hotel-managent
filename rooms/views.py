from django.shortcuts import render
from .models import Room



def rooms(request):
  room = Room.objects.all().order_by('-room_date')
  context={
    'show' : room
  }
  return render(request, 'rooms/rooms.html',context)

def room(request, id):
  room = Room.objects.get(id=id)
  context={
    'show' : room
  }
  return render(request, 'rooms/room.html',context)


def search(request):
  return render(request, 'rooms/search.html')