# Generated by Django 3.2.7 on 2021-11-27 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customer',
            fields=[
                ('c_id', models.AutoField(max_length=10, primary_key=True, serialize=False)),
                ('c_name', models.CharField(max_length=30)),
                ('c_email', models.EmailField(max_length=254, unique=True)),
                ('c_phno', models.CharField(max_length=13)),
                ('c_add', models.CharField(max_length=200)),
                ('c_pass', models.CharField(max_length=20)),
                ('otp', models.CharField(max_length=10, null=True)),
                ('otp_used', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'cust',
            },
        ),
    ]
