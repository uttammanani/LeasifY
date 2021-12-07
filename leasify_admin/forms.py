from leasify_admin.models import customer
from django import forms

class custform(forms.ModelForm):
    class Meta:
        model=customer
        fields=["c_name","c_email","c_phno","c_add"]