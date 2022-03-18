from django.forms import ModelForm, TextInput
from .models import *


class CreateUsersForm(ModelForm):
    class Meta:
        model = CreatedUsers
        fields = ['username', 'groups']

        widgets = {
            'username': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'username'
            }),
        }


class CreateGroupForm(ModelForm):
    class Meta:
        model = CreatedGroup
        fields = ['group']

        widgets = {
            'group': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'group_name'
            })
        }
