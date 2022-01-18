from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Request
from django.core.mail import send_mail


def userrequest(request):
  if request.method == 'POST':
    room_id = request.POST['room_id']
    room = request.POST['room']
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    message = request.POST['message']
    user_id = request.POST['user_id']
    #check if user make inquiry already
    if request.user.is_authenticated:
      user_id = request.user.id
      has_contacted = Request.objects.all().filter(
          room_id=room_id, user_id=user_id)
      if has_contacted:
        messages.error(
            request, 'You have already made an request for this !')
        return redirect('/rooms/'+room_id)

    user_request = Request(room=room, room_id=room_id, name=name, email=email, phone=phone, message=message, user_id=user_id)

    user_request.save()

    # send mail
    send_mail(
        'Made An Inquiry',
        'You have made a request for ' + room +
        '. admin will get back to you on your request',
        'nathanielnarth@gmail.com',
        [email, 'nathconclassichub@gmail.com'],
        fail_silently=False
    )

    messages.success(
        request, 'Your request has been submitted, we will get back to you soon!')
    return redirect('/rooms/'+room_id)
