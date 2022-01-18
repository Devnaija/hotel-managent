from django.urls import path
from .import views

urlpatterns = [
    path('check/<str:id>/', views.check, name='check'),
    path('pay/<str:id>/', views.pay, name='pay'),
]
