from django.urls import path
from app1.views import *
app1_name='tag'
urlpatterns=[
    path('jinja/',jinja,name='jinja'),
]
