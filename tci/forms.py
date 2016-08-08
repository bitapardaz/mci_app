from django import forms


class PhoneForm(forms.Form):
    tel_no = forms.CharField(label='tel_no', max_length=20)


class PaymentForm(forms.Form):
    pan = forms.CharField(label='pan', max_length=20)
    pin = forms.CharField(label='pin', max_length=20)
