from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.models import User
from .models import UserProfile
from .forms import UserProfileForm, ProfileEditForm, UserEditForm
from django.contrib.auth.decorators import login_required
from checkout.models import Order

@login_required
def profile(request):

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')


    return render(request, "profiles/profile.html")


@login_required
def update_profile(request):
    if request.method == 'POST':
        user_form = UserEditForm (instance=request.user,
                                    data=request.POST)
        profile_form = ProfileEditForm (
                                        instance=request.user.userprofile,
                                        data=request.POST,
                                        files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
           
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(
                                    instance=request.user.profile)
    return render (request,
                    'profiles/update_profile.html',
                    {'user_form':user_form, 'profile_form':profile_form})
