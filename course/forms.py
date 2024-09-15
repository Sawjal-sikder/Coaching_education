from django import forms
from .models import RegistrationCourse


class registrationForm(forms.ModelForm):
    class Meta:
        model = RegistrationCourse
        fields = ['first_name', 'last_name', 'email', 'phone', 'course']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Customize form fields here
        self.fields['first_name'].widget.attrs.update({
            'class': 'form-control',  # Add Bootstrap class for styling
            'placeholder': 'Enter your first name'
        })
        self.fields['last_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter your last name'
        })
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter your email address'
        })
        self.fields['phone'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter your phone number'
        })
        self.fields['course'].widget.attrs.update({
            'class': 'form-control'
        })

        # Optionally, you can set labels or help texts
        self.fields['first_name'].label = 'First Name'
        self.fields['last_name'].label = 'Last Name'
        self.fields['email'].label = 'Email Address'
        self.fields['phone'].label = 'Phone Number'
        self.fields['course'].label = 'Select a Course'
