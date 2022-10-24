from django.db import models
# Create your models here.

class ems_country(models.Model):
    name = models.CharField(max_length=100, blank=False, default='')
    shortCode = models.CharField(max_length=100, blank=False, default='')

    def __str__(self):
        return self.name
