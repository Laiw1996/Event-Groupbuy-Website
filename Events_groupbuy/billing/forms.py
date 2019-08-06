from django import forms

from .models import BillingProfile


class AddressForm(forms.ModelForm):
    class Meta:
        model = BillingProfile
        fields = [
            'email',
            'address_line_1',
            'address_line_2',
            'city',
            'country',
            'state',
            'postal_code'
        ]