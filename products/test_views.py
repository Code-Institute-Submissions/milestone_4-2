from django.test import TestCase
from .models import Training

class TestProductViews(TestCase):

    def test_get_product_page(self):
        page = self.client.get("/products/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed('products.html')