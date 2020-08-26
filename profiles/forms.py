from django import forms
from .models import UserProfile

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, HTML
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.utils.safestring import mark_safe
from django.db.utils import OperationalError
from datetime import date



class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'first_name' : 'First Name',
            'last_name' : 'Last Name',
            'user_name' : 'User Name',
            'email' : 'Email',
        }

        self.fields['first_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0 profile-form-input'
            self.fields[field].label = False

class UserEditForm (forms.ModelForm) :
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileEditForm (forms.ModelForm) :
    class Meta:
        model = UserProfile
        fields = ('username',)