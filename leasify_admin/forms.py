from leasify_admin.models import house_details, owner, area
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


