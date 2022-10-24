from django.urls import re_path as url
from info.views.District import district 
 
urlpatterns = [ 
    url(r'/district/(?P<pk>[0-9]+)$',district.district_view.as_view()),
    url(r'/district/',district.district_view.as_view()),
]