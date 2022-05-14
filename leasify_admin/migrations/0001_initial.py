# Generated by Django 4.0.2 on 2022-05-08 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
            options={
                'db_table': 'admin',
            },
        ),
        migrations.CreateModel(
            name='area',
            fields=[
                ('a_id', models.AutoField(primary_key=True, serialize=False)),
                ('a_name', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'Area',
            },
        ),
        migrations.CreateModel(
            name='customer',
            fields=[
                ('c_id', models.AutoField(primary_key=True, serialize=False)),
                ('c_name', models.CharField(max_length=30)),
                ('c_email', models.EmailField(max_length=254, unique=True)),
                ('c_phno', models.CharField(max_length=13)),
                ('c_add', models.CharField(max_length=200)),
                ('c_pass', models.CharField(max_length=20)),
                ('otp', models.CharField(max_length=10, null=True)),
                ('otp_used', models.IntegerField(default=0)),
                ('c_gender', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'customer',
            },
        ),
        migrations.CreateModel(
            name='house_details',
            fields=[
                ('h_id', models.AutoField(primary_key=True, serialize=False)),
                ('h_add', models.CharField(max_length=200)),
                ('h_imgpath', models.CharField(max_length=200)),
                ('h_name', models.CharField(max_length=100)),
                ('h_rent', models.IntegerField()),
                ('h_desc', models.CharField(max_length=300)),
                ('h_type', models.CharField(max_length=100)),
                ('h_parking', models.CharField(max_length=10)),
                ('h_lift', models.CharField(max_length=100)),
                ('a_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leasify_admin.area')),
            ],
            options={
                'db_table': 'House_Details',
            },
        ),
        migrations.CreateModel(
            name='owner',
            fields=[
                ('o_id', models.AutoField(primary_key=True, serialize=False)),
                ('o_type', models.CharField(max_length=30)),
                ('o_name', models.CharField(max_length=30)),
                ('o_email', models.EmailField(max_length=254, unique=True)),
                ('o_phno', models.CharField(max_length=13)),
                ('o_add', models.CharField(max_length=200)),
                ('o_pass', models.CharField(max_length=20)),
                ('otp', models.CharField(max_length=10, null=True)),
                ('otp_used', models.IntegerField(default=0)),
                ('o_gender', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'owner',
            },
        ),
        migrations.CreateModel(
            name='pg_details',
            fields=[
                ('pg_id', models.AutoField(primary_key=True, serialize=False)),
                ('pg_add', models.CharField(max_length=200)),
                ('pg_imgpath', models.CharField(max_length=200)),
                ('pg_name', models.CharField(max_length=100)),
                ('pg_rent', models.IntegerField()),
                ('pg_desc', models.CharField(max_length=300)),
                ('pg_beds', models.IntegerField()),
                ('pg_for', models.CharField(max_length=10)),
                ('pg_food', models.CharField(max_length=10)),
                ('pg_wifi', models.CharField(max_length=10)),
                ('pg_tv', models.CharField(max_length=10)),
                ('a_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leasify_admin.area')),
                ('o_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leasify_admin.owner')),
            ],
            options={
                'db_table': 'PG_details',
            },
        ),
        migrations.CreateModel(
            name='tiffin_owner',
            fields=[
                ('to_id', models.AutoField(primary_key=True, serialize=False)),
                ('to_name', models.CharField(max_length=30)),
                ('to_email', models.EmailField(max_length=254, unique=True)),
                ('to_phno', models.CharField(max_length=13)),
                ('to_add', models.CharField(max_length=200)),
                ('to_pass', models.CharField(max_length=20)),
                ('otp', models.CharField(max_length=10, null=True)),
                ('otp_used', models.IntegerField(default=0)),
                ('to_gender', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'Tiffin_Owner',
            },
        ),
        migrations.CreateModel(
            name='tiffin_details',
            fields=[
                ('tiff_id', models.AutoField(primary_key=True, serialize=False)),
                ('tiff_title', models.CharField(max_length=100)),
                ('tiff_type', models.CharField(max_length=30)),
                ('tiff_desc', models.CharField(max_length=300)),
                ('tiff_imgpath', models.CharField(max_length=200)),
                ('tiff_price', models.IntegerField()),
                ('to_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leasify_admin.tiffin_owner')),
            ],
            options={
                'db_table': 'Tiffn_Details',
            },
        ),
        migrations.CreateModel(
            name='status',
            fields=[
                ('st_id', models.AutoField(primary_key=True, serialize=False)),
                ('st_desc', models.CharField(max_length=50)),
                ('h_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leasify_admin.house_details')),
                ('o_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leasify_admin.owner')),
                ('pg_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leasify_admin.pg_details')),
                ('tiff_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leasify_admin.tiffin_details')),
                ('to_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leasify_admin.tiffin_owner')),
            ],
            options={
                'db_table': 'Status',
            },
        ),
        migrations.CreateModel(
            name='pg_gallery',
            fields=[
                ('pg_gallery_id', models.AutoField(primary_key=True, serialize=False)),
                ('pgg_imgpath', models.CharField(max_length=200)),
                ('pg_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leasify_admin.pg_details')),
            ],
            options={
                'db_table': 'PG_Gallery',
            },
        ),
        migrations.CreateModel(
            name='notification',
            fields=[
                ('noti_id', models.AutoField(primary_key=True, serialize=False)),
                ('noti_desc', models.CharField(max_length=300)),
                ('noti_date', models.DateField()),
                ('st_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leasify_admin.status')),
            ],
            options={
                'db_table': 'Notification',
            },
        ),
        migrations.CreateModel(
            name='house_gallery',
            fields=[
                ('gallery_id', models.AutoField(primary_key=True, serialize=False)),
                ('hg_imgpath', models.CharField(max_length=200)),
                ('h_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leasify_admin.house_details')),
            ],
            options={
                'db_table': 'House_Gallery',
            },
        ),
        migrations.AddField(
            model_name='house_details',
            name='o_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leasify_admin.owner'),
        ),
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('feed_id', models.AutoField(primary_key=True, serialize=False)),
                ('feed_date', models.DateField()),
                ('feed_desc', models.CharField(max_length=300)),
                ('c_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leasify_admin.customer')),
                ('h_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leasify_admin.house_details')),
                ('pg_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leasify_admin.pg_details')),
                ('tiff_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leasify_admin.tiffin_details')),
            ],
            options={
                'db_table': 'Feedback',
            },
        ),
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
