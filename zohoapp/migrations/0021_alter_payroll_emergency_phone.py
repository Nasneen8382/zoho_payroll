# Generated by Django 3.2.19 on 2023-08-10 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0020_alter_payroll_emergency_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payroll',
            name='emergency_phone',
            field=models.BigIntegerField(blank=True, default=1, null=True),
        ),
    ]