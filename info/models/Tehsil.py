
from django.db import models
from info.models.District import ems_district
# Create your models here.
class ems_tehsil(models.Model):
    name = models.CharField(max_length=100, blank=False, default='')
    shortCode = models.CharField(max_length=100, blank=False, default='')
    district  =  models.ForeignKey(ems_district, on_delete=models.SET_NULL, blank=True, null=True)
   
    def __str__(self):
        return self.name