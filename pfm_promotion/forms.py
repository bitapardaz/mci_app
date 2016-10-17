from django import forms

class MobileForm(forms.Form):
    mobile_no = forms.CharField(max_length=100)
