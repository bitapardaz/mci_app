from django import forms

class PhoneForm(forms.Form):
    tel_no = forms.CharField(label='tel_no', max_length=20)
