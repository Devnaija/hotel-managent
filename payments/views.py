from django.shortcuts import render,redirect
from django.contrib import messages, auth
from rooms.models import *
import datetime
# paypal
from django.http import JsonResponse
import json
# Create your views here.


def check(request, id):
  room = Room.objects.get(id=id)

  if request.method == 'POST': 
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    room = request.POST['room']
    checkin_date = request.POST['checkin_date']
    checkout_date = request.POST['checkout_date']

    check = Checks(user =request.user,checkin_date=checkin_date, checkout_date=checkout_date, first_name=first_name,last_name=last_name, room=Room.objects.filter(room_name=room).filter(is_booked=False).first())
    check.save()

    return redirect('pay',id=id)
 
  context={
    'show' : room,
  }
  return render(request, 'payments/check.html',context)



def pay(request,id):
  # get all rooms that is payed and also that is checked anf change their status to true
  getBook = Checks.objects.get(room=id)
  getBook.is_payed = True
  getBook.save()
  days = getBook.getdays
  total = getBook.gettotal
  room = Room.objects.get(id=id)
  room.is_booked = True
  room.save()

  # body = json.loads(request.body)
  context = {
   'show' : getBook,
   'days' : days,
   'total' : total,
  }
  
  return render(request, 'payments/pay.html', context)



# if check.room.exists():
#       return redirect('check',id=id)
#     else:
#       check.is_payed = True
#       check.save()
#       return redirect('pay',id=id)
