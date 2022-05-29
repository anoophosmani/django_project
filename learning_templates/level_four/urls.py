from django.contrib import admin
from django.urls import path,include
from level_four import views


# TEMPLATE TAGGING

app_name = 'level_four'

urlpatterns =[
    path('relative/',views.relative,name='relative'),
    path('other/',views.other,name='other'),

]