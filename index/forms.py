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