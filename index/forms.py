from django import forms
from .models import *

class AboutForm(forms.ModelForm):
    class Meta:
        model = About_coching
        fields = "__all__"

    def __init__(self, *args,**kwargs):
        super(AboutForm,self).__init__(*args,**kwargs)
        self.fields['title'].widget = forms.TextInput(attrs={'class':'form-control'})
        self.fields['description'].widget = forms.Textarea(attrs={'class':'form-control'})

class registrationForm(forms.ModelForm):
    class Meta:
        model = studentRegistration
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(registrationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget = forms.TextInput(attrs={'class': 'name98', 'placeholder': 'First Name'})
        self.fields['last_name'].widget = forms.TextInput(attrs={'class': 'lname178', 'placeholder': 'Last Name'})
        self.fields['email'].widget = forms.EmailInput(attrs={'class': 'email198', 'placeholder': 'Enter your Email'})
        self.fields['mobile_number'].widget = forms.TextInput(attrs={'class': 'mobilenum73', 'placeholder': 'Mobile Number'})






