from django.db import models

# Create your models here.

#This The Customer Model
class customer(models.Model):
    c_id = models.AutoField(primary_key=True)
    c_name= models.CharField(max_length=30)
    c_email= models.EmailField(unique=True)
    c_phno= models.CharField(max_length=13)
    c_add= models.CharField(max_length=200)
    c_pass=models.CharField(max_length=20)
    otp=models.CharField(max_length=10,null=True)
    otp_used=models.IntegerField(default=0)
    is_admin=models.IntegerField(null=True)
    c_gender=models.CharField(max_length=10)

    class Meta:
        db_table="customer"


#This Is House/PG Owner Model.
class owner(models.Model):
    o_id = models.AutoField(primary_key=True)
    o_type=models.CharField(max_length=30)
    o_name = models.CharField(max_length=30)
    o_email = models.EmailField(unique=True)
    o_phno = models.CharField(max_length=13)
    o_add = models.CharField(max_length=200)
    o_pass = models.CharField(max_length=20)
    otp = models.CharField(max_length=10, null=True)
    otp_used = models.IntegerField(default=0)
    is_admin = models.IntegerField(null=True)
    o_gender = models.CharField(max_length=10)

    class Meta:
        db_table="owner"


#This Is Area Table.
class area(models.Model):
    a_id=models.AutoField(primary_key=True)
    a_name=models.CharField(max_length=40)

    class Meta:
        db_table="Area"

#This is House Details Model.
class house_details(models.Model):
    o_id= models.ForeignKey(owner,on_delete=models.CASCADE)
    a_id=models.ForeignKey(area,on_delete=models.CASCADE)
    h_id=models.AutoField(primary_key=True)
    h_add = models.CharField(max_length=200)
    h_imgpath=models.CharField(max_length=200)
    h_name=models.CharField(max_length=100)
    h_rent=models.IntegerField()
    h_desc=models.CharField(max_length=300)
    h_type=models.CharField(max_length=100)
    h_parking=models.CharField(max_length=10)
    h_lift=models.CharField(max_length=100)

    class Meta:
        db_table="House_Details"


#This is House Gallery Model
class house_gallery(models.Model):
    h_id=models.ForeignKey(house_details,on_delete=models.CASCADE)
    gallery_id=models.AutoField(primary_key=True)
    hg_imgpath=models.CharField(max_length=200)

    class Meta:
        db_table="House_Gallery"

#This is PG Details Model
class pg_details(models.Model):
    o_id = models.ForeignKey(owner, on_delete=models.CASCADE)
    a_id = models.ForeignKey(area, on_delete=models.CASCADE)
    pg_id = models.AutoField(primary_key=True)
    pg_add = models.CharField(max_length=200)
    pg_imgpath = models.CharField(max_length=200)
    pg_name = models.CharField(max_length=100)
    pg_rent = models.IntegerField()
    pg_desc = models.CharField(max_length=300)
    pg_beds=models.IntegerField()
    pg_for=models.CharField(max_length=10)
    pg_food=models.CharField(max_length=10)
    pg_wifi=models.CharField(max_length=10)
    pg_tv=models.CharField(max_length=10)

    class Meta:
        db_table="PG_details"

#This is PG Gallery Model
class pg_gallery(models.Model):
    pg_id=models.ForeignKey(pg_details,on_delete=models.CASCADE)
    pg_gallery_id=models.AutoField(primary_key=True)
    pgg_imgpath=models.CharField(max_length=200)

    class Meta:
        db_table="PG_Gallery"

#This Is Tiffin Owner Model.
class tiffin_owner(models.Model):
    to_id = models.AutoField(primary_key=True)
    to_name = models.CharField(max_length=30)
    to_email = models.EmailField(unique=True)
    to_phno = models.CharField(max_length=13)
    to_add = models.CharField(max_length=200)
    to_pass = models.CharField(max_length=20)
    otp = models.CharField(max_length=10, null=True)
    otp_used = models.IntegerField(default=0)
    to_gender = models.CharField(max_length=10)

    class Meta:
        db_table="Tiffin_Owner"

#This Is Tiffin Details Model...
class tiffin_details(models.Model):
    to_id=models.ForeignKey(tiffin_owner,on_delete=models.CASCADE)
    tiff_id = models.AutoField(primary_key=True)
    tiff_title=models.CharField(max_length=100)
    tiff_type=models.CharField(max_length=30)
    tiff_desc=models.CharField(max_length=300)
    tiff_imgpath=models.CharField(max_length=200)
    tiff_price=models.IntegerField(max_length=10)

    class Meta:
        db_table="Tiffn_Details"

#This Is Status Model.
class status(models.Model):
    o_id=models.ForeignKey(owner,on_delete=models.CASCADE)
    h_id=models.ForeignKey(house_details,on_delete=models.CASCADE)
    pg_id=models.ForeignKey(pg_details,on_delete=models.CASCADE)
    to_id = models.ForeignKey(tiffin_owner, on_delete=models.CASCADE)
    tiff_id=models.ForeignKey(tiffin_details, on_delete=models.CASCADE)
    st_id=models.AutoField(primary_key=True)
    st_desc=models.CharField(max_length=50)

    class Meta:
        db_table="Status"

#This Is Notification Model.
class notification(models.Model):
    st_id=models.ForeignKey(status,on_delete=models.CASCADE)
    noti_id=models.AutoField(primary_key=True)
    noti_desc=models.CharField(max_length=300)
    noti_date=models.DateField()

    class Meta:
        db_table="Notification"

#This Is Feedback Model.
class feedback(models.Model):
    h_id = models.ForeignKey(house_details, on_delete=models.CASCADE)
    pg_id = models.ForeignKey(pg_details, on_delete=models.CASCADE)
    tiff_id = models.ForeignKey(tiffin_details, on_delete=models.CASCADE)
    c_id=models.ForeignKey(customer, on_delete=models.CASCADE)
    feed_id = models.AutoField(primary_key=True)
    feed_date=models.DateField()
    feed_desc=models.CharField(max_length=300)

    class Meta:
        db_table="Feedback"









