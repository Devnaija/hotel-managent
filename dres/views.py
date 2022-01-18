from django.shortcuts import render
from . models import *
# Create your views here.
def dining(request):
  dine = Dinedrink.objects.all()
  context={
    'dine': dine
  }
  return render(request, 'dres/dinning.html', context)

def spa(request):
  spaandine = Sparecreation.objects.all()
  context = {
    'spa':spaandine
  }
  return render(request,'dres/spa.html',context)

def event(request):
  event = Event.objects.all()
  context = {
    'event':event
  }
  return render(request, 'dres/event.html', context)
