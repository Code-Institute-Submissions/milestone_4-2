from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path('<pk>', views.checkout, name='checkout'),

    path('wh/', webhook, name='webhook'),
]