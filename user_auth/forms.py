from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Ваш логин'}),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder":"Ваш пароль"}),
    )

class RegistrationForm(LoginForm):
    check_password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder":"Повторите пароль"}),
    )
