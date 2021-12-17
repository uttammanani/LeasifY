from leasify_admin.models import house_details, owner, area, pg_details, tiffin_owner, tiffin_details, house_gallery, \
    pg_gallery
from django import forms

class house_details_form(forms.ModelForm):
    h_imgpath = forms.FileField()
    class Meta:
        model=house_details
        fields=["h_add","h_imgpath","h_name","h_rent","h_type","h_parking","h_lift","h_desc","a_id","o_id"]

class owner_form(forms.ModelForm):
    class Meta:
        model=owner
        fields=["o_type","o_name","o_email","o_phno","o_add","o_gender","o_pass"]

class area_form(forms.ModelForm):
    class Meta:
        model=area
        fields=["a_name"]


class pg_details_form(forms.ModelForm):
    pg_imgpath = forms.FileField()
    class Meta:
        model=pg_details
        fields=["a_id","pg_add","pg_name","pg_desc","pg_rent","pg_beds","pg_for","pg_food","pg_wifi","pg_tv","pg_imgpath","o_id"]

class tiffin_owner_form(forms.ModelForm):
    class Meta:
        model=tiffin_owner
        fields=["to_name","to_email","to_phno","to_add","to_gender","to_pass"]

class tiffin_details_form(forms.ModelForm):
    tiff_imgpath = forms.FileField()
    class Meta:
        model=tiffin_details
        fields=["to_id","tiff_title","tiff_type","tiff_desc","tiff_imgpath","tiff_price"]

class house_gallery_form(forms.ModelForm):
    hg_imgpath = forms.FileField()
    class Meta:
        model=house_gallery
        fields=["h_id","hg_imgpath"]

class pg_gallery_form(forms.ModelForm):
    pgg_imgpath = forms.FileField()
    class Meta:
        model=pg_gallery
        fields=["pg_id","pgg_imgpath"]
