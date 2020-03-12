from django.contrib import admin
from .models import *


# Register your models here.
class RoomModelAdmin(admin.ModelAdmin):
    list_display = ('room_no', 'location', 'get_sex_display', 'get_size_display', 'electric_charge', 'water_charge')
    search_fields = ('room_no',)
    list_filter = ('sex', 'size')

# student models in admin.
class StudentModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'get_sex_display', 'grade', 'profession', 'phone', 'room')
    search_fields = ('id',)
    list_filter = ()
    
# hygiene.
class SanitationModelAdmin(admin.ModelAdmin):
    list_display = ('room', 'target_date', 'score')
    list_filter = ()

# device models.
class DeviceModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'get_status_display')
    list_filter = ()


class DeviceSentRecordModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'device', 'room', 'person', 'borrow_time', 'send_time')
    list_filter = ()


class RuleModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_rule_type_display', 'room', 'person', 'record_time', 'remark')
    list_filter = ()
    

admin.site.register(RoomModel, RoomModelAdmin)
admin.site.register(StudentModel, StudentModelAdmin)
admin.site.register(SanitationModel, SanitationModelAdmin)
admin.site.register(DeviceModel, DeviceModelAdmin)
admin.site.register(DeviceSentRecordModel, DeviceSentRecordModelAdmin)
admin.site.register(RuleModel, RuleModelAdmin)
