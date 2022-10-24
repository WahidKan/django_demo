
from django.db import models
from info.models.Tehsil import ems_tehsil
from info.models.Constituency import ems_constituency
# Create your models here.
class ems_constituency_tehsil(models.Model):
    tehsil  =  models.ForeignKey(ems_tehsil, on_delete=models.SET_NULL, blank=True, null=True)
    constituency  =  models.ForeignKey(ems_constituency, on_delete=models.SET_NULL, blank=True, null=True)
   
