from django.urls import path
from . import views

from django.conf.urls import include
from django.urls import path
from profiles.views import update_profile

urlpatterns = [
    path('', views.profile, name='profile'),
    path('profile/update/', views.update_profile, name='update_profile'),
]