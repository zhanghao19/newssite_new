#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author: hao 2019/7/17-21:44
from django.urls import path
from apps.news import views

app_name = 'news'
urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
]
