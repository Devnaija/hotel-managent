from django.db import models
from datetime import datetime

from django.contrib.auth.models import User

# Create your models here.
class Room(models.Model):
  RoomCategory=(
    ('economy','Economy'),
    ('family','Family'),
    ('business class','Business Class'),
  )
  room_type = models.CharField(max_length=100, choices= RoomCategory)
  room_name = models.CharField(max_length=100)
  bedrooms = models.IntegerField()
  bathrooms = models.DecimalField(max_digits=2,decimal_places=1)
  sqft = models.IntegerField()
  description = models.TextField(blank=True)
  price = models.IntegerField()
  photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
  photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  is_booked = models.BooleanField(default=False)
  room_date = models.DateTimeField(default=datetime.now, blank=True)
 

  def __str__(self):
    return self.room_name

class Checks(models.Model):
  user = models.ForeignKey(
      User, on_delete=models.CASCADE, blank=True, null=True)
  room = models.OneToOneField(Room, on_delete=models.CASCADE, null=True, blank=True)
  is_payed = models.BooleanField(default=False)
  first_name = models.CharField(max_length=100, null=True, blank=True)
  last_name = models.CharField(max_length=100, null=True, blank=True)
  checkin_date = models.DateTimeField(default=datetime.now, blank=True, null=True)
  checkout_date = models.DateTimeField(default=datetime.now, blank=True, null=True)

  def __str__(self):
    return str(self.room)
  
  @property
  def getdays(self):
    diff = (self.checkout_date - self.checkin_date).days
    return diff
  @property
  def gettotal(self):
    amount = self.room.price
    total = ((self.checkout_date - self.checkin_date).days) * amount
    return total
