from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile, Booking, PostModel


class UserSignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        widgets = {
            'username'  : forms.TextInput(attrs={'class':'form-control col-2'}),
            'first_name'  : forms.TextInput(attrs={'class':'form-control col-2'}),
            'last_name'  : forms.TextInput(attrs={'class':'form-control col-2'}),
            'email'  : forms.TextInput(attrs={'class':'form-control col-2'}),
        }


class ProfileCreationForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ['profile_img', 'bg_img', 'name', 'desc',]


class BookingForm(forms.ModelForm):

    class Meta:
        model = Booking
        fields = ['booker_address', 'extra_members', 'booker_mobile', 'booking_occasion', 'booking_date', 'booking_time']


class PostForm(forms.ModelForm):

    class Meta:
        model = PostModel
        fields = ['post_img', 'post_caption', 'post_hashtags']