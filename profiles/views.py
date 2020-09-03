from django.shortcuts import render
from django.contrib import messages
from .forms import UserProfileForm
from django.contrib.auth.decorators import login_required



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
        return render(request,
                  'profiles/update_profile.html')
