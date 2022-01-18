from django.urls import path
from .import views

urlpatterns = [
    path('dining/', views.dining, name='dining'),
    path('spa/', views.spa, name='spa'),
    path('event/', views.event, name='event'),
]
