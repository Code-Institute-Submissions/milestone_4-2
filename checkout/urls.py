from django.urls import path
from . import views

urlpatterns = [
    path('<pk>', views.checkout, name='checkout'),
]