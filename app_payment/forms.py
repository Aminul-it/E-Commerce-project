from django import forms
from app_payment.models import Billingaddress
class BillingForm(forms.ModelForm):
    class Meta:
        model = Billingaddress
        fields = ['address','zipcode','city','country']
        
