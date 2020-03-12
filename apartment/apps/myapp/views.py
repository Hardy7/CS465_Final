from django.shortcuts import render, reverse
from django.views.generic.base import View
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger
from django.db.models import Q
from .custom_paginator import CustomPaginator
from .models import *


# if user doesn't register, it always display login page.
class LoginRequiredMixin(object):

    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view, login_url='/users/login')


class HomeView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'index.html')


class StudentListView(LoginRequiredMixin, View):
    def get(self, request):
        stu_list = StudentModel.objects.all()
        current_page = request.GET.get("page", '1')
        paginator = CustomPaginator(current_page, 9, stu_list, 10)
        try:
            paginator = paginator.page(current_page)
        except PageNotAnInteger:

            paginator = paginator.page(1)
        except EmptyPage:

            paginator = paginator.page(paginator.num_pages)
        return render(request, 'student.html', {"paginator": paginator})

    def post(self, request):
        q = request.POST.get('q')
        records = StudentModel.objects.all().filter(Q(name__icontains=q))
        current_page = request.GET.get("page", '1')
        paginator = CustomPaginator(current_page, 9, records, 10)
        try:
            paginator = paginator.page(current_page)
        except PageNotAnInteger:

            paginator = paginator.page(1)
        except EmptyPage:

            paginator = paginator.page(paginator.num_pages)
        return render(request, 'student.html', {"paginator": paginator})


class RoomListView(LoginRequiredMixin, View):
    def get(self, request):
        room_list = RoomModel.objects.all()
        current_page = request.GET.get("page", '1')
        paginator = CustomPaginator(current_page, 9, room_list, 10)
        try:
            paginator = paginator.page(current_page)
        except PageNotAnInteger:

            paginator = paginator.page(1)
        except EmptyPage:

            paginator = paginator.page(paginator.num_pages)
        return render(request, 'room.html', {"paginator": paginator})

    def post(self, request):
        q = request.POST.get('q')
        records = RoomModel.objects.all().filter(Q(name__icontains=q))
        current_page = request.GET.get("page", '1')
        paginator = CustomPaginator(current_page, 9, records, 10)
        try:
            paginator = paginator.page(current_page)
        except PageNotAnInteger:

            paginator = paginator.page(1)
        except EmptyPage:

            paginator = paginator.page(paginator.num_pages)
        return render(request, 'room.html', {"paginator": paginator})

    
#electric charge.
class ElectricChargeView(LoginRequiredMixin, View):
    def get(self, request):
        room_id = request.GET.get("room_id")
        room = RoomModel.objects.get(id=room_id)
        return render(request, 'electric_charge.html', {"room": room})

    def post(self, request):
        room_id = request.POST.get('room_id')
        charge = int(request.POST.get("charge"))
        room = RoomModel.objects.get(id=room_id)
        room.electric_charge += charge
        room.save()
        return HttpResponseRedirect(reverse("room"))


class WaterChargeView(LoginRequiredMixin, View):
    def get(self, request):
        room_id = request.GET.get("room_id")
        room = RoomModel.objects.get(id=room_id)
        return render(request, 'water_charge.html', {"room": room})

    def post(self, request):
        room_id = request.POST.get('room_id')
        charge = int(request.POST.get("charge"))
        room = RoomModel.objects.get(id=room_id)
        room.water_charge += charge
        room.save()
        return HttpResponseRedirect(reverse("room"))

#hygiene.
class SanitationListView(LoginRequiredMixin, View):
    def get(self, request):
        room_list = SanitationModel.objects.all()
        current_page = request.GET.get("page", '1')
        paginator = CustomPaginator(current_page, 9, room_list, 10)
        try:
            paginator = paginator.page(current_page)
        except PageNotAnInteger:

            paginator = paginator.page(1)
        except EmptyPage:

            paginator = paginator.page(paginator.num_pages)
        return render(request, 'sanitation.html', {"paginator": paginator})

    def post(self, request):
        q = request.POST.get('q')
        records = SanitationModel.objects.all().filter(Q(name__icontains=q))
        current_page = request.GET.get("page", '1')
        paginator = CustomPaginator(current_page, 9, records, 10)
        try:
            paginator = paginator.page(current_page)
        except PageNotAnInteger:

            paginator = paginator.page(1)
        except EmptyPage:

            paginator = paginator.page(paginator.num_pages)
        return render(request, 'sanitation.html', {"paginator": paginator})

# device record.
class DeviceListView(LoginRequiredMixin, View):
    def get(self, request):
        room_list = DeviceModel.objects.all()
        current_page = request.GET.get("page", '1')
        paginator = CustomPaginator(current_page, 9, room_list, 10)
        try:
            paginator = paginator.page(current_page)
        except PageNotAnInteger:

            paginator = paginator.page(1)
        except EmptyPage:

            paginator = paginator.page(paginator.num_pages)
        return render(request, 'device.html', {"paginator": paginator})

    def post(self, request):
        q = request.POST.get('q')
        records = DeviceModel.objects.all().filter(Q(name__icontains=q))
        current_page = request.GET.get("page", '1')
        paginator = CustomPaginator(current_page, 9, records, 10)
        try:
            paginator = paginator.page(current_page)
        except PageNotAnInteger:

            paginator = paginator.page(1)
        except EmptyPage:

            paginator = paginator.page(paginator.num_pages)
        return render(request, 'device.html', {"paginator": paginator})


class DeviceSentRecordListView(LoginRequiredMixin, View):
    def get(self, request):
        device_id = request.GET.get("device_id")
        device = DeviceModel.objects.get(id=device_id)
        device_record_list = DeviceSentRecordModel.objects.filter(device__id = device_id)
        current_page = request.GET.get("page", '1')
        paginator = CustomPaginator(current_page, 9, device_record_list, 10)
        try:
            paginator = paginator.page(current_page)
        except PageNotAnInteger:

            paginator = paginator.page(1)
        except EmptyPage:

            paginator = paginator.page(paginator.num_pages)
        return render(request, 'device_record.html', {"paginator": paginator, "device": device})

#violation record.
class RuleListView(LoginRequiredMixin, View):
    def get(self, request):
        room_list = RuleModel.objects.all()
        current_page = request.GET.get("page", '1')
        paginator = CustomPaginator(current_page, 9, room_list, 10)
        try:
            paginator = paginator.page(current_page)
        except PageNotAnInteger:

            paginator = paginator.page(1)
        except EmptyPage:

            paginator = paginator.page(paginator.num_pages)
        return render(request, 'rule.html', {"paginator": paginator})

