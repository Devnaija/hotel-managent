from django.db import models
from datetime import datetime

# Create your models here.
class Dinedrink(models.Model):
  Dinedrinks=(
    ('dine','Dine'),
    ('drink','Drink'),
  )
  dine_name = models.CharField(max_length=100)
  seaters = models.IntegerField()
  air = models.IntegerField()
  dine_type = models.CharField(max_length=100, choices=Dinedrinks)
  photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
  dine_created = models.DateTimeField(default=datetime.now, blank=True)
 
  def __str__(self):
    return self.dine_name

class Sparecreation(models.Model):
  Sparecreations=(
    ('spa','Spa'),
    ('recreation','Recreation'),
  )
  spa_name = models.CharField(max_length=100)
  spa_type = models.CharField(max_length=100, choices=Sparecreations)
  photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
  spa_created = models.DateTimeField(default=datetime.now, blank=True)
 
  def __str__(self):
    return self.spa_name


class Event(models.Model):
  event_name = models.CharField(max_length=100)
  seaters = models.IntegerField()
  air = models.IntegerField()
  photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
  event_created = models.DateTimeField(default=datetime.now, blank=True)

  def __str__(self):
    return self.event_name
