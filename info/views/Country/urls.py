from django.urls import re_path as url
from info.views.Country import country 
 
urlpatterns = [ 
    url(r'/country/(?P<pk>[0-9]+)$',country.country_view.as_view()),
    url(r'/country/',country.country_view.as_view()),
]