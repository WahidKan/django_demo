from django.urls import re_path as url
from info.views.Tehsil import tehsil 
 
urlpatterns = [ 
    url(r'/tehsil/(?P<pk>[0-9]+)$',tehsil.tehsil_view.as_view()),
    url(r'/tehsil/',tehsil.tehsil_view.as_view()),
]