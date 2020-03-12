"""apartment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from django.conf.urls import re_path
from myapp.views import *

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path('^users/', include('users.urls', namespace = "users")),
    re_path('^$', HomeView.as_view(), name = 'index'),
    re_path('^index/', HomeView.as_view(), name = 'index'),
    re_path('^student/', StudentListView.as_view(), name = 'student'),
    re_path('^room/', RoomListView.as_view(), name = 'room'),
    re_path('^electric_charge/', ElectricChargeView.as_view(), name = 'electric_charge'),
    re_path('^water_charge/', WaterChargeView.as_view(), name = 'water_charge'),
    re_path('^sanitation/', SanitationListView.as_view(), name = 'sanitation'),
    re_path('^device/', DeviceListView.as_view(), name = 'device'),
    re_path('^device_sent_record/', DeviceSentRecordListView.as_view(), name = 'device_sent_record'),
    re_path('^rule/', RuleListView.as_view(), name = 'rule'),
]
