# Generated by Django 3.2.19 on 2023-07-25 07:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0006_payroll'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bankdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acc_no', models.IntegerField()),
                ('IFSC', models.CharField(max_length=100)),
                ('bank_name', models.CharField(max_length=100)),
                ('branch', models.CharField(max_length=100)),
                ('transaction_type', models.CharField(max_length=100)),
                ('payroll', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='zohoapp.payroll')),
            ],
        ),
    ]
