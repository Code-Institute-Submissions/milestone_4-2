from django import forms
from .models import Order

class PaymentForm(forms.Form):
    class Meta:
        model = Order
        fields = ('full_name', 'email',)

    def __init__(self, *args, **kwargs):
        """
        Form customisation from Code Institute BoutiqueAdo project,
        with some modifications.
        
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False