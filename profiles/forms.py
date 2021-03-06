from django import forms
from .models import UserProfile
from django.contrib.auth.models import User


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
            'user_name': 'Username',
            'email': 'Email',
        }

        self.fields['user_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0 profile-form-input'
            self.fields[field].label = False


class UserEditForm (forms.ModelForm):
    class Meta:
        model = User
        fields = ('email',)


class ProfileEditForm (forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('username',)
