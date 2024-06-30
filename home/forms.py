from django import forms



class SignupForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    mobile= forms.IntegerField()
    password = forms.CharField()


class LoginForm(forms.Form):
    mobile = forms.CharField()
    password = forms.CharField()