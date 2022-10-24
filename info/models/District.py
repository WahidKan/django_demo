
from django.db import models
from info.models.Province import ems_province
# Create your models here.
class ems_district(models.Model):
    name = models.CharField(max_length=100, blank=False, default='')
    shortCode = models.CharField(max_length=100, blank=False, default='')
    province  =  models.ForeignKey(ems_province, on_delete=models.SET_NULL, blank=True, null=True)
   
    def __str__(self):
        return self.name
