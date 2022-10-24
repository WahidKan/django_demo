from django.urls import re_path as url
from info.views.Type import type 
 
urlpatterns = [ 
    url(r'/type/(?P<pk>[0-9]+)$',type.type_view.as_view()),
    url(r'/type/',type.type_view.as_view()),
]