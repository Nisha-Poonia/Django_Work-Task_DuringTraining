# Generated by Django 4.0.3 on 2022-05-04 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0004_rename_paymentdetails_paymentdetails1'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PaymentDetails1',
            new_name='PaymentDetails',
        ),
    ]
