from django.urls import path
from app2.views import *
app2_name='tag2'
urlpatterns=[
    path('jinja2/',jinja2,name='jinja2'),
]