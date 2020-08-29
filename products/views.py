from django.shortcuts import render
from .models import Training


# Create your views here.
def all_products(request):
    """ A view to show products """

    products = Training.objects.all().order_by('pk')

    context = {
        'products': products,
    }
    return render(request, "products/products.html", context)
