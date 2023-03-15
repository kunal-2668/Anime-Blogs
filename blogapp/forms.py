from.models import Blog
from django import forms
from django.forms.widgets import TextInput,EmailInput,Textarea



class Addblog(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'

        widgets = {
            'Title' : TextInput(attrs={'placeholder' : 'Enter Title'}),
            'Your_Name' : TextInput(attrs={'id':'username','type':'hidden'})
        }


