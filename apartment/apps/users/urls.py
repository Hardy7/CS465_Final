#!/usr/bin/env python
# -*- coding: utf-8 -*-
__version__ = '3.0.3'
from django.conf.urls import url
from django.urls import path
from .views import LoginView, RegisterView, LogoutView


app_name = 'users'


urlpatterns = [
    path(r'login/', LoginView.as_view(), name="login"),
    path(r'logout/', LogoutView.as_view(), name="logout"),
    path('register/', RegisterView.as_view(), name="register"),
]
