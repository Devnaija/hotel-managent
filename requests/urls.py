from django.urls import path
from .import views

urlpatterns = [
    path('userrequest/', views.userrequest, name='userrequest')
]
