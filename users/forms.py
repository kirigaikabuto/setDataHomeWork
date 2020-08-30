from django import forms
from .models import UserProfile


class UserProfileCreationForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude =('user',)
        fields = ('phone', 'avatar',)