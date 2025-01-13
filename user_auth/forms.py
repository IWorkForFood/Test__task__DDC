from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Ваш логин'}),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder":"Ваш пароль"}),
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"placeholder":"Ваш email"}),
    )

class RegistrationForm(LoginForm):
    check_password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder":"Повторите пароль"}),
    )
