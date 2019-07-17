#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author: hao 2019/7/17-21:58
from django.urls import path
from apps.users import views

app_name = 'users'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
]
