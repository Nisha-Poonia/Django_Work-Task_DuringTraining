# Generated by Django 4.0.3 on 2022-05-04 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0002_course_paymentdetails'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Students',
            new_name='Student',
        ),
    ]