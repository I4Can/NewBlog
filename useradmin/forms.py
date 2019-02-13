from django import forms
from useradmin.models import UserInfo

class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ['avatar', 'nickname', 'gender', 'presentation']
        widgets = {
            'nickname': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'presentation': forms.TextInput(attrs={'class': 'form-control'})
        }


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=64)
    password = forms.PasswordInput()
