from django.urls import re_path as url
from info.views.Province import province 
 
urlpatterns = [ 
    url(r'/province/(?P<pk>[0-9]+)$',province.province_view.as_view()),
    url(r'/province/',province.province_view.as_view()),
]