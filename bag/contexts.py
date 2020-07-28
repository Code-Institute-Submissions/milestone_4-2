from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Training

def bag_contents(request):

    bag = request.session.get('bag', {})

    bag_items = []
    total = 0    

    for item_id, item_data in bag.items():
        product = get_object_or_404(Training, pk=item_id)
        total = product.price
        bag_items.append({
            'item_id': item_id,
            'product': product,
        })

    context = {
        'bag_items': bag_items,
        'total': total,
    }

    return context

    