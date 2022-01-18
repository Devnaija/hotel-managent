from django.shortcuts import render, redirect
from .models import NewsletterUser
from django.contrib import messages, auth

from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
from django.utils.safestring import mark_safe

def index(request):
  if request.method == 'POST':
    email = request.POST['email'] 
    #check if email already exist make inquiry already
    if NewsletterUser.objects.filter(email=email).exists():
        messages.error(request, 'You have already subscribe to our newsletter !')
        return redirect('index')
    else:
      user_email = NewsletterUser.objects.create(email = email)
      user_email.save()


    # send mail
    subject = 'Welcome To Ncode Hotel'
    body = f"Greetings from Ncode Hotel Services, \n Thank you for signing up for Ncode Hotel Newsletter. You now have access to Ncode Hotel platforms. \n You can check our rooms, events hall, spa and recreation, dining and more for details and booking . \n We will be sending you updates on our latest services. \n —The Ncode Hotel Web Services Team"
    send_mail(
        subject,
        body,
        settings.EMAIL_HOST_USER,
        [user_email.email],
        fail_silently=False
    )

    messages.success(
        request, 'Your have successfully subscribe to our newsletter!')
    return redirect('index')
  return render(request,'pages/index.html')


def about(request):
  
  return render(request,'pages/about.html')


def deleted(request):

  return render(request,'pages/delete.html')
