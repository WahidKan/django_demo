
from django.db import models
from info.models.type import ems_type
# Create your models here.
class ems_constituency(models.Model):
    name = models.CharField(max_length=100, blank=False, default='')
    constituency_no = models.CharField(max_length=100, blank=False, default='')
    area_size = models.FloatField(blank=False, default=0)
    type  =  models.ForeignKey(ems_type, on_delete=models.SET_NULL, blank=True, null=True)
   
