from django.apps import AppConfig


class InfoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'info'
    def ready(self):
        from info.models.Country import ems_country
        from info.models.Province import ems_province
        from info.models.District import ems_district
        from info.models.Tehsil import ems_tehsil
        from info.models.type import ems_type
        from info.models.Constituency import ems_constituency
