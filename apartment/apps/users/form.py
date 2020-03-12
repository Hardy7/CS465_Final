#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms

__version__ = '3.0.3'

"""
@brief  
@details 
@author  HanyangXiao JianqiangHao
@date    2020-03-05 
"""


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "enter password", "value": "", "required": "required"}),
                               min_length=5, max_length=20, error_messages={"required": "invalid password"})


class RegisterForm(forms.Form):
    username = forms.CharField(min_length = 3, max_length=20, error_messages={"required": "invalid password"})
    email = forms.EmailField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "enter email", "value": ""}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "enter password", "value": "", "required": "required"}),
                               min_length=5, max_length=20, error_messages={"required": "invalid password"})