
from django.db import models
from info.models.Country import ems_country
# Create your models here.
class ems_province(models.Model):
    name = models.CharField(max_length=100, blank=False, default='')
    shortCode = models.CharField(max_length=100, blank=False, default='')
    country  =  models.ForeignKey(ems_country, on_delete=models.SET_NULL, blank=True, null=True)
   
    def __str__(self):
        return self.name