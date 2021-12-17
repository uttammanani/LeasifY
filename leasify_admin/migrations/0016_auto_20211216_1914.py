# Generated by Django 3.2.7 on 2021-12-16 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leasify_admin', '0015_feedback_notification'),
    ]

    operations = [
        migrations.CreateModel(
            name='admin',
            fields=[
                ('admin_id', models.AutoField(primary_key=True, serialize=False)),
                ('admin_name', models.CharField(max_length=30)),
                ('admin_email', models.EmailField(max_length=254, unique=True)),
                ('admin_pass', models.CharField(max_length=20)),
                ('otp', models.CharField(max_length=10, null=True)),
                ('otp_used', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='customer',
            name='is_admin',
        ),
        migrations.RemoveField(
            model_name='owner',
            name='is_admin',
        ),
    ]
