from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Training

# Create your views here.
def view_bag(request):
    """A View that renders the bag contents page"""
    return render(request, "bag/bag.html")


def add_to_bag(request, item_id):

    product = get_object_or_404(Training, pk=item_id)
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    request.session['bag'] = bag
    return redirect(redirect_url)
