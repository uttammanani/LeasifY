from leasify_admin.models import house_details
from django import forms

class house_details_form(forms.ModelForm):
    class Meta:
        model=house_details
        fields=["h_add"]