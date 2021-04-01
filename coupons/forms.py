from .models import PurchasedCoupons
from django import forms

class NewPurchasedCoupons(forms.ModelForm):
	class Meta:
		model = PurchasedCoupons
		fields = ['coupon', 'unique_code', 'owner']
