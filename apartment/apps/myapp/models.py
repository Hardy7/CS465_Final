from django.db import models

# Create your models here.


class RoomModel(models.Model):
    room_no = models.CharField(verbose_name="room_id", max_length=100, unique=True)
    location = models.CharField(verbose_name="region", max_length=100,default=None)
    sex = models.IntegerField(verbose_name='sex', choices=((0, 'male'), (1, 'female')))
    size = models.IntegerField(verbose_name="bed id", choices=((0, '4people'), (1, '6people')))
    electric_charge = models.IntegerField(verbose_name="remaining_electricity($)")
    water_charge = models.IntegerField(verbose_name="remaining_water($)")

    class Meta:
        verbose_name = "room_information"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.location + self.room_no


class StudentModel(models.Model):
    name = models.CharField(verbose_name='name',max_length=100)
    sex = models.IntegerField(verbose_name='sex', choices=((0, 'male'), (1, 'female')), default=0)
    grade = models.CharField(verbose_name="grade", max_length=100)
    profession = models.CharField(verbose_name="major", max_length=255, default=None)
    phone = models.CharField(verbose_name="phone", max_length=11)
    room = models.ForeignKey(RoomModel, verbose_name="room_id", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "user_information"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class SanitationModel(models.Model):
    """
    hygiene record
    """
    room = models.ForeignKey(RoomModel, verbose_name="room_id", on_delete=models.CASCADE)
    target_date = models.DateField(verbose_name="date")
    score = models.IntegerField(verbose_name="score")

    class Meta:
        verbose_name = "hygiene_information"
        verbose_name_plural = verbose_name


class DeviceModel(models.Model):
    """
    device
    """
    name = models.CharField(verbose_name="device_name", max_length=100)
    status = models.IntegerField(verbose_name="device_status", choices=((0, "exist"), (1, "lend")))

    class Meta:
        verbose_name = "device_information"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class DeviceSentRecordModel(models.Model):
    """
    device check record
    """
    device = models.ForeignKey(DeviceModel, verbose_name="device", related_name='sent_record', on_delete=models.CASCADE)
    room = models.ForeignKey(RoomModel, verbose_name="dorm", on_delete=models.CASCADE)
    person = models.ForeignKey(StudentModel, verbose_name="renter", on_delete=models.CASCADE)
    borrow_time = models.DateTimeField(verbose_name="lease_time")
    send_time = models.DateTimeField(verbose_name="return_time", blank=True)

    class Meta:
        verbose_name = "device_lending_record"
        verbose_name_plural = verbose_name


class RuleModel(models.Model):
    """
    violation record
    """
    rule_type = models.IntegerField(verbose_name="violation_type", choices=((0, 'roommateContradiction'), (1, 'drunk'), (2, 'damagePublicProperty'), (3, 'smoke'), (4, 'other')))
    room = models.ForeignKey(RoomModel, verbose_name="dorm", on_delete=models.CASCADE)
    person = models.ForeignKey(StudentModel, verbose_name="person", on_delete=models.CASCADE)
    record_time = models.DateTimeField(verbose_name="time")
    remark = models.CharField(verbose_name="comment", max_length=512)

    class Meta:
        verbose_name = "violation_record"
        verbose_name_plural = verbose_name

















