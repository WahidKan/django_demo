
from django.db import models
# Create your models here.
class ems_type(models.Model):
    code = models.CharField(max_length=100, blank=False, default='')
