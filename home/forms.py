from django import forms
from .models import Image
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = '__all__' # Include all fields from the image model.
        labels = {"photo": ""} # Custom Lable for the photo field.
        
        # Customizing the widgets for better UI.
        widgets = {
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control'}), 
            'title': forms.TextInput(attrs={'class': 'form-control'}),
        }

class SignUpForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput, label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = User
        fields = ['email', 'username']

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 != password2:
            raise forms.ValidationError("Passwords do not match!")

        return cleaned_data
    