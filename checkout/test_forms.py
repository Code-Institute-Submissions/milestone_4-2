from django.test import TestCase
from .forms import MakePaymentForm, OrderForm
from .models import Order


class TestMakePaymentForm(TestCase):
    def test_make_payment_form(self):
        form = MakePaymentForm({'credit_card_number': '', 'cvv': ''})
        self.assertFalse(form.is_valid())


class TestOrderForm(TestCase):
    def test_order_form(self):
        form = OrderForm({'user': 'Jsmith', 'first_name': 'John', 
                            'last_name': 'Smith',
                            'email': 'test@test.com'})
        self.assertFalse(form.is_valid())
