from django.db import models

# Create your models here.

class vehicleinfo(models.Model):
    registration_number = models.CharField(max_length=10)
    owner = models.CharField(max_length=100)
    make = models.CharField(max_length=100)
    colour = models.CharField(max_length=100)
    purchage_date = models.DateTimeField()



class violation(models.Model):
    vehicle_number = models.CharField(max_length=10)
    fine_amt = models.IntegerField()
    violation_done = models.CharField(max_length=500)
    violation_date = models.DateTimeField(auto_now_add=True)
