from django.contrib.gis import forms

from django.contrib.auth.models import User
from .models import UserProfile


class UpdateProfileForm(forms.ModelForm):
    home_address = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone_number = forms.CharField(max_length=15, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    location = forms.PointField(widget=forms.OSMWidget(attrs={'map_width': 800, 'map_height': 500}))

    class Meta:
        model = UserProfile
        fields = ['home_address', 'phone_number']
