from django.contrib import admin
from .models import *

# Register your models here.

# class Roomadmin(admin.ModelAdmin):
 
admin.site.register(Room)
admin.site.register(Checks)