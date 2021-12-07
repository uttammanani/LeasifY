# Generated by Django 3.2.7 on 2021-12-05 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leasify_admin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='c_gender',
            field=models.CharField(default=-1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='is_admin',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterModelTable(
            name='customer',
            table='customer',
        ),
    ]