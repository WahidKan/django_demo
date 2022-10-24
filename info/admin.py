from django.contrib import admin
from .models.Country import ems_country
from .models.Province import ems_province
from .models.District import ems_district
from .models.Tehsil import ems_tehsil
from .models.type import ems_type

@admin.register(ems_country)
class Country(admin.ModelAdmin):
    list_display = ['name','shortCode']

@admin.register(ems_province)
class Country(admin.ModelAdmin):
    list_display = ['name','shortCode','country']

@admin.register(ems_district)
class Country(admin.ModelAdmin):
    list_display = ['name','shortCode','province']

@admin.register(ems_tehsil)
class Country(admin.ModelAdmin):
    list_display = ['name','shortCode','district']

@admin.register(ems_type)
class Country(admin.ModelAdmin):
    list_display = ['code']