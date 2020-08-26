from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.models import User
from .models import UserProfile
from .forms import UserProfileForm, UserUpdateForm
from django.contrib.auth.decorators import login_required
from checkout.models import Order

def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')

    form = UserProfileForm(instance=profile)

    return render(request, "profiles/profile.html")

@login_required
def update_profile(request):
    """Update profile page"""
    orig = UserProfile.objects.get(user=request.user)
    profile_form = UserProfileForm(instance=request.user.userprofile)

    if request.method == "POST":
        if 'cancel' in request.POST:
            return render(request, 'profiles/profile.html')
        profile_form = UserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return render(request, 'profiles/profile.html')
        else:
            initial = request.user.profile
            profile_form = UserProfileForm(request.POST, request.FILES, instance=initial)

    return render(request, "profile_update.html", {'profile_form': profile_form})

