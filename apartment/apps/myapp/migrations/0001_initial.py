# Generated by Django 3.0.3 on 2020-03-08 08:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='device_name')),
                ('status', models.IntegerField(choices=[(0, 'exist'), (1, 'lend')], verbose_name='device_status')),
            ],
            options={
                'verbose_name': 'device_information',
                'verbose_name_plural': 'device_information',
            },
        ),
        migrations.CreateModel(
            name='RoomModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_no', models.CharField(max_length=100, unique=True, verbose_name='dorm_id')),
                ('location', models.CharField(default=None, max_length=100, verbose_name='region')),
                ('sex', models.IntegerField(choices=[(0, 'male'), (1, 'female')], verbose_name='sex')),
                ('size', models.IntegerField(choices=[(0, '4people'), (1, '6people')], verbose_name='bed_id')),
                ('electric_charge', models.IntegerField(verbose_name='remaining_electricity($)')),
                ('water_charge', models.IntegerField(verbose_name='remaining_water($)')),
            ],
            options={
                'verbose_name': 'dorm_information',
                'verbose_name_plural': 'dorm_information',
            },
        ),
        migrations.CreateModel(
            name='StudentModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('sex', models.IntegerField(choices=[(0, 'male'), (1, 'female')], default=0, verbose_name='sex')),
                ('grade', models.CharField(max_length=100, verbose_name='grade')),
                ('profession', models.CharField(default=None, max_length=255, verbose_name='major')),
                ('phone', models.CharField(max_length=11, verbose_name='phone')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.RoomModel', verbose_name='room_id')),
            ],
            options={
                'verbose_name': 'student_information',
                'verbose_name_plural': 'student_information',
            },
        ),
        migrations.CreateModel(
            name='SanitationModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target_date', models.DateField(verbose_name='date')),
                ('score', models.IntegerField(verbose_name='score')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.RoomModel', verbose_name='room_id')),
            ],
            options={
                'verbose_name': 'health_information',
                'verbose_name_plural': 'health_information',
            },
        ),
        migrations.CreateModel(
            name='RuleModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rule_type', models.IntegerField(choices=[(0, 'roommate_contradiction'), (1, 'drinking'), (2, 'damage_public_property'), (3, 'dangerous_articles_prohibited'), (4, 'other')], verbose_name='violation_type')),
                ('record_time', models.DateTimeField(verbose_name='disciplinary_time')),
                ('remark', models.CharField(max_length=512, verbose_name='comment')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.StudentModel', verbose_name='disciplinary_people')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.RoomModel', verbose_name='dorm')),
            ],
            options={
                'verbose_name': 'disciplinary_record',
                'verbose_name_plural': 'disciplinary_record',
            },
        ),
        migrations.CreateModel(
            name='DeviceSentRecordModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrow_time', models.DateTimeField(verbose_name='lease_time')),
                ('send_time', models.DateTimeField(blank=True, verbose_name='return_time')),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_record', to='myapp.DeviceModel', verbose_name='device')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.StudentModel', verbose_name='renter')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.RoomModel', verbose_name='dorm')),
            ],
            options={
                'verbose_name': 'equipment_concession_record',
                'verbose_name_plural': 'equipment_concession_record',
            },
        ),
    ]