# Generated by Django 4.0.3 on 2022-05-04 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0003_rename_students_student'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='paymentDetails',
            new_name='PaymentDetails1',
        ),
    ]