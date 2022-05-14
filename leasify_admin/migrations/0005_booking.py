# Generated by Django 4.0.2 on 2022-05-08 12:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leasify_admin', '0004_remove_customer_c_is_admin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('bk_id', models.AutoField(primary_key=True, serialize=False)),
                ('bk_date', models.DateField()),
                ('h_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leasify_admin.house_details')),
                ('pg_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leasify_admin.pg_details')),
                ('tiff_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leasify_admin.tiffin_details')),
            ],
            options={
                'db_table': 'booking',
            },
        ),
    ]