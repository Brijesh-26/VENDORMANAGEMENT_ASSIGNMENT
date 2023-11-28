from django import forms
from .models import Vendor, Purchase

class VendorForm(forms.ModelForm):
    on_time_delivery_rate = forms.FloatField(initial=0.0, required=False)
    quality_rating_avg = forms.FloatField(initial=0.0, required=False)
    average_response_time = forms.FloatField(initial=0.0, required=False)
    fulfillment_rate = forms.FloatField(initial=0.0, required=False)
    class Meta:
        model = Vendor
        fields = '__all__' 
        
        
class PurchaseForm(forms.ModelForm):
    delivery_date = forms.DateTimeField(initial=None, required=False)
    quality_rating = forms.FloatField(initial=0.0)
    # issue_date = forms.DateTimeField(initial=None, required=False)
    acknowledgment_date = forms.DateTimeField(initial=None, required=False)
    status= forms.CharField(initial= "Pending", required= True)
    class Meta:
        model = Purchase
        fields = '__all__'